#!/usr/bin/env python3
"""Apply the reviewed decisions of phynics/cast-iron#461 to a corpus.

    python3 scripts/membership-apply.py <corpus-dir> [--queue scripts/membership-queue-461.tsv]
        [--dry-run | --check] [--only-kind racial_trait] [--convert-body]

It reads the queue (`scripts/membership-queue-461.tsv`, kept by `scripts/membership-queue-461.py`
from the output of `scripts/membership-screen.py`) and acts only on the rows whose `verdict`
column is `remove` or `cite` (the print check is recorded there: `print_page`, `evidence`). Rows
marked `keep`, `expands` or `resolved` and rows without a verdict are never touched. Two actions:

`cite` (the book prints the entry and the membership stays)
  The entry gets a `[[sources]]` row for the book with `print_page`, which is what the
  `corpus-check` warning asks for. The book must be in `source_ids` (adding a book is the `add`
  action of `scripts/expansion-credits-apply.py`). The row goes where the entry's rows are in
  `source_ids` order. An entry that has the row already is left alone when its page is
  `print_page` ("already"), and refused when the page differs (the `page` action of
  `scripts/expansion-credits-apply.py` changes a page). A row without a page gets the page. A
  book with an `[[expanded_in]]` credit on the entry is refused: a credit is not membership.
  A body `**Source**` line stays as it is. With `--convert-body` the line becomes the row: the
  book's part of the line goes, the rest of the line stays, and a line with nothing left goes
  too. It is refused when the line's page and `print_page` do not overlap or the part cannot be
  read. A `keep` row needs the row to be there already (`--check` lists those that do not).

`remove` (the book does not print the entry)
  For each removal the script

  1. takes the book out of the entry's `source_ids` (order of the rest is kept),
  2. drops the entry's placement in that book from `books.toml` (format 3: from the curated `books/<book>.toml`;
     a derived book has none). The compiler requires every
     placement to be in `source_ids` (docs/corpus-format.md, "corpus-check"). A title-only group
     (no `entry`, no `anchor`) whose children are all removed is dropped as well.

It never deletes a page citation silently. A `[[sources]]` row must name a book in `source_ids`,
and a raw `**source:** Book/N` or `**Sources:** Book pg N` line in the body is the only page
citation for many entries, so a removal that would leave either one behind is refused: the whole
run stops before it writes anything. A `[[sources]]` row may go only when the audit file
(`scripts/membership-citation-audit-461.tsv`, `--audit`) has a row for that (entry, book) with
the same `cited_page` and one of these classes:

  wrong-credit the cited page was read and the book does not print the entry there or anywhere
               (the page prints another entry, usually a sibling variant). The rejected page
               stays in the audit file (`invalidated`).
  family-ref   the cited page prints a related entry (`family`). The script checks that it
               exists, lists the book, cites `related_cite` there (within one page of this
               entry's citation), and that a `variant`, `addon`, `part` or `revision` relation
               joins the two entries (either direction). The page then survives on the related
               entry.

  mention      the book only mentions the entry (owner decision 2026-11-17: a mention is not a
               printing; the membership goes). The row carries `invalidated`, `mention_pages` and
               `mention_kind` (in the maintainer's words, no book text). A queue row with evidence
               `passing-mention-recorded` needs such a row.

The columns and class names follow `scripts/expansion-credits-459.tsv` (#459).

A body source line is never deleted by this script, and it blocks the removal even when a
structured row exists too (checked first): convert it first (to an `expanded_in`
credit once #458 lands, or by keeping the membership if the book prints the entry).

It refuses a row that
  * has a `[[sources]]` row that the audit file does not release, or a body source line, that
    names the book (see above),
  * has `gate = primary` (removing the first book changes the entry's primary book) unless the
    reviewer cleared it: the row names `proposed_primary`, `proposed_status` is `printed` or
    `body` (the reviewer read the page), the book that becomes first is exactly `proposed_primary`,
    and the entry holds a `[[sources]]` row for it whose page is exactly the reviewed `print_page`.
    A gated row with any other value is refused, and so is a queue that also removes that proposed
    book from the same entry (the rows are checked against the files as they are now, then applied
    one after another). Or has tag `hub-keep`, unless its evidence is `hub-link`, `listed-link` or
    `hub-no-evidence` (design (a) of the link-only hubs, owner ruling of 2026-11-24),
  * would leave `source_ids` empty (the last book of an entry is never removed),
  * names a book that is not in the entry's `source_ids`, or an entry that does not exist.
It never edits an `id` and never moves a file. The edit is textual and keeps the canonical form;
run `cargo xtask corpus-fmt --check <dir>` and `cargo xtask corpus-check <dir>` afterwards.

Applying twice is safe: a row whose book is already out of `source_ids` and `books.toml` is
reported as already applied, and so is a `cite` row whose `[[sources]]` row is there.

`--check` writes nothing: it validates every row as a run would and prints how many changes are
pending (a removal whose book is still in `source_ids`, a `cite` whose row is missing, a `keep`
without its row). It exits 1 when any is pending, so it proves that a run has finished.
`--dry-run` is the same without the exit status. Output has ids and book ids only.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import tomllib
from collections import defaultdict
from pathlib import Path


# Owner ruling of 2026-11-24 on #461, design (a): a link-only hub keeps only its home book, so the tag
# `hub-keep` (#94: a hub membership is never a removal) yields to a verdict that names the listed
# entry which carries the book (`hub-link <target>`, `listed-link <target>`) or finds no entry that
# does (`hub-no-evidence <record>`). `scripts/hub-verdicts-461.py` derives them.
HUB_DESIGN_EVIDENCE = ("hub-link", "hub-no-evidence", "listed-link")

PAGE_TEXT = re.compile(r"\d+(?:\s*[-\u2013]\s*\d+)?(?:\s*,\s*\d+(?:\s*[-\u2013]\s*\d+)?)*|inside cover")


def read_cites(path: Path, only_kind: str | None) -> list[dict]:
    """The rows with verdict `cite`: they need a printed page and the evidence for it."""
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    out = []
    for r in rows:
        if r["verdict"] != "cite" or (only_kind and r["kind"] != only_kind):
            continue
        if not PAGE_TEXT.fullmatch(r["print_page"] or ""):
            raise SystemExit(f"refused: {r['entry']} in {r['book']} has verdict cite and print_page {r['print_page']!r}, which is not a page")
        if not r["evidence"]:
            raise SystemExit(f"refused: {r['entry']} in {r['book']} has no evidence recorded")
        out.append(r)
    return out


def read_queue(path: Path, only_kind: str | None) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    out = []
    for r in rows:
        if r["verdict"] != "remove":
            continue
        if only_kind and r["kind"] != only_kind:
            continue
        cleared = (r["gate"] == "primary" and r["proposed_primary"] and r["proposed_primary"] != r["book"]
                   and r["proposed_status"] in ("printed", "body"))
        hub_design = r["evidence"].split(" ")[0] in HUB_DESIGN_EVIDENCE
        if (r["gate"] and not cleared) or (r["tag"] == "hub-keep" and not hub_design):
            raise SystemExit(f"refused: {r['entry']} in {r['book']} is gated or a hub (gate={r['gate']!r}, tag={r['tag']})")
        if not r["print_page"] or not r["evidence"]:
            raise SystemExit(f"refused: {r['entry']} in {r['book']} has no print_page/evidence recorded")
        out.append(r)
    return out


def entry_path(root: Path, eid: str) -> Path:
    if not eid.startswith("ref/"):
        raise SystemExit(f"refused: unexpected entry id {eid}")
    return root / "entries" / (eid[len("ref/"):] + ".md")


SOURCE_IDS = re.compile(r"^source_ids = \[(.*)\]$", re.M)


SOURCE_LINE = re.compile(r"\*\*[Ss]ources?:?\*\*")


def fold(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.replace("\u2019", "'").replace("'", "").lower()).strip()


def has_sources_row(text: str, book: str) -> bool:
    """True when the entry holds a `[[sources]]` row for `book`."""
    lines = text.split("\n")
    return any(line == "[[sources]]" and f'publication = "{book}"' in lines[i + 1:i + 3]
               for i, line in enumerate(lines))


def body_citation(text: str, title: str) -> bool:
    """True when a body source line (`**source:**`, `**Sources:**`) names the book's title.
    It is checked on its own, whatever structured rows the entry also holds: the script never
    deletes a body citation, and an entry that holds one is never changed."""
    body = text.split("+++", 2)[2] if text.startswith("+++") else text
    ft = fold(title)
    return any(SOURCE_LINE.search(line) and ft and
               re.search(r"(?<![a-z0-9])" + re.escape(ft) + r"(?![a-z0-9])", fold(line))
               for line in body.split("\n"))


def drop_sources_row(text: str, book: str) -> str:
    """Delete the `[[sources]]` block of `book` (its header line and the lines up to the next
    blank line or table header)."""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line == "[[sources]]" and f'publication = "{book}"' in lines[i + 1:i + 3]:
            j = i + 1
            while j < len(lines) and lines[j] and not lines[j].startswith("["):
                j += 1
            return "\n".join(lines[:i] + lines[j:])
    return text


def sources_page(text: str, book: str) -> str:
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line == "[[sources]]" and f'publication = "{book}"' in lines[i + 1:i + 3]:
            for l in lines[i + 1:i + 4]:
                m = re.match(r'^page = "([^"]*)"$', l)
                if m:
                    return m.group(1)
    return ""


def spans(page: str) -> list[tuple[int, int]]:
    out = []
    for part in re.split(r"\s*,\s*", page):
        m = re.fullmatch(r"(\d+)(?:\s*[-\u2013]\s*(\d+))?", part.strip())
        if m:
            a = int(m.group(1))
            out.append((a, int(m.group(2) or a)))
    return out


def overlap(p1: str, p2: str) -> bool:
    return any(a <= z2 and a2 <= z for a, z in spans(p1) for a2, z2 in spans(p2))


def read_audit(path: Path | None) -> dict[tuple[str, str], dict]:
    if path is None or not path.is_file():
        return {}
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    out = {}
    for r in rows:
        if r["class"] not in ("wrong-credit", "family-ref", "mention"):
            raise SystemExit(f"refused: audit row {r['entry']} has unknown class {r['class']!r}")
        if not r["print_page"] or not r["evidence"] or not r["read"]:
            raise SystemExit(f"refused: audit row {r['entry']} in {r['book']} has no print_page/read/evidence")
        if r["class"] in ("wrong-credit", "mention") and not r["invalidated"]:
            raise SystemExit(f"refused: audit row {r['entry']} in {r['book']} has no invalidated citation")
        if r["class"] == "mention" and not (r["mention_pages"] and r["mention_kind"]):
            raise SystemExit(f"refused: audit row {r['entry']} in {r['book']} is a mention without mention_pages and mention_kind")
        if r["class"] == "family-ref" and not (r["family"] and r["related_cite"]):
            raise SystemExit(f"refused: audit row {r['entry']} in {r['book']} is a family-ref without family and related_cite")
        out[(r["entry"], r["book"])] = r
    return out


EDGE_KINDS = ("variant", "addon", "part", "revision")


def has_edge(root: Path, a: str, b: str) -> bool:
    for x, y in ((a, b), (b, a)):
        t = entry_path(root, x).read_text(encoding="utf-8")
        fm = t.split("+++", 2)[1]
        for m in re.finditer(r'\{ kind = "([a-z-]+)", target = "([^"]+)"', fm):
            if m.group(1) in EDGE_KINDS and m.group(2) == y:
                return True
    return False


def release_citation(root: Path, entry: str, book: str, text: str, audit: dict) -> None:
    """Refuse unless the audit file releases the entry's `[[sources]]` row for `book`."""
    row = audit.get((entry, book))
    if row is None:
        raise SystemExit(f"refused: {entry} holds a [[sources]] row for {book} and the audit file has no row for it; convert it, never delete it")
    page = sources_page(text, book)
    if row["cited_page"] != page:
        raise SystemExit(f"refused: {entry} audit cited_page {row['cited_page']!r} is not the row's page {page!r}")
    if row["class"] == "family-ref":
        rel = row["family"]
        rp = entry_path(root, rel)
        if not rp.is_file():
            raise SystemExit(f"refused: {entry} audit names no existing related entry")
        rt = rp.read_text(encoding="utf-8")
        ids = re.findall(r'"([^"]*)"', (SOURCE_IDS.search(rt) or [None, ""])[1])
        rpage = sources_page(rt, book)
        if book not in ids or rpage != row["related_cite"] or not overlap(page, rpage):
            raise SystemExit(f"refused: related {rel} does not list {book} at p. {row['related_cite']}")
        if not has_edge(root, entry, rel):
            raise SystemExit(f"refused: no variant/addon/part/revision relation between {entry} and {rel}; add it first")


