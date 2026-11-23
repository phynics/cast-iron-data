#!/usr/bin/env python3
"""Build and check the membership queue of phynics/cast-iron#461 (slice S0).

    python3 scripts/membership-queue-461.py <corpus-dir> --screen-all <screen-all.tsv> [--out queue.tsv]
    python3 scripts/membership-queue-461.py <corpus-dir> --check [--queue queue.tsv]

The queue `scripts/membership-queue-461.tsv` lists every membership that the cleanup of #461 has
to decide. It started as the output of `scripts/membership-screen.py` (a screen of the books the
owner has in print) and still has its columns. This script keeps it complete as the corpus
changes. It reads

  * the corpus (`entries/`, `publications.toml`),
  * the committed queue (the verdicts: they are never changed or dropped), and
  * a fresh screen written with `membership-screen.py ... --status-out screen-all.tsv`: one row for
    every screened membership, including the ones the screen counts as printed. Only the person
    who has the PDFs can make it. The script never reads a PDF.

and writes the queue again. A row is in the queue when its (book, entry) pair is

  1. in the `corpus-check` warning: the book is in the entry's `source_ids`, is not the first
     book, and the entry has no `[[sources]]` row for it (the same rule as `uncited_memberships`
     in the checker). The screen's old queue held only 312 of the 1,471 pairs, because the screen
     counts a title on two or more pages of a book as printed, and generic titles (Medium,
     Languages, Rogue, Dwarf) always pass that test;
  2. a figurine membership (the 22 Figurine of Wondrous Power variants and the entry that lists
     them): all 23 carry the same non-first books with identical `[[sources]]` rows, so the
     warning does not see them, and the screen passes them because it drops the parenthetical
     from the title;
  3. in the screen's own queue (the old tags: `cite-off`, `review`, `hub-keep`, family leaks); or
  4. an old row of the committed queue.

Columns: the 21 of the screen (see `membership-screen.py`), then

  group      what kind of membership it is. One value per row, the first that fits:
               standard-racial-trait  a `racial_trait` of one of the 7 core races with
                                      `alternate = false` (638 pairs in the warning)
               class-hub              an `ref/class/*` entry, or an `ref/rule/class-*/*` mirror
               race-hub               a `ref/race/*` entry
               faith-excerpt          a `ref/faith/*` entry whose body quotes a section (the deity's
                                      Divine Fighting Technique) under a `**Source**` line that
                                      names the book (16 pairs in the warning)
               hub-cited              another `rule` entry (hubs, abilities) whose body has a
                                      `**Source**` line that names the book (cite it)
               link-only-hub          another `rule` entry without such a line: one or two
                                      sentences and links (owner ruling of 2026-11-24, design (a))
               figurine               a Figurine of Wondrous Power variant, or the entry that lists them
               no-pdf                 any other entry, in a book that is not among the owner's PDFs
               single-entry           any other entry
  slice      the slice of #461 that decides it: `S1`..`S12`, `S4a`/`S4b` (figurines, seven books
             each in book order), `S6`/`S7` (class hubs A-M, N-Z), `S8` (class mirrors). A row
             that is not in the warning is `S11`, except for figurines. A row with a verdict has
             `done` (decided in batches 1-4 and #98) or `S0` (decided by this script's rules).
  ruling     the owner ruling that decides a row with no verdict yet (nothing waits any more):
               `hub-design-a` (link-only-hub): the hub keeps only its home book. The 14 navigation
                 hubs first get their topic lists back as `::: entry-link` blocks; then their
                 non-first books go (removed where a listed entry carries the book or nothing
                 does, cited where the body prints a section, read in print where the design
                 table says so). The hub page shows each listed row's book (an app change). The
                 home book of these hubs and the other 545 dropped subtopic lists are post-v1
                 (phynics/cast-iron-data#277 and #276)
               `faith-link` (faith-excerpt): replace the quoted technique section with a link to
                 the technique's own entry; the book then leaves the faith. Where no such entry
                 exists the slice reports it instead of guessing
  in_warning `yes` when the pair is in the `corpus-check` warning now
  pdf        `yes` when the book is among the owner's PDFs (the screen read it), else `no`
  body_line  `yes` when a body `**Source**` line names the book. `cite` converts it with
             `--convert-body`
  exact      `yes` when the title is printed on the cited page itself (the screen's `status` allows
             one page before and after), `no` when it is not, empty without a cited page
  paren      for a title with a parenthetical (a variant name): `page` when the parenthetical is on
             the cited page, `book` when it is elsewhere in the book, `none` when nowhere, empty
             otherwise. This is the evidence for figurines: `status` is `printed` for all of them

Verdicts (existing ones are kept as they are). `remove`, `keep` and `expands` are the decisions of
`membership-apply.py` and `expansion-credits-apply.py` (#459). This script adds two:

  keep      (existing) the book prints the entry and the entry already has its `[[sources]]` row
  cite      the book prints the entry and the entry has no row for it: `membership-apply.py` adds
            the row with `print_page`. Not assigned here; the slices assign it
  resolved  another change has settled the pair: the book is out of `source_ids` (evidence
            `out-of-source-ids`), or it is out and the entry holds an `[[expanded_in]]` credit
            for it (evidence `expanded-in-row`, `print_page` is the credited page)

Rule for the new keeps (verdict `keep`, evidence `title-on-cited-page`, `print_page` the row's
page): a row with no verdict, the entry has a `[[sources]]` row for the book with a page, the
screen found the title on the cited page itself (`exact = yes`), and the title has no
parenthetical, or the parenthetical is on the page as well (a figurine's variant name: the row's
page names the variant). A figurine whose variant name is not on the cited page gets no verdict;
S4 reads that page. The rule is the screen's, not a reading: the title is on the cited page, which
is what the row says.

`--check` needs no screen. It proves the committed queue against the corpus: every pair of the
warning and every figurine membership has a row, no pair appears twice, `group`, `slice`,
`ruling` and `in_warning` equal what the corpus gives, a `keep` or `cite`-applied row has its
`[[sources]]` row, and a `resolved` row is out of `source_ids`. It exits 1 with the first
problems when the queue is stale; run it after each slice.

Output is deterministic: sorted, no timestamps, no PDF text, no file names.
"""
from __future__ import annotations

