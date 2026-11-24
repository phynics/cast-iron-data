#!/usr/bin/env python3
"""Apply the reviewed decisions of phynics/cast-iron#459 to a corpus.

    python3 scripts/expansion-credits-apply.py <corpus-dir>
        [--decisions scripts/expansion-credits-459.tsv] [--dry-run]

The decision file has one row per (entry, book). Its `action` column is one of

  remove       the book does not print the entry. The script takes the book out of the entry's
               `source_ids`, drops the entry's `[[sources]]` row for it, and drops the entry's
               placement in that book from `books.toml` (format 3: from the curated
               `books/<book>.toml`; a derived book has none). The compiler requires every placement
               to be in `source_ids`). A removal needs a `class` that says what happens to the
               page the citation held:
                 family-ref    the cited page prints a related entry (the `family` column). The
                               script verifies that the related entry has the book in
                               `source_ids`, cites it at `related_cite` (within one page of this
                               entry's citation), and that a `variant`, `addon`, `part` or
                               `revision` relation ties the two entries. The reference then
                               lives on the related entry.
                 wrong-credit  the book prints neither the entry nor a related entry. The row
                               must carry the invalidated citation in `invalidated`; the
                               decision file is the audit record of it.
                 mention       the book only mentions the entry (owner decision 2026-11-17: a
                               mention is not a printing). The row must carry the invalidated
                               citation, the pages of the mentions (`mention_pages`) and what
                               kind of mention each is (`mention_kind`, in the corpus
                               maintainer's words: no book text is copied).
               Any other class is refused.
  expanded_in  the book expands the entry and the expanding text has no entry of its own.
               The script does what `remove` does, then writes an `[[expanded_in]]` row with
               the book, the page that the removed `[[sources]]` row held (`cited_page`) and,
               when the `via` column is set, that entry id. Two classes:
                 expands         the text sits under an entry that carries the book: `via`
                                 names it and is required
                 expands-no-via  no entry carries the text (for example the favored class
                                 options that a book prints for a race, owner ruling of
                                 2026-11-24 on #461): `via` must be empty and the row has no
                                 `via` key (docs/corpus-format.md allows it)
  page         the book prints the entry on a different page: the `[[sources]]` page becomes
               `print_page`. Nothing else changes.
  add          the book prints the entry and the entry did not list it (class `printed-group`):
               the book is appended to `source_ids` and a `[[sources]]` row with `print_page` is
               added. Its `books.toml` placement is a hand edit, because a placement needs a
               place in the book's tree.

The page that a removed `[[sources]]` row cited stays in the decision file (`cited_page`): the
entry can no longer hold it, because a `[[sources]]` row needs its book in `source_ids`.

Safety rules
  * An `id` is never edited and an entry file is never moved.
  * A removal is refused unless its class is `family-ref`, `wrong-credit` or `mention`, and a `family-ref`
    row is refused unless the related entry, its citation and the relation edge check out.
  * The last book of an entry is never removed.
  * Removing an entry's first book changes its primary book. The row must name the book that
    becomes first in `primary_to`, and the script refuses when it does not match.
  * A placement node that has children is never dropped (it would orphan them).
  * Applying twice is safe: a row that is already applied is reported and left alone.

Run `cargo xtask corpus-fmt <dir>` (canonical form) and `cargo xtask corpus-check <dir>` after.
Output has ids and book ids only.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

SOURCE_IDS = re.compile(r"^source_ids = \[(.*)\]$", re.M)
HEADER = re.compile(r"^\[\[books((?:\.chapters)(?:\.children)*)?\]\]$")


REMOVE_CLASSES = ("family-ref", "wrong-credit", "mention")
EDGE_KINDS = ("variant", "addon", "part", "revision")
EXPAND_CLASSES = ("expands", "expands-no-via")


def read_decisions(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    seen = set()
    for r in rows:
        name = f"{r['entry']} in {r['book']}"
        if r["action"] not in ("remove", "expanded_in", "page", "add"):
            raise SystemExit(f"refused: unknown action {r['action']!r} for {name}")
        key = (r["entry"], r["book"])
        if key in seen:
            raise SystemExit(f"refused: duplicate row {name}")
        seen.add(key)
        if r["action"] == "page" and not r["print_page"]:
            raise SystemExit(f"refused: {name} has action page but no print_page")
        if r["action"] != "page" and not r["evidence"]:
            raise SystemExit(f"refused: {name} has no evidence recorded")
        if r["action"] != "page" and not r["read"]:
            raise SystemExit(f"refused: {name} does not record what was read")
        if r["action"] == "remove":
            if r["class"] not in REMOVE_CLASSES:
                raise SystemExit(f"refused: {name} has class {r['class']!r}; only {', '.join(REMOVE_CLASSES)} may be removed")
            if r["class"] == "family-ref" and not (r["family"] and r["related_cite"] and r["print_page"]):
                raise SystemExit(f"refused: {name} is a family-ref without family, related_cite and print_page")
            if r["class"] in ("wrong-credit", "mention") and not r["invalidated"]:
                raise SystemExit(f"refused: {name} is a {r['class']} without the invalidated citation")
            if r["class"] == "mention" and not (r["mention_pages"] and r["mention_kind"]):
                raise SystemExit(f"refused: {name} is a mention without mention_pages and mention_kind")
        if r["action"] == "expanded_in":
            if r["class"] not in EXPAND_CLASSES:
                raise SystemExit(f"refused: {name} needs class {' or '.join(EXPAND_CLASSES)}")
            if r["class"] == "expands" and not r["via"]:
                raise SystemExit(f"refused: {name} needs class expands and a via entry (class expands-no-via writes none)")
            if r["class"] == "expands-no-via" and r["via"]:
                raise SystemExit(f"refused: {name} is class expands-no-via but names a via entry")
        if r["action"] == "add" and (r["class"] != "printed-group" or not r["print_page"]):
            raise SystemExit(f"refused: {name} needs class printed-group and a print_page")
    return rows


def front_matter(root: Path, eid: str) -> dict:
    path = entry_path(root, eid)
    if not path.is_file():
        raise SystemExit(f"refused: no entry file for {eid}")
    text = path.read_text(encoding="utf-8")
    return tomllib.loads(text.split("+++", 2)[1])


def page_range(page: str) -> tuple[int, int] | None:
    m = re.match(r"^\s*(\d+)\s*(?:[-\u2013]\s*(\d+))?\s*$", page or "")
    if not m:
        return None
    lo = int(m.group(1))
    hi = m.group(2)
    if hi is None:
        return lo, lo
    hi_n = int(hi)
    if hi_n < lo:  # an abbreviated range such as 263-4
        hi_n = int(str(lo)[: len(str(lo)) - len(hi)] + hi)
    return lo, hi_n


def pages_near(a: str, b: str) -> bool:
    ra, rb = page_range(a), page_range(b)
    return bool(ra and rb and ra[0] - 1 <= rb[1] and rb[0] <= ra[1] + 1)


def verify_family(root: Path, r: dict) -> None:
    """A family-ref row stands only if the related entry carries the reference."""
    name = f"{r['entry']} in {r['book']}"
    rel_id = r["family"]
    other = front_matter(root, rel_id)
    if r["book"] not in other.get("source_ids", []):
        raise SystemExit(f"refused: {name}: related entry {rel_id} does not list the book")
    row = next((s for s in other.get("sources", []) if s["publication"] == r["book"]), None)
    if not row or not row.get("page"):
        raise SystemExit(f"refused: {name}: related entry {rel_id} has no cited page for the book")
    if row["page"] != r["related_cite"]:
        raise SystemExit(f"refused: {name}: related entry {rel_id} cites p. {row['page']}, the decision says p. {r['related_cite']}")
    if not pages_near(r["cited_page"], row["page"]):
        raise SystemExit(f"refused: {name}: related entry {rel_id} cites p. {row['page']}, too far from p. {r['cited_page']}")
    mine = front_matter(root, r["entry"])
    edges = [x for x in mine.get("relations", []) if x["target"] == rel_id and x["kind"] in EDGE_KINDS]
    edges += [x for x in other.get("relations", []) if x["target"] == r["entry"] and x["kind"] in EDGE_KINDS]
    if not edges:
        raise SystemExit(f"refused: {name}: no {'/'.join(EDGE_KINDS)} relation between {r['entry']} and {rel_id}")


def entry_path(root: Path, eid: str) -> Path:
    if not eid.startswith("ref/"):
        raise SystemExit(f"refused: unexpected entry id {eid}")
    return root / "entries" / (eid[len("ref/"):] + ".md")


def source_ids(text: str, name: str) -> list[str]:
    m = SOURCE_IDS.search(text)
    if not m:
        raise SystemExit(f"refused: {name} has no single-line source_ids")
    return re.findall(r'"([^"]*)"', m.group(1))


def header_end(lines: list[str]) -> int:
    """Index of the line where the front matter's table section ends (`[fields]` or the closing +++)."""
    for i in range(1, len(lines)):
        if lines[i] == "[fields]" or lines[i] == "+++":
            return i
    raise SystemExit("refused: front matter does not end")