def edit_entry(path: Path, book: str, title: str, write: bool = True,
               entry: str = "", root: Path | None = None, audit: dict | None = None,
               primary_to: str = "", print_page: str = "") -> str:
    """Remove `book` from `source_ids` of one entry file. Returns 'removed' or 'absent'; refuses
    the last book, any body source line naming the book (checked first, whatever structured rows exist)
    and any `[[sources]]` row the audit file does not release."""
    text = path.read_text(encoding="utf-8")
    m = SOURCE_IDS.search(text)
    if not m:
        raise SystemExit(f"refused: {path.name} has no single-line source_ids")
    ids = re.findall(r'"([^"]*)"', m.group(1))
    if book not in ids:
        return "absent"
    if len(ids) == 1:
        raise SystemExit(f"refused: {book} is the last book of {path}")
    if body_citation(text, title):
        raise SystemExit(f"refused: {path.name} holds a body source line for {book}; convert it, never delete it")
    drop_row = has_sources_row(text, book)
    if drop_row:
        release_citation(root, entry, book, text, audit or {})
    if ids[0] == book and not primary_to:
        raise SystemExit(f"refused: {book} is the first book of {path.name}; the row needs a cleared proposed_primary")
    if primary_to:
        if ids[0] != book or len(ids) < 2 or ids[1] != primary_to:
            raise SystemExit(f"refused: {path.name} would not have {primary_to} as its first book after removing {book}")
        cited = sources_page(text, primary_to)
        if not cited:
            raise SystemExit(f"refused: {path.name} has no page citation for the new first book {primary_to}")
        if cited != print_page:
            raise SystemExit(f"refused: {path.name} cites {primary_to} at p. {cited}, but the reviewed print_page is {print_page!r}")
    ids.remove(book)
    new_line = "source_ids = [" + ", ".join(f'"{i}"' for i in ids) + "]"
    if write:
        new = text[:m.start()] + new_line + text[m.end():]
        if drop_row:
            new = drop_sources_row(new, book)
        path.write_text(new, encoding="utf-8")
    return "removed"



