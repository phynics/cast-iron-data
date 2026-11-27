#!/usr/bin/env python3
"""The `ref/ability/*` lists as printed prose (phynics/cast-iron#540, the rule-entry rulings of 2026-11-24 and the layout calls of 2026-11-27).

    ability-lists-540.py --self-test
    ability-lists-540.py [CORPUS] --compare [--ids a,b] [--write] [--books DIR] [--cache DIR] [--checker BIN]

The 16 lists of the survey (and `companion-tricks`): a bold name line over import rows (`**Destruction**`, `**Passive:** ...`). The compare
reads the list's printed section (the page of the first source, a printed title or the first item to the next title) with the shared print
comparison of the archetype pass (`feature-prose-540.py`) and, as the class writers do, a print-coverage check: every printed sentence of the section
must stand in the written entry, else the list holds.

The layout (owner calls of 2026-11-27): an item that print sets as a run-in label stays a bold-lead paragraph ("**Destruction (Su):** ..."), no head, no
key; the opening sentences stay as print has them; no `features` on a rule entry; an item that has an entry of its own is a link under print's lead-in
(ruling 52), only to an entry of the right kind and class.
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


co = _load("co", "feature-prose-540-class-options.py")
fp = co.fp

IDS = ("advanced-armor-training advanced-versatile-performances advanced-weapon-training animal-foci annointings bloodline-mutations capstones "
       "channel-energy combat-styles dares gunslinger-renowned-deeds judgments outer-rifts-exploits psi-tech swashbuckler-renowned-deeds ward-aspects "
       "companion-tricks").split()

# The printed title of the section when it is not the title of the entry, and the number of pages after the cited one that the list can run over.
TITLES: dict[str, str] = {
    "advanced-versatile-performances": "Advanced Versatile Performances",
    "annointings": "Anointings",
    "dares": "Dares",
    "ward-aspects": "Ward Aspects",
    "judgments": "Judgment",
    "animal-foci": "Animal Focus",
    "channel-energy": "Channel Energy",
    "combat-styles": "Combat Style Feat",
    "companion-tricks": "Companion Tricks",
}
# The head of a class feature that print sets over the opening of the list ("Animal Focus (Su): At 1st level ..."): the paragraph is the list's opening.
OPENING_LEAD: dict[str, str] = {"animal-foci": "Animal Focus"}
# A list that has no section title of its own: the printed text of its first block.
FIRST_BLOCK: dict[str, str] = {"capstones": r"^Antipaladin\u2014Tip of the Spear"}
# The text of another section that the text layer joins to the last paragraph of an item: (entry, anchor) -> where it starts.
CUT_AT: dict[tuple[str, str], str] = {
    ("gunslinger-renowned-deeds", "lethal-patience"): "Swashbuckler Renowned Deeds",
    ("swashbuckler-renowned-deeds", "vengeful-soul"): "MYSTICS, MASKS, AND MURDER",
}
EXTRA_PAGES: dict[str, int] = {"capstones": 3, "companion-tricks": 3, "judgments": 1, "swashbuckler-renowned-deeds": 1, "advanced-weapon-training": 1}


print_lost = co.print_lost                      # the print-coverage check of the class-option script (#373)


def load_lists(corpus: Path, ids: list[str] | None = None) -> list:
    want = {f"ref/ability/{x}" for x in (ids or IDS)}
    return [e for e in co.load_entries(corpus, "none") if e.id in want]


def first_page(page: str) -> int | None:
    m = re.match(r"\d+", page or "")
    return int(m.group(0)) if m else None


def section_for(e, bk) -> tuple[list, list[str]]:
    """The printed section of a list: a title block (the title of the entry's section) and the blocks after it up to the next title that is no head of the list."""
    notes: list[str] = []
    page = first_page(e.page)
    if page is None:
        return [], ["no page is cited"]
    nums = [int(x) for x in re.findall(r"\d+", e.page)]
    lo, hi = min(nums), max(nums) + 1 + EXTRA_PAGES.get(e.id.rsplit("/", 1)[1], 0)       # the printed pages that the entry cites and the next one
    blocks = [b for b in fp.read_blocks(bk, max(1, lo - 2), min(hi + 4 + fp.PAGE_OFFSET[0], max(bk.pages))) if lo <= b.page <= hi]       # by the printed label of the block
    names = {fp.squash(fp.ABILITY_TAG.sub("", f.name)) for f in fp.parse_import(e.body, set())[1]}
    want = fp.squash(TITLES.get(e.id.rsplit("/", 1)[1], e.title))
    first = FIRST_BLOCK.get(e.id.rsplit("/", 1)[1])
    start = next((n for n, b in enumerate(blocks) if first and re.search(first, b.plain().strip())), None)
    if start is not None:
        start -= 1
    start = start if start is not None else next((n for n, b in enumerate(blocks) if b.kind == "title" and b.size >= 17 and "(" not in b.plain() and want and want in fp.squash(b.plain())), None)       # a section title, not the title of a feat
    if start is None:
        def starts_item(b) -> bool:
            head = b.plain().strip().split(":", 1)[0]
            return b.kind == "para" and len(head) < 60 and fp.squash(fp.ABILITY_TAG.sub("", head)) in names
        start = next((n for n, b in enumerate(blocks) if starts_item(b)), None)
        if start is None:
            return [], [f"no printed title `{TITLES.get(e.id.rsplit('/', 1)[1], e.title)}` and no item on the cited pages"]
        while start > 0 and blocks[start - 1].kind == "para":
            start -= 1                                              # the paragraphs of the opening, over the first item
        start -= 1
    end = len(blocks)
    for n in range(start + 1, len(blocks)):
        b = blocks[n]
        if b.kind == "title" and len(b.plain().strip()) > 3 and not b.plain().strip().lower().startswith("table") and fp.squash(b.plain()) not in names:      # a drop cap is no title
            end = n
            break
    # the section ends after the text of its last item: the next paragraph that has a head of its own is another feature (a class's next ability, the next section)
    inside = blocks[start + 1:end]
    items = [n for n, b in enumerate(inside) if (b.plain().strip().split(":", 1)[0] and len(b.plain().strip().split(":", 1)[0]) < 60
                                                and fp.squash(fp.ABILITY_TAG.sub("", b.plain().strip().split(":", 1)[0])) in names)]
    if items:
        stop = items[-1] + 1
        while stop < len(inside) and inside[stop].kind == "para" and fp.head_candidate(inside[stop]) is None:
            stop += 1
        inside = inside[:stop]
    lead = OPENING_LEAD.get(e.id.rsplit("/", 1)[1])
    if lead and inside and (hc := fp.head_candidate(inside[0])) and fp.squash(fp.ABILITY_TAG.sub("", hc[0])) == fp.squash(lead):
        runs = list(hc[1])
        if runs and runs[0][0].lstrip().startswith(":"):
            runs[0] = (runs[0][0].lstrip()[1:].lstrip(), runs[0][1], runs[0][2])
        inside[0] = fp.Para("para", runs, inside[0].page, inside[0].col, 0)
    title = fp.Para("title", [(e.title, True, False)], page, 0, 20)
    return [title] + inside, notes


def decisions_file(corpus: Path) -> Path:
    return corpus / "scripts" / "ability-lists-540.decisions.tsv"


def read_decisions(corpus: Path) -> dict[tuple[str, str], tuple[str, str]]:
    """`(entry id, anchor) -> (print|hold, note)`: a hold that a reader has settled against print (a progression in other words, an import paraphrase)."""
    path = decisions_file(corpus)
    return co.read_decisions(path) if path.exists() else {}


def compare_list(corpus: Path, e, bk, decisions: dict) -> dict:
    section, notes = section_for(e, bk)
    if not section:
        return {"rows": [], "opening": [], "problems": notes, "section": [], "feats": []}
    res = fp.compare_entry(e, section, bk)
    rows = res["rows"]
    for r in rows:
        dec = decisions.get((e.id, r["anchor"]))
        if dec and dec[0] == "print" and r["status"] == "hold" and not any(n.startswith(("head not printed", "link not placed")) for n in r["notes"][:1]):
            r["status"] = "print"
            r["notes"].append(f"decision: {dec[1]}")
    for r in rows:
        cut = CUT_AT.get((e.id.rsplit("/", 1)[1], r["anchor"]))
        if cut and cut in r["print"]:
            r["print"] = r["print"][:r["print"].index(cut)].rstrip()
            r["notes"].append(f"the text layer joined the heading of the next section to the paragraph ({cut!r}): cut there")
    probe = {fp.namekey(h) for h in [fp.head_of_para(p) for p in section[1:]] if h}
    _, feats = fp.parse_import(e.body, probe)
    return {"rows": rows, "opening": res.get("opening", []), "opening_links": res.get("opening_links", []), "problems": notes + list(res["problems"]), "section": section,
            "feats": feats}


def settled(plan: dict) -> bool:
    rows = plan["rows"]
    return bool(rows) and not plan["problems"] and all(r["status"] in ("print", "draft") and r["span"] for r in rows) and not any(f.pseudo for f in plan["feats"])


def item_paragraphs(r: dict) -> list[str]:
    """The written paragraphs of an item: print's first paragraph under the bold run-in label of its head (layout call 1 of 2026-11-27), then the others."""
    paras = [x.strip() for x in r["print"].strip().split("\n\n") if x.strip()]
    head = r["head"].strip().rstrip(":")
    return [f"**{head}:** {paras[0]}"] + paras[1:] if paras else [f"**{head}**"]


def converted_body(e, plan: dict) -> str:
    """The body with each item as a run-in paragraph of print's text and the opening as print has it; the headings of the entry stay where they are."""
    by_span = {r["span"]: r for r in plan["rows"] if r["span"]}
    opening_imp, feats = plan["opening_imp"], plan["feats"]
    out: list[str] = []
    links = list(plan.get("opening_links", []))
    for para in plan["opening"]:
        if not para.strip():
            continue
        para, lost = fp.apply_links(para, links)                         # the links of the import's opening, each placed once
        links = [l for l in links if l[0] in lost]
        out.append(para)
    out += ["\n".join(b) for b in opening_imp if b and b[0].startswith("#")]
    for f in feats:
        r = by_span[f.span_sha()]
        out += item_paragraphs(r)
        out += ["\n".join(b) for b in f.raw[1:] if b and b[0].startswith("#")]
    return "\n\n".join(out) + "\n"


def coverage(plan: dict, new_body: str) -> list[str]:
    """Print sentences of the section that the written body lacks."""
    printed = " ".join(" ".join("".join(x[0] for x in p.runs).split()) for p in plan["section"][1:] if p.kind == "para")
    return print_lost(printed, new_body)


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    ids = args.ids.split(",") if args.ids else None
    books: dict[str, object] = {}
    total, written = Counter(), 0
    decisions = read_decisions(corpus)
    for e in load_lists(corpus, ids):
        fp.configure_book(e.book)
        if e.book not in books:
            pdf = fp.find_pdf(Path(args.books), fp.publication_title(corpus, e.book))
            books[e.book] = fp.load_book(fp.book_xml(pdf, Path(args.cache))) if pdf else None
        bk = books[e.book]
        if bk is None:
            print(f"{e.id}: no copy of {e.book}")
            continue
        plan = compare_list(corpus, e, bk, decisions)
        plan["opening_imp"] = fp.parse_import(e.body, set())[0]
        c = Counter(r["status"] for r in plan["rows"])
        total.update(c)
        print(f"{e.id} ({e.book} p. {e.page}): section {len(plan['section'])} blocks; " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())) + "; problems: " + "; ".join(plan["problems"])[:200])
        for r in plan["rows"]:
            if r["status"] == "hold":
                print(f"    hold {r['head'][:30]}: {(r['notes'] or [''])[0][:110]}")
        if settled(plan):
            new = converted_body(e, plan)
            lost = coverage(plan, new)
            if lost:
                print(f"    held by the coverage check ({len(lost)}): " + " | ".join(x[:70] for x in lost[:3]))
            elif args.write:
                co.write_atomic(e.path, "+++\n" + e.front.strip("\n") + "\n+++\n\n" + new)
                written += 1
                print("    written")
    print("total: " + ", ".join(f"{k} {v}" for k, v in sorted(total.items())) + (f"; {written} lists written" if args.write else ""))
    if args.write and written and args.checker:
        import subprocess
        subprocess.run([args.checker, "fmt", str(corpus)], check=True)
    return 0