import argparse
import collections
import csv
import importlib.util
import re
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_module(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


screen = load_module("membership_screen", "membership-screen.py")
apply = load_module("membership_apply", "membership-apply.py")

SCREEN_COLS = ["book", "entry", "kind", "title", "member", "n_books", "tag", "status", "cited", "cite",
               "hits", "found", "via", "family", "parent_has_book", "gate", "proposed_primary",
               "proposed_status", "verdict", "print_page", "evidence"]
NEW_COLS = ["group", "slice", "ruling", "in_warning", "pdf", "body_line", "exact", "paren"]
COLS = SCREEN_COLS + NEW_COLS
CORE_RACES = ("dwarf", "elf", "gnome", "half-elf", "half-orc", "halfling", "human")
DECIDED = ("remove", "keep", "expands", "cite", "resolved")
SLICE_BY_RACE = {"dwarf": "S1", "elf": "S1", "gnome": "S2", "half-elf": "S2",
                 "half-orc": "S3", "halfling": "S3", "human": "S3"}
FIGURINE = "Figurine of Wondrous Power"


# ---------------------------------------------------------------------------------- the corpus


def load(root: Path):
    pubs, entries = screen.load_corpus(root)
    title_to_pub = {}
    for pid, p in pubs.items():
        title_to_pub.setdefault(screen.title_key(p["title"]), pid)
        for t in screen.ALT_TITLES.get(pid, []):
            title_to_pub.setdefault(screen.title_key(t), pid)
    return pubs, entries, title_to_pub


def warning_pairs(entries: dict) -> set[tuple[str, str]]:
    """(book, entry) of every membership that `corpus-check` warns about (#461): a book of
    `source_ids` other than the first with no `[[sources]]` row."""
    out = set()
    for e, d in entries.items():
        rows = {s["publication"] for s in d.get("sources", [])}
        for b in d["source_ids"][1:]:
            if b not in rows:
                out.add((b, e))
    return out


def is_figurine(d: dict) -> bool:
    """The 22 variants (`Figurine of Wondrous Power (Slate Spider)`) and the entry that lists them
    (`Figurines of Wondrous Power`): all 23 carry the same books and identical rows."""
    return d["kind"] == "item" and (d["title"].startswith(FIGURINE + " (") or d["title"] == "Figurines of Wondrous Power")


def figurine_pairs(entries: dict) -> set[tuple[str, str]]:
    return {(b, e) for e, d in entries.items() if is_figurine(d) for b in d["source_ids"][1:]}


def group_of(d: dict, body_line: bool, pdf: bool) -> str:
    e = d["id"]
    parts = e.split("/")
    if d["kind"] == "racial_trait" and len(parts) > 2 and parts[2] in CORE_RACES \
            and d.get("fields", {}).get("alternate") is False:
        return "standard-racial-trait"
    if d["kind"] == "class" or re.match(r"ref/rule/class-[^/]+/", e):
        return "class-hub"
    if d["kind"] == "race":
        return "race-hub"
    if d["kind"] == "rule":
        # In a book that is not among the PDFs ruling 4 decides (keep, with the corpus's own page),
        # unless the entry is a collector hub that no body line cites: that one is a link-only hub.
        if not pdf and not (screen.is_hub(d) and not body_line):
            return "no-pdf"
        if body_line and e.startswith("ref/faith/"):
            return "faith-excerpt"
        return "hub-cited" if body_line else "link-only-hub"
    if is_figurine(d):
        return "figurine"
    return "single-entry" if pdf else "no-pdf"


def ruling_of(group: str) -> str:
    """The owner ruling of 2026-11-24 on link-only hubs (design (a)) and faith excerpts."""
    return {"link-only-hub": "hub-design-a", "faith-excerpt": "faith-link"}.get(group, "")


def slice_of(group: str, d: dict, book: str, in_warning: bool, figurine_books: list[str]) -> str:
    if group == "figurine":
        return "S4a" if figurine_books.index(book) < 7 else "S4b"
    if not in_warning:
        return "S11"
    parts = d["id"].split("/")
    if group == "standard-racial-trait":
        return SLICE_BY_RACE[parts[2]]
    if group == "class-hub":
        if d["kind"] == "class":
            return "S6" if parts[2][0] < "n" else "S7"
        return "S8"
    return {"race-hub": "S9", "hub-cited": "S10", "link-only-hub": "S10", "faith-excerpt": "S10",
            "single-entry": "S5", "no-pdf": "S12"}[group]


def expanded_pages(d: dict) -> dict[str, str]:
    return {x["publication"]: x.get("page", "") for x in d.get("expanded_in", [])}


# -------------------------------------------------------------------------------- the rows


def read_tsv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def corpus_row(d: dict, book: str, title_to_pub: dict) -> dict:
    """A row for a pair that no screen saw (the book has no owner PDF): the tag by the screen's
    rules, as far as the corpus alone decides them."""
    row = next((s for s in d.get("sources", []) if s["publication"] == book), None)
    page = (row or {}).get("page") or ""
    cite = "row" if page else "none"
    if not page:
        bp = screen.body_pages(d["_body"], title_to_pub).get(book)
        if bp:
            page, cite = bp, "body"
    parent = d.get("parent")
    if screen.is_hub(d):
        tag = "hub-keep"
    elif row is None and parent and book in PARENT_BOOKS.get(parent, ()):
        tag = "inherited"
    elif row is None:
        tag = "uncited"
    else:
        tag = "review"
    return {"kind": d["kind"], "title": d["title"].replace("\t", " "), "member": d["source_ids"].index(book) + 1,
            "n_books": len(d["source_ids"]), "tag": tag, "status": "no-pdf", "cited": page, "cite": cite,
            "hits": 0, "found": "", "via": "", "family": "",
            "parent_has_book": "yes" if parent and book in PARENT_BOOKS.get(parent, ()) else "",
            "gate": "", "proposed_primary": "", "proposed_status": "", "verdict": "", "print_page": "", "evidence": ""}


PARENT_BOOKS: dict[str, set[str]] = {}


def build(root: Path, queue_path: Path, screen_all: Path) -> list[dict]:
    pubs, entries, title_to_pub = load(root)
    PARENT_BOOKS.clear()
    PARENT_BOOKS.update({e: set(d["source_ids"]) for e, d in entries.items()})
    old = {(r["book"], r["entry"]): r for r in read_tsv(queue_path)}
    fresh = {(r["book"], r["entry"]): r for r in read_tsv(screen_all)}
    pdf_books = {b for b, _ in fresh}
    warn = warning_pairs(entries)
    fig = figurine_pairs(entries)
    fig_books = sorted({b for b, _ in fig})
    keys = set(old) | warn | fig | {k for k, r in fresh.items() if r["queued"] == "yes"}
    rows = []
    for (book, e) in sorted(keys):
        d = entries.get(e)
        if d is None or book not in pubs:
            raise SystemExit(f"refused: the queue names {e} in {book}, which the corpus does not have")
        o = old.get((book, e))
        f = fresh.get((book, e))
        in_warning = (book, e) in warn
        verdict = o["verdict"] if o else ""
        if o and verdict:
            r = {c: o[c] for c in SCREEN_COLS}  # a decided row keeps its screen columns as they were
        elif f:
            r = {c: f[c] for c in SCREEN_COLS}
            if o:  # a gate the reviewer cleared before the verdict is lost only with the verdict
                r["print_page"], r["evidence"] = o["print_page"], o["evidence"]
        elif o:  # no fresh evidence (the book left source_ids, or has no PDF): the old columns stay
            r = {c: o[c] for c in SCREEN_COLS}
        else:
            r = {"book": book, "entry": e, **corpus_row(d, book, title_to_pub)}
        r["book"], r["entry"] = book, e
        body_line = apply.body_citation("+++\n+++\n" + d["_body"], pubs[book]["title"])
        has_row = next((s for s in d.get("sources", []) if s["publication"] == book), None)
        # The fresh screen is the better evidence for both columns, also on a decided row.
        src = f or o or {}
        r["exact"], r["paren"] = src.get("exact", ""), src.get("paren", "")
        group = group_of(d, body_line, book in pdf_books)
        # The verdicts this script assigns (S0).
        assigned = False
        if not verdict:
            if book not in d["source_ids"]:
                exp = expanded_pages(d)
                if book in exp:
                    verdict, r["print_page"], r["evidence"] = "resolved", exp[book], "expanded-in-row"
                else:
                    verdict, r["print_page"], r["evidence"] = "resolved", "none", "out-of-source-ids"
                assigned = True
            elif has_row and has_row.get("page") and r["exact"] == "yes" and r["paren"] in ("", "page"):
                verdict, r["print_page"], r["evidence"] = "keep", has_row["page"], "title-on-cited-page"
                assigned = True
        r["verdict"] = verdict
        r["group"] = group
        r["in_warning"] = "yes" if in_warning else ""
        r["pdf"] = "yes" if book in pdf_books else "no"
        r["body_line"] = "yes" if body_line else ""
        if verdict:
            r["slice"] = "S0" if assigned else ((o or {}).get("slice") or "done")
        else:
            r["slice"] = slice_of(group, d, book, in_warning, fig_books)
        r["ruling"] = ruling_of(group) if not verdict else ""
        rows.append(r)
    order = {t: i for i, t in enumerate(screen.TAG_ORDER)}
    rows.sort(key=lambda r: (r["book"], order[r["tag"]], r["entry"]))
    return rows


def write(rows: list[dict], path: Path) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(COLS) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in COLS) + "\n")