# ------------------------------------------------------------------------------------- cite


def header_end(lines: list[str]) -> int:
    """Index of the line where the front matter's tables end (`[fields]` or the closing `+++`)."""
    for i in range(1, len(lines)):
        if lines[i] in ("[fields]", "+++"):
            return i
    raise SystemExit("refused: front matter does not end")


def source_blocks(lines: list[str], end: int) -> list[tuple[int, int, str]]:
    """(first line, line after the block, publication) of each `[[sources]]` row of the header."""
    out = []
    i = 1
    while i < end:
        if lines[i] == "[[sources]]":
            j = i + 1
            while j < end and lines[j] and not lines[j].startswith("["):
                j += 1
            pub = next((m.group(1) for l in lines[i:j] if (m := re.match(r'^publication = "([^"]*)"$', l))), "")
            out.append((i, j, pub))
            i = j
        else:
            i += 1
    return out


def has_expanded_in(text: str, book: str) -> bool:
    lines = text.split("\n")
    return any(line == "[[expanded_in]]" and f'publication = "{book}"' in lines[i + 1:i + 3]
               for i, line in enumerate(lines[:header_end(lines)]))


BODY_PAGE = re.compile(r"\s*(?:pg\.?|p\.?|page)\s*(\d.*)$", re.I)
SLASH_PAGE = re.compile(r"^(.+?)/(\d[\d\s,\-\u2013]*)$")


