#!/usr/bin/env python3
"""Add `[[sources]]` citation rows to the entries that have none (phynics/cast-iron-data#170).

    python3 scripts/add-citations.py <corpus-dir> --slice NAME [--slice NAME ...]
        [--books ID,ID,... | --books-range FROM:TO] [--candidates FILE] [--print-pages FILE]
        [--review FILE] [--list-proposal-only] [--sample N] [--seed N] [--write | --check]
    python3 scripts/add-citations.py --self-test

Without `--write` or `--check` the script only surveys: it prints what a write would do and
changes nothing. `--write` edits the entry files and the review queue. `--check` is a survey that
exits 1 when anything is stale (an entry of the slice has no rows, a paragraph a write would
remove is still there, or the review queue lists a row that has a page now). Run
`cargo xtask corpus-fmt <corpus-dir>` after `--write`.

Slices (`--slice`, repeatable):

  paragraphs     class options whose body has `**Sources:** Book pg N` paragraphs. For each
                 paragraph whose citations all resolve: a book with a row that covers the cited
                 page (or a cited book without a page) already agrees, and a member book with no row
                 gets one; then the paragraph is removed. A book whose row has another page, a
                 title that maps to no publication, a blog post and a book outside `source_ids`
                 go to the review queue and the paragraph stays.
  trap, skill, mythic, racial-trait, trait, affliction, class-option
                 the entries of that kind that have no `[[sources]]` row at all (`mythic` is the
                 carried Mythic Adventures feat entries). Each gets one row per `source_ids`
                 book, in `source_ids` order. `--books` limits a slice to the entries whose first
                 `source_ids` book is listed; `--books-range FROM:TO` to the entries whose first
                 book lies between the two ids (inclusive, in id order; FROM must not follow TO).

A row has a `page` when one of these gives it, in this order:

  1. a page read in print (`scripts/citation-print-pages-170.tsv`: entry_id, publication, page,
     basis; committed, one line per page);
  2. for a skill and a trap, the sibling `ref/skill/*` or `ref/trap/*` entry's row for the book;
     it must agree with a confident proposal, else the row is book-only (sibling-differs);
  3. a confident page proposal: one page for that book, and the book is in `source_ids`.

A page that is none of `N`, `N-N` or a comma list of those (any source, print included) makes the
row book-only (page-format). `--list-proposal-only` prints the rows that rest on a proposal alone,
for a reviewer to check in print.

A book that the page reference does not list for the entry (`book-differs`) gets NO row, not even
a book-only one (owner decision of 2026-11-22 on #170): the membership may be wrong, so the #461
warning must keep flagging it until print confirms the book (then it gets a row, for instance from
the print-pages file) or `source_ids` drops it. The review queue keeps a `book-differs` line
for it while the book stays in `source_ids` without a row.

Every other row without a page is book-only and gets a review-queue line that says why (coarse,
ambiguous, no-page, sibling-differs, no-proposal, page-format, unconfirmed). A print-pages line with an
empty page marks a proposal that print was searched for and did not confirm (`unconfirmed`); the row
is book-only and the proposal is kept in the review line only. A page of 0 is no page (page-format). Page proposals come from a
local reference (`--candidates`, the TSV its lookup writes: entry_id, publication, page,
confidence, notes). The reference is not part of the corpus and is not committed, so a rerun
without `--candidates` and with rows in place changes nothing. Each page a write adds still needs
a check against print, on a sample per slice (`--sample`).

The print-pages file may carry a fifth column `note`; a row with a note also gets a
`heading-form` review line (the page is read in print, but the heading does not look as expected).

The review queue (`scripts/citation-review-170.tsv`) holds the books that have a row and no
page, the books with no row (`book-differs`), the paragraphs that stayed and the print notes. A later pass fills in a page and the line goes away on the
next `--write`. The script never edits an `id`, never moves a file, never changes `source_ids`,
and never overwrites an existing row. It is idempotent. `--self-test` runs the script's own
tests on a throwaway corpus.
"""
from __future__ import annotations

import argparse
import csv
import random
import re
import sys
import tomllib
from collections import Counter
from pathlib import Path

REVIEW_DEFAULT = "scripts/citation-review-170.tsv"
PRINT_DEFAULT = "scripts/citation-print-pages-170.tsv"
# Review lines that stay while their entry exists (paragraph findings and print notes).
NOTE_REASONS = {"conflict", "unknown-title", "blog", "not-member", "marker", "heading-form"}
REVIEW_COLUMNS = ["entry_id", "kind", "publication", "reason", "candidate_page", "note"]
SLICES = [
    "paragraphs", "trap", "skill", "mythic", "racial-trait", "trait", "affliction",
    "class-option",
]
KIND_OF_SLICE = {
    "trap": "trap", "skill": "skill", "mythic": "feat", "racial-trait": "racial_trait",
    "trait": "trait", "affliction": "affliction", "class-option": "class_option",
}
MYTHIC_PREFIX = "ref/carried/mythic-adventures/feats/"

