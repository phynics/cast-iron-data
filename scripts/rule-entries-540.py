#!/usr/bin/env python3
"""The 33 rule entries of the rewrite, and the entries that stand beside them (phynics/cast-iron#540, the rule-entry rulings of 2026-11-24).

    rule-entries-540.py --self-test
    rule-entries-540.py [CORPUS] --check                 # CI: the corruption labels, the copies, the incidental rows (no PDF)
    rule-entries-540.py [CORPUS] --corruptions [--write] [--texts DIR]
    rule-entries-540.py [CORPUS] --copies [--write]

What it does
------------
1. **The 16 corruptions** (ruling 4): the labels that print has. The import wrote `**Flavor:**`, `**Details:**` and `**Prereq:**` rows that print
   does not have: the flavour line of a manifestation is printed with no label, a stage is the run-in "Corruption Stage 1: Once you feed ...", and a
   prerequisite line is printed "Prerequisites: ..." (or "Prerequisite: ..." with one item). `--corruptions` rewrites those labels in place (the
   text stays; nothing but the labels changes); with `--texts DIR` (the text of each book, `DIR/<publication>.txt`, from a copy of the book) the
   singular or plural of the prerequisite label is the printed one, else it is decided by the number of items and listed.
2. **The 11 class chapters and the 6 medium spirits** (ruling 1): each rule entry is a copy of its converted parent (the base class, the
   `ref/spirit/*` class option). `--copies` reports each pair, and with `--write` copies the parent's body when the parent is converted (a class
   option is converted when its ledger row is `written`; a base class when it has no import row left). `--check` fails when a copy's body hash
   differs from the converted parent's body. A parent that is not converted yet is reported, not an error.
3. **The incidental rows** (ruling 3): the invented row `**Action:** Trick` of `ref/ability/companion-tricks`, and the pages of the entries whose
   cited page is not the printed page that print has the stray row on (only `high-rp-types`: the other two cite the printed pages already).
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import tempfile
import tomllib
from pathlib import Path

CORRUPTIONS = [
    "ref/rule/accursed", "ref/rule/deep-one", "ref/rule/ghoul", "ref/rule/hellbound", "ref/rule/hive", "ref/rule/lich", "ref/rule/lycanthropy",
    "ref/rule/possessed", "ref/rule/promethean", "ref/rule/shadowbound", "ref/rule/vampirism", "ref/rule/aboleth", "ref/rule/demonic",
    "ref/rule/plagued", "ref/rule/amoral", "ref/rule/psychometabolic",
]
CLASSES = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "wizard"]
SPIRITS = ["archmage", "champion", "guardian", "hierophant", "marshal", "trickster"]
# (entry id, the page that its cited page row held, the page it must read, the book): print has the stray row of `high-rp-types` on printed p. 215 of the
# Advanced Race Guide. The other two rows were checked against the footers and are right as they stand: the heading and first paragraph of `grapple` are
# on printed p. 199 of the Core Rulebook (PDF page 200), and those of `advanced-actions` on printed p. 105 of Pathfinder Unchained (PDF page 106).
PAGE_FIXES = {
    "ref/rule/high-rp-types": ("217", "215", "Advanced Race Guide"),
    "ref/rule/grapple": ("199", "199", "Core Rulebook"),
    "ref/rule/advanced-actions": ("105", "105", "Pathfinder Unchained"),
}
INVENTED_ROW = ("ref/ability/companion-tricks", "**Action:** Trick")

STAGE = re.compile(r"^\*\*Corruption Stage (\d+)\*\*\n\n\*\*Details:\*\* ", re.M)
FLAVOR = re.compile(r"^\*\*Flavor:\*\* ", re.M)
PREREQ = re.compile(r"^\*\*Prereq:\*\* ", re.M)
OLD_LABELS = re.compile(r"^\*\*(?:Flavor|Details|Prereq):\*\*", re.M)


def split_entry(text: str) -> tuple[str, str]:
    front, _, body = text.partition("\n+++\n")
    return front + "\n+++\n", body


def printed_labels(book_text: str | None, name: str) -> str | None:
    """"Prerequisite" or "Prerequisites": the label that print sets under the manifestation `name` (its own line, then at most four lines to the
    prerequisite line), or None when the text has no such manifestation."""
    if not book_text:
        return None
    fold = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())             # the text layer breaks words ("T ransformation") and quotes
    raw = book_text.split("\n")
    lines = [fold(x) for x in raw]
    want = fold(name)
    for i, ln in enumerate(lines):
        if raw[i].rstrip().endswith((".", ",", "*", ":")):
            continue                                               # a mention in a prerequisite list, not the name of a manifestation
        if ln == want or (i + 1 < len(lines) and ln + lines[i + 1] == want):              # a name that wraps over two lines
            for nxt in raw[i + 1:i + 7]:
                m = re.match(r"^\s*(Prerequisites?):", nxt)
                if m:
                    return m.group(1)
    return None


def fix_corruption(body: str, book_text: str | None = None) -> tuple[str, list[str]]:
    """The body with the labels of print: no `Flavor:` label, a stage as a run-in, `Prerequisite(s):` for `Prereq:`. Returns the body and the notes
    of what was decided without print (the singular or plural of a prerequisite label)."""
    notes: list[str] = []
    body = STAGE.sub(lambda m: f"**Corruption Stage {m.group(1)}:** ", body)
    body = FLAVOR.sub("", body)
    out, name = [], ""
    for para in body.split("\n\n"):
        first = para.split("\n", 1)[0]
        if re.fullmatch(r"\*\*[^*:]+\*\*", first.strip()) and not first.startswith("**Corruption Stage"):
            name = first.strip()[2:-2]
        if PREREQ.match(para):
            label = printed_labels(book_text, name)
            if label is None:
                items = re.split(r",\s*(?![^()]*\))", re.sub(r"^\*\*Prereq:\*\*\s*", "", para.split("\n\n")[0]).replace("\n", " "))
                label = "Prerequisites" if len(items) > 1 else "Prerequisite"
                notes.append(f"{name}: label {label} decided by the number of items")
            para = PREREQ.sub(f"**{label}:** ", para, count=1)
        out.append(para)
    return "\n\n".join(out), notes


def entry_path(corpus: Path, eid: str) -> Path:
    return corpus / "entries" / (eid.removeprefix("ref/") + ".md")


def first_source(text: str) -> str:
    return tomllib.loads(split_entry(text)[0].split("+++\n", 1)[1].rsplit("+++", 1)[0])["sources"][0]["publication"]


def run_corruptions(corpus: Path, write: bool, texts: Path | None) -> int:
    changed = 0
    for eid in CORRUPTIONS:
        p = entry_path(corpus, eid)
        text = p.read_text(encoding="utf-8")
        front, body = split_entry(text)
        book = texts / f"{first_source(text)}.txt" if texts else None
        new, notes = fix_corruption(body, book.read_text(encoding="utf-8") if book and book.exists() else None)
        if new != body:
            changed += 1
            if write:
                p.write_text(front + new, encoding="utf-8")
        for n in notes:
            print(f"  {eid}: {n}")
    print(f"corruptions: {changed} of {len(CORRUPTIONS)} entries {'rewritten' if write else 'would change'}")
    return 0


# ---- the copies ------------------------------------------------------------------------------------

def body_hash(text: str) -> str:
    return hashlib.sha256(split_entry(text)[1].strip().encode("utf-8")).hexdigest()


def pairs() -> list[tuple[str, str]]:
    """(copy, parent): the rule entry and the entry that it copies."""
    return ([(f"ref/rule/class-{c}/{c}", f"ref/class/{c}") for c in CLASSES] + [(f"ref/rule/spirit-{s}/{s}", f"ref/spirit/{s}") for s in SPIRITS])


def converted(corpus: Path, eid: str) -> bool:
    """Whether the parent is converted: a base class has no import row left; a class option is `written` in a ledger of `scripts/class-options/`."""
    p = entry_path(corpus, eid)
    if not p.exists():
        return False
    if eid.startswith("ref/spirit/"):
        for tsv in (corpus / "scripts" / "class-options").glob("540-*.tsv"):
            for ln in tsv.read_text(encoding="utf-8").split("\n")[1:]:
                f = ln.split("\t")
                if f and f[0] == eid and "written" in f:
                    return True
        return False
    return not IMPORT_ROW.search(split_entry(p.read_text(encoding="utf-8"))[1])


IMPORT_ROW = re.compile(r"^\*\*(?:Gained|Passive|Ability|Ability2|Standard|Move|Swift|Immediate|Free|Fullround|Action|At \d+(?:st|nd|rd|th) Level):\*\*", re.M)


def run_copies(corpus: Path, write: bool) -> tuple[int, list[str]]:
    errors: list[str] = []
    ready = 0
    for copy, parent in pairs():
        cp, pp = entry_path(corpus, copy), entry_path(corpus, parent)
        if not cp.exists() or not pp.exists():
            errors.append(f"{copy}: the copy or its parent {parent} is missing")
            continue
        if not converted(corpus, parent):
            print(f"  {copy}: the parent {parent} is not converted yet")
            continue
        ready += 1
        ptext, ctext = pp.read_text(encoding="utf-8"), cp.read_text(encoding="utf-8")
        if body_hash(ptext) != body_hash(ctext):
            if write:
                cp.write_text(split_entry(ctext)[0] + split_entry(ptext)[1], encoding="utf-8")
            else:
                errors.append(f"{copy}: the body differs from the converted body of {parent}")
    print(f"copies: {len(pairs())} pairs, {ready} with a converted parent")
    return ready, errors


# ---- the check -------------------------------------------------------------------------------------

def run_check(corpus: Path) -> int:
    errors: list[str] = []
    for eid in CORRUPTIONS:
        p = entry_path(corpus, eid)
        body = split_entry(p.read_text(encoding="utf-8"))[1]
        for m in OLD_LABELS.finditer(body):
            errors.append(f"{eid}: the label {m.group(0)} is not print's")
        if re.search(r"^\*\*Corruption Stage \d+\*\*$", body, re.M):
            errors.append(f"{eid}: a corruption stage is not a run-in")
    eid, row = INVENTED_ROW
    if row in entry_path(corpus, eid).read_text(encoding="utf-8"):
        errors.append(f"{eid}: the invented row {row} is still there")
    for eid, (_old, new, _book) in PAGE_FIXES.items():
        front = split_entry(entry_path(corpus, eid).read_text(encoding="utf-8"))[0]
        pages = re.findall(r'^page = "([^"]*)"', front, re.M)
        if not pages or pages[0] != new:
            errors.append(f"{eid}: the page row reads {pages[:1]}, print has the row on {new}")
    _, copy_errors = run_copies(corpus, False)
    errors += copy_errors
    for e in errors:
        print("error:", e)
    return 1 if errors else 0


# ---- self-test -------------------------------------------------------------------------------------

def self_test() -> int:
    ok, bad = 0, []

    def eq(a, b, what):
        nonlocal ok
        if a == b:
            ok += 1
        else:
            bad.append(f"{what}: {a!r} != {b!r}")

    body = ("Intro.\n\n### Progression\n\nEat.\n\n**Corruption Stage 1**\n\n**Details:** Once you feed, you shift.\n\n**Corruption Stage 2**\n\n**Details:** Again.\n\n"
            "### Manifestations\n\n**Brain Eater**\n\n**Flavor:** Devouring brains imparts knowledge to you.\n\n**Prereq:** Manifestation level 5th, gnashing bite\n\n"
            "**Gift:** You gain a bonus.\n\n**Claws**\n\n**Flavor:** Claws.\n\n**Prereq:** Manifestation level 4th\n\n**Gift:** Claws grow.\n")
    new, notes = fix_corruption(body)
    eq("**Corruption Stage 1:** Once you feed, you shift." in new and "**Corruption Stage 2:** Again." in new, True, "ruling 4: a stage is the run-in of print")
    eq("**Flavor:**" in new or "**Details:**" in new, False, "ruling 4: no Flavor and no Details label")
    eq("**Brain Eater**\n\nDevouring brains imparts knowledge to you.\n\n**Prerequisites:** Manifestation level 5th, gnashing bite" in new, True, "ruling 4: the flavour line has no label, Prereq is Prerequisites")
    eq("**Prerequisite:** Manifestation level 4th" in new, True, "ruling 4: one item is Prerequisite when print is not read")
    eq(len(notes), 2, "the labels decided without print are listed")
    printed = "Brain Eater\nDevouring brains.\nPrerequisites: Manifestation level 5th, gnashing bite*.\nClaws\nClaws.\nPrerequisites: Manifestation level 4th.\n"
    new2, notes2 = fix_corruption(body, printed)
    eq(("**Prerequisites:** Manifestation level 4th" in new2, notes2), (True, []), "ruling 4: the label of print wins over the count of items")
    eq(fix_corruption(new)[0], new, "ruling 4: the rewrite is idempotent")
    eq(printed_labels(printed, "Claws"), "Prerequisites", "the printed label under a manifestation")
    eq(printed_labels(printed, "Nothing"), None, "a manifestation that print does not have")
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        for eid, txt in (("ref/class/fighter", "+++\nid = \"x\"\n+++\n\n#### Bravery {#bravery}\n\nAt 2nd level, a fighter.\n"),
                         ("ref/rule/class-fighter/fighter", "+++\nid = \"y\"\n+++\n\n**Bravery**\n\n**Passive:** At 2nd level.\n")):
            p = entry_path(root, eid)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(txt)
        eq(converted(root, "ref/class/fighter"), True, "a base class with no import row is converted")
        pp = entry_path(root, "ref/class/barbarian")
        pp.parent.mkdir(parents=True, exist_ok=True)
        pp.write_text("+++\nid = \"z\"\n+++\n\n**Rage**\n\n**Passive:** x\n")
        eq(converted(root, "ref/class/barbarian"), False, "a base class with import rows is not converted")
        cp, pp2 = entry_path(root, "ref/rule/class-fighter/fighter"), entry_path(root, "ref/class/fighter")
        eq(body_hash(cp.read_text()) == body_hash(pp2.read_text()), False, "a copy that differs has another hash")
        cp.write_text(split_entry(cp.read_text())[0] + split_entry(pp2.read_text())[1])
        eq(body_hash(cp.read_text()) == body_hash(pp2.read_text()), True, "a copy of the converted body has the same hash")
    for line in bad:
        print("FAIL", line)
    print(f"self-test: {ok} checks passed" if not bad else f"self-test: {len(bad)} failures")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--corruptions", action="store_true")
    ap.add_argument("--copies", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--texts")
    args = ap.parse_args()
    corpus = Path(args.corpus).resolve()
    if args.self_test:
        return self_test()
    if args.corruptions:
        return run_corruptions(corpus, args.write, Path(args.texts) if args.texts else None)
    if args.copies:
        _, errors = run_copies(corpus, args.write)
        for e in errors:
            print("error:", e)
        return 1 if errors else 0
    if args.check:
        return run_check(corpus)
    ap.error("one of --self-test, --check, --corruptions, --copies")


if __name__ == "__main__":
    sys.exit(main())