def split_segment(seg: str) -> tuple[str, str]:
    """A body citation part (`Book pg. 28`, `Book/28`, `Book`) -> (title, page text or '')."""
    seg = seg.strip()
    m = BODY_PAGE.search(seg)
    if m:
        return seg[:m.start()].strip(), m.group(1).strip().rstrip(".")
    m = SLASH_PAGE.match(seg)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return seg, ""


SERIES_PREFIX = re.compile(r"^(?:pathfinder rpg|pathfinder roleplaying game|prpg) ")


def same_book(seg_title: str, ft: str) -> bool:
    """The segment's title names the book, with or without the series prefix of the old citations
    (`Pathfinder RPG Bestiary`, `PRPG Core Rulebook`). `Bestiary 5` is another book."""
    s = fold(seg_title)
    return s == ft or SERIES_PREFIX.sub("", s) == ft


def convert_body_lines(text: str, title: str, page: str, name: str) -> tuple[str, int]:
    """Take the book's part out of the body `**Source**` lines. Returns the text and the number
    of parts taken out. Refuses a part whose page does not overlap `page`. A line that does not
    name the book exactly (a longer title, another book) is left as it is; the series prefix of the
    old citations (`Pathfinder RPG Bestiary`, `PRPG Core Rulebook`) is not part of the title."""
    start = text.index("+++", 3) + 3 if text.startswith("+++") else 0
    head, body = text[:start], text[start:]
    ft = fold(title)
    out, taken = [], 0
    for line in body.split("\n"):
        m = SOURCE_LINE.match(line)
        if not m:
            out.append(line)
            continue
        rest, tail = line[m.end():].strip(), ""
        if rest.endswith("\\"):
            rest, tail = rest[:-1].rstrip(), "\\"
        keep, found = [], 0
        for seg in re.split(r",\s*(?=[A-Z])", rest):
            seg_title, seg_page = split_segment(seg)
            if not same_book(seg_title, ft):
                keep.append(seg.strip())
                continue
            if seg_page and not overlap(seg_page, page):
                raise SystemExit(f"refused: {name} has a body line for the book at p. {seg_page}, not p. {page}; reconcile it by hand")
            found += 1
        if not found:
            out.append(line)
            continue
        taken += found
        if keep:  # a line with nothing left goes, and its trailing hard break with it
            out.append(line[:m.end()] + " " + ", ".join(keep) + tail)
    return head + "\n".join(out), taken


