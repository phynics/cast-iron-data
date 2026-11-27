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
cl = _load("cl", "feature-prose-540-classes.py")
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
# A list that print sets in a class chapter (its class table stands in the text): the class whose table the text layer runs into the list.
IN_CLASS_TABLE: dict[str, str] = {"judgments": "ref/class/inquisitor", "animal-foci": "ref/class/hunter"}
# Lists whose items print heads with a difficulty class ("Aid (DC 20):"): the "(DC 20)" is a suffix of the head, not of the name.
DC_LISTS = {"companion-tricks"}
DC_HEAD = re.compile(r"\s*\((DC \d+)\)\s*$")
# Items that print sets in the list's section and that other entries hold: left out of the written list. `ELSEWHERE_COUNT` is the number of printed heads that the
# review found there: the inventory check holds the list when print has more or fewer heads left out.
ELSEWHERE: dict[str, str] = {
    "capstones": "the capstones of the classes are the `### Alternate Capstones` sections of the class entries",
    "gunslinger-renowned-deeds": "the standards and deeds printed on the same pages belong to other entries (the Cavalier's battle standards, the swashbuckler's deeds)",
    "swashbuckler-renowned-deeds": "the gunslinger's deeds printed at the head of the page belong to the gunslinger's list",
    "animal-foci": "the feature heads of the Hunter's chapter printed on the same pages belong to the class entry"}
ELSEWHERE_COUNT: dict[str, int] = {"capstones": 38}          # the class-specific capstones of Chronicle of Legends pp. 28-30: each is in its class entry
# Lists whose printed items that the import lacks are written from print (the import has 16 of the 31 tricks of Ultimate Wilderness pp. 214-217; no entry of the
# corpus holds the others as items of their own, `animal-tricks` is one list of the Core Rulebook's version).
PRINT_ONLY = {"companion-tricks"}
# The first printed page of a list's section when the cited page is not where it starts (the Judgment ability starts on the page before its list of judgments).
PAGE_START: dict[str, int] = {"judgments": 38}
# Titles inside a list's section that do not end it: a box that print sets in the middle of the list ("Pathfinder Notes") is left out; a heading of the section
# stays a heading of the entry ("Arcanist Exploits", in the Exploits of the Outer Rifts).
SKIP_TITLES: dict[str, set[str]] = {"capstones": {"pathfindernotes"}}
HEADING_TITLES: dict[str, set[str]] = {"outer-rifts-exploits": {"Arcanist Exploits"}}
# An opening that print sets inside the last paragraph of the previous list (the text layer joins "DEEDS OF RENOWN Swashbucklers and gunslingers ..." to the end of
# the standards above it): typed from print here and checked against the pages it stands on (every paragraph must be found in the text of the pages): (kind, text),
# kind "p" a paragraph, "h" a heading of the entry (an explicit key is made from it).
_DEEDS_OPENING = ("Swashbucklers and gunslingers perform impressive deeds through their grit and panache, but some are capable of truly spectacular acts known as renowned "
                  "deeds. A swashbuckler or gunslinger (though not members of other classes) can select a renowned deed for her class upon reaching the class level listed in "
                  "the deed's description. This replaces the specific listed deed or deeds; if the character would not gain the appropriate deeds, she cannot select the "
                  "renowned deed, as if selecting an archetype.")
_CAPSTONES_OPENING = ("When a character reaches the 20th level of a class, she gains a powerful class feature or ability, sometimes referred to as a capstone. The following "
                      "section provides new capstones for characters to select at 20th level. A character can select one of the following capstones in place of the capstone "
                      "provided by her class. Some capstones are for specific classes, while others are for a range of classes that qualify for them.")
OPENING_TYPED: dict[str, list[tuple[str, str]]] = {
    # print sets "Other Capstones" and its sentence at the end of the last class-specific capstone (the text layer joins them); the class-specific capstones are in the
    # class entries, so the heading "Class-Specific Capstones" and its sentence are not written here
    "capstones": [("p", _CAPSTONES_OPENING),
                  ("p", "In some cases, a capstone specifies what ability it replaces. A character can't select a new capstone if she has previously traded away her class "
                        "capstone via an archetype. Clerics and wizards can receive a capstone at 20th level, despite not having one to begin with."),
                  ("h", "Other Capstones"),
                  ("p", "The following capstone abilities are for characters who meet the specifications listed in the text for each.")],
    "gunslinger-renowned-deeds": [("p", _DEEDS_OPENING), ("h", "Gunslinger Renowned Deeds"), ("p", "The following renowned deeds are available for gunslingers.")],
    "swashbuckler-renowned-deeds": [("p", _DEEDS_OPENING), ("h", "Swashbuckler Renowned Deeds"), ("p", "The following renowned deeds are available for swashbucklers.")],
}
# Headings of the import that print does not have (ruling 10): "1st-Level Renowned Deed" groups the deeds by the level that the import read in them.
INVENTED_HEADINGS = {"gunslinger-renowned-deeds", "swashbuckler-renowned-deeds"}
INVENTED_RE = re.compile(r"^#+ \d+(?:st|nd|rd|th)?-Level Renowned Deed\s*$")
# The head of a class feature that print sets over the opening of the list ("Animal Focus (Su): At 1st level ..."): the paragraph is the list's opening.
OPENING_LEAD: dict[str, str] = {"animal-foci": "Animal Focus", "judgments": "Judgment"}
# A list that has no section title of its own: the printed text of its first block.
FIRST_BLOCK: dict[str, str] = {"capstones": r"^Antipaladin\u2014Tip of the Spear", "gunslinger-renowned-deeds": r"^Thundering Shot", "swashbuckler-renowned-deeds": r"^Vengeful Heart"}
# The text of another section that the text layer joins to the last paragraph of an item: (entry, anchor) -> where it starts.
CUT_AT: dict[tuple[str, str], str] = {
    ("gunslinger-renowned-deeds", "lethal-patience"): "Swashbuckler Renowned Deeds",
    ("swashbuckler-renowned-deeds", "vengeful-soul"): "MYSTICS, MASKS, AND MURDER",
    ("capstones", "won-t-stay-dead"): "GRAND DISCOVERY",
}
EXTRA_PAGES: dict[str, int] = {"capstones": 3, "companion-tricks": 3, "judgments": 1, "swashbuckler-renowned-deeds": 1, "advanced-weapon-training": 1}