PAGE_FORM = re.compile(r"^\d+(?:-\d+)?(?:, \d+(?:-\d+)?)*$")


def page_ok(page: str) -> bool:
    """A page value in a known form whose numbers are all at least 1 (page 0 is no page)."""
    numbers = page_set(page)
    return bool(PAGE_FORM.match(page)) and numbers is not None and 0 not in numbers
SOURCES_LINE = re.compile(r"^\*\*Sources?:\*\*")
TITLE_PREFIX = re.compile(r"^(pathfinder rpg|pathfinder roleplaying game|prpg) ")

# Printed titles that differ from `publications.toml` titles (same table as sources-field.py).
ALIASES = {
    "prpg core rulebook": "core-rulebook",
    "pathfinder rpg bestiary": "bestiary",
    "gamemastery guide": "game-mastery-guide",
    "pathfinder campaign setting": "pathfinder-campaign-setting",
    "tome of horrors complete": "tome-of-horrors-complete-pf",
    "paizo blog - golarion day subdomains": "paizo-blog-golarion-day-subdomains",
}


def norm(text: str) -> str:
    text = text.replace("\\#", "#").replace("’", "'")
    text = re.sub(r"\\(.)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def toml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


# ---------------------------------------------------------------------------- pages


def page_set(page: str) -> set[int] | None:
    """The page numbers a `page` value names, or None when it is not a number list."""
    pages: set[int] = set()
    for part in page.split(","):
        part = part.strip()
        m = re.fullmatch(r"(\d+)(?:-(\d+))?", part)
        if not m:
            return None
        lo = int(m.group(1))
        hi = m.group(2)
        if hi is None:
            pages.add(lo)
            continue
        hi_n = int(hi)
        if hi_n < lo:  # abbreviated range: 263-4
            hi_n = int(str(lo)[: len(str(lo)) - len(hi)] + hi)
        if hi_n < lo:
            return None
        pages.update(range(lo, hi_n + 1))
    return pages


def covers(row_page: str, cited: str) -> bool:
    if row_page == cited:
        return True
    have, want = page_set(row_page), page_set(cited)
    return have is not None and want is not None and want <= have


def join_pages(pages: list[str]) -> str:
    """Merge cited pages into one value: sorted, adjacent single pages joined into a range."""
    numbers: set[int] = set()
    for page in pages:
        got = page_set(page)
        if got is None:
            return ", ".join(dict.fromkeys(pages))
        numbers |= got
    out: list[str] = []
    run = sorted(numbers)
    i = 0
    while i < len(run):
        j = i
        while j + 1 < len(run) and run[j + 1] == run[j] + 1:
            j += 1
        out.append(str(run[i]) if i == j else f"{run[i]}-{run[j]}")
        i = j + 1
    return ", ".join(out)


# ---------------------------------------------------------------------------- entries


class Entry:
    def __init__(self, path: Path, root: Path) -> None:
        self.path = path
        self.relative = path.relative_to(root).as_posix()
        self.text = path.read_text(encoding="utf-8")
        end = self.text.index("\n+++\n", 4)
        self.front = self.text[4:end]
        self.body = self.text[end + 5 :]
        self.data = tomllib.loads(self.front)
        self.id: str = self.data["id"]
        self.kind: str = self.data["kind"]
        self.source_ids: list[str] = self.data.get("source_ids", [])
        self.rows: list[dict] = [dict(r) for r in self.data.get("sources", [])]

    def render(self, rows: list[dict], body: str) -> str:
        lines = self.front.split("\n")
        start = next((i for i, l in enumerate(lines) if l == "[[sources]]"), None)
        if start is None:
            start = next(
                (i for i, l in enumerate(lines) if l in ("[[expanded_in]]", "[fields]")),
                len(lines),
            )
            end = start
        else:
            end = next(
                (i for i in range(start, len(lines))
                 if lines[i].startswith("[") and lines[i] != "[[sources]]"),
                len(lines),
            )
        head = lines[:start]
        while head and head[-1] == "":
            head.pop()
        tail = lines[end:]
        out = head + [""] if head else []
        for row in rows:
            out.append("[[sources]]")
            out.append(f"publication = {toml_string(row['publication'])}")
            if row.get("page"):
                out.append(f"page = {toml_string(row['page'])}")
        if tail:
            if tail[0] == "[fields]":
                out.append("")
            out.extend(tail)
        return "+++\n" + "\n".join(out) + "\n+++\n" + body


def load_entries(root: Path) -> list[Entry]:
    return [Entry(p, root) for p in sorted((root / "entries").rglob("*.md"))]


def load_publications(root: Path) -> tuple[dict[str, str], dict[str, str]]:
    data = tomllib.loads((root / "publications.toml").read_text(encoding="utf-8"))
    titles = {row["id"]: row["title"] for row in data["publication"]}
    by_title = {norm(t).lower(): pid for pid, t in titles.items()}
    by_title.update(ALIASES)
    return titles, by_title


def insert_row(rows: list[dict], row: dict, source_ids: list[str]) -> None:
    """Insert a row before the first existing row whose book comes later in `source_ids`."""
    index = source_ids.index(row["publication"])
    for at, existing in enumerate(rows):
        pub = existing["publication"]
        if pub in source_ids and source_ids.index(pub) > index:
            rows.insert(at, row)
            return
    rows.append(row)


# ---------------------------------------------------------------------------- paragraphs


def parse_citations(text: str, by_title: dict[str, str]) -> tuple[list[tuple[str, str | None]], list[str]]:
    """Parse `Title pg N, Title, Title pg N` into (publication, page) pairs and unmapped names."""
    text = norm(re.sub(r"^\*\*Sources?:\*\*\s*", "", text))
    ordered = sorted(by_title, key=len, reverse=True)
    found: list[tuple[str, str | None]] = []
    unmapped: list[str] = []
    i = 0
    while i < len(text):
        while i < len(text) and text[i] in " ,;":
            i += 1
        if i >= len(text):
            break
        rest = text[i:].lower()
        title = next(
            (t for t in ordered
             if rest.startswith(t)
             and (len(rest) == len(t) or rest[len(t)] in " ,;")),
            None,
        )
        if title is None:
            end = text.find(", ", i)
            end = len(text) if end == -1 else end
            unmapped.append(text[i:end].strip())
            i = end
            continue
        i += len(title)
        m = re.match(r"\s*(?:pg\.?|p\.?|page)\s*(\d+(?:-\d+)?)", text[i:], re.IGNORECASE)
        page = None
        if m:
            page = m.group(1)
            i += m.end()
        found.append((by_title[title], page))
    return found, unmapped


def sources_paragraphs(body_lines: list[str]) -> list[tuple[int, int, bool]]:
    """(first line, last line, ends in a hard break) of each `**Sources:**` citation text.

    The text runs to a line that ends in a backslash (the paragraph goes on after it) or to the
    line before a blank line.
    """
    out = []
    i = 0
    fenced = False
    while i < len(body_lines):
        line = body_lines[i]
        if line.startswith(":::"):
            fenced = line.strip() != ":::"
        if not fenced and SOURCES_LINE.match(line):
            j = i
            hard = False
            while j < len(body_lines) and body_lines[j].strip():
                if body_lines[j].rstrip().endswith("\\"):
                    hard = True
                    break
                j += 1
            last = j if hard else j - 1
            out.append((i, last, hard))
            i = last
        i += 1
    return out


LABEL_LINE = re.compile(r"^\*\*(?:Replaces|Alters):\*\*")


def normal_end(lines: list[str]) -> int:
    """The line where the drift check ends the entry's normal part (see `normal_part` in cast-iron
    `crates/corpus/src/drift.rs`): a `###` heading whose next block is a Sources line, or a
    Sources line after the first one."""
    seen = False
    for i, line in enumerate(lines):
        if SOURCES_LINE.match(line) and (i == 0 or lines[i - 1].strip() == "" or lines[i - 1].startswith("#")):
            if seen:
                return i
            seen = True
        elif re.match(r"^### ", line):
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and SOURCES_LINE.match(lines[j]):
                return i
    return len(lines)


def label_lines(lines: list[str], end: int) -> int:
    return sum(1 for l in lines[:end] if LABEL_LINE.match(l))


def process_paragraphs(entry: Entry, titles: dict[str, str], by_title: dict[str, str]):
    """Plan the change for one class option: (rows, body, review lines, counts)."""
    lines = entry.body.split("\n")
    rows = [dict(r) for r in entry.rows]
    by_pub = {r["publication"]: r for r in rows}
    reviews: list[dict] = []
    counts: Counter[str] = Counter()
    plan = []  # (first, last, hard, [(pub, page)], resolvable)
    added: dict[str, list[str]] = {}
    bookonly_added: set[str] = set()
    for first, last, hard in sources_paragraphs(lines):
        text = " ".join(l.rstrip("\\") for l in lines[first : last + 1])
        cites, unmapped = parse_citations(text, by_title)
        problems: list[tuple[str, str, str]] = []  # (publication, reason, note)
        for name in unmapped:
            if name.lower().startswith("paizo blog"):
                problems.append(("", "blog", name))
            else:
                problems.append(("", "unknown-title", name))
        for pub, page in cites:
            if pub not in entry.source_ids:
                problems.append((pub, "not-member", f"cited {page or 'no page'}"))
            elif pub.startswith("paizo-blog-"):
                problems.append((pub, "blog", f"cited {page or 'no page'}"))
            elif pub in by_pub and by_pub[pub].get("page") and page and not covers(by_pub[pub]["page"], page):
                problems.append((pub, "conflict", f"paragraph {page}, row {by_pub[pub]['page']}"))
        plan.append((first, last, hard, cites, problems))
    # Rows come only from paragraphs that resolve completely.
    for first, last, hard, cites, problems in plan:
        if problems:
            continue
        for pub, page in cites:
            row = by_pub.get(pub)
            if row is not None and (row.get("page") or not page):
                continue  # the row agrees: it covers the cited page (checked above)
            if page:
                added.setdefault(pub, []).append(page)
            elif row is None:
                bookonly_added.add(pub)
    for pub in sorted(set(added) | bookonly_added, key=entry.source_ids.index):
        page = join_pages(added[pub]) if pub in added else None
        if pub in by_pub:
            by_pub[pub]["page"] = page
            counts["row page filled"] += 1
        else:
            row = {"publication": pub}
            if page:
                row["page"] = page
            else:
                reviews.append(review(entry, pub, "no-page", "", "paragraph names the book only"))
            insert_row(rows, row, entry.source_ids)
            by_pub[pub] = row
            counts["row added"] += 1
    keep = [True] * len(lines)
    base_labels = label_lines(lines, normal_end(lines))
    for first, last, hard, cites, problems in plan:
        if problems:
            counts["paragraph kept"] += 1
            for pub, reason, note in problems:
                reviews.append(review(entry, pub, reason, "", note))
            continue
        trial = list(keep)
        for k in range(first, last + 1):
            trial[k] = False
        if not hard and last + 1 < len(lines) and lines[last + 1].strip() == "":
            trial[last + 1] = False
        after = [l for l, k in zip(lines, trial) if k]
        if label_lines(after, normal_end(after)) > base_labels:
            # The drift check ends the normal part at a `###` heading with a Sources line. Taking
            # the line away would put a printed Replaces/Alters line into the normal part.
            counts["paragraph kept (drift marker)"] += 1
            for pub, _page in cites:
                reviews.append(review(entry, pub, "marker", "", "paragraph agrees; it ends the normal part"))
            continue
        counts["paragraph removed"] += 1
        keep = trial
    new_lines = [l for l, k in zip(lines, keep) if k]
    return rows, "\n".join(new_lines), reviews, counts


def review(entry: Entry, publication: str, reason: str, candidate: str, note: str) -> dict:
    return {
        "entry_id": entry.id, "kind": entry.kind, "publication": publication,
        "reason": reason, "candidate_page": candidate, "note": note,
    }


# ---------------------------------------------------------------------------- candidates


def load_candidates(path: Path | None) -> dict[tuple[str, str], dict]:
    if path is None:
        return {}
    out: dict[tuple[str, str], dict] = {}
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            out[(row["entry_id"], row["publication"])] = row
    return out


def sibling_page(entry: Entry, pub: str, by_id: dict[str, Entry]) -> str | None:
    """Skill and trap: the page the sibling `ref/<kind>/<name>` entry gives for the book."""
    if entry.kind not in ("skill", "trap"):
        return None
    name = entry.id.rsplit("/", 1)[-1]
    sib = by_id.get(f"ref/{entry.kind}/{name}")
    if sib is None:
        return None
    for row in sib.rows:
        if row["publication"] == pub and row.get("page"):
            return row["page"]
    return None


BASIS: Counter[str] = Counter()
PRINT: dict[tuple[str, str], str] = {}
PRINT_NOTES: dict[tuple[str, str], str] = {}
PRINT_WITHHELD: dict[tuple[str, str], str] = {}  # print looked and did not confirm the proposal
QUEUED_DIFFERS: set[tuple[str, str]] = set()  # books the review queue already holds as book-differs
PROPOSAL_ONLY: list[tuple[str, str, str]] = []


def decide(entry: Entry, pub: str, cands: dict, by_id: dict[str, Entry]):
    """(page or None, review reason or None, candidate page, note)."""
    cand = cands.get((entry.id, pub))
    sib = sibling_page(entry, pub, by_id)
    cpage = (cand or {}).get("page") or ""
    confident = bool(cand) and cand["confidence"] == "confident" and cpage
    printed = PRINT.get((entry.id, pub))
    if printed:
        # A page read in print beats every proposal.
        if not page_ok(printed):
            return None, "page-format", printed, "the print-pages file gives a page in no known form"
        BASIS["print"] += 1
        if confident and not covers(printed, cpage):
            BASIS["print differs from proposal"] += 1
        return printed, None, "", ""
    if (entry.id, pub) in PRINT_WITHHELD:
        return None, "unconfirmed", cpage, PRINT_WITHHELD[(entry.id, pub)]
    if sib:
        if confident and not covers(sib, cpage) and not covers(cpage, sib):
            BASIS["sibling differs"] += 1
            return None, "sibling-differs", cpage, f"sibling entry gives {sib}"
        BASIS["sibling agrees with proposal" if confident else "sibling only"] += 1
        return sib, None, "", ""
    if cand is None:
        if (entry.id, pub) in QUEUED_DIFFERS:
            # Without the proposals file a rerun must not turn a queued book into a row.
            return None, "book-differs", "", "the reference lists the entry only in other books"
        return None, "no-proposal", "", ""
    if confident:
        if not page_ok(cpage):
            return None, "page-format", cpage, ""
        BASIS["proposal only"] += 1
        PROPOSAL_ONLY.append((entry.id, pub, cpage))
        return cpage, None, "", ""
    notes = cand.get("notes", "")
    if cand["confidence"] == "check":
        return None, "coarse", cpage, "the proposal is a section or parent page"
    if cand["confidence"] == "ambiguous":
        # The proposal lists the pages (`pages=62,306` in its notes): keep them for the reviewer.
        listed = re.search(r"pages=([0-9,]+)", notes)
        return None, "ambiguous", listed.group(1) if listed else cpage, "several pages proposed"
    if "no-aon-source-for-book" in notes:
        return None, "book-differs", "", "the reference lists the entry only in other books"
    return None, "no-page", "", ""


# ---------------------------------------------------------------------------- review file


def read_review(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_review(path: Path, rows: list[dict], order: dict[str, int]) -> None:
    rows = sorted(rows, key=lambda r: (r["kind"], r["entry_id"], order.get(r["publication"], 0), r["publication"], r["reason"], r["note"]))
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(REVIEW_COLUMNS)
        for r in rows:
            w.writerow([r[c] for c in REVIEW_COLUMNS])


# ---------------------------------------------------------------------------- self-test


def self_test() -> int:
    """Run the script on a throwaway corpus and assert the rules that matter."""
    import contextlib
    import io
    import tempfile

    failures: list[str] = []

    def expect(ok: bool, what: str) -> None:
        print(("ok   " if ok else "FAIL ") + what)
        if not ok:
            failures.append(what)

    def run(root: Path, *args: str) -> int:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return main([str(root), *args])

    def rows_of(root: Path, name: str) -> list[tuple[str, str | None]]:
        text = (root / "entries" / "trait" / f"{name}.md").read_text(encoding="utf-8")
        front = tomllib.loads(text[4 : text.index("\n+++\n", 4)])
        return [(r["publication"], r.get("page")) for r in front.get("sources", [])]

    def review_of(root: Path) -> list[tuple[str, str, str]]:
        return [(r["entry_id"], r["publication"], r["reason"]) for r in read_review(root / REVIEW_DEFAULT)]

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "entries" / "trait").mkdir(parents=True)
        (root / "scripts").mkdir()
        (root / "publications.toml").write_text(
            "".join(f'[[publication]]\nid = "{i}"\ntitle = "Book {i.upper()}"\n\n' for i in "abc"),
            encoding="utf-8",
        )

        def entry(name: str, books: list[str]) -> None:
            ids = ", ".join(f'"{b}"' for b in books)
            (root / "entries" / "trait" / f"{name}.md").write_text(
                f'+++\nid = "ref/trait/{name}"\nkind = "trait"\ntitle = "{name.upper()}"\n'
                f"source_ids = [{ids}]\n\n[fields]\nkind = \"none\"\n+++\n\nBody.\n",
                encoding="utf-8",
            )

        def candidates(lines: list[tuple[str, str, str, str, str]]) -> Path:
            path = root / "candidates.tsv"
            with path.open("w", encoding="utf-8", newline="") as f:
                w = csv.writer(f, delimiter="\t", lineterminator="\n")
                w.writerow(["entry_id", "publication", "page", "confidence", "notes"])
                w.writerows(lines)
            return path

        entry("t1", ["a", "b", "c"])
        cand = candidates([
            ("ref/trait/t1", "a", "10", "confident", ""),
            ("ref/trait/t1", "b", "", "none", "no-aon-source-for-book"),
            ("ref/trait/t1", "c", "12", "confident", ""),
        ])
        slice_args = ["--slice", "trait", "--candidates", str(cand)]
        expect(run(root, *slice_args, "--check") == 1, "a survey of an entry without rows is stale")
        expect(run(root, *slice_args, "--write") == 0, "write runs")
        expect(rows_of(root, "t1") == [("a", "10"), ("c", "12")], "book-differs writes no row, not even a book-only one")
        expect(("ref/trait/t1", "b", "book-differs") in review_of(root), "book-differs keeps a review line")
        expect(run(root, *slice_args, "--check") == 0, "a second run changes nothing")

        # A page read in print confirms the book: the row appears in source_ids order.
        (root / PRINT_DEFAULT).write_text(
            "entry_id\tpublication\tpage\tbasis\nref/trait/t1\tb\t7\tprint\n", encoding="utf-8"
        )
        expect(run(root, *slice_args, "--check") == 1, "a print page for a rowless book is stale until written")
        run(root, *slice_args, "--write")
        expect(rows_of(root, "t1") == [("a", "10"), ("b", "7"), ("c", "12")], "print adds the row in source_ids order")
        expect(("ref/trait/t1", "b", "book-differs") not in review_of(root), "the review line goes with the row")
        expect(run(root, *slice_args, "--check") == 0, "stable after the fill")

        # A print line with no page withholds a proposal; page 0 is no page.
        entry("t6", ["a", "b"])
        (root / PRINT_DEFAULT).write_text(
            "entry_id\tpublication\tpage\tbasis\tnote\nref/trait/t6\ta\t\tunconfirmed\tnot on the page\n",
            encoding="utf-8",
        )
        cand6 = candidates([
            ("ref/trait/t6", "a", "8", "confident", ""),
            ("ref/trait/t6", "b", "0", "confident", ""),
        ])
        run(root, "--slice", "trait", "--candidates", str(cand6), "--write")
        expect(rows_of(root, "t6") == [("a", None), ("b", None)], "a withheld proposal and page 0 give book-only rows")
        expect(("ref/trait/t6", "a", "unconfirmed") in review_of(root), "unconfirmed is queued")
        expect(("ref/trait/t6", "b", "page-format") in review_of(root), "page 0 is page-format")

        # An ambiguous proposal keeps its candidate pages in the review line.
        entry("t7", ["a"])
        cand7 = candidates([("ref/trait/t7", "a", "", "ambiguous", "monster;pages=62,306")])
        run(root, "--slice", "trait", "--candidates", str(cand7), "--write")
        with (root / REVIEW_DEFAULT).open(encoding="utf-8", newline="") as f:
            got = [r for r in csv.DictReader(f, delimiter="\t") if r["entry_id"] == "ref/trait/t7"]
        expect(bool(got) and got[0]["candidate_page"] == "62,306", "an ambiguous row keeps its candidate pages")

        # An entry whose books are all book-differs keeps no rows, and a rerun without the
        # proposals file leaves it alone.
        entry("t5", ["a", "b"])
        cand5 = candidates([
            ("ref/trait/t5", "a", "", "none", "no-aon-source-for-book"),
            ("ref/trait/t5", "b", "", "none", "no-aon-source-for-book"),
        ])
        run(root, "--slice", "trait", "--candidates", str(cand5), "--write")
        expect(rows_of(root, "t5") == [], "an entry whose books are all book-differs gets no rows")
        expect(run(root, "--slice", "trait", "--check") == 0, "a rerun without proposals leaves it alone")

        # Coarse and page-format rows are book-only and queued.
        entry("t2", ["a"])
        entry("t3", ["a"])
        (root / PRINT_DEFAULT).write_text(
            "entry_id\tpublication\tpage\tbasis\tnote\nref/trait/t3\ta\t12x\tprint\t\n", encoding="utf-8"
        )
        cand = candidates([("ref/trait/t2", "a", "5", "check", "")])
        run(root, "--slice", "trait", "--candidates", str(cand), "--write")
        expect(rows_of(root, "t2") == [("a", None)], "a coarse proposal gives a book-only row")
        expect(("ref/trait/t2", "a", "coarse") in review_of(root), "a coarse row is queued")
        expect(rows_of(root, "t3") == [("a", None)], "a print page in no known form gives a book-only row")
        expect(("ref/trait/t3", "a", "page-format") in review_of(root), "page-format is queued")

        # A print note queues the row for a look at its heading.
        entry("t4", ["a"])
        (root / PRINT_DEFAULT).write_text(
            "entry_id\tpublication\tpage\tbasis\tnote\nref/trait/t4\ta\t9\tprint\tfound without heading\n",
            encoding="utf-8",
        )
        run(root, "--slice", "trait", "--candidates", str(cand), "--write")
        expect(rows_of(root, "t4") == [("a", "9")], "a noted print page still gives a row")
        expect(("ref/trait/t4", "a", "heading-form") in review_of(root), "the note queues a heading-form line")

        # A range typo must fail loudly instead of selecting nothing.
        for bad in ("a", "b:a", ":b", "a:b:c"):
            try:
                parse_range(bad)
                expect(False, f"--books-range {bad!r} is rejected")
            except SystemExit:
                expect(True, f"--books-range {bad!r} is rejected")
        expect(parse_range("a:b") == ("a", "b"), "--books-range a:b parses")

        # Paragraph pages: a row covers its pages, ranges abbreviate.
        expect(covers("144-146", "145") and not covers("144", "147"), "covers() reads ranges")
        expect(join_pages(["144", "145", "147"]) == "144-145, 147", "join_pages() joins adjacent pages")

    print(f"{len(failures)} failure(s)")
    return 1 if failures else 0


# ---------------------------------------------------------------------------- main


def fillable(entry: Entry) -> bool:
    """An entry with rows that lacks a row for a book that the print-pages file confirms."""
    have = {r["publication"] for r in entry.rows}
    return any(pub not in have and (entry.id, pub) in PRINT for pub in entry.source_ids)


def selected(
    entry: Entry, slices: set[str], books: set[str] | None, book_range: tuple[str, str] | None = None
) -> str | None:
    """The slice that takes an entry, or None."""
    if "paragraphs" in slices and entry.kind == "class_option":
        lines = entry.body.split("\n")
        if sources_paragraphs(lines):
            return "paragraphs"
    for name in slices - {"paragraphs"}:
        if entry.kind != KIND_OF_SLICE[name]:
            continue
        if name == "mythic" and not entry.id.startswith(MYTHIC_PREFIX):
            continue
        if entry.kind == "feat" and name != "mythic":
            continue
        if entry.rows and not fillable(entry):
            continue
        if books is not None and (not entry.source_ids or entry.source_ids[0] not in books):
            continue
        if book_range is not None and not (
            entry.source_ids and book_range[0] <= entry.source_ids[0] <= book_range[1]
        ):
            continue
        return name
    return None


def parse_range(text: str) -> tuple[str, str]:
    """`FROM:TO` as a pair; a typo must not select nothing and pass `--check`."""
    if text.count(":") != 1:
        raise SystemExit(f"--books-range {text!r}: expected FROM:TO")
    lo, hi = text.split(":")
    if not lo or not hi:
        raise SystemExit(f"--books-range {text!r}: both ends are required")
    if lo > hi:
        raise SystemExit(f"--books-range {text!r}: FROM follows TO")
    return lo, hi


def reset_state() -> None:
    BASIS.clear()
    PRINT.clear()
    PRINT_NOTES.clear()
    PRINT_WITHHELD.clear()
    QUEUED_DIFFERS.clear()
    PROPOSAL_ONLY.clear()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("corpus", type=Path, nargs="?")
    ap.add_argument("--self-test", action="store_true", help="run the built-in tests and exit")
    ap.add_argument("--slice", action="append", choices=SLICES, dest="slices")
    ap.add_argument("--books", help="comma list of publication ids (first book of source_ids)")
    ap.add_argument("--books-range", help="FROM:TO, both inclusive, compared with the first source_ids book")
    ap.add_argument("--candidates", type=Path)
    ap.add_argument("--print-pages", type=Path, help=f"pages read in print (default {PRINT_DEFAULT})")
    ap.add_argument("--review", type=Path, help=f"review queue (default {REVIEW_DEFAULT})")
    ap.add_argument("--list-proposal-only", action="store_true",
                    help="print the rows whose page is a proposal with no sibling and no print basis")
    ap.add_argument("--sample", type=int, default=0, help="print N random added page rows")
    ap.add_argument("--seed", type=int, default=7)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    opts = ap.parse_args(argv)
    if opts.self_test:
        return self_test()
    if opts.corpus is None or not opts.slices:
        ap.error("a corpus directory and at least one --slice are required")
    reset_state()

    root = opts.corpus.resolve()
    review_path = opts.review or root / REVIEW_DEFAULT
    slices = set(opts.slices)
    books = set(opts.books.split(",")) if opts.books else None
    book_range = parse_range(opts.books_range) if opts.books_range else None
    titles, by_title = load_publications(root)
    entries = load_entries(root)
    by_id = {e.id: e for e in entries}
    cands = load_candidates(opts.candidates)
    print_path = opts.print_pages or root / PRINT_DEFAULT
    if print_path.exists():
        for key, row in load_candidates(print_path).items():
            if not row["page"]:
                # An empty page: print was searched and does not confirm the proposal.
                PRINT_WITHHELD[key] = row.get("note") or "print does not confirm the proposed page"
                continue
            PRINT[key] = row["page"]
            if row.get("note"):
                PRINT_NOTES[key] = row["note"]
    order = {pid: i for i, pid in enumerate(titles)}
    for line in read_review(review_path):
        if line["reason"] == "book-differs":
            QUEUED_DIFFERS.add((line["entry_id"], line["publication"]))

    counts: Counter[str] = Counter()
    changed: list[tuple[Entry, str]] = []
    new_reviews: list[dict] = []
    touched: set[str] = set()
    added_pages: list[tuple[str, str, str]] = []
    filled: set[tuple[str, str]] = set()  # books that got a row in an entry that had rows
    for entry in entries:
        slice_name = selected(entry, slices, books, book_range)
        if slice_name is None:
            continue
        filling = bool(entry.rows) and slice_name != "paragraphs"
        if not filling:
            touched.add(entry.id)
        counts[f"entries {slice_name}"] += 1
        if slice_name == "paragraphs":
            rows, body, reviews, c = process_paragraphs(entry, titles, by_title)
            counts.update(c)
            new_reviews.extend(reviews)
            if rows != entry.rows or body != entry.body:
                for r in rows:
                    old = next((o for o in entry.rows if o["publication"] == r["publication"]), None)
                    if r.get("page") and (old is None or old.get("page") != r["page"]):
                        added_pages.append((entry.id, r["publication"], r["page"]))
                changed.append((entry, entry.render(rows, body)))
            continue
        new_rows: list[dict] = [dict(r) for r in entry.rows]
        have = {r["publication"] for r in entry.rows}
        for pub in entry.source_ids:
            if pub in have:
                continue
            if filling and (entry.id, pub) not in PRINT:
                continue  # only a page read in print adds a row to an entry that has rows
            page, reason, cpage, note = decide(entry, pub, cands, by_id)
            row = {"publication": pub}
            if page:
                row["page"] = page
                counts["rows with page"] += 1
                added_pages.append((entry.id, pub, page))
                if (entry.id, pub) in PRINT_NOTES:
                    new_reviews.append(review(entry, pub, "heading-form", page, PRINT_NOTES[(entry.id, pub)]))
            elif reason == "book-differs":
                # No row: the membership stays flagged by the #461 warning (owner decision).
                counts["books left without a row (book-differs)"] += 1
                new_reviews.append(review(entry, pub, reason, cpage, note))
                continue
            else:
                counts["rows book-only"] += 1
                new_reviews.append(review(entry, pub, reason, cpage, note))
            if filling:
                filled.add((entry.id, pub))
                insert_row(new_rows, row, entry.source_ids)
            else:
                new_rows.append(row)
        text = entry.render(new_rows, entry.body) if new_rows else entry.text
        if text != entry.text:
            changed.append((entry, text))

    # The queue: keep a line while it still describes the corpus (see the reasons above) and this
    # run did not rebuild the entry; rebuilt entries take their new lines.
    current: dict[tuple[str, str], dict | None] = {}
    for e in entries:
        for r in e.rows:
            current[(e.id, r["publication"])] = r
    kept: list[dict] = []
    stale = 0
    for r in read_review(review_path):
        key = (r["entry_id"], r["publication"])
        if r["entry_id"] in touched:
            continue
        row = current.get(key)
        if r["reason"] in NOTE_REASONS:
            # Re-evaluated whenever the slice runs on the entry.
            if r["entry_id"] in by_id:
                kept.append(r)
            else:
                stale += 1
        elif r["reason"] == "book-differs":
            # It stays while the book is a member without a row; a row (print confirmed it) or
            # a `source_ids` without the book settles it.
            owner = by_id.get(r["entry_id"])
            if owner is not None and r["publication"] in owner.source_ids and row is None and key not in filled:
                kept.append(r)
            else:
                stale += 1
        elif row is not None and not row.get("page"):
            kept.append(r)
        else:
            stale += 1
    merged = []
    for r in kept + new_reviews:
        if r not in merged:
            merged.append(r)
    # Unknown-title lines have no publication; keep them stable by id.
    old_review_text = review_path.read_text(encoding="utf-8") if review_path.exists() else None
    tmp = review_path.with_suffix(".tmp")
    write_review(tmp, merged, order)
    new_review_text = tmp.read_text(encoding="utf-8")
    tmp.unlink()
    review_changed = new_review_text != (old_review_text if old_review_text is not None else "")
    if not merged and old_review_text is None:
        review_changed = False

    print(f"corpus {root}")
    for k in sorted(counts):
        print(f"  {k}: {counts[k]}")
    for k in sorted(BASIS):
        print(f"  {k}: {BASIS[k]}")
    print(f"  entry files to change: {len(changed)}")
    print(f"  review queue: {len(merged)} lines ({len(new_reviews)} from this run, {stale} stale dropped)")
    by_reason = Counter(r["reason"] for r in new_reviews)
    for k in sorted(by_reason):
        print(f"    {k}: {by_reason[k]}")

    if opts.list_proposal_only:
        print(f"\nproposal-only pages ({len(PROPOSAL_ONLY)}): no sibling row, no print basis")
        for eid, pub, page in sorted(PROPOSAL_ONLY):
            print(f"  {eid}\t{pub}\t{page}")
    if opts.sample and added_pages:
        rng = random.Random(opts.seed)
        sample = rng.sample(added_pages, min(opts.sample, len(added_pages)))
        print(f"\nsample of {len(sample)} of {len(added_pages)} added pages (seed {opts.seed}):")
        for eid, pub, page in sorted(sample):
            print(f"  {eid}\t{pub}\t{page}")

    if opts.write:
        for entry, text in changed:
            entry.path.write_text(text, encoding="utf-8")
        if review_changed:
            write_review(review_path, merged, order)
        print("written; run `cargo xtask corpus-fmt` next")
        return 0
    if opts.check:
        if changed or review_changed:
            print("STALE: a write would change files", file=sys.stderr)
            return 1
        print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
