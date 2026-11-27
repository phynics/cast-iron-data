#!/usr/bin/env python3
"""Rewrite archetype features as headed printed prose (phynics/cast-iron#540).

The import wrote an archetype feature as a bold name, then rows: `**Gained:**`, an effect label
(`**Passive:**`, `**Standard:**`, ...), `**Replaces:**`, invented `At Nth level:` upgrade rows. The book
prints it as one paragraph: "Shattering Strike (Ex): At 2nd level, a two-handed fighter gains ... This
ability replaces bravery." Owner decision of 2026-11-24 (form B, corpus format 4): a feature is a headed
section of printed prose, and the facts that the prose states are in `[fields]`:

    features = [{ anchor = "shattering-strike", level = 2 }, { anchor = "weapon-training" }]
    trades   = [{ replaces = "Bravery", feature = "bravery", by = ["shattering-strike"] }]

The contract of this script (spec: `docs/corpus-format.md`, "Feature facts", of phynics/cast-iron):

* `features` lists the feature headings in body order, after `kind` (archetype). Every feature heading
  has an explicit `{#anchor}` (the slug of its name without the ability tag). `level` is written only
  when print proves it: the first paragraph opens with "At / Starting at / Beginning at Nth level", or
  every trade of the feature (and no other feature) names one level.
* A trade gets `by`, the list of feature anchors whose printed text states it, in body order, or no
  `by` when the book prints the trade in the opening text. `replaces`, `alters` and the other trade keys
  stay as they are.
* Headings that print a label only (a trailing "Rogue Talents" list) stay plain headings: never listed
  in `features`, never trade targets. Scaffold headings (`SCAFFOLD`) are never listed.
* The body is the printed prose: the printed paragraphs, the printed "This ability replaces ..."
  sentence, no invented rows, subheads or action labels. The opening text stays as it is.

Text source. The rule draft is built from the import rows (level lead, effect, action phrase, upgrade
rows). The print text comes from the owner's copy of the book (`--compare`). Per feature:

  draft   the draft and print agree word for word (tolerance below)
  print   they differ only in wording (person, articles, order, punctuation, ligature spaces): the
          printed paragraph is taken
  hold    they differ in a number or a rule word (owner ruling 3 of 2026-11-24: held for an errata
          check, not written), or the print structure does not match the entry (an invented or a
          dropped feature head), or the entry's trades disagree with the printed trade sentences
  edit    a hand-written text in the proposals file (the compare never overwrites it)

An entry is converted all or nothing, and only when every feature row has the status `draft`, `print`
or `edit`. A converted entry has `features`, and the script skips it afterwards, so the output is a
fixed point.

Usage
-----
    feature-prose-540.py --self-test
    feature-prose-540.py --check   [CORPUS] [--book ID]   no PDF needed: exit 1 unless a rerun changes nothing
    feature-prose-540.py --compare [CORPUS] --book ID --books DIR --cache DIR [--only ID-PREFIX]
                                                          fill the review TSV and the proposals from print
    feature-prose-540.py --print-sentences [CORPUS] --book ID --books DIR --cache DIR
                                                          write `<book>.sentences.tsv`: the printed "This replaces/alters ..." sentences
                                                          of every archetype; `--check` fails when the entry lacks one
    feature-prose-540.py --write   [CORPUS] [--book ID] [--checker BIN] [--only ID-PREFIX]
                                                          convert the entries whose rows are all decided

`--compare` reads the PDF of the book (found by the words of its title in `--books`, searched
recursively) with `pdftohtml -xml` (poppler; its bold and italic runs tell heads from running text) and
caches the XML in `--cache`, named by the SHA-256 of the PDF. Neither the PDF, its file name nor the
extracted text are stored in the repository: the TSV and the proposals record the book title and the
printed page only. The printed page of a PDF page is read from its footer.

Advanced Class Guide and Advanced Race Guide (batch 2). The owner's copy of the Advanced Class Guide is the 1st printing:
`ERRATA`, `ERRATA_FEATURES` and `ERRATA_ADDED` apply the Paizo errata that brings it to the 2nd printing, and
`scripts/errata.tsv` has a row for each change (phynics/cast-iron-data#309). Small type after a name (a source-book
abbreviation such as "UM" or a dagger) is a cross-reference mark and is left out. In the Advanced Race Guide a table or a
sidebar of the race chapter can stand on the page of an archetype: its sans-serif cells and its box title are not the text of
the archetype (`SKIP_TABLES`). Printed cross-references ("(see below)", "(Core Rulebook 178)") stay (owner ruling 16), as
do asterisks when the page prints their key.

`--write` leaves long lines: run `cast-iron-corpus fmt <corpus>` after it. With `--checker BIN` (the
`cast-iron-corpus` binary) it also runs `check` on the result, puts back every entry that the check
rejects, and records the reason as a `hold`.

Campaign Setting books (Inner Sea Magic, Inner Sea Intrigue, Inner Sea Combat; the batch of the three, phynics/cast-iron#540). Their pages
set the columns at other margins on odd and even pages (`PAGE_GEOMETRY`: the margins of a page are the commonest left edges of its body
lines), run a chapter tab along the outer margin (dropped) and an illustration's caption in large type (`MARGIN_CAPTIONS`, `CAPTIONS`: a
title that repeats an archetype's name is no title), set boxes in a column that break a sentence (`BOX_TITLES`: read apart and set behind
the section), print bullet lists (`BULLETS`: a line that starts with a bullet starts a Markdown list item) and wrap text around art (a line
that starts in lower case continues the sentence, `LOWERCASE_CONTINUES`). Inner Sea Combat is a scan whose OCR layer has no bold or italic runs
(`NO_STYLE`: a head is told by its shape, `styled_head`) and a few systematic misreadings (`OCR_WORDS`, `OCR_PHRASES`, `ocr_repair`: "ist" for
1st, "13" for g, a soft hyphen for the hyphen of a line end, a lost "or" at a line end), and its italics are listed (`OCR_ITALICS`). The page
images were read for every archetype of that book.

Hold rules (owner decision of 2026-11-26, phynics/cast-iron#540; each is a switch of `RULES`, and `--rules` and
`scripts/feature-prose-540-measure.py` turn them off to count what each does)
-----
  values    values level by level: the corpus's fraction of the level ("1 + one-fourth of her level") or its upgrade rows, against the
            table that print states ("At Kth level and every N levels thereafter ... increases by S", "increases to +4 at 5th level, and
            +6 at 8th level"); a base value counts; a hold only when a value differs or a step is on one side only
  hyphens   a hyphen is a space when words are compared ("mind-affecting", "1st-detect", "brown-fur"); "full-round" stays one word
  prereq    `Prereq: 13th-level magus ...` is print's "The magus must be at least 13th level ..." when the level is the same
  usage     a `Usage` row whose words are in print in order is print's
  dropped   a corpus table that the print span lacks is a hold; so is a print span that ends at a title no rule names as another section
            of the book (a table title, a box): the entry needs a decision (`sidebar`, `drop`, `print`) or an edit
  choices   a listed feature whose text says that the reader selects from what follows ("can select an edge from those listed below",
            "can select from any of the following hexes") and whose next section is a listed feature too: the sections are probably its
            options (owner rulings 15 and 34, review of #338); a hold until a decision on the feature (`list`: they are features) or on the
            options (`sub-of:`) settles it
  lostlevel the import had a level (`Gained`) and the converted feature has none: a hold until a decision on the feature says that print
            gives no level (owner ruling 4)
  and `--print-sentences` / `<book>.sentences.tsv`: the printed "This replaces/alters ..." sentences of every archetype, which `--check`
  requires in the entries unless the review records the difference (a misprint fix, a Paizo errata)

Player Companions (batches 6 to 9: Wilderness Origins, Legacy of the First World, People of the Wastes, Healer's Handbook)
-----
`PLAYER_COMPANIONS` books read their titles like Blood of the Ancients (small capitals, any title ends an archetype's span), and their
chapter-opening title sits above the body (`CHAPTER_TITLES`: type of 40 or more at top 40..88), so that it ends the span of the last
archetype of the chapter. Printed citations of other books ("(Ultimate Wilderness 58)", "(Pathfinder Player Companion: Heroes of
the Wild 26)") go after a link that names the thing (owner ruling 26); `LEVEL_FROM_PRINT` gives a level that print states in other words.
The trades the books need are rows of `TRADE_RENAMES`, `TRADE_ADDITIONS` and `SCAFFOLD_TRADE_ADDITIONS` (a block each, at the top of the dict).

Files
-----
`scripts/feature-prose-540-<book>.tsv`
    One row per printed head: entry, feature (head as printed), anchor, listed (yes: in `features`),
    level, source (draft or print), status, note (the disagreement), page (printed), span_sha256 (the
    SHA-256 of the import span the row was made from).
`scripts/feature-prose-540-<book>.proposals.toml`
    The texts of the entries that are not converted yet: the print text and the draft of each feature.
    Converted entries leave it (their text is in the entry).
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import html
import re
import subprocess
import sys
import tomllib
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent

# The printing of the owner's copy of each book that a review table was made from (named in the first row of
# each entry): a rule that print and the corpus state differently is read against this printing.
PRINTINGS = {
    "advanced-players-guide": "Advanced Player's Guide, 2nd printing",
    "ultimate-magic": "Ultimate Magic, 2nd printing",
    "ultimate-combat": "Ultimate Combat, 3rd printing",
    "occult-adventures": "Occult Adventures, 1st printing",
    "ultimate-intrigue": "Ultimate Intrigue, 1st printing",
    "ultimate-wilderness": "Ultimate Wilderness, 1st printing",
    "adventurers-guide": "Adventurer's Guide, 1st printing",
    "blood-of-the-ancients": "Blood of the Ancients, 2018 (the owner's copy states no printing)",
    "horror-adventures": "Horror Adventures, 1st printing",
    "planar-adventures": "Planar Adventures, 1st printing",
    "inner-sea-magic": "Inner Sea Magic, 2011 (the owner's copy states no printing)",
    "inner-sea-intrigue": "Inner Sea Intrigue, 2016 (the owner's copy states no printing)",
    "inner-sea-combat": "Inner Sea Combat, 2014 (the owner's copy states no printing; a scan with an OCR text layer)",
}
ROOT = HERE.parent
FORGET_CHECKER_HOLDS = False

# The rules of the hold comparison that the owner added after the Blood of the Ancients pilot (phynics/cast-iron#540). Each is a
# switch so that a measurement can turn it off (`--rules` of scripts/feature-prose-540-measure.py): `hyphens` (a hyphen is a space),
# `prereq` (a "Prereq: Nth-level" row is print's "must be at least Nth level"), `usage` (a `Usage` row that print says word for word
# is print's), `values` (values level by level), `dropped` (a dropped table or paragraph is a hold).
RULES = {"hyphens": True, "prereq": True, "usage": True, "values": True, "dropped": True, "choices": True, "lostlevel": True}
HYPHEN_SPACES = [False]      # on while `compare_feature` runs: the comparison of the rule `hyphens`, not the choice of the text that is written

TSV_HEADER = [
    "entry", "feature", "anchor", "listed", "level", "source", "status", "note", "page", "span_sha256",
]
STATUSES = ("pending", "print", "draft", "edit", "hold")
WRITABLE = ("print", "draft", "edit")

# Headings that scaffold a feature and are never features themselves (owner ruling of 2026-11-24 on
# phynics/cast-iron#540): never listed in `features`, never a `by` target.
SCAFFOLD = {
    "size", "speed", "attack", "ac", "ability scores", "companion type", "prerequisites", "effect", "use",
    "cost", "action", "bonus spells", "bonus feats", "weapon and armor proficiency",
    "skills", "alignment",     # owner ruling 19 of 2026-11-24 (an app list change)
    # owner ruling 33 of 2026-11-25: variants that are never listed (an app list change)
    "class skills", "skill ranks per level", "weapon and armor proficiencies", "weapon proficiencies", "weapon proficiency",
    "armor proficiency", "armor proficiencies",
    "armor proficiency and class skills",      # Pearl Seeker (Aquatic Adventures p. 53): one head for the two sections that the import prints apart; owner question on #342's successor batch
}

# ---- text helpers -----------------------------------------------------------------------------------

ABILITY_TAG = re.compile(r"\s*\((?:Ex|Su|Sp)(?:(?:, | or | and )(?:Ex|Su|Sp))*\)\s*$", re.I)


def slugify(text: str) -> str:
    out: list[str] = []
    pending = False
    for ch in text:
        if ch.isascii() and ch.isalnum():
            if pending and out:
                out.append("-")
            pending = False
            out.append(ch.lower())
        else:
            pending = True
    return "".join(out)


def anchor_of(name: str) -> str:
    return slugify(ABILITY_TAG.sub("", name))


def squash(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", text).lower().replace("’", "'"))


def namekey(name: str) -> str:
    return squash(ABILITY_TAG.sub("", name))


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ordinal(n: int) -> str:
    return f"{n}" + {1: "st", 2: "nd", 3: "rd"}.get(n if n < 20 else n % 10, "th") if n not in (11, 12, 13) else f"{n}th"


LEAD = re.compile(r"^(?:At|Starting at|Beginning at)\s+(\d+)(st|nd|rd|th)\s+level\b[,:]?\s*", re.I)


# "Beginning at 5th level, ..." in the middle of a paragraph is "At 5th level, ..." (wording, not a rule word)
LEVEL_LEAD_WORDS = re.compile(r"\b(?:Beginning|Starting) at (?=\d+(?:st|nd|rd|th)\b)", re.I)


def lead_level(text: str) -> int | None:
    """The level of an "At Nth level" lead (also "Starting at", "Beginning at"), as the app's check reads it."""
    m = LEAD.match(text.strip())
    if not m:
        return None
    n = int(m.group(1))
    if 1 <= n <= 20 and m.group(2) == ordinal(n)[len(str(n)):]:
        return n
    return None


# The lead of a feature that the batch of the Campaign Setting books reads besides "At / Starting at / Beginning at Nth level" (`LEAD_EXT`):
# "Upon reaching 5th level", "At 3rd-level,", "of 8th level or higher" in the first sentence, and a lead at the start of the second sentence of the
# first paragraph ("... assaults. Starting at 2nd level, a siege gunner gains ...").
LEAD_EXT = {"on": False}
LEAD_NTH = r"(\d+)(st|nd|rd|th)"


def ext_lead_level(first: str) -> tuple[int | None, str]:
    def ok(m: re.Match) -> int | None:
        n = int(m.group(1))
        return n if 1 <= n <= 20 and m.group(2) == ordinal(n)[len(m.group(1)):] else None
    text = first.strip()
    text = re.sub(r"\s+", " ", text)                    # "1st" and "level" may stand on two lines
    m = re.match(r"(?:Upon reaching|At|Starting at|Beginning at)\s+" + LEAD_NTH + r"[ -]level\b", text, re.I)
    if m and ok(m):
        return ok(m), f'"{m.group(0)}" in the first sentence'
    m = re.match(r"[^.!?]*?\bof\s+" + LEAD_NTH + r"\s+level or higher\b", text)
    if m and ok(m):
        return ok(m), f'"{m.group(0)[m.group(0).index(" of ") + 1:]}" in the first sentence'
    # review of #344: "doesn't acquire the sneak attack until 3rd level", "When the fated guide reaches 9th level, her phantom gains", and
    # "... and at 4th level this grants her a death curse" state the level of the feature in its first sentence
    m = re.match(r"[^.!?]*?\buntil\s+" + LEAD_NTH + r"[ -]level\b", text, re.I)
    if m and ok(m):
        return ok(m), f'"{m.group(0)[m.group(0).lower().index("until"):]}" in the first sentence'
    m = re.match(r"(?:When|Once|As soon as|Upon)\s+[^.!?,]*?\breaches\s+" + LEAD_NTH + r"[ -]level\b", text, re.I)
    if m and ok(m):
        return ok(m), f'"{m.group(0)[m.group(0).lower().index("reaches"):]}" in the first sentence'
    m = re.match(r"[^.!?]*?\bat\s+" + LEAD_NTH + r"[ -]level\s+this\s+grants\b", text, re.I)
    if m and ok(m):
        return ok(m), f'"{m.group(0)[m.group(0).lower().rindex(" at ") + 1:]}" in the first sentence'
    sentences = re.split(r"(?<=[.!?])\s+", text, maxsplit=1)
    if len(sentences) == 2:
        # not "At": a later "At 4th level, ..." is an upgrade of the feature (Hamatulatsu Master's Stunning Fist), not its lead
        m = re.match(r"(?:Upon reaching|Starting at|Beginning at|Instead,? at)\s+" + LEAD_NTH + r"[ -]level\b", sentences[1], re.I)
        if m and ok(m):
            return ok(m), f'"{m.group(0)}" at the start of the second sentence'
        m = re.match(r"At\s+(1)(st)[ -]level\b", sentences[1])
        if m and ok(m):
            return 1, f'"{m.group(0)}" at the start of the second sentence (a step at 1st level starts the feature)'
    return None, ""


NUMBER_WORDS = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
    "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13", "fourteen": "14",
    "fifteen": "15", "sixteen": "16", "seventeen": "17", "eighteen": "18", "nineteen": "19",
    "twenty": "20", "once": "1", "twice": "2", "half": "1/2", "first": "1st", "second": "2nd", "third": "3rd",
}
# Words that carry no rule: articles, pronouns, copulas, prepositions, joining words, and the "can"/"may"
# pair that Pathfinder uses alike. Anything else that differs between the draft and print is a rule word.
IGNORED = set(
    """a an the this that these those such is are be been being was were am do does did has have had having
    it its itself he she his her him hers they their them themselves you your yours i also following then
    there here which who whom whose what where when while per of to in on at for with by from as into than
    so up out over can may will would could should one's ones other another its who s and level ability
    feature addition str dex con int wis cha however moreover furthermore thus therefore but gain""".split()
)
NUMBER_TOKEN = re.compile(r"^[+\-]?\d[\d/,.]*$")
TOKEN = re.compile(r"[+\-]?[a-z0-9]+(?:[-'/][a-z0-9]+)*", re.I)


def stem(word: str) -> str:
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 4 and word.endswith(("sses", "xes", "zes", "ches", "shes")):
        return word[:-2]
    if len(word) > 6 and word.endswith("uses"):
        return word[:-3]                                  # bonuses -> bonu, like bonus -> bonu
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def fold(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = text.replace("−", "-").replace("—", " ")
    text = re.sub(r"–(?=\d)", "-", text).replace("–", " ")
    return text.lower()


def tokens(text: str, drop: set[str] = frozenset()) -> list[str]:
    """Content tokens of a text: lower case, number words as digits, plural endings stripped, no
    ignored words. Markdown link markup is dropped first."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[\\*_`]", " ", text)
    text = fold(text)
    # a minus sign that is a dash between words is not a sign
    text = re.sub(r"(?<=[a-z0-9])-(?=\s)", " ", text)
    out = []
    for raw in TOKEN.findall(text):
        t = raw.strip("-'/")
        if RULES["hyphens"] and HYPHEN_SPACES[0] and re.search(r"[a-z0-9]-[a-z0-9]", t) and not NUMBER_TOKEN.match(t) and t != "full-round":
            # a hyphen is a space ("brown-fur", "5-foot"): the parts are tokens of their own
            for part in t.split("-"):
                if part and part not in IGNORED:
                    part = re.sub(r"^([+\-]?\d+)(?:st|nd|rd|th)$", r"\1", part).replace("'", "")      # a number word in a compound ("two-handed") stays a word
                    part = part if NUMBER_TOKEN.match(part) else stem(part)
                    if part not in drop:
                        out.append(part)
            continue
        if t in NUMBER_WORDS:
            t = NUMBER_WORDS[t]
        t = t.replace("'s", "") if t.endswith("'s") else t
        t = t.replace("'", "")
        t = re.sub(r"^([+\-]?\d+)(?:st|nd|rd|th)$", r"\1", t)
        if not t or t in IGNORED:
            continue
        if not NUMBER_TOKEN.match(t):
            t = stem(t)
        if t in drop or t in IGNORED:
            continue
        out.append(t)
    return out


def is_number(token: str) -> bool:
    return bool(NUMBER_TOKEN.match(token))


# ---- the import shape -------------------------------------------------------------------------------

NAME_BLOCK = re.compile(r"^\*\*([^*]+?)\*\*$")
ROW_A = re.compile(r"^\*\*([^*]+?):\*\*:?\s*(.*)$", re.S)
ROW_B = re.compile(r"^\*\*([^*]+?)\*\*:\s*(.*)$", re.S)
EFFECT_LABELS = ("Passive", "Ability", "Ability2", "Benefit")
ACTION_LABELS = {
    "Standard": "standard", "Move": "move", "Swift": "swift", "Immediate": "immediate", "Free": "free",
    "Fullround": "full-round", "Full-round": "full-round",
}
ACTION_VALUES = {
    "standard action": "standard", "standard": "standard", "move action": "move", "swift action": "swift",
    "immediate action": "immediate", "free action": "free", "full-round action": "full-round",
    "fullround": "full-round",
}
PLAIN_LABELS = ("Gained", "Replaces", "Alters", "Special", "Choice", "Info", "Flavor", "Usage", "Prereq", "Action")
UPGRADE_LABEL = re.compile(r"^At (\d+)(?:st|nd|rd|th) Level$", re.I)
UPGRADE_PLAIN = re.compile(r"^At (\d+)(?:st|nd|rd|th) level:\s*(.*)$", re.S)
LOWERCASE_FIRST = frozenset(
    "You Your The This These That Those Its It A An Any All Each In Once When Whenever While If As For Add By "
    "She He Her His They Their Instead Additionally Also Every Allies".split()
)


def split_entry(text: str) -> tuple[str, str]:
    if not text.startswith("+++\n"):
        raise ValueError("no front matter")
    i = text.index("\n+++\n", 4)
    return text[4:i], text[i + 5:]


def blocks_of(body: str) -> list[list[str]]:
    out: list[list[str]] = []
    cur: list[str] = []
    for ln in body.split("\n"):
        if ln.strip() == "":
            if cur:
                out.append(cur)
                cur = []
        else:
            cur.append(ln)
    if cur:
        out.append(cur)
    return out


def logical(block: list[str]) -> str:
    return " ".join(s.strip() for s in block)


@dataclass
class Item:
    label: str | None
    content: str


@dataclass
class ImportFeature:
    name: str
    items: list[Item] = field(default_factory=list)
    raw: list[list[str]] = field(default_factory=list)   # source blocks (the name block first)
    pseudo: bool = False                                  # a label row that print sets as a head
    label: str = ""                                       # the label of such a row, as written

    def span_sha(self) -> str:
        return sha("\n\n".join(logical(b) for b in self.raw))


def tail_name(label: str) -> str:
    """The head under which print sets a label row ("These rogue talents complement this archetype")."""
    m = re.match(r"^These (advanced )?(\w+) talents complement this archetype$", label, re.I)
    if m:
        return "Advanced Talents" if m.group(1) else f"{m.group(2).capitalize()} Talents"
    return label


def parse_import(body: str, heads: set[str] = frozenset()) -> tuple[list[list[str]], list[ImportFeature]]:
    opening: list[list[str]] = []
    feats: list[ImportFeature] = []
    cur: ImportFeature | None = None
    for block in blocks_of(body):
        text = logical(block)
        m = NAME_BLOCK.match(text)
        if m and not m.group(1).rstrip().endswith(":"):
            cur = ImportFeature(m.group(1).strip(), raw=[block])
            feats.append(cur)
            continue
        if cur is None:
            opening.append(block)
            continue
        r = ROW_A.match(text) or ROW_B.match(text)
        if r:
            label, content = r.group(1).strip(), r.group(2).strip()
            known = label in PLAIN_LABELS or label in EFFECT_LABELS or label in ACTION_LABELS or UPGRADE_LABEL.match(label)
            if not known and cur.pseudo and namekey(label) == namekey(cur.label):
                # the import split a printed table or list into rows with one label: they are one head
                cur.raw.append(block)
                cur.items.append(Item(None, content))
                continue
            if not known and (namekey(tail_name(label)) in heads or namekey(label) in heads):
                cur = ImportFeature(tail_name(label), [Item(None, content)], [block], pseudo=True, label=label)
                feats.append(cur)
                continue
            cur.raw.append(block)
            cur.items.append(Item(label, content))
        else:
            cur.raw.append(block)
            cur.items.append(Item(None, text))
    return opening, feats


def lower_first(text: str) -> str:
    first = text.split(" ", 1)[0].strip(",.;:")
    return text[0].lower() + text[1:] if first in LOWERCASE_FIRST else text


@dataclass
class Draft:
    text: str                                   # the rule draft: lead, action phrase, effect, rows
    core: str                                   # the draft without upgrade rows and the usage rows
    upgrades: list[tuple[int, str]]             # (level, sentence) rows that print states as a rule
    usage: list[str]
    level: int | None                           # the level of the Gained row
    inexpressible: list[str]                    # why the draft cannot be built without guessing
    parts: list[str] = field(default_factory=list)   # the paragraphs of the corpus text (no leads, no upgrade rows)
    action_labelled: bool = False               # an action label (`**Swift:**`) made a phrase that print may not have
    prereq: list[str] = field(default_factory=list)   # the `Prereq` rows


def build_draft(feat: ImportFeature) -> Draft:
    level = None
    effect: list[str] = []
    action = None
    rest: list[str] = []
    upgrades: list[tuple[int, str]] = []
    usage: list[str] = []
    prereq: list[str] = []
    bad: list[str] = []
    labelled = False
    for it in feat.items:
        lab = it.label
        if lab == "Gained":
            m = re.match(r"At (\d+)(?:st|nd|rd|th) Level", it.content, re.I)
            if m:
                level = int(m.group(1))
            else:
                bad.append(f"Gained: {it.content}")
        elif lab in EFFECT_LABELS:
            effect.append(it.content)
        elif lab in ACTION_LABELS:
            labelled = True
            effect.append(f"as a {ACTION_LABELS[lab]} action, " + lower_first(it.content))
        elif lab == "Action":
            v = ACTION_VALUES.get(it.content.strip().rstrip(".").lower())
            if it.content.strip().rstrip(".").lower() in ("ability", "special", "passive ability", "passive"):
                continue        # "Action: Ability" names no action
            if v:
                action = v
                labelled = True
            else:
                bad.append(f"Action: {it.content}")
        elif lab in ("Replaces", "Alters"):
            pass
        elif lab == "Usage":
            usage.append(it.content)
        elif lab == "Prereq":
            prereq.append(it.content)
            rest.append(it.content)
        elif lab and UPGRADE_LABEL.match(lab):
            upgrades.append((int(UPGRADE_LABEL.match(lab).group(1)), it.content))
        elif lab is None:
            m = UPGRADE_PLAIN.match(it.content)
            if m:
                upgrades.append((int(m.group(1)), m.group(2)))
            else:
                effect.append(it.content)
        else:
            rest.append(it.content)
    if not effect and upgrades and level is None:
        # `**At 3rd Level:** text` with no effect row: the first such row is the feature itself
        n, text = min(upgrades)      # the import does not sort its rows: the lowest level is the feature itself
        upgrades.remove((n, text))
        level = n
        effect.append(text)
    parts = []
    if effect:
        first = effect[0]
        if action and not first.lower().startswith("as a"):
            first = f"as a {action} action, " + lower_first(first)
        effect[0] = first
    if effect and level:
        effect[0] = f"At {ordinal(level)} level, " + lower_first(effect[0])
    if feat.pseudo and effect and namekey(feat.label) != namekey(feat.name):
        effect[0] = f"{feat.label}: {effect[0]}"
    parts += effect + rest
    core = " ".join(parts)
    full = core + "".join(f" At {ordinal(n)} level, {lower_first(t)}" for n, t in sorted(upgrades))
    return Draft(full, core, sorted(upgrades), usage, level, bad, [x for x in effect + rest], labelled, prereq)


# ---- links and italics carried over from the import --------------------------------------------------

LINK = re.compile(r"(_?)\[([^\]]+)\]\(([^)]+)\)(_?)")


def old_links(feat: ImportFeature) -> list[tuple[str, str]]:
    """Every link of the import text, once for each occurrence (a word that the import links twice is
    placed twice)."""
    text = "\n".join(it.content for it in feat.items) + "\n" + feat.name
    return [(m.group(2), m.group(3)) for m in LINK.finditer(text)]


I_OPEN, I_CLOSE = "\x01", "\x02"
LINK_SPAN = re.compile(r"(?<!\\)\[[^\[\]]*\]\([^()\s]*\)")


LINK_CTX = {"title": ""}        # the title of the archetype whose text the links are placed in (`LINK_TITLE_SPAN`)


def LINK_TITLE_SPAN(title: str):
    """The archetype's own name as it stands in running text (case folded, any blanks)."""
    words = [re.escape(w) for w in re.findall(r"[A-Za-z0-9']+", re.sub(r"\s*\([^()]*\)$", "", title))]
    return re.compile(r"\b" + r"\s+".join(words) + r"\b", re.I) if words else re.compile(r"(?!x)x")


def apply_links(text: str, links: list[tuple[str, str]]) -> tuple[str, list[str]]:
    """Wrap an occurrence of each old link text that is not inside a link already: the longer labels first (so
    "planar ally" does not take the words of "lesser planar ally"), and an occurrence with the same case as the
    label before another one ("Animal" in a domain list, not "animal companion"). The spans of the links already
    placed are found by their own shape (`[label](target)`, a target holds no parenthesis), so printed
    parentheses and brackets do not fool the test. Returns the text and the link texts that found no place."""
    lost = []
    for label, target in sorted(links, key=lambda x: -len(x[0])):
        plain = label.replace("\\", "")
        words = [re.escape(w) for w in re.split(r"[\s-]+", plain) if w]
        if not words:
            continue
        pat = re.compile(r"(?<![\w\[])" + r"[\s-]+".join(words) + r"(?![\w\]])", re.I)
        spans = [(m.start(), m.end()) for m in LINK_SPAN.finditer(text)]
        # an import link lands on the first occurrence of its text; that is not an occurrence inside the archetype's own name ("a mirror witch"
        # for the link of "mirror") or inside a longer italic name ("cause fear" for the link of "fear"): the next occurrence takes it
        spans += [(m.start(), m.end()) for m in LINK_TITLE_SPAN(LINK_CTX["title"]).finditer(text)] if LINK_CTX["title"] else []
        longer = [(m.start(), m.end()) for m in re.finditer(I_OPEN + "([^" + I_OPEN + I_CLOSE + "]*)" + I_CLOSE, text)]
        free = [m for m in pat.finditer(text) if not any(a <= m.start() < b for a, b in spans)
                and not any(a <= m.start() and m.end() <= b and re.sub(r"[^a-z0-9]", "", text[a + 1:b - 1].lower()) != re.sub(r"[^a-z0-9]", "", m.group(0).lower())
                            and not LINK_SPAN.search(text[a:b]) for a, b in longer)]
        chosen = next((m for m in free if m.group(0) == plain), free[0] if free else None)
        if chosen is None:
            lost.append(label)
            continue
        text = text[: chosen.start()] + f"[{chosen.group(0)}]({target})" + text[chosen.end():]
    return text, lost


def escape_md(text: str) -> str:
    text = text.replace("\\", "\\\\")
    for ch in "*_[]<>`":
        text = text.replace(ch, "\\" + ch)
    return text


def clean_runs(runs: list[tuple[str, bool, bool]]) -> str:
    """Runs of one paragraph -> text with italic marks (I_OPEN/I_CLOSE), no bold, escaped."""
    out: list[str] = []
    for text, _bold, italic in runs:
        text = text.replace("\xa0", " ")
        text = escape_md(text)
        if italic and text.strip():
            lead = text[: len(text) - len(text.lstrip())]
            trail = text[len(text.rstrip()):]
            out.append(lead + I_OPEN + text.strip() + I_CLOSE + trail)
        else:
            out.append(text)
    s = "".join(out)
    if DAGGER in s:
        if DAGGER_KEEP["on"]:
            s = re.sub(r"^(\s*)" + DAGGER + r"+ ", "\\1\u2020", s)          # the key paragraph: "\u2020This spell is ..."
            s = s.replace(DAGGER, "\u2020")
        else:
            s = re.sub(DAGGER + r"+ ?(?=[,.;:)])", "", s).replace(DAGGER, "")
    return s


def finish_text(s: str, vocab: set[str]) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("\u00ad", "")
    s = re.sub(r"(?<=\d)\)(?=[a-z])", ") ", s)               # "(see page 37)influences": the extraction lost the blank behind the parenthesis of a page reference
    s = re.sub(r"(?<=[A-Za-z0-9])/ (?=[A-Za-z0-9])", "/", s)                       # "law/" at a line end, "chaos" on the next ("DR 5/", "cold iron"; "1/", "round")
    s = re.sub(r"(?<=[A-Za-z" + I_CLOSE + r"]) +(?=['\u2019]s\b)", "", s)         # "thief 's" (kerning of an italic or bold run)
    s = re.sub("\ufffd(?=\\d)", "\u00d7", s)             # a multiplication sign that the extraction lost ("a x2 becomes a x3")
    s = re.sub(r"(?<![\w)\]])–(?=\d)", "-", s)           # a minus sign
    s = re.sub(r"(?<=\w) – (?=\d)", " - ", s)             # a minus operator ("druid level – 2")
    s = fix_ligatures(s, vocab)
    s = fix_hyphens(s, vocab)
    s = re.sub(r"\b([A-Z][a-z]+)- ([A-Z][a-z]+)\b", r"\1-\2", s)        # "Sahir-" at a line end and "Afiyun" at the start of the next: a compound of two capitalized words
    s = re.sub("(?<=[A-Za-z0-9)_" + I_CLOSE + "])\u2014 +(?=\\S)", "\u2014", s)   # a line that ends in an em dash joins the next one without a blank ("DR 5/\u2014 against" keeps its blank); an italic label ("3rd\u2014") too
    s = re.sub(r"(?<=[A-Za-z0-9" + I_CLOSE + r"]) +(?=[,;])", "", s)          # a superscript at a line end leaves "resistance , create"
    # an italic run of marks only (", " or "." between two words) is plain text: the period of "possession (see page 181)." is not italic
    s = re.sub(I_OPEN + r"([\s,.;:!?]+)" + I_CLOSE, r"\1", s)
    # the extraction pads italic runs with blanks
    s = re.sub(I_OPEN + r"\s+", " " + I_OPEN, s)
    s = re.sub(r"\s+" + I_CLOSE, I_CLOSE + " ", s)
    s = re.sub(I_CLOSE + I_OPEN, "", s)
    if ITALIC_FIRST["on"]:
        s = re.sub(r"(?<=[A-Za-z]) \u2014(?=[A-Za-z])", "\u2014", s)          # "agitation \u2014but": a blank that the layer sets before an em dash
        s = re.sub(r"(?<![A-Za-z'\u2019])([A-Za-z])" + I_OPEN + r"(?=[a-z])", I_OPEN + r"\1", s)       # the first letter of an italic word set apart ("s" + "un orchid elixir")
    s = re.sub(r"(\\\[|\()\s+", r"\1", s)        # no blank after an opening bracket or parenthesis
    s = re.sub(r"\s+(\)|\\\])", r"\1", s)        # none before a closing one
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fix_ligatures(s: str, vocab: set[str]) -> str:
    """`f ighter`, `inf lict`: the fi and fl ligatures leave a blank that a word does not have. A pair that does not join ("of inf") does not
    hide the next one that starts inside it ("inf luence")."""
    pat = re.compile(r"\b([A-Za-z]*f) ([il][a-z]*)\b")
    out, i = [], 0
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            return "".join(out)
        a, b = m.group(1), m.group(2)
        if (a + b).lower() in vocab:
            out += [s[i:m.start()], a + b]
            i = m.end()
        else:
            out.append(s[i:m.start(2)])
            i = m.start(2)


def fix_hyphens(s: str, vocab: set[str]) -> str:
    """A hyphen at a line end: keep it in a compound that the book prints whole (two-weapon), drop it in a
    word that the line break split."""

    def join(m: re.Match) -> str:
        a, b = m.group(1), m.group(2)
        if b.lower() in ("or", "and", "to"):
            return f"{a}- {b}"          # a suspended hyphen ("class- or level-based") stays as printed
        both = f"{a}-{b}".lower()
        glued = f"{a}{b}".lower()
        if both in vocab:
            return f"{a}-{b}"
        if glued in vocab:
            return f"{a}{b}"
        return f"{a}-{b}"

    return re.sub(r"\b([0-9]*[A-Za-z]+)- (?=[a-z])([A-Za-z]+)\b", join, s)


SPLIT_ITALIC = re.compile("(" + I_OPEN + "[^" + I_OPEN + I_CLOSE + r"\[\]]*)" + I_CLOSE + " " + I_OPEN + "(?=[^" + I_OPEN + I_CLOSE + r"\[\]]*" + I_CLOSE + ")")


def render_marks(s: str) -> str:
    """Italic marks to underscores. Two italic runs with only a space between them are one name that the line wrap of print cut
    ("_riding_ _possession_"): one span (review of #344)."""
    s = SPLIT_ITALIC.sub(lambda m: m.group(1) + " ", s)
    s = re.sub(I_OPEN + r"\(([^" + I_OPEN + I_CLOSE + r")]*)" + I_CLOSE, lambda m: "(" + I_OPEN + m.group(1) + I_CLOSE, s)      # print sets the parenthesis of a citation in italics: the mark goes inside it
    return s.replace(I_OPEN, "_").replace(I_CLOSE, "_")


# ---- the print: pdftohtml -xml ------------------------------------------------------------------------

TEXT_EL = re.compile(r'<text top="(-?\d+)" left="(-?\d+)" width="(-?\d+)" height="(-?\d+)" font="(\d+)">(.*?)</text>', re.S)
FONT_EL = re.compile(r'<fontspec id="(\d+)" size="(\d+)" family="([^"]*)" color="([^"]*)"')
TAG_SPLIT = re.compile(r"(</?[bi]>)")
BODY_TOP = (88, 1075)
BODY_BOTTOM_FORCE = [0]
BODY_BOTTOM_BOOKS = {"dungeoneers-handbook": 1110, "the-harrow-handbook": 1110, "technology-guide": 1110, "animal-archive": 1110, "giant-hunters-handbook": 1110, "kobolds-of-golarion": 1110, "people-of-the-stars": 1110, "champions-of-balance": 1110, "bastards-of-golarion": 1110, "knights-of-the-inner-sea": 1110, "people-of-the-river": 1110}      # the body runs to 1089 and the folios are not in the text layer (Dungeoneer's Handbook)
PAGE_SKIP: list[tuple[int, int]] = []     # printed pages (first, last) that hold other text than the archetypes (Legacy of Dragons pp. 16-23 and from 26)
CHAPTER_END = [0]              # the last printed page of the chapter of archetypes, where the book sets other text on the next page (0: none)
PAGE_OFFSET = [1]              # printed page = PDF page - this, when the page's folio is not in the text layer (Inner Sea Combat: 2)
BODY_CAP_TOP = 60
SUPERSCRIPT = "\x04"
DAGGER = "\x05"                 # a dagger of the book; DAGGER_KEEP says whether the entry keeps it
DAGGER_KEEP = {"on": False}
COL_SPLIT = 460
COL_LEFT = (108, 468)      # the left edge of the two columns of the Advanced Player's Guide


@dataclass
class Para:
    kind: str                                # para | title
    runs: list[tuple[str, bool, bool]]
    page: int                                # printed page
    col: int
    size: int = 0                            # the font size of a title

    def plain(self) -> str:
        return "".join(t for t, _, _ in self.runs).replace(DAGGER, "")


def runs_of(raw: str) -> list[tuple[str, bool, bool]]:
    out, b, i = [], False, False
    for part in TAG_SPLIT.split(raw):
        if part == "<b>":
            b = True
        elif part == "</b>":
            b = False
        elif part == "<i>":
            i = True
        elif part == "</i>":
            i = False
        elif part:
            out.append((html.unescape(part), b, i))
    return out


@dataclass
class Book:
    fonts: dict[str, int]
    pages: dict[int, list[tuple[int, int, int, str, int]]]    # pdf page -> (top, left, font, raw, width)
    printed: dict[int, int]                              # pdf page -> printed page
    vocab: set[str]
    sans: frozenset = frozenset()                        # the font ids of the sans-serif type that sets a table
    fams: dict = field(default_factory=dict)             # font id -> family, without the subset prefix


# Inner Sea Combat is a scan with an OCR text layer (ClearScan type): no bold or italic runs, and the OCR confuses a few
# characters of its own ("ist" for 1st, "i6th" for 16th, "13" for g, "k" for "lt"). `ocr_repair` mends the words that the layer
# mangles in a way that no reading of the page can doubt; what it cannot mend stays and shows up as a difference to be decided
# against the page image.
OCR = {"on": False}
OCR_WORDS = {
    "Blacltjacket": "Blackjacket", "Blacltjackets": "Blackjackets", "Oruman": "Druman", "bum": "burn", "Bum": "Burn", "tum": "turn",
    "tlie": "the", "Engineeruc": "Engineer", "lroran": "Iroran", "Oadiran": "Qadiran", "Arcl)etypes": "Archetypes",
    "Jun3le": "Jungle", "Raser": "Rager", "Oheno": "Okeno", "Monh": "Monk", "Rarnpager": "Rampager", "CMonR": "(Monk",
    "jlamin13": "flaming", "jlamin13,": "flaming,", "13lamered11E,": "glamered,", "stalkin13°E.": "stalking.",
    "nth": "11th", "nth-level": "11th-level", "ef": "of", "oflrori": "of Irori", "io3": "103", "Tar,geted": "Targeted", ".from": "from",
    "al(gn": "align", "Path.finder": "Pathfinder", "]ury-Ri13": "Jury-Rig", "]ury-Rig": "Jury-Rig", "+S": "+5",
    # Monster Codex (read from the page images)
    "Frinhiful": "Frightful", "Sonn": "Song", "YappinlJ": "Yapping", "SippinlJ": "Sipping", "Peiformance": "Performance",
    "+i/2": "+1/2", "i/4": "1/4", "+io": "+10", "id4+1": "1d4+1", "id4+i": "1d4+1",
}
OCR_GLUED = re.compile(r"(?i)^(of|if)(?=(?:her|his|the|this|their|bardic|both|temporary|that|a|an|its|any|each|one|your|my|which|those|them)$)")     # Monster Codex: "ofher", "ifthe"
OCR_MARK = re.compile(r"(?<=[a-z])(?:APG|APc|ARG|0c|uc|UC|UM|'PG|PG)(?=[\W_]|$)")


def ocr_repair(text: str) -> str:
    text = text.replace("\u00ad", "-")            # the layer sets the hyphen of a line end as a soft hyphen: `fix_hyphens` keeps it in a compound the book prints whole

    def word(m: re.Match) -> str:
        w = m.group(0)
        if html.unescape(w) in OCR_WORDS:
            return OCR_WORDS[html.unescape(w)]
        pre = re.match(r"^[^\w+\-]*", w).group(0)
        core = w[len(pre):]
        post = re.search(r"[^\w]*$", core).group(0)
        core = core[:len(core) - len(post)] if post else core
        if core in OCR_WORDS:
            return pre + OCR_WORDS[core] + post
        if OCR_MARK.search(core):
            core = OCR_MARK.sub("", core)               # a book mark (APG, UC, ARG) that the layer glued to the word
        if OCR_GLUE["on"]:
            core = OCR_GLUED.sub(lambda m: m.group(1) + " ", core)
        core = re.sub(r"^([+\-]?)[iIl|](?=\d)", r"\g<1>1", core)           # i6th, i50, +i2
        core = re.sub(r"^([+\-]?)[iIl|]$", r"\g<1>1", core) if re.match(r"^[+\-][iIl|]$", core) else core
        core = re.sub(r"^[iIl]/2$", "1/2", core)
        core = re.sub(r"^i(?=d\d+$)", "1", core)                              # id10: 1d10
        core = re.sub(r"^([iIl|]St|ist|[iIl]st)(?=$|-)", "1st", core)         # ist, lSt
        core = re.sub(r"^[iI]o(?=(?:th)?$)", "10", core)
        core = {"i": "1", "I": "1", "o": "0"}.get(core, core)                              # a lone i or o is the digit that the layer misread
        core = re.sub(r"^a-(?=\d)", "a -", core)                                  # "a-4 penalty": a minus sign that the layer set as a hyphen
        core = re.sub(r"(?<=[a-z])13(?=[a-z]|$)", "g", core)                  # Ma13ic, jlamin13
        core = re.sub(r"(?<=[a-z])JJ(?=[a-z])", "g", core)                    # maJJic
        return pre + core + post
    return re.sub(r"\S+", word, text)


SUPERSCRIPT_MARK = re.compile(r"([a-z]*)(?:APG|UM|UC|UE|UI|ARG|ACG|OA|ISM|B[2-6]|†)")


def load_book(xml_path: Path) -> Book:
    global BODY_TOP
    xml = xml_path.read_text(encoding="utf-8")
    fonts = {fid: int(sz) for fid, sz, _fam, _col in FONT_EL.findall(xml)}
    pages: dict[int, list] = {}
    printed: dict[int, int] = {}
    words: Counter = Counter()
    for chunk in re.split(r'<page number="', xml)[1:]:
        num = int(chunk[: chunk.index('"')])
        seen, items = set(), []
        for top, left, _w, _h, font, raw in TEXT_EL.findall(chunk):
            key = (top, left, raw)
            if key in seen:
                continue
            seen.add(key)
            top, left = int(top), int(left)
            if OCR["on"]:
                raw = ocr_repair(raw)
            plain = html.unescape(re.sub(r"</?[bi]>", "", raw)).strip()
            # a cross-reference mark: a book abbreviation (two to four capitals, or one named in `SUPERSCRIPT_MARK`) or a
            # dagger in small type after a name ("mutagen" + "UM"); the corpus links the name instead (owner ruling 26).
            # Letters that the extractor glued to the mark ("s" + "APG") are part of the word.
            if int(_h) <= 3 and plain.isdigit():
                continue                  # a watermark number set in tiny type at the page edge ("4412489"): it is no text of the page
            mark = SUPERSCRIPT_MARK.fullmatch(plain) if (fonts.get(font, 99) <= 8 or int(_h) <= 11) else None
            if mark and mark.group(1):
                raw, plain = mark.group(1), mark.group(1)
            elif int(_h) <= 11 and re.fullmatch(r"[\u2020\u2021]+", plain):
                # a dagger: kept as DAGGER; the text of an entry that prints the key of its daggers keeps it (owner ruling 10), the
                # others drop it with the other marks (`clean_runs`)
                items.append((top, left, int(font), DAGGER * len(plain) + (" " if raw != raw.rstrip() else ""), int(_w)))
                continue
            elif int(_h) <= 11 and re.fullmatch(r"[A-Z]{2,4}[.,;:)]+", plain):
                # a mark with the punctuation that follows it in one element ("UW."): the mark goes, the punctuation stays
                items.append((top, left, int(font), SUPERSCRIPT, 0))
                items.append((top, left, int(font), re.sub(r"^[A-Z]+", "", raw), int(_w)))
                continue
            elif (mark and not mark.group(1)) or (int(_h) <= 11 and re.fullmatch(r"[A-Z]{2,4}", plain)):
                # left out of the text; `page_lines` keeps the blank that ends a line when the mark stood last
                # a mark that carries the blank of the word space after it ("Performance" + "APG " + "feat") keeps it
                items.append((top, left, int(font), SUPERSCRIPT + (" " if raw != raw.rstrip() else ""), int(_w)))
                continue
            if top > BODY_TOP[1] and plain.isdigit():
                printed[num] = int(plain)
            items.append((top, left, int(font), raw, int(_w)))
            for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", plain):
                words[w.lower()] += 1
                if "-" in w:
                    for part in w.lower().split("-"):
                        words[part] += 1
        pages[num] = items
    # the body ends nine units above the page numbers of the book: 1075 in the Advanced Player's Guide, Ultimate Magic
    # and Ultimate Combat, 1090 in Ultimate Intrigue (its body runs lower)
    foot = sorted(top for chunk_items in pages.values() for top, _l, _f, raw, _w in chunk_items
                  if top > 1060 and html.unescape(re.sub(r"</?[bi]>", "", raw)).strip().isdigit())
    if foot:
        BODY_TOP = (BODY_TOP[0], foot[len(foot) // 2] - 9)
    if BODY_BOTTOM_FORCE[0]:
        BODY_TOP = (BODY_TOP[0], BODY_BOTTOM_FORCE[0])
    vocab = {w for w, _ in words.items()}
    sans = frozenset(fid for fid, _sz, fam, _col in FONT_EL.findall(xml) if "Sans" in fam)
    fams = {fid: re.sub(r"^[A-Z]{6}\+", "", fam) for fid, _sz, fam, _col in FONT_EL.findall(xml)}
    return Book(fonts, pages, printed, vocab, sans, fams)


# The Campaign Setting books set the right column of a page 28 units further left on some pages than on others (Inner Sea Intrigue
# p. 41: 440, not 468), and the left column 18 further in on the pages beside the spine. The margins of a page are the commonest
# left edges of its lines of body type.
PAGE_GEOMETRY = {"on": False}
ITALIC_JOIN = {"on": False}     # two italic runs with a plain blank between them are one italic span (Aquatic Adventures, Heroes of the Streets, Antihero's Handbook, Blood of the Sea)
SKIP_FAMILY = {"fam": ""}
SKIP_BANNERS: dict = {"pages": {}}      # page -> (first, last) top of the name banner (Pathfinder Society Field Guide)
PFSFG_BANNERS = {28: (605, 630), 30: (585, 610), 32: (575, 600)}
PAREN_SNAP = {"on": False}      # Dungeoneer's Handbook and Animal Archive set their parentheses in a face of their own, off the baseline
TAB_LEFT = {"min": 0, "title": 16}      # Aquatic Adventures: a tab left of which the text stands; its titles are set in 15-point small capitals (the body is 13)
OUTER_TAB_REACH = {"at": 340}      # how far right of the left edge of the right column the text can start (Technology Guide: 330, the page carries a chapter tab with stray glyphs at 786 to 880)
OUTER_TAB = {"on": False}       # the tab in the outer margin is large type (Construct Handbook): anything beyond the columns goes


def page_geometry(book: Book, num: int) -> tuple[int, tuple[int, int]]:
    if not PAGE_GEOMETRY["on"]:
        return COL_SPLIT, COL_LEFT
    count: Counter = Counter()
    for top, left, font, raw, width in book.pages.get(num, []):
        if 12 <= book.fonts[str(font)] <= 14 and BODY_TOP[0] <= top <= BODY_TOP[1] and left > 90:
            count[left] += 1
    lefts = [(n, x) for x, n in count.items() if x < 360]
    rights = [(n, x) for x, n in count.items() if x >= 360]
    if not lefts or not rights:
        return COL_SPLIT, COL_LEFT
    # the margin of a column is its commonest left edge; edges within 3 units are one
    def margin(c: list[tuple[int, int]]) -> int:
        return max(c, key=lambda nx: (sum(n for n, x in c if abs(x - nx[1]) <= 3), -nx[1]))[1]
    l0, l1 = margin(lefts), margin(rights)
    return l1 - 8, (l0, l1)


def page_lines(book: Book, num: int) -> list[dict]:
    by_col: dict[int, list] = {0: [], 1: []}
    split, col_left = page_geometry(book, num)
    parts = book.pages.get(num, [])
    if PAREN_SNAP["on"]:
        # a parenthesis that the book sets in a face of its own, a few units off the baseline ("Knowledge" "(" "engineering" ")"): it joins the line of the word beside it
        snapped = []
        for top, left, font, raw, width in parts:
            if raw.strip() == "=" and book.fonts[str(font)] <= 6:
                # the "=" of "DC = 10" stands in a face of its own, a few units below the baseline, and the layer sets it in a line of its own
                near = [(t, f) for t, l, f, r, w in parts if r.strip() not in ("=",) and abs(t - top) <= 10 and (abs(l + w - left) <= 8 or abs(left + width - l) <= 8) and book.fonts[str(f)] >= 12]
                if near:
                    top, font = min(near, key=lambda x: abs(x[0] - top))
            elif (raw.strip() in ("(", ")", "()", "[", "]") or (width < 15 and re.fullmatch(r"[()\[\]f]{1,3}", raw.strip()))) and book.fonts[str(font)] >= 15:      # ... and "f)": the layer sets the f of "half" with its closing parenthesis in that face (Kobolds of Golarion p. 22)
                near = [(t, f) for t, l, f, r, w in parts if r.strip() not in ("(", ")", "()", "[", "]") and abs(t - top) <= 8 and (abs(l + w - left) <= 6 or abs(left + width - l) <= 6)]
                if near:
                    top, font = min(near, key=lambda x: abs(x[0] - top))       # the baseline and the type of the word beside it
            snapped.append((top, left, font, raw, width))
        parts = snapped
    for top, left, font, raw, width in parts:
        window = SKIP_BANNERS["pages"].get(num)
        if window and window[0] <= top <= window[1] and "SC700" in book.fams.get(str(font), ""):
            continue        # the name banner of a Pathfinder Society master ("Kreighton Shaine", in the title face) that the art puts in the middle of the text: its letters are no title and no text
        if SKIP_FAMILY["fam"] and SKIP_FAMILY["fam"] in book.fams.get(str(font), "") and book.fonts[str(font)] <= 13:
            continue        # the cells of a table in the face that the book sets its tables in (Heroes of Golarion: "Dax"): a table that stands at the foot of the page across both columns is no text of the archetype
        if SKIP_TABLES["on"] and str(font) in book.sans and book.fonts[str(font)] <= 13:
            continue        # a table of the race chapter that stands on the page of the archetype: its cells are not the text
        if PAGE_GEOMETRY["on"] and (left > col_left[1] + 340 or left < col_left[0] - 30) and book.fonts[str(font)] <= 14 and book.fonts[str(font)] != 13:
            continue        # the chapter tab in the outer margin ("AVENUES OF INTRIGUE" in small bold capitals, Inner Sea Intrigue)
        if TAB_LEFT["min"] and left > TAB_LEFT["min"] and "ArgusExtraBold" in book.fams.get(str(font), ""):
            continue        # the chapter tab of Aquatic Adventures (AQUATIC ADVENTURES / INTRO / ANTARKOS OCEAN ...) is set in 11-point Argus Extra Bold at the right edge; a column on a page with shifted margins reaches 800
        if OUTER_TAB["on"] and (left > col_left[1] + OUTER_TAB_REACH["at"] or left < col_left[0] - 30):
            continue        # the chapter tab of the Construct Handbook (INTRODUCTION / CRAFTING CONSTRUCTS / ARCHETYPES ...), set in 16-point type
        if MARGIN_CAPTIONS["on"] and left < col_left[0] - 20 and book.fonts[str(font)] >= 16:
            continue        # the caption of an illustration, set in the margin beside the column (Inner Sea Magic: "Crypt Breaker" in large type)
        if BODY_TOP[0] <= top <= BODY_TOP[1] or (CHAPTER_TITLES["on"] and 40 <= top < BODY_TOP[0] and book.fonts[str(font)] >= 40):
            by_col[0 if left < split else 1].append((top, left, font, raw, width))
    lines = []
    for col in (0, 1):
        cur: list[dict] = []
        for top, left, font, raw, width in sorted(by_col[col], key=lambda x: (x[0], x[1])):
            # a title in small capitals sets its capitals and its small capitals 5 units apart (Blood of the Ancients): the
            # same family of type, a larger size above
            if cur and (abs(cur[-1]["top"] - top) <= 4 or (SMALL_CAP_TITLES["on"] and abs(cur[-1]["top"] - top) <= 8
                                                           and cur[-1]["size"] >= TAB_LEFT["title"] and book.fams.get(str(font)) == cur[-1]["fam"])):
                cur[-1]["parts"].append((left, raw, width))
                cur[-1]["size"] = max(cur[-1]["size"], book.fonts[str(font)])
            else:
                cur.append({"col": col, "top": top, "size": book.fonts[str(font)], "parts": [(left, raw, width)],
                            "fam": book.fams.get(str(font))})
        for ln in cur:
            ln["parts"].sort()
            ends_in_sup = ln["parts"][-1][1].startswith(SUPERSCRIPT)
            kept = []
            for k, (a, raw, w) in enumerate(ln["parts"]):
                if not raw.startswith(SUPERSCRIPT):
                    kept.append((a, raw, w))
                elif raw.endswith(" ") and k + 1 < len(ln["parts"]):
                    nxt = re.sub(r"</?[bi]>", "", ln["parts"][k + 1][1]).lstrip()[:1]
                    if nxt and nxt not in ",.;:)":
                        kept.append((a, " ", w))     # the blank of a mark in the middle of a line
            ln["parts"] = kept
            if ln["parts"] and ends_in_sup:
                a, raw, w = ln["parts"][-1]
                ln["parts"][-1] = (a, raw.rstrip() + " ", w)
        cur = [ln for ln in cur if ln["parts"]]
        for ln in cur:
            ln["left"] = ln["parts"][0][0]
            ln["margin"] = col_left[col]
            ln["right"] = max(a + w for a, _, w in ln["parts"])
            runs: list = []
            for _, raw, _w in ln["parts"]:
                runs += runs_of(raw)
            ln["runs"] = runs
            if MC_TITLES["on"] and 16 <= ln["size"] < 30 and ln["fam"] not in MC_TITLE_FAMILIES:
                ln["size"] = 14         # a stray large glyph of the OCR layer ("3 312)." in a citation): the titles of the book are told by their face
            if ARCHETYPE_CAPS["on"] and 14 <= ln["size"] <= 16:
                # Heroes of the Darklands sets "BLIGHTSEEKER (ALCHEMIST ARCHETYPE)" in capitals one size above the text (15 against 13)
                txt = "".join(t for t, _, _ in runs).strip()
                if CAPS_TITLE.fullmatch(txt):
                    ln["size"] = 18
            if NO_STYLE["on"] and 12 <= ln["size"] <= 15:
                # a title is set a size larger than the text (14 against 13) and ends "Archetype)": it is a title of the book's sections
                txt = "".join(t for t, _, _ in runs).rstrip()
                if re.fullmatch(r"[^.:;]{3,60}\((?:[A-Za-z]+ ){1,2}Archetype\)\s*:?", txt) or re.fullmatch(r"Archetypes", txt):
                    ln["size"] = 18
                    ln["runs"] = [(re.sub(r"\s*:$", "", txt), True, False)]
                elif MC_TITLES["on"] and ln["fam"] in MC_TITLE_FAMILIES:
                    ln["size"] = 18                # a title ("Dragon Yapper (Bard)", "KOBOLD COMPANIONS", "Coordinated Reposition (Teamwork)"): the book sets them in two faces of their own
                    ln["runs"] = [(re.sub(r"\s+", " ", txt), True, False)]
                elif ln["size"] == 15 and re.fullmatch(r"[\"\u201c\ufffd]?[^\d()]{3,40}", txt):
                    ln["runs"] = []                 # a caption of an illustration or a table title in the larger type: not text of the archetype
        if ARCHETYPE_CAPS["on"]:
            # a title that wraps around art: "PSYCHIC MARAUDER (PSYCHIC" over "ARCHETYPE)" (Heroes of the Darklands p. 22)
            for a, b in zip(cur, cur[1:]):
                ta, tb = ("".join(t for t, _, _ in x["runs"]).strip() for x in (a, b))
                if a["size"] in (14, 15, 16) and CAPS_TITLE_HEAD.fullmatch(ta) and CAPS_TITLE_TAIL.fullmatch(tb):
                    a["size"] = b["size"] = 18
        lines += [ln for ln in cur if ln["runs"]]
    return lines


def merge_runs(runs: list[tuple[str, bool, bool]]) -> list[tuple[str, bool, bool]]:
    """Joins adjacent runs of one style, and lets a blank between two runs of one style share it."""
    runs = [list(r) for r in runs if r[0] != ""]
    for i in range(1, len(runs) - 1):
        if runs[i][0].strip() == "" and runs[i - 1][1:] == runs[i + 1][1:]:
            runs[i][1:] = runs[i - 1][1:]
    out: list[tuple[str, bool, bool]] = []
    for t, b, it in runs:
        if out and out[-1][1] == b and out[-1][2] == it:
            out[-1] = (out[-1][0] + t, b, it)
        else:
            out.append((t, b, it))
    return out


# A box of the page whose title is named here sits in a column and breaks the sentence that the column carries on (Inner Sea Magic,
# "Black Blood of Orv", p. 33: the box is set in from the margin, above the end of the introduction of the next archetype). Its lines
# are read apart, and the box is set behind the section's last paragraph, before the next title.
BOX_TITLES: dict = {"titles": frozenset()}
BOX_LORE: dict = {"titles": frozenset()}      # boxes of pure lore or of references to other books, set in a column: read apart and left out (owner ruling 41)
BOX_TO_END = {"on": False}      # a box at the foot of a column (a table) runs to the end of that column (Psychic Anthology p. 6: the Phantom Weapon Progression)
BOX_INSET = 16                  # the lines of a box are set this far in from the margin of the column; the text around it is not


def split_boxes(plines: list[dict]) -> tuple[list[dict], list[dict]]:
    """The lines of a page without the boxes named in `BOX_TITLES`, and the lines of those boxes (a title and everything that
    follows it in its column)."""
    main, box, boxing = [], [], None
    for ln in plines:
        key = squash("".join(t for t, _, _ in ln["runs"]))
        title = (ln["size"] >= 16 and key in BOX_TITLES["titles"]) or (ln["size"] >= 14 and key in BOX_LORE["titles"])
        if title:
            boxing = ln["col"]
        elif boxing is not None and (ln["col"] != boxing or (not BOX_TO_END["on"] and ln["left"] - ln["margin"] < BOX_INSET)):
            boxing = None            # the text of the column goes on at its own margin below the box
        (box if boxing is not None else main).append(ln)
    return main, box


def page_skipped(printed: int | None) -> bool:
    """True for a page whose printed number lies in `PAGE_SKIP`: the book sets other text there (feats, spells, a new chapter)."""
    return printed is not None and any(a <= printed <= b for a, b in PAGE_SKIP)


def read_blocks(book: Book, first: int, last: int) -> list[Para]:
    """Paragraphs and titles of the PDF pages `first`..`last`, columns in reading order."""
    items, boxes = [], []
    if CHAPTER_END[0]:
        last = min(last, CHAPTER_END[0] + PAGE_OFFSET[0])            # the pages after the chapter hold other text (Inner Sea Combat p. 47: the magic items)
    for num in range(first, last + 1):
        if num not in book.pages:
            continue
        if page_skipped(book.printed.get(num)):
            continue
        plines = page_lines(book, num)
        if BOX_TITLES["titles"] or BOX_LORE["titles"]:
            plines, box = split_boxes(plines)
            if box and squash("".join(t for t, _, _ in box[0]["runs"])) in BOX_LORE["titles"]:
                box = []                        # a lore box is left out
            if box:
                boxes.append((num, box))
        items.append((num, plines))
    out = _assemble(book, items)
    for num, box in boxes:
        shown = book.printed.get(num, num - PAGE_OFFSET[0])
        bpar = _assemble(book, [(num, box)])
        col = box[0]["col"]
        at = max((i for i, p in enumerate(out) if p.page == shown and p.col == col and p.kind == "para"), default=-1)
        j = next((i for i in range(at + 1, len(out)) if out[i].kind == "title"), len(out))
        out[j:j] = bpar
    return out


ART_INDENT = {"on": False}      # the Tactics Toolboxes and the Villain Codex wrap text around figures: a line set in deeper than a first-line indent continues its paragraph
ART_INDENT_MAX = 20


RUN_IN_HEAD_ONLY = re.compile(r"^.{3,70}\((?:Ex|Su|Sp)(?:,\s*(?:Ex|Su|Sp))*\)\s*:\s*$")


FRAGMENT_TITLES = {"on": False}


def _assemble(book: Book, items: list[tuple[int, list[dict]]]) -> list[Para]:
    out: list[Para] = []
    insets: dict[int, int | None] = {}
    seen_big: list[str] = []
    for num, plines in items:
        shown = book.printed.get(num, num - PAGE_OFFSET[0])
        for li, ln in enumerate(plines):
            indent = ln["left"] - ln["margin"]
            nxt = plines[li + 1] if li + 1 < len(plines) else None
            if SKIP_TABLES["on"] and ln["size"] >= 16 and ln["size"] < 30:
                # the title of a box (a sidebar, a table) beside the archetype, not the title of an archetype or of the
                # chapter's new rules: the text of the archetype goes on below it
                ttl = "".join(t for t, _, _ in ln["runs"])
                two = nxt is not None and nxt["col"] == ln["col"] and nxt["size"] >= 16 and CLASS_SUFFIX.search("".join(t for t, _, _ in nxt["runs"]))
                if not CLASS_SUFFIX.search(ttl) and not two and squash(ttl) != "newracialrules":
                    continue
            if SMALL_CAP_TITLES["on"] and ln["size"] >= 60:
                # a chapter title that the page repeats unseen (Blood of the Ancients p. 21: "Imperial Lung Wa" again, in a
                # clipped object over the first lines of the column): it is not a title, and it must not end the section
                big = squash("".join(t for t, _, _ in ln["runs"]))
                if any(len(b) >= 4 and (big.startswith(b) or b.startswith(big)) for b in seen_big):
                    continue
                seen_big.append(big)
            if ln["size"] >= 16 and len(squash("".join(t for t, _, _ in ln["runs"]))) <= 2 and FRAGMENT_TITLES["on"]:
                continue                        # a title of one or two letters is a fragment of a drop capital or a vertical tab (Armor Master's Handbook p. 4), not a title
            if ln["size"] >= TAB_LEFT["title"]:
                insets[ln["col"]] = ln["left"] if indent >= 8 else None
                if out and out[-1].kind == "title" and out[-1].col == ln["col"] and out[-1].page == shown \
                        and not (SMALL_CAP_TITLES["on"] and out[-1].size != ln["size"]):
                    # a title of two lines is set in one size; a chapter title (36) above an archetype title (27) are two titles
                    out[-1].runs += [(" ", True, False)] + ln["runs"]
                else:
                    out.append(Para("title", list(ln["runs"]), shown, ln["col"], ln["size"]))
                continue
            # a paragraph starts at an indent. A sidebar is an inset block that a title opens: inside it every line is
            # indented, and only a deeper indent starts a paragraph
            inset = insets.get(ln["col"])
            if inset is not None and ln["left"] >= inset - 6:
                starts = ln["left"] - inset >= 8
            else:
                insets[ln["col"]] = None
                starts = indent >= 8
            if ART_RUNS["on"] and starts and out and out[-1].kind == "para" and li > 0 and plines[li - 1]["col"] == ln["col"]:
                # text that wraps around art is set flush to the column's right edge and steps in at the left (468, 480, 493,
                # 498), so an indent means nothing there. A paragraph ends in a short line: a line that fills the column
                # to its right edge is not the last of its paragraph, whatever it ends in. A head with its colon
                # ("Versed in Curses (Ex):") still starts a paragraph
                col_right = max(l["right"] for l in plines if l["col"] == ln["col"])
                first = next(((t, b, i) for t, b, i in ln["runs"] if t.strip()), None)
                colon_head = bool(first and (first[1] or first[2]) and re.match(r"\s*[^:]{3,70}:", "".join(t for t, _, _ in ln["runs"])))
                if plines[li - 1]["right"] >= col_right - 12 and not colon_head:
                    starts = False
            if ART_INDENT["on"] and starts and indent > ART_INDENT_MAX and out and out[-1].kind == "para":
                # beside art the lines are set in by the outline of the figure: only the first-line indent of the book starts a paragraph, and a bold head
                cand_a = head_candidate(Para("para", list(ln["runs"]), shown, ln["col"]))
                starts = bool(cand_a and cand_a[2])
            if ILLUSTRATED["on"] and starts and out and out[-1].kind == "para" and not re.search(r"[.!?:)\"”…]\s*$", out[-1].plain()) \
                    and not (all(bold for t, bold, _i in out[-1].runs if t.strip())
                             and not next((bold for t, bold, _i in ln["runs"] if t.strip()), True)):
                # beside an illustration a line may be indented without starting a paragraph: a paragraph does not
                # start in the middle of a sentence (a line of bold type only is a head, which has no sentence end, and
                # the next line in plain type starts its text: "4th-Level Ki Powers" of the Qinggong Monk; a second line
                # in bold type is the rest of the head: "Musketeer Instruction" over "(Ex)"). A bold head with its colon ("Summon
                # Fey Allies:") after a table, which ends without a sentence end, still starts one
                cand0 = head_candidate(Para("para", list(ln["runs"]), shown, ln["col"]))
                starts = bool(cand0 and cand0[2] and cand0[1] and cand0[1][0][0].lstrip().startswith(":") and len(cand0[0]) <= 60
                              and not all(bold for t, bold, _i in out[-1].runs if t.strip()))
            if ILLUSTRATED["on"] and starts and out and out[-1].kind == "para" and RUN_IN_HEAD_ONLY.search(out[-1].plain()):
                starts = False                  # a paragraph that is only a head with its colon ("Dualistic Energy (Su):") goes on in the next line, even if the art indents it
            if LOWERCASE_CONTINUES["on"] and starts and out and out[-1].kind == "para" \
                    and re.match(r"\s*[a-z]", "".join(t for t, _, _ in ln["runs"])):
                starts = False                  # a line that starts in lower case continues the sentence before it (text around an illustration)
            if ILLUSTRATED["on"] and not starts and out and out[-1].kind == "para" and re.search(r"[.)!?\"”]\s*$", out[-1].plain()):
                # beside an illustration the lines have no common indent: a head ("Rope Swing (Ex):") after the end of a
                # sentence still starts a paragraph
                cand = head_candidate(Para("para", list(ln["runs"]), shown, ln["col"]))
                starts = bool(cand and cand[1] and cand[1][0][0].lstrip().startswith(":") and len(cand[0]) <= 60)
            if BULLETS["on"] and re.match(r"\s*[\u2022\u2219]\s", "".join(t for t, _, _ in ln["runs"])):
                starts = True                   # a printed list item starts a paragraph of its own
            if not out or out[-1].kind == "title" or starts:
                out.append(Para("para", list(ln["runs"]), shown, ln["col"]))
            else:
                out[-1].runs.append((" ", False, False))
                out[-1].runs += ln["runs"]
    for p in out:
        p.runs = merge_runs(p.runs)
        if NO_STYLE["on"] and p.kind == "para":
            p.runs = ocr_italics(styled_head(ocr_paragraph(p.runs)))
    return out


STYLE_HEAD = re.compile(
    r"^\s*((?:[A-Z0-9][\w'’!-]*,?)(?:\s+(?:[A-Z0-9][\w'’!-]*,?|of|the|and|in|to|for|a|on|with|from|by|or|an|de|as)){0,7}"
    r"(?:\s*\((?:Ex|Su|Sp)(?:,\s*(?:Ex|Su|Sp))*\))?)\s*(?::(?=\s|$)|(?<=\))(?=\s+[A-Z]))")


OCR_PHRASES = [
    (re.compile(r"\ba s\b"), "as"),                                                       # "a s well a s": the layer spaces some words out
    (re.compile(r"\b[mn]d level\b"), "2nd level"),                                        # "At md level" (2nd)
    (re.compile(r"Advanced Players Guide"), "Advanced Player's Guide"),
    (re.compile(r"(Inner Sea World Guide) (\d\d) (\d)\)"), r"\1 \2\3)"),
    (re.compile(r"\(Advanced (\d\d)\) Players Guide 1 "), r"(Advanced Player's Guide 1\1) "),        # the page number of a citation set a line below its title
    # an em dash that the layer sets as a hyphen between two words (the page prints "pain\u2014a method")
    (re.compile(r"\b(creature|accessory|coat|feat|pain|might|properly)-(even|such|can|two|a|if|give)\b"), "\\1\u2014\\2"),
    (re.compile(r"\bloaded-in the\b"), "loaded\u2014in the"),
    (re.compile(r"\bfirearmflaming burst\b"), "firearm flaming burst"),
    (re.compile(r"paladin code-? ?each paladin"), "paladin code\u2014each paladin"),
    (re.compile(r"the very largest-? ?cannons"), "the very largest\u2014cannons"),
    (re.compile(r"attacks the seal breaker's foes"), "attacks the seal-breaker's foes"),
    (re.compile(r"reduced by half In addition"), "reduced by half. In addition"),
    (re.compile(r"level- 1 as his"), "level - 1 as his"),
    (re.compile(r"Spells car\b"), "Spellscar"),
    (re.compile(r"1st-protection \.?from evil; 2nd-al\(gn weapon, magic circle against evil; 4th-? ?dimensional anchor, dismissal"),
     "1st\u2014protection from evil; 2nd\u2014align weapon, magic circle against evil; 4th\u2014dimensional anchor, dismissal"),
    # a word that the layer lost at a line end: "or" before "perform" / "increases" (Gun Scavenger, Change Out)
    (re.compile(r"full-round action, perform the change out"), "full-round action, or perform the change out"),
    (re.compile(r"one die size; increases"), "one die size; or increases"),
]


def ocr_paragraph(runs: list[tuple[str, bool, bool]]) -> list[tuple[str, bool, bool]]:
    out = []
    for t, b, i in runs:
        t = re.sub(r"\s+", " ", t)
        for pat, rep in OCR_PHRASES:
            t, n = pat.subn(rep, t)
            OCR_HITS[(OCR_BOOK["name"], pat.pattern)] += n
        out.append((t, b, i))
    return out


# Repairs of text that the text layer breaks across two paragraphs (a line beside art starts a paragraph of its own): applied to the joined text.
OCR_JOINED = [
    (re.compile(r"\(DC 10 \+ the Spellscar drifter.s base attack bonus\) = reduces"), "(DC = 10 + the Spellscar drifter's base attack bonus) reduces"),
]

OCR_BOOK = {"name": ""}        # the book of the run: a hit counts for the book that read it, so a run over several books cannot hide a dead pattern of one of them (review of #356)
OCR_HITS: Counter = Counter()          # how often each OCR_PHRASES and OCR_ITALICS pattern matched in this run


def dead_ocr_patterns() -> list[str]:
    """The patterns of `OCR_PHRASES` and `OCR_ITALICS` that matched nothing in a run over the whole book: a repair that fails silently
    (the text layer spells the words another way) leaves the OCR text in the entry, so a dead pattern fails the run."""
    return [pat.pattern for pat in [p for p, _ in OCR_PHRASES + OCR_JOINED] + OCR_ITALICS if OCR_HITS[(OCR_BOOK["name"], pat.pattern)] == 0]


# Italics that print sets and that the text layer lacks (spells, magic weapon abilities, a book title in a citation): the span that the group
# `i` of each pattern names is italic. Read from the pages of the book.
OCR_ITALICS = [
    re.compile(r"enhancements for 1 round per gunslinger level: (?P<i>distance, flaming, glamered), or (?P<j>thundering)\."),
    re.compile(r"grant the firearm (?P<i>flaming burst) or (?P<j>stalking)\."),
    re.compile(r"1st\u2014(?P<i>protection from evil); 2nd\u2014(?P<j>align weapon, magic circle against evil); 4th\u2014(?P<k>dimensional anchor, dismissal)"),
    re.compile(r"ability to cast (?P<i>misdirection) on herself"),
    re.compile(r"as if using the spell (?P<i>see invisibility)"),
    re.compile(r"replicates the spell (?P<i>dance of a hundred cuts)"),
    re.compile(r"replicate (?P<i>dance of a thousand cuts)(?: \(Ultimate Magic 216\))? with"),
    re.compile(r"\((?P<i>Advanced Player's Guide) 150\)"),
    re.compile(r"as if it had the (?P<i>holy) weapon special ability"),
]


# The repairs of the Monster Codex (read from the page images); `configure_book` swaps them in for the Inner Sea Combat lists above
ISC_OCR = (OCR_PHRASES, OCR_JOINED, OCR_ITALICS)
MC_OCR_PHRASES = [
    (re.compile(r"\{(?=(?:Ex|Su|Sp)\))"), "("),                        # "Inspire Fervor {Ex):"
    (re.compile(r"\bat md level\b"), "at 2nd level"),                    # "replaces the discovery at md level" (Alchemical Trapper)
    (re.compile(r"\banti paladin"), "antipaladin"),                       # the layer breaks the word (Fearmonger)
]
MC_OCR_JOINED: list = [
    (re.compile(r"\(DC 10 \+ 1/2 the ancient guardian's druid level \+ her Wisdom = modifier\)"), "(DC = 10 + 1/2 the ancient guardian's druid level + her Wisdom modifier)"),
    (re.compile(r"\bwith its el\(Each"), "with itself. Each"),           # "does not stack with itself. Each time" (Troll Fury's Mark)
]
MC_OCR_ITALICS: list = [
    re.compile(r"see the (?P<i>atonement) spell on page 245 of the (?P<j>Pathfinder RPG Core Rulebook)\)"),
    re.compile(r"functions as (?P<i>beast shape II),"),
    re.compile(r"under the effects of (?P<i>speak with animals)\."),
    re.compile(r"in order to cast (?P<i>calm emotions)\."),
    re.compile(r"the DC of a (?P<i>calm emotions) spell"),
    re.compile(r"acts as the spell (?P<i>polymorph any object),"),
    re.compile(r"Unlike (?P<i>polymorph any object),"),
]
# The OCR books of the layout pass (batch of 2026-11-27): each has its own repairs (phrases, joined-text repairs, italics), read from its page images
# The scanned books of the second layout pass (2026-11-27): one repair set each (empty until the pages are read)
GH_OCR: tuple = ([
    (re.compile(r"\bB onus Languages:"), "Bonus Languages:"), (re.compile(r"Primal B ond \(Ex\):"), "Primal Bond (Ex):"),
    (re.compile(r"(?<=[a-z])B\d?\u2022\."), "."), (re.compile(r"(?<=[a-z])B\d?\u2022"), "."), (re.compile(r"(?<=[a-z])B\d?['\u2019]?(?![A-Za-z])"), ""),     # the superscript Bestiary marks ("DimorphodonB4\u2022.")
    (re.compile(r"(?<=[a-z])A\u2022G"), ""), (re.compile(r"\bit-she\b"), "it\u2014she"), (re.compile(r"herself She can"), "herself. She can"),
    (re.compile(r"^Limb- Climber"), "Limb-Climber"), (re.compile(r"^Summon Nature's Ally 1:"), "Summon Nature's Ally I:"), (re.compile(r"_giant form (1|II)\b"), lambda m: "giant form " + ("I" if m.group(1) == "1" else "II")),
], [], [
    re.compile(r"adds (?P<i>enlarge person) to her"), re.compile(r"cast (?P<i>enlarge person)[. ]"), re.compile(r"target it with (?P<i>enlarge person) even"),
    re.compile(r"as the (?P<i>alter self) spell"), re.compile(r"functions as (?P<i>giant form I+)\b"), re.compile(r"using (?P<i>summon nature's ally) spells"),
    re.compile(r"^(?P<i>Summon Nature's Ally [IVX]+:)"),
])           # Giant Hunter's Handbook
KG_OCR: tuple = ([
    (re.compile(r"\( (Ex|Su|Sp)\)"), r"(\1)"), (re.compile(r"\{(?=Su\))"), "("), (re.compile(r"\bweapon training z\b"), "weapon training 2"), (re.compile(r"\+z shield"), "+2 shield"),
    (re.compile(r"\+id6\b"), "+1d6"), (re.compile(r"\bofDisable\b"), "of Disable"), (re.compile(r"\bhalfher\b"), "half her"), (re.compile(r"\badj acent\b"), "adjacent"),
    (re.compile(r"\bcla s s\b"), "class"), (re.compile(r"\bweap ons\b"), "weapons"), (re.compile(r"\bafilicted\b"), "afflicted"), (re.compile(r"\bhersel\b"), "herself"),
    (re.compile(r"\bmes (sage|sengers)\b"), r"mes\1"), (re.compile(r"\btoo[\u00ad-] ?overwhelming\b"), "too\u2014overwhelming"), (re.compile(r"\bchoice-usually\b"), "choice\u2014usually"), (re.compile(r"\bu s e ranger traps\b"), "use ranger traps"),
    (re.compile(r"\bofranger\b"), "of ranger"), (re.compile(r"\bofhostile\b"), "of hostile"),
    (re.compile(r"herself\( Most"), "herself. Most"), (re.compile(r"\badd s\b"), "adds"), (re.compile(r"\btrap s\b"), "traps"),
    (re.compile(r"\(\?th, 11th"), "(7th, 11th"), (re.compile(r"\bD C\b"), "DC"),
], [], [
    re.compile(r"generate a (?P<i>sanctuary) effect"), re.compile(r"action to (?P<i>teleport) herself"), re.compile(r"page 75 of the (?P<i>Core Rulebook)\)"),
])           # Kobolds of Golarion
PS_OCR: tuple = ([
    (re.compile(r"\ba is-foot-radius\b"), "a 15-foot-radius"), (re.compile(r"\bisth level\b"), "15th level"), (re.compile(r"\bmagic-whenever\b"), "magic\u2014whenever"),
    (re.compile(r"\bSummer born\b"), "Summerborn"), (re.compile(r"\bGolarion-wielding\b"), "Golarion\u2014wielding"),
    (re.compile(r"^Def1ectin1J Arrow"), "Deflecting Arrow"), (re.compile(r"^HamperinlJ Strike"), "Hampering Strike"), (re.compile(r"^PinninlJ Strike"), "Pinning Strike"),
], [(re.compile(r"Two- Weapon Fighting feats"), "Two-Weapon Fighting feats")], [
    re.compile(r"of the (?P<i>Pathfinder RPG Advanced Player's Guide) for more details"),
])           # People of the Stars
CB_OCR: tuple = ([
    (re.compile(r"^BindinlJ Contract"), "Binding Contract"), (re.compile(r"^Counterar3ument"), "Counterargument"), (re.compile(r"\bJJeas\b"), "geas"),
], [(re.compile(r"\bifhe\b"), "if he"), (re.compile(r"\bifit\b"), "if it")], [
    re.compile(r"acts as (?P<i>lesser geas),"), re.compile(r"effect acts as (?P<i>geas/quest) \(no HD"), re.compile(r"with a (?P<i>geas)\. This acts"), re.compile(r"The (?P<i>geas) is discharged"),
    re.compile(r"trap \((?P<i>Pathfinder RPG Ultimate Magic) 65\)"), re.compile(r"^(?P<i>Ultimate Magic) 64\)"),
])           # Champions of Balance
BG_OCR: tuple = ([
    (re.compile(r"Bardic Per formance:"), "Bardic Performance:"), (re.compile(r"\bme lee\b"), "melee"), (re.compile(r"\(D C ="), "(DC ="),
    (re.compile(r"\bhalf-ores\b"), "half-orcs"), (re.compile(r"archetype :"), "archetype:"),
], [], [])           # Bastards of Golarion
KI_OCR: tuple = ([
    (re.compile(r"\{(?=Su\))"), "("), (re.compile(r"\badj acent\b"), "adjacent"), (re.compile(r"\bclas s\b"), "class"), (re.compile(r"\bsubj ected\b"), "subjected"),
    (re.compile(r"\bj ourneys\b"), "journeys"), (re.compile(r"\bofbeing\b"), "of being"), (re.compile(r"\bD exterity\b"), "Dexterity"), (re.compile(r"\bwishe s\b"), "wishes"),
    (re.compile(r"\bcast toniJues on\b"), "cast tongues on"), (re.compile(r"nimble \+L\.?"), "nimble +1."), (re.compile(r"(?<=[a-z]) \.(?=\s|$)"), "."),
    (re.compile(r"\btwo -handed\b"), "two-handed"), (re.compile(r"\bpair 0 f deeds\b"), "pair of deeds"),
], [], [
    re.compile(r"cast (?P<i>tongues) on herself"), re.compile(r"replaces (?P<i>detect evil)\."), re.compile(r"\(see (?P<i>Ultimate Equipment)\)"),
])           # Knights of the Inner Sea
PR_OCR: tuple = ([
    (re.compile(r"\bmd-doom\b"), "2nd\u2014doom"), (re.compile(r"\b(\d+(?:st|nd|rd|th))-(?=(?:obscure|commune|repulsion|shapechan))"), "\\1\u2014"), (re.compile(r"shapechan!Je"), "shapechange"),
    (re.compile(r"VengeanceuM"), "Vengeance"), (re.compile(r"\bAt md level\b"), "At 2nd level"), (re.compile(r"\bof(Gyronna)"), r"of \1"), (re.compile(r"increases by L The DC"), "increases by 1. The DC"),
    (re.compile(r"lethal accuracyuc"), "lethal accuracy"), (re.compile(r"poisons-brewing"), "poisons\u2014brewing"), (re.compile(r"2nd- and ioth-level"), "2nd- and 10th-level"),
    (re.compile(r"level\+ the barbarian"), "level + the barbarian"),
], [], [
    re.compile(r"2nd\u2014(?P<i>doom), 6th\u2014(?P<j>obscure object), 10th\u2014(?P<k>commune), 14th\u2014(?P<l>repulsion), 18th\u2014(?P<m>shapechange)"),
    re.compile(r"^(?P<i>(?:Major |Grand )?Hexes:)(?! The following)"), re.compile(r"\(Pathfinder RPG (?P<i>Bestiary) 215\)"), re.compile(r"located in the (?P<i>Pathfinder RPG Advanced Player's Guide)\."),
])           # People of the River
AA_OCR: tuple = ([
    (re.compile(r"(?<=[a-z])Ar[cG]\b"), ""),                                  # the superscript mark of a book ("beast totemAPG", read "Arc", "ArG") is no text
    (re.compile(r"\bLe9erdemain\b"), "Legerdemain"), (re.compile(r"\bmd, 6th\b"), "2nd, 6th"), (re.compile(r"\b19tli\b"), "19th"), (re.compile(r"\b2 0th\b"), "20th"),
], [], [])           # Animal Archive
TG_OCR: tuple = ([
    (re.compile(r"^Class skills:"), "Class Skills:"), (re.compile(r"\{(?=Su\))"), "("), (re.compile(r"\bweater make whole\b"), "greater make whole"),
    (re.compile(r"\bofbludgeoning\b"), "of bludgeoning"), (re.compile(r"\bofbeneficial\b"), "of beneficial"), (re.compile(r"\bofkeeping\b"), "of keeping"),
    (re.compile(r"\bweapon training L\b\.?"), "weapon training 1."), (re.compile(r"\bover 100 as loo\b"), "over 100 as 100"),
], [], [
    re.compile(r"cast (?P<i>make whole) and (?P<j>greater make whole) in place of (?P<k>cure/ ?inflict moderate wounds) and (?P<l>cure/ ?inflict critical wounds)"),
])           # Technology Guide
HH_OCR: tuple = ([
    (re.compile(r"Smitin9"), "Smiting"), (re.compile(r"ali9nment"), "alignment"),
    (re.compile(r"\b(flamin|returnin|seekin|shockin)IJ\b"), lambda m: m.group(1) + "g"), (re.compile(r"\bretumin,g\b"), "returning"), (re.compile(r"\bener,gy\b"), "energy"),
    (re.compile(r"\bd2o\b"), "d20"), (re.compile(r"\(to a maximum of \+s at 20th level\)"), "(to a maximum of +5 at 20th level)"),
    (re.compile(r"\balignment-such\b"), "alignment\u2014such"), (re.compile(r"\bcard-the summoner\b"), "card\u2014the summoner"),
    (re.compile(r"\bactivity-attack rolls\b"), "activity\u2014attack rolls"), (re.compile(r"\bsaving throw-equal\b"), "saving throw\u2014equal"),
    (re.compile(r"\bifhe\b"), "if he"), (re.compile(r"\+the monk's Wisdom"), "+ the monk's Wisdom"), (re.compile(r"\ba \+ 1 sacred\b"), "a +1 sacred"),
    (re.compile(r"\(see page is\)"), "(see page 15)"), (re.compile(r"\bx3\b"), "\u00d73"), (re.compile(r"\bprophecyuM\b"), "prophecy"),
], [(re.compile(r"\bifit\b"), "if it")], [
    re.compile(r"curse her target as the (?P<i>bestow curse) spell"), re.compile(r"as per the (?P<i>baleful)\s*$"), re.compile(r"^(?P<i>polymorph) spell\. This ability replaces"),
    re.compile(r"ranged weapons: (?P<a>brilliant energy), (?P<b>distance), (?P<c>flaming), (?P<d>flaming burst), (?P<e>frost), (?P<f>icy burst), (?P<g>returning), (?P<h>seeking), (?P<i>shock), (?P<j>shocking burst), and (?P<k>speed)\."),
    re.compile(r"special ability, such as (?P<i>flaming), must share"), re.compile(r"warded by (?P<i>protection from evil) and similar"),
    re.compile(r"for his (?P<i>summon monster) spell-like"), re.compile(r"gains the (?P<i>returning) weapon special ability"),
])         # The Harrow Handbook
DH_OCR: tuple = ([
    (re.compile(r"\bs park\b"), "spark"), (re.compile(r"\bs peak with animals\b"), "speak with animals"),      # the layer sets the first letter of an italic spell name apart
    (re.compile(r"\bhalfher\b"), "half her"), (re.compile(r"\bAt md level\b"), "At 2nd level"), (re.compile(r"\bher md-level\b"), "her 2nd-level"),
    (re.compile(r"\bTriIJIJer\b"), "Trigger"), (re.compile(r"\{(?=Su\))"), "("),
    (re.compile(r"\bwithin is feet\b"), "within 15 feet"), (re.compile(r"\bsetting it off The trap\b"), "setting it off. The trap"),
], [], [
    re.compile(r"can cast (?P<i>spark) as a"), re.compile(r"can use (?P<i>speak with animals) at will"), re.compile(r"source of (?P<i>raise dead)\."),
    re.compile(r"benefits of (?P<i>spider climb) for 1 round"), re.compile(r"as if using the spell (?P<i>passwall) with"), re.compile(r"per the spell (?P<i>earthquake),"),
    re.compile(r"the qualities (?P<i>Trigger): location and (?P<j>Reset): none"),
])         # Dungeoneer's Handbook
OCR_SETS: dict = {"monster-codex": (MC_OCR_PHRASES, MC_OCR_JOINED, MC_OCR_ITALICS), "dungeoneers-handbook": DH_OCR, "the-harrow-handbook": HH_OCR, "technology-guide": TG_OCR, "animal-archive": AA_OCR, "giant-hunters-handbook": GH_OCR, "kobolds-of-golarion": KG_OCR, "people-of-the-stars": PS_OCR, "champions-of-balance": CB_OCR, "bastards-of-golarion": BG_OCR, "knights-of-the-inner-sea": KI_OCR, "people-of-the-river": PR_OCR}
OCR_TITLES = {"on": False}      # the title of an archetype may be followed by a mangled class and "Archetype" (Dungeoneer's Handbook)
TITLE_CONTAINS = {"on": False}  # Heroes of Golarion: the decorative chapter title and the title of the archetype stand on one line ("ofTHeorld SPEAKER OF THE PALATINE EYE (BARD ARCHETYPE)")
OCR_GLUE = {"on": False}        # a word that the layer glued to "of" or "if" ("ofher", "ifthe") is split


def ocr_italics(runs: list[tuple[str, bool, bool]]) -> list[tuple[str, bool, bool]]:
    out = []
    for t, b, i in runs:
        for pat in OCR_ITALICS:
            OCR_HITS[(OCR_BOOK["name"], pat.pattern)] += len(pat.findall(t))
        spans = sorted((m.start(g), m.end(g)) for pat in OCR_ITALICS for m in pat.finditer(t) for g in pat.groupindex)
        if i or not spans:
            out.append((t, b, i))
            continue
        at = 0
        for a, z in spans:
            out += [(t[at:a], b, i), (t[a:z], b, True)]
            at = z
        out.append((t[at:], b, i))
    return [r for r in out if r[0] != ""]


# a line that starts like a head and is a list item ("Summon Nature's Ally II: Dimorphodon", an italic line of the Goliath Druid)
NOT_STYLE_HEAD = re.compile(r"Summon Nature['\u2019]s Ally [IVX1]+:|(?:Major |Grand )?Hexes:(?! The following)")


def styled_head(runs: list[tuple[str, bool, bool]]) -> list[tuple[str, bool, bool]]:
    """Inner Sea Combat has no bold runs: a paragraph that starts with a name and a colon ("Clean Capture (Ex): At 1st level") gets
    that name as its bold head."""
    text = "".join(t for t, _, _ in runs)
    m = STYLE_HEAD.match(text)
    if not m or len(m.group(1)) > 60 or NOT_STYLE_HEAD.match(text):
        return runs
    return [(text[:m.end(1)], True, False), (text[m.end(1):], False, False)]


CLASS_TITLES = {squash(x) for x in (
    "Alchemist", "Antipaladin", "Barbarian", "Bard", "Cavalier", "Cleric", "Druid", "Fighter", "Gunslinger", "Inquisitor",
    "Magus", "Monk", "Oracle", "Paladin", "Ranger", "Rogue", "Sorcerer", "Summoner", "Witch", "Wizard", "Archetypes")}


# a title that names a type of rules ("ORDER OF THE SHROUD (CAVALIER ORDER)", "NEW WILD TALENTS (KINETICIST)") ends the
# section of an archetype: it is the next entry of the book, not a sidebar of this one
TYPE_TITLE = re.compile(r"\([A-Za-z][A-Za-z' -]{3,}\)\s*$")           # the Advanced Player's Guide sets titles in mixed small caps

CLASS_NAMES = ("Alchemist", "Antipaladin", "Arcanist", "Barbarian", "Bard", "Bloodrager", "Brawler", "Cavalier", "Cleric", "Druid", "Fighter",
               "Gunslinger", "Hunter", "Inquisitor", "Investigator", "Kineticist", "Magus", "Medium", "Mesmerist", "Monk", "Occultist", "Oracle",
               "Paladin", "Psychic", "Ranger", "Rogue", "Shaman", "Skald", "Slayer", "Sorcerer", "Spiritualist", "Summoner", "Swashbuckler",
               "Vigilante", "Warpriest", "Witch", "Wizard", "Ninja", "Samurai")
CLASS_SUFFIX = re.compile(r"\s*\((?:" + "|".join(CLASS_NAMES) + r")(?: or (?:" + "|".join(CLASS_NAMES) + r"))?\)\s*$")      # "Scroll Scholar (Cleric or Wizard)": an archetype of two classes (Pathfinder Society Field Guide)
# the squashed rest of a title after the name of the archetype, when the book prints the class in small capitals with stray blanks
# ("PROWLER AT WOR LD'S END (BLOODR AGER)", "THRONEWARDEN (GUNSLINGER A) RCHETYPE"): the class, or the class and "archetype"
CLASS_REMAINDERS = {squash(c) for c in CLASS_NAMES} | {squash(c) + "archetype" for c in CLASS_NAMES} | {squash(a) + "or" + squash(b) for a in CLASS_NAMES for b in CLASS_NAMES if a != b}


# The titles of archetypes that print sets in the section of the archetype before them and that the corpus holds as headed
# prose of another entry (the Advanced Player's Guide's Totem Warrior and Animal Shamans): they end a section too.
UNTYPED_ARCHETYPE_TITLES = {squash(x) for x in ("Totem Warrior", "Animal Shamans", "Patron Familiars")}


# The Adventurer's Guide sets each archetype at the end of the chapter of a Pathfinder Society faction, followed by the faction's
# affiliation, equipment, feats, magic items and spells; the Ultimate Wilderness sets a race's equipment, feats, magic items and
# spells after the archetype of its chapter. These titles are the next section of the book, not a sidebar of the archetype.
SECTION_STOP = re.compile(r"^(?:AFFILIATION\b|.*\bAFFILIATION$|EQUIPMENT\b|FEATS?\b|MAGIC ITEMS?\b|SPELLS?$|CLASS OPTIONS?\b|"
                          r"VIGILANTE CLASS OPTION|INVESTIGATOR TALENTS|[A-Z]+ (?:EQUIPMENT|FEATS|MAGIC ITEMS?|SPELLS?)$)")
SECTION_STOPS = {"on": False}
# Blood of the Ancients: no archetype holds a box or a heading of its own, and what follows each one (a spell, a feat, a trait, an
# item of the chapter) has a title of its own: any title ends the section.
ANY_TITLE_ENDS = {"on": False}
# ... except the box of rules that an archetype carries as part of itself (owner ruling 41; the Invested Regent's Vested Powers and its lists of
# powers per level, Heroes of the High Court pp. 22-23): squashed titles that do not end the section even then.
STAYS_EXTRA = {"set": frozenset()}      # titles that stay inside the section of an archetype in the book at hand (Blood of Shadows: the "Discoveries" of the Gloom Chymist)
ANY_TITLE_STAYS = re.compile(r"^(?:\d+(?:st|nd|rd|th)level)?vestedpowers$")
# Blood of the Ancients sets its titles in small capitals (a capital and its small capitals sit 5 units apart in one family of type), and
# a chapter title that a page repeats unseen over the first lines of a column. Other books read as before.
SMALL_CAP_TITLES = {"on": False}
# Wilderness Origins, Legacy of the First World, People of the Wastes and Healer's Handbook set the title of a chapter-opening page
# above the body (top < `BODY_TOP[0]`) in type of 40 or more, so that the first lines of a column sit below it. The title ends a section.
CHAPTER_TITLES = {"on": False}
# Campaign Setting books (Inner Sea Magic, Inner Sea Intrigue): an illustration's caption in large type stands in the margin beside the
# column; it is not a title and must not end the section of the archetype.
MARGIN_CAPTIONS = {"on": False}
ITALIC_FIRST = {"on": False}            # the Campaign Setting books: the first letter of an italic word that the layer set apart ("s" + "un orchid elixir")
LOWERCASE_CONTINUES = {"on": False}      # the Campaign Setting books: no paragraph starts in lower case
RULE57_TRADE_LEVELS = {("ref/arc-warpriest/proselytizer", "emotional-appeal")}     # ruling 57: the lowest level across its trades, the bonus feat at 3rd (review of #347)
RULE57 = {"on": True}           # owner ruling 57 (the level of a whole class feature at any level); `--rules` could turn it off
LIST_CONTINUES = {"on": False}  # a line of a list item that print wraps without a bullet continues the item (Potions and Poisons: the bullets hang)
BULLETS = {"on": False}         # a line that starts with a bullet starts a list item (Inner Sea Intrigue "Tinkering")
MC_TITLES = {"on": False}       # Monster Codex: "Alchemical Trapper (Alchemist)" in a face of its own, no larger than the text
MC_TITLE_FAMILIES = ("Fd5569-Identity-H", "Fd1093040-Identity-H")
CLASS_ALT = "Alchemist|Antipaladin|Barbarian|Bard|Bloodrager|Cavalier|Cleric|Druid|Fighter|Gunslinger|Inquisitor|Investigator|Magus|Monk|Oracle|Paladin|Ranger|Rogue|Sorcerer|Summoner|Witch|Wizard|Warpriest|Shaman|Skald|Slayer|Swashbuckler|Arcanist|Brawler|Hunter"
CAPS_TITLE = re.compile(r"[A-Z0-9'\u2019 \-!.]+\([A-Z ]+ ARCHETYPE\)")
CAPS_TITLE_HEAD = re.compile(r"[A-Z0-9'\u2019 \-!.]+\([A-Z ]+")
CAPS_TITLE_TAIL = re.compile(r"ARCHETYPE\)")
ARCHETYPE_CAPS = {"on": False}  # Heroes of the Darklands: a title in capitals "(CLASS ARCHETYPE)" one size above the text is a title
NO_STYLE = {"on": False}        # Inner Sea Combat: the text layer has no bold or italic runs; a head is told by its shape
CAPTIONS = {"on": False}        # the same books: a title that repeats the archetype's own name in large type is an illustration's caption

# A title with a parenthesized type that does not end the section: the box of rules that the archetype uses (owner ruling 41;
# Elemental Aspects of the Elementalist Shifter, Ultimate Wilderness pp. 78-80, "(Elementalist Shifter Aspects)")
KEEP_TITLES = {squash("Elemental Aspects (Elementalist Shifter Aspects)")}


def k_is_class_free(sp: str) -> bool:
    return sp not in CLASS_TITLES


# an archetype whose span ends in the middle of a paragraph: the squashed title and the text at which the span ends (Kobolds of Golarion p. 23)
SPAN_COL_ONLY = {"seasonkeeper", "qabaratoutrider"}
SPAN_CUT = {"swarmfighter": " You empower spells using the ancient language of dragons.", "galvanicsaboteur": " Riverfolk and Numerians pursue magic"}


class Section(list):
    """The blocks of an archetype's print span; `end` is the title that ended it (None: the blocks ran out), `end_known` whether a rule
    names that title as the start of another section of the book."""
    end: str | None = None
    end_known: bool = True


# Blood of the Ancients: the titles that start the next section of its chapter (rule 5: any other title that ends an archetype is a
# table or a box that the entry may lack).
CHAPTER_SECTION_TITLE = re.compile(r"(?i)(?:^|\s)(?:traits?|spells?|feats?|runes|rituals|magic items?|price|fighter style|philosophy|"
                                   r"tricks|talents|options|vested feats|favors|masterpieces|protective hexes|bloodlines|techniques|"
                                   r"(?:advanced )?weapon training|style strikes|ki powers|discoveries|toxic heritages|hexes|sagas|[a-z-]+ equipment|[a-z-]+ weapons|"
                                   r"[a-z-]+ combat|nagaji|vishkanyas|gripplis)$|^items from\b|^rituals of\b")
# the same, in the letters of a title that the book sets in small capitals with stray blanks ("ST YLE ST RIKES")
CHAPTER_SECTION_SQUASHED = re.compile(r"(?:stylestrikes|unarmedmastery|improvisedstyle|improvisedfeats|newstyles|archetypes)$")


# The start of a title that the layer reads too badly for `ocr_title_close` (Technology Guide p. 12: "[ybl!r\u00b7Soldil!r [Fightl!r nr\ufffdh1!typ1!]" for "Cyber-Soldier (Fighter Archetype)"), squashed.
OCR_TITLE_ALIASES = {"cybersoldier": "yblrsoldilr", "maddog": "maodoc", "qabaratoutrider": "onenrntoutrider", "seasonkeeper": "sejlsdnkeeper", "heraldsquire": "heratosou1re"}


def ocr_title_close(seen: str, key: str) -> bool:
    """The start of an OCR title against the title of the entry: the layer reads a letter for another ("CARO CA STER" for "Card Caster", "SU1T" for "Suit"), so up to a fifth of the letters may differ."""
    import difflib
    fold = str.maketrans({"1": "i", "l": "i", "0": "o", "5": "s"})
    return difflib.SequenceMatcher(None, seen.translate(fold), key.translate(fold)).ratio() >= 0.8


def find_section(blocks: list[Para], title: str, stops: set[str] | None = None) -> list[Para] | None:
    """The blocks of an archetype: from its title to the next title of another archetype or of a class. Another
    title in between (a sidebar, a table heading) is a heading of the section. With no `stops`, the next title of
    any kind ends it."""
    key = squash(re.sub(r"\s*\([A-Z]{2,4}\)\s*$", "", title))        # "Ringleader (UI)": the corpus's mark of a second archetype of the name
    for i, b in enumerate(blocks):
        # Ultimate Magic and Ultimate Combat print "REANIMATOR (ARCHETYPE)"; Occult Adventures and Ultimate Intrigue print the
        # class on a second line ("ECTOCHYMIST (ALCHEMIST ARCHETYPE)"); the Advanced Race Guide "Saboteur (Alchemist)"
        sp = squash(b.plain()) if b.kind == "title" else ""
        if CAPTIONS["on"] and b.kind == "title" and b.size >= 20 and k_is_class_free(sp):
            continue                    # an illustration's caption in large type is not the title of the archetype
        if b.kind == "title" and (sp in (key, key + "archetype") or squash(CLASS_SUFFIX.sub("", b.plain())) == key
                                  or (sp.startswith(key) and sp[len(key):] in CLASS_REMAINDERS) or (
                sp.startswith(key) and sp.endswith("archetype") and len(sp) <= len(key) + len("archetype") + 24)
                                  or (OCR["on"] and OCR_TITLES["on"] and sp.startswith(OCR_TITLE_ALIASES.get(key, "\0")))
                                  or (OCR["on"] and OCR_TITLES["on"] and sp.startswith(key) and len(sp) <= len(key) + 26)
                                  or (OCR["on"] and OCR_TITLES["on"] and len(key) >= 8 and len(sp) <= len(key) + 26 and ocr_title_close(sp[:len(key)], key))
                                  or (TITLE_CONTAINS["on"] and key in sp and sp.endswith("archetype") and len(sp) <= len(key) + len("archetype") + 70)):     # a chapter title or a box title run into the line of the title      # an OCR title: "TERRA- COTTA MoNK (MoNK AACHETYPE)"
            j = i + 1
            out = Section([b])
            while j < len(blocks):
                nxt = blocks[j]
                if nxt.kind == "title":
                    k = squash(nxt.plain())
                    if CAPTIONS["on"] and nxt.size >= 20 and k not in CLASS_TITLES and (k == key or (stops is not None and k in stops)):
                        j += 1                  # the caption of an illustration repeats an archetype's name in large type (it can stand in the
                        continue                # section of the archetype before it): not a title
                    # another archetype, a class, a chapter title (a larger font) or a title of a type of rules ends the
                    # section; so does the "NEW RACIAL RULES" title that follows the archetypes of a race chapter
                    any_ends = ANY_TITLE_ENDS["on"] and not ANY_TITLE_STAYS.match(k) and k not in STAYS_EXTRA["set"]
                    if (stops is None or any_ends or k in stops or k.endswith(("archetype", "mystery", "bloodline")) or nxt.size >= 30 or (ARCHETYPE_CAPS["on"] and nxt.size >= 20)
                            or CLASS_SUFFIX.search(nxt.plain()) or k == "newracialrules" or (TYPE_TITLE.search(nxt.plain()) and k not in KEEP_TITLES)
                            or (SECTION_STOPS["on"] and SECTION_STOP.match(re.sub(r"\s+", " ", nxt.plain()).strip()))):
                        out.end = nxt.plain().strip()
                        ocr_stop = OCR["on"] and OCR_TITLES["on"] and stops is not None and any(
                            len(t) >= 8 and (ocr_title_close(k[:len(t)], t) or k.startswith(next((a for c, a in OCR_TITLE_ALIASES.items() if c == t), "\0"))) for t in stops)
                        out.end_known = ocr_stop or not (any_ends and stops is not None and k not in stops and not k.endswith(("archetype", "mystery", "bloodline"))
                                             and nxt.size < 30 and not CLASS_SUFFIX.search(nxt.plain()) and k != "newracialrules"
                                             and not TYPE_TITLE.search(nxt.plain()) and not CHAPTER_SECTION_TITLE.search(re.sub(r"\s+", " ", nxt.plain()).strip()) and not CHAPTER_SECTION_SQUASHED.search(k)
                                             and not MC_TITLES["on"])     # Monster Codex: every title (two faces of their own) is a section of the chapter
                        break
                    out.append(Para("para", [(t, True, i) for t, _, i in nxt.runs], nxt.page, nxt.col))
                else:
                    out.append(nxt)
                j += 1
            if key in SPAN_COL_ONLY:
                # the archetype sits in one column, and a planet sidebar fills the other (People of the Stars): the blocks of the other
                # column are no text of the archetype (what the archetype carries over below the sidebar is a hand text)
                keep_col = out[0].col
                out[:] = [blk for blk in out if blk.col == keep_col]
                out.end, out.end_known = None, True
            cut_at = SPAN_CUT.get(key)
            if cut_at:
                # the text layer runs the first line of the next section (a feat whose title it does not read as a title) into the last
                # paragraph of the archetype: the span ends at that marker, and what follows is no text of the archetype
                for n, blk in enumerate(out):
                    if blk.kind != "para":
                        continue
                    plain = blk.plain()
                    at = plain.find(cut_at)
                    if at < 0:
                        continue
                    kept, seen = [], 0
                    for t, b, i in blk.runs:
                        if seen + len(t) <= at:
                            kept.append((t, b, i))
                        elif seen < at:
                            kept.append((t[: at - seen], b, i))
                        seen += len(t)
                    blk.runs = kept
                    del out[(n if not kept else n + 1):]
                    out.end, out.end_known = None, True
                    break
            return out
    return None


@dataclass
class PrintFeature:
    head: str
    paras: list[list[tuple[str, bool, bool]]]        # runs of each printed paragraph (the head cut off)
    page: int
    bold: bool = True                                # a bold head; an italic one is a sub-power or an option
    errata: int = 0                                  # the errata page that replaced this ability


DASH_KEY_LEAD = re.compile(r"[A-Z][A-Za-z'\u2019 -]{1,30}\u2014")
# a key "Option\u2014Name (Ex)": a printed option of a choice, one for each bloodline, domain or the like (owner ruling 53)
DASH_KEY = re.compile(r"[A-Z][A-Za-z'\u2019 -]{1,30}\u2014[A-Z].*")


def head_candidate(p: Para) -> tuple[str, list, bool] | None:
    """The leading bold (or italic) run before the colon of a paragraph, and the rest of its runs. Blanks before
    the head (a justified first line) do not count."""
    runs = list(p.runs)
    while runs and not runs[0][0].strip():
        runs.pop(0)
    if not runs:
        return None
    first = runs[0]
    style = "bold" if first[1] else ("italic" if first[2] else "")
    if not style:
        return None
    i, head = 0, ""
    while i < len(runs) and (runs[i][1] if style == "bold" else runs[i][2]):
        head += runs[i][0]
        i += 1
    rest = runs[i:]
    if style == "bold" and len(rest) > 1 and rest[0][0].strip() == "\u2014" and not rest[0][1] and rest[1][1] and DASH_KEY_LEAD.fullmatch(head.strip() + "\u2014"):
        # "Aberrant" and "Squeezer (Ex)" in bold with a dash in plain type between them: the key is "Aberrant\u2014Squeezer (Ex)"
        # (Familiar Folio p. 16, owner ruling 53)
        head = head.strip() + "\u2014" + rest[1][0].strip()
        i += 2
        rest = runs[i:]
    while head.count("(") > head.count(")") and len(rest) >= 2 and rest[0][0].strip() == "," and (rest[1][1] if style == "bold" else rest[1][2]):
        head += ", " + rest[1][0].strip()                 # "_Apothecary (Ex_, _Sp)_:": the layer breaks the tag at its comma (Black Markets p. 28)
        rest = rest[2:]
    head = re.sub(r"\s+", " ", head).strip()
    if head.count("(") > head.count(")") and rest and rest[0][0].lstrip().startswith(")"):
        # "_Cat's Charge (Ex_): " the italics end inside the parenthesis
        head += ")"
        rest = [(rest[0][0].lstrip()[1:], rest[0][1], rest[0][2])] + list(rest[1:])
    if head.endswith(":"):
        # the Advanced Class Guide and the Advanced Race Guide set the colon of a run-in head in its italics
        head = head[:-1].strip()
        rest = [(":", False, False)] + rest
    if not head:
        return None
    return head, rest, style == "bold"


UPPER_HEAD_ENDS = {"on": False}
UPPER_HEAD = re.compile(r"(?=(?:.*[A-Z]){4})[A-Z0-9 '\u2019,&:()/.\-]+")


def head_of_para(p: Para) -> str | None:
    cand = head_candidate(p)
    return cand[0] if cand and cand[2] else None


def split_print(section: list[Para], expected: list[str]) -> tuple[list[list], list[PrintFeature]]:
    """The printed opening paragraphs and the printed features of an archetype section. A bold paragraph
    start is a head; an italic one is a head only when it is the next name that the entry expects."""
    want = [namekey(n) for n in expected]
    opening: list[list] = []
    feats: list[PrintFeature] = []
    for p in section[1:]:
        cand = head_candidate(p)
        if UPPER_HEAD_ENDS["on"] and feats and cand and cand[2] and UPPER_HEAD.fullmatch(cand[0]) and namekey(cand[0]) not in want:
            break           # the Villain Codex sets the equipment, the spells, the magic items and the statistics of the villain's crew behind the archetype under heads in capitals
        is_head = False
        if cand:
            head, rest, bold = cand
            colon = rest and rest[0][0].lstrip().startswith(":") if rest else False
            tail_ok = not rest or colon or (bold and namekey(head) in want)     # print leaves out a colon here and there
            if tail_ok and (bold or (namekey(head) in want)):
                is_head = True
        if is_head:
            head, rest, _ = cand
            rest = list(rest)
            if rest and rest[0][0].lstrip().startswith(":"):
                t = rest[0][0].lstrip()[1:]
                rest[0] = (t, rest[0][1], rest[0][2])
            feats.append(PrintFeature(head, [rest] if rest else [[]], p.page, cand[2]))
        elif feats:
            feats[-1].paras.append(p.runs)
        else:
            opening.append(p.runs)
    return opening, feats


# ---- trade sentences ---------------------------------------------------------------------------------

TRADE_SUBJECT_WORDS = (r"ability|abilities|class|feature|features|power|powers|archetype|performance|performances|trick|tricks|"
                       r"talent|talents|hex|hexes|discovery|discoveries|revelation|revelations|mercy|mercies|deed|deeds|exploit|"
                       r"exploits|arcana|arcanum|feat|feats|also|otherwise|acts|works|functions|as|like|and|bonus|spells|skills")
TRADE_SENTENCE = re.compile(
    r"(?:^|(?<=[.!?]\s)|(?<=[.!?]\)\s))((?:This|These|It)\b(?:\s+(?:bonus\s+feats?\s+choices?|" + TRADE_SUBJECT_WORDS + r"))*\s+(replaces?|alters?|changes|modifies)\b[^.]*\.)",
    re.I,
)


def _trade_matches(text: str) -> list:
    """The matches of TRADE_SENTENCE. A sentence that starts after ".)" counts only when that ")" closes a "(" opened
    earlier in the text (the reader's rule of #714: "(Those marked with an asterisk are detailed in this book.) This
    alters ..."); a stray ".) This ..." starts none. "choices" is a subject word only right after "bonus feat(s)"."""
    out = []
    for m in TRADE_SENTENCE.finditer(text):
        at = m.start(1)
        if re.match(r"alter\s+self(?![-\w])", text[m.start(2):], re.I):      # R19: "functions as alter self" is the spell, not a verb ("alters self" and "alter self-" are not skipped, as in the app)
            continue
        if at >= 2 and text[at - 2] == ")" and text[at - 3:at - 2] in ".!?":
            before = text[:at - 2]
            if before.count("(") <= before.count(")"):
                continue
        out.append(m)
    return out


ABILITY_NOUN = (r"\b(?:ability|abilities|feature|features|power|powers|archetype|performances?|tricks?|talents?|hex(?:es)?|"
                r"discover(?:y|ies)|revelations?|merc(?:y|ies)|deeds?|exploits?|arcana|arcanum)\b")


def _op_of(verb: str) -> str:
    return "replaces" if verb.lower().startswith("replace") else "alters"      # rulings 25 and 55: "changes" and "modifies" are alters verbs


def _clean_phrase(phrase: str) -> str:
    phrase = phrase.strip().rstrip(".").strip()
    phrase = re.sub(r",\s+but\b.*$", "", phrase)                              # R8: the phrase ends at ", but "
    phrase = re.sub(r",\s+and\s+(?:it\s+)?counts?\s+as\b.*$", "", phrase)    # R17: ", and counts as" and ", and it counts as" end the phrase
    phrase = re.sub(r",?\s+and\s+(?:it\s+)?(?:does not|cannot)\b.*$", "", phrase)    # app #737: ", and does not", ", and it does not" and ", and cannot" end the phrase
    phrase = re.sub(r"^and functions as\s+", "", phrase)                  # app #737: "modifies and functions as X" names X
    # R9 and R18: a parenthesis of 4+ words is an aside, at the end of the phrase or inside it
    phrase = re.sub(r"\s*\(([^()]*)\)", lambda m: "" if len(m.group(1).split()) >= 4 else m.group(0), phrase)
    return phrase.strip().rstrip(".").strip()


def trade_sentences(text: str, head: str = "") -> list[tuple[str, str, bool]]:
    """[(op, phrase, bare)] of the trade sentences of a text: "This ability replaces bravery." gives
    ("replaces", "bravery", False). A bare sentence ("These replace the normal attack roll bonus.") has no
    ability, feature, power or archetype in its subject: the app counts it only when it names a stored trade.
    The reader rules of owner ruling 21 (R8, R9, R11, R12) and 25: a phrase ends at ", but "; a final parenthesis of
    four or more words is an aside; "X replaces Y and alters Z" is two sentences; the heading of the feature
    (without its ability tag) is a subject too; "changes" and "modifies" are `alters` verbs (rulings 25 and 55)."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[\\_*]", "", text)
    text = re.sub(r"\s+", " ", text)        # a paragraph break inside a sentence (a column or page break) does not end it
    out = []
    found = [(m.group(1), m.start(1)) for m in _trade_matches(text)]
    plain = ABILITY_TAG.sub("", head).strip() if head else ""
    if plain:                                 # R12
        for m in re.finditer(r"(?:^|(?<=[.!?]\s))(" + re.escape(plain) + r"\s+(?:replaces?|alters?|changes?|modifies)\b[^.]*\.)", text, re.I):
            if all(m.start(1) != at for _, at in found):
                found.append((m.group(1), m.start(1)))
    for sentence, _ in sorted(found, key=lambda x: x[1]):
        verb = re.search(r"\b(replaces?|alters?|changes?|modifies)\b", sentence, re.I)
        subject = sentence[:verb.start()]
        bare = not re.search(ABILITY_NOUN, subject, re.I) and not (plain and subject.strip().lower() == plain.lower())
        rest = sentence[verb.end():]
        # R11: two verbs, two sentences; "changes" is a verb only as the first one (owner ruling 25)
        # R16: the second clause may have a subject: ", and it replaces X" (it, this, he, she, they, with "also")
        # app #737: "and also <verb>" and ", and it also changes/modifies X" split too; "and it changes X" without "also" stays prose (ruling 25)
        subj = r"(?:(?:it|this|he|she|they)\s+)?"
        clause = r"(?:" + subj + r"also\s+(?:replaces?|alters?|changes?|modifies)|" + subj + r"(?:replaces?|alters?))"
        parts = re.split(r"\s*,?\s+and\s+(?=" + clause + r"\b)", rest, flags=re.I)
        ops = [verb.group(1)] + [re.match(r"(?:" + subj + r"(?:also\s+)?)(replaces?|alters?|changes?|modifies)", x, re.I).group(1) for x in parts[1:]]
        for op_word, part in zip(ops, parts):
            part = re.sub(r"^" + subj + r"(?:also\s+)?(?:replaces?|alters?|changes?|modifies)\b", "", part.strip(), flags=re.I) if part is not parts[0] else part
            ph = _clean_phrase(part)
            if re.search(r"\bas indicated below$", ph, re.I):      # owner ruling 40: a cross-reference, like "(see ...)"; it stores no trade
                continue
            out.append((_op_of(op_word), ph, bare))
    return out


ORDINAL_WORDS = {"first": "1st", "second": "2nd", "third": "3rd", "fourth": "4th", "fifth": "5th", "sixth": "6th",
                 "seventh": "7th", "eighth": "8th", "ninth": "9th", "tenth": "10th", "eleventh": "11th", "twelfth": "12th",
                 "thirteenth": "13th", "fourteenth": "14th", "fifteenth": "15th", "sixteenth": "16th",
                 "seventeenth": "17th", "eighteenth": "18th", "nineteenth": "19th", "twentieth": "20th"}      # R3
CLASS_WORDS = {"alchemist", "barbarian", "bard", "cavalier", "cleric", "druid", "fighter", "gunslinger", "inquisitor",
               "magus", "monk", "oracle", "paladin", "ranger", "rogue", "sorcerer", "summoner", "witch", "wizard", "both"}


_ORD_STEM = re.compile(r"^(?:(?:the|a|an)\s+)?\d+(?:st|nd|rd|th)-$", re.I)
_ORD_FULL = re.compile(r"^(?:(?:the|a|an)\s+)?\d+(?:st|nd|rd|th)-(\S+(?:\s+.*)?)$", re.I)


def expand_suspended(text: str) -> str:
    """The app's list expansion of suspended hyphens (app #727): each suspended item takes the tail of the next full item after it, so
    "the 4th- and 14th-level vigilante talents and the 9th- and 19th-level social talents" expands per list. A suspended ordinal ("the
    4th-") takes only the tail of a full item that starts with an ordinal ("level vigilante talents"); any other suspended item
    ("low-") takes the hyphen tail of the next full hyphenated item ("level" of "high-level"). A suspended item with no full item
    after it stays as it is: no tail is borrowed from an earlier list. Text without a suspended item is returned as it is."""
    items = [x.strip() for x in re.split(r",|\band\b|\bor\b", text) if x.strip()]
    if not any(x.endswith("-") for x in items):
        return text
    out = []
    for i, item in enumerate(items):
        if item.endswith("-"):
            later = items[i + 1:]
            if _ORD_STEM.match(item):
                tail = next((m.group(1) for m in (_ORD_FULL.match(x) for x in later) if m), None)
            else:
                tail = next((x.split("-", 1)[1] for x in later if "-" in x and not x.endswith("-") and x.split("-", 1)[1]), None)
            if tail:
                out.append(item + tail)
                continue
        out.append(item)
    return ", ".join(out)


def phrase_tokens(text: str, possessor: bool = True) -> list[str]:
    """Words of a trade name or of a printed phrase, as the app reads them: no articles, no class names, ordinals as
    digits, "gained at 4th level" as "4th-level", "1 to 4" as one range."""
    text = expand_suspended(fold(text))                                                     # app #727
    text = text.replace(" as well as ", " and ")                                           # R7
    text = re.sub(r"\b(?:normal|normally)\s+", "", text)                                     # R2
    # R10: a possessor phrase before a name ("the sacred shield's holy champion ability") is not part of the name
    if possessor:
        text = re.sub(r"(?:\b(?:the|a|an)\s+)?(?:[a-z-]+\s+){0,2}[a-z-]+'s\s+", "", text)
    text = text.replace("'s", "") if possessor else text.replace("'s", "possessive")      # plain reading: a possessor stays a word
    text = re.sub(r"\b(\d+)(?:st|nd|rd|th)?\s*(?:to|-|through)\s*(\d+)(?:st|nd|rd|th)?\b(?!-level)", lambda m: " ".join(
        str(n) for n in range(int(m.group(1)), int(m.group(2)) + 1)) if 0 < int(m.group(1)) < int(m.group(2)) <= 20 else m.group(0), text)   # R6
    # R4 no longer turns "hex gained at 4th level" into "4th-level hex": the app (#728) compares the printed words, so a stored name
    # "4th-level hex" does not cover the sentence "the hex gained at 4th level" (owner ruling 22)
    words = re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text)
    out = []
    for w in words:
        w = ORDINAL_WORDS.get(w, w)
        if w in ("the", "a", "an", "standard", "ability", "abilities", "feature", "features", "class",    # R1
                 "normal", "normally") or w in CLASS_WORDS:                                                  # R2: `bonus` stays
            continue
        out.extend(stem(x) for x in (w.split("-") if re.fullmatch(r"\d+-\d+", w) is None else [w]))
    return out


def covers(phrase: str, trade_name: str) -> bool:
    """Whether the printed phrase of a trade sentence names the trade (a step list such as "armor training
    1, 2, 3, and 4" names the trade `Armor training 3`). The app's drift check is the authority; this
    only picks the features that print the trade."""
    # R10 is an alternative reading, tried after the plain one ("unarmed strike and brawler's flurry" names both)
    return any(_covers(phrase_tokens(phrase, poss), phrase_tokens(ABILITY_TAG.sub("", trade_name), poss2))
               for poss in (False, True) for poss2 in (False, True))


def _covers(p: list[str], t: list[str]) -> bool:
    if not t:
        return False
    n = len(t)
    for i in range(len(p) - n + 1):
        if p[i:i + n] == t:
            return True
    if t[-1].isdigit() and len(t) > 1:
        base, d = t[:-1], t[-1]
        for i in range(len(p) - len(base) + 1):
            if p[i:i + len(base)] == base:
                j = i + len(base)
                while j < len(p) and (p[j].isdigit() or p[j] == "and"):
                    if p[j] == d:
                        return True
                    j += 1
    return False


# ---- comparing the draft with print ------------------------------------------------------------------

LOOSE_TRADE = re.compile(r"(?:^|(?<=[.!?]\s)|(?<=\n))(?:This|These|It)\b[^.]{0,60}?\b(?:replaces?|alters?|changes?|modifies)\b[^.]*\.", re.I)
PROGRESSION = re.compile(r"(?:every|per)\s+\w+\s+(?:\w+\s+)?levels?(?:\s+(?:he|she|they|it|you)\s+(?:has|have))?\s+(?:beyond|after|above|thereafter)|every\s+\w+\s+levels?\s+thereafter", re.I)


def strip_trade_sentences(text: str) -> str:
    return LOOSE_TRADE.sub(" ", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text))


USAGE_SENTENCE = re.compile(r"\b(?:per|each|every) (?:day|week|encounter)\b|\bonce a day\b|\badditional (?:time|use)s?\b|\bper day\b", re.I)


def strip_usage(text: str) -> str:
    """Drops the sentences that state how often an ability can be used: the import holds them as `Usage`."""
    parts = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(x for x in parts if not USAGE_SENTENCE.search(x))


def strip_progression(text: str) -> str:
    """Drops the sentences that state a progression ("increases by +1 for every four levels beyond 2nd")."""
    parts = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(x for x in parts if not PROGRESSION.search(x))


def strip_leads(text: str) -> str:
    return LEAD.sub("", text.strip())


def progression_levels(text: str) -> set[int] | None:
    """The levels that a printed progression steps through ("every four levels beyond 2nd", "at 5th level and
    every six levels thereafter"), or None."""
    t = fold(text)
    m = re.search(r"at (\d+)(?:st|nd|rd|th) level and (?:for )?every\s+(\w+)\s+levels?\s+(?:thereafter|after that|beyond that)", t)
    if m:
        step = NUMBER_WORDS.get(m.group(2), m.group(2))
        if step.isdigit():
            k, n = int(m.group(1)), int(step)
            return {k + n * j for j in range(0, 20) if k + n * j <= 20}
    m = re.search(r"(?:every|for every|per)\s+(\w+)\s+(?:[a-z-]+\s+)?levels?(?:\s+(?:he|she|they|it|you)\s+(?:has|have))?\s+(?:beyond|after|above|thereafter)\s*(?:(\d+)(?:st|nd|rd|th))?", t)
    if not m:
        return None
    step = NUMBER_WORDS.get(m.group(1), m.group(1))
    if not step.isdigit():
        return None
    n = int(step)
    base = m.group(2)
    if base is None:
        m2 = re.search(r"at (\d+)(?:st|nd|rd|th) level", t)
        if not m2:
            return None
        base = m2.group(1)
    k = int(base)
    return {k + n * j for j in range(1, 20) if k + n * j <= 20}


@dataclass
class Compare:
    status: str                  # print | draft | hold
    notes: list[str]             # for a hold: why; otherwise what the comparison did
    level_print: int | None


ACTION_TOKENS = {"standard", "move", "swift", "immediate", "free", "full-round", "action"}
FRACTIONS = {"half": (1, 2), "one-half": (1, 2), "one-third": (1, 3), "one-fourth": (1, 4), "one-fifth": (1, 5),
             "one-sixth": (1, 6), "one-eighth": (1, 8)}
CORPUS_FRACTION = re.compile(
    r"(?:equal to\s+(?:a\s+)?)?(?:(\d+)\s*\+\s*)?(one-half|half|one-third|one-fourth|one-fifth|one-sixth|one-eighth)\s+"
    r"(?:of\s+)?(?:her|his|its|their|the)\s+(?:[\w-]+\s+){0,2}?levels?(?:\s*\((?:minimum|min\.?)\s*\+?(\d+)\))?", re.I)
PRINT_PROGRESSION = re.compile(
    r"(?:increases?|improves?|rises?|grows?)\s+by\s+\+?(\d+)[^.]*?(?:every|for every|per)\s+(\w+)\s+(?:[a-z-]+\s+)?levels?(?:\s+(?:he|she|they|it|you)\s+(?:has|have))?\s+(?:after|beyond|above)\s+(\d+)(?:st|nd|rd|th)", re.I)
PRINT_MAXIMUM = re.compile(r"maximum\s+(?:bonus\s+)?of\s+\+?(\d+)(?:[^.]*?\bat\s+(\d+)(?:st|nd|rd|th)\s+level)?", re.I)

# Features where the owner ruled that print wins over a corpus value that the expansion shows to differ
# (ruling 8 of 2026-11-24 on phynics/cast-iron-data#306).
PRINT_WINS = {
    ("ref/arc-fighter/archer", "hawkeye"): "ruling 8: print corrects the corpus (+1 at 2nd level and every 4 levels beyond; the corpus gave 1 + one-fourth of the level)",
}


# "At 5th level and every 5 levels thereafter, this enhancement bonus increases by 1" (rule 1 of the pilot's follow-up: values level by level)
PRINT_PROGRESSION_FROM = re.compile(
    r"(?:at\s+)?(\d+)(?:st|nd|rd|th)\s+level\s+and\s+(?:for\s+)?every\s+(\w+)\s+(?:[\w-]+\s+){0,2}?levels?\s+"
    r"(?:thereafter|after\s+that|beyond\s+that)[^.]*?(?:increases?|improves?|rises?|grows?)\s+by\s+(?:an\s+additional\s+)?\+?(\d+)", re.I)


def expand_rules_from(print_text: str, cm: re.Match) -> tuple[str, list[str]] | None:
    """The printed progression "At Kth level and every N levels thereafter, ... increases by S" against the corpus's fraction of the
    level, level by level: the bonus is B before the Kth level (B is the first "+B" of the text, else 0) and B + S for each step."""
    pm = PRINT_PROGRESSION_FROM.search(print_text)
    if not pm:
        return None
    step = NUMBER_WORDS.get(pm.group(2).lower(), pm.group(2))
    if not step.isdigit():
        return None
    first = re.search(r"\+(\d+)", print_text[:pm.start()])
    b = int(first.group(1)) if first else 0
    k, n, s_ = int(pm.group(1)), int(step), int(pm.group(3))
    base_c = int(cm.group(1) or 0)
    num, den = FRACTIONS[cm.group(2).lower()]
    minimum = int(cm.group(3)) if cm.group(3) else 0
    mx = PRINT_MAXIMUM.search(print_text)
    cap = int(mx.group(1)) if mx else None
    for level in range(max(1, lead_level(print_text) or 1), 21):
        printed = b + (s_ * ((level - k) // n + 1) if level >= k else 0)
        stored = max(base_c + level * num // den, minimum)
        if cap is not None:
            printed, stored = min(printed, cap), min(stored, cap)
        if printed != stored:
            return "differ", [f"at level {level} print gives +{printed}, the corpus {stored}"]
    forget = ([f"+{b}", f"+{s_}"] if b else [f"+{s_}", str(s_)]) + [str(k), str(n)]
    if mx:
        forget += [f"+{cap}", str(cap), "maximum"] + ([mx.group(2)] if mx.group(2) else [])
    return "equal", forget


# Values level by level (rule 1): the corpus's upgrade rows against the table that print states.
PRINT_STEP = re.compile(r"\+(\d+)\s+at\s+(\d+)(?:st|nd|rd|th)\s+level", re.I)
PRINT_THEREAFTER = re.compile(
    r"by\s+(?:an\s+additional\s+)?\+?(\d+)\s+(?:every|for\s+every)\s+(\w+)\s+(?:[\w-]+\s+){0,2}?levels?\s+(?:thereafter|after\s+that|beyond\s+that)", re.I)
PRINT_BY_FROM = re.compile(
    r"(?:increases?|improves?|rises?|grows?)\s+by\s+\+?(\d+)\s+at\s+(\d+)(?:st|nd|rd|th)\s+level\s+and\s+(?:for\s+)?every\s+(\w+)\s+(?:[\w-]+\s+){0,2}?levels?\s+"
    r"(?:thereafter|after\s+that|beyond\s+that)", re.I)


def last_number(text: str) -> int:
    """The last number of a text that is not a level ("fast healing 1", "10 feet", "reduced by 1 point"), the base of a value that
    a progression raises; 0 when the text has none."""
    t = re.sub(r"\b\d+(?:st|nd|rd|th)\b", " ", text)
    nums = re.findall(r"\+?(\d+)", t)
    return int(nums[-1]) if nums else 0


def print_value_table(print_text: str) -> dict[int, int] | None:
    """The values by level that print states, from 1 to 20 (the levels before the first step are the base), or None: a progression
    ("At 5th level and every 5 levels thereafter ... increases by 2", "increases by +1 for every four levels beyond 2nd") or
    steps ("increases to +4 at 5th level, and +6 at 8th level"). The base is the first "+B" of the text."""
    flat = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", print_text)
    mx = PRINT_MAXIMUM.search(flat)
    cap = int(mx.group(1)) if mx else None
    out: dict[int, int] = {}
    base = 0
    m = PRINT_BY_FROM.search(flat) or PRINT_PROGRESSION_FROM.search(flat)
    if m:
        if m.re is PRINT_BY_FROM:
            s_, k, step = int(m.group(1)), int(m.group(2)), NUMBER_WORDS.get(m.group(3).lower(), m.group(3))
        else:
            k, step, s_ = int(m.group(1)), NUMBER_WORDS.get(m.group(2).lower(), m.group(2)), int(m.group(3))
        if not step.isdigit():
            return None
        n = int(step)
        base = last_number(flat[:m.start()])
        for level in range(1, 21):
            out[level] = base + (s_ * ((level - k) // n + 1) if level >= k else 0)
    else:
        m = PRINT_PROGRESSION.search(flat)
        if m:
            step = NUMBER_WORDS.get(m.group(2).lower(), m.group(2))
            if not step.isdigit():
                return None
            s_, n, k = int(m.group(1)), int(step), int(m.group(3))
            base = last_number(flat[:m.start()])
            for level in range(1, 21):
                out[level] = base + (s_ * ((level - k) // n) if level >= k else 0)
        else:
            steps = sorted((int(b), int(a)) for a, b in PRINT_STEP.findall(PRINT_MAXIMUM.sub(" ", flat)))
            if not steps:
                return None
            base = last_number(flat[:PRINT_STEP.search(PRINT_MAXIMUM.sub(" ", flat)).start()])
            tm = PRINT_THEREAFTER.search(flat)
            if PROGRESSION.search(flat) and not tm:
                return None                # a progression that no pattern reads: no table
            for level in range(1, 21):
                out[level] = base
                for lv, v in steps:
                    if level >= lv:
                        out[level] = v
                if tm:
                    k, v = steps[-1]
                    step = NUMBER_WORDS.get(tm.group(2).lower(), tm.group(2))
                    if not step.isdigit():
                        return None
                    if level >= k:
                        out[level] = v + int(tm.group(1)) * ((level - k) // int(step))
    if cap is not None:
        out = {k_: min(v, cap) for k_, v in out.items()}
    return out


def row_numbers(text: str) -> list[int]:
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    t = re.sub(r"\b\d+(?:st|nd|rd|th)\b", " ", t)
    return [int(x) for x in re.findall(r"\+?(\d+)", t)]


def rows_against_print(draft: Draft, print_text: str) -> tuple[str, str] | None:
    """Rule 1. The upgrade rows ("At 5th Level: This bonus increases to +4") as a table of level and value against the table that
    print states. ("equal", "") when the values agree at every row (a row is the value at its level, or the sum of the rows up to it:
    the import writes both "now increase by 4" and "increase by 1"); ("differ", why) when one row differs or print has a step that
    no row has; None when either side has no table (a row with no number, or two numbers)."""
    if not draft.upgrades:
        return None
    table = print_value_table(print_text)
    if table is None:
        return None
    rows = []
    for n, t in draft.upgrades:
        nums = row_numbers(t)
        if len(nums) != 1:
            return None
        rows.append((n, nums[0]))
    absolute = [(n, v) for n, v in rows]
    total, cumulative = 0, []
    for n, v in rows:
        total += v
        cumulative.append((n, total))
    first = min(table)
    for series in (absolute, cumulative):
        if all(table.get(n) == v for n, v in series):
            row_levels = {n for n, _ in series}
            steps = [level for level in range(2, 21) if table[level] != table[level - 1] and level >= min(row_levels)]
            if all(level in row_levels for level in steps):
                return "equal", ""
    bad = next(((n, v) for n, v in absolute if table.get(n) != v), None)
    return "differ", (f"at level {bad[0]} the corpus row gives {bad[1]}, print {table.get(bad[0])}" if bad else "print has a step that no row has")


def strip_steps(text: str) -> str:
    """Drops the sentences that state steps of a value ("increases to +4 at 5th level, and +6 at 8th level")."""
    parts = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(x for x in parts if not PRINT_STEP.search(x))


def expand_rules(print_text: str, corpus_text: str) -> tuple[str, list[str]] | None:
    """Rule 8. When print states "+B ... increases by +S for every N levels after Kth" and the corpus states
    "equal to one-third of her X level (minimum +M)", expands both into the values at levels K..20. Returns
    ("equal", [words]) when they agree (the words are the numbers to leave out of the comparison), or
    ("differ", [description]) when they do not; None when the text has no such pair."""
    flat = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", corpus_text)
    cm = CORPUS_FRACTION.search(flat)
    pm = PRINT_PROGRESSION.search(print_text)
    if RULES["values"] and cm and not pm:
        return expand_rules_from(print_text, cm)
    if not cm or not pm:
        return None
    base_c = int(cm.group(1) or 0)
    num, den = FRACTIONS[cm.group(2).lower()]
    minimum = int(cm.group(3)) if cm.group(3) else 0
    step = NUMBER_WORDS.get(pm.group(2).lower(), pm.group(2))
    first = re.search(r"\+(\d+)", print_text)
    if not step.isdigit() or not first:
        return None
    b, s_, n, k = int(first.group(1)), int(pm.group(1)), int(step), int(pm.group(3))
    start = max(k, lead_level(print_text) or k)
    mx = PRINT_MAXIMUM.search(print_text)
    cap = int(mx.group(1)) if mx else None
    for level in range(start, 21):
        printed = b + s_ * ((level - k) // n)
        if cap is not None:
            printed = min(printed, cap)
        stored = max(base_c + level * num // den, minimum)
        if cap is not None:
            stored = min(stored, cap)
        if printed != stored:
            return "differ", [f"at level {level} print gives +{printed}, the corpus {stored}"]
    forget = [f"+{b}", f"+{s_}", str(k), str(n)]
    if mx:
        forget += [f"+{cap}", str(cap), "maximum"] + ([mx.group(2)] if mx.group(2) else [])
    return "equal", forget


PREREQ_LEVEL = re.compile(r"(\d+)(?:st|nd|rd|th)[- ]level\b", re.I)
PRINT_AT_LEAST = re.compile(r"[^.]*\bmust be at least (\d+)(?:st|nd|rd|th)[- ]level\b[^.]*\.", re.I)


def take_prerequisites(draft: Draft, p_clean: str, d_clean: str) -> tuple[str, str, list[str]]:
    """A `Prereq: 13th-level magus ...` row is print's "The magus must be at least 13th level and have ... before selecting this
    arcana" when the level is the same: both go out of the comparison (the other words of a prerequisite are not compared; the
    number is the rule). A prerequisite of another shape stays in the comparison."""
    info: list[str] = []
    for pr in draft.prereq:
        m = PREREQ_LEVEL.match(pr.strip())
        flat = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", pr).strip()
        if not m or flat not in d_clean:
            continue
        sm = next((x for x in PRINT_AT_LEAST.finditer(p_clean) if x.group(1) == m.group(1)), None)
        if sm:
            p_clean = p_clean.replace(sm.group(0), " ", 1)
            d_clean = d_clean.replace(flat, " ", 1)
            info.append(f"rule 3: the prerequisite row \"{flat[:40]}\" is print's \"must be at least {ordinal(int(m.group(1)))} level\" (the same level)")
    return p_clean, d_clean, info


def printed_phrase(text: str) -> re.Pattern:
    """A pattern for a text in print: its words in order, any punctuation, spacing and Markdown between them."""
    words = re.findall(r"[a-z0-9]+", fold(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)))
    return re.compile(r"[\W_]*".join(re.escape(w) for w in words), re.I)


USED_BEFORE_USAGE = re.compile(r"(?:\b(?:this ability|it)\s+)?\b(?:can|may)\s+(?:be\s+)?used?\s*(?=[.,;]|$)", re.I)


def take_printed_usage(rows: list[str], p_clean: str) -> tuple[str, list[str], list[str]]:
    """A `Usage` row whose words are in print, in order, is print's: those words go out of the comparison (the draft has no usage rows
    in its text, so it does not have them either; "this ability can be used" that led them goes too), and the row needs no other
    check. A row that print words otherwise stays."""
    keep: list[str] = []
    info: list[str] = []
    for u in rows:
        words = re.findall(r"[A-Za-z0-9]+", u)
        flat = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", p_clean)
        pat = re.compile(r"[\W_]*".join(re.escape(w) for w in words), re.I)
        if len(words) >= 3 and pat.search(flat):
            p_clean = USED_BEFORE_USAGE.sub(" ", pat.sub(" ", flat, count=1))
            info.append(f"rule 4: the usage row \"{u[:40]}\" is in print word for word")
        else:
            keep.append(u)
    return p_clean, keep, info


TABLE_ROW = re.compile(r"(?m)^\s*\|.*\|\s*$")


def table_lost(parts: list[str], print_text: str) -> bool:
    """Rule 5, second case: the corpus has a Markdown table in this feature and the print text has none (the extraction ran the cells of a
    table together as one paragraph, so no word is missing and the comparison sees no loss: Keleshite Prophet's Divining Dance)."""
    return any(TABLE_ROW.search(x) for x in parts) and not TABLE_ROW.search(print_text)


def compare_feature(draft: Draft, print_text: str, drop: set[str], title_tokens: set[str]) -> Compare:
    HYPHEN_SPACES[0] = True
    try:
        return _compare_feature(draft, print_text, drop, title_tokens)
    finally:
        HYPHEN_SPACES[0] = False


def _compare_feature(draft: Draft, print_text: str, drop: set[str], title_tokens: set[str]) -> Compare:
    """Draft against the printed paragraph. Differences in words that carry no rule (articles, pronouns, the
    person, connectives, action labels, the order of sentences) are wording; a number or any other word that
    only one side has is a changed number or rule word (held). Printed progressions are expanded against the
    corpus's fractions of the level (ruling 8); a corpus paragraph that print does not have is dropped
    (ruling 10)."""
    notes: list[str] = []
    info: list[str] = []
    if RULES["hyphens"]:
        # the title's own hyphenated words are compared as their parts, like the text ("Two-Handed Fighter")
        title_tokens = title_tokens | {x if NUMBER_TOKEN.match(x) else stem(x) for t in title_tokens if "-" in t for x in t.split("-") if x}
        drop = drop | {x if NUMBER_TOKEN.match(x) else stem(x) for t in drop if "-" in t for x in t.split("-") if x}      # (the feature's own name)
    skip = drop | title_tokens
    p_clean = LEVEL_LEAD_WORDS.sub("At ", strip_trade_sentences(print_text))
    d_clean = LEVEL_LEAD_WORDS.sub("At ", strip_trade_sentences(draft.core))
    lp = lead_level(print_text)
    if draft.level is not None and lp is not None and draft.level != lp:
        notes.append(f"level: corpus {ordinal(draft.level)}, print {ordinal(lp)}")
    lvl = draft.level if lp is None or lp == draft.level else None
    p_clean = strip_level_phrase(strip_leads(p_clean), lvl)
    d_clean = strip_level_phrase(strip_leads(d_clean), lvl)
    if RULES["prereq"]:
        p_clean, d_clean, pre = take_prerequisites(draft, p_clean, d_clean)
        info += pre
    usage_rows = list(draft.usage)
    if RULES["usage"] and usage_rows:
        p_clean, usage_rows, use = take_printed_usage(usage_rows, p_clean)
        info += use
    forget_p: set[str] = set()
    expanded = expand_rules(print_text, d_clean)
    if expanded:
        if expanded[0] == "equal":
            forget_p = set(expanded[1])
            p_clean = strip_progression(p_clean)
            d_clean = CORPUS_FRACTION.sub(" ", d_clean)
            info.append("rule 8: the printed progression and the corpus's fraction of the level give the same values; print's wording taken")
        else:
            notes.append("hand review: " + expanded[1][0])
    rows_ok = False
    if RULES["values"] and draft.upgrades and not expanded:
        rv = rows_against_print(draft, print_text)
        if rv and rv[0] == "equal":
            rows_ok = True
            p_clean = strip_steps(strip_progression(p_clean))
            info.append("rule 1: the corpus rows and the printed values agree level by level; print's wording taken")
        elif rv:
            notes.append("hand review: " + rv[1])
    d_tok = Counter(tokens(d_clean, skip))
    if usage_rows:
        # the sentences that state the usage cancel words of the draft, but add none: the import keeps the
        # usage in its `Usage` row
        rest = strip_usage(p_clean)
        p_tok = Counter(tokens(rest, skip))
        for t, n in Counter(tokens(p_clean, skip)).items():
            room = d_tok[t] - p_tok[t]
            if room > 0:
                p_tok[t] += min(n - p_tok[t], room) if n > p_tok[t] else 0
    else:
        p_tok = Counter(tokens(p_clean, skip))
    for t in forget_p:
        p_tok.pop(t, None)
    prog = progression_levels(print_text)
    if prog is not None:
        # the progression that print states may be written out in the corpus ("6th, 9th, 12th") or as rows
        d_only_levels = {int(t) for t in (d_tok - p_tok) if t.isdigit()}
        if d_only_levels and d_only_levels <= prog:
            for t in list(d_tok):
                if t.isdigit() and int(t) in prog and d_tok[t] > p_tok[t]:
                    d_tok[t] = p_tok[t]
    if draft.upgrades:
        rows = {n for n, _ in draft.upgrades}
        if rows_ok or (prog is not None and rows <= prog and rows == {x for x in prog if min(rows) <= x <= max(rows)}):
            # the rows expand the printed rule; they are not rule text of their own
            p_tok = Counter(tokens(strip_leads(strip_level_phrase(strip_progression(p_clean), draft.level)), skip))
            if usage_rows:
                p_tok = Counter(tokens(strip_usage(strip_leads(strip_level_phrase(strip_progression(p_clean), draft.level))), skip))
                for t, n in Counter(tokens(strip_leads(strip_level_phrase(strip_progression(p_clean), draft.level)), skip)).items():
                    room = d_tok[t] - p_tok[t]
                    if room > 0 and n > p_tok[t]:
                        p_tok[t] += min(n - p_tok[t], room)
        else:
            for n, t in draft.upgrades:
                for tk in tokens(f"{n} " + strip_leads(f"At {ordinal(n)} level, {t}"), skip):
                    d_tok[tk] += 1
    only_print = p_tok - d_tok
    only_draft = d_tok - p_tok
    if draft.action_labelled:
        for t in ACTION_TOKENS:          # a phrase that an action label made ("as a swift action") is not a rule word
            only_draft.pop(t, None)
    if forget_p:
        for t in ("bonu", "bonuse"):     # the noun of "These bonuses are equal to ..." that the expansion replaces
            only_draft.pop(t, None)
            only_print.pop(t, None)
    if only_draft and not only_print:
        # ruling 10: a paragraph of the corpus that print does not have is dropped
        dropped = []
        for part in draft.parts:
            tk = Counter(tokens(strip_level_phrase(strip_leads(strip_trade_sentences(part)), lvl), skip))
            total = sum(tk.values())
            if total >= 4 and sum(min(n, p_tok[t]) for t, n in tk.items()) * 2 < total:
                dropped.append(part)
                d_tok = d_tok - tk
        only_draft = d_tok - p_tok
        if draft.action_labelled:
            for t in ACTION_TOKENS:
                only_draft.pop(t, None)
        if dropped and not only_draft:
            text10 = "corpus text that print does not have is dropped: " + "; ".join("“" + " ".join(x.split()[:7]) + " …”" for x in dropped)
            if RULES["dropped"] and any(re.search(r"(?m)^\s*\|.*\|\s*$", x) for x in dropped):
                # rule 5: a corpus table that the print span lacks is a hold (a decision of the review takes print's text)
                notes.append("dropped table: " + text10)
            else:
                info.append("ruling 10: " + text10)
    if RULES["dropped"] and table_lost(draft.parts, print_text) and not any(n.startswith("dropped table") for n in notes):
        notes.append("dropped table: the corpus has a table that the print text carries as running text; a hand text (`edit`) sets it")
    a = sorted(only_draft.elements())
    b = sorted(only_print.elements())
    if (a or b) and letters(a) == letters(b):
        a = b = []     # the same letters and numbers in another spelling (point-blank, point blank)
    if a or b:
        kind = "number" if any(is_number(x) for x in a + b) else "rule word"
        notes.append(f"{kind}: corpus {a or '-'} / print {b or '-'}")
    if usage_rows:
        usage_nums = {x for u in usage_rows for x in tokens(u) if is_number(x)}
        printed_nums = {x for x in tokens(print_text) if is_number(x)}
        if "once" in print_text.lower():
            printed_nums.add("1")
        missing = sorted(usage_nums - printed_nums)
        if missing:
            notes.append(f"number: usage row {missing} not in print")
    if draft.inexpressible:
        notes.append("draft cannot express: " + "; ".join(draft.inexpressible))
    if notes:
        return Compare("hold", notes + info, lp)
    same = [fold(strip_leads(x)) for x in (draft.text, print_text)]
    norm = [re.sub(r"[^a-z0-9+\-]+", " ", s).split() for s in same]
    return Compare("draft" if norm[0] == norm[1] and draft.level == lp and not info else "print", info, lp)




def strip_level_phrase(text: str, level: int | None) -> str:
    """Drops "of 18th level or higher" and the like for the level that the import's Gained row gives: the
    import wrote it as a lead, print words it inside the sentence."""
    if level is None:
        return text
    o = ordinal(level)
    return re.sub(rf"\b(?:of\s+|at\s+|starting at\s+|beginning at\s+|reaching\s+|upon reaching\s+)?{o}[\s-]level(?:\s+or\s+(?:higher|above))?", " ", text, flags=re.I)


def letters(tokens_: list[str]) -> str:
    """The letters, digits and signs of some tokens, as a multiset (a list that print sets with blanks and
    the corpus with hyphens has the same letters)."""
    chars = []
    for t in tokens_:
        chars += ([t[0]] if t[0] in "+-" else []) + list(re.sub(r"[^a-z0-9]", "", t))
    return "".join(sorted(chars))


# ---- corpus access ------------------------------------------------------------------------------------

@dataclass
class Entry:
    path: Path
    id: str
    title: str
    kind: str
    front: str
    body: str
    data: dict
    book: str | None
    page: str
    classes: list[str]

    @property
    def converted(self) -> bool:
        if "features" in (self.data.get("fields") or {}):
            return True
        # the text is an opening only (no head is printed): `fmt` leaves no empty `features`, so it is converted when it has
        # no key row of the import form left
        return self.id in OPENING_ONLY and not re.search(r"^\*\*[A-Z][^*\n]*\*\*", self.body, re.M)


# Entries whose print has no head of its own: the printed text is the opening (Familiar Folio p. 16, Bloodline Familiars)
OPENING_ONLY = {"ref/arc-sorcerer/bloodline-familiars", "ref/arc-bloodrager/bloodline-familiars"}


# A broken head of the import that the script reads as the head that print has (the import is not edited by hand): Black Markets p. 28 "Envenom (Su" for "Envenom (Su)"
IMPORT_BODY_FIXES = {"ref/arc-alchemist/eldritch-poisoner": [("**Envenom (Su**", "**Envenom (Su)**")],
                     "ref/arc-ranger/yokai-hunter": [("Tians refer to as\nyokai. The yokai hunter", "Tians refer to as\n_yokai_. The yokai hunter")]}      # print sets "yokai" in italics in the opening (Dragon Empires Primer p. 23; review of #356)


def load_entries(corpus: Path, book: str | None, only: str = "") -> list[Entry]:
    out = []
    for path in sorted((corpus / "entries").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        head = text[:4000]
        if 'kind = "archetype"' not in head:
            continue
        front, body = split_entry(text)
        data = tomllib.loads(front)
        fields = data.get("fields") or {}
        if fields.get("kind") != "archetype":
            continue
        sources = data.get("sources") or []
        first = sources[0]["publication"] if sources else (data.get("source_ids") or [None])[0]
        page = str(sources[0].get("page", "")) if sources else ""
        if book and first != book:
            continue
        if only and not data["id"].startswith(only):
            continue
        classes = [r["target"] for r in data.get("relations", []) if r.get("kind") == "archetype"]
        for old_, new_ in IMPORT_BODY_FIXES.get(data["id"], []):
            body = body.replace(old_, new_)
        out.append(Entry(path, data["id"], data["title"], "archetype", front, body, data, first, page, classes))
    return out


def trades_of(e: Entry) -> list[dict]:
    return list((e.data.get("fields") or {}).get("trades") or [])


def trade_name(t: dict) -> tuple[str, str]:
    return ("replaces", t["replaces"]) if "replaces" in t else ("alters", t["alters"])


DECISION_HEADER = ["entry", "anchor", "decision", "note"]
DECISIONS = ("print", "drop", "to-opening", "hold", "unlist", "list", "sidebar", "carried")


def decisions_path(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / f"feature-prose-540-{book}.decisions.tsv"


def read_decisions(corpus: Path, book: str) -> dict[tuple[str, str], tuple[str, str]]:
    """Hand decisions of a review (phynics/cast-iron-data#306, ruling 14): `print` takes print's wording for a
    held row, `drop` leaves out a feature that print does not have, `to-opening` also moves its sentence into
    the opening text, `tail-to:ANCHOR` moves the paragraphs after the first one into that feature. The structure
    decisions (owner rulings 15 and 18) also take print's wording: `unlist` makes the feature a plain heading that is
    no class feature, `sub-of:ANCHOR` a subheading of that feature, `list` a class feature that the option rule
    would have made a subheading. `after:ANCHOR` (joined to another decision with `;`) moves the row behind that
    feature: a sidebar that print sets before the text it belongs after. `carried` leaves out a section whose text an edit of another feature carries (a printed list, ruling 45). `end:SLUG` (with `sidebar`, `drop` or `print`) records the
    title that ends the print span (the next section of the chapter, a box) in a row of its own, so that it never meets a feature
    of the same slug (a plain slug still works, as in the earlier books). `fold-into:ANCHOR` (owner ruling 44) folds a section
    whose print head is the title of a table into the end of that feature: the head becomes a bold line directly above the
    Markdown table, which is the section's text."""
    path = decisions_path(corpus, book)
    out: dict[tuple[str, str], tuple[str, str]] = {}
    if not path.exists():
        return out
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines[0].split("\t") != DECISION_HEADER:
        raise SystemExit(f"{path}: header is not {DECISION_HEADER}")
    for n, ln in enumerate(lines[1:], 2):
        if not ln:
            continue
        cells = ln.split("\t")
        if len(cells) != 4 or not all(k in DECISIONS or k.startswith(("tail-to:", "sub-of:", "after:", "fold-into:")) for k in cells[2].split(";")):
            raise SystemExit(f"{path}:{n}: not a decision row")
        out[(cells[0], cells[1])] = (cells[2], cells[3])
    return out


def read_edits(corpus: Path, book: str) -> dict[tuple[str, str], tuple[str, str]]:
    """Hand-written texts of a review (`scripts/feature-prose-540-<book>.edits.toml`, one `[[edit]]` with `entry`,
    `anchor`, `note` and `text` each): a feature whose printed structure the extraction cannot give (a table in the
    middle of a sentence, a sidebar). The text is written from print; the note says where and why."""
    path = corpus / "scripts" / f"feature-prose-540-{book}.edits.toml"
    if not path.exists():
        return {}
    out = {}
    for row in tomllib.loads(path.read_text(encoding="utf-8")).get("edit", []):
        if set(row) != {"entry", "anchor", "note", "text"}:
            raise SystemExit(f"{path}: an edit needs exactly entry, anchor, note and text")
        out[(row["entry"], row["anchor"])] = (row["text"].strip("\n"), row["note"])
    return out


def apply_edit(r: dict, edit: tuple[str, str] | None) -> dict:
    """A hand-written text of a review (`read_edits`) replaces the text of the row; it is never added to it, so that applying an edit again
    gives the same row (review of #339: Pei Zin's list stood three times when a tool appended it at every regeneration)."""
    if edit:
        r["print"] = edit[0]
        r["status"] = "print"
        r["notes"] = [edit[1]] + [n for n in r["notes"] if n.startswith(("print:", "level", "ruling"))]
    return r


def repeated_paragraphs(text: str) -> list[str]:
    """The paragraphs of 40 or more letters that a text states twice (a printed text may repeat a sentence, never a whole paragraph of an edit)."""
    seen: set[str] = set()
    out: list[str] = []
    for para in re.split(r"\n\s*\n", text):
        key = re.sub(r"\s+", " ", para).strip()
        if len(re.sub(r"[^A-Za-z]", "", key)) >= 40:
            if key in seen:
                out.append(key[:60])
            seen.add(key)
    return out


def read_adds(corpus: Path, book: str) -> dict[str, list[dict]]:
    """Sections that another owner book prints and that the entry carries (owner ruling 32 of 2026-11-25): `[[add]]` in
    `scripts/feature-prose-540-<book>.edits.toml` with `entry`, `anchor`, `head`, `parent`, `after`, `note` and `text`.
    The section is an unlisted subheading of `parent`, behind the feature `after`; its head and text name the other
    book and page, checked against that book's print."""
    path = corpus / "scripts" / f"feature-prose-540-{book}.edits.toml"
    out: dict[str, list[dict]] = {}
    if path.exists():
        for row in tomllib.loads(path.read_text(encoding="utf-8")).get("add", []):
            if set(row) != {"entry", "anchor", "head", "parent", "after", "note", "text"}:
                raise SystemExit(f"{path}: an add needs exactly entry, anchor, head, parent, after, note and text")
            out.setdefault(row["entry"], []).append(row)
    return out


def tsv_path(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / f"feature-prose-540-{book}.tsv"


def proposals_path(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / f"feature-prose-540-{book}.proposals.toml"


def read_tsv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines[0].split("\t") != TSV_HEADER:
        raise SystemExit(f"{path}: header is not {TSV_HEADER}")
    rows = []
    for n, ln in enumerate(lines[1:], 2):
        if not ln:
            continue
        cells = ln.split("\t")
        if len(cells) != len(TSV_HEADER):
            raise SystemExit(f"{path}:{n}: {len(cells)} cells, want {len(TSV_HEADER)}")
        row = dict(zip(TSV_HEADER, cells))
        if row["status"] not in STATUSES:
            raise SystemExit(f"{path}:{n}: unknown status {row['status']!r}")
        rows.append(row)
    return rows


def write_tsv(path: Path, rows: list[dict]) -> None:
    lines = ["\t".join(TSV_HEADER)]
    for r in rows:
        lines.append("\t".join(str(r[k]).replace("\t", " ").replace("\n", " ") for k in TSV_HEADER))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def toml_str(s: str) -> str:
    if "\n" not in s:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    if "'''" not in s and "\\" not in s and "\r" not in s:
        return "'''\n" + s + "'''"
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\r", "\\r").replace("\n", "\\n") + '"'


def read_proposals(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    return {e["id"]: e for e in data.get("entry", [])}


def write_proposals(path: Path, entries: dict[str, dict]) -> None:
    out = ["# Texts of the entries that feature-prose-540.py has not converted yet. Generated: never edit by hand\n"
           "# except the `edit` text of a feature (status `edit` in the review TSV).\n"]
    for eid in sorted(entries):
        e = entries[eid]
        out.append(f"\n[[entry]]\nid = {toml_str(eid)}\n")
        if e.get("hold"):
            out.append(f"hold = {toml_str(e['hold'])}\n")
        if e.get("opening_from_print"):
            out.append("opening_from_print = true\n")
        out.append("opening = [" + ", ".join(toml_str(o) for o in e.get("opening", [])) + "]\n")
        for f in e.get("feature", []):
            out.append("\n[[entry.feature]]\n")
            out.append(f"anchor = {toml_str(f['anchor'])}\nhead = {toml_str(f['head'])}\nlisted = {str(f['listed']).lower()}\n")
            if f.get("parent"):
                out.append(f"parent = {toml_str(f['parent'])}\n")
            if f.get("level") is not None:
                out.append(f"level = {f['level']}\n")
            out.append(f"print = {toml_str(f['print'])}\n")
            if f.get("import_trades"):
                out.append("import_trades = [" + ", ".join(toml_str(x) for x in f["import_trades"]) + "]\n")
            if f.get("draft") is not None:
                out.append(f"draft = {toml_str(f['draft'])}\n")
            if f.get("edit") is not None:
                out.append(f"edit = {toml_str(f['edit'])}\n")
    path.write_text("".join(out), encoding="utf-8")


# ---- --compare ----------------------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tok_set(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", fold(text).replace("'", ""))
    return {w[:-1] if len(w) > 4 and w.endswith("s") else w for w in words}


def find_pdf(books: Path, title: str) -> Path | None:
    want = tok_set(title) - {"the", "of", "and", "a"}
    best, score = None, 0.0
    for f in sorted(books.rglob("*.pdf")):
        have = tok_set(re.sub(r"^PZO\d+", "", f.stem))
        s = len(want & have) / len(want) - 0.01 * len(have - want) if want else 0
        if s > score:
            best, score = f, s
    return best if score >= 0.96 else None


def book_xml(pdf: Path, cache: Path) -> Path:
    cache.mkdir(parents=True, exist_ok=True)
    out = cache / f"{sha256_file(pdf)}.xml"
    if not out.exists() or out.stat().st_size == 0:
        part = out.with_suffix(".part")
        with open(part, "wb") as fh:
            r = subprocess.run(["pdftohtml", "-xml", "-i", "-nodrm", "-stdout", str(pdf)], stdout=fh,
                               stderr=subprocess.DEVNULL, check=False)
        if r.returncode != 0 or part.stat().st_size == 0:
            part.unlink(missing_ok=True)
            raise SystemExit("pdftohtml failed (poppler; on NixOS run this inside `nix shell nixpkgs#poppler-utils -c`)")
        part.rename(out)
    return out


def publication_title(corpus: Path, book: str) -> str:
    data = tomllib.loads((corpus / "publications.toml").read_text(encoding="utf-8"))
    for row in data["publication"]:
        if row.get("id") == book or row.get("slug") == book:
            return row["title"]
    raise SystemExit(f"publication {book!r} is not in publications.toml")


# Misprints of the book that are fixed because the meaning is certain (owner ruling 9 of 2026-11-24): the
# entry, the printed words, the words written, and why. The review table's note records each fix.
MISPRINTS = [
    ("ref/arc-summoner/twinned-summoner", "usin\u0192g", "using", "a stray glyph inside \"using\" in print (the page image shows \"usin\u0192g\")"),
    ("ref/arc-unchained-summoner/twinned-summoner", "usin\u0192g", "using", "a stray glyph inside \"using\" in print (the page image shows \"usin\u0192g\")"),
    # Batches 6 to 9 (Player Companions)
    ("ref/arc-skald/serpent-herald", "battle roar knockback", "battle roar, knockback",
     "a comma is missing in print's list of rage powers (the list reads \"animal fury, battle roar, knockback, knockdown, ...\" in the Deepwater Rager's and every other list of the book)"),
    ("ref/arc-rogue/shadow-scion", "complement the shadow walker archetype", "complement the shadow scion archetype",
     "the archetype of the entry is the shadow scion; \"shadow walker\" is a leftover name (owner ruling 43: a wrong proper name is fixed when the intended name is certain)"),
    ("ref/arc-vigilante/zealot", "This alter's the vigilante's skill ranks per level", "This alters the vigilante's skill ranks per level",
     "alters: the printed \"alter's\" is a slip for the verb of the trade sentence"),
    ("ref/arc-spiritualist/involutionist", "available at 11th, 15th, and 17th levels", "available at 11th, 15th, and 19th levels",
     "19th: the spiritualist's calm spirit gains an additional use per 4 levels beyond 7th (11th, 15th, 19th), the ability itself says 'At 15th and 19th levels', and the stored trade says 19th"),
    ("ref/arc-summoner/naturalist", "on its feat.", "on its feet.", "feet: the sentence is about the hooves of the eidolon (antlers and hoof like nails)"),
    ("ref/arc-summoner/naturalist", "superficial physical charges", "superficial physical changes",
     "changes: the same ability says \"superficial physical changes appropriate to that aspect\" two paragraphs earlier"),
    ("ref/arc-investigator/sleuth", "for a investigator", "for an investigator", "an article before a vowel"),
    ("ref/arc-brawler/strangler", "instead of a standard can.", "instead of a standard action.",
     "the sentence needs the word \"action\"; print has \"standard can\" at a column end"),
    ("ref/arc-swashbuckler/flying-blade", "perfect strike .deed,", "perfect thrust deed,",
     "there is no perfect strike deed; the same entry's trade sentence says \"replaces perfect thrust\""),
    ("ref/arc-swashbuckler/mouser", "hits a for larger than her size", "hits a foe larger than her size",
     "\"for\" is a slip for \"foe\"; the next feature prints \"hits a foe whose size is larger than her own\""),
    ("ref/arc-inquisitor/infiltrator", "such as _detect lies_", "such as discern lies",
     "there is no detect lies spell in Pathfinder; the same entry's trade sentence says \"replaces discern lies\""),
    ("ref/arc-wizard/scrollmaster", "masterwork light shield sword", "masterwork light shield", "a stray word; the scroll shield is a light shield"),
    ("ref/arc-alchemist/internal-alchemist", "Lighting Reflexes", "Lightning Reflexes", "the feat is Lightning Reflexes"),
    ("ref/arc-barbarian/elemental-kin", "at at 18th level", "at 18th level", "a doubled word"),
    ("ref/arc-druid/cave-druid", "A underground druid", "A cave druid",
     "every other feature of the entry says \"a cave druid\"; \"underground druid\" names nothing"),
    ("ref/arc-ranger/shapeshifter", "the shapeshifter subtype", "the shapechanger subtype",
     "there is no shapeshifter subtype; the same book writes \"the shapechanger subtype\" (p. 139)"),
    ("ref/arc-rogue/acrobat", "expert leaper, ledge walker,", "expert leaper, fast getaway, ledge walker,",
     "the same book prints Fast Getaway among the rogue talents (p. 130), not the advanced talents"),
    ("ref/arc-rogue/acrobat", "defensive roll, fast getaway, fast tumble,", "defensive roll, fast tumble,",
     "Fast Getaway is a rogue talent (p. 130), not an advanced rogue talent"),
    ("ref/arc-ranger/horse-lord", "of the him", "of him", "the sentence needs no article before the pronoun"),
    ("ref/arc-monk/hungry-ghost-monk", "The ability replaces diamond soul", "This ability replaces diamond soul",
     "every other trade sentence of the book starts \"This ability\""),
    ("ref/arc-mesmerist/vexing-daredevil", "replaces glib tongue", "replaces glib lie",
     "the mesmerist class feature is glib lie (Occult Adventures, class table and feature); there is no glib tongue"),
    ("ref/arc-druid/world-walker", "resist nature's lore", "resist nature's lure",
     "the druid ability is resist nature's lure; the entry's own trade row names it"),
    ("ref/arc-druid/reincarnated-druid", "a reincarnated druids adds", "a reincarnated druid adds", "a stray plural ending"),
    ("ref/arc-fighter/unbreakable", "Die Hard", "Diehard", "the feat is Diehard (Core Rulebook p. 119); print splits the name"),
    ("ref/arc-barbarian/wild-rager", "bloody blow", "[bleeding blow](ref/ragepower/bleeding-blow)",
     "the rage power is bleeding blow (Advanced Player's Guide); there is no bloody blow"),
    ("ref/arc-paladin/holy-gun", "This ability function like", "This ability functions like", "a verb that does not agree with its subject"),
    ("ref/arc-ranger/wild-stalker", "1oth", "10th", "a letter o for a zero"),
    ("ref/arc-rogue/investigator", "thought reexamining", "thoughtful reexamining",
     "the advanced rogue talent is Thoughtful Reexamining, which the same book prints in full for the burglar"),
]


# ---- Paizo errata -------------------------------------------------------------------------------------
#
# The owner's copy of the Advanced Class Guide is the 1st printing (August 2014). Paizo's errata for that book brings it
# to the 2nd printing, and the corpus holds the corrected text (phynics/cast-iron-data#309, ruling 1: print plus recorded
# errata; `scripts/errata.tsv` has a row of class `errata` for each feature that this table changes). Each entry of
# `ERRATA` is the archetype, the anchor of the feature, the errata page, the printed words and the words that the errata
# gives. Printed words with an ellipsis ("start … end") name a span. A change that finds no place is a problem of the
# entry, so the entry is held. `ERRATA_FEATURES` replaces a whole printed ability under its printed head, and
# `ERRATA_ADDED` is an ability that the errata adds (the import has it as a feature that print lacks).
ERRATA_BOOKS = {"advanced-class-guide": "Advanced Class Guide"}
ERRATA_CTX: dict = {"book": "", "used": set()}
# The titles of the boxes that a book sets in the foot of a column (`BOX_TITLES`).
BOXES_OF_BOOK = {"inner-sea-magic": ("Black Blood of Orv",),
                 "psychic-anthology": ("Phantom Weapon Progression",)}       # the table of the Phantom Blade, set in the foot of a column of the Totem Spiritualist (p. 6)
LORE_BOXES_OF_BOOK = {"armor-masters-handbook": ("Armor Master Archetypes and Prestige Classes",),
                      "cohorts-and-companions": ("Equipment Cohorts", "Heroic Cohorts", "Cohorts of the Faith", "Student Cohorts")}
SKIP_TABLES = {"on": False}         # the Advanced Race Guide sets its tables in sans-serif type
# The Advanced Class Guide and the Advanced Race Guide set text beside illustrations: a line may be indented without
# starting a paragraph, and a head may follow a sentence end in a line without the common indent. The other books
# have regular columns, where those two rules would join a head to the line before it.
ILLUSTRATED = {"on": False}
ART_RUNS = {"on": False}           # black-markets, blood-of-shadows: text beside art steps right line by line


def _arc(entry: str) -> str:
    return "ref/arc-" + entry


ERRATA = [
    (_arc("arcanist/blade-adept"), "magus-arcana", 76,
     "dispelling strike, hasted assault, and wand wielder.", "dispelling strike, and hasted assault."),
    (_arc("bloodrager/bloodrider"), "blood-bond", 83,
     "replaces the bloodline feat gained at.", "replaces the bloodline feat gained at 9th level."),
    (_arc("bloodrager/spelleater"), "blood-of-life", 85,
     "the increase is instead added to", "the increase is added to"),
    (_arc("brawler/exemplar"), "call-to-arms", 86,
     "This ability replaces unarmed strike.", "This ability replaces unarmed strike and close weapon mastery."),
    (_arc("brawler/shield-champion"), "weapon-and-armor-proficiency", 86,
     "is proficient with all simple weapons.", "is proficient with all simple weapons and with shields as weapons."),
    (_arc("brawler/shield-champion"), "throw-shield", 86,
     "throw a medium or light shield", "throw a heavy or light shield"),
    (_arc("brawler/wild-child"), "animal-companion", 89,
     "gained at 2nd, 5th, 11th, and 14th levels.", "gained at 2nd, 8th, 14th, and 20th levels."),
    (_arc("brawler/wild-child"), "wild-tricks", 89,
     "every 3 levels thereafter", "every 6 levels thereafter"),
    (_arc("brawler/wild-child"), "wild-tricks", 89,
     "gained at 5th, 8th, 11th, 14th, 17th, and 20th levels.", "gained at 5th, 11th, and 17th levels."),
    (_arc("cavalier/daring-champion"), "panache-and-deeds", 90,
     "dodging panache, opportune parry and riposte, precise strike", "dodging panache, precise strike"),
    (_arc("cleric/ecclesitheurge"), "ecclesitheurge-s-vow", 91,
     "who wears prohibited armor or uses a prohibited shield", "who wears armor or uses a shield"),
    (_arc("cleric/ecclesitheurge"), "bonded-holy-symbol", 91,
     "forms a powerful bond … gained at 3rd level.",
     "forms a powerful bond with a holy symbol of his deity, which functions identically to a wizard's bonded object "
     "except it can be used to cast cleric and domain spells (instead of wizard spells) and the ecclesitheurge can grant "
     "his bonded holy symbol only magic abilities appropriate for a holy symbol or a neck slot item.\n\n"
     "As with a wizard's bonded item, an ecclesitheurge can add additional magic abilities to his bonded holy symbol as if "
     "he had the required item creation feat (typically Craft Wondrous Item), provided he meets the feat's level "
     "prerequisites. For example, an ecclesitheurge with a bonded holy symbol who wants to add a wondrous amulet ability, "
     "like amulet of natural armor, to his bonded holy symbol must be at least 3rd level to do so. The magic properties of "
     "a bonded holy symbol, including any magic abilities the ecclesitheurge added to the object, function for only the "
     "ecclesitheurge. If a bonded holy symbol's owner dies or the item is replaced, the object loses all enhancements the "
     "ecclesitheurge added using this ability.\n\n"
     "This ability replaces the increase to channel energy gained at 3rd level."),
    (_arc("druid/wild-whisperer"), "wild-shape", 92,
     "she never gains the ability to take the form of an elemental or plant.",
     "she never gains access to any forms beyond Small and Medium animal forms, as beast shape I."),
    (_arc("druid/wild-whisperer"), "natural-expertise", 92,
     "replaces the increase to wild shape given at 6th level.", "replaces the additional use of wild shape at 6th level."),
    (_arc("druid/wild-whisperer"), "investigator-talent", 92,
     "replaces the increase to wild shape given at 8th level.", "replaces the additional use of wild shape at 8th level."),
    (_arc("fighter/mutation-warrior"), "mutagen", 93,
     "At 1st level, a mutation warrior", "At 3rd level, a mutation warrior"),
    (_arc("fighter/mutation-warrior"), "mutagen", 93,
     "the alchemist's mutagen ability (Advanced Player's Guide 28).",
     f"the alchemist's mutagen ability ({I_OPEN}Advanced Player's Guide{I_CLOSE} 28), using his fighter level as his alchemist level."),   # the printed citation stays (ruling 26)
    (_arc("fighter/mutation-warrior"), "mutagen-discovery", 93,
     "one of the follow alchemist", "one of the following alchemist"),
    (_arc("fighter/mutation-warrior"), "mutagen-discovery", 93,
     "for determining whether he qualifies for these discoveries", "for the purpose of these discoveries"),
    (_arc("gunslinger/bolt-ace"), "deeds", 94,
     "The bolt thrower swaps", "The bolt ace swaps"),
    (_arc("gunslinger/bolt-ace"), "sharp-shoot", 94,
     "Performing this deed costs 1 grit point.",
     "Performing this deed costs 1 grit point. This deed's cost cannot be reduced by any ability or effect that reduces the "
     "amount of grit points a deed costs (such as Signature Deed)."),
    (_arc("ranger/divine-tracker"), "opening", 108, "His imbued weapon", "His weapon"),
    (_arc("hunter/divine-hunter"), "otherworldly-companion", 95,
     "it cannot be changed.",
     "it cannot be changed. The companion's CR is considered to be equal to its Hit Dice for the purpose of the celestial or "
     "fiendish template."),
    (_arc("hunter/feral-hunter"), "feral-focus", 96,
     "This ability replaces the animal focus, hunter tactics, and speak with master class abilities.",
     "This ability alters animal focus and replaces the hunter tactics and speak with master class abilities."),
    (_arc("hunter/feral-hunter"), "precise-summoned-animal", 96,
     "if the hunter chooses Outf lank as a bonus feat, she grants it to all", "the hunter grants all her teamwork feats to all"),
    (_arc("hunter/feral-hunter"), "summon-pack", 96,
     "ends his feral focus ability.",
     "ends his feral focus ability. She can increase the duration of any one summon nature's ally spell affected by this "
     "ability to 1 minute per level. She can have only one spell with a duration increased by this ability active at a time."),
    (_arc("hunter/primal-companion-hunter"), "primal-transformation", 97,
     "The animal companion gains a pool … until she gains another level.",
     "The animal companion gains a pool of 2 evolution points that can be used to temporarily give the companion evolutions "
     "as if it were an eidolon. A primal companion hunter uses her hunter level to determine her effective summoner level for "
     "the purpose of qualifying for evolutions and determining their effects. At 8th level, the number of evolution points in "
     "her pool increases to 4, and at 15th level, it increases to 6."),
    (_arc("hunter/verminous-hunter"), "leech", 98,
     " (this bleed stacks with itself)", ""),
    (_arc("hunter/verminous-hunter"), "worm", 98,
     "The creature gains fast healing 1 (Pathfinder RPG Bestiary 300) and a 25% chance", "The creature gains a 25% chance"),   # the citation names the fast healing that the errata removes
    (_arc("hunter/verminous-hunter"), "worm", 98,
     "This increases to fast healing 2 and 50% at 8th level, and fast healing 3 and 75% at 15th level.",
     "This increases to 50% at 8th level, and 75% at 15th level."),
    (_arc("inquisitor/sacred-huntsmaster"), "hunter-tactics", 99,
     "prerequisites of these teamwork feats.", "prerequisites of these teamwork feats. This ability replaces solo tactics."),
    (_arc("investigator/mastermind"), "mastermind-s-inspiration", 101,
     "A mastermind can use inspiration on any … a use of inspiration.",
     "A mastermind can use inspiration on Diplomacy and Intimidate checks without expending a use of inspiration, but can't do "
     "so for Linguistics or Spellcraft checks."),
    (_arc("investigator/sleuth"), "make-it-count", 102, "uses inspired strike", "uses studied strike"),
    (_arc("investigator/sleuth"), "make-it-count", 102, "which affects inspired strike", "which affects studied strike"),
    (_arc("investigator/sleuth"), "make-it-count", 102, "to his inspired strike", "to his studied strike"),
    (_arc("investigator/sleuth"), "grit-luck-and-panache", 102,
     "Those who use panache and luck gain twice", "Those who use panache and luck do not gain twice"),
    (_arc("investigator/spiritualist"), "strong-life", 102,
     "His dealings with the other side", "At 2nd level, his dealings with the other side"),
    (_arc("investigator/steel-hound"), "packing-heat", 103,
     "This ability replaces poison use.", "This ability replaces poison lore."),
    (_arc("monk/kata-master"), "panache", 105,
     "derring-do and opportune parry and riposte deeds", "derring-do and dodging panache deeds"),
    (_arc("oracle/psychic-searcher"), "inspiration", 106,
     "based on her Wisdom modifier, not Intelligence.", "based on her Charisma modifier, not her Intelligence modifier."),
    (_arc("oracle/spirit-guide"), "bonded-spirit", 106,
     "She uses her oracle level as her shaman level and her Charisma score instead of Wisdom for the purpose of determining its effects.",
     "She uses her oracle level as her shaman level, and she switches Wisdom for Charisma and vice versa for the purpose of "
     "determining the hex's effects."),
    (_arc("paladin/holy-guide"), "teamwork-feat", 107,
     "At 5th level, a holy guide gains", "At 6th level, a holy guide gains"),
    (_arc("paladin/holy-guide"), "teamwork-feat", 107,
     "replaces the mercy gained at 5th level.", "replaces the mercy gained at 6th level."),
    (_arc("paladin/temple-champion"), "blessing", 107,
     "of the domain she selected at 1st level.", "of the domain she selected at 4th level."),
    (_arc("ranger/hooded-champion"), "dead-aim", 108,
     "when making a single ranged attack with a bow", "when making a single ranged attack (not a full attack) with a bow"),
    (_arc("shaman/animist"), "wrangle-condition", 110,
     "but it includes verbal and somatic components.", "but it relies on audible components and the target must be within 30 feet."),
    (_arc("shaman/unsworn-shaman"), "minor-spirit", 112,
     "access to a witch hex of her choosing", "access to a shaman or witch hex of her choosing"),
    (_arc("shaman/unsworn-shaman"), "minor-spirit", 112,
     "continues to have access to the witch hex.", "continues to have access to the shaman or witch hex."),
    (_arc("shaman/unsworn-shaman"), "minor-spirit", 112,
     "This ability replaces spirit and hex.", "This ability replaces spirit and alters hex."),
    (_arc("shaman/witch-doctor"), "channel-energy", 113,
     "as the cleric class feature. The witch doctor uses",
     "as the cleric class feature. This is a separate pool of channel energy that does not stack with the life spirit's channel "
     "spirit ability. The witch doctor uses"),
    (_arc("skald/spell-warrior"), "enhance-weapons", 116,
     "count as one weapon for this purpose.",
     "count as one weapon for this purpose. The wielder of a weapon enhanced by this raging song counts as if he were under the "
     "effect of an inspired rage raging song for all purposes involving the skald's rage powers."),
    (_arc("slayer/stygian-slayer"), "weapon-and-armor-proficiency", 120,
     "replaces the slayer's weapon and armor proficiency.", "replaces the slayer's armor proficiency."),
    (_arc("swashbuckler/daring-infiltrator"), "bonus-feats", 124,
     "bonus feats at 2nd, 10th, and 18th level", "bonus feats at 4th, 8th, 12th, 16th, and 20th level"),
    (_arc("swashbuckler/inspired-blade"), "rapier-weapon-mastery", 125,
     "(this increase to the critical threat range stacks with the increases from the keen weapon special ability and similar effects)",
     "(this increase to the critical threat range stacks with the increase from rapier training, to a total threat range of 14-20)"),
    (_arc("swashbuckler/mouser"), "hamstring", 126,
     "this deed can stagger the target only if", "this deed can only stagger the target if"),
    (_arc("swashbuckler/mysterious-avenger"), "avenger-finesse", 127,
     "At 2nd level, a mysterious avenger gains", "A mysterious avenger gains"),
    (_arc("swashbuckler/picaroon"), "two-weapon-finesse", 127,
     "At 2nd level, a picaroon gains", "A picaroon gains"),
    (_arc("warpriest/cult-leader"), "weapon-and-armor-proficiency", 128,
     "does not gain Improved Unarmed Strike as a bonus feat", "does not gain Weapon Focus as a bonus feat"),
    (_arc("warpriest/sacred-fist"), "weapon-and-armor-proficiency", 131,
     "not proficient with any armor or shields.",
     "not proficient with any armor or shields. When wearing armor, using a shield, or carrying a medium or heavy load, a sacred "
     "fist loses his AC bonus and flurry of blows."),
    (_arc("warpriest/sacred-fist"), "ac-bonus", 131,
     "a +1 deflection bonus to AC and CMD", "a +1 dodge bonus to AC and CMD"),
    (_arc("warpriest/sacred-fist"), "ac-bonus", 131,
     "or when he carries a medium or heavy load.",
     "or when he carries a medium or heavy load. This counts as the monk ability of the same name, and the sacred fist's warpriest "
     "levels stack with monk levels for determining the benefits."),
    (_arc("warpriest/sacred-fist"), "flurry-of-blows", 131,
     "works like the monk ability of the same name.",
     "works like the monk ability of the same name, except the sacred fist's attack bonus from warpriest levels does not count "
     "as his warpriest level."),
    (_arc("witch/hex-channeler"), "channel-energy", 132,
     "(including major or grand hexes)", "(including major or grand hexes, but not hexes gained through the Extra Hex feat)"),
]

# A printed ability that the errata replaces: the entry, the printed head, the new head, the errata page, the new text.
ERRATA_FEATURES = {
    (_arc("slayer/sniper"), "deadly-range"): (
        "Deadly Sniper (Ex)", 120,
        "At 2nd level, when the sniper makes an attack against a target who is within his weapon's first range increment and "
        "completely unaware of his presence, that attack ignores the 30 foot range limit on ranged sneak attacks, and if it is a "
        "sneak attack, he adds his sniper level as a bonus on his sneak attack damage roll. After this first attack, the target "
        "is aware of the sniper's presence."),
}

# An ability that the errata adds: the entry and anchor, the head, the errata page, the anchor of the feature that it follows
# (or None: it comes first), and the text.
ERRATA_ADDED = {
    (_arc("cleric/ecclesitheurge"), "blessing-of-the-faithful"): (
        "Blessing of the Faithful (Su)", 91, "ecclesitheurge-s-vow",
        "As a standard action, the ecclesitheurge can bless one ally within close range (25 ft. + 5 ft./2 levels). A blessed ally "
        "gains a +2 sacred or profane bonus (depending on whether the ecclesitheurge channels positive or negative energy) on "
        "attack rolls, skill checks, ability checks, or saving throws or to AC until the ecclesitheurge's next turn. The "
        "ecclesitheurge can expend 1 use of channel energy when activating this ability to increase the duration to a number of "
        "rounds equal to the number of dice of his channel energy."),
    (_arc("gunslinger/bolt-ace"), "crossbow-maven"): (
        "Crossbow Maven", 94, None,
        "A bolt ace is proficient with all crossbows instead of all firearms and begins play with a masterwork crossbow of her "
        "choice. This ability alters the gunslinger's weapon proficiencies and replaces gunsmith."),
}

# Heads that print sets as the items of a list, though they carry an ability tag: plain subheadings of the feature before
# them (owner ruling 15). The entry and the anchor.
# Sidebars that stand between the features and belong to no feature: unlisted `##` sections (owner ruling 18).
PLAIN_HEADS = {
    (_arc("investigator/sleuth"), "grit-luck-and-panache"),
}

OPTION_HEADS = {
    (_arc("arcanist/blade-adept"), "weapon-specialization"),
    (_arc("arcanist/white-mage"), "fast-healing"),
    (_arc("arcanist/blade-adept"), "spell-strike"),
    (_arc("arcanist/blade-adept"), "student-of-the-blade"),
}


def marks_stripped(text: str) -> tuple[str, list[int]]:
    plain, idx = [], []
    for i, ch in enumerate(text):
        if ch not in (I_OPEN, I_CLOSE):
            plain.append(ch)
            idx.append(i)
    return "".join(plain), idx


def apply_errata(text: str, entry_id: str, anchor: str, notes: list[str]) -> str:
    """The text with each change of `ERRATA` for this entry and feature that finds its printed words once."""
    for n, (eid, anc, page, old, new) in enumerate(ERRATA):
        if eid != entry_id or anc != anchor or (entry_id, n) in ERRATA_CTX["used"]:
            continue
        plain, idx = marks_stripped(text)
        if "…" in old:
            a, b = old.split("…", 1)
            a, b = a.rstrip(), b.lstrip()
            i = plain.find(a)
            j = plain.find(b, i + len(a)) if i >= 0 and plain.count(a) == 1 else -1
            if j < 0:
                continue
            start, end = i, j + len(b)
        else:
            if plain.count(old) != 1:
                continue
            start = plain.find(old)
            end = start + len(old)
        text = text[: idx[start]] + new + text[idx[end - 1] + 1:]
        ERRATA_CTX["used"].add((entry_id, n))
        notes.append(f"errata: Paizo errata for {ERRATA_BOOKS.get(ERRATA_CTX['book'], '')} p. {page}: print has \"{old if chr(8230) not in old else old.replace(chr(8230), ' ... ')}\", written \"{new[:90]}{'...' if len(new) > 90 else ''}\"")
    return balance_marks(text)


def errata_unused(entry_id: str) -> list[str]:
    return [f"errata change not applied ({anc}): \"{old[:50]}\"" for n, (eid, anc, page, old, new) in enumerate(ERRATA)
            if eid == entry_id and (entry_id, n) not in ERRATA_CTX["used"]]



def is_scaffold(head: str) -> bool:
    """The app's list (`NOT_FEATURE_HEADINGS`): the whole heading, without case, surrounding space and a trailing colon."""
    key = head.strip().rstrip(":").strip().lower()
    return key in SCAFFOLD or ABILITY_TAG.sub("", key).strip() in SCAFFOLD      # "Bonus Feats (Ex)" is "Bonus Feats"


def place_elsewhere(rows: list[dict], label: str, target: str) -> str | None:
    """Wraps the first free occurrence of `label` in the text of any section of the entry in a link; returns the anchor.

    A link to a heading of the entry itself (a footnote mark such as `1` to `#footnote-i`) is not placed: its heading is
    printed text of a dropped section, and the link would point at nothing (Qinggong Monk's "1/2 the monk's level")."""
    if "#" in target:
        return None
    for r in rows:
        if r.get("print"):
            # the italic marks are underscores here: back to marks, so that a word inside italics is a word
            marked = re.sub(r"(?<![\w\\])_(?=\S)", I_OPEN, r["print"])
            marked = re.sub(r"(?<=\S)_(?!\w)", I_CLOSE, marked)
            text, lost = apply_links(marked, [(label, target)])
            if not lost:
                r["print"] = render_marks(text)
                return r["anchor"]
    return None


def join_wrapped(raw_paras: list[str], vocab: set[str]) -> list[str]:
    """The finished paragraphs of cleaned runs. A line of a sidebar that print sets in a narrow column starts no
    paragraph of its own: a paragraph that ends without a sentence end continues (a list item, a heading or a table
    cell that print sets alone ends so too: those are hand-written, see `edits.toml`)."""
    paras: list[str] = []
    for raw in raw_paras:
        s = finish_text(raw, vocab)
        if not s:
            continue
        item = BULLETS["on"] and bool(re.match(r"[\u2022\u2219]\s", s))
        if item:
            s = "- " + s[1:].strip()
            if re.match(r"- This (?:ability |performance )?(?:replaces|alters)\b", s):
                s = s[2:]               # print sets its bullet before the trade sentence that closes the list: a prose sentence, not an item
        if item:
            paras.append(s)
            continue
        if paras and (LIST_CONTINUES["on"] or not paras[-1].startswith("- ")) and not re.search(r"(?:[.!?:]|[.!?]\))\s*$", paras[-1].rstrip().removesuffix(I_CLOSE)):      # a semicolon ends no paragraph
            gap = "" if re.search(r"[A-Za-z0-9]/$", paras[-1].rstrip()) else " "      # a slash at a line end joins the next word ("DR 5/" "cold iron")
            joined = fix_hyphens(paras[-1].rstrip() + gap + s, vocab)
            joined = re.sub(I_CLOSE + r"\s+" + I_OPEN + r"(?=[,;.)])", "", joined)      # an italic run that a line end cut
            paras[-1] = re.sub(I_CLOSE + r"\s+" + I_OPEN, " ", joined)
        else:
            paras.append(s)
    return paras


# The parentheses that are only a page citation (owner ruling 26): one that a link replaces goes, any other stays as printed
CITE_RPG = r"\s*\(" + I_OPEN + r"?Pathfinder (?:RPG|Player Companion:|Campaign Setting:)[^()]*?(?:page[\s_\x01\x02]*|[\s\x01\x02]+)\d+(?:[–-]\d+)?\)"
CITE_BOOK = (r"\s*\([\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-6])?|Inner Sea Bestiary|Horror Adventures|"
             r"Ultimate (?:Magic|Combat|Equipment|Campaign|Wilderness|Intrigue)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures|Pathfinder Unchained|"
             r"Pathfinder (?:Player Companion|Campaign Setting|Adventure Path|Module)\b[^()]*?)"
             r"[\x02_]*[,\s]*(?:page[\s_\x01\x02]*)?\d+(?:[–-]\d+)?\)")
CITE_PAGE = r"\s*\(\s*(?:[\x01_]*[A-Z][\w'\u2019:, \-]*?[\x02_]*\s+)?page[\s_\x01\x02]*\d+(?:[\u2013-]\d+)?\s*\)"


CITE_SEMI = (r";\s*[\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-6])?|Inner Sea Bestiary|Horror Adventures|"
             r"Ultimate (?:Magic|Combat|Equipment|Campaign|Wilderness|Intrigue)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures|Pathfinder Unchained)"
             r"[\x02_]*[,\s]*(?:page[\s_\x01\x02]*)?\d+(?:[–-]\d+)?(?=\))")


# The same patterns for the Campaign Setting books (`CITE_EXT`): the italic of a title may end after the page ("_Ultimate Intrigue 102_"), the
# words of a title may be italic one by one ("_Ultimate_ _Intrigue_ 142"), and the Inner Sea World Guide, Ultimate Intrigue and Pathfinder
# Unchained are cited. The other books keep the patterns above, so that their entries regenerate as they were written.
CITE_EXT = {"on": False}
CITE_RPG_X = r"\s*\(" + I_OPEN + r"?Pathfinder RPG[^()]*?(?:page[\s_\x01\x02]*|[\s\x01\x02]+)\d+(?:[–-]\d+)?[\x02_]*\)"
CITE_BOOK_X = (r"\s*\([\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-5])?|"
             r"Ultimate[\s\x01\x02_]+(?:Magic|Combat|Equipment|Campaign|Intrigue)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures|Inner Sea World Guide|Pathfinder Unchained)"
             r"[\x02_]*[,\s]*(?:page[\s_\x01\x02]*)?\d+(?:[–-]\d+)?[\x02_]*\)")
CITE_PAGE = r"\s*\(\s*(?:[\x01_]*[A-Z][\w'\u2019:, \-]*?[\x02_]*\s+)?page[\s_\x01\x02]*\d+(?:[\u2013-]\d+)?\s*\)"


CITE_SEMI_X = (r";\s*[\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-5])?|"
             r"Ultimate[\s\x01\x02_]+(?:Magic|Combat|Equipment|Campaign|Intrigue)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures|Inner Sea World Guide|Pathfinder Unchained)"
             r"[\x02_]*[,\s]*(?:page[\s_\x01\x02]*)?\d+(?:[–-]\d+)?[\x02_]*(?=\))")


def _cites() -> tuple[str, str, str, str]:
    """The patterns of a page citation (RPG title, book title, page only, after a semicolon) for the book at hand."""
    return (CITE_RPG_X, CITE_BOOK_X, CITE_PAGE, CITE_SEMI_X) if CITE_EXT["on"] else (CITE_RPG, CITE_BOOK, CITE_PAGE, CITE_SEMI)


def strip_citations(text: str) -> str:
    """The text without its bare page citations: a page number that stays as printed is not a rule word."""
    text = re.sub(r"_([^_]*)_", lambda m: I_OPEN + m.group(1) + I_CLOSE, text)    # the patterns read the marks that print_md sets
    for pattern in _cites():
        text = re.sub(pattern, "", text)
    return text.replace(I_OPEN, "_").replace(I_CLOSE, "_")


# A citation that the link rule cannot judge from the words before it (owner ruling 26, Muse review of #335): the page number of the
# parenthesis, per entry. True drops it (the sentence's link already points at the cited thing), False keeps it.
EDGE_CITATIONS = {
    ("ref/arc-rogue/heister", "95–96"): True,        # "Escape Artist check to move through a tight space where her head fits ..."
    ("ref/arc-bard/prankster", "322"): True,         # "steal an object ... This functions as the steal combat maneuver": the link is on the first mention
    ("ref/arc-inquisitor/secret-seeker", "196–197"): False,
    ("ref/arc-summoner/shaitan-binder", "143"): False,        # [shaitan] is the creature; the citation names its stone curse ability (#335 review), also where the link lands on the later mention   # [read aura] goes to Perception; the citation names the occult skill unlocks
    # review of #342 (ruling 26): the two words of the rule that cut each way here
    ("ref/arc-witch/havocker", "14"): True,          # "[kineticist] element (Occult Adventures 14)": the class link makes the rule keep a citation that names an ability of the class; the link names the element's owner and the corpus links the element, so it goes
    ("ref/arc-medium/uda-wendo", "11"): True,        # "[kineticist] ... (Occult Adventures 11)": the same case
    ("ref/arc-magus/spell-trapper", "64"): False,    # "ranger traps (Ultimate Magic 64)": "traps" links to the rule of traps, which the second-mention rule takes for the name before the parenthesis; ranger traps are another thing, and no link names them
}


def link_names_ability(label: str, target: str) -> bool:
    """A link on a class or a possessive word ("[alchemist's](ref/class/alchemist) mutagen ability", "[cavalier] class feature",
    "[nymph's] unearthly grace") names the owner of the ability that a following citation cites, not the ability. A link to one thing
    of a class (`ref/class/gunslinger#gunsmith`) is such a thing."""
    plain = re.sub(r"[\x01\x02_*\\]", "", label)
    return bool(re.search(r"(?:['\u2019]s|s['\u2019])$", plain) or re.fullmatch(r"ref/(?:class|pclass)/[^#]+", target))


def _close_italics(citation: str) -> str:
    """What stays of a dropped citation: the italic that the text layer set over a spell name and the title in its citation as one run
    ("_overwhelming presence (Pathfinder RPG Ultimate Magic_ 230)") closes where the citation was, so that the name keeps its italics."""
    extra = citation.count(I_CLOSE) - citation.count(I_OPEN)
    return I_CLOSE * extra if extra > 0 else ""


def drop_linked_citation(pattern: str, text: str, links: list[tuple[str, str]], entry_id: str = "") -> str:
    """Owner ruling 26 (Muse review of #335): a printed page citation goes where the link just before it already points at the thing
    that the citation cites ("mutagen (Ultimate Magic 14)", "[steal] combat maneuver (Advanced Player's Guide 322)": the link may cover
    only part of the phrase, with up to five plain words between it and the parenthesis). The link is the one that `apply_links` will
    place, and the nearest one before the parenthesis. A name that repeats a link label of the same paragraph and ends the phrase is that
    link's second mention and goes too, unless "see" points at it. The citation stays where no link takes its place (Idealist's
    "arbitrament (page 39)": a comma ends the phrase), and where words stand between the parenthesis and a link on a class or a
    possessive word, because the citation names an ability of that class. `EDGE_CITATIONS` has the few that the words cannot show."""
    marks = r"[\x01\x02_*\\]"
    probe = apply_links(text, links)[0]                    # the text as it will read with its links, to see which words they cover
    here, there = list(re.finditer(pattern, text)), list(re.finditer(pattern, probe))
    if len(here) != len(there):
        raise ValueError(f"a link falls inside a citation: {text[:80]!r}")
    out, at = [], 0
    for m, q in zip(here, there):
        out.append(text[at:m.start()])
        at = m.end()
        pages = re.findall(r"\d+(?:[–-]\d+)?", m.group(0))
        edge = EDGE_CITATIONS.get((entry_id, pages[-1] if pages else ""))
        if edge is not None:
            drop = edge
        else:
            before = re.sub(marks, "", probe[:q.start()]).rstrip()
            hit = re.search(r"\[([^\]]+)\]\(([^)]*)\)((?:\s+[\w'\u2019-]+){0,5})$", before)
            if hit:
                drop = not hit.group(3).strip() or not link_names_ability(hit.group(1), hit.group(2))
            else:
                # the name is a second mention of a link of the same paragraph ("[black blade] ... a black blade (Ultimate Magic 47)"),
                # unless it is a pointer ("See the bard (Core Rulebook 35)": owner ruling 16 keeps a cross-reference)
                para = before.rsplit("\n\n", 1)[-1]
                names = [re.sub(r"[\\]", "", lb).lower() for lb, _ in re.findall(r"\[([^\]]+)\]\(([^)]*)\)", para)]
                tail = para.lower()
                drop = (any(lb and re.search(r"(?<![\w'])" + re.escape(lb) + r"$", tail) for lb in names)
                        and not re.search(r"\bsee\b(?:\s+[\w'\u2019-]+){0,3}$", tail))
        out.append(_close_italics(m.group(0)) if drop else m.group(0))
    out.append(text[at:])
    return "".join(out)


def drop_semicolon_citation(pattern: str, text: str, links: list[tuple[str, str]]) -> str:
    """The "; Book 28" at the end of a parenthesis ("(including the alchemist's bomb class ability; Advanced Player's Guide 28)"): it
    goes where the parenthesis has a link before the semicolon, or follows a link directly ("[Expert Driver] (water vehicles only;
    Ultimate Combat 100)"), because the link names the rule (owner ruling 26)."""
    probe = apply_links(text, links)[0]
    here, there = list(re.finditer(pattern, text)), list(re.finditer(pattern, probe))
    if len(here) != len(there):
        raise ValueError(f"a link falls inside a citation: {text[:80]!r}")
    out, at = [], 0
    for m, q in zip(here, there):
        out.append(text[at:m.start()])
        at = m.end()
        seen = re.sub(r"\[([^\]]*)\]\([^)]*\)", "\x03\\1\x04", probe[:q.start()])    # a link marks its label, its target has no parenthesis
        opened = seen.rfind("(")
        linked = opened >= 0 and ")" not in seen[opened:] and ("\x03" in seen[opened:] or seen[:opened].rstrip().endswith("\x04"))
        out.append(_close_italics(m.group(0)) if linked else m.group(0))
    out.append(text[at:])
    return "".join(out)


def tidy_italics(text: str) -> str:
    """Italic marks of the layer, tidied for the books that set their italics in the text layer (`ITALIC_JOIN`): two italic runs with a blank between
    are one span, a closing parenthesis or a full stop that the run took is roman."""
    if not ITALIC_JOIN["on"]:
        return text
    text = re.sub(I_CLOSE + " " + I_OPEN, " ", text)       # the layer sets each word of "see invisibility" as an italic run of its own
    text = re.sub("(" + I_OPEN + r"[^" + I_OPEN + I_CLOSE + r"()]*)\)" + I_CLOSE, r"\1" + I_CLOSE + ")", text)       # "(... from _Pathfinder Unchained)_": the closing parenthesis is roman
    text = re.sub("(" + I_OPEN + r"[^" + I_OPEN + I_CLOSE + r"]*[^" + I_OPEN + I_CLOSE + r"\s.,;:])([.,;:]+)" + I_CLOSE, r"\1" + I_CLOSE + r"\2", text)       # "_wish._": the full stop is roman
    return text


def print_md(feat: PrintFeature, links: list[tuple[str, str]], vocab: set[str], entry_id: str = "",
             keep_marks: bool = False) -> tuple[str, list[str], list[str]]:
    """The printed paragraphs as Markdown, the link texts that found no place, and the notes (misprint fixes,
    dropped asterisks)."""
    paras = join_wrapped([clean_runs(runs) for runs in feat.paras], vocab)
    text = "\n\n".join(paras)
    text = tidy_italics(text)
    if OCR["on"]:
        for pat, rep in OCR_JOINED:
            text, n = pat.subn(rep, text)
            OCR_HITS[(OCR_BOOK["name"], pat.pattern)] += n
    notes: list[str] = []
    fixed = re.sub(r"^A (\d+(?:st|nd|rd|th) level\b)", r"At \1", text)
    if fixed != text:
        notes.append("misprint fixed: print has \"A " + text.split(" level", 1)[0][2:] + " level\", the lead is \"At " + text.split(" level", 1)[0][2:] + " level\"")
        text = fixed
    # print's asterisks mark a talent or a feat that has a prerequisite; the key is not printed here (ruling 10)
    # a mark is `*` or `**`: the whole mark goes, never one star of it. The marks stay when the entry prints its key
    # (Crusader: "Bonus feats marked with an asterisk (*) must be applied to the favored weapon").
    stripped = text if keep_marks else re.sub(r"(?<=[\w)\]" + I_CLOSE + r"])(?:\\\*)+", "", text)
    if stripped != text:
        notes.append("print asterisks without their key dropped")
        text = stripped
    for eid, wrong, right, why in MISPRINTS:
        if eid == entry_id and wrong in text:
            text = text.replace(wrong, right)
            notes.append(f"misprint fixed: print has \"{wrong}\", written \"{right}\" ({why})")
    # print sets the italic of a title inside a parenthesis; the extraction can open it before the parenthesis ("_(Occult Adventures_ 48)")
    text = re.sub(r"\x01\(([^()\x01\x02]*)\x02", "(\x01\\1\x02", text)
    # a page reference of the book ("Pathfinder RPG Core Rulebook page 469"): the corpus links instead
    cite_rpg, cite_book, cite_page, cite_semi = _cites()
    text = drop_linked_citation(cite_rpg, text, links, entry_id)
    # a "(see ...)" cross-reference stays (owner ruling 16 of 2026-11-24). A page citation of another book without
    # "see" ("(Core Rulebook 123)", "(page 83)"): the corpus links instead
    xref = drop_linked_citation(cite_book, text, links, entry_id)
    # a bare book citation at the end of a parenthesis ("(including the alchemist's bomb class ability; Advanced
    # Player's Guide 28)", owner ruling 26): the corpus links the named rule
    xref = drop_semicolon_citation(cite_semi, xref, links)
    # a book reference in front of or behind a level inside a list ("(Advanced Player's Guide 212; 4th)", "(14th, Ultimate Magic)",
    # "(Ultimate Combat, 2nd)", owner ruling 26): the level stays, the reference goes
    book = (r"[\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-5])?|"
            r"Ultimate (?:Magic|Combat|Equipment|Campaign)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures)[\x02_]*")
    if CITE_EXT["on"]:
        book = (r"[\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-5])?|"
                r"Ultimate[\s\x01\x02_]+(?:Magic|Combat|Equipment|Campaign|Intrigue)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures|"
                r"Inner Sea World Guide|Pathfinder Unchained)[\x02_]*")
    xref = re.sub(r"\(" + book + r"(?:\s*\d+(?:[–-]\d+)?)?[;,]\s*(?=\d+(?:st|nd|rd|th))", "(", xref)
    xref = re.sub(r",\s*" + book + r"(?:\s*\d+(?:[–-]\d+)?)?(?=\))", "", xref)
    # a parenthesis that is only "page 83" or "Core Rulebook page 469" (a title of capitalized words, then the page): a
    # citation with words of its own ("as if he had cast greater magic aura; see page 219", "as lesser simulacrum on
    # page 238 of Ultimate Magic") has a rule or a pointer and stays (owner rulings 16 and 26)
    xref = drop_linked_citation(cite_page, xref, links, entry_id)
    if xref != text:
        notes.append("printed cross-reference left out")
        text = xref
    # the key of print's asterisks ("An asterisk (*) indicates ...", "* Indicates a new feat in this book."): print apparatus
    keyless = re.sub(r"(?:^|\n\n)(?:An asterisk \(\\\*\)|\\\*) [Ii]ndicates[^\n]*", "", text)
    if keyless != text:
        notes.append("print's asterisk key left out")
        text = keyless.strip()
    text = balance_marks(text)
    text = apply_errata(text, entry_id, anchor_of(head_text(feat.head)), notes)
    if getattr(feat, "errata", 0):
        notes.append(f"errata: Paizo errata for {ERRATA_BOOKS.get(ERRATA_CTX['book'], '')} p. {feat.errata} replaces this ability")
    lost: list[str] = []
    if links:
        links = [l for l in links if (entry_id, l[0]) not in LINK_DROP]
        text, links = apply_context_links(entry_id, text, links)
        text, lost = apply_links(text, links)
    return render_marks(text), lost, notes


def opening_with_links(entry_id: str, text: str, links: list[tuple[str, str]], deferred: list[tuple[str, str]]) -> str:
    """The links of the opening placed in the text of the opening. A link that CONTEXT_LINKS ties to a phrase that the opening does
    not hold goes to `deferred`: a section places it (Umbral Scion: the import's "Prerequisites: Shadow bloodline" is printed in
    the Bloodline section, and the opening says "potent shadow heritage")."""
    text, rest = apply_context_links(entry_id, text, links)
    for l in list(rest):
        if (entry_id, l[0]) in CONTEXT_LINKS:
            rest.remove(l)
            deferred.append(l)
    return apply_links(text, rest)[0]


def apply_context_links(entry_id: str, text: str, links: list[tuple[str, str]]) -> tuple[str, list[tuple[str, str]]]:
    """Place the links that CONTEXT_LINKS ties to a phrase of this text (the link keeps the case that print has); returns
    the text and the links still to place."""
    rest = list(links)
    for label, target in links:
        phrase = CONTEXT_LINKS.get((entry_id, label))
        if phrase and phrase in text:
            text = text.replace(phrase, phrase[: -len(label)] + f"[{phrase[-len(label):]}]({target})", 1)
            rest.remove((label, target))
    return text, rest


def final_citations(text: str, entry_id: str = "") -> str:
    """Owner ruling 26 on the finished Markdown: a book citation that follows a link goes. `print_md` drops them before the links of the
    entry are placed, so a link that only the placement of a lost link, or the import's own opening text, brings (Ward Spiritualist's
    "[spirit-bound blade] (Pathfinder RPG Occult Adventures 186)", the openings of Shadow Scion, Nornkith and Wasteland Blightbreaker)
    needs this second pass. The patterns and the rules are those of `print_md`, read on text that already has its links."""
    marked = re.sub(r"_([^_\n]*)_", lambda m: I_OPEN + m.group(1) + I_CLOSE, text)
    out = drop_linked_citation(CITE_RPG, marked, [], entry_id)
    out = drop_linked_citation(CITE_BOOK, out, [], entry_id)
    out = drop_semicolon_citation(CITE_SEMI, out, [])
    out = drop_linked_citation(CITE_PAGE, out, [], entry_id)
    return out.replace(I_OPEN, "_").replace(I_CLOSE, "_")


def balance_marks(s: str) -> str:
    """Drops an italic mark that has no partner (a cut that took the text between two marks)."""
    out, depth, opened = [], 0, []
    for ch in s:
        if ch == I_OPEN:
            depth += 1
            opened.append(len(out))
            out.append(ch)
        elif ch == I_CLOSE:
            if depth == 0:
                continue
            depth -= 1
            opened.pop()
            out.append(ch)
        else:
            out.append(ch)
    for i in reversed(opened):
        del out[i]
    return "".join(out)


def head_text(head: str) -> str:
    return re.sub(r"\s+", " ", head.replace("’", "'").replace("‘", "'")).strip()


def unprinted_notes(opening: list[list[str]], printed: list[str]) -> list[int]:
    """Indices of the blockquote notes of the import's opening text that print does not have (ruling 10): fewer than
    half of their words are in the printed opening."""
    have = set(tokens(" ".join(printed)))
    out = []
    for i, block in enumerate(opening):
        if block[0].lstrip().startswith(">"):
            tk = tokens(" ".join(re.sub(r"^\s*>\s?", "", ln) for ln in block))
            if tk and sum(1 for t in tk if t in have) * 2 < len(tk):
                out.append(i)
    return out


# A head of the import that misspells the printed head (data fix; the section is the printed one): the entry, the
# import's head, the printed head. Gun Tank (Ultimate Combat p. 50): "Bullet Defection (Ex)" for "Bullet Deflection (Ex)".
IMPORT_HEAD_FIXES = {
    ("ref/arc-gunslinger/gun-tank", "Bullet Defection (Ex)"): "Bullet Deflection (Ex)",
}


def import_name(entry_id: str, name: str) -> str:
    return IMPORT_HEAD_FIXES.get((entry_id, name), name)


# Links the import lacks and the owner asked for (a feature of the entry, found by its printed head): the entry, the
# anchor, the labels and targets. Gunmaster (Ultimate Intrigue p. 61): "the gunslinger's gunsmith ability".
EXTRA_LINKS = {
    ("ref/arc-vigilante/gunmaster", "gunmaster"): [("gunsmith", "ref/class/gunslinger#gunsmith")],
}

# A link of the import that points at the wrong thing: the entry and the label, retargeted (the TSV does not list it; the PR says so).
# Faith Hunter's Hateful Bane means the inquisitor class feature, not the spell (owner review of batch 3).
LINK_RETARGETS = {
    ("ref/arc-inquisitor/faith-hunter", "bane"): "ref/class/inquisitor#bane",
    # review of #356: the second "distraction" of these entries links the universal monster rule; print means the bard performance
    ("ref/arc-rogue/carnivalist", "distraction"): "ref/performance/distraction",
    ("ref/arc-bard/ringleader-ui", "distraction"): "ref/performance/distraction",
    ("ref/arc-paladin/martyr", "distraction"): "ref/performance/distraction",
}


def feature_links(entry_id: str, f, head: str) -> list[tuple[str, str]]:
    """The links of a feature in the import, retargeted where LINK_RETARGETS says so, plus the extra ones."""
    links = [(lb, LINK_RETARGETS.get((entry_id, lb), tg)) for lb, tg in old_links(f)]
    return links + EXTRA_LINKS.get((entry_id, anchor_of(head)), [])


# A misprint of an opening text, which the compare keeps from the import when the words agree: the entry and the note
# that the review table records (owner ruling 9).
# The opening text keeps the import's words when its words (stemmed) are the printed ones; an entry whose import differs from print in
# an ending only (a plural possessive) is named here, with the printed word, so that its opening text is written from print.
OPENING_FROM_PRINT_FORCED = {
    "ref/arc-cavalier/verdivant": "leshys'",         # print: "Some vine leshys' spirits ..."; the import: "Some vine leshy spirits ..."
}

OPENING_NOTES = {
    "ref/arc-bard/masked-performer": 'misprint fixed: print has "a entertainer" in the opening text, written "an entertainer" (the import has the article right)',
}


# A link of the import that belongs on one phrase of the text, not on the first occurrence of its word: the entry, the
# label and the words that end with it. Fey Caller (Ultimate Intrigue p. 71): the import links "fey" in "also counts as a
# fey", the first "fey" of the text is the name of the archetype.
# A link of the import that belongs to text this entry no longer has in the place where the placement would put it: the link of the
# domain list of the Treesinger's Plant Bond (an unlisted section written in full, ruling 46) would otherwise land on "target plant" of
# Eldritch Botanist. The entry writes the link in the section's own text (owner review of #344).
LINK_DROP = {
    ("ref/arc-druid/supernaturalist", "plant"),
    ("ref/arc-paladin/chaos-knight", "fast healing"),       # the import links "fast healing" twice in the table row; the hand text of Blessings of the Maelstrom links the first mention (review of #351)
}


MISPRINTS.append(
    ("ref/arc-cleric/triadic-priest", "within 10 feet of least one", "within 10 feet of at least one",
     "print has \"of least one\" where \"of at least one\" belongs (Blood of the Coven p. 19; owner ruling 9, review of #344)"))


CONTEXT_LINKS = {
    ("ref/arc-gunslinger/scatter-gunner", "scatter"): "with the scatter",     # the link of the import is on "scatter weapon quality", not on the archetype's name
    ("ref/arc-unchained-summoner/fey-caller", "fey"): "counts as a fey",
}


def dagger_key_printed(pfeats: list[PrintFeature], opening: list[list] | None = None) -> bool:
    """Whether the printed section holds the key of its daggers: a paragraph that starts with the dagger ("†This spell is not
    added to your cleric list ...", Idealist): then its marks stay (owner ruling 10)."""
    paras = [runs for pf in pfeats for runs in pf.paras] + list(opening or [])
    for runs in paras:
        t = "".join(r[0] for r in runs).lstrip()
        if t.startswith(DAGGER) and len(t.split()) >= 4:
            return True
    return False


def marks_key_printed(pfeats: list[PrintFeature], vocab: set[str], opening: list[list] | None = None) -> bool:
    """Whether the printed section holds a key of its asterisks (a sentence that names the asterisk and is not the
    book's "An asterisk (*) indicates ..." line): then its marks stay (owner ruling 10). The opening counts: the White-Haired Witch
    says "Rogue talents and advanced rogue talents marked with an asterisk (*) can be found in the Pathfinder RPG Advanced Player's Guide"
    in its first paragraph (Dragon Empires Primer p. 23)."""
    for runs in (opening or []):
        t = finish_text(clean_runs(runs), vocab)
        if re.search(r"\basterisks?\b", t, re.I):
            return True
    for pf in pfeats:
        for runs in pf.paras:
            t = finish_text(clean_runs(runs), vocab)
            t = re.sub(r"(?:^|\n\n)(?:An asterisk \(\\\*\)|\\\*) [Ii]ndicates[^\n]*", "", t)
            if re.search(r"\basterisks?\b", t, re.I):
                return True
    return False


# Where the printed section of an archetype ends although no title follows: the next section of the chapter begins with a bold
# line that is no feature of the archetype. Elder Mythos Cultist (Horror Adventures p. 49) is followed by "NEW DOMAIN" and "NEW
# SUBDOMAINS" (the corpus has them as the Void domain and the subdomains); Psychokineticist (p. 57) by "UTILITY WILD TALENTS" (the
# corpus has Elemental Whispers and Greater Elemental Whispers as wild talents).
SECTION_ENDS = {
    "ref/arc-cleric/elder-mythos-cultist": "NEW DOMAIN",
    "ref/arc-kineticist/psychokineticist": "UTILITY WILD TALENTS",
}


def cut_section(entry_id: str, section: list[Para]) -> list[Para]:
    """The section up to the line that SECTION_ENDS names for the entry."""
    end = SECTION_ENDS.get(entry_id)
    if not end:
        return section
    for i, p in enumerate(section[1:], 1):
        if squash(p.plain()).startswith(squash(end)):
            return section[:i]
    return section


# Paragraphs that print sets beside art, where the line that continues a paragraph is set in like a first line: the text that starts the line, joined to
# the paragraph before it (the review of #347, checked on the page images)
PARA_JOINS = {
    ("ref/arc-fighter/molthuni-defender", "armored-defense"): ("This bonus also applies to the DC",),
    ("ref/arc-paladin/legate", "celestial-armor"): ("The legate can use this ability a number of times",),
    ("ref/arc-alchemist/construct-rider", "craft-mount"): ("The GM may approve other animals as mounts.",),
    ("ref/arc-rogue/earthshadow", "earthlink"): ("When an earthshadow is in direct contact",),
}


# Repairs of the extraction that the page images show (not corrections of print): a mark that the text layer sets one character off, a space before
# a dash, a link on a word that is no name of the rule (review of #347). (entry, anchor): [(wrong, right)]; each must match, or the run fails.
TEXT_REPAIRS = {
    ("ref/arc-cleric/herald-caller", "mighty-heralds"): [("P_athfinder RPG Advanced Class Guide_", "_Pathfinder RPG Advanced Class Guide_")],
    ("ref/arc-summoner/morphic-savant", "chaos-magic"): [("3rd \u2014_magic circle", "3rd\u2014_magic circle")],
    ("ref/arc-unchained-summoner/morphic-savant", "chaos-magic"): [("3rd \u2014_magic circle", "3rd\u2014_magic circle")],
    ("ref/arc-wizard/bonded-wizard", "bonded-force"): [("[shield](ref/spell/shield) bonus", "shield bonus")],
}


def repair_text(entry_id: str, anchor: str, text: str) -> str:
    for wrong, right in TEXT_REPAIRS.get((entry_id, anchor), ()):
        if wrong not in text:
            raise SystemExit(f"TEXT_REPAIRS: `{wrong}` is not in {entry_id} `{anchor}`")
        text = text.replace(wrong, right)
    return text


def join_paras(entry_id: str, anchor: str, text: str) -> str:
    for start in PARA_JOINS.get((entry_id, anchor), ()):
        text = text.replace("\n\n" + start, " " + start, 1)
    return text


def compare_entry(e: Entry, section: list[Para], book: Book) -> dict:
    """The comparison of one archetype with its printed section: a row for each printed head, in print
    order, then one for each feature of the import that print lacks."""
    section = cut_section(e.id, section)
    plain_names = [m.group(1) for b in blocks_of(e.body) for m in [NAME_BLOCK.match(logical(b))] if m]
    probe = {namekey(h) for h in [head_of_para(p) for p in section[1:]] if h}
    opening_imp, feats = parse_import(e.body, probe)
    names = [f.name for f in feats]
    opening_print, pfeats = split_print(section, plain_names + [tail_name(n) for n in names])
    ERRATA_CTX["used"] -= {u for u in ERRATA_CTX["used"] if u[0] == e.id}
    for pf in pfeats:
        rep = ERRATA_FEATURES.get((e.id, anchor_of(head_text(pf.head))))
        if rep:
            pf.head, pf.errata, text_ = rep[0], rep[1], rep[2]
            pf.paras = [[(escape_md(text_), False, False)]]
    vocab = book.vocab | {w.lower() for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", e.body)} | {
        p.lower() for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)+", e.body) for p in w.split("-")}
    # match the heads in order, so a name that occurs twice is matched to its own printed head
    used: set[int] = set()
    last = -1
    matched: list[int | None] = []
    for pf in pfeats:
        key = namekey(pf.head)
        idx = next((i for i in range(last + 1, len(feats)) if i not in used and namekey(import_name(e.id, feats[i].name)) == key), None)
        if idx is not None:
            used.add(idx)
            last = idx
        matched.append(idx)
    # a head that print sets in another order than the import (a sidebar before a list) matches wherever it stands
    for n, pf in enumerate(pfeats):
        if matched[n] is None:
            key = namekey(pf.head)
            idx = next((i for i in range(len(feats)) if i not in used and namekey(import_name(e.id, feats[i].name)) == key), None)
            if idx is not None:
                used.add(idx)
                matched[n] = idx
    keep = marks_key_printed(pfeats, vocab, opening_print)
    DAGGER_KEEP["on"] = dagger_key_printed(pfeats, opening_print)
    problems: list[str] = []
    lost_heads = [feats[i].name for i in range(len(feats)) if i not in used]
    if lost_heads:
        problems.append("head not printed: " + ", ".join(lost_heads))
    title_tokens = set(tokens(e.title)) | {w for c in e.classes for w in tokens(c.split("/")[-1].replace("-", " "))}
    rows = []
    for pf, idx in zip(pfeats, matched):
        head = fix_ligatures(head_text(pf.head), vocab)
        if idx is None:
            text, _, pnotes = print_md(pf, [], vocab, e.id, keep)
            rows.append({"anchor": anchor_of(head), "span": "", "page": pf.page, "pseudo": False, "draft": "",
                         "level_import": None, "head": head, "print": text, "status": "print",
                         "notes": ["head printed, not in the import: added from print"] + pnotes,
                         "listed": not is_scaffold(head) and not is_option_head(head, pf.bold) and not DASH_KEY.fullmatch(head),
                         "option": is_option_head(head, pf.bold) and not DASH_KEY.fullmatch(head),
                         "name": pf.head})
            continue
        f = feats[idx]
        draft = build_draft(f)
        text, lost, pnotes = print_md(pf, feature_links(e.id, f, head), vocab, e.id, keep)
        text = repair_text(e.id, anchor_of(head), join_paras(e.id, anchor_of(head), text))
        # a printed "(see ...)" cross-reference is kept in the text but is not a rule word: the corpus links instead
        cmp = compare_feature(draft, strip_citations(re.sub(r"\s*\([Ss]ee\b[^()]*\)", "", text)), set(tokens(ABILITY_TAG.sub("", f.name))), title_tokens)
        # the whole row, then its parts: a name that is a list ("The 1st-, 9th-, and 15th-level channel energy
        # abilities") is one stored trade, a row of several names is several
        named = list(dict.fromkeys(x.strip() for it in f.items if it.label in ("Replaces", "Alters")
                                   for x in [re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", it.content)]
                                   + re.split(r",| and ", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", it.content)) if x.strip()))
        row = {"anchor": anchor_of(head), "span": f.span_sha(), "page": pf.page, "pseudo": f.pseudo,
               "import_trades": named, "links": [],
               "draft": draft.text, "level_import": draft.level, "head": head, "print": text,
               "status": cmp.status, "notes": list(cmp.notes) + pnotes, "name": pf.head}
        if lost:
            row["notes"].append("link not placed: " + ", ".join(lost))
            pool = list(feature_links(e.id, f, head))
            row["lost_links"] = []
            for label in lost:
                at = next((k for k, (lb, _t) in enumerate(pool) if lb == label), None)
                if at is not None:
                    row["lost_links"].append(pool.pop(at))
        row["option"] = (is_option_head(head, pf.bold) and not f.pseudo) or (e.id, row["anchor"]) in OPTION_HEADS
        if DASH_KEY.fullmatch(head):
            row["option"] = False
        row["listed"] = not is_scaffold(head) and not f.pseudo and not row["option"] and not DASH_KEY.fullmatch(head)
        if (e.id, row["anchor"]) in PRINT_WINS and row["status"] == "hold":
            row["status"], row["notes"] = "print", [PRINT_WINS[(e.id, row["anchor"])]] + pnotes
        rows.append(row)
    for i, f in enumerate(feats):
        if i not in used:
            rows.append({"anchor": anchor_of(f.name), "span": f.span_sha(), "page": "", "pseudo": f.pseudo,
                         "links": old_links(f),
                         "draft": build_draft(f).text, "level_import": None, "head": head_text(f.name), "print": "",
                         "status": "hold", "notes": ["head not printed"], "listed": False, "name": f.name})
    for r in rows:
        # a head that only lists the options that complement the archetype ("The following slayer talents complement the
        # sniper archetype: ...") is a label, not a feature
        plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", r["print"]).replace("_", "")
        if r["listed"] and re.match(r"(?:The following|These)\b[^.:]{0,120}\bcomplements?\b", plain) and not trade_sentences(plain):
            r["listed"] = False
            r["notes"].append("label head (a list of the options that complement the archetype), not a feature")
    for r in rows:
        if (e.id, r["anchor"]) in PLAIN_HEADS:
            r["listed"], r["option"] = False, False
    for (eid, anchor), (head, page, after, text_) in ERRATA_ADDED.items():
        if eid != e.id:
            continue
        i = next((n for n, r in enumerate(rows) if r["anchor"] == anchor and r["status"] == "hold" and "head not printed" in r["notes"]), None)
        if i is None:
            problems.append(f"errata ability `{anchor}` has no feature in the import")
            continue
        row = rows.pop(i)
        problems[:] = [p for p in problems if not p.startswith("head not printed")] + (
            ["head not printed: " + ", ".join(r["head"] for r in rows if r["status"] == "hold" and "head not printed" in r["notes"])]
            if any(r["status"] == "hold" and "head not printed" in r["notes"] for r in rows) else [])
        txt, lost = apply_links(text_, row.get("links", []))
        row.update(print=txt, status="print", page=page, listed=True, option=False, head=head, name=head,
                   notes=[f"head added by the Paizo errata for {ERRATA_BOOKS.get(ERRATA_CTX['book'], '')} p. {page}"]
                   + (["link not placed: " + ", ".join(lost)] if lost else []))
        at = 0 if after is None else next(n for n, r in enumerate(rows) if r["anchor"] == after) + 1
        rows.insert(at, row)
    # the opening text is print's too, with the errata (Divine Tracker p. 108: the errata removes "imbued")
    opening = []
    for joined in join_wrapped([clean_runs(r) for r in opening_print], vocab):
        o_notes: list[str] = []
        o = apply_errata(tidy_italics(joined), e.id, "opening", o_notes)
        opening.append(render_marks(o))
        if o_notes and rows:
            rows[0]["notes"] += o_notes
    problems += errata_unused(e.id)
    links = [(m.group(2), m.group(3)) for b in opening_imp for m in LINK.finditer(logical(b))]
    for i, f in enumerate(feats):
        if i not in used or e.id in OPENING_ONLY:
            links += old_links(f)          # an entry that is an opening only: the links of the import's sections go with its text
    kept = [o for o in opening if o]
    # the opening text follows print: when the import's words differ from the printed ones (an unprinted sentence, a
    # broken row, `Prerequisites` rows for printed prose), the printed paragraphs are written
    gone = unprinted_notes(opening_imp, kept)
    imp_words = Counter(tokens(" ".join(logical(b) for i, b in enumerate(opening_imp) if i not in gone)))
    print_words = Counter(tokens(" ".join(kept)))
    diff = sorted(((imp_words - print_words) + (print_words - imp_words)).elements())
    if not diff and "\u2014" in " ".join(kept) and "\u2014" not in " ".join(logical(b) for i, b in enumerate(opening_imp) if i not in gone):
        diff = ["\u2014"]          # the import writes the printed em dash as " - "
    if not diff and e.id in OPENING_FROM_PRINT_FORCED:
        diff = [OPENING_FROM_PRINT_FORCED[e.id]]
    return {"rows": rows, "problems": problems, "opening": kept, "opening_links": links,
            "opening_dropped": [logical(opening_imp[i]) for i in gone], "opening_diff": diff,
            "section_end": (getattr(section, "end", None), getattr(section, "end_known", True))}


def contained_in_longer(phrase: str, trades: list[dict], i: int) -> bool:
    """Whether every place where the phrase names trade `i` lies inside the name of a longer stored trade of the
    same op ("replaces mass suggestion" names `Mass suggestion`, so it does not also name `Suggestion`; "replaces
    quarry and improved quarry" names both, because `quarry` stands once outside `improved quarry`)."""
    op, name = trade_name(trades[i])
    mine = phrase_tokens(ABILITY_TAG.sub("", name))
    p = phrase_tokens(phrase)

    def spans(tokens_: list[str]) -> list[tuple[int, int]]:
        return [(k, k + len(tokens_)) for k in range(len(p) - len(tokens_) + 1) if p[k:k + len(tokens_)] == tokens_]

    own = spans(mine)
    if not own:
        # a step of a numbered list ("armor training 3") that the phrase names only inside a longer step list
        # ("armor training 1, 2, 3, and 4") that another stored trade of the op holds
        if len(mine) > 1 and mine[-1].isdigit():
            base, d = mine[:-1], mine[-1]
            for j, other in enumerate(trades):
                if j == i or trade_name(other)[0] != op:
                    continue
                theirs = phrase_tokens(ABILITY_TAG.sub("", trade_name(other)[1]))
                if (len(theirs) > len(mine) and theirs[:len(base)] == base and d in theirs[len(base):]
                        and spans(theirs)):
                    return True
        return False
    longer: list[tuple[int, int]] = []
    for j, other in enumerate(trades):
        if j == i or trade_name(other)[0] != op:
            continue
        theirs = phrase_tokens(ABILITY_TAG.sub("", trade_name(other)[1]))
        if len(theirs) > len(mine) and any(theirs[k:k + len(mine)] == mine for k in range(len(theirs) - len(mine) + 1)):
            longer += spans(theirs)
    return all(any(a <= x and y <= b for a, b in longer) for x, y in own)


def trade_asides(text: str) -> list[tuple[str, str]]:
    """[(op, aside)]: the final parenthesis of four or more words that a trade sentence carries (owner ruling 29,
    "This ability replaces swift alchemy (a deep bomber never gains instant alchemy)"). An aside that starts with "see" states nothing."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[\\_*]", "", text)
    text = re.sub(r"\s+", " ", text)
    out = []
    for m in _trade_matches(text):
        sentence = m.group(1)
        verb = re.search(r"\b(replaces?|alters?|changes?|modifies)\b", sentence, re.I)
        for a in re.finditer(r"\(([^()]*)\)", sentence):           # R18: an aside inside the phrase states the trades too
            if len(a.group(1).split()) >= 4 and not a.group(1).lower().startswith("see"):
                out.append((_op_of(verb.group(1)), a.group(1)))
    return out


def prose_sentences(text: str) -> list[str]:
    """The sentences of a feature text that are not trade sentences (owner ruling 28: prose supports a trade): a
    "(see ...)" parenthesis and the part from a comparison on ("functions as the X ability") state nothing."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[\\_*]", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s*\((?:see|See)\b[^()]*\)", "", text)
    out = []
    for sent in re.split(r"(?<=[.!?])\s+", text):
        if TRADE_SENTENCE.search(sent) or re.match(r"(?:This|These|It)\b.{0,60}?\b(?:replaces?|alters?|changes?|modifies)\b", sent, re.I):
            continue
        out.append(re.split(r"\b(?:functions as|works like|as the)\b", sent, maxsplit=1)[0])
    return out


def assign_by(trades: list[dict], listed: list[dict], opening: list[str]) -> tuple[dict[int, list[str]], list[str]]:
    """For each trade, the anchors of the listed features whose printed text states it. A trade that print
    states only in the opening text (the blocks before the first listed feature) gets no `by`. A trade that
    print never states in a sentence takes the listed feature of its own name that prints no trade sentence
    (owner ruling A of 2026-11-24: the feature prints the changed ability). Returns the map and the problems."""
    problems: list[str] = []
    by: dict[int, list[str]] = {}
    sentences = {f["anchor"]: trade_sentences(f["print"], f.get("head", "")) for f in listed}
    opening_sentences = [s for o in opening for s in trade_sentences(o)]
    for i, t in enumerate(trades):
        op, name = trade_name(t)
        if t.get("_no_by"):
            by[i] = []
            continue
        anchors = [f["anchor"] for f in listed
                   if any(sop == op and covers(ph, name) and not contained_in_longer(ph, trades, i)
                          for sop, ph, _ in sentences[f["anchor"]])]
        if anchors:
            by[i] = anchors
        elif any(sop == op and covers(ph, name) and not contained_in_longer(ph, trades, i)
                 for sop, ph, _ in opening_sentences):
            by[i] = []
        else:
            if t.get("_prose_by") and any(f["anchor"] == t["_prose_by"] for f in listed):
                by[i] = [t["_prose_by"]]        # owner ruling 28: the prose of that feature states the trade
                continue
            # ruling A per operation (owner ruling 24): the feature prints no sentence of the trade's own op
            quiet = lambda f: not any(sop == op for sop, _, _ in sentences[f["anchor"]])
            own = [f["anchor"] for f in listed if quiet(f) and namekey(f["head"]) == namekey(name)]
            if not own:
                # the feature under which the import held the `**Replaces:**` / `**Alters:**` row of this trade
                own = [f["anchor"] for f in listed
                       if quiet(f) and namekey(name) in {namekey(x) for x in f.get("import_trades", [])}]
            if own:
                by[i] = own
            elif (op == "alters" and t.get("feature") == "weapon-and-armor-proficiencies"
                  and not any(sop == "alters" for sop, _, _ in opening_sentences)):
                by[i] = []              # owner ruling 23, per operation: a proficiency section that prints no `alters` sentence
            else:
                # owner rulings 28 and 29: the prose of a feature, or the aside of one of its trade sentences of the same op
                prose = [f["anchor"] for f in listed
                         if any(covers(sent, name) for sent in prose_sentences(f["print"]))
                         or any(sop == op and covers(aside, name) for sop, aside in trade_asides(f["print"]))]
                if len(prose) == 1:
                    by[i] = prose
                else:
                    problems.append(f"the {op} trade `{name}` is not printed in a sentence, and no listed feature of that name prints it")
    for i, t in enumerate(trades):
        if t.get("_extra_by"):
            # owner ruling 47: an ability gained at a fixed level that replaces a class feature carries the trade, though print states it once
            have = set(by.get(i, [])) | {a for a in t["_extra_by"] if any(f["anchor"] == a for f in listed)}
            by[i] = [f["anchor"] for f in listed if f["anchor"] in have]
    for f in listed:
        for sop, ph, bare in sentences[f["anchor"]]:
            if not bare and not any(sop == trade_name(t)[0] and covers(ph, trade_name(t)[1]) for t in trades):
                problems.append(f"{f['head']}: the sentence \"This ability {sop} {ph}\" names no trade")
    return by, problems


# A stored trade whose printed name the reader cannot match to the printed sentence takes the printed
# words (owner instruction of 2026-11-24; the `feature` link and the ids stay). The TSV note records it.
TRADE_RENAMES = {
    ("ref/arc-witch/hagbound", "1st-level hex"): "Hex gained at 1st level",
    ("ref/arc-witch/hagbound", "2nd-, 8th-, and 14th-level hexes"): "The hexes gained at 2nd, 8th, and 14th levels",
    ("ref/arc-witch/hagbound", "4th- and 12th-level hexes"): "The hexes gained at 4th and 12th levels",
    ("ref/arc-witch/hagbound", "10th-level hex"): "Hex gained at 10th level",
    ("ref/arc-witch/hagbound", "20th-level hex"): "Hex gained at 20th level",
    ("ref/arc-witch/putrefactor", "1st-level hex"): "Hex gained at 1st level",
    ("ref/arc-witch/putrefactor", "2nd-level hex"): "Hex gained at 2nd level",
    ("ref/arc-witch/putrefactor", "4th-, 10th-, and 16th-level hexes"): "The hexes gained at 4th, 10th, and 16th levels",
    ("ref/arc-witch/putrefactor", "6th-level hex"): "Hex gained at 6th level",
    ("ref/arc-sorcerer/stone-warder", "3rd-level bloodline spell"): "The bloodline spell gained at 3rd level",
    ("ref/arc-sorcerer/stone-warder", "7th-level bloodline feat"): "The bloodline feat gained at 7th level",
    ("ref/arc-witch/rhetorician", "1st-level hex"): "Hex gained at 1st level",
    ("ref/arc-witch/rhetorician", "All spells granted by the witch's patron"): "All the spells the witch gains from her patron",
    ("ref/arc-monk/elemental-monk", "All bonus feats"): "All of the monk's bonus feats",
    ("ref/arc-ninja/mask-of-the-living-god", "Weapon and armor proficiency"): "The mask of the Living God's weapon and armor proficiency",
    ("ref/arc-oracle/divine-numerologist", "The bonus spells gained at 10th, 12th, 14th, 16th, and 18th levels from the oracle's mystery"): "The oracle's normal mystery bonus spells at these levels",
    # Batch of Psychic Anthology, Disciple's Doctrine, Occult Origins, Arcane Anthology and Blood of the Coven: the printed words of the sentence (ruling 22)
    ("ref/arc-kineticist/kinetic-knight", "3rd-level infusion"): "The kineticist infusion gained at 3rd level",
    ("ref/arc-oracle/pei-zin-practitioner", "Class skills gained from the oracle's mystery"): "The additional class skills the oracle gains from her mystery",
    ("ref/arc-paladin/faithful-wanderer", "Skills per level"): "Class skills",
    ("ref/arc-oracle/hermit", "The bonus spells gained at 4th, 8th, 12th, and 16th levels from the oracle's mystery"): "The oracle's normal mystery bonus spells at these levels",
    ("ref/arc-wizard/chronomancer", "10th-, 15th-, and 20th-level bonus feats"): "The bonus feats gained at 10th, 15th, and 20th levels",
    ("ref/arc-witch/seducer", "1st-level hex"): "Hex gained at 1st level",
    ("ref/arc-witch/seducer", "6th-level hex"): "Hex gained at 6th level",
    ("ref/arc-witch/seducer", "8th-level hex"): "Hex gained at 8th level",
    # Batches 6 to 9 (Player Companions: Wilderness Origins, Legacy of the First World, People of the Wastes, Healer's Handbook): a stored name
    # that is not the printed wording of its sentence, rewritten as the sentence says it (ruling 22; `feature`, `levels` and ids stay)
    ("ref/arc-psychic/esoteric-starseeker", "Discipline spells"): "The bonus spells normally granted by the psychic's discipline",
    ("ref/arc-psychic/esoteric-starseeker", "1st- and 11th-level phrenic amplifications"): "The phrenic amplifications gained at 1st and 11th levels",
    ("ref/arc-psychic/magaambyan-telepath", "1st- and 11th-level phrenic amplifications"): "The phrenic amplifications gained at 1st and 11th levels",
    ("ref/arc-shifter/feyform-shifter", "Shifter aspect and all improvements to it"): "All improvements to shifter aspect",
    ("ref/arc-shifter/dragonblood-shifter", "Shifter aspect"): "Shifter aspect and all improvements to shifter aspect",
    ("ref/arc-shifter/swarm-shifter", "shifter aspect"): "Shifter aspect, and all improvements to shifter aspect",
    # The Paizo errata for Advanced Class Guide (p. 89) moves the bonus combat feats that the Wild Child replaces; the stored
    # names follow the 1st printing, so they are aligned with the sentences of the corrected text (levels: TRADE_LEVELS).
    ("ref/arc-brawler/wild-child", "Bonus combat feats gained at 2nd, 5th, 11th, and 14th levels"):
        "Bonus combat feats gained at 2nd, 8th, 14th, and 20th levels",
    ("ref/arc-brawler/wild-child", "Bonus combat feats gained at 5th, 8th, 11th, 14th, 17th, and 20th levels"):
        "Bonus combat feats gained at 5th, 11th, and 17th levels",
    # Batch 2 (Advanced Class Guide, Advanced Race Guide): a stored name that is not the printed wording in the sentence
    # of its feature, rewritten as the sentence says it (the `feature` link, `levels` and ids stay; the TSV note records each).
    ("ref/arc-bard/voice-of-the-wild", "versatile performance"): "All instances of versatile performance",
    ("ref/arc-paladin/holy-guide", "3rd-level mercy"): "Mercy gained at 3rd level",
    ("ref/arc-paladin/holy-guide", "6th-level mercy"): "Mercy gained at 6th level",
    ("ref/arc-ranger/wild-hunter", "Favored enemy"): "All instances of the favored enemy class ability",
    ("ref/arc-shaman/animist", "2nd-level hex"): "Hex gained at 2nd level",
    ("ref/arc-witch/hex-channeler", "2nd-level hex"): "Hex gained at 2nd level",
    ("ref/arc-witch/mountain-witch", "2nd-level hex"): "Hex gained at 2nd level",
    ("ref/arc-witch/dreamweaver", "2nd-level hex"): "Witch's hex gained at 2nd level",
    ("ref/arc-alchemist/plague-bringer", "Poison resistance"): "All increments of poison resistance",
    ("ref/arc-bard/shadow-puppeteer", "Inspire courage"): "All levels of inspire courage",
    ("ref/arc-ranger/wild-shadow", "Woodland stride"): "Ranger's woodland stride class feature gained at 7th level",
    ("ref/arc-rogue/swordmaster", "Trap sense"): "All increments of trap sense",
    ("ref/arc-bard/voice-of-the-wild", "Inspire competence"): "All increments of inspire competence",
    ("ref/arc-witch/dreamweaver", "6th-level hex"): "Witch's hex gained at 6th level",
    ("ref/arc-witch/dreamweaver", "10th-level hex"): "Witch's hex gained at 10th level",
    # Owner ruling 31 of 2026-11-25: the holds of the renamed shape convert in the same PR; the stored name is the printed wording.
    ("ref/arc-barbarian/feral-gnasher", "2nd-level rage power"): "Rage power gained at second level",
    # Final review of batch 3 (ruling 22): the printed words of the sentence, as stored by the owner's rule
    ("ref/arc-swashbuckler/guiding-blade", "Kip-up"): "Kip-up deed",
    ("ref/arc-paladin/gray-paladin", "Code of conduct and associated abilities"): "Paladin's code of conduct and associated abilities",
    ("ref/arc-paladin/gray-paladin", "Ex-paladin"): "Section on ex-paladins",
    ("ref/arc-barbarian/hateful-rager", "2nd, 8th, 14th, and 20th level rage powers"): "Barbarian's rage power gained at 2nd level",
    ("ref/arc-rogue/deadly-courtesan", "Rogue talent gained at 2nd level"): "Rogue trick gained at 2nd level",
    ("ref/arc-paladin/stonelord", "3rd-, 9th-, and 15th-level mercies"): "Her mercies gained at 3rd, 9th, and 15th level",
    ("ref/arc-ranger/wave-warden", "All combat style bonus feats"):
        "Standard ranger's combat style bonus feats, including the limitations on armor worn",
    ("ref/arc-magus/spell-dancer", "5th-level bonus feat"): "Bonus feat a magus receives at 5th level",
    ("ref/arc-swashbuckler/mysterious-avenger", "4th-level bonus feat"): "Bonus feat gained at 4th level",
    ("ref/arc-wizard/wind-listener", "5th-level bonus feat"): "Bonus feat gained at 5th level",
    ("ref/arc-wizard/wind-listener", "10th-level bonus feat"): "Bonus feat gained at 10th level",
    ("ref/arc-wizard/wind-listener", "15th-level bonus feat"): "Bonus feat gained at 15th level",
    ("ref/arc-sorcerer/wishcrafter", "All bloodline spells"): "Bloodline spells gained by the sorcerer's bloodline",
    ("ref/arc-sorcerer/wishcrafter", "7th-level bloodline feat"): "Bloodline bonus feat gained at 7th level",
    ("ref/arc-sorcerer/wishcrafter", "13th-level bloodline feat"): "Bloodline bonus feat gained at 13th level",
    ("ref/arc-sorcerer/wishcrafter", "19th-level bloodline feat"): "Bloodline bonus feat gained at 19th level",
    ("ref/arc-sorcerer/eldritch-scrapper", "Bloodline powers gained at 1st, 9th, and 15th level"):
        "Sorcerer's bloodline powers gained 1st, 9th, and 15th levels",
    ("ref/arc-wizard/spirit-whisperer", "Spellbook"): "Spellbooks class feature",
    ("ref/arc-wizard/spirit-whisperer", "20th-level bonus feat"): "Bonus feat gained at 20th level",
    ("ref/arc-wizard/spirit-whisperer", "5th-, 10th-, and 15th-level bonus feats"): "Bonus feats",
    ("ref/arc-oracle/spirit-guide", "Bonus skills from the oracle's mystery"): "Bonus class skills gained from the oracle's mystery",
    ("ref/arc-oracle/ancient-lorekeeper", "Bonus skills from the oracle's mystery"): "Bonus skills the ancient lorekeeper gains from her mystery",
    ("ref/arc-oracle/community-guardian", "Bonus skills from the oracle's mystery"): "Additional class skills from her mystery",
    ("ref/arc-monk/ironskin-monk", "and Spring Attack on the monk's bonus feat list"): "Spring Attack on his bonus feat list",
    ("ref/arc-summoner/blood-god-disciple", "Summon monster I"): "Summon monster I, III, V, VII, and IX spell-like abilities",
    ("ref/arc-summoner/blood-god-disciple", "Summon monster II"): "Summon monster II spell-like ability",
    ("ref/arc-summoner/blood-god-disciple", "Summon monster IV"): "Summon monster IV spell-like ability",
    ("ref/arc-rogue/deadly-courtesan", "Trap sense"): "All levels of trap sense",
    # Owner ruling 22 (reader of #710 reads "These bonus spells replace ..."): the level back-references of batch 2
    ("ref/arc-oracle/psychic-searcher", "The bonus spells gained at 4th, 6th, 8th, 12th, 16th, and 18th levels from the oracle's mystery"):
        "Mystery bonus spells at these levels",
    ("ref/arc-oracle/community-guardian", "The bonus spells gained at 2nd, 4th, 6th, 10th, and 12th levels from the oracle's mystery"):
        "Mystery bonus spells from these levels",
    ("ref/arc-oracle/reincarnated-oracle", "The bonus spells gained at 2nd, 4th, 10th, 16th, and 18th levels from the oracle's mystery"):
        "Mystery bonus spells at these levels",
    ("ref/arc-oracle/shigenjo", "The bonus spells gained at 2nd, 4th, 8th, 12th, 14th, and 16th levels from the oracle's mystery"):
        "Mystery bonus spells at these levels",
    ("ref/arc-oracle/ancient-lorekeeper", "Bonus spells gained from the oracle's mystery"):
        "Bonus spells she would normally gain at these levels from her chosen mystery",
    ("ref/arc-oracle/shigenjo", "Final revelation"): "Final revelation of the shigenjo's mystery",
    ("ref/arc-druid/urban-druid", "Spontaneous casting"): "Ability to spontaneously cast summon nature's ally spells",
    ("ref/arc-ranger/skirmisher", "Spellcasting ability"): "Spells",
    ("ref/arc-monk/monk-of-the-empty-hand", "Weapon proficiencies"): "Normal monk weapon proficiencies",
    ("ref/arc-alchemist/psychonaut", "15th-level bomb damage increase"): "Increase to bomb damage at this level",
    ("ref/arc-alchemist/psychonaut", "17th-level bomb damage increase"): "Increase to bomb damage at this level",
    ("ref/arc-oracle/dual-cursed-oracle", "The bonus spells gained at 2nd, 4th, and 6th levels from the oracle's mystery"): "Mystery bonus spells at these levels",
    ("ref/arc-oracle/enlightened-philosopher", "All bonus spells gained from the oracle's mystery after 2nd level"): "Mystery bonus spells at these levels",
    ("ref/arc-oracle/planar-oracle", "All bonus spells from the oracle's mystery"): "Mystery bonus spells at these levels",
    ("ref/arc-oracle/possessed-oracle", "The bonus spells gained at 1st, 4th, 6th, 8th, 10th, 12th, and 16th levels from the oracle's mystery"): "Mystery bonus spells at these levels",
    ("ref/arc-oracle/seer", "Bonus spells granted by the oracle's mystery after 2nd level"): "Mystery bonus spells at these levels",
    ("ref/arc-oracle/stargazer", "The bonus spells gained at 2nd, 4th, 6th, 8th, and 18th levels from the oracle's mystery"): "Mystery bonus spells at these levels",
    ("ref/arc-oracle/enlightened-philosopher", "Final revelation"): "Final revelation of the oracle's mystery",
    ("ref/arc-oracle/planar-oracle", "Final revelation"): "Final revelation of the oracle's mystery",
    ("ref/arc-oracle/enlightened-philosopher", "Bonus skills from the oracle's mystery"): "Additional class skills from her mystery",
    ("ref/arc-oracle/stargazer", "Bonus skills from the oracle's mystery"): "Additional class skills from her mystery",
    ("ref/arc-inquisitor/sin-eater", "Teamwork feat gained at 6th level"): "Bonus teamwork feat gained at 6th level",
    ("ref/arc-inquisitor/spellbreaker", "Teamwork feats"): "Bonus teamwork feats",
    ("ref/arc-ranger/trapper", "Spellcasting ability"): "Spells",
    ("ref/arc-gunslinger/gun-tank", "All bonus combat/grit feats"): "Bonus feats the gunslinger gains at 4th level and every four levels thereafter",
    ("ref/arc-gunslinger/musket-master", "Firearm training 1, 2, 3, and 4"): "Gun training 1, 2, 3, and 4",
    ("ref/arc-magus/myrmidarch", "10th-level fighter training"): "Fighter training the magus gains at 10th level",
    ("ref/arc-monk/sensei", "Bonus feats gained at 6th, 10th, and 14th level"): "Bonus feats at 6th, 10th, and 14th level",
    ("ref/arc-ranger/falconer", "6th-level combat style feat"): "Combat style feat the ranger gains at 6th level",
    ("ref/arc-cavalier/gendarme", "cavalier bonus feats"): "Selection of bonus feats",
    ("ref/arc-kineticist/elemental-annihilator", "Omnikinesis, 20th-level utility wild talent"): "Omnikinesis and the 20th-level utility wild talent",
    ("ref/arc-monk/karmic-monk", "The slow fall improvement; it remains at 70 feet"): "Slow fall 80 feet",
    ("ref/arc-monk/karmic-monk", "Slow fall"): "Slow fall at 19th level to become slow fall 80 feet",
    ("ref/arc-witch/ley-line-guardian", "1st- and 8th-level hexes"): "Hexes gained at 1st and 8th levels",
    ("ref/arc-investigator/hallucinist", "3rd-level trap sense boost"): "Trap sense gained at 3rd level",
    ("ref/arc-mesmerist/vox", "10th-level mesmerist trick"): "Mesmerist trick normally gained at 10th level",
    ("ref/arc-occultist/tome-eater", "6th-level implement"): "Implement gained at 6th level",
    ("ref/arc-antipaladin/tyrant", "ex-antipaladins"): "Section on ex-antipaladins",
    ("ref/arc-rogue/consigliere", "Trap sense"): "All instances of trap sense",
    ("ref/arc-skald/bold-schemer", "Bardic knowledge"): "Class skills and bardic knowledge",
    ("ref/arc-swashbuckler/noble-fencer", "Dodging panache"): "Dodging panache deed",
    ("ref/arc-swashbuckler/veiled-blade", "Opportune parry and riposte"): "Opportune parry and riposte deed",
    ("ref/arc-unchained-summoner/fey-caller", "Summon monster"): "Summon monster spell-like ability",
    ("ref/arc-kineticist/overwhelming-soul", "Key ability score of wild talents"): "Class skills and the key ability score of wild talents",
    ("ref/arc-kineticist/elemental-annihilator", "6th-, 12th-, and 16th level utility wild talents"): "6th-, 12th-, and 16th-level utility wild talents",
    ("ref/arc-swashbuckler/noble-fencer", "Superior feint"): "Superior feint deed",
    ("ref/arc-swashbuckler/veiled-blade", "Menacing swordplay"): "Menacing swordplay deed",
    ("ref/arc-swashbuckler/veiled-blade", "Swashbuckler's edge"): "Swashbuckler's edge deed",
    ("ref/arc-swashbuckler/veiled-blade", "Swashbuckler's grace"): "Swashbuckler's grace deed",
    ("ref/arc-swashbuckler/noble-fencer", "Subtle blade"): "Subtle blade deed",
    ("ref/arc-rogue/phantom-thief", "Rogue's edge (unchained rogue only)"): "Rogue's edge",
    ("ref/arc-paladin/divine-hunter", "Aura of righteousness"): "Aura of faith",
    ("ref/arc-monk/qinggong-monk", "The monk class abilities the qinggong monk gives up for a ki power"):
        "The monk class ability the qinggong monk gives up for this ki power",
    ("ref/arc-alchemist/reanimator", "7th-level bomb damage increase"): "Increase to bomb damage at this level",
    ("ref/arc-alchemist/reanimator", "13th-level bomb damage increase"): "Increase to bomb damage at this level",
    ("ref/arc-alchemist/reanimator", "15th-level bomb damage increase"): "Increase to bomb damage at this level",
    # Batch 4 (Ultimate Wilderness, Adventurer's Guide), owner ruling 22: the stored name is the printed wording (the TSV note records each)
    ('ref/arc-alchemist/ice-chemist', '2nd-level discovery'): 'Discovery that the alchemist normally gains at 2nd level',
    ('ref/arc-antipaladin/blighted-myrmidon', '10th-level use of smite good'): 'Use of smite good gained at 10th level',
    ('ref/arc-barbarian/brutish-swamper', '6th-level rage power'): 'Rage power normally gained at 6th level',
    ('ref/arc-barbarian/pack-hunter', '6th-level rage power'): 'Rage power normally gained at 6th level',
    ('ref/arc-barbarian/sharptooth', '6th- and 12th-level rage powers'): 'Rage powers normally gained at 6th and 12th levels',
    ('ref/arc-monk/water-dancer', 'Bonus feat gained at 1st level'): 'Bonus feat the monk normally gains at 1st level',
    ('ref/arc-occultist/geomancer', '7th-level focus power'): 'Focus power gained at 7th level',
    ('ref/arc-occultist/geomancer', '13th-level focus power'): 'Focus power gained at 13th level',
    ('ref/arc-occultist/occult-historian', '3rd-level focus power'): 'Focus power gained at 3rd level',
    ('ref/arc-paladin/hunting-paladin', '1st-level use of smite evil'): 'Use of smite evil gained at 1st level',
    ('ref/arc-witch/herb-witch', '1st- and 10th-level hexes'): 'Hexes gained at 1st and 10th levels',
    ('ref/arc-fighter/aldori-defender', '6th level fighter bonus feat'): 'Bonus feat the fighter would normally gain at 6th level',
    ('ref/arc-fighter/aldori-defender', '8th level fighter bonus feat'): 'Bonus feat the fighter would normally gain at 8th level',
    ('ref/arc-fighter/aldori-defender', '10th level fighter bonus feat'): 'Bonus feat the fighter would normally gain at 10th level',
    ('ref/arc-monk/brazen-disciple', 'Bonus feats gained at 1st level and at 6th level'): "Monk's bonus feats at 1st level and at 6th level",
    ('ref/arc-occultist/curator', '3rd-level focus power'): 'Focus power gained at 3rd level',
    ('ref/arc-ranger/lantern-lighter', '8th-level favored terrain'): 'Favored terrain gained at 8th level',
    ('ref/arc-oracle/elementalist-oracle', "The bonus spells gained at 4th, 6th, 8th, 10th, 12th and 18th levels from the oracle's mystery"): "The oracle's mystery bonus spells at these levels",
    ('ref/arc-oracle/river-soul', "The bonus spells gained at 2nd, 6th, 8th, 10th, and 18th levels from the oracle's mystery"): "The oracle's mystery bonus spells at these levels",
    ('ref/arc-oracle/tree-soul', "The bonus spells gained at 2nd, 10th, 12th, 14th, 16th, and 18th levels from the oracle's mystery"): "The oracle's mystery bonus spells at these levels",
    ('ref/arc-oracle/river-soul', "Bonus skills from the oracle's mystery"): "The class skills granted by the oracle's mystery",
    ('ref/arc-oracle/tree-soul', "Bonus skills from the oracle's mystery"): "The class skills granted by the oracle's mystery",
    ('ref/arc-shifter/oozemorph', 'Chimeric aspect'): 'Chimeric form',
    ('ref/arc-shifter/oozemorph', 'greater chimeric aspect'): 'Greater chimeric form',
    ('ref/arc-swashbuckler/arrow-champion', 'Swashbuckler initiative'): "Swashbuckler's initiative",
    ('ref/arc-occultist/curator', '6th- and 14th-level implements'): 'Implements learned at 6th level and 14th level',
    ('ref/arc-druid/tempest-druid', 'Spontaneous casting'): "The druid's normal ability to spontaneously cast summon spells",
    ('ref/arc-gunslinger/commando', 'Utility shot deed'): 'Utility shot',
    ('ref/arc-gunslinger/commando', 'Expert loading deed'): 'Expert loading',
    ('ref/arc-gunslinger/commando', 'Lightning reload deed'): 'Lightning reload',
    ('ref/arc-gunslinger/commando', "Slinger's luck deed"): "Slinger's luck",
    ('ref/arc-paladin/wilderness-warden', '3rd-, 9th-, and 15th-level mercies'): 'Mercies gained at 3rd level, 9th level, and 15th level',
    ('ref/arc-monk/water-dancer', 'Bonus feats gained at 2nd, 6th, 10th, 14th, and 18th levels'): 'Bonus feats at 2nd, 6th, 10th, 14th, and 18th levels',
    ('ref/arc-barbarian/geminate-invoker', '4th, 8th, and 12th level rage powers'): 'Rage powers gained at 4th, 8th, and 12th levels',
    ('ref/arc-alchemist/horticulturist', '2nd-level discovery'): 'Discovery normally gained at 2nd level',
    ('ref/arc-druid/green-faith-initiate', 'Daily use of wild shape gained at 6th level'): "The druid's additional daily use of wild shape gained at 6th level",
    ('ref/arc-druid/green-faith-initiate', 'Daily use of wild shape gained at 10th level'): "The druid's additional daily use of wild shape gained at 10th level",
    ('ref/arc-fighter/skirmisher', "The fighter's armor proficiency"): "The fighter's weapon and armor proficiency",
    ('ref/arc-oracle/tree-soul', "The class skills granted by the oracle's mystery"): "The class skills granted by the oracle's mystery and class skills",
    ('ref/arc-shifter/fiendflesh-shifter', 'shifter aspect'): 'Shifter aspect, and all improvements to shifter aspect',
    ('ref/arc-shifter/rageshaper', 'shifter aspect'): 'Shifter aspect, and all improvements to shifter aspect',
    ('ref/arc-shifter/oozemorph', 'shifter aspect'): 'Shifter aspect, and all improvements of shifter aspect',
    ('ref/arc-shifter/verdant-shifter', 'Shifter aspect'): 'Shifter aspect and all improvements of shifter aspect',
    ('ref/arc-shifter/weretouched', 'Shifter aspect'): 'Shifter aspect and all of its improvements',
    ('ref/arc-witch/herb-witch', 'Patron'): "The witch's patron spells",
    ('ref/arc-witch/season-witch', '1st-level hex'): 'Hex gained at 1st level',
    ('ref/arc-bard/brazen-deceiver', 'distraction'): 'Distraction bardic performances',
    ('ref/arc-swashbuckler/dashing-thief', "swashbuckler's edge"): "Swashbuckler's edge deeds",
    ('ref/arc-bloodrager/enlightened-bloodrager', '1st-level bloodline power'): 'Bloodline power the bloodrager normally gains at 1st level',
    ('ref/arc-bloodrager/enlightened-bloodrager', 'bloodline bonus spells'): 'All bonus spells gained as part of a bloodline',
    ('ref/arc-swashbuckler/dashing-thief', 'Regain panache from a killing blow'): "The swashbuckler's ability to regain panache from a killing blow",
    ('ref/arc-swashbuckler/dashing-thief', 'Menacing swordplay'): 'Menacing swordplay deed',
    ('ref/arc-swashbuckler/dashing-thief', 'Dizzying defense'): 'Dizzying defense deed',
    # Batch 5 (Horror Adventures, Planar Adventures), owner ruling 22: the stored name is the printed wording (the TSV note records each)
    ('ref/arc-alchemist/mad-scientist', '2nd-level discovery'): 'Discovery gained at 2nd level',
    ('ref/arc-alchemist/energist', '2nd-level discovery'): 'Discovery gained at 2nd level',
    ('ref/arc-cleric/elder-mythos-cultist', 'Alignment'): "The cleric's required alignment",
    ('ref/arc-swashbuckler/azatariel', 'Menacing swordplay'): 'Menacing swordplay deed',
    ('ref/arc-occultist/talisman-crafter', '5th- and 17th-level focus powers'): 'Focus powers normally gained at 5th and 17th levels',
    ('ref/arc-spiritualist/exciter', 'ability to use emotional focus abilities that require a manifested phantom'): 'Use emotional focus abilities that require a manifested phantom',
    ('ref/arc-alchemist/mad-scientist', '4th-level discovery'): 'Discovery gained at 4th level',
    ('ref/arc-alchemist/mad-scientist', 'Mutagen'): "The alchemist's mutagen",
    ('ref/arc-witch/gingerbread-witch', '4th-level hex'): 'Hex gained at 4th level',
    ('ref/arc-swashbuckler/azatariel', 'Precise strike'): 'Precise strike deed',
    ('ref/arc-witch/gingerbread-witch', '1st- and 10th-level hexes'): 'Hexes gained at 1st and 10th levels',
    ('ref/arc-wizard/hallowed-necromancer', 'Grave touch necromancy school ability'): 'Grave touch',
    ('ref/arc-wizard/hallowed-necromancer', '5th-level bonus feat'): 'Bonus feat gained at 5th level',
    ('ref/arc-wizard/hallowed-necromancer', '10th-level bonus feat'): 'Bonus feat gained at 10th level',
    ('ref/arc-wizard/hallowed-necromancer', 'Power over undead necromancy school ability'): 'Power over undead',
    ('ref/arc-wizard/undead-master', '5th-, 10th-, and 15th-level bonus feats'): 'Bonus feats gained at 5th, 10th, and 15th levels',
    ('ref/arc-wizard/undead-master', '20th-level bonus feat'): 'Bonus feat gained at 20th level',
    ('ref/arc-wizard/worldseeker', '5th-level bonus feat'): 'Bonus feat gained at 5th level',
    ('ref/arc-wizard/worldseeker', '15th-level bonus feat'): 'Bonus feat gained at 15th level',
    ('ref/arc-witch/gingerbread-witch', '8th-level hex'): 'Hex gained at 8th level',
    ('ref/arc-witch/gingerbread-witch', '12th-level hex'): 'Hex gained at 12th level',
    ('ref/arc-witch/gingerbread-witch', '16th-level hex'): 'Hex gained at 16th level',
    ('ref/arc-swashbuckler/azatariel', 'Targeted strike'): 'Targeted strike deed',
    ('ref/arc-swashbuckler/azatariel', 'Bleeding wound'): 'Bleeding wound deed',
    ('ref/arc-swashbuckler/azatariel', 'Bonus feats'): "The swashbuckler's bonus feats",
    ('ref/arc-fighter/skirmisher', '2nd level fighter bonus feat'): 'Bonus feat the fighter normally receives at 2nd level',
    # Blood of the Ancients (ruling 22: the stored name is the printed wording)
    ("ref/arc-investigator/antiquarian", "Alchemy (including Extracts)"): "Alchemy",
    ("ref/arc-wizard/arcane-warden", "5th-, 10th-, 15th-, and 20th-level bonus feats"): "The bonus feats gained at 5th, 10th, 15th, and 20th levels",
    ('ref/arc-witch/tatterdemalion', '4th-, 8th-, 12th-, and 16th-level hexes'): 'Hexes gained at 4th, 8th, 12th, and 16th levels',
    # The app's check of the printed trade sentences (phynics/cast-iron#728): the stored name is the printed words (ruling 22)
    ('ref/arc-paladin/soul-sentinel', '6th-level mercy'): 'Mercy gained at 6th level',
    ('ref/arc-paladin/soul-sentinel', '12th-level mercy'): 'Mercy gained at 12th level',
    ('ref/arc-witch/flood-walker', '1st-level hex'): 'Hex gained at 1st level',
    ('ref/arc-witch/flood-walker', '6th-level hex'): 'Hex gained at 6th level',
    ('ref/arc-witch/flood-walker', '10th-level hex'): 'Hex gained at 10th level',
    ('ref/arc-witch/gravewalker', '4th-level hex'): "Witch's hex gained at 4th level",
    ('ref/arc-witch/gravewalker', '8th-level hex'): "Witch's hex gained at 8th level",
    ('ref/arc-witch/hedge-witch', '4th-level hex'): "Witch's hex gained at 4th level",
    ('ref/arc-witch/hedge-witch', '8th-level hex'): "Witch's hex gained at 8th level",
    ('ref/arc-witch/pact-witch', '6th-level hex'): 'Hex normally gained at 6th level',
    ('ref/arc-witch/tatterdemalion', '1st-level hex'): 'Hex gained at 1st level',
}


# A stored trade that gets the link and the levels of the errata'd text (Wild Child p. 89: the third trade now names
# the bonus combat feats at 5th, 11th and 17th level, which the corrected Wild Tricks replaces).
TRADE_LINKS = {
    # Possessed Oracle (Ultimate Magic p. 59): the bonus-spell trade names the mystery's bonus spells at the printed levels
    ("ref/arc-oracle/possessed-oracle", "Mystery bonus spells at these levels"): ("mystery", [1, 4, 6, 8, 10, 12, 16], "bonus spells"),
    ("ref/arc-brawler/wild-child", "Bonus combat feats gained at 5th, 11th, and 17th levels"): ("bonus-combat-feats", [5, 11, 17]),
}

# The levels of a stored trade that follow the errata (the entry, the name as renamed, the levels).
TRADE_LEVELS = {
    ("ref/arc-oracle/planar-oracle", "Mystery bonus spells at these levels"): [2, 4, 6, 8, 10, 12, 14, 16, 18],         # UM p. 59
    ("ref/arc-oracle/ancient-lorekeeper", "Bonus spells she would normally gain at these levels from her chosen mystery"):
        [4, 6, 8, 10, 12, 14, 16, 18],                                                                                   # ARG p. 24
    ("ref/arc-summoner/blood-god-disciple", "Summon monster I, III, V, VII, and IX spell-like abilities"): [1, 5, 9, 13, 17, 19],
    ("ref/arc-brawler/wild-child", "Bonus combat feats gained at 2nd, 8th, 14th, and 20th levels"): [2, 8, 14, 20],
}


# A stored trade whose op print contradicts (data fix; the TSV note records it): the entry, the printed name,
# the op that print says. Reanimator (Ultimate Magic p. 20): "functions as and replaces the standard alchemist
# bomb class feature", stored as `alters`.
TRADE_OP_FIXES = {
    ("ref/arc-bard/lotus-geisha", "Weapon proficiencies"): "replaces",     # print: "This replaces the normal bard weapon proficiencies." (Dragon Empires Primer p. 22)
    ("ref/arc-witch/gravewalker", "Patron spells"): "replaces",     # print: "This replaces the patron spells."
    ("ref/arc-druid/rot-warden", "Wild shape"): "alters",       # Opus review of batch 4: "This alters wild shape."
    ("ref/arc-alchemist/reanimator", "Bombs"): "replaces",
    ("ref/arc-inquisitor/infiltrator", "Stern gaze"): "replaces",
    ("ref/arc-bard/geisha", "Armor and weapon proficiencies"): "replaces",
    ("ref/arc-bard/dervish-dancer", "Bardic performance"): "replaces",
    ("ref/arc-alchemist/deep-bomber", "Swift alchemy"): "replaces",     # ruling 29: "This ability replaces swift alchemy (...)"
    ("ref/arc-cavalier/gendarme", "cavalier bonus feats"): "alters",
    ("ref/arc-fighter/gladiator", "Proficiency with heavy armor"): "alters",         # owner ruling 23: proficiency changes are `alters`
    ("ref/arc-fighter/gladiator", "tower shields"): "alters",
    ("ref/arc-kineticist/elemental-annihilator", "1st-level infusion"): "replaces",
    ("ref/arc-kineticist/elemental-annihilator", "the basic utility wild talent normally granted by selecting an element"): "replaces",
    ("ref/arc-investigator/cipher", "the investigator talent gained at 5th level"): "replaces",
    ("ref/arc-investigator/majordomo", "Alchemy"): "replaces",
    ("ref/arc-investigator/majordomo", "swift alchemy"): "replaces",
    ("ref/arc-skald/battle-scion", "Bardic knowledge"): "alters",
    ("ref/arc-skald/battle-scion", "Rage power"): "alters",
    ("ref/arc-kineticist/ioun-kineticist", "Basic telekinesis utility wild talent granted by the aether element"): "replaces",   # Blood of the Ancients p. 12: "This replaces the basic telekinesis utility wild talent ..."
}


# A trade that print states in a trade sentence and that the entry does not store (data fix inside the
# pilot's book; the TSV note records it). The other four shaman archetypes store `Venom immunity`.
TRADE_ADDITIONS = {
    "ref/arc-kineticist/kinetic-knight": [{"alters": "Class skills"}],     # "This ability alters the kineticist's class skills." (Courtly)
    "ref/arc-shifter/feyform-shifter": [{"alters": "Shifter aspect", "feature": "shifter-aspect"}],     # owner ruling 49
    "ref/arc-druid/nature-priest": [{"alters": "Class skills"}],     # "This alters the druid's class skills." (Faithful)
    "ref/arc-kineticist/elysiokineticist": [{"alters": "The class skills granted by the wood element"}],     # "This alters elemental focus and the class skills granted by the wood element, and it replaces expanded element."
    # "This ability replaces the ki power gained at 4th level for an unchained monk." (Healing Ki, Greater Hone Body, Hone Soul)
    "ref/arc-monk/disciple-of-wholeness": [{"replaces": "The ki power gained at 4th level for an unchained monk", "levels": [4]},
                                           {"replaces": "The ki power gained at 12th level for an unchained monk", "levels": [12]},
                                           {"replaces": "The ki power gained at 14th level for an unchained monk", "levels": [14]}],
    # Batches 6 to 9 (Player Companions): a printed sentence that no stored trade states
    # Printed sentences that name a base-class feature the import stored no trade for (ruling 31)
    "ref/arc-summoner/shadow-caller": [{"replaces": "Summon monster spell-like abilities", "feature": "summon-monster-i"}],
    "ref/arc-summoner/wild-caller-arg": [{"alters": "Eidolon", "feature": "eidolon"}],
    "ref/arc-druid/eagle-shaman": [{"replaces": "Venom immunity", "feature": "venom-immunity"}],
    "ref/arc-bard/silver-balladeer": [{"alters": "Alignment"}],
    "ref/arc-rogue/phantom-thief": [{"alters": "Class skills"}],
    # Batch 4: the sentence "alters the ... class skills and ..." names class skills; the import stored no trade for them
    "ref/arc-swashbuckler/dashing-thief": [{"alters": "Class skills"}],
    "ref/arc-swashbuckler/rostland-bravo": [{"alters": "Class skills"}],
    "ref/arc-magus/magic-warrior": [{"alters": "Class skills"}],
    "ref/arc-kineticist/dark-elementalist": [{"alters": "Class skills"}],
    "ref/arc-fighter/gloomblade": [{"alters": "Class skills"}],
    # Opus review of batch 4: a printed "This alters/replaces ..." sentence that no stored trade states (the check `printed_trade_gaps`)
    "ref/arc-fighter/savage-warrior": [{"replaces": "The normal attack roll bonus and AC penalty for charging"}],
    "ref/arc-paladin/scion-of-talmandor": [{"alters": "Class skills"}],
    "ref/arc-alchemist/alchemical-sapper": [{"alters": "Class skills"}],
    "ref/arc-antipaladin/tyrant": [{"alters": "Class skills"}],
    "ref/arc-cavalier/hussar": [{"alters": "Class skills"}],
    "ref/arc-hunter/roof-runner": [{"alters": "Class skills"}, {"replaces": "The hunter's proficiency with medium armor and shields"}],
    "ref/arc-druid/dinosaur-druid": [{"alters": "Spontaneous casting", "feature": "spontaneous-casting"}],
    "ref/arc-summoner/leshy-caller": [{"alters": "Eidolon", "feature": "eidolon"}],
    "ref/arc-unchained-summoner/leshy-caller": [{"alters": "Eidolon", "feature": "eidolon"}],
    # Blood of the Ancients: "This replaces poison resistance and poison immunity." (Antiquarian, Curse Resistance)
    "ref/arc-investigator/antiquarian": [{"replaces": "Poison resistance and poison immunity", "feature": "poison-resistance"}],
    "ref/arc-wizard/arcane-warden": [{"alters": "Class skills"}],       # "This alters the wizard's class skills." (Universal Magic)
    # Opus review of the pilot (the check of #329 reads the sections before the first listed feature): "This alters the ... class skills"
    "ref/arc-warpriest/jistkan-magistrate": [{"alters": "Class skills"}],
    "ref/arc-mesmerist/chart-caster": [{"alters": "Class skills"}],
    "ref/arc-fighter/aerial-assaulter": [{"alters": "Skills"}],     # print: "This alters the fighter's skills." (Class Skills section)
}


# Batch 5 (Opus review of #329): the sentences "This alters the ...'s class skills" and the like that print sets in a section before the first
# feature (Class Skills, Alignment) state a trade that the import did not store; each is stored without `by` (ruling 6, as for Magic Warrior).
SCAFFOLD_TRADE_ADDITIONS = {
    # Psychic Anthology, Disciple's Doctrine, Occult Origins, Arcane Anthology, Blood of the Coven: a sentence of a section before the first feature
    "ref/arc-samurai/ward-speaker": [{"alters": "Alignment"}],
    "ref/arc-warpriest/fist-of-the-godclaw": [{"alters": "Alignment restriction"}],
    "ref/arc-monk/serpent-fire-adept": [{"alters": "Class skills"}],
    "ref/arc-shaman/true-silvered-throne": [{"alters": "Class skills"}],
    # Batches 6 to 9 (Player Companions): "This alters the ...'s class skills." in the Class Skills section before the first feature
    "ref/arc-bard/solacer": [{"alters": "Class skills"}],
    "ref/arc-cavalier/hooded-knight": [{"alters": "Class skills"}],
    "ref/arc-brawler/constructed-pugilist": [{"alters": "Class skills"}],
    "ref/arc-kineticist/cinderlands-adept": [{"alters": "Class skills"}],
    "ref/arc-ninja/petal-ninja": [{"alters": "Class skills"}],
    "ref/arc-paladin/champion-of-the-cascade": [{"alters": "Class skills"}],
    "ref/arc-swashbuckler/daring-infiltrator": [{"alters": "The swashbuckler's class skill list"}],
    "ref/arc-swashbuckler/mysterious-avenger": [{"alters": "Class skills"}],
    "ref/arc-warpriest/cult-leader": [{"replaces": "Class skills"}],
    "ref/arc-warpriest/sacred-fist": [{"replaces": "Class skills"}],
    "ref/arc-ranger/beast-master": [{"replaces": "Class skills"}],
    "ref/arc-arcanist/magaambyan-initiate": [{"alters": "Alignment"}],
    "ref/arc-druid/sunrider": [{"alters": "Class skills"}],
    "ref/arc-druid/tempest-druid": [{"alters": "Alignment"}],
    "ref/arc-monk/brazen-disciple": [{"alters": "Class skills"}],
    "ref/arc-ranger/raven-master": [{"alters": "Class skills"}],
    "ref/arc-shaman/name-keeper": [{"alters": "Class skills"}],
    "ref/arc-slayer/witch-killer": [{"alters": "Class skills"}],
    "ref/arc-vigilante/experimenter": [{"alters": "Class skills"}],
    "ref/arc-alchemist/ectochymist": [{"alters": "Class skills"}],
    "ref/arc-fighter/sensate": [{"replaces": "Class skills"}],
    "ref/arc-investigator/psychic-detective": [{"alters": "Class skills"}],
    "ref/arc-mesmerist/vexing-daredevil": [{"alters": "Class skills"}],
    "ref/arc-monk/karmic-monk": [{"alters": "Class skills"}],
    "ref/arc-occultist/battle-host": [{"alters": "Class skills"}],
    "ref/arc-ranger/planar-scout": [{"alters": "The ranger's skills"}],
    "ref/arc-rogue/dreamthief": [{"alters": "Class skills"}],
    "ref/arc-alchemist/interrogator": [{"alters": "Class skills"}],
    "ref/arc-alchemist/metamorph": [{"alters": "Class skills"}],
    "ref/arc-druid/skinshaper": [{"alters": "Class skills"}],
    "ref/arc-hunter/courtly-hunter": [{"alters": "Class skills"}],
    "ref/arc-inquisitor/cloaked-wolf": [{"alters": "Class skills"}],
    "ref/arc-inquisitor/umbral-stalker": [{"alters": "Class skills"}],
    "ref/arc-mesmerist/fey-trickster": [{"alters": "Class skills"}],
    "ref/arc-monk/sage-counselor": [{"alters": "Class skills"}],
    "ref/arc-occultist/ancestral-aspirant": [{"alters": "Class skills"}],
    "ref/arc-occultist/secret-broker": [{"alters": "Class skills"}],
    "ref/arc-paladin/gray-paladin": [{"alters": "Class skills"}],
    "ref/arc-ranger/code-runner": [{"alters": "Class skills"}],
    "ref/arc-ranger/dandy": [{"alters": "Class skills"}],
    "ref/arc-ranger/guildbreaker": [{"alters": "Class skills"}],
    "ref/arc-rogue/consigliere": [{"alters": "Class skills"}],
    "ref/arc-slayer/velvet-blade": [{"alters": "Class skills"}],
    "ref/arc-swashbuckler/veiled-blade": [{"alters": "Class skills"}],
    "ref/arc-unchained-summoner/fey-caller": [{"alters": "Class skills"}],
    "ref/arc-vigilante/cabalist": [{"alters": "Class skills"}],
    "ref/arc-vigilante/magical-child": [{"alters": "Class skills"}],
    "ref/arc-vigilante/mounted-fury": [{"alters": "Class skills"}],
    "ref/arc-vigilante/psychometrist": [{"alters": "Class skills"}],
    "ref/arc-vigilante/warlock": [{"alters": "Class skills"}],
    "ref/arc-vigilante/zealot": [{"alters": "Class skills"}, {"alters": "Skill ranks per level"}],
    "ref/arc-barbarian/brutish-swamper": [{"alters": "The barbarian's skills"}],
    "ref/arc-barbarian/cave-dweller": [{"alters": "The barbarian's skills"}],
    "ref/arc-bard/cultivator": [{"alters": "Class skills"}],
    "ref/arc-cavalier/saurian-champion": [{"alters": "Class skills"}],
    "ref/arc-gunslinger/commando": [{"alters": "Class skills"}],
    "ref/arc-hunter/chameleon-adept": [{"alters": "Class skills"}],
    "ref/arc-hunter/patient-ambusher": [{"alters": "Class skills"}],
    "ref/arc-investigator/natural-philosopher": [{"alters": "Class skills"}],
    "ref/arc-occultist/geomancer": [{"alters": "Class skills"}],
    "ref/arc-occultist/naturalist": [{"alters": "Class skills"}],
    "ref/arc-oracle/river-soul": [{"alters": "Class skills"}],
    "ref/arc-paladin/forest-preserver": [{"alters": "Class skills"}],
    "ref/arc-paladin/hunting-paladin": [{"alters": "Class skills"}],
    "ref/arc-paladin/wilderness-warden": [{"alters": "Class skills"}],
    "ref/arc-ranger/wilderness-explorer": [{"alters": "Class skills"}],
    "ref/arc-rogue/desert-raider": [{"alters": "Class skills"}],
    "ref/arc-rogue/river-rat": [{"alters": "Class skills"}],
    "ref/arc-rogue/sly-saboteur": [{"alters": "Class skills"}],
    "ref/arc-rogue/sylvan-trickster": [{"alters": "Class skills"}],
    "ref/arc-swashbuckler/wildstrider": [{"alters": "Class skills"}],
    "ref/arc-vigilante/avenging-beast": [{"alters": "Class skills"}],
    "ref/arc-witch/flood-walker": [{"alters": "Class skills"}],
}
for _eid, _adds in SCAFFOLD_TRADE_ADDITIONS.items():
    TRADE_ADDITIONS[_eid] = TRADE_ADDITIONS.get(_eid, []) + [a for a in _adds if a not in TRADE_ADDITIONS.get(_eid, [])]


# A stored trade that only repeats another one (Roughrider stores `Armor training 4` twice, once without
# its feature link): the repeat is left out and the TSV note records it.
TRADE_DROPS = {
    "ref/arc-fighter/roughrider": [("replaces", "Armor training 4")],
    "ref/arc-monk/sage-counselor": [("alters", "Ki pool")],
    "ref/arc-paladin/gray-paladin": [("alters", "Smite evil")],
}


# Stored trades that lose their `feature` link and `levels` (data fix; the TSV note records it): the entry and
# the stored names. Reanimator (Ultimate Magic p. 20): the Bomb feature "functions as and replaces the standard
# alchemist bomb class feature" (the trade `Bombs`, whole feature), and three features each "replace the
# increase to bomb damage at this level". A trade of the whole feature and a trade of one level of it on one
# feature overlap (the check refuses them), so the printed level trade is written once, as the printed name, and
# stays unlinked, the way the check allows; `by` names the three features that print it, whose levels are 7, 13
# and 15. TRADE_UNLINKS lists the stored trade that stays, TRADE_MERGED the two that print states with the
# same words and that the one trade covers.
TRADE_UNLINKS = {
    "ref/arc-alchemist/reanimator": ["7th-level bomb damage increase"],
}
TRADE_MERGED = {
    "ref/arc-alchemist/reanimator": [("replaces", "13th-level bomb damage increase"),
                                     ("replaces", "15th-level bomb damage increase")],
    "ref/arc-alchemist/psychonaut": [("replaces", "17th-level bomb damage increase")],
    # Blood God Disciple (ARG p. 53): one printed sentence, "the summon monster I, III, V, VII, and IX spell-like abilities"
    "ref/arc-summoner/blood-god-disciple": [("replaces", "III"), ("replaces", "V"), ("replaces", "VII"), ("replaces", "and IX")],
    "ref/arc-hunter/packmaster": [("alters", "Teamwork feats")],         # stored twice; the second has no feature link
}


# Features whose first paragraph states the level after a flavor sentence or inside its first sentence (owner review
# of batch 1): the level is the first "At Nth level" of the paragraph. The paragraphs of the other features hold
# progressions ("At 6th level ..., at 9th level ...") that this reading would take for the level of the feature.
LEVEL_ONE_REPLACES = {
    ("ref/arc-paladin/faithful-wanderer", "hidden-aura"),    # replaces aura of good, a 1st-level feature: the printed "At 3rd level, her alignment aura emulates ..." is a step of it (review of #339)
    ("ref/arc-warpriest/divine-commander", "mount"),
    ("ref/arc-gunslinger/black-powder-vaulter", "mobile-reload"),   # replaces the deadeye deed, a 1st-level deed (Martial Arts Handbook p. 10)
    ("ref/arc-gunslinger/black-powder-vaulter", "daring-vault"),    # replaces the gunslinger's dodge deed, a 1st-level deed
    ("ref/arc-wizard/arcane-warden", "generous-touch"),     # replaces the hand of the apprentice universalist school ability, a 1st-level power (rulings 11 and 35)
}

# a lead at the start of a later sentence of the first paragraph, or "of Nth level" in its first sentence
LATER_LEAD = re.compile(r"(?:(?<=[.!?]\s)|(?<=[.!?][\"\u201d]\s))(?:At|Starting at|Beginning at)\s+(\d+)(st|nd|rd|th)\s+level\b", re.I)
UPGRADE_WORDS = re.compile(r"\b(?:increases?|improves?|becomes?|rises?|grows?|decreases?|additional|instead)\b", re.I)
OF_LEVEL = re.compile(r"^[^.]*?\bof\s+(\d+)(st|nd|rd|th)\s+level\b(?!\s+or\s+lower)", re.I)
# A level that the text of the feature does not state but the section before it does (review of #338): "must take the following revelation at 3rd level"
LEVEL_FROM_PRINT = {
    # Psychic Anthology, Disciple's Doctrine, Occult Origins, Arcane Anthology, Blood of the Coven (ruling 50)
    ("ref/arc-bard/arrowsong-minstrel", "diminished-spellcasting"): (1, "ruling 50: alters the bard's spellcasting (one fewer spell of each level per day, the whole feature, a 1st-level class feature)"),
    ("ref/arc-occultist/reliquarian", "spells"): (1, "ruling 50: alters the occultist's spells (the whole spellcasting, divine spells with a divine focus, a 1st-level class feature)"),
    ("ref/arc-warpriest/fist-of-the-godclaw", "blessings-of-the-godclaw"): (1, "ruling 50: alters blessings, a 1st-level class feature (the class table lists blessings (minor))"),
    # ruling 50: altering the whole spellcasting of the class (the Special column of the class table does not list it) or its blessings (the table lists "blessings (minor)")
    ("ref/arc-medium/rivethun-spirit-channeler", "mind-and-soul"): (1, "ruling 50: alters the medium's spellcasting (the whole feature, a 1st-level class feature); print: \"This choice is made at 1st level\""),
    ("ref/arc-wizard/pact-wizard-hhh", "effortless-magic"): (1, "ruling 50: alters the wizard's spellcasting (the whole feature, a 1st-level class feature)"),
    # batches 6 to 9 (review of #339)
    ("ref/arc-rogue/eldritch-scoundrel", "uncanny-training"): (4, "print says \"Beginning at 4th level, she can take uncanny dodge instead of a rogue talent\""),
    ("ref/arc-bard/first-world-minstrel", "gremlin-s-luck"): (8, "print says \"A First World minstrel of 8th level or higher\""),
    ("ref/arc-oracle/hermit", "recluse-s-stride"): (1, "print says \"You must take this revelation at 1st level\""),
    ("ref/arc-cleric/angelfire-apostle", "diminished-spellcasting"): (1, "ruling 50: alters the cleric's spellcasting (one fewer spell slot of each level, the whole feature, a 1st-level class feature)"),
    # owner ruling 50 (review of #338): altering the whole spellcasting of the class, or its implements, is altering a whole 1st-level feature
    ("ref/arc-occultist/silksworn", "spells"): (1, "ruling 50: alters the occultist's spells (the whole spellcasting, a 1st-level class feature)"),
    ("ref/arc-occultist/silksworn", "implements"): (1, "ruling 50: alters the occultist's implements, a 1st-level class feature on the class table"),
    ("ref/arc-occultist/silksworn", "devoted-mystic"): (1, "ruling 50: alters implements, a 1st-level class feature on the class table (and the printed four schools \"at 1st level\")"),
    ("ref/arc-magus/iron-ring-striker", "diminished-spellcasting"): (1, "ruling 50: alters the magus's spellcasting (the whole feature, a 1st-level class feature)"),
    ("ref/arc-witch/witch-watcher", "diminished-spellcasting"): (1, "ruling 50: alters the witch's spellcasting (the whole feature, a 1st-level class feature)"),
    ("ref/arc-oracle/inerrant-voice", "revelations"): (3, "its own sentence: \"must take the following revelation at 3rd level\""),
    ("ref/arc-oracle/inerrant-voice", "vigilant-protector"): (3, "the Revelations paragraph before it: \"must take the following revelation at 3rd level\""),
}
# a feature that offers a choice from what follows ("can select an edge from those listed below", "can select from any of the following hexes")
CHOICE_INTRO = re.compile(r"\b(?:select|selects|choose|chooses|take|takes|pick|picks)\b[^.]{0,100}?\b(?:from|among|of|in)\s+(?:the\s+|these\s+|those\s+)?"
                          r"(?:following|listed below|below)\b|\bfrom (?:those|the list) (?:listed )?below\b|"
                          r"\b(?:select|selects|choose|chooses|take|takes|pick|picks)\s+(?:any\s+of\s+)?the\s+following\b"
                          r"|\bcan (?:also )?select the following additional\b|\bcan be selected by any\b|\bcan also be taken by any\b|\bselect the [^.]{0,60}\bbelow\b"
                          r"|\badds? the following (?!spells?\b)[^.]{0,120}\bto (?:the|her|his) list\b|\bways? listed below\b|\b(?:are|is) (?:listed|noted|described|shown) below\b|\bas noted below\b", re.I)
LEVEL_IN_FIRST_PARAGRAPH = {
    ("ref/arc-paladin/invigorator", "champion-of-life"),     # a flavor sentence, then "At 20th level, three times per day ..."
    ("ref/arc-brawler/wild-child", "wild-tricks"),
    ("ref/arc-bloodrager/spelleater", "blood-of-life"),
    ("ref/arc-investigator/empiricist", "ceaseless-observation"),
    ("ref/arc-investigator/empiricist", "unfailing-logic"),
    ("ref/arc-druid/naga-aspirant", "aspirant-s-bond"),
    ("ref/arc-ranger/dusk-stalker", "shadow-guide"),
    ("ref/arc-warpriest/forgepriest", "craft-magic-arms-and-armor"),
    ("ref/arc-ranger/wild-shadow", "woodland-stride"),
    ("ref/arc-barbarian/true-primitive", "trophy-fetish"),
    ("ref/arc-gunslinger/gun-tank", "bullet-deflection"),
    ("ref/arc-inquisitor/exorcist", "closed-mind"),
    ("ref/arc-paladin/empyreal-knight", "celestial-heart"),
    ("ref/arc-rogue/pirate", "unflinching"),
    ("ref/arc-paladin/divine-hunter", "precise-shot"),
    # Blood of the Ancients: a flavor sentence, then "At 2nd level, he ..." in the first paragraph
    ("ref/arc-investigator/antiquarian", "item-lore"),
    ("ref/arc-investigator/tekritanin-arbiter", "expert-mediator"),
    ("ref/arc-investigator/tekritanin-arbiter", "hidden-meaning"),
}


# A stored trade that print states in the prose of a feature and in no trade sentence (owner ruling 28 of 2026-11-25):
# the entry, the stored name, the feature whose text states it. The check accepts the prose of the feature as support.
# A trade that names more features than the sentence that states it (owner ruling 47): the entry and the stored name (before a rename), the anchors.
TRADE_EXTRA_BY = {
    ("ref/arc-wizard/chronomancer", "10th-, 15th-, and 20th-level bonus feats"): ["accelerate", "complex-contingency", "parallel-self"],
}

TRADE_PROSE_BY = {
    ("ref/arc-ninja/mask-of-the-living-god", "Spend ki to make an additional attack"): "expurgate",     # "The mask of the Living God cannot spend a point from his ki pool to make an additional attack." (ruling 28)
    ("ref/arc-shifter/feyform-shifter", "Shifter aspect"): "fey-aspect",     # owner ruling 49: "This alters and replaces all improvements to shifter aspect" stores both trades
    ("ref/arc-inquisitor/faith-hunter", "justice"): "sworn-enemy",
    ("ref/arc-inquisitor/faith-hunter", "destruction judgments"): "sworn-enemy",
    ("ref/arc-rogue/phantom-thief", "Debilitating injury"): "refined-education",
    ("ref/arc-rogue/phantom-thief", "Rogue's edge (unchained rogue only)"): "refined-education",
}


# An anchor that the dedupe of the extraction made long, or that reads unnaturally, written as the head says it (the TSV note records it).
ANCHOR_FIXES = {
    # Winding Path Renegade (Adventurer's Guide p. 106): the table title "Monk Moves" is its own section, so the dedupe gave the
    # feature "Monk Moves (Ex)" the long anchor of its predecessor
    ("ref/arc-brawler/winding-path-renegade", "mystery-of-untwisting-iron-monk-moves"): "monk-moves",
    # Opus review of batch 4: the anchor without the ability tag, and a name that reads naturally
    ("ref/arc-unchained-summoner/devil-binder", "infernal-affinity-ex-su-or-sp"): "infernal-affinity",
    ("ref/arc-summoner/leshy-caller", "alignment-base-form"): "plant-eidolon-base-form",
    ("ref/arc-unchained-summoner/leshy-caller", "alignment-base-form"): "plant-eidolon-base-form",
}


# Stored trades that print's sentence names and that carry no `by`: print has only a bare sentence for them ("This
# replaces the monk class ability the qinggong monk gives up for this ki power", Ultimate Magic p. 51).
TRADE_NO_BY = {
}


# Stored trades that print does not support in any sentence, and that are dropped (owner ruling 17 of 2026-11-24,
# review of batch 1): the Totem Transformation of the dragon, saurian and shark shaman never mentions woodland stride.
# The entries whose removal an owner ruling after ruling 17 confirms (ruling 39 of 2026-11-25: Sage Counselor keeps it).
TRADE_REMOVAL_RULED = {"ref/arc-monk/sage-counselor"}
TRADE_REMOVALS = {
    "ref/arc-druid/dragon-shaman": [("replaces", "Woodland stride")],
    "ref/arc-druid/saurian-shaman": [("replaces", "Woodland stride")],
    # Purifier (Advanced Race Guide p. 86) lists its bonus spells and prints no sentence that replaces the mystery's
    "ref/arc-oracle/purifier": [("replaces", "All bonus spells from the oracle's mystery")],
    # Buccaneer (ARG p. 74): Gun Training prints no sentence that replaces gun training 3
    "ref/arc-gunslinger/buccaneer": [("replaces", "Gun training 3")],
    "ref/arc-druid/shark-shaman": [("replaces", "Woodland stride")],
    # Sage Counselor (Ultimate Intrigue p. 67): Feinting Flurry says he "can't spend 1 ki point to make an additional attack when
    # making a flurry of blows", a restriction that the sentence "alters flurry of blows and ki pool" states; print names no
    # trade of "the ability to spend ki to make an additional attack" (the import made one of the sentence; owner question)
    "ref/arc-monk/sage-counselor": [("replaces", "The ability to spend ki to make an additional attack with a flurry of blows")],
}


# A stored trade whose `feature` link changes with its name (data fix, the TSV note records it): the entry, the
# stored name, the anchor of the base class feature that print names. Divine Hunter (Ultimate Combat p. 62): print
# says "replaces aura of faith" for Righteous Hunter; the import stored aura of righteousness.
TRADE_RELINKS = {
    ("ref/arc-paladin/divine-hunter", "Aura of righteousness"): "aura-of-faith",
    ("ref/arc-cleric/iron-priest", "Casting"): "spontaneous-casting",      # "This ability alters casting." (Technology Guide p. 13) names the cleric's spontaneous casting, not the spells (review of #356)
}


def dropped_trade_indices(e: Entry) -> set[int]:
    """The indices of the stored trades that repeat another one without a `feature`, and of those that print
    does not support."""
    out = set()
    for i, t in enumerate(trades_of(e)):
        key = trade_name(t)
        if key in TRADE_MERGED.get(e.id, []) or key in TRADE_REMOVALS.get(e.id, []):
            out.add(i)
        elif "feature" not in t and any(     # owner ruling 5 (Opus review of #329): a repeat of a linked trade, names equal without case, is left out
                j != i and (trade_name(u)[0], trade_name(u)[1].lower()) == (key[0], key[1].lower()) and "feature" in u
                for j, u in enumerate(trades_of(e))):
            out.add(i)
        elif (key[0], key[1].lower()) in [(o, n.lower()) for o, n in TRADE_DROPS.get(e.id, [])] and "feature" not in t and any(
                j != i and (trade_name(u)[0], trade_name(u)[1].lower()) == (key[0], key[1].lower()) and "feature" in u
                for j, u in enumerate(trades_of(e))):
            out.add(i)
    return out


def effective_trades_origin(e: Entry) -> list[tuple[dict, int | None]]:
    """The trades that the entry ends up with, each with the index of the stored trade it comes from (None for an addition)."""
    out: list[tuple[dict, int | None]] = []
    skip = dropped_trade_indices(e)
    for i, t in enumerate(trades_of(e)):
        if i in skip:
            continue
        op, name = trade_name(t)
        new = TRADE_RENAMES.get((e.id, name))
        t2 = dict(t, **{op: new}) if new else t
        fixed = TRADE_OP_FIXES.get((e.id, name))
        if fixed and fixed != op:
            t2 = {("replaces" if fixed == "replaces" else "alters") if k == op else k: v for k, v in t2.items()}
        if name in TRADE_NO_BY.get(e.id, []):
            t2 = dict(t2, _no_by=True)
        if (e.id, name) in TRADE_PROSE_BY:
            t2 = dict(t2, _prose_by=TRADE_PROSE_BY[(e.id, name)])
        if (e.id, name) in TRADE_EXTRA_BY:
            t2 = dict(t2, _extra_by=TRADE_EXTRA_BY[(e.id, name)])
        out.append((t2, i))
    return out + [(dict(t, _prose_by=TRADE_PROSE_BY[(e.id, trade_name(t)[1])]) if (e.id, trade_name(t)[1]) in TRADE_PROSE_BY else dict(t), None)
                  for t in TRADE_ADDITIONS.get(e.id, [])]


def effective_trades(e: Entry) -> list[dict]:
    return [t for t, _ in effective_trades_origin(e)]


def is_option_head(head: str, bold: bool) -> bool:
    """Owner ruling 15 of 2026-11-24: an item of an option list (the creature types of the infiltrator, the forms of
    the shapeshifter, and in later books bloodlines, domains, mysteries, totems) is not a class feature. In print
    it is an italic head with no ability tag; a sub-power such as "Rallying Cry (Su)" has a tag and stays a feature."""
    return not bold and not ABILITY_TAG.search(head)


def with_children(rows: list[dict]) -> list[dict]:
    """The listed rows, each with the text of its option subheadings added: a trade sentence of an option belongs to
    the feature that holds it."""
    out = []

    def below(anchor: str) -> list[dict]:
        kids = [k for k in rows if k.get("parent") == anchor]
        return [x for k in kids for x in [k] + below(k["anchor"])]

    for r in rows:
        if r["listed"]:
            kids = [k["print"] for k in below(r["anchor"]) if k["print"]]
            out.append(dict(r, print="\n\n".join([r["print"]] + kids)) if kids else r)
    return out


def opening_texts(rows: list[dict], opening: list[str]) -> list[str]:
    """The text whose trade sentences carry no `by`: the opening, and every section under a heading that is not
    a feature (owner ruling 13 of 2026-11-24, app #690: the innermost heading decides). An option subheading
    belongs to its feature."""
    return list(opening) + [r["print"] for r in rows if not r["listed"] and not r.get("parent") and r["print"]]


def first_level_key(name: str) -> str:
    """A feature name as the class table of a base class writes it, compared without case, plural, tag and suffix:
    "smite evil 1/day", "channel energy 1d6", "bomb 1d6", "Bombs" and "witch's familiar" are the names smite evil,
    channel energy, bomb, bomb and witch's familiar."""
    name = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", ABILITY_TAG.sub("", name))
    name = re.sub(r"[_*]", "", name)
    name = re.sub(r"^((?:the|a|an)\s+)?(\S.*?\S)\s+bonus feats?$", r"\1\2", name.strip(), flags=re.I)   # "The Brew Potion bonus feat" is the name Brew Potion, as the alchemist table writes it
    name = re.sub(r"\s*\((?:minor|major|[a-z]+)\)\s*$", "", name.strip(), flags=re.I)  # the class table of the warpriest: "Blessings (minor)"
    name = re.sub(r"^\d+(?:st|nd|rd|th)\s+", "", name.strip())                    # the class table of the ranger: "1st favored enemy"
    name = re.sub(r"[,;]?\s+and (?:all|each|every)\s+(?:of\s+)?(?:its\s+|the\s+)?(?:improvements?|upgrades?)\b.*$", "", name, flags=re.I)   # "Shifter aspect and all improvements to it"
    name = re.sub(r"\s+(?:\d+/[\w-]+|\d+d\d+|[+\-]\d.*|\d+)$", "", name.strip())
    name = re.sub(r"\s*\([^()]*\)$", "", name.strip())                          # "blessings (minor)" is the name blessings
    name = re.sub(r"^(?:the|a|an)\s+", "", fold(name))              # "The cavalier's order" is the name order
    name = re.sub(r"^[a-z]+'s\s+", "", name)                       # "witch's familiar" is the name familiar
    return " ".join(stem(w) for w in re.findall(r"[a-z0-9']+", name))


def first_level_alt_key(name: str) -> str:
    """The same name with a possessive kept as a word: "Nature's bond" is `nature bond`, the name that the druid's class table writes."""
    name = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", ABILITY_TAG.sub("", name))
    name = re.sub(r"[_*]", "", name)
    name = re.sub(r"\s*\([^()]*\)$", "", fold(name).strip())
    name = re.sub(r"^((?:the|a|an)\s+)?(\S.*?\S)\s+bonus feats?$", r"\1\2", name.strip(), flags=re.I)
    name = re.sub(r"^(?:the|a|an)\s+", "", name).replace("'s ", " ")
    return " ".join(stem(w) for w in re.findall(r"[a-z0-9]+", name))


# 1st-level features of a base class that its table does not list as such (owner ruling 48 of 2026-11-26): the druid's spontaneous casting, and the
# gunslinger's 1st-level deeds (the table lists "Deeds"; their entries say "Prereq: 1st-level gunslinger"). Names as `first_level_key` reads them.
FIRST_LEVEL_EXTRA = {
    "ref/class/druid": ("Spontaneous casting",),
    "ref/class/cleric": ("Spontaneous casting",),       # owner ruling 57 (review of #346): the cleric's spontaneous casting is a 1st-level feature that the table does not list, as the druid's
    "ref/class/gunslinger": ("Deadeye", "Deadeye deed", "Gunslinger's dodge", "Gunslinger's dodge deed", "Quick clear", "Quick clear deed"),
}


def class_first_level(corpus: Path, class_id: str, cache: dict) -> set[str]:
    """The names (see `first_level_key`) of the features that the Special column of the class table of a base class
    lists at 1st level. The column is found by its heading: it is the last column of a martial class and the sixth
    of a caster's table, never a spell-slot column or fast movement."""
    if class_id in cache:
        return cache[class_id]
    path = corpus / "entries" / (class_id.removeprefix("ref/") + ".md")
    keys: set[str] = set()
    if path.exists():
        col = None
        for ln in path.read_text(encoding="utf-8").split("\n"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if col is None and ln.startswith("|Level|") and "Special" in cells:
                col = cells.index("Special")
            elif col is not None and ln.startswith("|1st|"):
                if col < len(cells):
                    for item in re.split(r",(?![^()]*\))", cells[col]):
                        keys.add(first_level_key(item))
                break
    keys |= {first_level_key(x) for x in FIRST_LEVEL_EXTRA.get(class_id, ())}
    cache[class_id] = keys
    return keys


def class_table_levels(corpus: Path, class_id: str, cache: dict) -> dict[str, int]:
    """The names (see `first_level_key`) of the features that the Special column of the class table of a base class lists, each with the lowest level at
    which it is listed (owner ruling 57: the rulings 35, 48 and 50 hold for any level), and the names of `FIRST_LEVEL_EXTRA` at level 1."""
    ck = ("levels", class_id)
    if ck in cache:
        return cache[ck]
    path = corpus / "entries" / (class_id.removeprefix("ref/") + ".md")
    out: dict[str, int] = {}
    if path.exists():
        col = None
        for ln in path.read_text(encoding="utf-8").split("\n"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if col is None and ln.startswith("|Level|") and "Special" in cells:
                col = cells.index("Special")
            elif col is not None and (m := re.match(r"\|(\d+)(?:st|nd|rd|th)\|", ln)):
                if col < len(cells):
                    for item in re.split(r",(?![^()]*\))", cells[col]):
                        out.setdefault(first_level_key(item), int(m.group(1)))
                if int(m.group(1)) >= 20:
                    break
    for x in FIRST_LEVEL_EXTRA.get(class_id, ()):
        out[first_level_key(x)] = 1
    cache[ck] = out
    return out



# A trade whose name print makes longer than the class table's name ("The bomb class feature", "Brew Potion, though an oozemaster can still select ...",
# the summoner's "summon monster I-IX abilities"): the table's name for it, per entry (review of #347; a looser match would give levels to parts of
# features that ruling 57 records as no level).
TABLE_NAMES = {
    ("ref/arc-alchemist/oozemaster", "The bomb class feature"): "Bomb",
    ("ref/arc-alchemist/oozemaster", "Brew Potion, though an oozemaster can still select Brew Potion without meeting the feat's prerequisites"): "Brew potion",
    ("ref/arc-summoner/morphic-savant", "Summon monster"): "Summon monster I",
    ("ref/arc-unchained-summoner/morphic-savant", "Summon monster"): "Summon monster I",
    ("ref/arc-summoner/unwavering-conduit", "Summon monster"): "Summon monster I",
    ("ref/arc-summoner/storm-caller", "the summoner's summon monster I\u2013IX abilities"): "Summon monster I",
    ("ref/arc-unchained-summoner/storm-caller", "the summoner's summon monster I\u2013IX abilities"): "Summon monster I",
}


def table_level(tab: dict[str, int], name: str, entry_id: str = "") -> int | None:
    """The level at which the class table lists the feature that a trade names: the exact name (`first_level_key`), or the table's name that
    `TABLE_NAMES` gives for a trade that print names longer."""
    for k in (first_level_key(name), first_level_alt_key(name), first_level_key(TABLE_NAMES.get((entry_id, name), ""))):
        if k and k in tab:
            return tab[k]
    return None


def fold_table_sections(rows: list[dict], decisions: dict, entry_id: str, problems: list[str]) -> None:
    """The `fold-into:ANCHOR` decisions of an entry (owner ruling 44): the section moves behind the end of the section that the
    decision names, its head as a bold line directly above its text (the Markdown table)."""
    for (eid, anchor), (kind, note) in decisions.items():
        if eid != entry_id or not kind.startswith("fold-into:"):
            continue
        row = next((x for x in rows if x["anchor"] == anchor), None)
        target = next((x for x in rows if x["anchor"] == kind.split(":", 1)[1]), None)
        if row is None or target is None:
            problems.append(f"the fold-into decision of `{anchor}` names a section that is not there")
            continue
        rows.remove(row)
        target["print"] += "\n\n**" + re.sub(r"(?<!\\)([*_])", r"\\\1", row["head"]) + "**\n\n" + row["print"]
        target["notes"].append(f"table `{anchor}` set under this section behind its printed title (ruling 44): {note}")
        target["status"] = "print" if target["status"] == "draft" else target["status"]


def finalize(e: Entry, res: dict, class_cache: dict | None = None) -> dict:
    """Anchors, levels, `by` and the entry-level problems, from the compared rows."""
    class_cache = {} if class_cache is None else class_cache
    corpus = e.path.parents[2]
    rows = res["rows"]
    problems = list(res["problems"])
    # an anchor that occurs twice: the later one is prefixed with the nearest unique head before it
    counts = Counter(r["anchor"] for r in rows)
    seen: set[str] = set()
    for i, r in enumerate(rows):
        if r["anchor"] in seen:
            owner = next((q["anchor"] for q in reversed(rows[:i]) if counts[q["anchor"]] == 1 and q["anchor"] not in ("rage-powers",)), "")
            new = f"{owner}-{r['anchor']}" if owner else r["anchor"]
            r["notes"].append(f"anchor `{r['anchor']}` occurs twice; this one is `{new}`")
            r["anchor"] = new
        seen.add(r["anchor"])
    # hand decisions of the review (ruling 14)
    decisions = res.get("decisions", {})
    dropped: list[dict] = []
    opening = list(res["opening"])
    opening_from_print = False
    deferred: list[tuple[str, str]] = []          # links of the opening that CONTEXT_LINKS ties to a phrase of a section
    by_anchor = {r["anchor"]: r for r in rows}
    for r in list(rows):
        dec = decisions.get((e.id, r["anchor"]))
        if not dec:
            continue
        kind, note = dec
        if ";" in kind:
            kind, _, after = kind.partition(";")
            if after.startswith("after:") and after.split(":", 1)[1] in by_anchor:
                rows.remove(r)
                rows.insert(rows.index(by_anchor[after.split(":", 1)[1]]) + 1, r)
                r["notes"].append("moved behind `" + after.split(":", 1)[1] + "`: print sets the sidebar before the text it belongs after")
        if kind.startswith("tail-to:"):
            paras = r["print"].split("\n\n")
            tail = "\n\n".join(paras[1:])
            r["print"] = paras[0]
            target = by_anchor[kind.split(":", 1)[1]]
            target["print"] += "\n\n" + tail
            r["notes"] = [note] + [n for n in r["notes"] if n.startswith(("print asterisks", "misprint", "link", "anchor", "errata"))]
            r["status"] = "print"
        elif kind in ("sidebar", "carried"):
            # `carried`: the section is a printed list whose text the hand-written edit of another feature carries (owner ruling 45); it is left out
            # a box of the page that is not part of the archetype (lore of a faction, a deity, an order): the book prints it beside the
            # archetype, the corpus does not have it; it is left out and the note says so (Adventurer's Guide, Ultimate Wilderness)
            rows.remove(r)
            r["notes"], r["status"] = [note], "print"
            dropped.append(r)
        elif kind in ("drop", "to-opening"):
            if kind == "drop" and r.get("print", "").strip() and r.get("span"):
                # the head is printed and the corpus has it: dropping it would leave print's text out
                problems.append(f"the drop decision of `{r['anchor']}` leaves out printed text: the head is printed")
            rows.remove(r)
            r["notes"], r["status"] = [note], "print"
            dropped.append(r)
            if kind == "to-opening":
                opening_from_print = True
                opening = [opening_with_links(e.id, o, res.get("opening_links", []), deferred) for o in res["opening"]]
        elif kind == "hold":
            r["status"] = "hold"
            r["notes"] = [note] + [n for n in r["notes"] if n.startswith(("print asterisks", "misprint", "link", "anchor", "errata"))]
        elif kind in ("unlist", "list") or kind.startswith("sub-of:"):
            r["listed"] = kind == "list"
            r["option"] = False
            r["parent"] = kind.split(":", 1)[1] if kind.startswith("sub-of:") else None
            if r["status"] == "hold":
                r["status"] = "print"
            r["notes"] = [note] + [n for n in r["notes"] if n.startswith(("print asterisks", "misprint", "link", "anchor", "level 1", "rule 8", "ruling", "trade", "errata"))]
        elif kind == "print" and r["status"] == "hold":
            r["status"] = "print"
            r["notes"] = [note] + [n for n in r["notes"] if n.startswith(("print asterisks", "misprint", "link", "anchor", "level 1", "rule 8", "ruling", "trade", "errata"))]

    # rule 5: a printed table or box that the print span does not carry is a hold, not a silent loss. The span ended at a title that no
    # rule names as the start of another section of the book (a table title, a box): the entry needs a decision about it
    end, known = res.get("section_end", (None, True))
    if RULES["dropped"] and end and not known:
        dec_end = decisions.get((e.id, "end:" + anchor_of(end))) or decisions.get((e.id, anchor_of(end)))     # `end:SLUG` names the title that ends the span, so that it cannot meet a feature of the same slug
        if not dec_end or dec_end[0].split(";")[0] not in ("sidebar", "drop", "print"):
            problems.append(f"the print span ends at the title \"{end}\", which names no other section of the book (a table, a box?): "
                            f"decide `sidebar` (a lore box, ruling 41) or `drop`, or write it with an edit, for `{anchor_of(end)}`")
    for r in rows:
        apply_edit(r, res.get("edits", {}).get((e.id, r["anchor"])))
    for add in res.get("adds", {}).get(e.id, []):
        row = {"anchor": add["anchor"], "span": "", "page": "", "pseudo": False, "draft": "", "level_import": None,
               "head": add["head"], "print": add["text"].strip("\n"), "status": "print", "notes": [add["note"]],
               "listed": False, "name": add["head"], "option": False, "parent": add["parent"] or None}
        at = -1 if not add["after"] else next((i for i, x in enumerate(rows) if x["anchor"] == add["after"]), len(rows) - 1)      # an empty `after` puts the section before the first feature
        rows.insert(at + 1, row)
    # owner ruling 44: a printed table title goes on a bold line directly above the Markdown table, not in a heading. A section
    # whose print head is the title of a table (Table 2-2: Homunculus Companions, Monk Moves, 4th-Level Ki Powers) is folded behind
    # the end of the section `fold-into:ANCHOR` names; its head becomes the bold line and its text the table
    fold_table_sections(rows, decisions, e.id, problems)
    # an anchor that two kept rows share is a problem; rows that a decision dropped are not kept (Leshy Caller's four sets of
    # stat rows, each dropped, share their anchors)
    for a, n in Counter(r["anchor"] for r in rows).items():
        if n > 1:
            problems.append(f"anchor `{a}` occurs {n} times")
    # a decided row of the first kind that moved text into another row is re-decided there
    for r in rows:
        dec = decisions.get((e.id, r["anchor"]))
        if dec and dec[0] == "print" and r["status"] == "hold":
            r["status"] = "print"
    if res.get("opening_diff") and not opening_from_print and rows:
        opening_from_print = True
        opening = [opening_with_links(e.id, o, res.get("opening_links", []), deferred) for o in res["opening"]]
        rows[0]["notes"].append("opening text written from print: the import differs in " + ", ".join(res["opening_diff"][:12])
                                + (" ..." if len(res["opening_diff"]) > 12 else ""))
    res["opening"] = opening
    for label, target in deferred:
        place_elsewhere(rows, label, target)
    # a link that its own section could not place goes on the first free occurrence of its words in any section of the
    # entry (owner review of batch 3); only the links that find no place anywhere stay in the notes
    for r in rows:
        placed = []
        for label, target in r.pop("lost_links", []):
            at = place_elsewhere(rows, label, target)
            if at:
                placed.append((label, at))
        if placed:
            old = next((n for n in r["notes"] if n.startswith("link not placed: ")), "")
            gone = {lb for lb, _ in placed}
            rest = [x for x in old[len("link not placed: "):].split(", ") if x and x not in gone]
            r["notes"] = [n for n in r["notes"] if not n.startswith("link not placed: ")]
            if rest:
                r["notes"].append("link not placed: " + ", ".join(rest))
            r["notes"] += [f"link of `{lb}` placed in `{at}`" for lb, at in placed]
    for r in dropped:
        for label, target in r.get("links", []):
            if not any(f"[{label}]({target})" in o["print"] for o in rows):
                at = place_elsewhere(rows, label, target)
                r["notes"].append(f"link of the dropped section placed in `{at}`: {label}" if at else f"link of the dropped section not placed: {label}")
    # the last links are placed: the citations that now follow a link go (owner ruling 26)
    for r in rows:
        if (e.id, r["anchor"]) not in res.get("edits", {}) and r["print"]:
            r["print"] = final_citations(r["print"], e.id)         # a hand-written edit says what it keeps (ruling 42)
    res["opening"] = [final_citations(o, e.id) for o in res["opening"]]
    res["problems"] = [p for p in problems if not p.startswith("head not printed")]
    problems = res["problems"]
    left = [r["head"] for r in rows if "head not printed" in r["notes"] and r["status"] == "hold"]
    if left:
        problems.append("head not printed: " + ", ".join(left))
    # an anchor that the dedupe of the extraction made long, written as the head says it (the TSV note records it)
    for (eid, old), new in ANCHOR_FIXES.items():
        if eid == e.id and any(r["anchor"] == old for r in rows) and not any(r["anchor"] == new for r in rows):
            for r in rows:
                if r["anchor"] == old:
                    r["anchor"] = new
                    r["notes"].append(f"anchor `{old}` is `{new}`: the section that shared the name is not an entry of its own")
                if r.get("parent") == old:
                    r["parent"] = new
    # ruling 15: an option item is a plain subheading of the nearest feature before it (none: a plain heading)
    holder = None
    for r in rows:
        if r["listed"]:
            holder = r
        elif r.get("option") and holder is not None:
            r["parent"] = holder["anchor"]
            r["notes"].append(f"option item, not a feature (ruling 15): a subheading of `{holder['anchor']}`")
    listed = [r for r in rows if r["listed"]]
    trades = effective_trades(e)
    by, more = assign_by(trades, with_children(rows), opening_texts(rows, res["opening"])) if all(r["print"] for r in listed) else ({}, [])
    problems += more
    # an entry whose every head is not printed has no row: the notes of its trades go nowhere (the decisions file holds the reasons)
    sink = rows[0] if rows else {"notes": [], "anchor": None}
    for i, (t, origin) in enumerate(effective_trades_origin(e)):
        if origin is None:
            anchors = by.get(i) or [sink["anchor"]]
            where = f' (feature `{t["feature"]}`)' if "feature" in t else ""
            note = f'trade added: {trade_name(t)[0]} "{trade_name(t)[1]}"{where}, which print states and the entry did not store'
            next((r for r in rows if r["anchor"] == anchors[0]), sink)["notes"].append(note)
            continue
        old = trades_of(e)[origin]
        if t.get("_no_by"):
            sink["notes"].append(f'trade without `by`: {trade_name(old)[0]} "{trade_name(old)[1]}" has only a bare printed sentence')
            t = {k: v for k, v in t.items() if k != "_no_by"}
        if t.get("_prose_by"):
            sink["notes"].append(f'trade by prose (ruling 28): {trade_name(old)[0]} "{trade_name(old)[1]}" is stated in the text of `{t["_prose_by"]}`, in no trade sentence')
            t = {k: v for k, v in t.items() if k != "_prose_by"}
        if (e.id, trade_name(old)[1]) in TRADE_RELINKS:
            sink["notes"].append(f'trade relinked: "{trade_name(old)[1]}" now names `{TRADE_RELINKS[(e.id, trade_name(old)[1])]}`, the feature that print says it replaces')
        if trade_name(old)[1] in TRADE_UNLINKS.get(e.id, []):
            sink["notes"].append(f'trade unlinked: "{trade_name(old)[1]}" loses its `feature` and `levels`: a trade of the whole Bomb feature (print: "functions as and replaces the standard alchemist bomb class feature", p. 20) overlaps a trade of one level of it, so the printed level trade is one unlinked trade')
        if old != t:
            anchors = by.get(i) or [sink["anchor"]]
            note = ""
            if trade_name(old)[0] != trade_name(t)[0]:
                note = f'trade op fixed: stored as {trade_name(old)[0]} "{trade_name(old)[1]}", print says {trade_name(t)[0]}'
            if trade_name(old)[1] != trade_name(t)[1]:
                note += ("; " if note else "") + f'trade renamed: "{trade_name(old)[1]}" to "{trade_name(t)[1]}" to match the printed sentence'
                if (e.id, trade_name(t)[1]) in TRADE_LEVELS:
                    note += f"; its levels are now {TRADE_LEVELS[(e.id, trade_name(t)[1])]}, the printed levels"
            next((r for r in rows if r["anchor"] == anchors[0]), sink)["notes"].append(note)
    for origin in sorted(dropped_trade_indices(e)):
        old = trades_of(e)[origin]
        if trade_name(old) in TRADE_REMOVALS.get(e.id, []):
            ruling = "ruling 39, which keeps the removal; ruling 17" if e.id in TRADE_REMOVAL_RULED else "ruling 17"
            sink["notes"].append(f'trade dropped ({ruling}): {trade_name(old)[0]} "{trade_name(old)[1]}" has no printed support in any sentence')
            continue
        if trade_name(old) in TRADE_MERGED.get(e.id, []):
            sink["notes"].append(f'trade merged: {trade_name(old)[0]} "{trade_name(old)[1]}" is the printed trade of the sentence that each feature prints with the same words; one trade names all three features')
            continue
        sink["notes"].append(f'duplicate trade left out: {trade_name(old)[0]} "{trade_name(old)[1]}" was stored twice, once without its feature link')
    for r in rows:
        first = r["print"].split("\n\n", 1)[0] if r["print"] else ""
        r["level"] = lead_level(first)
        if r["level"] is None and r["listed"] and LEAD_EXT["on"]:
            r["level"], why = ext_lead_level(first)
            if why:
                r["notes"].append(f"level {r['level']}: print says {why}")
        if r["level"] is None and r["listed"]:
            # a level that print states after a flavor sentence or inside the sentence (reviewed list)
            if (e.id, r["anchor"]) in LEVEL_IN_FIRST_PARAGRAPH:
                m = re.search(r"\b(?:At|Starting at|Beginning at)\s+(\d+)(st|nd|rd|th)\s+level\b", first, re.I)
                if m and 1 <= int(m.group(1)) <= 20 and m.group(2) == ordinal(int(m.group(1)))[len(m.group(1)):]:
                    r["level"] = int(m.group(1))
                    r["notes"].append(f"level {r['level']}: print says \"{m.group(0)}\" in its first paragraph, after an opening sentence")
        if r["level"] is None and r["listed"] and (e.id, r["anchor"]) in LEVEL_FROM_PRINT:
            r["level"], why = LEVEL_FROM_PRINT[(e.id, r["anchor"])]
            r["notes"].append(f"level {r['level']}: {why}")
        if r["level"] is None and r["listed"] and r["level_import"] is not None and (e.id, r["anchor"]) not in LEVEL_ONE_REPLACES:
            # a lead after an opening sentence ("... honed. At 3rd level, if ...") or "a fortune-finder of 20th level becomes ...": print gives the
            # level that the import's Gained row has (review of #338)
            m = LATER_LEAD.search(first)
            if m and UPGRADE_WORDS.search(first[m.start():].split(". ", 1)[0]):
                m = None                      # "At 5th level, if the target is Large or larger, these bonuses increase": a step of the feature, not its level
            m = m or OF_LEVEL.search(first)
            if m and int(m.group(1)) == r["level_import"] and ordinal(int(m.group(1)))[len(m.group(1)):] == m.group(2):
                r["level"] = int(m.group(1))
                r["notes"].append(f"level {r['level']}: print says \"{m.group(0).strip()[-40:]}\" in its first paragraph, as the import has it")
        if r["level"] is None and r["listed"]:
            # "gains this ability at 7th level", "receives this ability at 7th level instead of at 3rd level", "gains the poison lore ability at 1st level"
            m = re.match(r"[^.]*?\b(?:gains|receives)\s+(?:this|the\s+[\w' -]+?)\s+ability at (\d+)(st|nd|rd|th) level\b", first)
            if m and 1 <= int(m.group(1)) <= 20 and m.group(2) == ordinal(int(m.group(1)))[len(m.group(1)):]:
                r["level"] = int(m.group(1))
                r["notes"].append(f"level {r['level']}: print says \"{m.group(0)[len(m.group(0)) - 50:].strip()}\"")
        if r["level"] is None and r["listed"]:
            mine = [trades[i] for i, a in by.items() if a == [r["anchor"]]]
            levels = {tuple(t.get("levels") or ()) for t in mine}
            if mine and len(levels) == 1 and len(next(iter(levels))) == 1 and all("levels" in t for t in mine):
                r["level"] = next(iter(levels))[0]
                r["notes"].append("level from the trade")
            elif (e.id, r["anchor"]) in LEVEL_ONE_REPLACES:
                r["level"] = 1
                r["notes"].append("level 1 (ruling 35): replaces " + ", ".join(trade_name(t)[1] for t in mine) + ", a 1st-level feature of the class" + (" (the class table lists it as `Blessing (minor)`)" if e.id == "ref/arc-warpriest/divine-commander" else ""))
            elif mine and (e.id, r["anchor"]) not in NO_LEVEL_ONE:
                # ruling 11: the feature replaces features that the base class gains at 1st level. Print states no level here, so
                # the import's level (a line of the feature's own text, "At 2nd Level: ...") does not stop the rule (final review of
                # batch 3); a differing import level is the hold below, which a hand decision settles.
                firsts = []
                for t in mine:
                    cls = t.get("class") or (e.classes[0] if e.classes else "")
                    # a trade of the 1st level: its `levels` include 1, or its name states "1st" ("bonus feats gained at 1st, 2nd,
                    # and 6th levels", "1st-, 7th-, and 15th-level deeds"), or the class table lists it at 1st level
                    firsts.append(1 in (t.get("levels") or ()) or bool(re.search(r"\b1st\b", trade_name(t)[1]))
                                  or (bool(cls) and (first_level_key(trade_name(t)[1]) in class_first_level(corpus, cls, class_cache)
                                                     or first_level_alt_key(trade_name(t)[1]) in class_first_level(corpus, cls, class_cache)
                                                     or table_level(class_table_levels(corpus, cls, class_cache), trade_name(t)[1], e.id) == 1)))
                # ruling 35: level 1 when any feature that it replaces is a 1st-level feature, even if it also replaces later ones
                # owner ruling 50: altering a whole 1st-level feature counts like replacing it; a part of a feature (a proficiency, class skills,
                # a spell list) is no class-table name and gives none (ruling 48)
                if any(f and trade_name(t)[0] in ("replaces", "alters") for f, t in zip(firsts, mine)):
                    r["level"] = 1
                    named = any(f and (1 in (t.get("levels") or ()) or re.search(r"\b1st\b", trade_name(t)[1])) for f, t in zip(firsts, mine))
                    ops = [t for t in mine if trade_name(t)[0] in ("replaces", "alters")]
                    r["notes"].append("level 1: " + ("replaces " + ", ".join(trade_name(t)[1] for t in ops) if all(trade_name(t)[0] == "replaces" for t in ops)
                                                     else ", ".join(trade_name(t)[0] + " " + trade_name(t)[1] for t in ops))
                                      + (", of which one is gained at 1st level (the printed level of the trade, or the class table)" if named
                                         else ", of which one is gained at 1st level in the class table"))
                elif RULE57["on"]:
                    # owner ruling 57: the rulings 35, 48 and 50 hold for any level: a feature with no printed level that alters or replaces a whole class feature
                    # that the class table lists at level N gets level N, the lowest of its trades (a trade of a power is a part: none; a trade that names its levels counts with its lowest level)
                    found = []
                    for t in mine:
                        op, name = trade_name(t)
                        cls = t.get("class") or (e.classes[0] if e.classes else "")
                        if op in ("replaces", "alters") and t.get("levels") and not t.get("power") and (e.id, r["anchor"]) in RULE57_TRADE_LEVELS:
                            found.append((min(t["levels"]), op, name))       # the lowest level of a trade that names its levels, for the features that the review of a batch names (Emotional Appeal: the bonus feat gained at 3rd level)
                        elif op in ("replaces", "alters") and cls and not t.get("levels") and not t.get("power"):
                            lv = table_level(class_table_levels(corpus, cls, class_cache), name, e.id)
                            if lv:
                                found.append((lv, op, name))
                    if found:
                        r["level"] = min(lv for lv, _o, _n in found)
                        r["notes"].append(f"level {r['level']} (ruling 57): " + ", ".join(f"{o} {n} (level {lv})" for lv, o, n in found))
        if (e.id, r["anchor"]) in LEVEL_NONE and r["level"] is not None:
            r["notes"].append(f"no level: print states none and the feature alters a part of a class feature (owner rulings 4 and 48); the reader would take {r['level']}")
            r["level"] = None
        if r["level"] is not None and r["level_import"] is not None and r["level"] != r["level_import"] and r["status"] != "hold" \
                and (e.id, r["anchor"]) not in decisions:
            r["status"] = "hold"
            r["notes"].append(f"level: corpus {ordinal(r['level_import'])}, print {ordinal(r['level'])}")
    # owner review of #338: the lead decides the two cases that a first read of print does not show
    if RULES["lostlevel"]:
        for r in rows:
            if r["listed"] and r["level"] is None and r["level_import"] is not None and r["status"] != "hold" and (e.id, r["anchor"]) not in decisions:
                r["status"] = "hold"
                r["notes"].append(f"level: the import had {ordinal(r['level_import'])} and print gives none (no lead, no trade that proves it): "
                                  "decide `print` (no level), or give it in `LEVEL_FROM_PRINT`")
    if RULES["choices"]:
        for i, r in enumerate(rows):
            nxt = rows[i + 1] if i + 1 < len(rows) else None
            if (r["listed"] and not r.get("parent") and (e.id, r["anchor"]) not in decisions and CHOICE_INTRO.search(r["print"] or "")
                    and nxt is not None and nxt["listed"] and not nxt.get("parent")):
                r["status"] = "hold"       # also a row that is a hold already: its note then says that the structure is one of the questions
                r["notes"].append(f"choices: the text says that the reader selects from what follows, and the next section `{nxt['anchor']}` is a listed feature: "
                                  "decide `sub-of:` for the options (rulings 15 and 34), or `list` on this feature if they are features")
    if e.id in OPENING_NOTES:
        rows[0]["notes"].append(OPENING_NOTES[e.id])
    for text in res.get("opening_dropped", []):
        rows[0]["notes"].append("opening note that print does not have dropped (ruling 10): \u201c" + " ".join(text.split()[:9]) + " \u2026\u201d")
    return {"rows": rows, "problems": problems, "by": by, "opening": res["opening"], "dropped": dropped,
            "opening_from_print": opening_from_print}


# The title that print sets over an archetype whose corpus title differs: a misspelling of the corpus title, kept until the owner decides (#540,
# batch of 2026-11-26: "Aquakinetcist" for "Aquakineticist", Aquatic Adventures p. 50). The entry's title and id stay as they are.
PRINT_TITLES = {
    "ref/arc-kineticist/aquakinetcist": "Aquakineticist",
    "ref/arc-fighter/lore-warden-pfs-field-guide": "Lore Warden",          # the corpus tells it from the Lore Warden of Ultimate Combat; print has the plain name (Pathfinder Society Field Guide p. 31)
}


# The corpus titles that are corrected to the printed ones (the id stays; the precedent is #283): `--write` puts the printed title in the entry.
TITLE_FIXES = {"ref/arc-kineticist/aquakinetcist": ("Aquakinetcist", "Aquakineticist")}


def ptitle(e: "Entry") -> str:
    return PRINT_TITLES.get(e.id, e.title)


# An entry whose `[[sources]]` page row names a page other than the one that print has the archetype on (the page rows follow print): cited page,
# printed page. `--compare` holds an entry that cites a wrong page and is not listed; `--write` puts the printed page in the row.
PAGE_FIXES = {
    "ref/arc-witch/invoker": ("14", "20"),
    "ref/arc-paladin/pearl-seeker": ("54", "53"),      # Aquatic Adventures: the archetype starts on page 53 (review of #346)          # Haunted Heroes Handbook: the Invoker is printed on page 20 (owner answer on #342)
}

# The Player Companions that set their titles in small capitals and give each archetype no box of its own (batches 6 to 9).
BATCH_B_BOOKS = ("psychic-anthology", "disciples-doctrine", "occult-origins", "arcane-anthology", "blood-of-the-coven")     # the lead reader of `LEAD_EXT` reads them (review of #344)
BATCH_B4_BOOKS = ("merchants-manifest", "champions-of-corruption")     # the lead reader of `LEAD_EXT` reads them (batch B4)
BATCH_B3_BOOKS = ("dirty-tactics-toolbox", "villain-codex", "weapon-masters-handbook", "melee-tactics-toolbox", "distant-realms")     # the lead reader of `LEAD_EXT` reads them (batch B3)
PLAYER_COMPANIONS = ("blood-of-the-ancients", "wilderness-origins", "legacy-of-the-first-world", "people-of-the-wastes", "healers-handbook", "psychic-anthology", "disciples-doctrine", "occult-origins", "arcane-anthology", "blood-of-the-coven",
                     "elemental-masters-handbook", "monster-hunters-handbook", "monster-summoners-handbook", "armor-masters-handbook", "cohorts-and-companions")

# The Player Companions that set their archetype titles in small capitals (a capital and its small capitals 5 units apart), and whose
# archetypes are followed by sections of the chapter of their own (feats, techniques, spells): any title ends the section of an archetype.
SMALL_CAP_BOOKS = ("blood-of-the-ancients", "blood-of-the-beast", "heroes-of-the-high-court", "martial-arts-handbook", "magic-tactics-toolbox", "potions-and-poisons", "heroes-from-the-fringe", "haunted-heroes-handbook", "antiheros-handbook", "blood-of-the-sea", "aquatic-adventures", "legacy-of-dragons", "plane-hoppers-handbook", "dirty-tactics-toolbox", "weapon-masters-handbook", "melee-tactics-toolbox", *BATCH_B4_BOOKS, "pathfinder-society-field-guide", "dragon-empires-primer", "qadira-jewel-of-the-east")
# ... and of these, the ones whose chapter titles or capitals stand above the usual top of the body (Blood of the Ancients keeps 88)
HIGH_TITLE_BOOKS = ("knights-of-the-inner-sea", "people-of-the-river", "giant-hunters-handbook", "kobolds-of-golarion", "people-of-the-stars", "champions-of-balance", "bastards-of-golarion", "dungeoneers-handbook", "the-harrow-handbook", "animal-archive", "blood-of-the-beast", "heroes-of-the-high-court", "martial-arts-handbook", "magic-tactics-toolbox", "haunted-heroes-handbook", "familiar-folio", "advanced-class-origins", "cohorts-and-companions", "dirty-tactics-toolbox", "weapon-masters-handbook", "melee-tactics-toolbox", *BATCH_B4_BOOKS)

# ---- Potions & Poisons, Construct Handbook, Magic Tactics Toolbox, Haunted Heroes Handbook, Heroes from the Fringe (one block of tables) ----
MISPRINTS.extend([
    ("ref/arc-cleric/divine-scourge", "and retributions", "and retribution",
     "the major hex is retribution (the corpus links it); print makes the name plural beside \"infected wounds\" and \"nightmares\" (Magic Tactics Toolbox p. 23)"),
    ("ref/arc-shifter/wild-effigy", "The enahncement increases", "The enhancement increases", "a transposition of letters (Construct Handbook p. 13)"),
    ("ref/arc-rogue/construct-saboteur", "can user her arcane prowess", "can use her arcane prowess", "a stray letter (Construct Handbook p. 12)"),
    ("ref/arc-druid/mantella", "the mantilla can never", "the mantella can never", "the name of the archetype, misspelled once in print (Potions and Poisons p. 4); the meaning is certain (owner ruling 9)"),
])
TRADE_RENAMES.update({
    ("ref/arc-alchemist/dimensional-excavator", "4th-level discovery"): "Discovery gained at 4th level",
    ("ref/arc-witch/havocker", "All 2nd-level and higher hexes"): "The witch's hexes from 2nd level on",
    ("ref/arc-occultist/construct-collector", "3rd-, 9th- and 15th-level focus powers"): "Focus power selected at 3rd level, 9th level, and 15th level",
    ("ref/arc-wizard/clocksmith", "5th-, 10th-, 15th-, and 20th-level bonus feats"): "Bonus feats gained at 5th, 10th, 15th, and 20th levels",
    ("ref/arc-wizard/first-world-caller", "10th- and 15th-level bonus feats"): "Bonus feats gained at 10th and 15th level",
    ("ref/arc-witch/venom-siphoner", "1st-level hex"): "Hex gained at 1st level",
    ("ref/arc-witch/venom-siphoner", "2nd-level hex"): "Hex gained at 2nd level",
    ("ref/arc-witch/venom-siphoner", "6th-level hex"): "Hex gained at 6th level",
    ("ref/arc-rogue/swamp-poisoner", "Trap sense (core rogue)"): "Trap sense",
    ("ref/arc-rogue/swamp-poisoner", "danger sense (unchained rogue)"): "Danger sense",
    ("ref/arc-investigator/toxin-codexer", "Alchemy and replaces"): "Alchemy",
    ("ref/arc-investigator/skeptic", "Investigator talent gained at 7th level"): "Investigator talent the skeptic would otherwise gain at 7th level",
    ("ref/arc-wizard/pact-wizard-hhh", "5th-, 10th-, 15th-, and 20th-level bonus feats"): "Bonus feats a wizard gains at 5th, 10th, 15th, and 20th level",
    ("ref/arc-psychic/terror-weaver", "11th- and 19th-level phrenic amplifications"): "Phrenic amplifications gained at 11th and 19th levels",
    ("ref/arc-psychic/terror-weaver", "15th-level phrenic amplification"): "Phrenic amplification gained at 15th level",
})
TRADE_OP_FIXES.update({
    ("ref/arc-investigator/toxin-codexer", "trapfinding"): "replaces",                              # "This modifies alchemy and replaces trapfinding and the investigator talent ..."
    ("ref/arc-investigator/toxin-codexer", "investigator talent gained at 3rd level"): "replaces",
})
TRADE_PROSE_BY.update({
    ("ref/arc-rogue/swamp-poisoner", "danger sense (unchained rogue)"): "poison-the-well",      # "An unchained rogue replaces danger sense instead." (ruling 28)
})
for _eid in (        # "This alters the rogue's class skills." (the Class Skills section stands before the first feature): stored without `by`
        "ref/arc-rogue/construct-saboteur", "ref/arc-medium/uda-wendo", "ref/arc-bloodrager/symbol-striker", "ref/arc-inquisitor/urban-infiltrator",
        "ref/arc-magus/spell-trapper"):
    TRADE_ADDITIONS.setdefault(_eid, []).append({"alters": "Class skills"})
TRADE_ADDITIONS.setdefault("ref/arc-slayer/spiritslayer", []).append({"alters": "Sneak attack", "feature": "sneak-attack"})    # "This talent alters the spiritslayer's sneak attack"
# "A cruorchymist doesn't gain the poison use, poison resistance, poison immunity, or swift poisoning class features." (Diminished Poisoning, Construct
# Handbook p. 12): a trade stated in the prose of its own feature (owner ruling 36); one trade each, `by` that feature (poison immunity is gained with poison resistance at 10th level, as the other alchemist archetypes store it)
TRADE_ADDITIONS.setdefault("ref/arc-alchemist/cruorchymist", []).extend(
    [{"replaces": "Poison use", "feature": "poison-use"}, {"replaces": "Poison resistance", "feature": "poison-resistance"},
     {"replaces": "Poison immunity", "feature": "poison-resistance"}, {"replaces": "Swift poisoning", "feature": "swift-poisoning"}])
for _name in ("Poison use", "Poison resistance", "Poison immunity", "Swift poisoning"):
    TRADE_PROSE_BY[("ref/arc-alchemist/cruorchymist", _name)] = "diminished-poisoning"
TRADE_LEVELS[("ref/arc-alchemist/cruorchymist", "Poison resistance")] = [2, 5, 8]
TRADE_LEVELS[("ref/arc-alchemist/cruorchymist", "Poison immunity")] = [10]
# the class skills and the alignment that the scaffold sections print ("This alters the cavalier's class skills.", "This alters the druid's alignment."): trades without `by`
for _eid in ("ref/arc-gunslinger/blatherskite", "ref/arc-alchemist/aquachymist", "ref/arc-spiritualist/drowned-channeler", "ref/arc-bloodrager/urban-bloodrager",
             "ref/arc-cavalier/constable", "ref/arc-hunter/urban-hunter"):
    TRADE_ADDITIONS.setdefault(_eid, []).append({"alters": "Class skills"})
for _eid in ("ref/arc-druid/planar-extremist", "ref/arc-investigator/ruthless-agent"):
    TRADE_ADDITIONS.setdefault(_eid, []).append({"alters": "Alignment"})
TRADE_ADDITIONS.setdefault("ref/arc-alchemist/winged-marauder", []).append({"replaces": "Disable Device, Sleight of Hand, and Use Magic Device as class skills"})
# ---- Black Markets, Plane-Hopper's Handbook, Blood of Shadows (batch of 2026-11-27) ----
LEVEL_FROM_PRINT[("ref/arc-sorcerer/umbral-scion", "diminished-spellcasting")] = (1, "ruling 50: alters the sorcerer's spellcasting (the whole spellcasting, a 1st-level class feature)")
TRADE_ADDITIONS.setdefault("ref/arc-paladin/dusk-knight", []).append({"alters": "Class skills"})       # "This alters the paladin's class skills." (Skills)
TRADE_RENAMES.update({
    ("ref/arc-sorcerer/umbral-scion", "1st-level bloodline power"): "Shadowstrike bloodline power",      # "This ability replaces the shadowstrike bloodline power."
    ("ref/arc-occultist/planar-harmonizer", "7th-level focus power"): "Focus power gained at 7th level",
    ("ref/arc-occultist/planar-harmonizer", "5th-level focus power"): "Focus power gained at 5th level",
})
# ---- Heroes of Golarion, Dungeoneer's Handbook, The Harrow Handbook, Pathfinder Society Field Guide, Technology Guide, Animal Archive, Dragon Empires Primer (layout pass of 2026-11-27) ----
LEVEL_FROM_PRINT[("ref/arc-cleric/iron-priest", "spontaneous-casting")] = (1, "ruling 48: the trade names the cleric's spontaneous casting, a 1st-level class feature that the table does not list (review of #356; as Crashing Wave and Rot Warden)")
LEVEL_FROM_PRINT[("ref/arc-oracle/seeker", "tinkering")] = (1, "print says \"at 1st level, a seeker adds half his oracle or sorcerer level\" (Pathfinder Society Field Guide p. 29): the level is stated in the sentence (rulings 4 and 51), as in the sorcerer's Seeker")
LEVEL_FROM_PRINT[("ref/arc-bard/speaker-of-the-palatine-eye", "spells")] = (1, "ruling 50: alters the bard's spells (the whole spellcasting, a 1st-level class feature)")
# Pathfinder Society Field Guide: Seeker and Scroll Scholar print their trades for each class in a sentence of its own ("For an oracle, this
# ability replaces the revelation gained at 3rd level."), which the app does not read as a trade sentence; the feature prints no other trade
# sentence, so `by` names it (owner ruling of 2026-11-24, #540: a trade whose `by` names a listed feature that prints no trade sentence is not drift)
TRADE_PROSE_BY.update({
    ("ref/arc-oracle/seeker", "Bonus skills from the oracle's mystery"): "tinkering",
    ("ref/arc-oracle/seeker", "Revelation gained at 3rd level"): "seeker-lore",
    ("ref/arc-oracle/seeker", "Revelation gained at 15th level"): "seeker-magic",
    ("ref/arc-sorcerer/seeker", "Eschew Materials"): "tinkering",
    ("ref/arc-sorcerer/seeker", "3rd-level bloodline power"): "seeker-lore",
    ("ref/arc-sorcerer/seeker", "15th-level bloodline power"): "seeker-magic",
    ("ref/arc-cleric/scroll-scholar", "One of the 1st-level granted powers from her domains - the character gets to choose which of her two 1st-level granted powers it replaces"): "diligent-student",
    ("ref/arc-cleric/scroll-scholar", "Channel energy damage boost at 5th level"): "secrets-revealed",
    ("ref/arc-wizard/scroll-scholar", "Diviner's fortune (if a diviner) or hand of the apprentice (if a universalist)"): "diligent-student",
    ("ref/arc-wizard/scroll-scholar", "5th-level bonus feat"): "secrets-revealed",
})
SLOT_PHRASE = ("The normal addition of a new 4th-level spell slot to the character's spells per day\u2014from this point on, the cleric or wizard has one fewer "
               "4th-level spell slot than other clerics or wizards")      # the whole phrase of the printed sentence names the trade (the checker reads the phrase to its end)
# the import splits the wizard's slot trade at the dash of the printed sentence; one trade with the printed words (ruling 22), as the cleric's
TRADE_RENAMES.update({
    ("ref/arc-wizard/scroll-scholar", "The normal addition of a new 4th-level spell slot; from this point on"): SLOT_PHRASE,
    ("ref/arc-cleric/scroll-scholar", "The normal addition of a new 4th-level spell slot to the character's spells per day"): SLOT_PHRASE,
})
TRADE_REMOVALS.setdefault("ref/arc-wizard/scroll-scholar", []).append(("replaces", "the wizard has one fewer 4th-level spell slot than other wizards"))
TRADE_ADDITIONS.setdefault("ref/arc-druid/goliath-druid", []).extend([      # "This ability replaces venom immunity and a thousand faces." (Giant Hunter's Handbook p. 21): the import stores no trade for them
    {"replaces": "Venom immunity", "feature": "venom-immunity"}, {"replaces": "A thousand faces", "feature": "a-thousand-faces"}])
LEVEL_FROM_PRINT[("ref/arc-druid/survivor", "diminished-spellcasting")] = (1, "ruling 50: alters the druid's spellcasting (the whole spellcasting, a 1st-level class feature)")
LEVEL_FROM_PRINT[("ref/arc-bard/averaka-arbiter", "inspire-teamwork")] = (3, "print says \"A 3rd-level Averaka arbiter can use his performance\" (Bastards of Golarion p. 15)")
LEVEL_FROM_PRINT[("ref/arc-rogue/carnivalist", "sneak-attack")] = (2, "print says \"A carnivalist gains this ability starting at 2nd level\" (Animal Archive p. 6): the archetype's sneak attack starts at 2nd level, not at the 1st level of the class table")
LEVEL_FROM_PRINT[("ref/arc-rogue/carnivalist", "pet-performance")] = (2, "print says \"At 2nd level, she gains the distraction bardic performance\" (Animal Archive p. 6): the first performance is gained at 2nd level, the level of the first rogue talent it replaces")
TRADE_RENAMES.update({
    ("ref/arc-fighter/swarm-fighter", "The bonus feat a fighter gains at first level"): "The bonus feat a fighter gains at first level, and can't be replaced at a later level",      # the printed sentence "This replaces the bonus feat a fighter gains at first level, and can't be replaced at a later level." (ruling 22)
    ("ref/arc-witch/ashiftah", "2nd-level hex"): "Hex gained at 2nd level",          # "This ability replaces the hex gained at 2nd level." (ruling 22)
    ("ref/arc-witch/ashiftah", "6th-level hex"): "Hex gained at 6th level",
    ("ref/arc-fighter/swarm-fighter", "The bonus combat feats the fighter normally receives at 2nd, 6th, 10th, 14th, and 18th levels"): "The bonus combat feats the fighter normally receives at those levels",      # "...replaces the bonus combat feats the fighter normally receives at those levels." (ruling 22)
    ("ref/arc-cavalier/huntmaster", "Cavalier bonus feats"): "A cavalier's standard bonus feats",      # "This ability replaces a cavalier's standard bonus feats." (ruling 22)
    ("ref/arc-barbarian/mad-dog", "2nd, 6th, 10th, 14th, and 18th level rage powers"): "Rage powers gained at 2nd, 6th, 10th, 14th, and 18th level",      # "This ability replaces the rage powers gained at 2nd, 6th, 10th, 14th, and 18th level." (ruling 22)
    ("ref/arc-magus/card-caster", "Spellstrike"): "and modifies spellstrike",      # owner ruling 58: "This ability replaces and modifies spellstrike." is ONE replaces trade of Spellstrike; the checker reads the phrase to its end (review of #356)
    ("ref/arc-rogue/scroll-scoundrel", "10th-level rogue talent"): "The scroll scoundrel's 10th-level rogue talent",      # "This ability replaces the scroll scoundrel's 10th-level rogue talent." (ruling 22)
    ("ref/arc-witch/dimensional-occultist", "2nd-level hex"): "Hex gained at 2nd level",          # "This ability replaces the witch's hex gained at 2nd level." (ruling 22)
    ("ref/arc-witch/dimensional-occultist", "8th-level hex"): "Hex gained at 8th level",
    ("ref/arc-witch/dimensional-occultist", "12th-level hex"): "Hex gained at 12th level",
})
MISPRINTS.append(
    ("ref/arc-paladin/combat-healer-squire", "temporary alleviating his suffering", "temporarily alleviating his suffering",
     "print has \"temporary alleviating\" for \"temporarily alleviating\" (Knights of the Inner Sea p. 20; owner ruling 9)"))
MISPRINTS.append(
    ("ref/arc-druid/goliath-druid", "she must selected from the Animal", "she must select from the Animal",
     "print has \"must selected\" for \"must select\" (Giant Hunter's Handbook p. 20; owner ruling 43, with an errata row)"))
MISPRINTS.append(
    ("ref/arc-fighter/swarm-fighter", "against the swam fighter's attacks", "against the swarm fighter's attacks",
     "print has \"swam fighter's attacks\" for \"swarm fighter's attacks\" (Kobolds of Golarion p. 23; owner ruling 9)"))
MISPRINTS.append(
    ("ref/arc-barbarian/savage-technologist", "Sense Motive Wis),", "Sense Motive (Wis),",
     "print has \"Sense Motive Wis)\" without the opening parenthesis (Technology Guide p. 13; owner ruling 9); the list also names Perception twice, as printed"))
MISPRINTS.append(
    ("ref/arc-fighter/lore-warden-pfs-field-guide", "negate a confirmation role for a critical hit", "negate a confirmation roll for a critical hit",
     "print has \"role\" where \"roll\" belongs (Pathfinder Society Field Guide p. 31; owner ruling 9)"))
# Blood of the Sea
TRADE_RENAMES.update({
    ("ref/arc-oracle/oceans-echo", "Bonus skills from the oracle's mystery"): "Additional class skills from her mystery",
    ("ref/arc-oracle/oceans-echo", "The bonus spells gained at 4th, 8th, 10th, 12th, and 14th levels from the oracle's mystery"): "Mystery bonus spells at these levels",
    ("ref/arc-witch/coral-witch", "8th-level hex"): "Hex gained at 8th level",
    ("ref/arc-vigilante/hidden-current", "2nd-level vigilante talent"): "The hidden current's 2nd-level vigilante talent",
})
# Antihero's Handbook: "Replaces: Ki pool, alters high jump" is one import row for two trades; "alters high jump" is an alters trade of "High jump"
# Discretion Specialist prints "This replaces trap sense (for a core rogue) or danger sense (for an unchained rogue)."
TRADE_RENAMES[("ref/arc-rogue/discretion-specialist", "Trap sense (for a core rogue)")] = "Trap sense"
TRADE_RENAMES[("ref/arc-rogue/discretion-specialist", "danger sense (for an unchained rogue)")] = "Danger sense"
TRADE_PROSE_BY[("ref/arc-rogue/discretion-specialist", "danger sense (for an unchained rogue)")] = "obfuscation"
TRADE_OP_FIXES[("ref/arc-monk/sin-monk", "alters high jump")] = "alters"
TRADE_RENAMES[("ref/arc-monk/sin-monk", "alters high jump")] = "High jump"
# the levels that review of #342 read from the middle of a feature (owner rulings 4 and 51)
LEVEL_FROM_PRINT.update({
    ("ref/arc-bard/disciple-of-the-forked-tongue", "serpent-of-the-mind"): (2, "print says \"at 2nd level and every 4 levels thereafter\" (Potions and Poisons p. 7): the level is stated inside the sentence (ruling 4)"),
    ("ref/arc-wizard/pact-wizard-hhh", "great-power-greater-expense"): (5, "print says \"At 5th level, the pact wizard chooses one oracle curse\" in its second sentence (Haunted Heroes Handbook p. 20)"),
    ("ref/arc-druid/toxicologist", "toxic-shaper"): (8, "ruling 51: print says \"At 8th level\" in the feature itself; it wins over the 4th level at which the druid gains wild shape"),
})

# ---- Monster Codex, Aquatic Adventures, Heroes of the Streets, Antihero's Handbook, Blood of the Sea (batch of 2026-11-26) ----
TRADE_RENAMES.update({
    ("ref/arc-barbarian/pack-rager", "2nd, 6th, 10th, 14th, and 18th level rage powers"): "Rage powers gained at 2nd, 6th, 10th, 14th, and 18th level",
    ("ref/arc-witch/bouda", "10th-level major hex"): "Major hex granted at 10th level",
    ("ref/arc-kineticist/aquakinetcist", "Basic hydrokinesis"): "Basic hydrokinesis as her basic utility talent",
})
# "This alters the paladin's armor proficiency and class skills." and "This alters spirit, spirit animal, and the shaman's class skills.": the class skills are a trade of their own, without `by` for the scaffold head
# Crowd Patron (Heroes of the Streets p. 20) prints "This ability alters witch's familiar." for a feature that says "She doesn't select a patron at 1st level": print wins, the
# corpus's trades for the patron are removed and the printed one is stored (an owner question in the pull request)
TRADE_ADDITIONS.setdefault("ref/arc-investigator/lamplighter", []).append({"alters": "Class skills"})       # "This alters the investigator's class skills." (the Skills section)
TRADE_ADDITIONS.setdefault("ref/arc-witch/alley-witch", []).append({"alters": "Class skills"})              # "This alters the witch's class skills." (Child of the Streets, a listed feature)
TRADE_PROSE_BY[("ref/arc-witch/alley-witch", "Class skills")] = "child-of-the-streets"
TRADE_REMOVALS.setdefault("ref/arc-witch/alley-witch", []).extend([("alters", "Patron"), ("alters", "patron spells")])
TRADE_ADDITIONS.setdefault("ref/arc-witch/alley-witch", []).append({"alters": "Witch's familiar", "feature": "witch-s-familiar"})
for _eid in ("ref/arc-paladin/pearl-seeker", "ref/arc-shaman/deep-shaman"):
    TRADE_ADDITIONS.setdefault(_eid, []).append({"alters": "Class skills"})
LEVEL_FROM_PRINT.update({
    # owner ruling 50: altering the whole spellcasting of the class is altering a whole 1st-level class feature; the cleric's spontaneous casting is a 1st-level feature
    # that its table does not list, as the druid's (ruling 48): an owner question in the pull request
    ("ref/arc-cleric/channeler-of-the-unknown", "spells"): (1, "ruling 50: alters the cleric's spells (the whole spellcasting, a 1st-level class feature)"),
    ("ref/arc-paladin/vindictive-bastard", "no-aura"): (1, "owner rulings 50 and 57: it alters the paladin's aura (a whole 1st-level class feature, the aura of good), and print states no level"),
    ("ref/arc-antipaladin/fearmonger", "panicked"): (12, "ruling 47: print says in Frightening Cruelty \"At 12th level, the fearmonger gains the panicked cruelty\": a fixed ability that comes with no choice"),
    ("ref/arc-druid/planar-extremist", "spells"): (1, "ruling 50: alters the druid's spells (the whole spellcasting, a 1st-level class feature)"),
    ("ref/arc-magus/eldritch-archer", "arcane-pool"): (5, "print says \"choices of weapon special abilities to apply with arcane pool at 5th level\" in the feature itself (Heroes of the Streets p. 11): the level that the feature states wins over the 1st level of the arcane pool it modifies (ruling 51); an owner question in the pull request"),
    ("ref/arc-bard/dragon-yapper", "versatile-performance"): (2, "print says \"A dragon yapper must choose sing at 2nd level\" (Monster Codex p. 128): the level is stated inside the sentence (ruling 4)"),
    ("ref/arc-druid/ancient-guardian", "patience-of-nature"): (2, "print says \"Instead, at 2nd level, an ancient guardian adds\" (Monster Codex p. 140): the level of the ability, not that of wild empathy (ruling 51)"),
    ("ref/arc-druid/ancient-guardian", "dispel-hostility"): (3, "print says \"Instead, at 3rd level, she can channel stored spell energy\" (Monster Codex p. 140): the level of the ability, not that of spontaneous casting (ruling 51)"),
})


# ---- Batch B4: Merchant's Manifest, Champions of Corruption ----
for _eid in ("ref/arc-paladin/knight-of-coins", "ref/arc-inquisitor/oathkeeper"):
    TRADE_ADDITIONS.setdefault(_eid, []).append({"alters": "Class skills"})     # "This alters the paladin's class skills and skill ranks per level." (the Class Skills section before the first feature)
LEVEL_FROM_PRINT[("ref/arc-antipaladin/dread-vanguard", "beacon-of-evil")] = (4, "owner ruling 57: replaces the spells class feature, which the antipaladin gains at 4th level (the spells per day begin there), and print's first step of the ability is \"At 4th level and every 4 levels thereafter\"")
TRADE_RENAMES[("ref/arc-paladin/knight-of-coins", "3rd-, 9th-, and 15th-level mercies")] = "The mercies gained at 3rd, 9th, and 15th levels"


# ---- Batch B3: Dirty Tactics Toolbox, Villain Codex, Weapon Master's Handbook, Melee Tactics Toolbox, Distant Realms ----
TRADE_RENAMES.update({
    ("ref/arc-swashbuckler/rondelero-swashbuckler", "Derring-do"): "The derring-do deed",
})
TRADE_ADDITIONS.setdefault("ref/arc-ranger/realm-wanderer", []).append({"alters": "Class skills"})     # "This alters the ranger's class skills." (the Class Skills section before the first feature)
TRADE_ADDITIONS.setdefault("ref/arc-ninja/hunting-serpent", []).append({"alters": "Class skills"})     # "This ability alters the ninja's class skills." (the Class Skills section before the first feature)
for _eid, _cls in (("ref/arc-monk/hellcat", "monk"), ("ref/arc-fighter/relic-master", "fighter"), ("ref/arc-fighter/varisian-free-style-fighter", "fighter")):
    TRADE_ADDITIONS.setdefault(_eid, []).append({"alters": "Class skills"})     # "This alters the %s's class skills." (the Class Skills section before the first feature)
# Bloody-Knuckled Rowdy (Melee Tactics Toolbox p. 13): "does not gain damage reduction" is a replaced class feature (ruling 36), stated in the prose of Bloody Knuckles
TRADE_ADDITIONS["ref/arc-bloodrager/bloody-knuckled-rowdy"] = [{"replaces": "Damage reduction", "feature": "damage-reduction"}]
TRADE_PROSE_BY[("ref/arc-bloodrager/bloody-knuckled-rowdy", "Damage reduction")] = "bloody-knuckles"
LINK_DROP.update({("ref/arc-medium/voice-of-the-void", "surge"), ("ref/arc-medium/voice-of-the-void", "blasphemy")})     # the monster rule "surge" and the spell blasphemy, for the medium's spirit surge and the archetype's ability
for _a in ("surge-of-the-void", "blasphemy"):
    EXTRA_LINKS[("ref/arc-medium/voice-of-the-void", _a)] = [("spirit surge", "ref/class/medium#spirit-surge")]
TRADE_RENAMES[("ref/arc-alchemist/vaultbreaker", "Brew Potion")] = "The Brew Potion bonus feat"
TRADE_RENAMES[("ref/arc-alchemist/vaultbreaker", "Throw Anything")] = "The Throw Anything bonus feat"
LEVEL_FROM_PRINT[("ref/arc-alchemist/mnemostiller", "natural-empath")] = (2, "print says \"He gains infusion as a bonus discovery at 2nd level\"")
for _a, _lv, _col in (("cryptic-omens", 1, "1st-2nd"), ("seek-guidance", 1, "1st-2nd"), ("greater-omens", 3, "3rd-4th"), ("specialized-knowledge", 5, "5th-6th"),
                      ("clairvoyance-clairaudience", 7, "7th-8th"), ("scrying", 11, "11th-12th"), ("mirror-casting", 13, "13th-14th")):
    LEVEL_FROM_PRINT[("ref/arc-witch/mirror-witch", _a)] = (_lv, f"the Special column of the Patron Mirror table lists the ability at {_col} level (Villain Codex p. 153)")
MISPRINTS.append(
    ("ref/arc-warpriest/sixth-wing-bulwark", "This replaced the bonus feat", "This replaces the bonus feat",
     "print has \"replaced\" where \"replaces\" belongs (Distant Realms p. 32; owner ruling 9)"))


def configure_book(book: str) -> None:
    """The layout switches of a book (the leaf tool `feature-prose-540-leaves.py` sets the same ones)."""
    ERRATA_CTX["book"] = book
    PAGE_OFFSET[0] = 2 if book == "inner-sea-combat" else 1
    CHAPTER_END[0] = 47 if book == "inner-sea-combat" else 0
    PAGE_SKIP[:] = [(16, 23), (26, 999)] if book == "legacy-of-dragons" else []
    LOWERCASE_CONTINUES["on"] = BULLETS["on"] = ITALIC_FIRST["on"] = CITE_EXT["on"] = LEAD_EXT["on"] = book in ("inner-sea-magic", "inner-sea-intrigue", "inner-sea-combat")
    LEAD_EXT["on"] = LEAD_EXT["on"] or book in BATCH_B_BOOKS or book in BATCH_B3_BOOKS or book in BATCH_B4_BOOKS or book in ("heroes-of-the-darklands", "legacy-of-dragons", "familiar-folio", "advanced-class-origins", "armor-masters-handbook", "cohorts-and-companions",
                                                                                                  "elemental-masters-handbook", "monster-hunters-handbook", "monster-summoners-handbook")
    OCR["on"] = NO_STYLE["on"] = book == "inner-sea-combat" or book in OCR_SETS
    MC_TITLES["on"] = book == "monster-codex"
    SKIP_FAMILY["fam"] = "Dax" if book == "heroes-of-golarion" else ""
    SKIP_BANNERS["pages"] = PFSFG_BANNERS if book == "pathfinder-society-field-guide" else {}
    PAREN_SNAP["on"] = book in ("dungeoneers-handbook", "animal-archive", "giant-hunters-handbook", "kobolds-of-golarion", "people-of-the-stars", "champions-of-balance", "bastards-of-golarion", "knights-of-the-inner-sea", "people-of-the-river")
    ITALIC_JOIN["on"] = book in ("aquatic-adventures", "heroes-of-the-streets", "antiheros-handbook", "blood-of-the-sea")
    global OCR_PHRASES, OCR_JOINED, OCR_ITALICS
    OCR_BOOK["name"] = book
    OCR_PHRASES, OCR_JOINED, OCR_ITALICS = OCR_SETS.get(book, ISC_OCR)
    OCR_GLUE["on"] = book in OCR_SETS
    OCR_TITLES["on"] = book in ("dungeoneers-handbook", "the-harrow-handbook", "technology-guide", "animal-archive", "giant-hunters-handbook", "kobolds-of-golarion", "people-of-the-stars", "champions-of-balance", "bastards-of-golarion", "knights-of-the-inner-sea", "people-of-the-river")
    TITLE_CONTAINS["on"] = book == "heroes-of-golarion"
    ARCHETYPE_CAPS["on"] = book == "heroes-of-the-darklands"
    FRAGMENT_TITLES["on"] = book == "armor-masters-handbook"
    LOWERCASE_CONTINUES["on"] = LOWERCASE_CONTINUES["on"] or book == "armor-masters-handbook"
    LIST_CONTINUES["on"] = book in ("potions-and-poisons", "black-markets")
    BULLETS["on"] = BULLETS["on"] or book in ("potions-and-poisons", "black-markets")           # the Toxin Codexer's Modify Toxin prints bullet lists (ruling 45, review of #342)
    OUTER_TAB["on"] = book in ("construct-handbook", "technology-guide", "qadira-jewel-of-the-east")
    OUTER_TAB_REACH["at"] = 330 if book in ("technology-guide", "qadira-jewel-of-the-east") else 340
    TAB_LEFT["min"], TAB_LEFT["title"] = (780, 15) if book == "aquatic-adventures" else ((0, 15) if book in ("dungeoneers-handbook", "heroes-of-golarion", "qadira-jewel-of-the-east") else (0, 16))
    PAGE_GEOMETRY["on"] = book in ("inner-sea-magic", "inner-sea-intrigue", "inner-sea-combat", "construct-handbook", "aquatic-adventures", "distant-realms", "technology-guide", "qadira-jewel-of-the-east")
    MARGIN_CAPTIONS["on"] = CAPTIONS["on"] = book in ("inner-sea-magic", "inner-sea-intrigue", "inner-sea-combat")
    BOX_TITLES["titles"] = frozenset(squash(t) for t in BOXES_OF_BOOK.get(book, ()))
    BOX_LORE["titles"] = frozenset(squash(t) for t in LORE_BOXES_OF_BOOK.get(book, ()))
    BOX_TO_END["on"] = book == "psychic-anthology"
    SKIP_TABLES["on"] = book == "advanced-race-guide"
    UPPER_HEAD_ENDS["on"] = book == "villain-codex"
    ILLUSTRATED["on"] = book in ("advanced-class-guide", "advanced-race-guide", "adventurers-guide", "ultimate-wilderness",
                                 "horror-adventures", "planar-adventures", "inner-sea-magic", "inner-sea-intrigue", "inner-sea-combat", "construct-handbook",
                                 "heroes-of-the-darklands", "legacy-of-dragons", "familiar-folio", "advanced-class-origins", "cohorts-and-companions",
                                 "dirty-tactics-toolbox", "melee-tactics-toolbox", "villain-codex")
    ART_INDENT["on"] = book in ("dirty-tactics-toolbox", "melee-tactics-toolbox", "villain-codex")
    ART_RUNS["on"] = book in ("black-markets", "blood-of-shadows")
    SECTION_STOPS["on"] = book in ("adventurers-guide", "ultimate-wilderness", "horror-adventures", "planar-adventures")
    ANY_TITLE_ENDS["on"] = book in SMALL_CAP_BOOKS or book in PLAYER_COMPANIONS or book in ("monster-codex", "advanced-class-origins", "black-markets", "blood-of-shadows", "dungeoneers-handbook", "heroes-of-golarion", "the-harrow-handbook", "technology-guide", "animal-archive", "giant-hunters-handbook", "kobolds-of-golarion", "people-of-the-stars", "champions-of-balance", "bastards-of-golarion", "knights-of-the-inner-sea", "people-of-the-river")
    STAYS_EXTRA["set"] = frozenset({"discoveries"}) if book == "blood-of-shadows" else frozenset()
    SMALL_CAP_TITLES["on"] = book in SMALL_CAP_BOOKS or book in PLAYER_COMPANIONS
    CHAPTER_TITLES["on"] = book in PLAYER_COMPANIONS and book != "blood-of-the-ancients"
    # a title in small capitals and a chapter title can stand higher than the body of the other books (Heroes of the High Court p. 29: capital at 86; Martial Arts Handbook p. 18: chapter title at 70; the running heads stand at 13-29)
    global BODY_TOP
    BODY_BOTTOM_FORCE[0] = BODY_BOTTOM_BOOKS.get(book, 0)
    BODY_TOP = (BODY_CAP_TOP if book in HIGH_TITLE_BOOKS else 88, BODY_BOTTOM_BOOKS.get(book, BODY_TOP[1]))


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    title = publication_title(corpus, book)
    configure_book(book)
    pdf = find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = load_book(book_xml(pdf, Path(args.cache)))
    entries = load_entries(corpus, book, args.only)
    old_rows = read_tsv(tsv_path(corpus, book))
    old_props = read_proposals(proposals_path(corpus, book))
    decisions = read_decisions(corpus, book)
    edits = read_edits(corpus, book)
    adds = read_adds(corpus, book)
    stops = {squash(ptitle(x)) for x in entries} | CLASS_TITLES | UNTYPED_ARCHETYPE_TITLES
    whole = None
    done = {e.id for e in entries if e.converted}
    redo = {e.id for e in entries if not e.converted}
    rows: list[dict] = [r for r in old_rows if r["entry"] in done or r["entry"] not in redo]
    props: dict[str, dict] = {k: v for k, v in old_props.items() if k not in redo and k not in done}
    for e in entries:
        if e.converted:
            continue
        page = int(e.page) if e.page.isdigit() else None
        top = max(bk.pages)
        if page is None:
            # no page cited: the title must occur once in the book
            if whole is None:
                whole = read_blocks(bk, 1, top)
            hits = [b for b in whole if b.kind == "title" and squash(b.plain()) in (squash(ptitle(e)), squash(ptitle(e)) + "archetype")]
            if len(hits) != 1:
                rows.append(entry_hold_row(e, f"no page cited, and the title is printed {len(hits)} times"))
                continue
            section = find_section(whole, ptitle(e), stops)
        else:
            blocks = read_blocks(bk, max(1, page + PAGE_OFFSET[0] - 3), min(page + PAGE_OFFSET[0] + 4, top))
            section = find_section(blocks, ptitle(e), stops)
        if section is None and page is not None:
            # the cited page is wrong (Haunted Heroes Handbook: the Invoker is cited on page 14 and printed on page 20): the title is looked for in the whole book; the TSV and the printed-sentence file read the printed page, the entry's `page` row is a data fix
            if whole is None:
                whole = read_blocks(bk, 1, top)
            section = find_section(whole, ptitle(e), stops)
            # a hold until the entry's page row is a decided data fix (`PAGE_FIXES`): the fallback found the title elsewhere (review of #342)
            if section is not None and PAGE_FIXES.get(e.id) != (e.page, str(section[0].page)):
                rows.append(entry_hold_row(e, f"the entry cites page {page}; the title is printed on page {section[0].page}"))
                continue
        if section is None:
            rows.append(entry_hold_row(e, f"title not found near page {page}"))
            continue
        LINK_CTX["title"] = e.title
        res = compare_entry(e, section, bk)
        res["decisions"] = decisions
        res["edits"] = edits
        res["adds"] = adds
        fin = finalize(e, res)
        if book in PRINTINGS and fin["rows"]:
            fin["rows"][0]["notes"].append(f"print: {PRINTINGS[book]}")
        old = {(r["entry"], r["anchor"]): r for r in old_rows if r["entry"] == e.id}
        entry_rows, entry_props = rows_of(e, fin, old, old_props.get(e.id))
        rows += entry_rows
        props[e.id] = entry_props
    rows.sort(key=lambda r: (r["entry"], int(r.pop("_n", 0))))
    write_tsv(tsv_path(corpus, book), rows)
    write_proposals(proposals_path(corpus, book), props)
    summarize(rows, props)
    if OCR["on"] and not args.only and len(redo) == len(entries):      # every entry was read from print (a run over converted entries reads nothing)
        dead = dead_ocr_patterns()
        if dead:
            print("error: OCR patterns that matched nothing (the text layer spells the words another way):", file=sys.stderr)
            for d in dead:
                print(f"  {d}", file=sys.stderr)
            return 1
    return 0


def entry_hold_row(e: Entry, why: str) -> dict:
    return {"entry": e.id, "feature": "", "anchor": "", "listed": "no", "level": "", "source": "",
            "status": "hold", "note": why, "page": e.page, "span_sha256": sha(e.body), "_n": 0}


def rows_of(e: Entry, fin: dict, old: dict, old_props: dict | None) -> tuple[list[dict], dict]:
    """The TSV rows and the proposals of one entry. A feature with a hand text (`edit`) keeps it while
    its span and print text are unchanged."""
    rows, feats = [], []
    hold = "; ".join(fin["problems"])
    for n, r in enumerate(fin["rows"]):
        prev = old.get((e.id, r["anchor"]))
        edit = None
        status = r["status"]
        if prev and prev["status"] == "hold" and prev["note"].startswith("checker:") and prev["span_sha256"] == r["span"] \
                and not FORGET_CHECKER_HOLDS:
            status, r["notes"] = "hold", [prev["note"]]
        if prev and prev["status"] == "edit" and prev["span_sha256"] == r["span"] and old_props:
            for f in old_props.get("feature", []):
                if f["anchor"] == r["anchor"] and f.get("edit") is not None and f.get("print") == r["print"]:
                    edit, status, r["notes"] = f["edit"], "edit", list(r["notes"]) + ["hand-edited text"]
        rows.append({
            "entry": e.id, "feature": r["head"], "anchor": r["anchor"], "listed": "yes" if r["listed"] else "no",
            "level": "" if r["level"] is None or not r["listed"] else r["level"],
            "source": "" if status == "hold" else ("draft" if status == "draft" else ("edit" if status == "edit" else "print")),
            "status": status, "note": "; ".join(r["notes"]), "page": r["page"], "span_sha256": r["span"], "_n": n,
        })
        f = {"anchor": r["anchor"], "head": r["head"], "listed": r["listed"], "print": r["print"]}
        if r.get("parent"):
            f["parent"] = r["parent"]
        if r.get("import_trades"):
            f["import_trades"] = r["import_trades"]
        if r["level"] is not None and r["listed"]:
            f["level"] = r["level"]
        if edit is not None:
            f["edit"] = edit
        feats.append(f)
    for r in fin.get("dropped", []):
        rows.append({"entry": e.id, "feature": r["head"], "anchor": r["anchor"], "listed": "no", "level": "", "source": "",
                     "status": "print", "note": "; ".join(r["notes"]), "page": r["page"], "span_sha256": r["span"],
                     "_n": 1000 + len(rows)})
    if not hold:
        hold = next((r["note"] for r in rows if r["status"] == "hold" and r["note"].startswith("checker:")), "")
    prop = {"id": e.id, "hold": hold, "opening": fin["opening"], "feature": feats}
    if fin.get("opening_from_print"):
        prop["opening_from_print"] = True
    return rows, prop


def summarize(rows: list[dict], props: dict) -> None:
    c = Counter(r["status"] for r in rows)
    print("rows:", dict(c))
    held = {r["entry"] for r in rows if r["status"] == "hold"}
    held |= {k for k, v in props.items() if v.get("hold")}
    print(f"entries with a hold: {len(held)}")


# ---- --write --------------------------------------------------------------------------------------------

def feature_text(f: dict, status: str) -> str:
    return f["edit"] if status == "edit" and f.get("edit") is not None else f["print"]


def convertible(e: Entry, rows: list[dict], prop: dict | None) -> str | None:
    """None when the entry can be converted, else the reason it cannot."""
    if not rows:
        return "not compared yet"
    if prop is None:
        return "no proposals"
    if prop.get("hold"):
        return prop["hold"]
    bad = [r for r in rows if r["status"] not in WRITABLE]
    if bad:
        return "undecided or held: " + ", ".join(r["feature"] or r["note"] for r in bad)
    return None


def edit_front(front: str, feats: list[dict], by: dict[int, list[str]], n_trades: int, added: list[dict] | None = None,
               skip: set[int] = frozenset()) -> str:
    lines = front.split("\n")
    out, in_fields, in_trades, k, orig = [], False, False, 0, 0
    listed = [f for f in feats if f["listed"]]
    for ln in lines:
        if ln.strip() == "[fields]":
            in_fields = True
        if in_fields and re.match(r'kind = "archetype"\s*$', ln):
            out.append(ln)
            if listed:
                items = []
                for f in listed:
                    lv = f", level = {f['level']}" if f.get("level") is not None else ""
                    items.append(f'  {{ anchor = "{f["anchor"]}"{lv} }},')
                out.append("features = [")
                out += items
                out.append("]")
            continue
        if in_fields and re.match(r"trades = \[\s*$", ln):
            in_trades = True
            out.append(ln)
            continue
        if in_trades:
            if ln.strip() == "]":
                in_trades = False
                for t in added or []:
                    op, name = trade_name(t)
                    extra = "".join(f', {key} = "{t[key]}"' for key in ("feature",) if key in t)
                    anchors = ", ".join(f'"{a}"' for a in by.get(k, []))
                    out.append(f'  {{ {op} = "{name}"{extra}' + (f", by = [{anchors}]" if anchors else "") + " },")
                    k += 1
            elif ln.strip().startswith("{"):
                m = re.match(r"^(\s*\{.*?) \},?\s*$", ln)
                if not m:
                    raise ValueError(f"trade line not understood: {ln}")
                if orig in skip:
                    orig += 1
                    continue
                if by.get(k):
                    anchors = ", ".join(f'"{a}"' for a in by[k])
                    ln = f"{m.group(1)}, by = [{anchors}] }},"
                k += 1
                orig += 1
        out.append(ln)
    if k != n_trades - len(skip) + len(added or []):
        raise ValueError(f"{k} trade lines, want {n_trades - len(skip) + len(added or [])}")
    return "\n".join(out)


# A head that print sets in capitals as the title of a box is written in title case, like the other boxes (Opus review of batch 4)
HEAD_REWRITES = {
    # Legacy of the First World p. 19 (ruling 41): the printed heads of the evolutions that only twinned summoners' eidolons take
    ("ref/arc-summoner/twinned-summoner", "twinned-eidolon-evolutions"): "Evolutions",
    ("ref/arc-summoner/twinned-summoner", "shared-evolution"): "Shared Evolution (Su)",
    ("ref/arc-summoner/twinned-summoner", "extra-feat"): "Extra Feat (Ex)",
    ("ref/arc-summoner/twinned-summoner", "shared-slot"): "Shared Slot (Su)",
    ("ref/arc-unchained-summoner/twinned-summoner", "twinned-eidolon-evolutions"): "Evolutions",
    ("ref/arc-unchained-summoner/twinned-summoner", "shared-evolution"): "Shared Evolution (Su)",
    ("ref/arc-unchained-summoner/twinned-summoner", "extra-feat"): "Extra Feat (Ex)",
    ("ref/arc-unchained-summoner/twinned-summoner", "shared-slot"): "Shared Slot (Su)",
    ("ref/arc-summoner/leshy-caller", "plant-eidolon-subtype"): "Plant Eidolon Subtype",
    ("ref/arc-unchained-summoner/leshy-caller", "plant-eidolon-subtype"): "Plant Eidolon Subtype",
}


# ---- Blood of the Beast, Heroes of the High Court, Martial Arts Handbook (one block, so that the lanes of #540 do not collide) ----
MISPRINTS.extend([
    ("ref/arc-inquisitor/ravener-hunter", "She cannot cast 2 with the", "She cannot cast spells with the",
     "print has the digit 2 where \"spells\" belongs (Blood of the Beast p. 5); the corpus has \"spells\""),
    ("ref/arc-ranger/fortune-finder", "the fortune-seeker's highest", "the fortune-finder's highest",
     "the archetype is the fortune-finder; the same paragraph says \"fortune-finder\" (Blood of the Beast p. 30)"),
    ("ref/arc-skald/war-painter", "A war painter cab apply", "A war painter can apply", "a letter b for an n"),
    ("ref/arc-ranger/poison-darter", "the poison dart can choose", "the poison darter can choose",
     "the archetype is the poison darter; the same feature says \"poison darter\" throughout (Blood of the Beast p. 9)"),
])
CONTEXT_LINKS.update({
    ("ref/arc-druid/swarm-monger", "swarm"): "gains the swarm",
    ("ref/arc-inquisitor/suit-seeker", "Fate"): "or the Fate",          # the import links "the Fate, Fervor, or Illumination inquisition" (The Harrow Handbook p. 22), not the Fate subdomain before it
    # review of #351: the link of the import belongs on the word that print marks, not on the first one of the text
    ("ref/arc-sorcerer/sorcerer-of-sleep", "arcane"): "The arcane",                # "The arcane and dreamspun bloodlines" (Black Markets p. 26), not "her arcane power"
    ("ref/arc-sorcerer/umbral-scion", "Shadow"): "have the shadow",                # "must have the shadow bloodline" (Blood of Shadows p. 19), not "potent shadow heritage"
})
# the print head of a section that the book sets in small capitals comes out in mixed case ("vesteD powers"): written as the book titles it
HEAD_REWRITES.update({
    ("ref/arc-monk/invested-regent", "vested-powers"): "Vested Powers",
    ("ref/arc-monk/invested-regent", "2nd-level-vested-powers"): "2nd-Level Vested Powers",
    ("ref/arc-monk/invested-regent", "6th-level-vested-powers"): "6th-Level Vested Powers",
    ("ref/arc-monk/invested-regent", "10th-level-vested-powers"): "10th-Level Vested Powers",
    ("ref/arc-monk/invested-regent", "14th-level-vested-powers"): "14th-Level Vested Powers",
    ("ref/arc-monk/invested-regent", "18th-level-vested-powers"): "18th-Level Vested Powers",
})
for _eid in (        # "This alters the cavalier's class skills." (the Class Skills section stands before the first feature): stored without `by`
        "ref/arc-cavalier/first-mothers-fang", "ref/arc-witch/jinx-witch", "ref/arc-alchemist/royal-alchemist", "ref/arc-fighter/high-guardian",
        "ref/arc-gunslinger/thronewarden", "ref/arc-occultist/silksworn", "ref/arc-brawler/battle-dancer", "ref/arc-fighter/spear-fighter",
        "ref/arc-medium/medium-of-the-master"):
    TRADE_ADDITIONS.setdefault(_eid, []).append({"alters": "Class skills"})
TRADE_RENAMES.update({
    ("ref/arc-bard/buccaneer", "Bardic knowledge"): "bardic knowledge",
    ("ref/arc-bard/buccaneer", "Suggestion"): "suggestion",
    ("ref/arc-bard/buccaneer", "Lore master"): "lore master",
    ("ref/arc-bard/buccaneer", "Mass suggestion"): "mass suggestion",
    ("ref/arc-fighter/corsair", "The fighter's 2nd-level bonus feat"): "the fighter's 2nd-level bonus feat",
    ("ref/arc-fighter/corsair", "Armor training"): "armor training",
    ("ref/arc-fighter/corsair", "The fighter's 6th-level bonus feat"): "the fighter's 6th-level bonus feat",
    ("ref/arc-ranger/freebooter", "Favored enemy"): "favored enemy",
    ("ref/arc-ranger/freebooter", "Hunter's bond"): "hunter's bond",
    ("ref/arc-ranger/freebooter", "Woodland stride"): "woodland stride",
    ("ref/arc-rogue/smuggler", "Trapfinding"): "trapfinding",
    ("ref/arc-rogue/smuggler", "Evasion"): "Evasion",
    ("ref/arc-rogue/smuggler", "Trap sense"): "trap sense",
})
TRADE_RENAMES.update({
    ("ref/arc-witch/jinx-witch", "2nd-level hex"): "Witch's hex normally gained at 2nd level",
    ("ref/arc-witch/jinx-witch", "6th-level hex"): "Hex normally gained at 6th level",
    ("ref/arc-witch/jinx-witch", "10th-level hex"): "Major hex gained at 10th level",
    ("ref/arc-swashbuckler/courser", "4th-level bonus feat"): "Bonus feat gained at 4th level",
    ("ref/arc-swashbuckler/courser", "Opportune parry and riposte"): "Opportune parry and riposte deeds",
    ("ref/arc-swashbuckler/courser", "Superior feint"): "Superior feint deed",
    ("ref/arc-swashbuckler/courser", "Bleeding wound"): "Bleeding wound deed",
    ("ref/arc-gunslinger/thronewarden", "Startling shot deed"): "Startling shot",
    ("ref/arc-gunslinger/thronewarden", "Bleeding wound deed"): "Bleeding wound",
    ("ref/arc-oracle/inerrant-voice", "The bonus spells gained at 2nd, 4th, 8th, and 14th levels from the oracle's mystery"):
        "Bonus spells at those levels gained from the oracle's mystery",
})



def convert_text(e: Entry, prop: dict, rows: list[dict]) -> str:
    status = {r["anchor"]: r["status"] for r in rows if r["anchor"]}
    feats = prop.get("feature", [])          # an entry whose every head is not printed (a section of the opening only) has none
    full = [dict(f, print=feature_text(f, status.get(f["anchor"], "print"))) for f in feats]
    by, problems = assign_by(effective_trades(e), with_children(full), opening_texts(full, prop.get("opening", [])))
    if problems:
        raise ValueError("; ".join(problems))
    probe = {namekey(f["head"]) for f in feats}
    opening, _ = parse_import(e.body, probe)
    parts = ["\n".join(b) for i, b in enumerate(opening) if i not in unprinted_notes(opening, prop.get("opening", []))]
    parts = [final_citations(o, e.id) for o in parts]
    if prop.get("opening_from_print"):
        parts = list(prop["opening"])
    for f in feats:
        depth, up = 0, f
        while up.get("parent"):
            depth += 1
            up = next((x for x in feats if x["anchor"] == up["parent"]), {})
        head = HEAD_REWRITES.get((e.id, f["anchor"]), f["head"])
        if not f["listed"] and depth == 0 and DASH_KEY.fullmatch(f["head"]):
            depth = 1                       # owner ruling 53: an option "Aberrant\u2014Squeezer (Ex)" is an unlisted `###` section
        parts.append(f"{'#' * (2 + depth)} {re.sub(r'(?<!\\)([*_])', r'\\\1', head)} {{#{f['anchor']}}}")
        text = feature_text(f, status.get(f["anchor"], "print"))
        parts += [p for p in text.split("\n\n") if p.strip()]
    front = edit_front(e.front, feats, by, len(trades_of(e)), TRADE_ADDITIONS.get(e.id), dropped_trade_indices(e))
    if e.id in TITLE_FIXES:
        front = front.replace(f'title = "{TITLE_FIXES[e.id][0]}"', f'title = "{TITLE_FIXES[e.id][1]}"', 1)
    if e.id in PAGE_FIXES:
        front = front.replace(f'page = "{PAGE_FIXES[e.id][0]}"', f'page = "{PAGE_FIXES[e.id][1]}"', 1)
    for (eid, old), anchor in TRADE_RELINKS.items():
        if eid == e.id:
            front = re.sub(r'^(\s*\{ \w+ = "' + re.escape(old) + r'", feature = ")[^"]*"', r"\g<1>" + anchor + '"', front, count=1, flags=re.M)
    for old in TRADE_UNLINKS.get(e.id, []):
        front = re.sub(r'^(\s*\{ \w+ = "' + re.escape(old) + r'")(?:, feature = "[^"]*")?(?:, levels = \[[^\]]*\])?',
                       r"\1", front, count=1, flags=re.M)
    for (eid, name), op in TRADE_OP_FIXES.items():
        if eid == e.id:
            other = "alters" if op == "replaces" else "replaces"
            front = front.replace(f'{other} = "{name}"', f'{op} = "{name}"', 1)
    for (eid, old), new in TRADE_RENAMES.items():
        if eid == e.id:
            front = front.replace(f'"{old}"', f'"{new}"', 1)
    for (eid, name), link in TRADE_LINKS.items():
        if eid == e.id:
            feat, lv, *power = link
            front = front.replace(f'"{name}"', f'"{name}", feature = "{feat}", levels = {lv}' + (f', power = "{power[0]}"' if power else ""), 1)
    for (eid, name), lv in TRADE_LEVELS.items():
        if eid == e.id:
            def set_levels(ln: str, lv=lv) -> str:
                if re.search(r"levels = \[[^\]]*\]", ln):
                    return re.sub(r"levels = \[[^\]]*\]", "levels = " + str(lv), ln)
                return re.sub(r"(, power = |, by = | \},?$)", ", levels = " + str(lv) + r"\1", ln, count=1)      # levels come before power and by
            front = "\n".join(set_levels(ln) if f'"{name}"' in ln else ln for ln in front.split("\n"))
    return "+++\n" + front + "\n+++\n\n" + "\n\n".join(parts) + "\n"


def stale_rows(e: Entry, rows: list[dict]) -> list[str]:
    """The rows whose import span changed since the compare (the entry was edited in between)."""
    # The compare read the import with the printed bold heads as the names of its features; an option that print sets in italics
    # ("Spells:" under Pathfinders Past) is no such name, and a row `**Spells:** Stone shield` of another feature must not split it.
    # So the spans are read with the names of all rows and with the names of the listed rows only.
    spans: dict[str, set[str]] = {}
    for probe in ({namekey(r["feature"]) for r in rows if r["feature"]},
                  {namekey(r["feature"]) for r in rows if r["feature"] and r.get("listed", "yes") == "yes"}):
        _, feats = parse_import(e.body, probe)
        for f in feats:
            spans.setdefault(namekey(import_name(e.id, f.name)), set()).add(f.span_sha())
    bad = []
    for r in rows:
        if r["span_sha256"] and r["feature"]:
            have = spans.get(namekey(r["feature"]))
            if have is None or r["span_sha256"] not in have:
                bad.append(r["feature"])     # the feature changed, or its name is gone
    return bad


def run_write(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    rows = read_tsv(tsv_path(corpus, book))
    props = read_proposals(proposals_path(corpus, book))
    entries = load_entries(corpus, book, args.only)
    written: list[Entry] = []
    originals: dict[Path, str] = {}
    for e in entries:
        if e.converted:
            continue
        mine = [r for r in rows if r["entry"] == e.id]
        why = convertible(e, mine, props.get(e.id))
        if why:
            continue
        stale = stale_rows(e, mine)
        if stale:
            print(f"{e.id}: stale rows ({', '.join(stale)}); run --compare")
            continue
        try:
            new = convert_text(e, props[e.id], mine)
        except ValueError as err:
            print(f"{e.id}: not written: {err}")
            continue
        originals[e.path] = e.path.read_text(encoding="utf-8")
        e.path.write_text(new, encoding="utf-8")
        written.append(e)
    if args.checker and written:
        written = recheck(corpus, args, written, originals, rows, props)
    keep = {k: v for k, v in props.items() if k not in {e.id for e in written}}
    write_proposals(proposals_path(corpus, book), keep)
    write_tsv(tsv_path(corpus, book), [dict(r) for r in rows])
    print(f"converted {len(written)} entries")
    return 0


def recheck(corpus: Path, args, written: list[Entry], originals: dict[Path, str], rows: list[dict], props: dict) -> list[Entry]:
    """Runs the checker on the written corpus; puts back each entry that it rejects and holds it."""
    fmt = subprocess.run([args.checker, "fmt", str(corpus)], capture_output=True, text=True)
    if fmt.returncode != 0:
        for path, text in originals.items():      # leave the corpus as it was
            path.write_text(text, encoding="utf-8")
        raise SystemExit("fmt failed; every entry of this run is put back:\n" + fmt.stderr[-2000:])
    for _ in range(5):
        r = subprocess.run([args.checker, "check", str(corpus)], capture_output=True, text=True)
        if r.returncode == 0:
            return written
        bad: dict[str, list[str]] = {}
        for ln in (r.stdout + r.stderr).splitlines():
            m = re.search(r"(entries/[^\s:]+\.md):\d+: (.*)", ln)
            if m and not ln.startswith("warning"):
                bad.setdefault(m.group(1), []).append(m.group(2))
        hit = [e for e in written if str(e.path.relative_to(corpus)) in bad]
        if not hit:
            raise SystemExit("check failed outside the written entries:\n" + (r.stdout + r.stderr)[-3000:])
        for e in hit:
            e.path.write_text(originals[e.path], encoding="utf-8")
            why = "checker: " + bad[str(e.path.relative_to(corpus))][0][:300]
            props[e.id]["hold"] = why
            first = next(row for row in rows if row["entry"] == e.id)
            first["status"], first["source"], first["note"] = "hold", "", why
            print(f"{e.id}: put back, {why}")
        written = [e for e in written if e not in hit]
    raise SystemExit("the checker still fails after five rounds")


# ---- --check --------------------------------------------------------------------------------------------

# The printed trade sentences that state no trade on purpose are listed in `trade-sentence-exceptions.toml` in the corpus root (the file
# that the app's check reads; one `[[exception]]` row each with `entry`, `feature`, `sentence`, `reason` and `issue`); the script reads the
# same file, so the two never disagree. A sentence matches when its squashed text contains the row's squashed `sentence`.
def trade_sentence_exceptions(root: Path) -> list[dict]:
    path = root / "trade-sentence-exceptions.toml"
    return tomllib.loads(path.read_text(encoding="utf-8")).get("exception", []) if path.exists() else []


def printed_trade_gaps(e: Entry) -> list[str]:
    """The printed trade sentences of a converted entry that no stored trade states (Opus review of batch 4: the app's check does
    not require a stored trade for every printed sentence). Every "This alters X" or "This replaces X" in the text of a feature
    (its unlisted subheadings count with it) needs a stored trade of that op whose name covers X; a phrase that ends "as indicated
    below" is a cross-reference (ruling 40) and states none."""
    fields = e.data.get("fields") or {}
    listed = {f["anchor"] for f in fields.get("features") or []}
    trades = [trade_name(t) for t in trades_of(e)]
    out: list[str] = []
    head = None
    for part in re.split(r"(?m)^(?=#+ )", e.body):
        m = re.match(r"#+ (.*?)(?: \{#([^}]+)\})?\n", part)
        if not m:
            continue
        if m.group(2) in listed:
            head = m.group(1)
        # an unlisted section before the first listed feature ("Class Skills", "Alignment") counts with its own heading (Opus
        # review of #329: Planar Scout, Witch Killer, Dreamthief and Experimenter print "This alters the ... class skills" there)
        sentences = trade_sentences(part[m.end():], ABILITY_TAG.sub("", head or m.group(1)).strip())
        for sop, ph, _bare in sentences:
            if not ph.strip() or re.match(r"(?:grants|to|does|do|not)\b", ph) or any(
                    x["entry"] == e.id and squash(x["sentence"]) in squash(ph) for x in trade_sentence_exceptions(e.path.parents[2])):
                continue                    # "This change to spells doesn't apply", "This ability does not alter ...": no trade sentence
            if not any(op == sop and covers(ph, name) for op, name in trades):
                out.append(f'{head}: the sentence "This {sop} {ph}" has no stored trade')
    return out


# ---- the printed trade sentences (opus audit of the Blood of the Ancients pilot) -----------------------------------

PRINTED_TRADE = re.compile(r"This (?:(?:ability|class feature|performance|archetype|deed|hex|talent|trick|power|discovery|revelation|exploit|mercy) )?"
                           r"(?:replaces|alters|changes|modifies)\b[^.]*\.")


def sentences_path(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / f"feature-prose-540-{book}.sentences.tsv"


def letters_key(text: str) -> str:
    """The comparison key of a sentence: letters and digits only, Markdown and the quote styles gone."""
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    t = t.replace(SUPERSCRIPT, "").replace("\u2019", "'").replace("\\", "")
    return re.sub(r"[^a-z0-9]", "", t.lower())


def printed_trade_sentences(section: list) -> list[str]:
    """Every "This replaces/alters/changes ..." sentence of the printed span of an archetype, in print order."""
    text = re.sub(r"\s+", " ", " ".join(b.plain() for b in section if b.kind == "para"))
    text = re.sub(r"\b1oth\b", "10th", text)      # the text layer reads a zero as a letter
    return [re.sub(r"\s+", " ", m.group(0)).strip() for m in PRINTED_TRADE.finditer(text)]


# A printed trade sentence that print leaves without its period, so that it runs into the head of the next ability: the sentence ends where the
# head begins (Honor Guard, Ultimate Combat p. 37: "This modifies the challenge ability" and then "Intercept (Ex):")
SENTENCE_TRIMS = {"ref/arc-cavalier/honor-guard": "This modifies the challenge ability",
                  "ref/arc-spiritualist/plague-eater": "This ability replaces see invisibility"}      # print has no period after "see invisibility" (Heroes of Golarion p. 12); the next head follows
SENTENCE_FIXES = {"ref/arc-fighter/titan-fighter": {"This ability replaces 1 0.": "This ability replaces armor training."}}      # the text layer sets the words of the last sentence of Incredible Heft out of order (a hand text writes it, Giant Hunter's Handbook p. 21)
SENTENCE_SKIP: set = set()      # the books whose printed sentences are not read (none: the Card Caster is written since owner ruling 58)


def run_print_sentences(args) -> int:
    """Writes `<book>.sentences.tsv`: the printed trade sentences of every archetype of the book (converted or not), so that
    `--check` can require them in the entries without the book. Needs `--books` and `--cache`."""
    corpus = Path(args.corpus).resolve()
    book = args.book
    configure_book(book)
    pdf = find_pdf(Path(args.books), publication_title(corpus, book))
    if not pdf:
        raise SystemExit(f"no copy of {publication_title(corpus, book)!r} under {args.books}")
    bk = load_book(book_xml(pdf, Path(args.cache)))
    entries = load_entries(corpus, book, args.only)
    stops = {squash(ptitle(x)) for x in entries} | CLASS_TITLES | UNTYPED_ARCHETYPE_TITLES
    rows = []
    for e in entries:
        page = int(e.page) if e.page.isdigit() else None
        if page is None or e.id in SENTENCE_SKIP:
            continue
        blocks = read_blocks(bk, max(1, page + PAGE_OFFSET[0] - 3), min(page + PAGE_OFFSET[0] + 4, max(bk.pages)))
        section = find_section(blocks, ptitle(e), stops)
        if section is None:
            whole = read_blocks(bk, 1, max(bk.pages))
            section = find_section(whole, ptitle(e), stops)      # a wrong cited page (see run_compare)
        if section is None:
            print(f"warning: {e.id}: title not found near page {page}")
            continue
        rows += [(e.id, (lambda t: t if t and sent.startswith(t) else sent)(SENTENCE_TRIMS.get(e.id))) for sent in
                 (SENTENCE_FIXES.get(e.id, {}).get(x, x) for x in printed_trade_sentences(section))]
    lines = ["entry\tsentence"] + [f"{eid}\t{sent}" for eid, sent in rows]
    sentences_path(corpus, book).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(rows)} printed trade sentences of {len(entries)} archetypes")
    return 0


def recorded_print_texts(corpus: Path, entry_id: str) -> tuple[list[tuple[str, str]], str]:
    """The differences from print that the review records for an entry: pairs (written, printed) of the misprint list and of the
    errata list of this script, and the printed values of its rows in `scripts/errata.tsv` (the owner's 1st printing against the
    Paizo errata, which the corpus follows)."""
    pairs = [(w, p_) for e_, p_, w, *_ in MISPRINTS if e_ == entry_id] + [(w, p_) for e_, _a, _pg, p_, w in ERRATA if e_ == entry_id]
    printed = ""
    path = corpus / "scripts" / "errata.tsv"
    if path.exists():
        for ln in path.read_text(encoding="utf-8").split("\n")[1:]:
            cells = ln.split("\t")
            if len(cells) > 5 and cells[0] == entry_id:
                printed += " " + cells[5]
    return pairs, printed


def missing_printed_sentences(corpus: Path, book: str, entries: list) -> list[str]:
    """The reverse of the drift check: every printed "This replaces/alters ..." sentence of the book's archetypes (the rows of
    `<book>.sentences.tsv`) is in the entry, or the review records the difference (a misprint fix, a Paizo errata)."""
    path = sentences_path(corpus, book)
    if not path.exists():
        return []
    by = {e.id: e for e in entries}
    out = []
    for ln in path.read_text(encoding="utf-8").split("\n")[1:]:
        if not ln:
            continue
        eid, sent = ln.split("\t", 1)
        if eid not in by:
            continue
        key = letters_key(sent)
        flat = re.sub(r"\s+", " ", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", by[eid].body).replace("_", ""))
        if key in letters_key(flat):
            continue
        pairs, printed = recorded_print_texts(corpus, eid)
        if key in letters_key(printed) or any(w in flat and key in letters_key(flat.replace(w, p_)) for w, p_ in pairs):
            continue
        out.append(f"{eid}: the printed sentence \"{sent}\" is not in the entry")
    return out


def run_check(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    rows = read_tsv(tsv_path(corpus, book))
    props = read_proposals(proposals_path(corpus, book))
    entries = load_entries(corpus, book, args.only)
    by_entry: dict[str, list[dict]] = {}
    for r in rows:
        by_entry.setdefault(r["entry"], []).append(r)
    ids = {e.id for e in entries}
    errors: list[str] = []
    converted = held = 0
    for e in entries:
        mine = by_entry.get(e.id, [])
        fields = e.data.get("fields") or {}
        if e.converted:
            converted += 1
            listed = [r for r in mine if r["listed"] == "yes"]
            want = [(f["anchor"], f.get("level")) for f in fields.get("features", [])]
            have = [(r["anchor"], int(r["level"]) if r["level"] else None) for r in listed]
            if not mine:
                errors.append(f"{e.id}: converted, but the review TSV has no rows for it")
            elif want != have:
                errors.append(f"{e.id}: `features` {want} differ from the review TSV {have}")
            if any(r["status"] not in WRITABLE for r in mine):
                errors.append(f"{e.id}: converted, but a row is not decided")
            if e.id in props:
                errors.append(f"{e.id}: converted, but still in the proposals")
            errors += [f"{e.id}: {gap}" for gap in printed_trade_gaps(e)]
            continue
        if not mine:
            errors.append(f"{e.id}: not in the review TSV; run --compare")
            continue
        held += 1
        stale = stale_rows(e, mine)
        if stale:
            errors.append(f"{e.id}: stale rows ({', '.join(stale)}); run --compare")
        if e.id not in props:
            errors.append(f"{e.id}: no proposals; run --compare")
        elif convertible(e, mine, props[e.id]) is None:
            errors.append(f"{e.id}: every row is decided; run --write")
    for k in props:
        if k not in ids:
            errors.append(f"{k}: in the proposals but not an entry of {book}")
    for k in by_entry:
        if k not in ids:
            errors.append(f"{k}: in the review TSV but not an entry of {book}")
    errors += missing_printed_sentences(corpus, book, entries)
    for (eid, anchor), (text, _note) in read_edits(corpus, book).items():
        errors += [f"{eid}: the edit of `{anchor}` states a paragraph twice (\"{dup}...\")" for dup in repeated_paragraphs(text)]
    print(f"{book}: {len(entries)} archetypes, {converted} converted, {held} not converted")
    for err in errors:
        print("error:", err)
    return 1 if errors else 0


# ---- --self-test ----------------------------------------------------------------------------------------

# ---- the Campaign Setting batch (Inner Sea Magic, Inner Sea Intrigue, Inner Sea Combat) --------------------------------------------
# The per-entry rows of the three books, set in one place so that the other leads' batches (which add rows to the tables above) do not
# meet them in a merge. Each row is a decision of the batch lead against print, recorded in the review note of its feature.

MISPRINTS.extend([
    ("ref/arc-sorcerer/tattooed-sorcerer", "Inscribe Magic Tattoo", "Inscribe Magical Tattoo",
     "the feat is Inscribe Magical Tattoo, which the same book prints in full on p. 16"),
    ("ref/arc-wizard/shadowcaster", "a primalist uses his shadow", "a shadowcaster uses his shadow",
     "the Shadowcaster's first ability repeats the Primalist's wording before it; the archetype is the shadowcaster"),
    ("ref/arc-ranger/tanglebriar-demonslayer", "he can the forgo the normal +2 attack bonus", "he can forgo the normal +2 attack bonus",
     "\"can the forgo\" is a slip: the next ability prints \"he can forgo the normal +4 attack bonus\""),
    ("ref/arc-ranger/nirmathi-irregular", "and 18th level. This otherwise acts as and replaces the standard favored enemy ability.",
     "and 18th level. This otherwise acts as and replaces the standard favored terrain ability.",
     "Focused Terrain repeats the sentence of Focused Enemy above it; the ability it replaces is the favored terrain ability (its trade, its own text)"),
])

TRADE_RENAMES.update({
    # the printed words of the sentence of the feature that replaces them ("This replaces the paladin's mercy gained at 6th level")
    ("ref/arc-paladin/sword-of-valor", "6th-level mercy"): "Mercy gained at 6th level",
    ("ref/arc-sorcerer/razmiran-priest", "9th-level bloodline power"): "Bloodline power gained at 9th level",
    ("ref/arc-sorcerer/tattooed-sorcerer", "7th-level bloodline feat"): "Bloodline feat gained at 7th level",
    ("ref/arc-wizard/primalist", "5th-level bonus feat"): "Wizard bonus feat acquired at 5th level",
    ("ref/arc-wizard/primalist", "10th-level bonus feat"): "Wizard bonus feat acquired at 10th level",
    ("ref/arc-alchemist/crypt-breaker", "Brew potion"): "Brew Potion bonus feat",
    ("ref/arc-bard/dawnflower-dervish", "Dirge of doom"): "Dirge of doom bardic performance",
    ("ref/arc-sorcerer/razmiran-priest", "Bloodline spells gained at 3rd level and 5th level"):
        "Bloodline spells gained at 3rd level and 5th level respectively",
    ("ref/arc-summoner/first-worlder", "Summon monster"): "Summon monster ability of a normal summoner",
    # Keleshite Prophet (Inner Sea Intrigue pp. 41-42): the sentences of its Class Skills and Bonus Spells sections (ruling 22)
    # Inner Sea Combat: the printed words of the sentence of the feature that replaces them
    ("ref/arc-barbarian/shoanti-burn-rider", "4th, 8th, 12th, and 16th level rage powers"): "Rage powers gained at 4th, 8th, 12th, and 16th level",
    ("ref/arc-gunslinger/siege-gunner", "Deadeye deed"): "Deadeye",
    ("ref/arc-gunslinger/siege-gunner", "Gunslinger initiative deed"): "Gunslinger initiative",
    ("ref/arc-monk/ouat", "and the greed and hatred dwarf racial traits"): "Greed and hatred racial traits",
    ("ref/arc-monk/ouat", "The defensive training"): "Defensive training",
    ("ref/arc-monk/ouat", "and weapon familiarity dwarf racial traits"): "Weapon familiarity racial traits",
    ("ref/arc-oracle/keleshite-prophet", "Bonus skills from the oracle's mystery"): "Additional skills gained from the oracle's mystery",
    ("ref/arc-oracle/keleshite-prophet", "The bonus spells gained at 6th, 10th, 12th, 16th, and 18th levels from the oracle's mystery"):
        "Bonus spells at those levels gained from the oracle's mystery",
})

# the lost levels of the earlier books (cross-batch review of the level rules, owner rulings 4, 35, 48 and 50): print states the level in
# a later sentence or paragraph of the feature, or the replaced feature is a 1st-level deed
LEVEL_FROM_PRINT.update({
    ("ref/arc-investigator/sleuth", "deeds"): (1, "its next sentence: \"At 1st level, a sleuth gains the following deeds\""),
    ("ref/arc-sorcerer/eldritch-scrapper", "bloodline-weapons"): (3, "\"at 3rd level she can select that 1st-level bloodline power in place of her 3rd-level\""),
    ("ref/arc-bard/sandman", "greater-stealspell"): (15, "\"A sandman's stealspell power improves at 15th level\""),
    ("ref/arc-monk/monk-of-the-empty-hand", "bonus-feat"): (6, "\"adds the following feats to his list of bonus feats at 6th level\""),
    ("ref/arc-paladin/shining-knight", "divine-bond"): (5, "\"Upon reaching 5th level, a shining knight must form a bond with a mount\""),
    ("ref/arc-ranger/guide", "improved-ranger-s-luck"): (16, "\"Upon reaching 16th level\""),
    ("ref/arc-cleric/forgemaster", "craft-magic-arms-and-armor"): (3, "\"gains this as a bonus feat at 3rd level\""),
    ("ref/arc-gunslinger/buccaneer", "gun-training"): (13, "\"A buccaneer gains this ability only at 13th level\""),
    ("ref/arc-oracle/reincarnated-oracle", "oracle-s-curse"): (1, "\"must choose the haunted or tongues curse at 1st level\""),
    ("ref/arc-oracle/shigenjo", "final-revelation"): (20, "\"Upon reaching 20th level, you achieve true enlightenment\""),
    ("ref/arc-medium/storm-dreamer", "storm-trance"): (3, "\"A 3rd-level storm dreamer can enter a meditative trance\""),
    ("ref/arc-swashbuckler/dashing-thief", "swaying-charm-deed"): (15, "\"At 15th level, when a dashing thief successfully dazes a creature\""),
    ("ref/arc-alchemist/promethean-alchemist", "ability-score-increase"): (5, "\"The homunculus adds 1 to one of its ability scores at 5th level\""),
    ("ref/arc-druid/green-faith-initiate", "mediator-s-ear"): (3, "\"By 3rd level, a Green Faith initiate is respected\""),
    ("ref/arc-familiar/animal-exemplar", "influence-animals"): (3, "\"gains speak with animals ... at 3rd level instead of 7th level\""),
    ("ref/arc-familiar/egotist", "order-master"): (3, "\"gains speak with master at 3rd level instead of 5th level\""),
    ("ref/arc-familiar/mascot", "heart-of-the-team"): (13, "\"Once per day at 13th level\""),
    ("ref/arc-swashbuckler/wildstrider", "subterfuge"): (1, "owner rulings 35 and 48: the deed replaces dodging panache, a 1st-level deed (and alters derring-do)"),
})
# a feature whose print states no level although a reader of the text would take one (a step of the feature, "Beginning at 2nd level, when he selects a taboo"):
# the feature alters a part of a class feature, so it has none (owner ruling 48 on Nexian Channeler's Third Eye, review of #344)
LEVEL_NONE = {
    ("ref/arc-medium/nexian-channeler", "third-eye"),
}
LEVEL_NONE.add(("ref/arc-bloodrager/bloody-knuckled-rowdy", "reduced-spells-known"))      # it changes the spells known, a part of spellcasting (ruling 48)
# Ruling 57 and ruling 48 (cross-batch review): a feature that only adds options to, removes options from, or widens the choice of a pool (talents,
# hexes, tricks, discoveries, spell lists, "in place of a talent") alters a part of the class feature, so it has no level from the trade (as Coral Witch,
# #346); Eldritch Scion's bloodline is "selected at 1st level" while the feature it replaces is gained at 4th, so print gives it none
LEVEL_NONE.update({
    ("ref/arc-alchemist/crimson-chymist", "crimson-discoveries"),
    ("ref/arc-investigator/psychic-detective", "investigator-talents"),
    ("ref/arc-investigator/questioner", "restricted-talents"),
    ("ref/arc-investigator/star-watcher", "investigator-talents"),
    ("ref/arc-investigator/steel-hound", "investigator-talents"),
    ("ref/arc-mesmerist/cult-master", "masterful-cult-tricks"),
    ("ref/arc-rogue/phantom-thief", "broad-education"),
    ("ref/arc-rogue/sylvan-trickster", "fey-tricks"),
    ("ref/arc-shaman/benefactor", "benefactor-hexes"),
    ("ref/arc-shaman/primal-warden", "hexes"),
    ("ref/arc-slayer/spiritslayer", "spiritslayer-talents"),
    ("ref/arc-slayer/witch-killer", "superstitious"),
    ("ref/arc-vigilante/brute", "brute-talents"),
    ("ref/arc-vigilante/cabalist", "cabalist-talents"),
    ("ref/arc-vigilante/gunmaster", "gunmaster-talents"),
    ("ref/arc-vigilante/warlock", "warlock-talents"),
    ("ref/arc-vigilante/zealot", "zealot-talents"),
    ("ref/arc-skald/battle-scion", "battle-prowess"),
    ("ref/arc-kineticist/blood-kineticist", "blood-blast"),
    ("ref/arc-magus/eldritch-scion", "bloodline"),
})
# Ruling 57 against a level that print states in the feature itself (ruling 51): the printed level wins
LEVEL_FROM_PRINT.update({
    ("ref/arc-druid/urushiol", "venom-immunity"): (4, "gains venom immunity at 4th level instead of 9th level"),
    ("ref/arc-skald/boaster", "rage-power"): (4, "does not gain this ability until 4th level"),
    ("ref/arc-bard/animal-speaker", "nature-s-speaker"): (5, "At 5th, 11th, and 17th level, the animal speaker selects another kind of animal friend"),
})
LEVEL_NONE.add(("ref/arc-sorcerer/wishcrafter", "wishbound-arcana"))      # it replaces the bloodline arcana, a part of the bloodline (ruling 48)
# Diminished Spellcasting alters the whole spellcasting of the class, a 1st-level class feature (owner ruling 50; the corpus was split 7/7 on it)
LEVEL_FROM_PRINT.update({(f"ref/arc-{e}", "diminished-spellcasting"): (1, "ruling 50: alters the whole spellcasting, a 1st-level class feature") for e in (
    "magus/esoteric", "magus/myrmidarch", "magus/skirnir", "magus/jistkan-artificer", "magus/kensai", "magus/soul-forger", "oracle/purifier")})
# a feature that replaces or alters only a part of a feature gets no level from the trade (owner ruling 48)
LEVEL_FROM_PRINT.update({
    # Geist Channeler (Occult Adventures p. 109): "This ability alters the phantom" (Geistform Phantom) and "This ability modifies the phantom and replaces the
    # phantom's emotional focus" (Emotionless, ruling 55): two features state the one trade `alters Phantom`, a whole 1st-level feature (ruling 50)
    ("ref/arc-spiritualist/geist-channeler", "geistform-phantom"): (1, "ruling 50: alters the phantom, a whole 1st-level feature (also stated by Emotionless)"),
    ("ref/arc-spiritualist/geist-channeler", "emotionless"): (1, "rulings 50 and 55: modifies the phantom, a whole 1st-level feature"),
})
NO_LEVEL_ONE = {
    ("ref/arc-gunslinger/bushwhacker", "craven-deeds"),       # "replaces some of her deeds with the following deeds"
}

LEVEL_FROM_PRINT[("ref/arc-oracle/keleshite-prophet", "divining-dance")] = (
    1, 'print says the prophet "must take the following revelation at 1st level" (Inner Sea Intrigue p. 42): a fixed ability, no choice (ruling 47)')

LEVEL_ONE_REPLACES.update({
    # Owner rulings 48 and 50 of 2026-11-26. The class-table lookup of #338 finds the whole 1st-level features that the other features of these
    # books replace or alter; these two it does not (the name "spontaneous casting" is no entry of the druid's Special column, and the stored
    # trade name "Eidolon ability of a normal summoner" is not the class feature's name)
    ("ref/arc-druid/nithveil-adept", "animal-speech"),            # replaces spontaneous casting
    ("ref/arc-summoner/first-worlder", "eidolon"),                # replaces the eidolon ability of a normal summoner
    ("ref/arc-alchemist/crypt-breaker", "trapfinding"),      # replaces the Brew Potion bonus feat, which the alchemist gains at 1st level (rulings 11 and 35)
})

TRADE_ADDITIONS.update({
    # "This otherwise works like and replaces the eidolon ability of a normal summoner" (Inner Sea Magic p. 35): the import stored only the
    # summon monster trade
    "ref/arc-summoner/first-worlder": [{"replaces": "Eidolon ability of a normal summoner", "feature": "eidolon"}],
})

TRADE_ADDITIONS.update({
    # "This ability replaces nature sense" (Inner Sea Intrigue p. 44, Nithveil Skills): the import stored no trade for it
    "ref/arc-druid/nithveil-adept": [{"replaces": "Nature sense", "feature": "nature-sense"}],
})

for _eid in ("ref/arc-monk/perfect-scholar", "ref/arc-ninja/frozen-shadow", "ref/arc-summoner/god-caller",
             "ref/arc-unchained-summoner/god-caller", "ref/arc-inquisitor/royal-accuser"):
    # "This ability alters the ...'s class skills" in the Class Skills section before the first feature (Inner Sea Intrigue); stored without `by`
    TRADE_ADDITIONS[_eid] = TRADE_ADDITIONS.get(_eid, []) + [{"alters": "Class skills"}]

TRADE_REMOVALS.setdefault("ref/arc-fighter/druman-blackjacket", []).append(("alters", "Bonus fighter feats"))      # print states no trade for its Bonus Feats section (ruling 17)

TRADE_OP_FIXES.update({
    # "functions identically to and replaces the cavalier's mount ability" (Inner Sea Combat p. 47), "functions as and replaces the banner
    # cavalier ability" (p. 45): stored as `alters`
    ("ref/arc-cavalier/wave-rider", "Mount"): "replaces",
    ("ref/arc-cavalier/spellscar-drifter", "Banner"): "replaces",
    # "This otherwise acts as and replaces the standard favored enemy ability" (Inner Sea Magic p. 37), stored as `alters`, as in the
    # Reanimator's "functions as and replaces the standard alchemist bomb class feature"
    ("ref/arc-ranger/nirmathi-irregular", "Favored enemy"): "replaces",
    ("ref/arc-ranger/nirmathi-irregular", "Favored terrain"): "replaces",
})


# ---- the batch of Heroes of the Darklands, Legacy of Dragons, Familiar Folio and Advanced Class Origins (phynics/cast-iron#540, lead A, second batch) ----

IMPORT_HEAD_FIXES.update({
    # the import's misspelled heads (Legacy of Dragons p. 13)
    ("ref/arc-fighter/dragonheir-scion", "Draconic Defense (Su)"): "Draconic Defenses (Su)",
    ("ref/arc-fighter/dragonheir-scion", "Draconic Presense (Su)"): "Draconic Presence (Su)",
    ("ref/arc-mesmerist/mindwyrm-mesmer", "Phantasmagorical Breath (Su)"): "Phantasmagoric Breath (Su)",
})
EXTRA_LINKS[("ref/arc-cavalier/drakerider", "approved-order")] = [("order of the beast", "ref/order/order-of-the-beast-isc")]

TRADE_RENAMES.update({
    # the printed words of the sentence of the feature that replaces them (ruling 22)
    ("ref/arc-barbarian/beastkin-berserker", "4th, 8th, and 12th level rage powers"): "Rage powers gained at 4th, 8th, and 12th levels",
    ("ref/arc-psychic/psychic-marauder", "3rd-, 11th-, and 19th-level phrenic amplifications"): "Phrenic amplifications gained at 3rd, 11th, and 19th levels",
    ("ref/arc-vigilante/darklantern", "1st-level social talent"): "Social talent that the darklantern gains at 1st level",
    ("ref/arc-witch/demon-sworn", "6th-level hex"): "Hex gained at 6th level",
    ("ref/arc-alchemist/blightseeker", "The discovery gained at 6th level"): "Discoveries gained at 6th, 12th, and 18th levels",
    ("ref/arc-kineticist/blightburner", "Basic geokinesis wild talent"): "Basic geokinesis wild talent gained from elemental focus",
    ("ref/arc-druid/fungal-pilgrim", "Wild shape"): "Wild shape if the fungal pilgrim selected the Plant domain as her nature bond",
})
TRADE_RENAMES.update({
    ("ref/arc-fighter/dragonheir-scion", "Bonus feat gained at 4th level"): "Bonus feat gained at 3rd level",
    ("ref/arc-fighter/dragonheir-scion", "Bonus feat gained at 6th level.1-2"): "Bonus feat gained at 5th level",
})
TRADE_RENAMES[("ref/arc-samurai/sovereign-blade", "Bonus feats gained at 6th, 12th, and 18th level")] = "Bonus feats a samurai gained at 6th, 12th, and 18th level"
TRADE_LEVELS[("ref/arc-fighter/dragonheir-scion", "Bonus feat gained at 3rd level")] = [3]
TRADE_LEVELS[("ref/arc-fighter/dragonheir-scion", "Bonus feat gained at 5th level")] = [5]
TRADE_RENAMES.update({
    ("ref/arc-wizard/familiar-adept", "5th- and 10th-level bonus feats"): "Bonus feats at 5th and 10th levels",
    ("ref/arc-witch/synergist", "1st-, 8th-, and 14th-level hexes"): "Hexes gained at 1st, 8th, and 14th level",
})
EXTRA_LINKS[("ref/arc-witch/synergist", "symbiosis")] = [("beast shape II", "ref/spell/beast-shape-2")]
TRADE_RENAMES.update({
    ("ref/arc-sorcerer/bloodline-familiars", "1st-level bloodline power"): "1st-level bloodline power granted by the character's bloodline",
    ("ref/arc-bloodrager/bloodline-familiars", "The 1st-level bloodline power"): "The 1st-level bloodline power granted by the character's bloodline",
})
TRADE_RENAMES[("ref/arc-skald/belkzen-war-drummer", "7th-level versatile performance gained benefit")] = "Versatile performance gained benefit at 7th level"
IMPORT_HEAD_FIXES.update({
    # Bloodline Familiars (Familiar Folio p. 16): print sets the bloodline before the ability in the key
    **{("ref/arc-bloodrager/bloodline-familiars", old): f"{lead}\u2014{old}" for old, lead in (
        ("Squeezer (Ex)", "Aberrant"), ("Grotesque Appendages (Ex)", "Abyssal"), ("Spell Catalyst (Su)", "Arcane"),
        ("Heavenly Touch (Su)", "Celestial"), ("Foretold Touch (Su)", "Destined"), ("Dragon's Flight (Ex)", "Draconic"),
        ("Dualistic Energy (Su)", "Elemental"), ("Amusing Familiar (Su)", "Fey"), ("Hellish Aura (Su)", "Infernal"),
        ("Unliving Physiology (Su)", "Undead"))},
})
# Scaled Fist (Legacy of Dragons p. 14): "This ability modifies bonus feats" stands under the unlisted Bonus Feats scaffold: `alters Bonus feats` has no
# `by` (rulings 13 and 55) and Draconic Might gains no level from it
TRADE_NO_BY.setdefault("ref/arc-monk/scaled-fist", []).append("Bonus feats")
# Ectoplasm Master (Haunted Heroes Handbook p. 14): "This discovery modifies the alchemist's bombs" (ruling 55); one discovery of a list is a part of bombs, so no level
TRADE_ADDITIONS.setdefault("ref/arc-alchemist/ectoplasm-master", []).append({"alters": "The alchemist's bombs and doesn't stack with other discoveries that modify bombs", "feature": "bomb"})
NO_LEVEL_ONE.add(("ref/arc-alchemist/ectoplasm-master", "ectoplasm-master-discoveries"))
# Iron-Ring Striker (Martial Arts Handbook p. 5): the stored name is the printed words of "This modifies the bonus feat gained at 5th level"
TRADE_RENAMES[("ref/arc-magus/iron-ring-striker", "5th-level bonus feat")] = "Bonus feat gained at 5th level"
# Ilsurian Archer: the stored name is the printed words of "This modifies the ranger's combat style feat class feature" (ruling 22, app #737)
TRADE_RENAMES[("ref/arc-ranger/ilsurian-archer", "Combat style")] = "The ranger's combat style feat class feature"
# Eldritch Archer (Heroes of the Streets p. 11): "This ability modifies the magus's class skills." under the unlisted Class Skills section: an alters trade with no `by` (rulings 13 and 55)
TRADE_ADDITIONS.setdefault("ref/arc-magus/eldritch-archer", []).append({"alters": "Class skills", "_no_by": True})
NO_LEVEL_ONE.add(("ref/arc-witch/coral-witch", "waves-spirit-hex"))       # it only widens which hexes can be chosen: a part of the hex feature (ruling 48, review of #346)
EXTRA_LINKS[("ref/arc-druid/fungal-pilgrim", "fungal-companion")] = [("fungal creature", "ref/template/fungal-creature")]
MISPRINTS.append(("ref/arc-slayer/sczarni-executioner", "must make a successful a Fortitude save", "must make a successful Fortitude save",
                  "a stray \"a\" in print (\"a successful a Fortitude save\"); the same book prints \"a successful Fortitude save\" elsewhere"))
TRADE_ADDITIONS["ref/arc-fighter/dragonheir-scion"] = [{"alters": "Class skills"}]
TRADE_ADDITIONS["ref/arc-druid/fungal-pilgrim"] = [{"replaces": "Wild shape if the fungal pilgrim selected an animal companion as her nature bond"}]
TRADE_LEVELS[("ref/arc-alchemist/blightseeker", "Discoveries gained at 6th, 12th, and 18th levels")] = [6, 12, 18]
TRADE_MERGED["ref/arc-alchemist/blightseeker"] = [("replaces", "The discovery gained at 12th level"), ("replaces", "The discovery gained at 18th level")]

def self_test() -> int:
    import tempfile
    ok = 0

    def eq(a, b, what):
        nonlocal ok
        if a != b:
            raise SystemExit(f"self-test failed: {what}: {a!r} != {b!r}")
        ok += 1

    eq(anchor_of("Shattering Strike (Ex)"), "shattering-strike", "anchor")
    eq(anchor_of("Sic 'Em (Ex)"), "sic-em", "anchor apostrophe")
    eq(anchor_of("Jack of All Trades (Su, Ex)"), "jack-of-all-trades", "anchor tag list")
    eq(lead_level("At 2nd level, a two-handed fighter gains"), 2, "lead")
    eq(lead_level("Starting at 11th level, a thing"), 11, "lead starting")
    eq(lead_level("Beginning at 3rd level a thing"), 3, "lead beginning")
    eq(lead_level("At 2th level, a thing"), None, "lead suffix")
    eq(lead_level("A 3rd level, a thing"), None, "lead typo")
    eq(lead_level("An arcane duelist of 6th level or higher"), None, "lead inside")
    eq(namekey("Jack-of-All-Trades (Ex)"), namekey("Jack of All Trades"), "namekey")
    eq(progression_levels("This bonus increases by +1 for every four levels beyond 2nd."), {6, 10, 14, 18}, "progression")
    eq(progression_levels("increases by +1 at 5th level and every six levels thereafter"), {5, 11, 17}, "progression thereafter")
    eq(progression_levels("no rule here"), None, "no progression")
    eq(trade_sentences("It works. This ability replaces armor training 1 and 2.")[0], ("replaces", "armor training 1 and 2", False), "trade sentence")
    eq(trade_sentences("These replace the normal attack roll bonus.")[0][2], True, "bare trade sentence")
    eq(covers("armor training 1, 2, 3, and 4", "Armor training 3"), True, "covers step")
    eq(covers("armor training 1 and 2", "Armor training 3"), False, "covers step miss")
    eq(covers("the standard alchemist bomb class feature", "Bombs"), True, "covers a name inside a longer phrase")
    eq(covers("bravery and armor training", "Bravery"), True, "covers list")
    eq(fix_ligatures("a f ighter in f lank and inf lict", {"fighter", "flank", "inflict"}), "a fighter in flank and inflict", "ligatures")
    eq(fix_ligatures("lots of f ine", {"fine"}), "lots of fine", "ligature fine")
    eq(fix_hyphens("two- weapon fighter", {"two-weapon"}), "two-weapon fighter", "hyphen kept")
    eq(fix_hyphens("conven- tional", {"conventional"}), "conventional", "hyphen dropped")
    eq([bool(RUN_IN_HEAD_ONLY.search(t)) for t in ("Elemental\u2014Dualistic Energy (Su):", "Wings (Su): At 15th level, a thing grows.", "Wings (Su): the wings")], [True, False, False], "head only")
    eq([bool(DASH_KEY.fullmatch(t)) for t in ("Aberrant\u2014Squeezer (Ex)", "Squeezer (Ex)", "Wild shape (Su)")], [True, False, False], "dash key")
    hc = head_candidate(Para("para", [("Aberrant", True, False), ("\u2014", False, False), ("Squeezer (Ex)", True, False), (": The familiar gains", False, False)], "16", 0))
    eq(hc[0] if hc else None, "Aberrant\u2014Squeezer (Ex)", "dash key head")
    eq(head_candidate(Para("para", [("Aberrant", True, False), ("Squeezer (Ex)", True, False), (": x", False, False)], "16", 0))[0], "AberrantSqueezer (Ex)", "no dash, one bold run")
    BOX_LORE["titles"] = frozenset({squash("Armor Master Archetypes and Prestige Classes")})
    _ln = lambda text, size, left: {"size": size, "runs": [(text, False, False)], "col": 1, "left": left, "margin": 468}
    _main, _box = split_boxes([_ln("Text before.", 13, 468), _ln("Armor Master Archetypes and Prestige Classes", 15, 487), _ln("Many organizations", 13, 487), _ln("Channel Energy (Su): text", 13, 468)])
    eq([x["runs"][0][0] for x in _main], ["Text before.", "Channel Energy (Su): text"], "lore box apart: the text around it stays")
    eq([x["runs"][0][0] for x in _box], ["Armor Master Archetypes and Prestige Classes", "Many organizations"], "lore box apart: its lines")
    BOX_LORE["titles"] = frozenset()
    eq([bool(CHOICE_INTRO.search(t)) for t in ("He can select the following additional discoveries: x.", "These talents can be selected by any rogue.", "These can also be taken by any fighter.", "He can take a feat.")], [True, True, True, False], "choice lead-ins of ruling 57's message")
    _tab = {"bomb": 1, "brew potion": 1, "sacred weapon": 1, "summon monster i": 1, "channel energy": 4}
    eq([table_level(_tab, "The bomb class feature", "ref/arc-alchemist/oozemaster"), table_level(_tab, "The bomb class feature"), table_level(_tab, "Sacred weapon"), table_level(_tab, "Channel energy"),
        table_level(_tab, "Summon monster", "ref/arc-summoner/morphic-savant"), table_level(_tab, "Mount")],
       [1, None, 1, 4, 1, None], "table_level: the exact name, or the table's name that TABLE_NAMES gives for a renamed trade")
    eq(join_paras("ref/arc-paladin/legate", "celestial-armor", "A.\n\nThe legate can use this ability a number of times per day."), "A. The legate can use this ability a number of times per day.", "join_paras")
    UPPER_HEAD_ENDS["on"] = True
    _P = lambda text, bold: Para("para", [(text, bold, False)], "1", 0)
    _sec = [Para("title", [("Rogue", True, False)], "1", 0), _P("Opening.", False), Para("para", [("Alpha (Ex)", True, False), (": text", False, False)], "1", 0), _P("more text", False), _P("EQUIPMENT", True), _P("Bag PRICE 5 GP", False)]
    _op, _ft = split_print(_sec, ["Alpha (Ex)"])
    eq([f.head for f in _ft], ["Alpha (Ex)"], "UPPER_HEAD_ENDS: the first head in capitals that the entry does not expect ends the span")
    _op, _ft = split_print(_sec, ["Alpha (Ex)", "Equipment"])
    eq([f.head for f in _ft], ["Alpha (Ex)", "EQUIPMENT"], "UPPER_HEAD_ENDS: a head in capitals that the entry expects stays")
    _op, _ft = split_print([_sec[0], Para("para", [("ALPHA ABILITY", True, False), (": text", False, False)], "1", 0), _P("more", False)], ["Alpha Ability"])
    eq([f.head for f in _ft], ["ALPHA ABILITY"], "UPPER_HEAD_ENDS: the first head never ends the span")
    UPPER_HEAD_ENDS["on"] = False
    LINK_CTX["title"] = "Mirror Witch (Witch Archetype)"
    eq(apply_links("a mirror witch uses a mirror (worth 10 gp)", [("mirror", "ref/eq-misc/mirror")])[0], "a mirror witch uses a [mirror](ref/eq-misc/mirror) (worth 10 gp)", "a link skips the archetype's own name")
    eq(apply_links("%scause fear%s, then %sfear%s" % (I_OPEN, I_CLOSE, I_OPEN, I_CLOSE), [("fear", "ref/spell/fear")])[0], "%scause fear%s, then %s[fear](ref/spell/fear)%s" % (I_OPEN, I_CLOSE, I_OPEN, I_CLOSE), "a link skips a longer italic spell name")
    LINK_CTX["title"] = ""
    eq(bool(CAPS_TITLE.fullmatch("BLIGHTSEEKER (ALCHEMIST ARCHETYPE)")), True, "caps title")
    eq(bool(CAPS_TITLE.fullmatch("Blightseeker (Alchemist Archetype)")), False, "caps title lower case")
    eq(bool(CAPS_TITLE_HEAD.fullmatch("PSYCHIC MARAUDER (PSYCHIC")) and bool(CAPS_TITLE_TAIL.fullmatch("ARCHETYPE)")), True, "caps title wrapped")
    eq([page_skipped(n) for n in (None, 15)], [False, False], "page skip off")
    PAGE_SKIP[:] = [(16, 23), (26, 999)]
    eq([page_skipped(n) for n in (None, 15, 16, 23, 24, 25, 26, 40)], [False, False, True, True, False, False, True, True], "page skip")
    PAGE_SKIP[:] = []
    eq(apply_links("a bull rush works", [("bull rush", "ref/rule/bull-rush")])[0], "a [bull rush](ref/rule/bull-rush) works", "link")
    eq(apply_links("a trip", [("bull rush", "x")])[1], ["bull rush"], "link lost")
    # the owner's examples
    imp = parse_import(
        "Intro.\n\n**Shattering Strike (Ex)**\n\n**Gained:** At 2nd Level\n\n**Passive:** A two-handed fighter gains a +1 bonus to CMB and CMD on sunder attempts.\n\n"
        "**Replaces:** Bravery\n\nAt 6th level: These bonuses increase to +2.\n\nAt 10th level: These bonuses increase to +3.\n\nAt 14th level: These bonuses increase to +4.\n\n"
        "At 18th level: These bonuses increase to +5.\n")[1][0]
    d = build_draft(imp)
    eq((d.level, [n for n, _ in d.upgrades]), (2, [6, 10, 14, 18]), "draft rows")
    printed = ("At 2nd level, a two-handed fighter gains a +1 bonus to CMB and CMD on sunder attempts. "
               "These bonuses increase by +1 for every four levels beyond 2nd. This ability replaces bravery.")
    c = compare_feature(d, printed, set(), set(tokens("Two-Handed Fighter")))
    eq(c.status, "print", "shattering strike takes print")
    changed = printed.replace("+1 bonus to CMB", "+2 bonus to CMB")
    c = compare_feature(d, changed, set(), set(tokens("Two-Handed Fighter")))
    eq(c.status, "hold", "a changed number is held")
    c = compare_feature(d, printed.replace("sunder", "disarm"), set(), set())
    eq(c.status, "hold", "a changed rule word is held")
    c = compare_feature(d, printed.replace("a two-handed fighter gains", "he gains"), set(), set(tokens("Two-Handed Fighter")))
    eq(c.status, "print", "person is wording")
    # links: printed parentheses do not fool the inside-a-link test; every linked occurrence is placed
    got, lost = apply_links("she gains darkvision 60 feet (or adds 60 feet to the range of any darkvision already possessed)",
                            [("darkvision", "ref/umr/darkvision"), ("darkvision", "ref/rule/darkvision")])
    eq(got, "she gains [darkvision](ref/umr/darkvision) 60 feet (or adds 60 feet to the range of any [darkvision](ref/rule/darkvision) already possessed)", "links after a parenthesis")
    eq(lost, [], "no lost link")
    got, lost = apply_links("equal to half his level, while a penalty equal to half his level", [("half", "x"), ("half", "x"), ("half", "x")])
    eq(got.count("[half](x)"), 2, "a repeated linked word is placed twice")
    eq(lost, ["half"], "the third link of a word that occurs twice is reported lost")
    # rule 8: the printed progression against the corpus's fraction of the level
    eq(expand_rules("At 3rd level, a barbarian gains a +1 bonus. This bonus increases by +1 for every three levels after 3rd.",
                    "Gains a bonus equal to [one-third](ref/misc/f) of her barbarian level.")[0], "equal", "rule 8 equal")
    eq(expand_rules("At 2nd level, an archer gains a +1 bonus. These bonuses increase by +1 for every 4 levels beyond 2nd.",
                    "A bonus equal to 1 + one-fourth his fighter level.")[0], "differ", "rule 8 differ")
    # rule 8 and action labels in the comparison
    imp = parse_import("**Fast (Ex)**\n\n**Gained:** At 3rd Level\n\n**Passive:** A rake gains a morale bonus equal to one-third of her rogue level.\n\n**Replaces:** Trap sense\n")[1][0]
    c = compare_feature(build_draft(imp), "At 3rd level, a rake gains a +1 morale bonus. This bonus increases by +1 for every 3 levels beyond 3rd. This ability replaces trap sense.", set(), set(tokens("Rake rogue")))
    eq(c.status, "print", "rule 8 takes print when the values agree")
    imp = parse_import("**Deft (Ex)**\n\n**Gained:** At 7th Level\n\n**Move:** The skirmisher can move and attack.\n")[1][0]
    c = compare_feature(build_draft(imp), "At 7th level, the skirmisher can move and attack.", set(), set(tokens("Skirmisher")))
    eq(c.status, "print", "an action label is not a rule word")
    # print_md: misprints and asterisks are recorded
    pf = PrintFeature("Poison Use (Ex)", [[("A 3rd level, a spy is trained in poison, and talent* too.", False, False)]], 135)
    text, _, notes = print_md(pf, [], set(), "ref/arc-rogue/spy")
    eq(text.startswith("At 3rd level, a spy"), True, "misprint fixed")
    eq(any("misprint fixed" in n for n in notes) and any("asterisks" in n for n in notes), True, "fixes are in the notes")
    # a longer stored trade wins: "replaces mass suggestion" does not name `Suggestion`
    trades = [{"replaces": "Suggestion"}, {"replaces": "Mass suggestion"}, {"replaces": "Evasion"}, {"replaces": "Improved evasion"}]
    feats = [{"anchor": "a", "head": "A", "print": "This performance replaces mass suggestion."},
             {"anchor": "b", "head": "B", "print": "This ability replaces improved evasion."}]
    by, problems = assign_by(trades, feats, [])
    eq(by.get(1), ["a"], "the longer trade is named")
    eq(by.get(3), ["b"], "improved evasion is named")
    eq(0 in by or 2 in by, False, "the shorter trades are not named by the longer phrase")
    eq(len(problems), 2, "the shorter trades have no sentence of their own")
    trades = [{"replaces": "Uncanny dodge"}, {"replaces": "improved uncanny dodge"}]
    by, _ = assign_by(trades, [{"anchor": "a", "head": "A", "print": "This ability replaces uncanny dodge, improved uncanny dodge, and damage reduction."}], [])
    eq(by, {0: ["a"], 1: ["a"]}, "a plain trade stated beside the longer one is named")
    trades = [{"replaces": "Armor training 3"}, {"replaces": "Armor training 4"}]
    by, _ = assign_by(trades, [{"anchor": "a", "head": "A", "print": "This ability replaces armor training 3 and 4."}], [])
    eq(by, {0: ["a"], 1: ["a"]}, "a step list still names both trades")
    # the reader rules of owner ruling 21 (R1 to R12), 24 and 25, as the script reads a trade sentence
    eq(covers("the mutagen class ability (a mindchemist cannot create mutagens unless he selects mutagen as a discovery)", "Mutagen"), True, "R1 class ability, R9 aside")
    eq(covers("a monk's normal bonus feats", "Bonus feats"), True, "R2 normal")
    eq(covers("a monk's normal bonus feats", "Feats"), True, "R2 a longer name still holds the short one")
    eq(phrase_tokens("the bonus feats"), phrase_tokens("bonus feats"), "R2 bonus stays")
    eq("bonu" in phrase_tokens("normal bonus feats"), True, "R2 bonus is never dropped")
    eq(covers("the magus arcana normally gained at 9th level", "Magus arcana gained at 9th level"), True, "R2 normally before gained at")
    eq(trade_sentences("These bonus spells replace the oracle's mystery bonus spells at these levels.")[0][2], True, "a bonus spells sentence is bare")
    eq(covers("the oracle's normal mystery bonus spells at these levels", "Mystery bonus spells at these levels"), True, "the oracles' bonus spells, renamed (ruling 22)")
    eq(covers("the ranger's second favored enemy", "2nd favored enemy"), True, "R3 spelled ordinal")
    eq(covers("the ranger's twentieth level feat", "20th level feat"), True, "R3 twentieth")
    eq(covers("the 10th-level wizard bonus feat", "10th-level bonus feat"), True, "R5 class name after Nth-level")
    eq(covers("gun training 1 to 4", "Gun training 1-4"), True, "R6 range")
    eq(covers("gun training 1, 2, 3, and 4", "Gun training 1-4"), True, "R6 range against a list")
    eq(covers("poison resistance +2, +4, and +6, as well as poison immunity", "poison immunity"), True, "R7 as well as")
    eq(trade_sentences("This ability replaces cantrips, but the arcanist gains detect magic and read magic.")[0][1], "cantrips", "R8 phrase ends at but")
    eq(trade_sentences("This ability replaces the mutagen class ability (a mindchemist cannot create mutagens unless he selects mutagen).")[0][1], "the mutagen class ability", "R9 aside")
    eq(trade_sentences("This ability replaces bravery (see page 4).")[0][1], "bravery (see page 4)", "R9 a short parenthesis stays")
    eq(covers("the sacred shield's holy champion ability", "Holy champion"), True, "R10 possessor phrase")
    eq(covers("the sacred shield's holy champion ability", "Sacred shield"), False, "R10 the possessor is not a name")
    eq(print_md(PrintFeature("X", [[("confess (Advanced Player's Guide 212; 4th), shield (Ultimate Magic, 2nd), ki shout (14th, Ultimate Magic).", False, False)]], 1),
                [], set(), "ref/x")[0], "confess (4th), shield (2nd), ki shout (14th).", "ruling 26: the book reference in a list goes, the level stays")
    eq(covers("unarmed strike and brawler's flurry", "Unarmed strike"), True, "R10 is an alternative reading: the plain one names both")
    eq(covers("unarmed strike and brawler's flurry", "brawler's flurry"), True, "R10 plain reading of a possessor name")
    eq(trade_asides("This ability replaces swift alchemy (the deep bomber gains swift alchemy at 18th level and never gains instant alchemy).")[0],
       ("replaces", "the deep bomber gains swift alchemy at 18th level and never gains instant alchemy"), "ruling 29 aside")
    eq(any(covers(x, "hunter tactics") for x in prose_sentences("This ability alters animal companion. The hunter tactics class ability allows her to grant feats.")), True,
       "ruling 28 prose")
    eq(any(covers(x, "hunter tactics") for x in prose_sentences("This ability replaces bravery. It works as the hunter tactics class ability.")), False,
       "ruling 28: a comparison states nothing")
    eq(trade_sentences("This ability replaces tactician and alters the standard cavalier's selection of bonus feats.", "Bonus Feats (Ex)"),
       [("replaces", "tactician", False), ("alters", "the standard cavalier's selection of bonus feats", False)], "R11 two verbs, two sentences")
    eq(trade_sentences("Sermonic performance replaces inspire courage.", "Sermonic Performance (Su)"), [("replaces", "inspire courage", False)], "R12 the heading is a subject")
    # the reader of app #716 (R16 to R19): a second clause with a subject, ", and counts as", an aside inside a phrase, "alter self"
    eq(trade_sentences("This ability alters flurry of blows and ki pool, and it replaces the bonus feat gained at 10th level."),
       [("alters", "flurry of blows and ki pool", False), ("replaces", "the bonus feat gained at 10th level", False)], "R16 ', and it replaces'")
    eq(trade_sentences("This ability alters smite evil, and this also replaces aura of good."),
       [("alters", "smite evil", False), ("replaces", "aura of good", False)], "R16 'this also'")
    eq(trade_sentences("This ability replaces arcane pool, and counts as arcane pool for the purpose of feats, abilities, and class features."),
       [("replaces", "arcane pool", False)], "R17 ', and counts as' ends the phrase")
    eq(trade_sentences("This ability replaces alchemy (which also includes bombs, extracts, and mutagen) and Throw Anything."),
       [("replaces", "alchemy and Throw Anything", False)], "R18 an aside inside the phrase")
    eq(trade_asides("This ability replaces alchemy (which also includes bombs, extracts, and mutagen) and Throw Anything."),
       [("replaces", "which also includes bombs, extracts, and mutagen")], "R18 the aside states the same-op trades")
    eq(trade_sentences("This ability alters hunter's bond and replaces specific ranger abilities as indicated below."),
       [("alters", "hunter's bond", False)], "ruling 40: 'as indicated below' is a cross-reference, no trade")
    eq(trade_sentences("This ability replaces specific ranger abilities as indicated below."), [], "ruling 40: alone, it names no trade")
    eq(trade_sentences("This ability replaces woodland stride as indicated by the table."), [("replaces", "woodland stride as indicated by the table", False)], "ruling 40: only 'as indicated below'")
    eq(trade_sentences("This ability functions like alter self, except as noted here. This ability alters alchemy."),
       [("alters", "alchemy", False)], "R19 'alter self' is the spell")
    eq(trade_sentences("This ability functions as alter self, beast shape IV, or giant form II, as appropriate."), [], "R19 no verb at all")
    # the list expansion of suspended hyphens (app #727)
    eq(expand_suspended("the 4th- and 14th-level vigilante talents and the 9th- and 19th-level social talents"),
       "the 4th-level vigilante talents, 14th-level vigilante talents, the 9th-level social talents, 19th-level social talents", "two suspended lists, each against its own tail")
    eq(expand_suspended("low- and high-level"), "low-level, high-level", "a non-ordinal stem takes the generic hyphen tail")
    eq(expand_suspended("the 4th- and low-light vision"), "the 4th-, low-light vision", "a suspended ordinal takes only an ordinal tail: no tail, no expansion")
    eq(expand_suspended("1st-level hexes, 4th-"), "1st-level hexes, 4th-", "a trailing suspended item stays: no backward tail")
    eq(expand_suspended("bonus feats gained at 2nd, 6th, and 10th levels"), "bonus feats gained at 2nd, 6th, and 10th levels", "no suspended item: unchanged")
    eq(covers("the 4th- and 14th-level vigilante talents and the 9th- and 19th-level social talents", "9th- and 19th-level social talents"), True, "a name against its own list")
    eq(trade_sentences("This ability replaces arcane pool, and it counts as arcane pool for feats."), [("replaces", "arcane pool", False)], "R17 ', and it counts as'")
    eq(trade_sentences("This ability alters self, except as noted here."), [("alters", "self, except as noted here", False)], "R19 'alters self' is not skipped")
    eq(trade_sentences("This ability alters self-sufficiency."), [("alters", "self-sufficiency", False)], "R19 'self-' is not skipped")
    eq(finish_text("gain DR 5/ cold iron and 1/ round for law/ chaos", set()), "gain DR 5/cold iron and 1/round for law/chaos", "a slash at a line end joins the next word")
    eq(join_wrapped(["At 12th level, fey eidolons gain DR 5/", "cold iron. They also grow wings, gaining"], set()), ["At 12th level, fey eidolons gain DR 5/cold iron. They also grow wings, gaining"], "a slash at a line end joins the next line of a narrow column")
    eq(finish_text("as \x01possession\x02 (see page 181)\x01.\x02 To use", set()), "as \x01possession\x02 (see page 181). To use", "the period of an italic run of its own is plain")
    eq(finish_text("a \x01conductive\x02\x01, \x02\x01defending\x02", set()), "a \x01conductive\x02, \x01defending\x02", "a comma between italic words is plain")
    eq(trade_sentences("Sermonic performance replaces inspire courage.", ""), [], "R12 without the heading it is prose")
    eq(trade_sentences("This ability replaces tactician and changes the cavalier's feats.")[0][1], "tactician and changes the cavalier's feats", "ruling 25: a second `changes` is no verb")
    eq(trade_sentences("This ability changes the Arcane Pool class feature and replaces the magus arcana gained at 3rd level."),
       [("alters", "the Arcane Pool class feature", False), ("replaces", "the magus arcana gained at 3rd level", False)], "ruling 25 changes")
    # ruling 24: ruling A per operation; ruling 23: a proficiency change stored as alters needs no sentence
    trades = [{"alters": "Teamwork feats"}]
    by, problems = assign_by(trades, [{"anchor": "p", "head": "Teamwork Feats", "print": "This ability replaces solo tactics.", "import_trades": []}], [])
    eq((by, problems), ({0: ["p"]}, ["Teamwork Feats: the sentence \"This ability replaces solo tactics\" names no trade"]), "ruling A reads per operation")
    by, problems = assign_by([{"alters": "Heavy armor", "feature": "weapon-and-armor-proficiencies"}], [{"anchor": "a", "head": "A", "print": "x"}], [])
    eq((by, problems), ({0: []}, []), "a proficiency alters needs no sentence")
    # a step trade that a longer step-list trade covers is named only by its own sentence (Unarmed Fighter, p. 48)
    trades = [{"replaces": "Weapon training 1, 2, 3, and 4"}, {"replaces": "Weapon training 3"}]
    feats = [{"anchor": "a", "head": "A", "print": "This ability replaces weapon training 1, 2, 3, and 4."},
             {"anchor": "b", "head": "B", "print": "This ability replaces weapon training 3."}]
    by, _ = assign_by(trades, feats, [])
    eq(by, {0: ["a"], 1: ["b"]}, "a step inside a longer step list is not named by the longer sentence")
    # asterisk marks: the whole mark goes when the key is absent, stays when the entry prints it; a "(see ...)" stays
    pf = PrintFeature("Rage Powers", [[("Choose boasting taunt**, guarded life*, and a feat (see the Stealth skill).", False, False)]], 28)
    text, _, notes = print_md(pf, [], set(), "ref/arc-barbarian/armored-hulk")
    eq(text, "Choose boasting taunt, guarded life, and a feat (see the Stealth skill).", "both stars of a mark go, a cross-reference stays")
    text, _, notes = print_md(pf, [], set(), "ref/arc-fighter/crusader", True)
    eq(text.count("\\*"), 3, "the marks stay when the key is printed")
    pf = PrintFeature("Bullet Deflection (Ex)", [[("(including the alchemist's bomb class ability; ", False, False), ("Advanced Player's Guide", False, True), (" 28). It works.", False, False)]], 50)
    text, _, notes = print_md(pf, [("alchemist's", "ref/class/alchemist")], set(), "ref/arc-gunslinger/gun-tank")
    eq(text, "(including the [alchemist's](ref/class/alchemist) bomb class ability). It works.", "ruling 26: a bare book citation goes, the link stays")
    eq(finish_text("gains DR 5/\u2014 against ranged attacks, 1st\u2014 _spell_", set()), "gains DR 5/\u2014 against ranged attacks, 1st\u2014_spell_", "an em dash joins the next line after a word, not after DR 5/")
    eq(finish_text("adds Sahir- Afiyun (see page 18)", set()), "adds Sahir-Afiyun (see page 18)", "a compound of two capitalized words that a line end split keeps its hyphen without a blank")
    eq(finish_text(I_OPEN + "3rd" + I_CLOSE + "\u2014 blue whinnis", set()), I_OPEN + "3rd" + I_CLOSE + "\u2014blue whinnis", "an em dash after an italic label joins the next line without a blank (review of #342)")
    # a mark in the middle of a line keeps the blank of its word space; before a comma it keeps none; at a line end the blank joins the line
    bk = Book({"1": 16}, {1: [(500, 108, 1, "the Lingering Performance", 137), (501, 245, 1, SUPERSCRIPT + " ", 17), (500, 263, 1, "feat, and", 50),
                              (520, 108, 1, "simulacrum", 60), (521, 170, 1, SUPERSCRIPT, 15), (520, 190, 1, ", then", 40),
                              (540, 108, 1, "or vanish", 60), (541, 170, 1, SUPERSCRIPT, 15)]}, {}, set())
    got = ["".join(t for t, _, _ in ln["runs"]) for ln in page_lines(bk, 1)]
    eq(got, ["the Lingering Performance feat, and", "simulacrum, then", "or vanish "], "the blank of a superscript mark")
    eq(finish_text("the law/ chaos axis and a thief \u2019s broad study", set()), "the law/chaos axis and a thief's broad study", "a slash at a line end, a spaced apostrophe")
    rows_t = [{"anchor": "a", "print": "a _mirror image_ and a [grease](x) spell"}, {"anchor": "b", "print": "he casts _mirror image_ too"}]
    eq((place_elsewhere(rows_t, "mirror image", "ref/spell/mirror-image"), rows_t[0]["print"]), ("a", "a _[mirror image](ref/spell/mirror-image)_ and a [grease](x) spell"), "a link inside italics")
    rows_f = [{"anchor": "a", "print": "10 + 1/2 the monk's level"}]
    eq((place_elsewhere(rows_f, "1", "ref/arc-monk/qinggong-monk#footnote-i"), rows_f[0]["print"]), (None, "10 + 1/2 the monk's level"), "a footnote link of a dropped section stays out")
    # a section ends at a parenthesized type title (owner review of batch 3), not only at an archetype title
    blocks = [Para("title", [("SILVER BALLADEER (BARD ARCHETYPE)", True, False)], 1, 0, 18), Para("para", [("Text.", False, False)], 1, 0),
              Para("title", [("ORDER OF THE SHROUD (CAVALIER ORDER)", True, False)], 1, 0, 18), Para("para", [("Order text.", False, False)], 1, 0)]
    eq(len(find_section(blocks, "Silver Balladeer", set()) or []), 2, "a type title ends the section")
    # a parenthesis that has words of its own stays; a bare page citation goes where the corpus links the name before it, and stays
    # where no link takes its place (owner ruling 26, Opus review of #329)
    pf = PrintFeature("Hidden Magic (Sp)", [[("Items (as if he had cast greater magic aura; see page 219) and mutagen (page 83) and arbitrament (Core Rulebook page 469) end.", False, False)]], 67)
    text, _, notes = print_md(pf, [("mutagen", "ref/discovery/mutagen")], set(), "ref/arc-monk/black-asp")
    eq(text, "Items (as if he had cast greater magic aura; see page 219) and [mutagen](ref/discovery/mutagen) and arbitrament (Core Rulebook page 469) end.", "a citation with words stays, a linked bare one goes, an unlinked one stays")
    # a link that covers part of the phrase still takes the citation of the thing it names; a class or possessive link does not
    # (owner ruling 26, Muse review of #335)
    def cited(text_in, links_in, entry="ref/arc-monk/black-asp"):
        return print_md(PrintFeature("Hidden Magic (Sp)", [[(text_in, False, False)]], 67), links_in, set(), entry)[0]
    eq(cited("She gains a bonus when performing a steal combat maneuver (Advanced Player's Guide 322) at once.", [("steal", "ref/rule/steal")]),
       "She gains a bonus when performing a [steal](ref/rule/steal) combat maneuver at once.", "a link on the first word of the phrase takes the citation")
    eq(cited("He uses the alchemist's mutagen ability (Advanced Player's Guide 28) daily.", [("alchemist's", "ref/class/alchemist")]),
       "He uses the [alchemist's](ref/class/alchemist) mutagen ability (Advanced Player's Guide 28) daily.", "a possessive link keeps it")
    eq(cited("She has the cavalier class feature (Advanced Player's Guide 34).", [("cavalier", "ref/class/cavalier")]),
       "She has the [cavalier](ref/class/cavalier) class feature (Advanced Player's Guide 34).", "a class link keeps it")
    eq(cited("It is a black blade. It advances as a black blade (Ultimate Magic 47) here.", [("black blade", "ref/arc-magus/bladebound")]),
       "It is a [black blade](ref/arc-magus/bladebound). It advances as a black blade here.", "a second mention of a linked name of the paragraph loses its citation")
    eq(cited("Bards cast spells, just as a bard does. See the bard (Core Rulebook 35) for more.", [("bard", "ref/class/bard")]),
       "Bards cast spells, just as a [bard](ref/class/bard) does. See the bard (Core Rulebook 35) for more.", "a pointer (see) keeps it")
    eq(cited("It uses the mutagens' strength (Advanced Player's Guide 28) daily.", [("mutagens'", "ref/class/alchemist")]),
       "It uses the [mutagens'](ref/class/alchemist) strength (Advanced Player's Guide 28) daily.", "a plural possessive keeps it")
    eq(cited("It takes Expert Driver (water vehicles only; Ultimate Combat 100) too.", [("Expert Driver", "ref/feat/expert-driver")]),
       "It takes [Expert Driver](ref/feat/expert-driver) (water vehicles only) too.", "a link in front of the parenthesis takes its book citation")
    eq(cited("It is an ability (including a bomb ability; Advanced Player's Guide 28) here.", []),
       "It is an ability (including a bomb ability; Advanced Player's Guide 28) here.", "an unlinked parenthesis keeps its book citation")
    eq(cited("A steal is easy. She makes a steal combat maneuver (Advanced Player's Guide 322) now.", [("steal", "ref/rule/steal")]),
       "A [steal](ref/rule/steal) is easy. She makes a steal combat maneuver (Advanced Player's Guide 322) now.", "a mention that the link does not cover keeps it")
    eq(cited("She attracts phantoms like a spiritualist (Occult Adventures 72), though she rests.", [("spiritualist", "ref/class/spiritualist")]),
       "She attracts phantoms like a [spiritualist](ref/class/spiritualist), though she rests.", "a class link right before the citation takes it")
    eq(cited("It gets implements from the occultist class (Occult Adventures 47).", [("implements", "ref/ability/implements"), ("occultist", "ref/class/occultist")]),
       "It gets [implements](ref/ability/implements) from the [occultist](ref/class/occultist) class (Occult Adventures 47).", "the nearest link decides")
    eq(cited("It acts as the gunsmith ability (Ultimate Combat 9).", [("gunsmith", "ref/class/gunslinger#gunsmith")]),
       "It acts as the [gunsmith](ref/class/gunslinger#gunsmith) ability.", "a link to one thing of a class takes it")
    eq(cited("Deathwatch, death ward, and arbitrament (page 39) end.", [("death ward", "ref/spell/death-ward")]),
       "Deathwatch, [death ward](ref/spell/death-ward), and arbitrament (page 39) end.", "a comma between the link and the citation keeps it")
    eq(cited("A tight space where her head fits but her shoulders do not (Core Rulebook 95–96).", [("Escape Artist", "ref/skill/escape-artist")], "ref/arc-rogue/heister"),
       "A tight space where her head fits but her shoulders do not.", "an edge citation of the list is dropped")
    # ruling 44: a section whose head is a table title is folded behind the section it names, the head as a bold line
    rows_ = [{"anchor": "alignment", "head": "Alignment", "print": "A paragraph.", "status": "draft", "notes": []},
             {"anchor": "table-1-1-pacts", "head": "Table 1–1: Planar Pacts", "print": "|A|B|\n|---|---|\n|1|2|", "status": "print", "notes": []},
             {"anchor": "planar-pact", "head": "Planar Pact (Su)", "print": "Text.", "status": "print", "notes": []}]
    probs_: list[str] = []
    fold_table_sections(rows_, {("ref/arc-witch/pact-witch", "table-1-1-pacts"): ("fold-into:alignment", "why")}, "ref/arc-witch/pact-witch", probs_)
    eq([r["anchor"] for r in rows_], ["alignment", "planar-pact"], "the table section is gone")
    eq(rows_[0]["print"], "A paragraph.\n\n**Table 1–1: Planar Pacts**\n\n|A|B|\n|---|---|\n|1|2|", "the title is a bold line directly above the table")
    eq((rows_[0]["status"], probs_), ("print", []), "the target takes print's text")
    fold_table_sections(rows_, {("ref/arc-witch/pact-witch", "gone"): ("fold-into:alignment", "why")}, "ref/arc-witch/pact-witch", probs_)
    eq(len(probs_), 1, "a fold of a section that is not there is a problem")
    with tempfile.TemporaryDirectory() as tmp_:
        (Path(tmp_) / "scripts").mkdir()
        decisions_path(Path(tmp_), "bk").write_text("\t".join(DECISION_HEADER) + "\ne\ta\tfold-into:x\tn\n", encoding="utf-8")
        eq(read_decisions(Path(tmp_), "bk"), {("e", "a"): ("fold-into:x", "n")}, "the decision reader takes fold-into")
    eq(is_scaffold("Weapon and Armor Proficiencies") and is_scaffold("Class Skills") and is_scaffold("Skill Ranks per Level"), True, "scaffold variants")
    # the hold rules of the owner (phynics/cast-iron#540, after the Blood of the Ancients pilot): each is a switch, so each test runs the
    # same comparison with the rule off (the old script) and on
    def cmp_rule(rule: str, import_rows: str, printed: str, title: str = "Feature") -> tuple[str, str]:
        d_ = build_draft(parse_import("Intro.\n\n**Feature (Ex)**\n\n" + import_rows)[1][0])
        out_ = []
        for on in (False, True):
            RULES[rule] = on
            out_.append(compare_feature(d_, printed, set(), set(tokens(title))).status)
        RULES[rule] = True
        return out_[0], out_[1]

    # rule 2: a hyphen is a space
    RULES["hyphens"] = False
    HYPHEN_SPACES[0] = True
    off2 = (tokens("a mind-affecting 1st-detect effect"), tokens("a mind affecting effect"))
    RULES["hyphens"] = True
    on2 = (tokens("a mind-affecting 1st-detect effect"), tokens("a mind affecting 1 detect effect"))
    eq((off2[0] == off2[1], on2[0] == on2[1]), (False, True), "rule 2: mind-affecting is mind affecting, 1st-detect is 1 detect")
    eq(tokens("a full-round action and a 5-foot step"), ["full-round", "action", "5", "foot", "step"], "rule 2: full-round stays one word (an action)")
    HYPHEN_SPACES[0] = False
    eq(tokens("a mind-affecting effect"), ["mind-affecting", "effect"], "rule 2 is a rule of the comparison of a feature: other uses of the words keep the hyphen")
    d2_ = build_draft(parse_import("Intro.\n\n**Counter-Grapple (Ex)**\n\n**Gained:** At 1st Level\n\n**Passive:** A monk who is grappled gains a counter-grapple.\n")[1][0])
    eq(compare_feature(d2_, "At 1st level, a monk who is grappled gains a counter grapple.", set(tokens("Counter-Grapple")), set()).status, "print",
       "rule 2: the feature's own hyphenated name is dropped as its parts")
    eq(cmp_rule("hyphens", "**Gained:** At 1st Level\n\n**Passive:** The transmuter takes a 5-foot step.",
                "At 1st level, the transmuter takes a 10 foot step.")[1], "hold", "rule 2: a different number is still a hold")
    # rule 3: a `Prereq: Nth-level` row is print's "must be at least Nth level"
    imp3 = "**Ability:** A Jistkan artificer can use his arm. He cannot be fooled.\n\n**Prereq:** 13th-level magus and the _shielding arm_ magus arcana.\n"
    p3 = "A Jistkan artificer can use his arm. He cannot be fooled. The magus must be at least 13th level and have the shielding arm arcana before selecting this arcana."
    eq(cmp_rule("prereq", imp3, p3), ("hold", "print"), "rule 3: the same level")
    eq(cmp_rule("prereq", imp3, p3.replace("13th", "14th"))[1], "hold", "rule 3: another level is a hold")
    # rule 4: a `Usage` row that print says word for word is print's
    imp4 = "**Ability:** A hunter can speak with animals.\n\n**Usage:** She can use this ability no more than once per minute.\n"
    eq(cmp_rule("usage", imp4, "A hunter can speak with animals. She can use this ability no more than once per minute.")[1], "print", "rule 4: the row is in print")
    eq(cmp_rule("usage", imp4, "A hunter can speak with animals. She can use this ability twice per day.")[1], "hold", "rule 4: another usage is held")
    eq(cmp_rule("usage", "**Ability:** A knight calls an ally.\n\n**Usage:** A number of times per day equal to her Charisma modifier.\n",
                "A knight calls an ally. This ability can be used a number of times per day equal to her Charisma modifier.")[1], "print",
       "rule 4: the sentence that holds the row goes out of the comparison")
    # rule 1: values level by level
    imp1f = "**Gained:** At 1st Level\n\n**Passive:** A courtly knight gains a bonus on checks. This bonus is equal to 1 + one-fourth of her cavalier level.\n"
    p1 = "At 1st level, a courtly knight gains a +1 bonus on checks. At 4th level and every 4 cavalier levels thereafter, this bonus increases by 1 (to a maximum of +6 at 20th level)."
    eq(cmp_rule("values", imp1f, p1), ("hold", "print"), "rule 1: a fraction of the level against a progression with a base")
    eq(cmp_rule("values", imp1f, p1.replace("every 4", "every 5"))[1], "hold", "rule 1: another step is a hold")
    imp1r = ("**Gained:** At 2nd Level\n\n**Passive:** An aerochemist gains a +2 bonus on Fly checks.\n\n"
             "**At 5th Level:** This bonus increases to +4.\n\n**At 8th Level:** This bonus increases to +6.\n")
    p1r = "At 2nd level, an aerochemist gains a +2 bonus on Fly checks. This bonus increases to +4 at 5th level, and +6 at 8th level."
    eq(cmp_rule("values", imp1r, p1r), ("hold", "print"), "rule 1: rows against printed steps")
    eq(cmp_rule("values", imp1r, p1r.replace("+6 at 8th", "+5 at 8th"))[1], "hold", "rule 1: a row that differs is a hold")
    eq(cmp_rule("values", imp1r, p1r.replace("and +6 at 8th level", "and +6 at 8th level, and +8 at 11th level"))[1], "hold", "rule 1: a step on one side only is a hold")
    imp1b = ("**Gained:** At 5th Level\n\n**Passive:** A hunter's bonuses in the terrain begin.\n\n**At 10th Level:** The bonuses now increase by 4.\n\n"
             "**At 15th Level:** The bonuses now increase by 6.\n\n**At 20th Level:** The bonuses now increase by 8.\n")
    p1b = "At 5th level, a hunter's bonuses in the terrain begin. At 5th level and every 5 levels thereafter, these bonuses increase by 2."
    eq(cmp_rule("values", imp1b, p1b)[1], "print", "rule 1: rows that sum up to the printed progression")
    # rule 5: a corpus paragraph that print does not have is a hold; a title that no rule names ends the print span as a hold
    imp5 = "**Gained:** At 1st Level\n\n**Passive:** A fighter gains a bonus.\n\n**Info:** The extra paragraph that print never states anywhere in the book.\n"
    imp1d = ("**Gained:** At 4th Level\n\n**Passive:** A druid can see through 10 feet of fog.\n\n**At 8th Level:** His sight increases to 15 feet.\n\n"
             "**At 12th Level:** His sight increases to 20 feet.\n\n**At 16th Level:** His sight increases to 25 feet.\n\n**At 20th Level:** His sight increases to 30 feet.\n")
    p1d = "At 4th level, a druid can see through 10 feet of fog. This distance increases by 5 feet for every 4 levels beyond 4th."
    eq(cmp_rule("values", imp1d, p1d)[1], "print", "rule 1: a distance counts as a value, the base is the number before the progression")
    eq(cmp_rule("values", imp1d, p1d.replace("by 5 feet", "by 10 feet"))[1], "hold", "rule 1: another step of the distance is a hold")
    imp5 = ("**Gained:** At 1st Level\n\n**Passive:** A fighter gains a bonus.\n\n"
            "**Info:** The extra table that print never states anywhere in the book.\n\n|Blessing|Damage type|\n| --- | --- |\n|Air|Electricity|\n")
    eq(cmp_rule("dropped", imp5, "At 1st level, a fighter gains a bonus."), ("print", "hold"), "rule 5: a dropped table is a hold")
    ANY_TITLE_ENDS["on"] = True
    blocks5 = [Para("title", [("Jistkan Magistrate (Warpriest Archetype)", True, False)], 1, 0, 18), Para("para", [("Text.", False, False)], 1, 0),
               Para("title", [("Channel Element Damage", True, False)], 1, 0, 18), Para("para", [("Blessing", False, False)], 1, 0)]
    sec5 = find_section(blocks5, "Jistkan Magistrate", {"x"})
    eq((sec5.end, sec5.end_known), ("Channel Element Damage", False), "rule 5: a table title ends the span as an unknown end")
    blocks5[2] = Para("title", [("Jistkan Spells", True, False)], 1, 0, 18)
    sec5 = find_section(blocks5, "Jistkan Magistrate", {"x"})
    eq((sec5.end, sec5.end_known), ("Jistkan Spells", True), "rule 5: a chapter section ends the span, known")
    ANY_TITLE_ENDS["on"] = False
    # the printed trade sentences of a span, and the key that finds them in an entry
    span = [Para("para", [("Improvised Maneuver (Ex): At 4th level, a hinyasi learns. This combat maneuver still provokes.", False, False)], 1, 0),
            Para("para", [("This replaces knockout.", False, False)], 1, 0),
            Para("para", [("This alters the warpriest\u2019s blessings.", False, False)], 1, 0)]
    eq(printed_trade_sentences(span), ["This replaces knockout.", "This alters the warpriest\u2019s blessings."], "printed trade sentences")
    split_trade = [Para("para", [("This  ", False, False)], 1, 0), Para("para", [("ability replaces suggestion.", False, False)], 1, 0)]
    eq(printed_trade_sentences(split_trade), ["This ability replaces suggestion."], "a trade sentence split between extracted paragraphs")
    eq(letters_key("This alters the warpriest\u2019s _[blessings](ref/x/y)_.") in letters_key("a\n\nThis alters the warpriest's blessings.\n"), True, "a printed sentence is found in the entry")
    eq(letters_key("This replaces knockout.") in letters_key("At 4th level, a hinyasi learns to confound."), False, "a missing printed sentence")
    import tempfile
    from types import SimpleNamespace
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "scripts").mkdir()
        (root / "scripts" / "feature-prose-540-demo.sentences.tsv").write_text(
            "entry\tsentence\nref/arc-x/a\tThis replaces knockout.\nref/arc-x/a\tThis replaces the bonus feats gained at 2nd level.\n"
            "ref/arc-x/a\tThis ability replaces poison use.\n", encoding="utf-8")
        (root / "scripts" / "errata.tsv").write_text(
            "entry\tfield\tbook\tpage\tprinting\tprinted_value\n"
            "ref/arc-x/a\tf\tb\t1\tp\tText. This ability replaces poison use.\n", encoding="utf-8")
        ent = SimpleNamespace(id="ref/arc-x/a", body="A feature. This replaces the bonus feats\ngained at 2nd level.\n")
        got = missing_printed_sentences(root, "demo", [ent])
        eq([g.split('"')[1] for g in got], ["This replaces knockout."], "a printed sentence that the entry lacks; a recorded errata row explains another")
    # Blood of the Ancients: a title in small capitals sets a capital (size 18, top 469) and its small capitals (size 13, top 474) in one family
    cap = Book({"5": 18, "6": 13, "28": 13}, {1: [(469, 108, 5, "a", 13), (474, 122, 6, "erial", 43), (469, 165, 5, " a", 18), (474, 184, 6, "ssaulter", 71),
                                                  (492, 108, 28, "Body text starts here.", 200), (498, 400, 28, "x", 10)]}, {}, set(), fams={"5": "Didot", "6": "Didot", "28": "Nexus"})
    SMALL_CAP_TITLES["on"] = True
    got = ["".join(t for t, _, _ in ln["runs"]) for ln in page_lines(cap, 1)]
    SMALL_CAP_TITLES["on"] = False
    got_off = ["".join(t for t, _, _ in ln["runs"]) for ln in page_lines(cap, 1)]
    eq(got[0], "aerial assaulter", "a small-capital title is one line (the capital and its small capitals are 5 units apart)")
    eq(len(got_off), 4, "other books keep the tolerance of 4 units")
    # a chapter title that a page repeats unseen is not a title, and does not end the section
    big = Book({"7": 63, "28": 13}, {1: [(91, 108, 7, "mperiAlung", 200), (150, 108, 28, "Text of the first page.", 200)],
                                      2: [(91, 108, 7, "mperiAlungA", 200), (96, 150, 28, "maneuver against the enemy", 200)]}, {1: 20, 2: 21}, set(),
               fams={"7": "First-Order", "28": "Nexus"})
    SMALL_CAP_TITLES["on"] = True
    on_kinds = [b.kind for b in read_blocks(big, 1, 2)]
    SMALL_CAP_TITLES["on"] = False
    off_kinds = [b.kind for b in read_blocks(big, 1, 2)]
    eq((on_kinds, off_kinds), (["title", "para", "para"], ["title", "para", "title", "para"]), "a repeated chapter title is dropped")
    # in that book any title ends the section of an archetype
    ANY_TITLE_ENDS["on"] = True
    blocks = [Para("title", [("Aerial Assaulter (Fighter Archetype)", True, False)], 1, 0, 18), Para("para", [("Text.", False, False)], 1, 0),
              Para("title", [("Shory Runes", True, False)], 1, 0, 18), Para("para", [("Spells.", False, False)], 1, 0)]
    eq(len(find_section(blocks, "Aerial Assaulter", {"x"}) or []), 2, "any title ends the section")
    ANY_TITLE_ENDS["on"] = False
    eq(len(find_section(blocks, "Aerial Assaulter", {"x"}) or []), 4, "a sidebar title stays in the section of other books")
    # batches 6 to 9 (Player Companions): a chapter title above the body ends a section, and only in those books
    chap = Book({"23": 60, "24": 13}, {1: [(72, 105, 23, "Wardens of the Wild", 500), (150, 108, 24, "In the wilds of the world.", 300), (11, 497, 23, "Running head", 300)]},
                {1: 18}, set())
    CHAPTER_TITLES["on"] = True
    got = ["".join(t for t, _, _ in ln["runs"]) for ln in page_lines(chap, 1)]
    CHAPTER_TITLES["on"] = False
    got_off = ["".join(t for t, _, _ in ln["runs"]) for ln in page_lines(chap, 1)]
    eq((got, got_off), (["Wardens of the Wild", "In the wilds of the world."], ["In the wilds of the world."]),
       "a chapter title above the body is a line (the running head at the top is not), in the books that set it so")
    configure_book("healers-handbook")
    eq((CHAPTER_TITLES["on"], SMALL_CAP_TITLES["on"], ANY_TITLE_ENDS["on"]), (True, True, True), "a Player Companion of batches 6 to 9 reads its titles that way")
    configure_book("blood-of-the-ancients")
    eq((CHAPTER_TITLES["on"], SMALL_CAP_TITLES["on"]), (False, True), "Blood of the Ancients sets its chapter titles in the body")
    configure_book("ultimate-magic")
    eq((CHAPTER_TITLES["on"], SMALL_CAP_TITLES["on"], ANY_TITLE_ENDS["on"]), (False, False, False), "the other books read as before")
    # a printed book citation of another publication goes after a link that already names the thing, in the books of the new batches
    eq(strip_citations("positive blast (_Ultimate Wilderness_ 60) as"), "positive blast as", "a citation of Ultimate Wilderness")
    eq(strip_citations("corruption (Horror Adventures 14) progressing"), "corruption progressing", "a citation of Horror Adventures")
    eq(strip_citations("seven (_Pathfinder Player Companion: Heroes of the Wild_ 26) here"), "seven here", "a citation of a Player Companion")
    eq(strip_citations("a template (Bestiary 6 46), another (Inner Sea Bestiary 28\u201329)."), "a template, another.", "Bestiary 6 and Inner Sea Bestiary")
    eq(strip_citations("the grapple weapon (Adventurer's Guide 12)"), "the grapple weapon (Adventurer's Guide 12)", "a book that no pattern names stays")
    # review of #339: the class-table lookup (ruling 35 and 48), and the citation pass on the finished Markdown
    eq(first_level_key("1st studied target"), first_level_key("Studied target"), "a class table entry with an ordinal in front")
    eq(first_level_key("Shifter aspect, and all improvements to shifter aspect"), first_level_key("Shifter aspect"), "a name with all its improvements")
    eq(first_level_key("Shifter aspect and all improvements of shifter aspect"), "shifter aspect", "improvements of")
    eq(first_level_key("Wild shape"), "wild shape", "a plain name is unchanged")
    eq(first_level_key("Blessings (minor)"), first_level_key("Blessings"), "a parenthesis of the class table")
    eq(finish_text("a fortune-teller (see page 37)influences people", set()), "a fortune-teller (see page 37) influences people", "a blank behind a page reference")
    eq(first_level_key("The Brew Potion bonus feat"), first_level_key("Brew Potion"), "a bonus feat of a name is that name, as the class table writes it")
    eq(first_level_key("Bonus feats"), "bonu feat", "Bonus feats alone stays")
    eq(first_level_key("Deadeye deed") in {first_level_key(x) for x in FIRST_LEVEL_EXTRA["ref/class/gunslinger"]}, True, "a 1st-level deed")
    eq(first_level_key("Spontaneous casting") in {first_level_key(x) for x in FIRST_LEVEL_EXTRA["ref/class/druid"]}, True, "the druid's spontaneous casting")
    eq(final_citations("a _[spirit-bound blade](ref/spell/x)_ (_Pathfinder RPG Occult Adventures_ 186) for", "x"), "a _[spirit-bound blade](ref/spell/x)_ for",
       "a citation after a link in finished Markdown goes")
    eq(final_citations("a spirit-bound blade (_Pathfinder RPG Occult Adventures_ 186) for", "x"), "a spirit-bound blade (_Pathfinder RPG Occult Adventures_ 186) for",
       "a citation after an unlinked name stays")
    eq(final_citations("the [fey](ref/a) (see the Core Rulebook 12) and", "x"), "the [fey](ref/a) (see the Core Rulebook 12) and", "a cross-reference with see stays")
    for txt in ("a mutated defender can select from the following mutant talents, in addition to the vigilante talents normally available to him.",
                "A benefactor adds the following hexes to the list of shaman hexes she can choose from whenever she gains a new hex.",
                "to manipulate the time stream in a variety of ways listed below."):
        eq(bool(CHOICE_INTRO.search(txt)), True, "a lead-in that offers a choice from the sections that follow: " + txt[:30])
    eq(bool(CHOICE_INTRO.search("At 3rd level, the bonus increases by 1.")), False, "no choice in a plain feature")
    for txt in ("A winged marauder can select the following additional discovery.", "The following magus arcana can be selected by any magus who meets their prerequisites.",
                "The new talents below can also be taken by any rogue that meets their prerequisites.", "She can select the two hexes below."):
        eq(bool(CHOICE_INTRO.search(txt)), True, "review of #346: a lead-in of talents that a character chooses: " + txt[:30])
    # owner ruling 57: a whole class feature at a later level of the class table gives its level; a part (a trade of some levels or of a power) gives none
    tbl = class_table_levels(Path("."), "ref/class/none-such", {})
    eq(tbl, {}, "no class table, no levels")
    # review of #339: an edit replaces the text of a row, so applying it twice gives the same row; an edit that repeats a paragraph is an error
    row0 = {"print": "text that print gives", "status": "hold", "notes": ["a hold note", "level 1: x"]}
    ed = ("The edit text.\n\n- A list item.", "hand-written note")
    once = apply_edit(dict(row0, notes=list(row0["notes"])), ed)
    twice = apply_edit(dict(once, notes=list(once["notes"])), ed)
    eq((once, once["print"]), (twice, "The edit text.\n\n- A list item."), "applying an edit twice gives the same row")
    eq(apply_edit(dict(row0), None), row0, "no edit leaves the row")
    para = "This ability replaces the revelation gained at 7th level and nothing else of the class."
    eq(repeated_paragraphs(para + "\n\nOther text of the feature that is long enough to count.\n\n" + para), [para[:60]], "an edit that states a paragraph twice")
    eq(repeated_paragraphs(para + "\n\n" + para.replace("7th", "9th")), [], "two different paragraphs")
    # a box at the foot of a column (Psychic Anthology's Phantom Weapon Progression) runs to the end of the column when its rows are not set in
    mk = lambda text, size, col, left: {"size": size, "col": col, "left": left, "margin": 108, "runs": [(text, False, False)]}
    lines = [mk("Body text.", 13, 0, 108), mk("Phantom Weapon Progression", 20, 0, 108), mk("1st-2nd +0 10 6 5", 13, 0, 108), mk("3rd-4th +1 11 7 5", 13, 0, 108)]
    BOX_TITLES["titles"] = frozenset({squash("Phantom Weapon Progression")})
    BOX_TO_END["on"] = False
    main_off, box_off = split_boxes(lines)
    BOX_TO_END["on"] = True
    main_on, box_on = split_boxes(lines)
    BOX_TITLES["titles"] = frozenset()
    BOX_TO_END["on"] = False
    eq((len(main_off), len(box_off), len(main_on), len(box_on)), (3, 1, 1, 3), "a box of the foot of a column takes its rows when the book says so")
    eq("carried" in DECISIONS, True, "the decision for a section that an edit carries")
    # "This change remains in effect" is no trade sentence; "alters and replaces X" has no phrase of its own to cover
    eq(trade_sentences("This change remains in effect for 1 minute."), [], "a noun after This is no verb")
    eq(trade_sentences("This changes the sentence name.")[0][0], "alters", "changes is an alters verb")
    eq(LEVEL_FROM_PRINT[("ref/arc-oracle/hermit", "recluse-s-stride")][0], 1, "a level that print states in other words")
    # Blood of the Beast, Heroes of the High Court, Martial Arts Handbook (#540 batch of 2026-11-26)
    # a title in small capitals can stand 7 units from its capital (size 27 over size 19), and a class in a title can carry stray blanks
    cap2 = Book({"5": 27, "6": 19, "28": 13}, {1: [(696, 108, 5, "r", 14), (703, 123, 6, "oyal", 42), (696, 165, 5, " a", 28), (703, 194, 6, "lChemist", 82),
                                                   (730, 108, 28, "Body text starts here.", 200)]}, {}, set(), fams={"5": "Yngreena", "6": "Yngreena", "28": "Nexus"})
    SMALL_CAP_TITLES["on"] = True
    got2 = ["".join(t for t, _, _ in ln["runs"]) for ln in page_lines(cap2, 1)]
    SMALL_CAP_TITLES["on"] = False
    eq(got2[0], "royal alChemist", "a small-capital title of capitals 7 units above its small capitals is one line")
    ANY_TITLE_ENDS["on"] = True
    blocks = [Para("title", [("Prowler at Wor ld\u2019s End (Bloodr aGer)", True, False)], 4, 0, 20), Para("para", [("Text.", False, False)], 4, 0),
              Para("title", [("mesmerist triCks", True, False)], 4, 0, 20), Para("para", [("Tricks.", False, False)], 4, 0)]
    sec = find_section(blocks, "Prowler at World's End", {"x"})
    eq((len(sec or []), sec.end, sec.end_known), (2, "mesmerist triCks", True), "a class in small capitals with a stray blank names the archetype; a chapter section ends it, known")
    blocks[0] = Para("title", [("thronewarDen (GunslinGer  a) rChetype", True, False)], 8, 1, 27)
    eq(len(find_section(blocks, "Thronewarden", {"x"}) or []), 2, "the rest of a title after the name is a class, or a class and archetype")
    blocks = [Para("title", [("investeD reGent (monk arChetype)", True, False)], 22, 1, 27), Para("para", [("Text.", False, False)], 22, 1),
              Para("title", [("vesteD powers", True, False)], 22, 1, 27), Para("para", [("Powers.", False, False)], 22, 1),
              Para("title", [("2nD-level vesteD powers", True, False)], 23, 0, 21), Para("para", [("List.", False, False)], 23, 0),
              Para("title", [("vesteD feats", True, False)], 23, 1, 27), Para("para", [("Feats.", False, False)], 23, 1)]
    sec = find_section(blocks, "Invested Regent", {"x"})
    eq((len(sec or []), sec.end, sec.end_known), (6, "vesteD feats", True), "the box of the Vested Powers stays in the section of the archetype; the Vested Feats end it")
    ANY_TITLE_ENDS["on"] = False
    # a chapter title and an archetype title that follow one another in a column are two titles when their sizes differ
    two = Book({"1": 36, "2": 27, "3": 13}, {1: [(100, 468, 1, "ivInIty", 100), (150, 468, 2, "investeD reGent (monk arChetype)", 300), (190, 468, 3, "Text.", 100)]},
               {}, set(), fams={"1": "A", "2": "A", "3": "B"})
    SMALL_CAP_TITLES["on"] = True
    kinds2 = [(b.kind, b.size) for b in read_blocks(two, 1, 1)]
    SMALL_CAP_TITLES["on"] = False
    eq(kinds2, [("title", 36), ("title", 27), ("para", 0)], "a title of another size is a title of its own")
    eq(fix_ligatures("he gains 1 point of inf luence over him and f ighter", {"influence", "fighter"}), "he gains 1 point of influence over him and fighter",
       "a ligature pair after a word that ends in f")
    # review of #338: the class table of the ranger writes "1st favored enemy"; a lead after an opening sentence; "of 20th level"; a choice from what follows
    eq(first_level_key("1st favored enemy"), first_level_key("Favored enemy"), "a class table entry with an ordinal in front")
    eq(first_level_key("Favored enemy"), first_level_key("favored enemies"), "plural of the class table name")
    eq(LATER_LEAD.search("Eventually, a loyalist trains. At 5th level, a loyalist chooses one house.").group(1), "5", "a lead after an opening sentence")
    eq(OF_LEVEL.search("A fortune-finder of 20th level becomes a master explorer.").group(1), "20", "of Nth level in the first sentence")
    eq(bool(LATER_LEAD.search("At 5th level, a loyalist chooses.")), False, "a lead at the start is the ordinary lead")
    eq(bool(UPGRADE_WORDS.search("At 5th level, if the target is Large or larger, these bonuses increase by an additional 1.")), True, "a step of a feature is not its level")
    eq(bool(CHOICE_INTRO.search("An opportunist can select an edge from those listed below.")), True, "choices: from those listed below")
    eq(bool(CHOICE_INTRO.search("A serendipity shaman can select from any of the following hexes, in addition to general shaman hexes.")), True, "choices: of the following hexes")
    eq(bool(CHOICE_INTRO.search("A fighter can select any feat he qualifies for.")), False, "choices: no list follows")
    eq(bool(CHOICE_INTRO.search("A bard can select the following additional masterpieces.")), True, "choices: can select the following additional")
    eq(bool(CHOICE_INTRO.search("These talents can be selected by any rogue.")), True, "choices: can be selected by any")
    eq(bool(CHOICE_INTRO.search("The talent can also be taken by any ninja.")), True, "choices: can also be taken by any")
    eq(first_level_key("Blessings"), first_level_key("Blessings (minor)"), "a parenthesis after the name in the class table")
    eq(first_level_alt_key("Nature's bond"), first_level_key("Nature bond"), "a possessive kept as a word: Nature's bond is the druid's nature bond")
    # review of the batch of 2026-11-26: "can select the following slayer talents" is a choice; "receives this ability at 7th level"; spontaneous casting
    eq(bool(CHOICE_INTRO.search("A spiritslayer can select the following slayer talents, in addition to general slayer talents.")), True, "choices: select the following")
    eq(bool(re.match(r"[^.]*?\b(?:gains|receives)\s+(?:this|the\s+[\w' -]+?)\s+ability at (\d+)(st|nd|rd|th) level\b",
                     "A rivethun spirit channeler receives this ability at 7th level instead of at 3rd level.")), True, "receives this ability at Nth level")
    eq(bool(re.match(r"[^.]*?\b(?:gains|receives)\s+(?:this|the\s+[\w' -]+?)\s+ability at (\d+)(st|nd|rd|th) level\b",
                     "A toxin codexer gains the poison lore ability at 1st level.")), True, "gains the poison lore ability at Nth level")
    # a progression in print with a class word, or "he has", between the number and "levels"
    eq(progression_levels("This bonus increases by 1 for every 4 fighter levels beyond 2nd."), {6, 10, 14, 18}, "progression with a class word")
    eq(progression_levels("This bonus increases by 1 for every 4 levels he has beyond 2nd."), {6, 10, 14, 18}, "progression with 'he has'")
    eq(cmp_rule("values", "**Gained:** At 2nd Level\n\n**Passive:** A high guardian gains a +1 bonus.\n\nAt 6th level: This bonus increases to +2.\n\n"
                "At 10th level: This bonus increases to +3.\n\nAt 14th level: This bonus increases to +4.\n\nAt 18th level: This bonus increases to +5.\n",
                "At 2nd level, a high guardian gains a +1 bonus. This bonus increases by 1 for every 4 fighter levels beyond 2nd.")[1], "print",
       "rule 1: a printed step 'for every 4 fighter levels beyond 2nd' equals the corpus rows")
    # "Beginning at 5th level" inside a paragraph is "At 5th level"; "This ability modifies X." is a trade-like sentence, not a rule word
    eq(cmp_rule("values", "**Passive:** A swarm monger bonds with a familiar.\n\n**At 5th Level:** Creatures take 1d6 damage.\n",
                "A swarm monger bonds with a familiar. Beginning at 5th level, creatures take 1d6 damage.")[1], "print", "Beginning at Nth level is wording")
    eq(cmp_rule("values", "**Ability:** A scavenger can use inspiration.\n\n**Alters:** Inspiration\n",
                "A scavenger can use inspiration. This ability modifies inspiration.")[1], "print", "a 'modifies' sentence is not a rule word")
    eq(strip_trade_sentences("This ability works like modify memory to erase the memory of an event. The rest stays.").strip(),
       "This ability works like modify memory to erase the memory of an event. The rest stays.", "the spell modify memory is not a trade verb")
    # a citation of a Player Companion, a Campaign Setting or an Adventure Path after a link goes (owner ruling 26)
    eq(drop_linked_citation(CITE_BOOK, "[lunar](ref/mystery/lunar) (Pathfinder Player Companion: Blood of the Moon 28), [nature](ref/mystery/nature)",
                            [("lunar", "ref/mystery/lunar")]), "[lunar](ref/mystery/lunar), [nature](ref/mystery/nature)", "a Player Companion citation after a link goes")
    eq(drop_linked_citation(CITE_BOOK, "[volcano](ref/mystery/volcano) (Pathfinder Adventure Path #95: Anvil of Fire 72)",
                            [("volcano", "ref/mystery/volcano")]), "[volcano](ref/mystery/volcano)", "an Adventure Path citation after a link goes")
    eq(printed_trade_sentences([Para("para", [("This deed replaces the bleeding wound deed.", False, False)], 1, 0)]), ["This deed replaces the bleeding wound deed."],
       "a printed trade sentence of a deed")
    eq(join_wrapped(["the vox's mesmerist spells use both", "thought and verbal components. Next."], set()), ["the vox's mesmerist spells use both thought and verbal components. Next."], "wrapped sidebar lines join")
    # ruling 11: the Special column of the class table, with its suffixes, never a spell-slot or fast-movement column
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "entries" / "class").mkdir(parents=True)
        (Path(tmp) / "entries" / "class" / "witch.md").write_text(
            "|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|0|1st|\n|---|---|---|---|---|---|---|---|\n"
            "|1st|+0|+0|+0|+2|Cantrips, hex, witch's familiar|3|1|\n", encoding="utf-8")
        (Path(tmp) / "entries" / "class" / "monk.md").write_text(
            "|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|Flurry|Fast Movement|\n|---|---|---|---|---|---|---|---|\n"
            "|1st|+0|+2|+2|+2|Bonus feat, flurry of blows, _[stunning fist](ref/x)_|-1/-1|+0 ft.|\n", encoding="utf-8")
        (Path(tmp) / "entries" / "class" / "paladin.md").write_text(
            "|Level|Base Attack Bonus|Special|\n|---|---|---|\n|1st|+1|Aura of good, smite evil 1/day, channel energy 1d6, bomb 1d6|\n", encoding="utf-8")
        eq(sorted(class_first_level(Path(tmp), "ref/class/witch", {})), ["cantrip", "familiar", "hex"], "Special column of a caster")
        eq("+0 ft." in class_first_level(Path(tmp), "ref/class/monk", {}), False, "never fast movement")
        eq("flurry of blow" in class_first_level(Path(tmp), "ref/class/monk", {}), True, "monk special")
        eq(first_level_key("Bombs") in class_first_level(Path(tmp), "ref/class/paladin", {}), True, "a plural trade name, a suffixed table name")
        eq(first_level_key("Smite evil") in class_first_level(Path(tmp), "ref/class/paladin", {}), True, "smite evil 1/day")
        eq(first_level_key("Channel energy") in class_first_level(Path(tmp), "ref/class/paladin", {}), True, "channel energy 1d6")
    # links: the longer label first, the same case first
    got, lost = apply_links("a lesser planar ally and a planar ally later", [("planar ally", "ref/spell/planar-ally"), ("lesser planar ally", "ref/spell/lesser-planar-ally")])
    eq(got, "a [lesser planar ally](ref/spell/lesser-planar-ally) and a [planar ally](ref/spell/planar-ally) later", "longer label first")
    got, _ = apply_links("an animal companion and the Animal, Earth domains", [("Animal", "ref/domain/animal")])
    eq(got, "an animal companion and the [Animal](ref/domain/animal), Earth domains", "same case first")
    # ligature gap in a head, a digit before a line-end hyphen
    eq(fix_ligatures("Humanoid (half ling)", {"halfling"}), "Humanoid (halfling)", "ligature in a head")
    eq(fix_hyphens("the 4th- level list", set()), "the 4th-level list", "digit before a hyphen")
    eq(fix_hyphens("class- or level-based", set()), "class- or level-based", "a suspended hyphen stays")
    # stale rows: a changed span, and a name that is gone
    body = "Intro.\n\n**Alpha (Ex)**\n\n**Passive:** One.\n\n**Beta (Ex)**\n\n**Passive:** Two.\n"
    ent = Entry(Path("x.md"), "ref/x", "X", "archetype", "", body, {}, None, "", [])
    feats_ = parse_import(body)[1]
    rows_ = [{"feature": "Alpha (Ex)", "span_sha256": feats_[0].span_sha()}, {"feature": "Beta (Ex)", "span_sha256": feats_[1].span_sha()}]
    eq(stale_rows(ent, rows_), [], "no stale row")
    eq(stale_rows(ent, [dict(rows_[0], span_sha256="0" * 64), rows_[1]]), ["Alpha (Ex)"], "a changed span is stale")
    eq(stale_rows(ent, rows_ + [{"feature": "Gamma (Ex)", "span_sha256": "1" * 64}]), ["Gamma (Ex)"], "a name that is gone is stale")
    # words that matter are not ignored; words that do not are
    eq(len(tokens("any all each both either neither")), 6, "quantifiers are rule words")
    eq(tokens("the she its but gains however"), [], "articles, pronouns and connectives are ignored")
    eq(balance_marks(f"a {I_OPEN}b{I_CLOSE} c d{I_CLOSE} e {I_OPEN}f"), f"a {I_OPEN}b{I_CLOSE} c d e f", "an italic mark without a partner is dropped")
    # an opening note that print does not have
    eq(unprinted_notes([["Intro text."], ["> _**Note:** This is a rogue archetype, and has no relation to the class."]], ["Intro text."]), [1], "an unprinted note")
    eq(unprinted_notes([["> kept words here and more"]], ["kept words here and more"]), [], "a printed note stays")
    # ruling 15: an option item is a subheading, not a feature; a tagged sub-power stays a feature
    eq(is_option_head("Humanoid (dwarf)", False), True, "an italic untagged head is an option")
    eq(is_option_head("Form of the Bear", False), True, "a form is an option")
    eq(is_option_head("Rallying Cry (Su)", False), False, "a tagged sub-power is a feature")
    eq(is_option_head("Adaptation (Ex)", True), False, "a bold head is a feature")
    ent = Entry(Path("x.md"), "ref/x", "X", "archetype", 'id = "ref/x"\n\n[fields]\nkind = "archetype"\ntrades = [\n  { replaces = "Trapfinding", feature = "trapfinding" },\n]', "Intro.\n",
              {"fields": {"trades": [{"replaces": "Trapfinding", "feature": "trapfinding"}]}}, None, "", [])
    props = {"feature": [
        {"anchor": "adaptation", "head": "Adaptation (Ex)", "listed": True, "level": 3, "print": "At 3rd level, a ranger learns a type. This ability replaces trapfinding."},
        {"anchor": "aberration", "head": "Aberration", "listed": False, "parent": "adaptation", "print": "amphibious, darkvision 60 ft."},
        {"anchor": "fey", "head": "Fey", "listed": False, "parent": "adaptation", "print": "Iron Will."},
    ], "opening": []}
    out = convert_text(ent, props, [{"anchor": f["anchor"], "status": "print"} for f in props["feature"]])
    eq(out.count("features = [") == 1 and 'anchor = "adaptation", level = 3' in out and "anchor = \"aberration\"" not in out, True, "options are not listed")
    eq("### Aberration {#aberration}" in out and "## Adaptation (Ex) {#adaptation}" in out, True, "options are ### subheadings")
    eq('by = ["adaptation"]' in out, True, "the trade names the feature")
    props["feature"][1]["print"] = "amphibious. This ability replaces trapfinding."
    props["feature"][0]["print"] = "At 3rd level, a ranger learns a type."
    out = convert_text(ent, props, [{"anchor": f["anchor"], "status": "print"} for f in props["feature"]])
    eq('by = ["adaptation"]' in out, True, "a trade sentence of an option belongs to its feature")
    # owner rulings 48 and 50: a feature with no printed level that alters a whole 1st-level feature of the class table is level 1; a part is none
    with tempfile.TemporaryDirectory() as tmp:
        root_ = Path(tmp)
        (root_ / "entries" / "class").mkdir(parents=True)
        (root_ / "entries" / "arc-cavalier").mkdir(parents=True)
        (root_ / "entries" / "class" / "cavalier.md").write_text(
            "|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|\n|---|---|---|---|---|---|\n|1st|+1|+2|+0|+0|Challenge 1/day, mount, order, tactician|\n",
            encoding="utf-8")
        trades_ = [{"alters": "Mount", "feature": "mount"}, {"alters": "Weapon proficiencies", "feature": "wp"}, {"alters": "The cavalier's order", "feature": "order"},
                   {"replaces": "Tactician", "feature": "tactician"}]
        fld_ = "".join("  { " + ("alters" if "alters" in t_ else "replaces") + ' = "' + (t_.get("alters") or t_.get("replaces")) + '", feature = "' + t_["feature"] + '" },\n' for t_ in trades_)
        ent_ = Entry(root_ / "entries" / "arc-cavalier" / "x.md", "ref/arc-cavalier/x", "X", "archetype",
                     'id = "ref/arc-cavalier/x"\n\n[fields]\nkind = "archetype"\ntrades = [\n' + fld_ + "]", "Intro.\n", {"fields": {"trades": trades_}}, None, "", ["ref/class/cavalier"])

        def row_(a, txt):
            return {"anchor": a, "span": "", "page": "", "pseudo": False, "draft": "", "level_import": None, "head": a, "print": txt, "status": "print",
                    "notes": [], "listed": True, "name": a, "option": False}
        out_ = finalize(ent_, {"rows": [row_("steed", "A rider gets a steed. This ability alters mount."), row_("arms", "A rider drills. This ability alters weapon proficiencies."),
                                       row_("code", "A rider swears a code. This ability alters the cavalier's order."), row_("tact", "A rider plans. This ability replaces tactician.")],
                               "problems": [], "opening": [], "decisions": {}, "edits": {}})
        eq([r["level"] for r in out_["rows"]], [1, None, 1, 1], "ruling 50: altering the whole mount or order is level 1, altering a part (weapon proficiencies) none; replacing stays level 1")
    # front matter edit
    front = 'id = "x"\n\n[fields]\nkind = "archetype"\ntrades = [\n  { replaces = "Bravery", feature = "bravery" },\n  { replaces = "Armor training", feature = "armor-training" },\n]'
    got = edit_front(front, [{"anchor": "a", "level": 2, "listed": True}, {"anchor": "b", "listed": True}], {0: ["a"], 1: []}, 2)
    eq("features = [\n  { anchor = \"a\", level = 2 },\n  { anchor = \"b\" },\n]" in got, True, "features written")
    eq('{ replaces = "Bravery", feature = "bravery", by = ["a"] },' in got, True, "by written")
    eq('{ replaces = "Armor training", feature = "armor-training" },' in got, True, "no by for the opening text")
    for scaffold in ("Bonus Feats", "Weapon and Armor Proficiency", "Companion Type", "AC:"):
        eq(is_scaffold(scaffold), True, f"scaffold {scaffold}")
    eq(is_scaffold("Bonus Feat"), False, "the app's list has no singular")
    eq((is_scaffold("Skills"), is_scaffold("Alignment")), (True, True), "ruling 19: Skills and Alignment are scaffold heads")
    # the Advanced Class Guide and Advanced Race Guide: heads, marks and errata
    eq(head_candidate(Para("para", [("Spell Strike (Su):", False, True), (" The blade adept", False, False)], 1, 0))[:2],
       ("Spell Strike (Su)", [(":", False, False), (" The blade adept", False, False)]), "an italic head with its colon inside")
    eq(head_candidate(Para("para", [("Cat's Charge (Ex", False, True), ("): At 11th level", False, False)], 1, 0))[0], "Cat's Charge (Ex)",
       "an italic head with the parenthesis split")
    # review of #351: a tag that the layer breaks at its comma ("Apothecary (Ex, Sp)", Black Markets p. 28) joins into one head, in italics or in bold
    eq(head_candidate(Para("para", [("Apothecary (Ex", False, True), (",", False, False), ("Sp)", False, True), (": The alchemist", False, False)], 1, 0))[:2],
       ("Apothecary (Ex, Sp)", [(": The alchemist", False, False)]), "an italic head with its tag split at the comma")
    eq(head_candidate(Para("para", [("Apothecary (Ex", True, False), (",", False, False), ("Sp)", True, False), (": The alchemist", False, False)], 1, 0))[:2],
       ("Apothecary (Ex, Sp)", [(": The alchemist", False, False)]), "a bold head with its tag split at the comma")
    eq(head_candidate(Para("para", [("Apothecary (Ex)", False, True), (", Sp", False, False), (": x", False, False)], 1, 0))[0], "Apothecary (Ex)",
       "a balanced tag is not joined to what follows")
    # review of #351: a line that fills the column to its right edge is not the last of its paragraph beside art (Black Markets p. 29, Blood of Shadows p. 9)
    def art_line(text, left, right, head=False):
        return {"size": 13, "col": 1, "left": left, "margin": 468, "right": right, "top": 0,
                "runs": [(text, False, head)] if not head else [("Curse Breaker (Su)", False, True), (text, False, False)]}
    art = [art_line("Personal Guarantee (Su): A hoaxer can prevent his wares from afflicting a target until he is safely out of sight.", 481, 800),
           art_line("He can spend up to 1 round of bardic performance per", 480, 800),
           art_line("owner. This performance replaces distraction.", 498, 640),
           art_line("This ability replaces nothing else.", 482, 700),
           art_line(": A hoaxer of 12th level or higher can use performance", 519, 800, head=True)]
    ART_RUNS["on"] = False
    off = len(_assemble(Book({}, {}, {}, set()), [(1, art)]))
    ART_RUNS["on"] = True
    on = [p.plain() for p in _assemble(Book({}, {}, {}, set()), [(1, art)])]
    ART_RUNS["on"] = False
    eq((off, len(on)), (5, 3), "a full line before an indented one does not end a paragraph beside art; a short line, or a head with its colon, still does")
    eq(on[0].endswith("distraction."), True, "the full line joins the next")
    # review of #351: a link that belongs to a phrase goes there, keeping print's case
    eq(apply_context_links("ref/arc-sorcerer/umbral-scion", "must have the shadow bloodline", [("Shadow", "ref/sorcbloodline/shadow")]),
       ("must have the [shadow](ref/sorcbloodline/shadow) bloodline", []), "a context link keeps the case of print")
    # review of #356: a hit counts for the book that read it, so a pattern that is alive in one book cannot hide a dead one of another
    OCR_HITS.clear()
    probe = re.compile(r"\bprobe-token\b")
    OCR_BOOK["name"] = "book-a"
    OCR_HITS[("book-a", probe.pattern)] += 1
    OCR_BOOK["name"] = "book-b"
    saved = OCR_ITALICS[:]
    OCR_ITALICS.append(probe)
    eq(probe.pattern in dead_ocr_patterns(), True, "a pattern that only another book matched is dead in this one")
    OCR_ITALICS[:] = saved
    OCR_HITS.clear()
    OCR_BOOK["name"] = ""
    eq(SUPERSCRIPT_MARK.fullmatch("UM") is not None and SUPERSCRIPT_MARK.fullmatch("sAPG").group(1) == "s", True, "a superscript mark")
    eq(finish_text("a \ufffd2 becomes a \ufffd3", set()), "a \u00d72 becomes a \u00d73", "a lost multiplication sign")
    ERRATA_CTX.update(book="advanced-class-guide", used=set())
    notes: list[str] = []
    got = apply_errata(f"it is {I_OPEN}instead{I_CLOSE} added to this effective damage reduction.", "ref/arc-bloodrager/spelleater", "blood-of-life", [])
    eq(got, f"it is {I_OPEN}instead{I_CLOSE} added to this effective damage reduction.", "an errata change needs its printed words")
    got = apply_errata("the increase is instead added to this effective damage reduction. This ability replaces uncanny dodge.",
                       "ref/arc-bloodrager/spelleater", "blood-of-life", notes)
    eq(got, "the increase is added to this effective damage reduction. This ability replaces uncanny dodge.", "an errata change is applied")
    eq(len(notes) == 1 and notes[0].startswith("errata: Paizo errata for Advanced Class Guide p. 85"), True, "an errata change is recorded")
    eq(apply_errata("the increase is instead added to", "ref/arc-bloodrager/spelleater", "blood-of-life", []), "the increase is instead added to",
       "an errata change applies once")
    ERRATA_CTX["used"].clear()
    got = apply_errata("At 3rd level, an ecclesitheurge forms a powerful bond with a holy symbol. This ability replaces the increase to channel energy gained at 3rd level. More.",
                       "ref/arc-cleric/ecclesitheurge", "bonded-holy-symbol", [])
    eq(got.startswith("forms a powerful bond with a holy symbol of his deity") or "functions identically" in got, True, "an errata span is replaced")
    ERRATA_CTX["used"].clear()
    eq(len(errata_unused("ref/arc-bloodrager/spelleater")), 1, "an errata change that found no place is a problem")
    # print's asterisks: the whole mark goes when the page has no key, stays when it has one
    eq(print_md(PrintFeature("X", [[("Bore bomb** and talent*.", False, False)]], 1), [], set(), "ref/x")[0], "Bore bomb and talent.", "asterisks without a key are dropped whole")
    eq(print_md(PrintFeature("X", [[("Bore bomb*.", False, False)]], 1), [], set(), "ref/x", True)[0], "Bore bomb\\*.", "asterisks with a key stay")
    eq(bool(trade_sentences("(Those marked with an asterisk are detailed in this book.) This alters the bonus feat class ability.")), True, "a trade sentence after a closing parenthesis")
    eq(trade_sentences("A bonus of 1.) This replaces bravery."), [], "a stray closing parenthesis starts no sentence")
    eq(trade_sentences("A bravery bonus (Ex) This alters armor training."), [], "a tag is no sentence end")
    eq(trade_sentences("These bonus feat choices replace Dodge, Mobility, and Spring Attack on his bonus feat list."),
       [("replaces", "Dodge, Mobility, and Spring Attack on his bonus feat list", True)], "bonus feat choices are a bare subject")
    eq(trade_sentences("These choices replace Dodge."), [], "choices alone is no subject word")
    eq(trade_sentences("This ability modifies bonus feats."), [("alters", "bonus feats", False)], "ruling 55: modifies is an alters verb")
    eq(trade_sentences("This ability modifies bonus feats and also replaces the 5th-level bonus feat."),
       [("alters", "bonus feats", False), ("replaces", "the 5th-level bonus feat", False)], "app #737: and also <verb> splits")
    eq(trade_sentences("This ability alters rogue talents, and it also modifies trapfinding."),
       [("alters", "rogue talents", False), ("alters", "trapfinding", False)], "app #737: and it also modifies splits")
    eq(trade_sentences("This ability alters rogue talents, and it changes trapfinding."), [("alters", "rogue talents, and it changes trapfinding", False)],
       "ruling 25: and it changes without also is prose")
    eq(trade_sentences("This ability modifies the bombs and does not stack with other discoveries."), [("alters", "the bombs", False)], "app #737: and does not ends the phrase")
    eq(trade_sentences("This ability modifies and functions as true judgment."), [("alters", "true judgment", False)], "app #737: modifies and functions as X names X")
    eq(trade_sentences("This discovery modifies the alchemist's bombs and doesn't stack with other discoveries that modify bombs."),
       [("alters", "the alchemist's bombs and doesn't stack with other discoveries that modify bombs", False)], "ruling 55: the phrase after modifies")
    # ---- Campaign Setting books (Inner Sea Magic, Intrigue, Combat; phynics/cast-iron#540) ----
    eq(ocr_repair("At  ist level, +i bonus, i6th, i50, io feet, id10"), "At  1st level, +1 bonus, 16th, 150, 10 feet, 1d10", "ocr digits")
    eq(ocr_repair("Ma13ic and Chan13e, jlamin13, stalkin13\u00b0E."), "Magic and Change, flaming, stalking.", "ocr g")
    eq(ocr_repair("i point, I round, o grit, a-4 penalty"), "1 point, 1 round, 0 grit, a -4 penalty", "ocr lone letters")
    eq(ocr_repair("camouflageAPG, survivalistAPc, observer'PG, weapon snatcher0c"), "camouflage, survivalist, observer, weapon snatcher", "ocr book marks")
    eq(ocr_repair("seal\u00ad breaker"), "seal- breaker", "ocr soft hyphen")
    eq(ocr_paragraph([("At  md  level, a  s  well  a s shields", False, False)])[0][0], "At 2nd level, as well as shields", "ocr phrases")
    eq(ocr_paragraph([("the creature-even one, accessory-such as", False, False)])[0][0], "the creature\u2014even one, accessory\u2014such as", "ocr em dash")
    eq(styled_head([("Clean  Capture  (Ex): At 1st level", False, False)])[0], ("Clean  Capture  (Ex)", True, False), "style-less head")
    eq(styled_head([("Aura  of  Law  (Su) The power of", False, False)])[0], ("Aura  of  Law  (Su)", True, False), "style-less head without colon")
    eq(styled_head([("Esprit  de  Corps  (Ex): At 16th", False, False)])[0][0], "Esprit  de  Corps  (Ex)", "style-less head with a connector")
    eq(styled_head([("At 1st level, a thing: it", False, False)])[0][1], False, "a sentence is no head")
    eq(ocr_italics([("grant the firearm flaming burst or stalking. More", False, False)]),
       [("grant the firearm ", False, False), ("flaming burst", False, True), (" or ", False, False), ("stalking", False, True), (". More", False, False)], "ocr italics")
    BULLETS["on"] = ITALIC_FIRST["on"] = CITE_EXT["on"] = True
    eq(join_wrapped(["At 2nd level:", "\u2022 The first item.", "\u2022 This ability replaces poison use."], set()),
       ["At 2nd level:", "- The first item.", "This ability replaces poison use."], "bullet items; a bullet before the trade sentence is no item")
    eq(join_wrapped(["\u2022 One without an end", "\u2022 Two."], set()), ["- One without an end", "- Two."], "bullet items do not merge")
    LIST_CONTINUES["on"] = True
    eq(join_wrapped(["\u2022 Grant a +2 bonus or impose a -2", "penalty on saving throws.", "\u2022 Two."], set()), ["- Grant a +2 bonus or impose a -2 penalty on saving throws.", "- Two."],
       "a wrapped line of a list item continues it where print hangs its bullets")
    LIST_CONTINUES["on"] = False
    eq(finish_text("the s" + I_OPEN + "un orchid elixir" + I_CLOSE + ", granting", set()), "the " + I_OPEN + "sun orchid elixir" + I_CLOSE + ", granting", "a split italic first letter")
    eq(len(re.findall(CITE_BOOK_X, "x (" + I_OPEN + "Ultimate" + I_CLOSE + " " + I_OPEN + "Intrigue" + I_CLOSE + " 142) y")), 1, "citation with split italic words")
    eq(render_marks(f"a {I_OPEN}riding{I_CLOSE} {I_OPEN}possession{I_CLOSE} (10th), {I_OPEN}x{I_CLOSE}, {I_OPEN}y{I_CLOSE}"), "a _riding possession_ (10th), _x_, _y_", "italic runs that the line wrap of print splits are one span")
    eq(render_marks(f"x {I_OPEN}(Pathfinder RPG Ultimate Combat{I_CLOSE} 65)"), "x (_Pathfinder RPG Ultimate Combat_ 65)", "the parenthesis of a citation stays outside the italics")
    eq(render_marks(f"{I_OPEN}a{I_CLOSE} {I_OPEN}[b](t){I_CLOSE}"), "_a_ _[b](t)_", "a span with a link keeps its own marks")
    eq(len(re.findall(CITE_BOOK_X, "x (" + I_OPEN + "Ultimate Intrigue 102" + I_CLOSE + ") y")), 1, "citation whose italic holds the page")
    eq(len(re.findall(CITE_BOOK_X, "x (Inner Sea World Guide 286) y")), 1, "citation of the Inner Sea World Guide")
    geo = Book({}, {1: [(200, 108, 0, "a", 300)] * 3 + [(200, 440, 0, "b", 300)] * 3 + [(200, 122, 0, "c", 300)], 2: []}, {}, set())
    geo.fonts = {"0": 13}
    eq(table_lost(["Intro.\n|A|B|\n| --- | --- |\n|1|2|"], "Intro. A B 1 2"), True, "a table that print's text runs together is a hold")
    eq(table_lost(["Intro.\n|A|B|\n| --- | --- |\n|1|2|"], "Intro.\n\n|A|B|\n|---|---|\n|1|2|"), False, "a table that print's text keeps is no hold")
    eq(table_lost(["No table here."], "No table here."), False, "no table on either side")
    eq(ext_lead_level("Upon reaching 5th level, a seal-breaker receives a boon.")[0], 5, "lead: upon reaching")
    eq(ext_lead_level("At 3rd-level, a witch can use a vessel.")[0], 3, "lead: Nth-level")
    eq(ext_lead_level("A Chelish diva of 8th level or higher can use her performance.")[0], 8, "lead: of Nth level or higher")
    eq(ext_lead_level("A siege gunner is trained in siegecraft. Starting at 2nd level, a siege gunner gains a bonus.")[0], 2, "lead: second sentence, starting at")
    eq(ext_lead_level("A master expands the conditions. At 4th level, she can choose to make the target shaken.")[0], None, "an upgrade in the second sentence is no lead")
    eq(ext_lead_level("The scoundrel doesn't acquire the sneak attack ability until 3rd level, when she gains +1d6.")[0], 3, "lead: until Nth level")
    eq(ext_lead_level("When the fated guide reaches 9th level, her phantom gains a +4 bonus.")[0], 9, "lead: reaches Nth level")
    eq(ext_lead_level("A hag phantom is animated by a curse, and at 4th level this grants her a death curse.")[0], 4, "lead: at Nth level this grants")
    eq(ext_lead_level("A fated guide can use this until she reaches the end of the day.")[0], None, "no level in until")
    eq(bool(CHOICE_INTRO.search("the fortunes each of those kami grant are listed below.")), True, "a lead-in that lists below")
    eq(bool(CHOICE_INTRO.search("as noted below, each one has its own cost.")), True, "a lead-in that says as noted below")
    eq(ext_lead_level("At 2th level, a thing")[0], None, "lead: a wrong suffix")
    CITE_EXT["on"] = True
    eq(_close_italics("(Pathfinder RPG Ultimate Magic" + I_CLOSE + " 230)"), I_CLOSE, "a dropped citation closes the italic that it shared with the name")
    eq(_close_italics("(" + I_OPEN + "Core Rulebook" + I_CLOSE + " 5)"), "", "a citation with both marks leaves none")
    eq(len(dead_ocr_patterns()) > 0, True, "with no hits every OCR pattern is dead")
    BULLETS["on"] = ITALIC_FIRST["on"] = CITE_EXT["on"] = False
    eq(_close_italics("(Pathfinder RPG Ultimate Magic" + I_CLOSE + " 230)"), I_CLOSE, "every book restores the italic that a dropped citation shared with the name")
    eq(len(NO_LEVEL_ONE) > 0 and ("ref/arc-gunslinger/bushwhacker", "craven-deeds") in NO_LEVEL_ONE, True, "ruling 48: a part of a feature has no level from the trade")
    eq(LEVEL_FROM_PRINT[("ref/arc-swashbuckler/wildstrider", "subterfuge")][0], 1, "a deed that replaces a 1st-level deed has level 1")
    eq(len(re.findall(CITE_BOOK, "x (Inner Sea World Guide 286) y")), 0, "the other books do not cite the Inner Sea World Guide")
    PAGE_GEOMETRY["on"] = True
    eq(page_geometry(geo, 1), (432, (108, 440)), "page geometry: the right column starts at 440")
    PAGE_GEOMETRY["on"] = False
    print(f"self-test: {ok} checks passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", nargs="?", default=str(ROOT))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--print-sentences", action="store_true",
                    help="write `<book>.sentences.tsv`, the printed trade sentences of the book (needs --books and --cache); --check requires them in the entries")
    ap.add_argument("--book", default=None, help="publication id (--check without it covers every book with a review TSV)")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    ap.add_argument("--only", default="")
    ap.add_argument("--forget-checker-holds", action="store_true",
                    help="--compare: forget the holds that an earlier --write recorded from the checker (after the script or the app changed)")
    ap.add_argument("--checker")
    ap.add_argument("--rules", default="all", help="the hold rules that are on: all, none, or names joined by + (hyphens, prereq, usage, values, dropped, choices, lostlevel)")
    args = ap.parse_args()
    for k in RULES:
        RULES[k] = args.rules == "all" or k in args.rules.split("+")
    global FORGET_CHECKER_HOLDS
    FORGET_CHECKER_HOLDS = args.forget_checker_holds
    if args.self_test:
        return self_test()
    if (args.compare or args.write) and not args.book:
        raise SystemExit("--compare and --write need --book ID")
    if args.print_sentences:
        if not (args.book and args.books and args.cache):
            raise SystemExit("--print-sentences needs --book ID, --books DIR and --cache DIR")
        return run_print_sentences(args)
    if args.compare:
        if not (args.books and args.cache):
            raise SystemExit("--compare needs --books DIR and --cache DIR")
        return run_compare(args)
    if args.write:
        return run_write(args)
    if args.check:
        corpus = Path(args.corpus).resolve()
        books = [args.book] if args.book else sorted(
            p.name[len("feature-prose-540-"):-len(".tsv")] for p in (corpus / "scripts").glob("feature-prose-540-*.tsv")
            if not p.name.endswith((".decisions.tsv", ".queue.tsv", ".sentences.tsv")))
        status = 0
        for b in books:
            args.book = b
            status |= run_check(args)
        return status
    ap.print_help()
    return 2



MISPRINTS.extend([
    ("ref/arc-bard/flamesinger", "without needing the meet the normal", "without needing to meet the normal",
     "\"needing the meet\" is a slip (Elemental Master's Handbook p. 5); the sentence reads \"without needing to meet the normal prerequisites\" (ruling 9)"),
    ("ref/arc-bard/luring-piper", "using the lurid piper's bard level", "using the luring piper's bard level",
     "the archetype is the luring piper; \"lurid piper\" is a wrong proper name (Monster Hunter's Handbook p. 11; owner ruling 43)"),
])
# ---- Batch A3: Elemental Master's Handbook, Monster Hunter's Handbook, Monster Summoner's Handbook, Armor Master's Handbook, Cohorts and Companions ----
LEVEL_FROM_PRINT.update({
    ("ref/arc-paladin/divine-guardian", "bonus-feat"): (7, "print says \"A divine guardian gains a bonus feat at 7th level\" (Cohorts and Companions p. 23); the hand edit of the ability keeps the level"),
    ("ref/arc-gunslinger/firebrand", "scorched-earth"): (4, "print says \"At 4th level and every 4 levels thereafter\" (Elemental Master's Handbook p. 5): the level is stated inside the sentence (ruling 4)"),
})
_STORM = [("eagle", "ref/monster/eagle"), ("small air elemental", "ref/monster/air-elemental"), ("small lightning elemental", "ref/monster/lightning-elemental"),
          ("dire bat", "ref/monster/bat-dire-bat"), ("medium air elemental", "ref/monster/air-elemental"), ("medium lightning elemental", "ref/monster/lightning-elemental"),
          ("pteranodon", "ref/monster/dinosaur-pteranodon"), ("large air elemental", "ref/monster/air-elemental"), ("large lightning elemental", "ref/monster/lightning-elemental"),
          ("huge air elemental", "ref/monster/air-elemental"), ("huge lightning elemental", "ref/monster/lightning-elemental"), ("roc", "ref/monster/roc"),
          ("elder air elemental", "ref/monster/air-elemental"), ("elder lightning elemental", "ref/monster/lightning-elemental"), ("advanced", "ref/template/advanced"),
          ("call lightning", "ref/spell/call-lightning")]
for _eid in ("ref/arc-summoner/storm-caller", "ref/arc-unchained-summoner/storm-caller"):
    EXTRA_LINKS[(_eid, "summon-storm-s-fury")] = list(_STORM)
    TRADE_ADDITIONS[_eid] = TRADE_ADDITIONS.get(_eid, []) + [{"alters": "the summoner's summon monster I\u2013IX abilities", "feature": "summon-monster-i"}]
TRADE_ADDITIONS["ref/arc-alchemist/energy-scientist"] = [{"alters": "Class skills"}]
EXTRA_LINKS[("ref/arc-investigator/dread-investigator", "investigator-talent")] = [("alchemical discovery", "ref/invtalent/alchemist-discovery")]
TRADE_RENAMES.update({
    ("ref/arc-warpriest/proselytizer", "3rd-level bonus feat"): "Bonus feat gained at 3rd level",
    ("ref/arc-wizard/bonded-wizard", "5th- and 15th-level bonus feats"): "A wizard's bonus feats normally gained at 5th and 15th level",
    ("ref/arc-wizard/bonded-wizard", "10th-level bonus feat"): "The wizard's bonus feat normally gained at 10th level",
    ("ref/arc-wizard/instructor", "5th-, 10th-, 15th-, and 20th-level bonus feats"): "The bonus feats gained at 5th, 10th, 15th, and 20th level",
})
# print: "This ability alters sacred weapon and also replaces sacred armor": two trades, as the app reads it since #737 ("and also <verb>" splits)
TRADE_OP_FIXES[("ref/arc-warpriest/shieldbearer", "sacred armor")] = "replaces"
# ruling 55 ("modifies" is an alters verb): the gap that its sentence leaves in this batch (the verb itself is the cross-batch PR's)
TRADE_ADDITIONS["ref/arc-warpriest/shieldbearer"] = [{"alters": "Channel energy", "feature": "channel-energy"}]
TRADE_ADDITIONS["ref/arc-alchemist/oozemaster"] = [{"replaces": "The bomb class feature", "feature": "bomb"}]
TRADE_RENAMES[("ref/arc-alchemist/oozemaster", "Brew Potion")] = "Brew Potion, though an oozemaster can still select Brew Potion without meeting the feat's prerequisites"
for _eid in ("ref/arc-bard/luring-piper", "ref/arc-druid/defender-of-the-true-world", "ref/arc-occultist/psychodermist"):
    TRADE_ADDITIONS[_eid] = TRADE_ADDITIONS.get(_eid, []) + [{"alters": "Class skills"}]
TRADE_RENAMES[("ref/arc-paladin/banishing-warden", "3rd-level mercy")] = "Mercy gained at 3rd level"
MISPRINTS.append(("ref/arc-bard/luring-piper", "and a when employing a wind instrument", "and when employing a wind instrument",
                  "a stray \"a\" in print (\"and a when employing a wind instrument\"); the sentence reads \"... when using Perform (wind instruments) and when employing a wind instrument\" (Monster Hunter's Handbook p. 11)"))
TRADE_RENAMES[("ref/arc-monk/windstep-master", "Slow fall")] = "Slow fall or the ki power gained at 4th level for an unchained monk"

if __name__ == "__main__":
    sys.exit(main())