print_lost = co.print_lost                      # the print-coverage check of the class-option script (#373)


# The pages that the printed section of a list covers (the page row of the first source): the page row names where the section is, from its title or opening to its last item.
PAGE_ROWS: dict[str, str] = {
    "advanced-versatile-performances": "12-13", "animal-foci": "27-28", "annointings": "22-23", "bloodline-mutations": "10-11", "capstones": "28-31",
    "companion-tricks": "214-217", "gunslinger-renowned-deeds": "4-5", "judgments": "38-39", "outer-rifts-exploits": "6-7"}
# The title of the entry when the import's is a misspelling of print's (the section is "Anointings" in print).
TITLE_ROWS: dict[str, str] = {"annointings": "Anointings"}


def fixed_front(e) -> str:
    """The front matter with the page row of the list's section and the corrected title."""
    front = e.front
    key = e.id.rsplit("/", 1)[1]
    if key in PAGE_ROWS:
        front = re.sub(r'^page = "[^"]*"', f'page = "{PAGE_ROWS[key]}"', front, count=1, flags=re.M)
    if key in TITLE_ROWS:
        front = re.sub(r'^title = "[^"]*"', f'title = "{TITLE_ROWS[key]}"', front, count=1, flags=re.M)
    return front


def load_lists(corpus: Path, ids: list[str] | None = None) -> list:
    want = {f"ref/ability/{x}" for x in (ids or IDS)}
    return [e for e in co.load_entries(corpus, "none") if e.id in want]


def first_page(page: str) -> int | None:
    m = re.match(r"\d+", page or "")
    return int(m.group(0)) if m else None


CORPUS_DIR: list[Path] = [HERE.parent]
CONTEXT_TEXT: dict[str, str] = {}              # entry -> the squashed text of the cited pages and the one before (the typed openings are checked against it)
DC_OF: dict[tuple[str, str], str] = {}        # (entry, namekey of the head) -> "DC 20"
TRAILING: dict[str, list[str]] = {}           # entry -> the printed heads that follow the last known item inside the titles of the section (an item that the entry lacks, at the end)


def corpus_dir() -> Path:
    return CORPUS_DIR[0]


def table_clean(blocks: list, tail: str) -> list:
    """The blocks without the class table that the text layer runs into the text of a class chapter: the prose before and after the cells stays (the class
    script's reading: `split_table_runs`, `prose_after_cells`, `join_across_tables`)."""
    out = []
    for b in blocks:
        if b.kind == "title" and b.plain().strip().lower().startswith("table"):
            continue                                                # the title of a class table is no text of the list
        if b.kind == "para":
            cut = cl.split_table_runs(b, tail)
            if cut is not None:
                out += cut
                continue
            if cl.is_table_para(b.plain()):
                prose = cl.prose_after_cells(b.plain(), tail)
                if prose:
                    out.append(fp.Para("para", [(prose, False, False)], b.page, b.col, 0))
                continue
        out.append(b)
    return cl.join_across_tables(out)