def drop_source_row(lines: list[str], book: str) -> tuple[list[str], str]:
    """Remove the `[[sources]]` block of `book`. Returns the lines and the page it held."""
    out, i, page = [], 0, ""
    end = header_end(lines)
    while i < len(lines):
        if i < end and lines[i] == "[[sources]]":
            j = i + 1
            while j < len(lines) and lines[j] and not lines[j].startswith("["):
                j += 1
            block = lines[i:j]
            if f'publication = "{book}"' in block:
                for l in block:
                    m = re.match(r'^page = "([^"]*)"$', l)
                    if m:
                        page = m.group(1)
                i = j
                continue
        out.append(lines[i])
        i += 1
    return out, page


def edit_entry(root: Path, path: Path, r: dict) -> str:
    """Apply one decision to one entry file. Returns 'applied' or 'already'."""
    text = path.read_text(encoding="utf-8")
    ids = source_ids(text, path.name)
    book, action = r["book"], r["action"]
    lines = text.split("\n")

    if action == "add":
        if book in ids:
            return "already"
        m = SOURCE_IDS.search(text)
        lines = (text[: m.start()] + "source_ids = [" + ", ".join(f'"{i}"' for i in ids + [book]) + "]" + text[m.end():]).split("\n")
        end = header_end(lines)
        at = end - 1 if end > 0 and lines[end - 1] == "" else end
        lines[at:at] = ["[[sources]]", f'publication = "{book}"', f'page = "{r["print_page"]}"']
        path.write_text("\n".join(lines), encoding="utf-8")
        return "applied"

    if action == "page":
        end = header_end(lines)
        for i in range(end):
            if lines[i] == "[[sources]]" and i + 1 < end and lines[i + 1] == f'publication = "{book}"':
                j = i + 2
                if j < end and lines[j].startswith("page = "):
                    if lines[j] == f'page = "{r["print_page"]}"':
                        return "already"
                    lines[j] = f'page = "{r["print_page"]}"'
                    path.write_text("\n".join(lines), encoding="utf-8")
                    return "applied"
                raise SystemExit(f"refused: {r['entry']} has no page to change in {book}")
        raise SystemExit(f"refused: {r['entry']} has no [[sources]] row for {book}")

    if book not in ids:
        if action == "expanded_in" and f'publication = "{book}"' not in text.split("[fields]")[0]:
            raise SystemExit(f"refused: {r['entry']} has neither {book} in source_ids nor an expanded_in row")
        return "already"
    if len(ids) == 1:
        raise SystemExit(f"refused: {book} is the last book of {r['entry']}")
    if action == "remove" and r["class"] == "family-ref":
        verify_family(root, r)
    rest = [i for i in ids if i != book]
    if ids[0] == book and r["primary_to"] != rest[0]:
        raise SystemExit(f"refused: {r['entry']} loses its first book {book}; primary_to must be {rest[0]}")
    if ids[0] != book and r["primary_to"]:
        raise SystemExit(f"refused: {r['entry']} names primary_to but {book} is not its first book")

    m = SOURCE_IDS.search(text)
    lines = (text[: m.start()] + "source_ids = [" + ", ".join(f'"{i}"' for i in rest) + "]" + text[m.end():]).split("\n")
    lines, page = drop_source_row(lines, book)
    if action == "expanded_in":
        block = ["[[expanded_in]]", f'publication = "{book}"']
        if page or r["cited_page"]:
            block.append(f'page = "{page or r["cited_page"]}"')
        if r["via"]:
            block.append(f'via = "{r["via"]}"')
        end = header_end(lines)
        at = end - 1 if end > 0 and lines[end - 1] == "" else end
        lines[at:at] = block
    path.write_text("\n".join(lines), encoding="utf-8")
    return "applied"