def cite_entry(path: Path, book: str, title: str, page: str, write: bool = True, convert_body: bool = False) -> str:
    """Give the entry a `[[sources]]` row for `book` at `page`. Returns 'cited' or 'already'."""
    text = path.read_text(encoding="utf-8")
    m = SOURCE_IDS.search(text)
    if not m:
        raise SystemExit(f"refused: {path.name} has no single-line source_ids")
    ids = re.findall(r'"([^"]*)"', m.group(1))
    if book not in ids:
        if has_expanded_in(text, book):
            raise SystemExit(f"refused: {path.name} credits {book} with expanded_in, which is not membership; it cannot be cited")
        raise SystemExit(f"refused: {book} is not in source_ids of {path.name}; add it first")
    lines = text.split("\n")
    end = header_end(lines)
    blocks = source_blocks(lines, end)
    mine = next((b for b in blocks if b[2] == book), None)
    state = "already"
    if mine:
        have = sources_page(text, book)
        if have and have != page:
            raise SystemExit(f"refused: {path.name} cites {book} at p. {have}, not p. {page}; change a page with expansion-credits-apply.py")
        if not have:
            lines.insert(mine[0] + 2 if lines[mine[0] + 1].startswith("publication") else mine[0] + 1, f'page = "{page}"')
            state = "cited"
    else:
        before = [b for b in blocks if b[2] in ids and ids.index(b[2]) < ids.index(book)]
        if before:
            at = before[-1][1]
        elif blocks:
            at = blocks[0][0]
        else:
            at = end - 1 if lines[end - 1] == "" else end
        lines[at:at] = ["[[sources]]", f'publication = "{book}"', f'page = "{page}"']
        state = "cited"
    new = "\n".join(lines)
    if convert_body:
        new, taken = convert_body_lines(new, title, page, path.name)
        if taken:
            state = "cited"
    if write and new != text:
        path.write_text(new, encoding="utf-8")
    return state


# --------------------------------------------------------------------------------- books.toml


HEADER = re.compile(r"^\[\[books((?:\.chapters)(?:\.children)*)?\]\]$")


def parse_books(text: str, name: str = "books.toml") -> list[list[str]]:
    """Split books.toml into blocks: a header line and its lines, up to the blank line.

    The file is canonical, so blocks are separated by exactly one blank line."""
    if "\n\n\n" in text or not text.endswith("\n") or text.endswith("\n\n"):
        raise SystemExit(f"refused: {name} is not in canonical block form; run corpus-fmt first")
    return [b.split("\n") for b in text[:-1].split("\n\n")]