def section_for(e, bk, names: set[str] | None = None) -> tuple[list, list[str]]:
    """The printed section of a list: a title block (the title of the entry's section) and the blocks after it up to the next title that is no head of the list."""
    notes: list[str] = []
    page = first_page(e.page)
    if page is None:
        return [], ["no page is cited"]
    nums = [int(x) for x in re.findall(r"\d+", e.page)]
    lo, hi = min(nums + [PAGE_START.get(e.id.rsplit("/", 1)[1], min(nums))]), max(nums) + 1 + EXTRA_PAGES.get(e.id.rsplit("/", 1)[1], 0)       # the printed pages that the entry cites and the next one
    blocks = [b for b in fp.read_blocks(bk, max(1, lo - 2), min(hi + 4 + fp.PAGE_OFFSET[0], max(bk.pages))) if lo <= b.page <= hi]       # by the printed label of the block
    if e.id.rsplit("/", 1)[1] in IN_CLASS_TABLE:
        blocks = table_clean(blocks, cl.table_tail((corpus_dir() / "entries" / (IN_CLASS_TABLE[e.id.rsplit("/", 1)[1]].removeprefix("ref/") + ".md")).read_text(encoding="utf-8")))
    if names is None:
        names = {fp.squash(fp.ABILITY_TAG.sub("", f.name)) for f in fp.parse_import(e.body, set())[1]}
    want = fp.squash(TITLES.get(e.id.rsplit("/", 1)[1], e.title))
    CONTEXT_TEXT[e.id] = fp.squash(" ".join(b.plain() for b in fp.read_blocks(bk, max(1, lo - 3), min(hi + 4 + fp.PAGE_OFFSET[0], max(bk.pages))) if lo - 1 <= b.page <= hi))
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
    key = e.id.rsplit("/", 1)[1]
    soft = SKIP_TITLES.get(key, set()) | {fp.squash(x) for x in HEADING_TITLES.get(key, set())}
    end = len(blocks)
    for n in range(start + 1, len(blocks)):
        b = blocks[n]
        if b.kind == "title" and len(b.plain().strip()) > 3 and not b.plain().strip().lower().startswith("table") and fp.squash(b.plain()) not in names | soft:      # a drop cap is no title
            end = n
            break
    # the section ends after the text of its last item: the next paragraph that has a head of its own is another feature (a class's next ability, the next section)
    inside = [b for b in blocks[start + 1:end] if not (b.kind == "title" and fp.squash(b.plain()) in SKIP_TITLES.get(key, set()))]
    items = [n for n, b in enumerate(inside) if (b.plain().strip().split(":", 1)[0] and len(b.plain().strip().split(":", 1)[0]) < 60
                                                and fp.squash(fp.ABILITY_TAG.sub("", b.plain().strip().split(":", 1)[0])) in names)]
    if items:
        stop = items[-1] + 1
        while stop < len(inside) and inside[stop].kind == "para" and fp.head_candidate(inside[stop]) is None:
            stop += 1
        TRAILING[e.id] = [fp.ABILITY_TAG.sub("", hc[0]).strip() for b in inside[stop:] if b.kind == "para" and (hc := fp.head_candidate(b)) and hc[2]]
        inside = inside[:stop]
    lead = OPENING_LEAD.get(e.id.rsplit("/", 1)[1])
    if lead:
        n = next((n for n, b in enumerate(inside) if b.kind == "para" and (hc := fp.head_candidate(b)) and fp.squash(fp.ABILITY_TAG.sub("", hc[0])) == fp.squash(lead)), None)
        if n is not None:
            hc = fp.head_candidate(inside[n])
            runs = list(hc[1])
            if runs and runs[0][0].lstrip().startswith(":"):
                runs[0] = (runs[0][0].lstrip()[1:].lstrip(), runs[0][1], runs[0][2])
            inside = [fp.Para("para", runs, inside[n].page, inside[n].col, 0)] + inside[n + 1:]         # the paragraphs before it are the class's own
    if e.id.rsplit("/", 1)[1] in DC_LISTS:
        fixed = []
        for b in inside:
            hc = fp.head_candidate(b) if b.kind == "para" else None
            if hc and DC_HEAD.search(hc[0]):
                dc = DC_HEAD.search(hc[0]).group(1)
                first = next(r for r in b.runs if r[0].strip())
                b = fp.Para("para", [(DC_HEAD.sub("", hc[0]), first[1], first[2])] + list(hc[1]), b.page, b.col, 0)
                DC_OF[(e.id, fp.namekey(DC_HEAD.sub("", hc[0])))] = dc
            fixed.append(b)
        inside = fixed
    title = fp.Para("title", [(e.title, True, False)], page, 0, 20)
    return [title] + inside, notes


def decisions_file(corpus: Path) -> Path:
    return corpus / "scripts" / "ability-lists-540.decisions.tsv"


def read_decisions(corpus: Path) -> dict[tuple[str, str], tuple[str, str]]:
    """`(entry id, anchor) -> (print|hold, note)`: a hold that a reader has settled against print (a progression in other words, an import paraphrase)."""
    path = decisions_file(corpus)
    return co.read_decisions(path) if path.exists() else {}


def adopt_tables(printed: str, body: str) -> tuple[str, int]:
    """Ruling 62 as the class-option script has it, and for a paragraph that has links outside the rows of the table: the rows run together as one stretch of
    words (no link inside it) are replaced by the table of the corpus."""
    out, n = co.adopt_tables(printed, body)
    if n:
        return out, n
    for tab in co.corpus_tables(body):
        rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in tab if not re.match(r"^\|\s*:?-{3,}", ln)]
        words = " ".join(" ".join(r) for r in rows).split()
        m = re.search(r"\s+".join(re.escape(w) for w in words), printed)
        if m and "](" not in printed[m.start():m.end()]:
            printed = printed[:m.start()].rstrip() + "\n\n" + "\n".join(tab) + "\n\n" + printed[m.end():].lstrip()
            n += 1
    return printed, n