def parse_books(text: str, name: str = "books.toml") -> list[list[str]]:
    """Split books.toml into blocks: a header line and its lines, up to the blank line."""
    if "\n\n\n" in text or not text.endswith("\n") or text.endswith("\n\n"):
        raise SystemExit(f"refused: {name} is not in canonical block form; run corpus-fmt first")
    return [b.split("\n") for b in text[:-1].split("\n\n")]


def apply_books(text: str, removals: dict[str, set[str]], name: str = "books.toml") -> tuple[str, dict[str, int], int]:
    """Drop the node of each (book -> entry ids) removal. Returns the new text, the number of
    nodes dropped per book, and the number of title-only groups dropped because all their
    children went."""
    blocks = parse_books(text, name)
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
    for idx in sorted(drop):
        if children.get(idx):
            raise SystemExit(f"refused: a placement of {blocks[idx][0]} in {name} has children; decide it by hand")
    dropped_groups = 0
    changed = True
    while changed:
        changed = False
        for idx, kids in children.items():
            if idx in drop or not kids or not all(k in drop for k in kids):
                continue
            if any(l.startswith(("entry = ", "anchor = ")) for l in blocks[idx]):
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
    ap.add_argument("--decisions", type=Path, default=Path(__file__).with_name("expansion-credits-459.tsv"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    rows = read_decisions(args.decisions)
    root = args.corpus
    tally: dict[str, int] = defaultdict(int)
    removals: dict[str, set[str]] = defaultdict(set)
    for r in rows:
        path = entry_path(root, r["entry"])
        if not path.is_file():
            raise SystemExit(f"refused: no entry file for {r['entry']}")
        if args.dry_run:
            ids = source_ids(path.read_text(encoding="utf-8"), path.name)
            applies = r["action"] == "page" or (r["book"] in ids) == (r["action"] != "add")
            if applies and r["action"] == "remove" and r["class"] == "family-ref":
                verify_family(root, r)
            state = "applied" if applies else "already"
        else:
            state = edit_entry(root, path, r)
        tally[f"{r['action']} {state}"] += 1
        if r["action"] in ("remove", "expanded_in"):
            removals[r["book"]].add(r["entry"])

    layout, counts, groups = apply_layout(root, removals, args.dry_run)
    for k in sorted(tally):
        print(f"{k}: {tally[k]}")
    print(f"{layout}: placements dropped {sum(counts.values())}, empty title-only groups dropped {groups}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