def apply_books(text: str, removals: dict[str, set[str]], name: str = "books.toml") -> tuple[str, dict[str, int], int]:
    """Drop the node of each (book -> entry ids) removal. Returns the new text, counts per book,
    and the number of title-only groups dropped because their children all went."""
    blocks = parse_books(text, name)
    # Walk blocks in order, tracking the current book and a stack of (depth, block index).
    book = None
    stack: list[tuple[int, int]] = []
    children: dict[int, list[int]] = defaultdict(list)
    drop: set[int] = set()
    counts: dict[str, int] = defaultdict(int)
    for idx, blk in enumerate(blocks):
        m = HEADER.match(blk[0])
        if not m:
            continue
        if m.group(1) is None:  # [[books]]
            sm = next((re.match(r'^source = "([^"]*)"$', l) for l in blk if l.startswith("source = ")), None)
            book = sm.group(1) if sm else None
            stack = []
            continue
        depth = 1 + m.group(1).count(".children")
        while stack and stack[-1][0] >= depth:
            stack.pop()
        parent = stack[-1][1] if stack else None
        if parent is not None:
            children[parent].append(idx)
        stack.append((depth, idx))
        em = next((re.match(r'^entry = "([^"]*)"$', l) for l in blk if l.startswith("entry = ")), None)
        if em and book in removals and em.group(1) in removals[book]:
            drop.add(idx)
            counts[book] += 1
    # Dropping a node block that has children would leave the child blocks behind, and TOML would
    # attach them to the previous sibling. Refuse unless every child goes too.
    for idx in sorted(drop):
        if any(k not in drop for k in children.get(idx, [])):
            raise SystemExit(f"refused: a placement of {blocks[idx][0]} in {name} has children; decide it by hand")
    # A title-only group (no `entry`, no `anchor`) whose children all went is dropped as well.
    dropped_groups = 0
    changed = True
    while changed:
        changed = False
        for idx, kids in children.items():
            if idx in drop or not kids or not all(k in drop for k in kids):
                continue
            blk = blocks[idx]
            if any(l.startswith(("entry = ", "anchor = ")) for l in blk):
                continue
            drop.add(idx)
            dropped_groups += 1
            changed = True
    kept = ["\n".join(blk) for idx, blk in enumerate(blocks) if idx not in drop]
    return "\n\n".join(kept) + "\n", dict(counts), dropped_groups