def resolve_missing(corpus: Path, e, rows: list[dict], decisions: dict, loader) -> list[dict]:
    """The items that the cited pages do not print: an item that print has in another source of the entry is read there and written with that book and page in its
    head (owner ruling 32); an item that no owner book prints (an import copy of another class's text, "Relevant text from the warpriest class ability") goes by
    a `drop` decision (ruling 10)."""
    def missing(r):
        return r["status"] == "hold" and r["notes"] and r["notes"][0] == "head not printed"
    for src in (e.data.get("sources") or [])[1:]:
        if not any(missing(r) for r in rows) or loader is None:
            break
        pub, pg = src.get("publication"), str(src.get("page", ""))
        got = loader(pub)
        if got is None or not re.match(r"\d", pg):
            continue
        bk2 = got
        e2 = dataclasses.replace(e, book=pub, page=pg)
        section2, _ = section_for(e2, bk2)
        if not section2:
            continue
        res2 = fp.compare_entry(e2, section2, bk2)
        by_span = {r2["span"]: r2 for r2 in res2["rows"] if r2["span"]}
        for r in rows:
            r2 = by_span.get(r["span"]) if missing(r) else None
            if r2 is not None and not (r2["notes"] and r2["notes"][0] == "head not printed"):
                dec = decisions.get((e.id, r2["anchor"]))
                r.update({k: r2[k] for k in ("print", "status", "head", "notes", "anchor", "level_import", "draft") if k in r2})
                if dec and dec[0] == "print" and r["status"] == "hold":
                    r["status"] = "print"
                    r["notes"].append(f"decision: {dec[1]}")
                r["source"] = (pub, pg)
    for r in rows:
        dec = decisions.get((e.id, r["anchor"]))
        if missing(r) and dec and dec[0] == "drop":
            r["status"], r["drop"] = "print", True
            r["notes"] = [f"dropped: {dec[1]}"]
    return rows


def compare_list(corpus: Path, e, bk, decisions: dict, loader=None) -> dict:
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
    for r in rows:
        if any(n.startswith("dropped table") for n in r["notes"]):
            printed, adopted = adopt_tables(r["print"], e.body)             # ruling 62: the table of the corpus is print's rows, cell by cell
            if adopted:
                only_table = not any(n.startswith(("rule word", "number", "hand review")) for n in r["notes"])
                r["print"] = printed
                r["notes"] = [n for n in r["notes"] if not n.startswith("dropped table")] + ["ruling 62: the table of the corpus is print's rows, cell by cell: kept as a table"]
                if r["status"] == "hold" and only_table:
                    r["status"] = "print"
    key = e.id.rsplit("/", 1)[1]
    if key in PRINT_ONLY:
        for r in rows:
            if not r["span"] and r.get("print", "").strip():
                r["extra"] = True                                           # a printed item that the import lacks: written from print
                r["notes"].append("added from print: the import has no row for it")
                if r["status"] == "hold" and not (r["notes"] and r["notes"][0].startswith("head not printed")):
                    r["status"] = "print"
    probe = {fp.namekey(h) for h in [fp.head_of_para(p) for p in section[1:]] if h}
    _, feats = fp.parse_import(e.body, probe)
    elsewhere: list[str] = []
    if key in ELSEWHERE:
        gone = {fp.squash(fp.ABILITY_TAG.sub("", r["head"])) for r in rows if not r["span"]}
        elsewhere = [r["head"] for r in rows if not r["span"]]
        rows = [r for r in rows if r["span"]]
        kept, skipping = [section[0]], False
        for p in section[1:]:
            hc = fp.head_candidate(p) if p.kind == "para" else None
            if hc:
                skipping = fp.squash(fp.ABILITY_TAG.sub("", hc[0])) in gone              # the paragraphs of an item that other entries hold, up to the next head
            if not skipping:
                kept.append(p)
        section = kept
    if key in DC_LISTS:
        by_span = {f.span_sha(): f for f in feats}
        for r in rows:
            f = by_span.get(r["span"])
            dc = DC_OF.get((e.id, fp.namekey(r["head"])))
            import_dc = next((it.content.strip() for it in (f.items if f else []) if it.label in ("D C", "DC")), "")
            m = re.match(r"number: corpus \[([^\]]*)\]", r["notes"][0]) if r["notes"] else None
            if r["status"] == "hold" and m and dc and import_dc and dc.endswith(import_dc) and set(re.findall(r"'([^']*)'", m.group(1))) <= {import_dc, "non"}:
                r["status"] = "print"
                r["notes"].append("ruling 60: the import's Prereq, Special and D C rows are print's head \"(" + dc + ")\" and its sentences; the DC of the row is the DC of the head")
    for kind, text in OPENING_TYPED.get(key, []):
        if kind == "p" and fp.squash(text) not in CONTEXT_TEXT.get(e.id, ""):
            notes = notes + [f"the typed opening is not found on the cited pages: {text[:50]}..."]
    rows = resolve_missing(corpus, e, rows, decisions, loader)
    problems = [x for x in res["problems"] if not x.startswith("head not printed")]
    unresolved = [r["head"] for r in rows if r["status"] == "hold" and r["notes"] and r["notes"][0] == "head not printed"]
    if unresolved:
        problems.append("head not printed: " + ", ".join(unresolved))
    return {"key": key, "rows": rows, "opening": res.get("opening", []), "opening_links": res.get("opening_links", []), "problems": notes + problems, "section": section,
            "feats": feats, "elsewhere": elsewhere}