def summary(rows: list[dict], root: Path) -> None:
    _, entries, _ = load(root)
    warn = warning_pairs(entries)
    print(f"rows: {len(rows)}; warning pairs: {len(warn)} in {len({e for _, e in warn})} entries; "
          f"figurine memberships: {len(figurine_pairs(entries))}")
    inq = {(r["book"], r["entry"]) for r in rows}
    print(f"warning pairs without a row: {len(warn - inq)}")
    print("verdict:", dict(sorted(collections.Counter(r["verdict"] or "(none)" for r in rows).items())))
    print("group, in the warning:")
    for g, n in sorted(collections.Counter(r["group"] for r in rows if r["in_warning"]).items()):
        print(f"  {g}\t{n}")
    print("group, all rows with no verdict:")
    for g, n in sorted(collections.Counter(r["group"] for r in rows if not r["verdict"]).items()):
        print(f"  {g}\t{n}")
    print("slice, rows with no verdict:", dict(sorted(collections.Counter(r["slice"] for r in rows if not r["verdict"]).items())))
    print("slice, rows with a verdict:", dict(sorted(collections.Counter(r["slice"] for r in rows if r["verdict"]).items())))
    print("new in S0:", dict(sorted(collections.Counter((r["verdict"], r["evidence"], r["group"]) for r in rows if r["slice"] == "S0").items())))