def apply_layout(root: Path, removals: dict[str, set[str]], dry_run: bool) -> tuple[str, dict[str, int], int]:
    """Drop the placements in whichever layout the corpus has: the single `books.toml` of formats 1
    and 2, or the curated `books/<publication-id>.toml` files of format 3. A book that has no file
    is derived from the `[[sources]]` pages, so it holds no placement and there is nothing to drop.
    Returns the layout's name, the nodes dropped per book, and the title-only groups dropped."""
    legacy = root / "books.toml"
    if legacy.is_file():
        new_text, counts, groups = apply_books(legacy.read_text(encoding="utf-8"), removals, "books.toml")
        if not dry_run:
            legacy.write_text(new_text, encoding="utf-8")
        return "books.toml", counts, groups
    counts: dict[str, int] = {}
    groups = 0
    for book in sorted(removals):
        path = root / "books" / f"{book}.toml"
        if not path.is_file():
            continue
        new_text, one, dropped = apply_books(path.read_text(encoding="utf-8"), {book: removals[book]}, f"books/{book}.toml")
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")
        counts.update(one)
        groups += dropped
    return "books/", counts, groups


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--queue", type=Path, default=Path(__file__).with_name("membership-queue-461.tsv"))
    ap.add_argument("--audit", type=Path, default=Path(__file__).with_name("membership-citation-audit-461.tsv"),
                    help="rows that release a [[sources]] row (class invalidated or reference)")
    ap.add_argument("--only-kind", default=None, help="act on one entry kind only, for example racial_trait")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="write nothing; exit 1 when a decision of the queue is still pending")
    ap.add_argument("--convert-body", action="store_true",
                    help="a `cite` also takes the book out of the body `**Source**` lines (the row replaces them)")
    args = ap.parse_args()
    args.dry_run = args.dry_run or args.check

    rows = read_queue(args.queue, args.only_kind)
    cites = read_cites(args.queue, args.only_kind)
    root = args.corpus
    audit = read_audit(args.audit)
    titles = {p["id"]: p["title"] for p in tomllib.loads((root / "publications.toml").read_text(encoding="utf-8"))["publication"]}
    removals: dict[str, set[str]] = defaultdict(set)
    seen = set()
    todo = []
    for r in rows:
        key = (r["book"], r["entry"])
        if key in seen:
            raise SystemExit(f"refused: duplicate row {r['entry']} in {r['book']}")
        seen.add(key)
        if r["book"] not in titles:
            raise SystemExit(f"refused: unknown book {r['book']}")
        path = entry_path(root, r["entry"])
        if not path.is_file():
            raise SystemExit(f"refused: no entry file for {r['entry']}")
        if r["evidence"] == "passing-mention-recorded" and audit.get((r["entry"], r["book"]), {}).get("class") != "mention":
            raise SystemExit(f"refused: {r['entry']} in {r['book']} is a passing mention with no `mention` audit row")
        todo.append((path, r))
    # Rows are checked against the files as they are now and applied one after another, so a queue
    # must not remove the book that another row of the same entry proposes as its new first book.
    wanted = {(r["entry"], r["book"]) for _, r in todo}
    for _, r in todo:
        if r["gate"] and (r["entry"], r["proposed_primary"]) in wanted:
            raise SystemExit(f"refused: {r['entry']} clears {r['book']} -> {r['proposed_primary']}, and the queue also removes {r['proposed_primary']}")
    # Check every row first (a refusal stops the run before anything is written), then write.
    for path, r in todo:
        edit_entry(path, r["book"], titles[r["book"]], write=False, entry=r["entry"], root=root, audit=audit,
                   primary_to=r["proposed_primary"] if r["gate"] else "", print_page=r["print_page"])
    # `cite` rows are checked now too: a refusal of any row, removal or cite, stops the run before
    # the first file is written.
    cite_todo = []
    for r in cites:
        key = (r["book"], r["entry"])
        if key in seen:
            raise SystemExit(f"refused: duplicate row {r['entry']} in {r['book']}")
        seen.add(key)
        if r["book"] not in titles:
            raise SystemExit(f"refused: unknown book {r['book']}")
        path = entry_path(root, r["entry"])
        if not path.is_file():
            raise SystemExit(f"refused: no entry file for {r['entry']}")
        cite_todo.append((path, r))
    for path, r in cite_todo:
        cite_entry(path, r["book"], titles[r["book"]], r["print_page"], write=False, convert_body=args.convert_body)
    # A `keep` row is a decision that the entry's `[[sources]]` row is right, so it must be there.
    # (The first book needs no row: it is the entry's home.)
    unrowed = []
    with open(args.queue, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["verdict"] != "keep" or (args.only_kind and r["kind"] != args.only_kind):
                continue
            path = entry_path(root, r["entry"])
            if not path.is_file():
                raise SystemExit(f"refused: no entry file for {r['entry']}")
            text = path.read_text(encoding="utf-8")
            m = SOURCE_IDS.search(text)
            ids = re.findall(r'"([^"]*)"', m.group(1)) if m else []
            if r["book"] in ids and ids[0] != r["book"] and not has_sources_row(text, r["book"]):
                unrowed.append(r)

    # The book files are checked before anything is written as well.
    planned: dict[str, set[str]] = defaultdict(set)
    for _, r in todo:
        planned[r["book"]].add(r["entry"])
    apply_layout(root, planned, dry_run=True)
    removed = absent = 0
    for path, r in todo:
        state = edit_entry(path, r["book"], titles[r["book"]], write=not args.dry_run, entry=r["entry"], root=root,
                           audit=audit, primary_to=r["proposed_primary"] if r["gate"] else "",
                           print_page=r["print_page"])
        removed += state == "removed"
        absent += state == "absent"
        removals[r["book"]].add(r["entry"])

    layout, counts, groups = apply_layout(root, removals, args.dry_run)
    placed = sum(counts.values())

    cited = cite_already = 0
    for path, r in cite_todo:
        state = cite_entry(path, r["book"], titles[r["book"]], r["print_page"], write=not args.dry_run,
                           convert_body=args.convert_body)
        cited += state == "cited"
        cite_already += state == "already"

    print(f"rows with verdict remove: {len(rows)}")
    print(f"source_ids: removed {removed}, already out {absent}")
    print(f"{layout}: placements dropped {placed}, empty title-only groups dropped {groups}")
    print(f"rows with verdict cite: {len(cites)}")
    print(f"[[sources]] rows: added {cited}, already there {cite_already}")
    print(f"rows with verdict keep and no [[sources]] row: {len(unrowed)}")
    for r in unrowed[:10]:
        print(f"  {r['entry']} in {r['book']}")
    pending = removed + cited + len(unrowed)
    if args.check:
        print(f"pending changes: {pending}")
        return 1 if pending else 0
    if args.dry_run:
        print("dry run: nothing written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