def settled(plan: dict) -> bool:
    rows = plan["rows"]
    return bool(rows) and not plan["problems"] and all(r["status"] in ("print", "draft") and (r["span"] or r.get("extra") or is_heading_row(plan, r)) for r in rows) and not any(f.pseudo for f in plan["feats"])


def is_heading_row(plan: dict, r: dict) -> bool:
    """A printed head without text that the entry's list keeps as a heading (`HEADING_TITLES`)."""
    return not r["span"] and not r.get("print", "").strip() and fp.squash(r.get("head", "")) in {fp.squash(x) for x in HEADING_TITLES.get(plan.get("key", ""), set())}


def item_paragraphs(r: dict, dc: str = "", source: str = "") -> list[str]:
    """The written paragraphs of an item: print's first paragraph under the bold run-in label of its head (layout call 1 of 2026-11-27), then the others."""
    paras = [x.strip() for x in r["print"].strip().split("\n\n") if x.strip()]
    head = r["head"].strip().rstrip(":") + (f" ({dc})" if dc else "") + (f" ({source})" if source else "")
    return [f"**{head}:** {paras[0]}"] + paras[1:] if paras else [f"**{head}**"]


def converted_body(e, plan: dict) -> str:
    """The body with each item as a run-in paragraph of print's text and the opening as print has it; the headings of the entry stay where they are."""
    by_span = {r["span"]: r for r in plan["rows"] if r["span"]}
    opening_imp, feats = plan["opening_imp"], plan["feats"]
    out: list[str] = []
    links = list(plan.get("opening_links", []))
    typed = OPENING_TYPED.get(plan["key"])
    if typed:
        for kind, text in typed:
            out.append(text if kind == "p" else f"### {text} {{#{fp.slugify(text)}}}")
    for para in ([] if typed else plan["opening"]):
        if not para.strip():
            continue
        for h in sorted(HEADING_TITLES.get(plan["key"], set())):
            if para.startswith(h + " "):                                 # a heading of the section that the reader joined to the paragraph after it
                out.append(f"### {h} {{#{fp.slugify(h)}}}")
                para = para[len(h):].lstrip()
        para, lost = fp.apply_links(para, links)                         # the links of the import's opening, each placed once
        links = [l for l in links if l[0] in lost]
        out.append(para)
    printed_titles = {fp.squash(p.plain()) for p in plan["section"][1:] if p.kind == "title"} | {fp.squash(x) for x in HEADING_TITLES.get(plan["key"], set())}
    typed_heads = {fp.squash(text) for kind, text in (typed or []) if kind == "h"}

    def keep_heading(b):
        """A heading of the import stays only when print has it (ruling 10); one that the typed opening sets again is not written twice."""
        if not (b and b[0].startswith("#")) or (plan["key"] in INVENTED_HEADINGS and INVENTED_RE.match(b[0])):
            return False
        title = fp.squash(re.sub(r"^#+\s*|\s*\{#[^}]*\}\s*$", "", b[0]))
        return title in printed_titles and title not in typed_heads
    out += ["\n".join(b) for b in opening_imp if keep_heading(b)]
    by_feat = {f.span_sha(): f for f in feats}
    for r in plan["rows"]:
        if r.get("drop"):
            continue
        if r.get("extra"):
            out += item_paragraphs(r, DC_OF.get((e.id, fp.namekey(r["head"])), ""), "")
        elif r["span"]:
            src = f"{fp.publication_title(CORPUS_DIR[0], r['source'][0])} page {r['source'][1]}" if r.get("source") else ""
            out += item_paragraphs(r, DC_OF.get((e.id, fp.namekey(r["head"])), ""), src)
            out += ["\n".join(b) for b in by_feat[r["span"]].raw[1:] if keep_heading(b)]
        elif is_heading_row(plan, r):
            out.append(f"### {r['head'].strip()} {{#{fp.slugify(r['head'])}}}")
    # the corrections of `scripts/errata.tsv` that the entry keeps (a misprint of print, owner ruling 43) are written as corrected
    return co.apply_fixes("\n\n".join(out) + "\n", co.errata_fixes(CORPUS_DIR[0], e.id))


def entry_heads(body: str) -> list[str]:
    """The heads of the written items: the bold run-in labels at the start of a paragraph, without their "(DC n)" and "(Book page n)"."""
    heads = re.findall(r"^\*\*([^*\n]{2,80}?):\*\*", body, re.M)
    return [re.sub(r"\s*\((?:DC \d+|[^()]* page \d+)\)", "", h) for h in heads]


