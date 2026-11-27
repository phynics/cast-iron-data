#!/usr/bin/env python3
"""Base classes as printed prose (phynics/cast-iron#540): the compare of the class features of a `kind = "class"` entry against print.

A companion of `feature-prose-540.py` and `feature-prose-540-class-options.py`, which it loads. This first step is a REPORT: it writes no entry and no
file. It reads each base class of a book the way the archetype pass reads an archetype, so that the verdicts and holds can be counted before a
writer is built (the pilot on the seven Advanced Player's Guide classes, phynics/cast-iron#540).

What is read
------------
- The **region** of a class is its feature heads: the lines from the first `####` head to the next `###` heading (the class table, the spells-known
  table, the alternate capstones and the archetypes are outside it and stay as they are). No head, no anchor and no key moves: only the text under a
  head is compared. Each `####` head is read as the bold name of a feature (`headings_as_names` of the class-option script).
- The **window** of print is the section "Class Features" of the class: from that title to the next title that is not the title of a table.
  A class table is set in the middle of the text in print, and a table title does not end the window.
- A feature has its **level** from the class table (`class_table_levels` of the archetype script), which is what a class feature's trades point at.

Usage
-----
    feature-prose-540-classes.py --self-test
    feature-prose-540-classes.py [CORPUS] --compare --book ID [--classes alchemist,cavalier] --books DIR --cache DIR
"""

from __future__ import annotations

import argparse
import dataclasses
import importlib.util
import os
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


co = _load("feature_prose_540_class_options", "feature-prose-540-class-options.py")
fp = co.fp


def feature_region(body: str) -> tuple[int, int] | None:
    """(first line, end line) of the class features of a base-class body: from the first `####` head to the next `###` or higher heading."""
    lines = body.split("\n")
    first = next((i for i, ln in enumerate(lines) if ln.startswith("#### ")), None)
    if first is None:
        return None
    end = next((i for i in range(first, len(lines)) if re.match(r"^#{1,3} ", lines[i])), len(lines))
    return first, end


def window(blocks: list) -> list:
    """The blocks of the section "Class Features" of the class: after that title, up to the next title that is not the title of a table."""
    at = next((i for i, b in enumerate(blocks) if b.kind == "title" and fp.squash(b.plain()) == "classfeatures"), None)
    if at is None:
        return []
    out = []
    for b in blocks[at + 1:]:
        # a sidebar or a table title is set larger (24) than a subsection title (18): the section ends at the next subsection or class title
        if b.kind == "title" and not b.plain().strip().lower().startswith("table") and (b.size == 18 or b.size >= 38):
            break
        out.append(b)
    return out


def compare_class(corpus: Path, e, bk, cache: dict) -> dict:
    """The comparison of one base class: rows of the archetype comparison (print order), the window size and the levels of the class table."""
    region = feature_region(e.body)
    if region is None or not e.page.isdigit():
        return {"rows": [], "window": 0, "levels": {}, "problems": ["no `####` head, or no page"]}
    lines = e.body.split("\n")
    pseudo = co.headings_as_names("\n".join(lines[region[0]:region[1]]))
    page = int(e.page)
    blocks = fp.read_blocks(bk, page, min(page + 12, max(bk.pages)))
    win = window(blocks)
    e2 = dataclasses.replace(e, body=pseudo)
    res = fp.compare_entry(e2, [fp.Para("title", [(e.title, True, False)], page, 0, 20)] + win, bk)
    return {"rows": res["rows"], "window": len(win), "levels": fp.class_table_levels(corpus, e.id, cache), "problems": res["problems"]}


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), fp.publication_title(corpus, book))
    if not pdf:
        raise SystemExit(f"no copy of the book {book} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    co.install_split([x.title for x in co.load_class_options(corpus)])
    wanted = set(args.classes.split(",")) if args.classes else None
    total = Counter()
    cache: dict = {}
    for e in co.load_entries(corpus, "class", book):
        if not e.id.startswith("ref/class/") or (wanted and e.id.rsplit("/", 1)[1] not in wanted):
            continue                                       # the base classes (`ref/pclass/*` are prestige classes)
        r = compare_class(corpus, e, bk, cache)
        c = Counter(x["status"] for x in r["rows"])
        total.update(c)
        print(f"{e.id}: window {r['window']} blocks; " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())) + f"; heads not printed: {sum('head not printed' in x['notes'] for x in r['rows'])}")
        for x in r["rows"]:
            if x["status"] == "hold":
                print(f"    hold {x['head'][:34]}: {(x['notes'] or [''])[0][:100]}")
    print("total: " + ", ".join(f"{k} {v}" for k, v in sorted(total.items())))
    return 0


def self_test() -> int:
    ok, bad = 0, []

    def eq(a, b, what):
        nonlocal ok
        if a == b:
            ok += 1
        else:
            bad.append(f"{what}: {a!r} != {b!r}")

    body = "Intro.\n\n### Class Features and Spells Per Day\n\n|Level|\n| --- |\n|1st|\n\n#### Spells {#spells}\n\n**Ability:** A.\n\n#### Mystery {#mystery}\n\nB.\n\n### Alternate Capstones\n\nC.\n"
    r = feature_region(body)
    eq(body.split("\n")[r[0]:r[1]][0], "#### Spells {#spells}", "the region starts at the first head")
    eq("### Alternate Capstones" in "\n".join(body.split("\n")[r[0]:r[1]]), False, "the region ends at the next ### heading")
    eq(feature_region("No heads here.\n"), None, "a class with no head has no region")
    P = fp.Para
    blocks = [P("title", [("Oracle", True, False)], 42, 1, 38), P("title", [("Class Features", True, False)], 42, 1, 18),
              P("para", [("Spells: A.", False, False)], 42, 1), P("title", [("Table 2–5: Oracle", True, False)], 44, 0, 24), P("para", [("1st +0", False, False)], 44, 0),
              P("para", [("Orisons: B.", False, False)], 45, 0), P("title", [("Alternate Capstones", True, False)], 46, 0, 18), P("para", [("Late.", False, False)], 46, 0)]
    eq([b.plain() for b in window(blocks)], ["Spells: A.", "Table 2–5: Oracle", "1st +0", "Orisons: B."], "the window runs over a table and ends at the next title")
    side = blocks[:3] + [P("title", [("Fall From Grace", True, False)], 46, 0, 24), P("para", [("Sidebar.", False, False)], 46, 0), P("title", [("Ex-Antipaladins", True, False)], 46, 0, 18)]
    eq([b.plain() for b in window(side)], ["Spells: A.", "Fall From Grace", "Sidebar."], "a sidebar title (larger) does not end the window, the next subsection does")
    eq(window([blocks[0]]), [], "a page without the Class Features title has no window")
    for line in bad:
        print("FAIL", line)
    print(f"self-test: {ok} checks passed" if not bad else f"self-test: {len(bad)} failures")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(HERE.parent))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--book")
    ap.add_argument("--classes")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.compare:
        return run_compare(args)
    ap.error("one of --self-test, --compare")


if __name__ == "__main__":
    sys.exit(main())