# ------------------------------------------------------------------------------------ --check


def check(root: Path, queue_path: Path) -> int:
    pubs, entries, _ = load(root)
    rows = read_tsv(queue_path)
    problems = []
    seen = set()
    for r in rows:
        k = (r["book"], r["entry"])
        if k in seen:
            problems.append(f"duplicate row {r['entry']} in {r['book']}")
        seen.add(k)
    warn = warning_pairs(entries)
    fig = figurine_pairs(entries)
    for b, e in sorted((warn | fig) - seen):
        problems.append(f"no row for {e} in {b} ({'warning' if (b, e) in warn else 'figurine'})")
    fig_books = sorted({b for b, _ in fig})
    pdf_of = {r["book"]: r["pdf"] for r in rows}
    for r in rows:
        for c in NEW_COLS:
            if c not in r:
                raise SystemExit(f"refused: the queue has no column {c}; run this script with --screen-all")
        e, b = r["entry"], r["book"]
        d = entries.get(e)
        if d is None:
            problems.append(f"{e} is not an entry")
            continue
        in_ids = b in d["source_ids"]
        row = next((s for s in d.get("sources", []) if s["publication"] == b), None)
        in_warning = (b, e) in warn
        if (r["in_warning"] == "yes") != in_warning:
            problems.append(f"{e} in {b}: in_warning is {r['in_warning']!r}, the corpus says {in_warning}")
        body_line = apply.body_citation("+++\n+++\n" + d["_body"], pubs[b]["title"])
        group = group_of(d, body_line, pdf_of.get(b) == "yes")
        if r["group"] != group:
            problems.append(f"{e} in {b}: group {r['group']} is not {group}")
        if r["verdict"] == "keep" and in_ids and r["member"] != "1" and row is None:
            problems.append(f"{e} in {b}: verdict keep, but the entry has no [[sources]] row for the book (use cite)")
        if r["verdict"] == "resolved" and in_ids:
            problems.append(f"{e} in {b}: verdict resolved, but the book is back in source_ids")
        if not r["verdict"]:
            if r["ruling"] != ruling_of(group):
                problems.append(f"{e} in {b}: ruling {r['ruling']!r} is not {ruling_of(group)!r}")
            want = slice_of(group, d, b, in_warning, fig_books) if in_ids else "?"
            if in_ids and r["slice"] != want:
                problems.append(f"{e} in {b}: slice {r['slice']} is not {want}")
            if not in_ids:
                problems.append(f"{e} in {b}: no verdict, but the book is out of source_ids")
    for p in problems[:40]:
        print(p)
    print(f"queue rows: {len(rows)}; warning pairs: {len(warn)}; figurine memberships: {len(fig)}; problems: {len(problems)}")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--queue", type=Path, default=HERE / "membership-queue-461.tsv")
    ap.add_argument("--screen-all", type=Path, help="the --status-out file of a fresh membership-screen.py run")
    ap.add_argument("--out", type=Path, help="default: --queue (the queue is rewritten in place)")
    ap.add_argument("--check", action="store_true", help="check the queue against the corpus; write nothing")
    args = ap.parse_args()
    if args.check:
        return check(args.corpus, args.queue)
    if not args.screen_all:
        ap.error("--screen-all is required unless --check")
    rows = build(args.corpus, args.queue, args.screen_all)
    write(rows, args.out or args.queue)
    summary(rows, args.corpus)
    return 0


if __name__ == "__main__":
    sys.exit(main())