# Printed heads after the last item of a list that are no items of it: the next features of a class chapter (the lists that print sets inside one), or other sections.
TRAILING_OK = {"judgments", "animal-foci", "capstones", "gunslinger-renowned-deeds", "swashbuckler-renowned-deeds", "outer-rifts-exploits", "advanced-weapon-training"}


def head_problems(printed: list[str], entry: list[str], elsewhere: int, trailing: list[str]) -> list[str]:
    """The heads of the printed section against the items of the entry: each printed head has an item (but as many as `elsewhere`), each item has a printed head, and
    no printed head follows the last item."""
    names = {fp.squash(fp.ABILITY_TAG.sub("", h)) for h in entry}
    printed_keys = {fp.squash(fp.ABILITY_TAG.sub("", h)) for h in printed}
    problems = []
    absent = [h for h in printed if fp.squash(fp.ABILITY_TAG.sub("", h)) not in names]
    if len(absent) != elsewhere:
        problems.append(f"{len(absent)} printed heads have no item in the entry, {elsewhere} are expected elsewhere: " + ", ".join(absent))
    invented = [h for h in entry if fp.squash(fp.ABILITY_TAG.sub("", h)) not in printed_keys]
    if invented:
        problems.append("items of the entry that the printed section lacks: " + ", ".join(invented[:10]))
    if trailing:
        problems.append("printed heads after the last item of the section: " + ", ".join(trailing[:10]))
    return problems


def printed_opening(e, bk, names: set[str]) -> str:
    """The printed paragraphs over the first item of the list, read from the page before the cited ones too (the section of a list can start on an earlier page than
    the one that the row cites): back from the first item over the paragraphs without a head of their own, up to a title or the head of another feature; the head of
    the lead feature (`OPENING_LEAD`) gives its text to the opening."""
    key = e.id.rsplit("/", 1)[1]
    if key in OPENING_TYPED:
        return ""
    nums = [int(x) for x in re.findall(r"\d+", e.page)] or [0]
    lo, hi = min(nums + [PAGE_START.get(key, min(nums))]), max(nums) + 1 + EXTRA_PAGES.get(key, 0)
    blocks = [b for b in fp.read_blocks(bk, max(1, lo - 3), min(hi + 4 + fp.PAGE_OFFSET[0], max(bk.pages))) if lo - 1 <= b.page <= hi]
    if key in IN_CLASS_TABLE:
        blocks = table_clean(blocks, cl.table_tail((corpus_dir() / "entries" / (IN_CLASS_TABLE[key].removeprefix("ref/") + ".md")).read_text(encoding="utf-8")))
    first = next((n for n, b in enumerate(blocks) if b.kind == "para" and (hc := fp.head_candidate(b)) and fp.squash(fp.ABILITY_TAG.sub("", re.sub(DC_HEAD, "", hc[0]))) in names), None)
    if first is None:
        return ""
    out: list[str] = []
    n = first - 1
    while n >= 0 and blocks[n].kind == "para":
        hc = fp.head_candidate(blocks[n])
        if hc and hc[2]:
            lead = OPENING_LEAD.get(key)
            if lead and fp.squash(fp.ABILITY_TAG.sub("", hc[0])) == fp.squash(lead):
                out.insert(0, " ".join("".join(x[0] for x in hc[1]).lstrip(": ").split()))
            break
        out.insert(0, " ".join(blocks[n].plain().split()))
        n -= 1
    return " ".join(out)


def inventory(e, bk, body: str) -> list[str]:
    """The check that every printed item head and the opening of the list are in the entry (review of #379, 2026-11-27): the heads of the printed section that the
    entry has no item for must be as many as the review found elsewhere (`ELSEWHERE_COUNT`); the entry has no item that print lacks; the printed heads after the last
    item are no more items; the paragraphs over the first printed item stand in the opening of the entry."""
    key = e.id.rsplit("/", 1)[1]
    names = {fp.squash(fp.ABILITY_TAG.sub("", h)) for h in entry_heads(body)}
    section, notes = section_for(e, bk, names)
    if not section:
        return [f"no section found ({'; '.join(notes)})"]
    problems: list[str] = []
    printed = []
    for p in section[1:]:
        hc = fp.head_candidate(p) if p.kind == "para" else None
        if hc:
            printed.append(re.sub(DC_HEAD, "", fp.ABILITY_TAG.sub("", hc[0])).strip())
    problems += head_problems(printed, entry_heads(body), ELSEWHERE_COUNT.get(key, 0), [] if key in TRAILING_OK else TRAILING.get(e.id, []))
    for kind, text in OPENING_TYPED.get(key, []):
        if kind == "p" and fp.squash(text) not in fp.squash(body):
            problems.append(f"the typed opening is not in the entry: {text[:60]}...")
        if kind == "p" and fp.squash(text) not in CONTEXT_TEXT.get(e.id, ""):
            problems.append(f"the typed opening is not on the cited pages: {text[:60]}...")
    opening = printed_opening(e, bk, names)
    if opening:
        before = body.split("\n**", 1)[0] if "\n**" in body else body
        lost = print_lost(opening, before, co.errata_fixes(CORPUS_DIR[0], e.id))           # the corrections of the errata file are no loss
        if lost:
            problems.append(f"the opening over the first item lacks {len(lost)} printed sentences: " + " | ".join(x[:80] for x in lost[:3]))
    return problems