def self_test() -> int:
    ok, bad = 0, []

    def eq(a, b, what):
        nonlocal ok
        if a == b:
            ok += 1
        else:
            bad.append(f"{what}: {a!r} != {b!r}")

    eq(item_paragraphs({"head": "Destruction (Su)", "print": "First sentence.\n\nSecond paragraph."}), ["**Destruction (Su):** First sentence.", "Second paragraph."],
       "an item is a bold-lead paragraph with print's head; the other paragraphs follow")
    eq(print_lost("This is a long printed sentence of the list. Another printed sentence that is missing here.", "This is a long printed sentence of the list."),
       ["Another printed sentence that is missing here."], "the coverage check names a printed sentence that the entry lacks")
    eq(print_lost("This ability 4 4 3 3 is the equivalent of a spell of a level equal to one-third the level.", "This ability is the equivalent of a spell of a level equal to one-third the level."), [],
       "cells inside a printed sentence are no words of it")
    eq(settled({"rows": [{"status": "print", "span": "x"}], "problems": [], "feats": []}), True, "a list whose rows are all print or draft is settled")
    eq(settled({"rows": [{"status": "print", "span": ""}], "problems": [], "feats": []}), False, "a printed head that the import lacks holds the list (the window ran past the list)")
    eq(settled({"rows": [{"status": "hold", "span": "x"}], "problems": [], "feats": []}), False, "a held row holds the list")
    eq(settled({"rows": [{"status": "print", "span": "x"}], "problems": ["head not printed: A"], "feats": []}), False, "a problem holds the list")
    eq(first_page("14-15"), 14, "the first of the cited pages")
    eq(first_page(""), None, "no page")
    for line in bad:
        print("FAIL", line)
    print(f"self-test: {ok} checks passed" if not bad else f"self-test: {len(bad)} failures")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(HERE.parent))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--ids")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--checker")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.compare:
        return run_compare(args)
    ap.error("one of --self-test, --compare")


if __name__ == "__main__":
    sys.exit(main())