def coverage(plan: dict, new_body: str) -> list[str]:
    """Print sentences of the section that the written body lacks."""
    cuts = [m for (i, _a), m in CUT_AT.items() if i == plan.get("key")]
    paras = []
    for p in plan["section"][1:]:
        if p.kind != "para":
            continue
        text = " ".join("".join(x[0] for x in p.runs).split())
        hit = next((m for m in cuts if m in text), None)
        if hit:                                                       # the text layer joined the next section to this paragraph: it and what follows are not this list's
            paras.append(text[:text.index(hit)])
            break
        paras.append(text)
    printed = " ".join(paras)
    return print_lost(printed, re.sub(r"\s*\(DC \d+\):", ":", new_body), co.errata_fixes(CORPUS_DIR[0], f"ref/ability/{plan['key']}"))           # the "(DC n)" of a head is set back into it when written; the section was read without it


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    CORPUS_DIR[0] = corpus
    ids = args.ids.split(",") if args.ids else None
    books: dict[str, object] = {}
    total, written = Counter(), 0
    decisions = read_decisions(corpus)
    for e in load_lists(corpus, ids):
        if co.shape_of(e.body)[0] == "none":
            print(f"{e.id}: written already (a bold-lead item is no import row): skipped; `--audit` checks it against print")
            continue                                                  # a rerun is a no-op: the writer reads import rows, never its own paragraphs
        fp.configure_book(e.book)
        if e.book not in books:
            pdf = fp.find_pdf(Path(args.books), fp.publication_title(corpus, e.book))
            books[e.book] = fp.load_book(fp.book_xml(pdf, Path(args.cache))) if pdf else None
        bk = books[e.book]
        if bk is None:
            print(f"{e.id}: no copy of {e.book}")
            continue
        def loader(pub, e=e):
            if pub not in books:
                pdf2 = fp.find_pdf(Path(args.books), fp.publication_title(corpus, pub))
                fp.configure_book(pub)
                books[pub] = fp.load_book(fp.book_xml(pdf2, Path(args.cache))) if pdf2 else None
            fp.configure_book(pub)
            return books[pub]
        plan = compare_list(corpus, e, bk, decisions, loader)
        fp.configure_book(e.book)
        plan["opening_imp"] = fp.parse_import(e.body, set())[0]
        c = Counter(r["status"] for r in plan["rows"])
        total.update(c)
        pages = sorted({b.page for b in plan["section"][1:] if isinstance(b.page, int)})
        if pages:
            print(f"    printed pages of the section: {pages[0]}-{pages[-1]} (row: {e.page})")
        print(f"{e.id} ({e.book} p. {e.page}): section {len(plan['section'])} blocks; " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())) + "; problems: " + "; ".join(plan["problems"])[:200])
        for r in plan["rows"]:
            if r["status"] == "hold":
                print(f"    hold {r['head'][:30]}: {(r['notes'] or [''])[0][:110]}")
        if settled(plan):
            new = converted_body(e, plan)
            lost = coverage(plan, new)
            inv = inventory(e, bk, new)
            fp.configure_book(e.book)
            if inv:
                print("    held by the inventory check: " + " | ".join(x[:200] for x in inv))
                lost = lost or ["inventory"]
            elif lost:
                print(f"    held by the coverage check ({len(lost)}): " + " | ".join(x[:70] for x in lost[:3]))
            elif args.write:
                co.write_atomic(e.path, "+++\n" + fixed_front(e).strip("\n") + "\n+++\n\n" + new)
                written += 1
                print("    written")
    print("total: " + ", ".join(f"{k} {v}" for k, v in sorted(total.items())) + (f"; {written} lists written" if args.write else ""))
    if args.write and written and args.checker:
        import subprocess
        subprocess.run([args.checker, "fmt", str(corpus)], check=True)
    return 0


def run_audit(args) -> int:
    """The print-coverage check over the lists that are written already (read only): the printed section of each, read again from the pages with the heads of the
    written items, against the entry's body. Prints the sentences that the check holds."""
    corpus = Path(args.corpus).resolve()
    CORPUS_DIR[0] = corpus
    books: dict[str, object] = {}
    held = n = 0
    for e in load_lists(corpus, args.ids.split(",") if args.ids else None):
        if co.shape_of(e.body)[0] != "none":
            continue                                                  # not written yet
        fp.configure_book(e.book)
        if e.book not in books:
            pdf = fp.find_pdf(Path(args.books), fp.publication_title(corpus, e.book))
            books[e.book] = fp.load_book(fp.book_xml(pdf, Path(args.cache))) if pdf else None
        heads = re.findall(r"^\*\*([^*\n]{2,80}?):\*\*", e.body, re.M)
        key = e.id.rsplit("/", 1)[1]
        names = {fp.squash(re.sub(r"\s*\((?:DC \d+|[^()]* page \d+)\)", "", fp.ABILITY_TAG.sub("", h))) for h in heads}
        section, notes = section_for(e, books[e.book], names)
        n += 1
        if not section:
            print(f"{e.id}: no section found ({'; '.join(notes)})")
            continue
        kept, skipping = [], False
        for p in section[1:]:
            hc = fp.head_candidate(p) if p.kind == "para" else None
            if hc and key in ELSEWHERE:
                skipping = fp.squash(re.sub(r"\s*\(DC \d+\)", "", fp.ABILITY_TAG.sub("", hc[0]))) not in names
            if not skipping:
                kept.append(p)
        plan = {"key": key, "section": [section[0]] + kept}
        lost = coverage(plan, e.body)
        inv = inventory(e, books[e.book], e.body)
        if inv:
            held += 1
            print(f"{e.id} ({e.book} p. {e.page}): the inventory of heads and opening is not met")
            for x in inv:
                print("    " + x[:4000])
        if lost:
            held += 1
            print(f"{e.id} ({e.book} p. {e.page}): {len(lost)} printed sentences that the entry lacks")
            for s in lost[:5]:
                print("    " + s[:240])
    print(f"audit of the written lists: {n} read, {held} held by the check")
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
    eq(item_paragraphs({"head": "Aid", "print": "The animal helps."}, "DC 20"), ["**Aid (DC 20):** The animal helps."], "the DC of a head is set back into it")
    eq(item_paragraphs({"head": "Warrior Spirit (Su)", "print": "x."}, "", "Magic Tactics Toolbox page 10"), ["**Warrior Spirit (Su) (Magic Tactics Toolbox page 10):** x."],
       "an item that another owner book prints names that book and page (ruling 32)")
    eq(DC_HEAD.sub("", "Build Simple Structure (DC 25)"), "Build Simple Structure", "the DC is no part of the name")
    P = fp.Para
    cleaned = table_clean([P("title", [("Table 2-1: Inquisitor", True, False)], 1, 0, 24), P("para", [("Smiting: ends for the", False, False)], 1, 0),
                           P("para", [("Base Attack Fort Ref Will Level Bonus Save Save Save Special 1st +0 +2 +0 +2 Domain 20th +15/+10/+5 +12 +6 +12 True judgment purpose of overcoming (but not hardness).", True, False)], 1, 0)], "True judgment")
    eq([b.plain() for b in cleaned], ["Smiting: ends for the purpose of overcoming (but not hardness)."], "the class table that the text layer runs into a list is cut, the sentence it broke is joined")
    rows = [{"anchor": "a", "status": "hold", "notes": ["head not printed"], "span": "s", "head": "A", "print": ""}]
    eq(resolve_missing(Path("."), type("E", (), {"id": "ref/ability/x", "data": {}})(), rows, {("ref/ability/x", "a"): ("drop", "an import copy")}, None)[0]["drop"], True, "an item that no owner book prints goes by a drop decision (ruling 10)")
    eq(sorted(set(OPENING_TYPED) - {"capstones"}), sorted(INVENTED_HEADINGS), "the two renowned-deed lists have a typed opening and drop the import's level headings")
    eq(head_problems(["Aid", "Bombard", "Cocoon"], ["Aid", "Cocoon"], 0, []), ["1 printed heads have no item in the entry, 0 are expected elsewhere: Bombard"],
       "a printed head without an item holds the list (the 15 missing tricks of Companion Tricks)")
    eq(head_problems(["Aid", "Bombard"], ["Aid"], 1, []), [], "a printed head that another entry holds is counted by the review, not found by the check")
    eq(head_problems(["Aid"], ["Aid", "Fetch"], 0, []), ["items of the entry that the printed section lacks: Fetch"], "an item that print lacks holds the list")
    eq(head_problems(["Aid"], ["Aid"], 0, ["Watch"]), ["printed heads after the last item of the section: Watch"], "a printed head after the last item holds the list")
    eq(head_problems(["Aid (Su)"], ["Aid"], 0, []), [], "a tag of the ability is no part of the name")
    eq(entry_heads("**Aid (DC 20):** x\n\n**Warrior Spirit (Su) (Magic Tactics Toolbox page 10):** y\n\nplain: no"), ["Aid", "Warrior Spirit (Su)"], "the heads of the written items")
    eq(co.shape_of("+++\n+++\n\n**Aid (DC 20):** The animal helps.\n\n**Fetch (DC 15):** It fetches.\n")[0], "none", "a written list has no import row: a rerun skips it")
    eq(INVENTED_RE.match("### 11-Level Renowned Deed") is not None and INVENTED_RE.match("### 1st-Level Renowned Deed") is not None, True, "the import's level headings go with or without an ordinal suffix")
    eq(INVENTED_RE.match("### Gunslinger Renowned Deeds") is None, True, "the printed heading stays")
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
    ap.add_argument("--audit", action="store_true", help="the print-coverage check over the written lists (read only)")
    ap.add_argument("--ids")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--checker")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.audit:
        return run_audit(args)
    if args.compare:
        return run_compare(args)
    ap.error("one of --self-test, --compare")


if __name__ == "__main__":
    sys.exit(main())
