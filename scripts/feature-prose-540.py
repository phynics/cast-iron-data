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
}
ROOT = HERE.parent
FORGET_CHECKER_HOLDS = False

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


def lead_level(text: str) -> int | None:
    """The level of an "At Nth level" lead (also "Starting at", "Beginning at"), as the app's check reads it."""
    m = LEAD.match(text.strip())
    if not m:
        return None
    n = int(m.group(1))
    if 1 <= n <= 20 and m.group(2) == ordinal(n)[len(str(n)):]:
        return n
    return None


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


def build_draft(feat: ImportFeature) -> Draft:
    level = None
    effect: list[str] = []
    action = None
    rest: list[str] = []
    upgrades: list[tuple[int, str]] = []
    usage: list[str] = []
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
    return Draft(full, core, sorted(upgrades), usage, level, bad, [x for x in effect + rest], labelled)


# ---- links and italics carried over from the import --------------------------------------------------

LINK = re.compile(r"(_?)\[([^\]]+)\]\(([^)]+)\)(_?)")


def old_links(feat: ImportFeature) -> list[tuple[str, str]]:
    """Every link of the import text, once for each occurrence (a word that the import links twice is
    placed twice)."""
    text = "\n".join(it.content for it in feat.items) + "\n" + feat.name
    return [(m.group(2), m.group(3)) for m in LINK.finditer(text)]


I_OPEN, I_CLOSE = "\x01", "\x02"
LINK_SPAN = re.compile(r"(?<!\\)\[[^\[\]]*\]\([^()\s]*\)")


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
        free = [m for m in pat.finditer(text) if not any(a <= m.start() < b for a, b in spans)]
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
    return s


def finish_text(s: str, vocab: set[str]) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("\u00ad", "")
    s = re.sub(r"(?<=[A-Za-z0-9])/ (?=[A-Za-z0-9])", "/", s)                       # "law/" at a line end, "chaos" on the next ("DR 5/", "cold iron"; "1/", "round")
    s = re.sub(r"(?<=[A-Za-z" + I_CLOSE + r"]) +(?=['\u2019]s\b)", "", s)         # "thief 's" (kerning of an italic or bold run)
    s = re.sub("\ufffd(?=\\d)", "\u00d7", s)             # a multiplication sign that the extraction lost ("a x2 becomes a x3")
    s = re.sub(r"(?<![\w)\]])–(?=\d)", "-", s)           # a minus sign
    s = re.sub(r"(?<=\w) – (?=\d)", " - ", s)             # a minus operator ("druid level – 2")
    s = fix_ligatures(s, vocab)
    s = fix_hyphens(s, vocab)
    s = re.sub("(?<=[A-Za-z0-9)_])\u2014 +(?=\\S)", "\u2014", s)   # a line that ends in an em dash joins the next one without a blank ("DR 5/\u2014 against" keeps its blank)
    # an italic run of marks only (", " or "." between two words) is plain text: the period of "possession (see page 181)." is not italic
    s = re.sub(I_OPEN + r"([\s,.;:!?]+)" + I_CLOSE, r"\1", s)
    # the extraction pads italic runs with blanks
    s = re.sub(I_OPEN + r"\s+", " " + I_OPEN, s)
    s = re.sub(r"\s+" + I_CLOSE, I_CLOSE + " ", s)
    s = re.sub(I_CLOSE + I_OPEN, "", s)
    s = re.sub(r"(\\\[|\()\s+", r"\1", s)        # no blank after an opening bracket or parenthesis
    s = re.sub(r"\s+(\)|\\\])", r"\1", s)        # none before a closing one
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fix_ligatures(s: str, vocab: set[str]) -> str:
    """`f ighter`, `inf lict`: the fi and fl ligatures leave a blank that a word does not have."""

    def join(m: re.Match) -> str:
        a, b = m.group(1), m.group(2)
        if (a + b).lower() in vocab:
            return a + b
        return m.group(0)

    return re.sub(r"\b([A-Za-z]*f) ([il][a-z]*)\b", join, s)


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


def render_marks(s: str) -> str:
    return s.replace(I_OPEN, "_").replace(I_CLOSE, "_")


# ---- the print: pdftohtml -xml ------------------------------------------------------------------------

TEXT_EL = re.compile(r'<text top="(-?\d+)" left="(-?\d+)" width="(-?\d+)" height="(-?\d+)" font="(\d+)">(.*?)</text>', re.S)
FONT_EL = re.compile(r'<fontspec id="(\d+)" size="(\d+)" family="([^"]*)" color="([^"]*)"')
TAG_SPLIT = re.compile(r"(</?[bi]>)")
BODY_TOP = (88, 1075)
SUPERSCRIPT = "\x04"
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
        return "".join(t for t, _, _ in self.runs)


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
            plain = html.unescape(re.sub(r"</?[bi]>", "", raw)).strip()
            # a cross-reference mark: a book abbreviation (two to four capitals, or one named in `SUPERSCRIPT_MARK`) or a
            # dagger in small type after a name ("mutagen" + "UM"); the corpus links the name instead (owner ruling 26).
            # Letters that the extractor glued to the mark ("s" + "APG") are part of the word.
            mark = SUPERSCRIPT_MARK.fullmatch(plain) if (fonts.get(font, 99) <= 8 or int(_h) <= 11) else None
            if mark and mark.group(1):
                raw, plain = mark.group(1), mark.group(1)
            elif (mark and not mark.group(1)) or (int(_h) <= 11 and re.fullmatch(r"[A-Z]{2,4}|[\u2020\u2021]+", plain)):
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
    vocab = {w for w, _ in words.items()}
    sans = frozenset(fid for fid, _sz, fam, _col in FONT_EL.findall(xml) if "Sans" in fam)
    fams = {fid: re.sub(r"^[A-Z]{6}\+", "", fam) for fid, _sz, fam, _col in FONT_EL.findall(xml)}
    return Book(fonts, pages, printed, vocab, sans, fams)


def page_lines(book: Book, num: int) -> list[dict]:
    by_col: dict[int, list] = {0: [], 1: []}
    for top, left, font, raw, width in book.pages.get(num, []):
        if SKIP_TABLES["on"] and str(font) in book.sans and book.fonts[str(font)] <= 13:
            continue        # a table of the race chapter that stands on the page of the archetype: its cells are not the text
        if BODY_TOP[0] <= top <= BODY_TOP[1]:
            by_col[0 if left < COL_SPLIT else 1].append((top, left, font, raw, width))
    lines = []
    for col in (0, 1):
        cur: list[dict] = []
        for top, left, font, raw, width in sorted(by_col[col], key=lambda x: (x[0], x[1])):
            # a title in small capitals sets its capitals and its small capitals 5 units apart (Blood of the Ancients): the
            # same family of type, a larger size above
            if cur and (abs(cur[-1]["top"] - top) <= 4 or (SMALL_CAP_TITLES["on"] and abs(cur[-1]["top"] - top) <= 6
                                                           and cur[-1]["size"] >= 16 and book.fams.get(str(font)) == cur[-1]["fam"])):
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
            ln["right"] = max(a + w for a, _, w in ln["parts"])
            runs: list = []
            for _, raw, _w in ln["parts"]:
                runs += runs_of(raw)
            ln["runs"] = runs
        lines += cur
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


def read_blocks(book: Book, first: int, last: int) -> list[Para]:
    """Paragraphs and titles of the PDF pages `first`..`last`, columns in reading order."""
    out: list[Para] = []
    insets: dict[int, int | None] = {}
    seen_big: list[str] = []
    for num in range(first, last + 1):
        if num not in book.pages:
            continue
        shown = book.printed.get(num, num - 1)
        plines = page_lines(book, num)
        for li, ln in enumerate(plines):
            indent = ln["left"] - COL_LEFT[ln["col"]]
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
            if ln["size"] >= 16:
                insets[ln["col"]] = ln["left"] if indent >= 8 else None
                if out and out[-1].kind == "title" and out[-1].col == ln["col"] and out[-1].page == shown:
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
            if ILLUSTRATED["on"] and not starts and out and out[-1].kind == "para" and re.search(r"[.)!?\"”]\s*$", out[-1].plain()):
                # beside an illustration the lines have no common indent: a head ("Rope Swing (Ex):") after the end of a
                # sentence still starts a paragraph
                cand = head_candidate(Para("para", list(ln["runs"]), shown, ln["col"]))
                starts = bool(cand and cand[1] and cand[1][0][0].lstrip().startswith(":") and len(cand[0]) <= 60)
            if not out or out[-1].kind == "title" or starts:
                out.append(Para("para", list(ln["runs"]), shown, ln["col"]))
            else:
                out[-1].runs.append((" ", False, False))
                out[-1].runs += ln["runs"]
    for p in out:
        p.runs = merge_runs(p.runs)
    return out


CLASS_TITLES = {squash(x) for x in (
    "Alchemist", "Antipaladin", "Barbarian", "Bard", "Cavalier", "Cleric", "Druid", "Fighter", "Gunslinger", "Inquisitor",
    "Magus", "Monk", "Oracle", "Paladin", "Ranger", "Rogue", "Sorcerer", "Summoner", "Witch", "Wizard", "Archetypes")}


# a title that names a type of rules ("ORDER OF THE SHROUD (CAVALIER ORDER)", "NEW WILD TALENTS (KINETICIST)") ends the
# section of an archetype: it is the next entry of the book, not a sidebar of this one
TYPE_TITLE = re.compile(r"\([A-Za-z][A-Za-z' -]{3,}\)\s*$")           # the Advanced Player's Guide sets titles in mixed small caps

CLASS_SUFFIX = re.compile(r"\s*\((?:Alchemist|Antipaladin|Barbarian|Bard|Cavalier|Cleric|Druid|Fighter|Gunslinger|Inquisitor|Magus|"
                          r"Monk|Oracle|Paladin|Ranger|Rogue|Sorcerer|Summoner|Witch|Wizard)\)\s*$")


# The titles of archetypes that print sets in the section of the archetype before them and that the corpus holds as headed
# prose of another entry (the Advanced Player's Guide's Totem Warrior and Animal Shamans): they end a section too.
UNTYPED_ARCHETYPE_TITLES = {squash(x) for x in ("Totem Warrior", "Animal Shamans")}


# The Adventurer's Guide sets each archetype at the end of the chapter of a Pathfinder Society faction, followed by the faction's
# affiliation, equipment, feats, magic items and spells; the Ultimate Wilderness sets a race's equipment, feats, magic items and
# spells after the archetype of its chapter. These titles are the next section of the book, not a sidebar of the archetype.
SECTION_STOP = re.compile(r"^(?:AFFILIATION\b|.*\bAFFILIATION$|EQUIPMENT\b|FEATS?\b|MAGIC ITEMS?\b|SPELLS?$|CLASS OPTIONS?\b|"
                          r"VIGILANTE CLASS OPTION|INVESTIGATOR TALENTS|[A-Z]+ (?:EQUIPMENT|FEATS|MAGIC ITEMS?|SPELLS?)$)")
SECTION_STOPS = {"on": False}
# Blood of the Ancients: no archetype holds a box or a heading of its own, and what follows each one (a spell, a feat, a trait, an
# item of the chapter) has a title of its own: any title ends the section.
ANY_TITLE_ENDS = {"on": False}
# Blood of the Ancients sets its titles in small capitals (a capital and its small capitals sit 5 units apart in one family of type), and
# a chapter title that a page repeats unseen over the first lines of a column. Other books read as before.
SMALL_CAP_TITLES = {"on": False}

# A title with a parenthesized type that does not end the section: the box of rules that the archetype uses (owner ruling 41;
# Elemental Aspects of the Elementalist Shifter, Ultimate Wilderness pp. 78-80, "(Elementalist Shifter Aspects)")
KEEP_TITLES = {squash("Elemental Aspects (Elementalist Shifter Aspects)")}


def find_section(blocks: list[Para], title: str, stops: set[str] | None = None) -> list[Para] | None:
    """The blocks of an archetype: from its title to the next title of another archetype or of a class. Another
    title in between (a sidebar, a table heading) is a heading of the section. With no `stops`, the next title of
    any kind ends it."""
    key = squash(re.sub(r"\s*\([A-Z]{2,4}\)\s*$", "", title))        # "Ringleader (UI)": the corpus's mark of a second archetype of the name
    for i, b in enumerate(blocks):
        # Ultimate Magic and Ultimate Combat print "REANIMATOR (ARCHETYPE)"; Occult Adventures and Ultimate Intrigue print the
        # class on a second line ("ECTOCHYMIST (ALCHEMIST ARCHETYPE)"); the Advanced Race Guide "Saboteur (Alchemist)"
        sp = squash(b.plain()) if b.kind == "title" else ""
        if b.kind == "title" and (sp in (key, key + "archetype") or squash(CLASS_SUFFIX.sub("", b.plain())) == key or (
                sp.startswith(key) and sp.endswith("archetype") and len(sp) <= len(key) + len("archetype") + 24)):
            j = i + 1
            out = [b]
            while j < len(blocks):
                nxt = blocks[j]
                if nxt.kind == "title":
                    k = squash(nxt.plain())
                    # another archetype, a class, a chapter title (a larger font) or a title of a type of rules ends the
                    # section; so does the "NEW RACIAL RULES" title that follows the archetypes of a race chapter
                    if (stops is None or ANY_TITLE_ENDS["on"] or k in stops or k.endswith(("archetype", "mystery", "bloodline")) or nxt.size >= 30
                            or CLASS_SUFFIX.search(nxt.plain()) or k == "newracialrules" or (TYPE_TITLE.search(nxt.plain()) and k not in KEEP_TITLES)
                            or (SECTION_STOPS["on"] and SECTION_STOP.match(re.sub(r"\s+", " ", nxt.plain()).strip()))):
                        break
                    out.append(Para("para", [(t, True, i) for t, _, i in nxt.runs], nxt.page, nxt.col))
                else:
                    out.append(nxt)
                j += 1
            return out
    return None


@dataclass
class PrintFeature:
    head: str
    paras: list[list[tuple[str, bool, bool]]]        # runs of each printed paragraph (the head cut off)
    page: int
    bold: bool = True                                # a bold head; an italic one is a sub-power or an option
    errata: int = 0                                  # the errata page that replaced this ability


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
    head = re.sub(r"\s+", " ", head).strip()
    rest = runs[i:]
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
    r"(?:^|(?<=[.!?]\s)|(?<=[.!?]\)\s))((?:This|These|It)\b(?:\s+(?:bonus\s+feats?\s+choices?|" + TRADE_SUBJECT_WORDS + r"))*\s+(replaces?|alters?|changes?)\b[^.]*\.)",
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
    return "replaces" if verb.lower().startswith("replace") else "alters"      # ruling 25: "changes" is an alters verb


def _clean_phrase(phrase: str) -> str:
    phrase = phrase.strip().rstrip(".").strip()
    phrase = re.sub(r",\s+but\b.*$", "", phrase)                              # R8: the phrase ends at ", but "
    phrase = re.sub(r",\s+and\s+(?:it\s+)?counts?\s+as\b.*$", "", phrase)    # R17: ", and counts as" and ", and it counts as" end the phrase
    # R9 and R18: a parenthesis of 4+ words is an aside, at the end of the phrase or inside it
    phrase = re.sub(r"\s*\(([^()]*)\)", lambda m: "" if len(m.group(1).split()) >= 4 else m.group(0), phrase)
    return phrase.strip().rstrip(".").strip()


def trade_sentences(text: str, head: str = "") -> list[tuple[str, str, bool]]:
    """[(op, phrase, bare)] of the trade sentences of a text: "This ability replaces bravery." gives
    ("replaces", "bravery", False). A bare sentence ("These replace the normal attack roll bonus.") has no
    ability, feature, power or archetype in its subject: the app counts it only when it names a stored trade.
    The reader rules of owner ruling 21 (R8, R9, R11, R12) and 25: a phrase ends at ", but "; a final parenthesis of
    four or more words is an aside; "X replaces Y and alters Z" is two sentences; the heading of the feature
    (without its ability tag) is a subject too; "changes" is an `alters` verb."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[\\_*]", "", text)
    text = re.sub(r"\s+", " ", text)        # a paragraph break inside a sentence (a column or page break) does not end it
    out = []
    found = [(m.group(1), m.start(1)) for m in _trade_matches(text)]
    plain = ABILITY_TAG.sub("", head).strip() if head else ""
    if plain:                                 # R12
        for m in re.finditer(r"(?:^|(?<=[.!?]\s))(" + re.escape(plain) + r"\s+(?:replaces?|alters?|changes?)\b[^.]*\.)", text, re.I):
            if all(m.start(1) != at for _, at in found):
                found.append((m.group(1), m.start(1)))
    for sentence, _ in sorted(found, key=lambda x: x[1]):
        verb = re.search(r"\b(replaces?|alters?|changes?)\b", sentence, re.I)
        subject = sentence[:verb.start()]
        bare = not re.search(ABILITY_NOUN, subject, re.I) and not (plain and subject.strip().lower() == plain.lower())
        rest = sentence[verb.end():]
        # R11: two verbs, two sentences; "changes" is a verb only as the first one (owner ruling 25)
        # R16: the second clause may have a subject: ", and it replaces X" (it, this, he, she, they, with "also")
        clause = r"(?:(?:it|this|he|she|they)\s+(?:also\s+)?)?"
        parts = re.split(r"\s*,?\s+and\s+(?=" + clause + r"(?:replaces?|alters?)\b)", rest, flags=re.I)
        ops = [verb.group(1)] + [re.match(clause + r"(replaces?|alters?)", x, re.I).group(1) for x in parts[1:]]
        for op_word, part in zip(ops, parts):
            part = re.sub(r"^" + clause + r"(?:replaces?|alters?)\b", "", part.strip(), flags=re.I)
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


def phrase_tokens(text: str, possessor: bool = True) -> list[str]:
    """Words of a trade name or of a printed phrase, as the app reads them: no articles, no class names, ordinals as
    digits, "gained at 4th level" as "4th-level", "1 to 4" as one range."""
    text = fold(text)
    text = text.replace(" as well as ", " and ")                                           # R7
    text = re.sub(r"\b(?:normal|normally)\s+", "", text)                                     # R2
    # R10: a possessor phrase before a name ("the sacred shield's holy champion ability") is not part of the name
    if possessor:
        text = re.sub(r"(?:\b(?:the|a|an)\s+)?(?:[a-z-]+\s+){0,2}[a-z-]+'s\s+", "", text)
    text = text.replace("'s", "") if possessor else text.replace("'s", "possessive")      # plain reading: a possessor stays a word
    text = re.sub(r"\b(\d+)(?:st|nd|rd|th)?\s*(?:to|-|through)\s*(\d+)(?:st|nd|rd|th)?\b(?!-level)", lambda m: " ".join(
        str(n) for n in range(int(m.group(1)), int(m.group(2)) + 1)) if 0 < int(m.group(1)) < int(m.group(2)) <= 20 else m.group(0), text)   # R6
    text = re.sub(r"\b(\w+) gained at (\d+(?:st|nd|rd|th)) levels?\b", r"\2-level \1", text)
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

LOOSE_TRADE = re.compile(r"(?:^|(?<=[.!?]\s)|(?<=\n))(?:This|These|It)\b[^.]{0,60}?\b(?:replaces?|alters?|changes?)\b[^.]*\.", re.I)
PROGRESSION = re.compile(r"(?:every|per)\s+\w+\s+(?:\w+\s+)?levels?\s+(?:beyond|after|above|thereafter)|every\s+\w+\s+levels?\s+thereafter", re.I)


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
    m = re.search(r"(?:every|for every|per)\s+(\w+)\s+levels?\s+(?:beyond|after|above|thereafter)\s*(?:(\d+)(?:st|nd|rd|th))?", t)
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
    r"(?:increases?|improves?|rises?|grows?)\s+by\s+\+?(\d+)[^.]*?(?:every|for every|per)\s+(\w+)\s+levels?\s+(?:after|beyond|above)\s+(\d+)(?:st|nd|rd|th)", re.I)
PRINT_MAXIMUM = re.compile(r"maximum\s+(?:bonus\s+)?of\s+\+?(\d+)(?:[^.]*?\bat\s+(\d+)(?:st|nd|rd|th)\s+level)?", re.I)

# Features where the owner ruled that print wins over a corpus value that the expansion shows to differ
# (ruling 8 of 2026-11-24 on phynics/cast-iron-data#306).
PRINT_WINS = {
    ("ref/arc-fighter/archer", "hawkeye"): "ruling 8: print corrects the corpus (+1 at 2nd level and every 4 levels beyond; the corpus gave 1 + one-fourth of the level)",
}


def expand_rules(print_text: str, corpus_text: str) -> tuple[str, list[str]] | None:
    """Rule 8. When print states "+B ... increases by +S for every N levels after Kth" and the corpus states
    "equal to one-third of her X level (minimum +M)", expands both into the values at levels K..20. Returns
    ("equal", [words]) when they agree (the words are the numbers to leave out of the comparison), or
    ("differ", [description]) when they do not; None when the text has no such pair."""
    flat = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", corpus_text)
    cm = CORPUS_FRACTION.search(flat)
    pm = PRINT_PROGRESSION.search(print_text)
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


def compare_feature(draft: Draft, print_text: str, drop: set[str], title_tokens: set[str]) -> Compare:
    """Draft against the printed paragraph. Differences in words that carry no rule (articles, pronouns, the
    person, connectives, action labels, the order of sentences) are wording; a number or any other word that
    only one side has is a changed number or rule word (held). Printed progressions are expanded against the
    corpus's fractions of the level (ruling 8); a corpus paragraph that print does not have is dropped
    (ruling 10)."""
    notes: list[str] = []
    info: list[str] = []
    skip = drop | title_tokens
    p_clean = strip_trade_sentences(print_text)
    d_clean = strip_trade_sentences(draft.core)
    lp = lead_level(print_text)
    if draft.level is not None and lp is not None and draft.level != lp:
        notes.append(f"level: corpus {ordinal(draft.level)}, print {ordinal(lp)}")
    lvl = draft.level if lp is None or lp == draft.level else None
    p_clean = strip_level_phrase(strip_leads(p_clean), lvl)
    d_clean = strip_level_phrase(strip_leads(d_clean), lvl)
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
    d_tok = Counter(tokens(d_clean, skip))
    if draft.usage:
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
        if prog is not None and rows <= prog and rows == {x for x in prog if min(rows) <= x <= max(rows)}:
            # the rows expand the printed rule; they are not rule text of their own
            p_tok = Counter(tokens(strip_leads(strip_level_phrase(strip_progression(p_clean), draft.level)), skip))
            if draft.usage:
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
            info.append("ruling 10: corpus text that print does not have is dropped: " + "; ".join(
                "“" + " ".join(x.split()[:7]) + " …”" for x in dropped))
    a = sorted(only_draft.elements())
    b = sorted(only_print.elements())
    if (a or b) and letters(a) == letters(b):
        a = b = []     # the same letters and numbers in another spelling (point-blank, point blank)
    if a or b:
        kind = "number" if any(is_number(x) for x in a + b) else "rule word"
        notes.append(f"{kind}: corpus {a or '-'} / print {b or '-'}")
    if draft.usage:
        usage_nums = {x for u in draft.usage for x in tokens(u) if is_number(x)}
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
        return "features" in (self.data.get("fields") or {})


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
        out.append(Entry(path, data["id"], data["title"], "archetype", front, body, data, first, page, classes))
    return out


def trades_of(e: Entry) -> list[dict]:
    return list((e.data.get("fields") or {}).get("trades") or [])


def trade_name(t: dict) -> tuple[str, str]:
    return ("replaces", t["replaces"]) if "replaces" in t else ("alters", t["alters"])


DECISION_HEADER = ["entry", "anchor", "decision", "note"]
DECISIONS = ("print", "drop", "to-opening", "hold", "unlist", "list", "sidebar")


def decisions_path(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / f"feature-prose-540-{book}.decisions.tsv"


def read_decisions(corpus: Path, book: str) -> dict[tuple[str, str], tuple[str, str]]:
    """Hand decisions of a review (phynics/cast-iron-data#306, ruling 14): `print` takes print's wording for a
    held row, `drop` leaves out a feature that print does not have, `to-opening` also moves its sentence into
    the opening text, `tail-to:ANCHOR` moves the paragraphs after the first one into that feature. The structure
    decisions (owner rulings 15 and 18) also take print's wording: `unlist` makes the feature a plain heading that is
    no class feature, `sub-of:ANCHOR` a subheading of that feature, `list` a class feature that the option rule
    would have made a subheading. `after:ANCHOR` (joined to another decision with `;`) moves the row behind that
    feature: a sidebar that print sets before the text it belongs after."""
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
        if len(cells) != 4 or not all(k in DECISIONS or k.startswith(("tail-to:", "sub-of:", "after:")) for k in cells[2].split(";")):
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
SKIP_TABLES = {"on": False}         # the Advanced Race Guide sets its tables in sans-serif type
# The Advanced Class Guide and the Advanced Race Guide set text beside illustrations: a line may be indented without
# starting a paragraph, and a head may follow a sentence end in a line without the common indent. The other books
# have regular columns, where those two rules would join a head to the line before it.
ILLUSTRATED = {"on": False}


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
     "the alchemist's mutagen ability.", "the alchemist's mutagen ability, using his fighter level as his alchemist level."),
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
     "The creature gains fast healing 1 and a 25% chance", "The creature gains a 25% chance"),
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
        if paras and not re.search(r"(?:[.!?:]|[.!?]\))\s*$", paras[-1].rstrip().removesuffix(I_CLOSE)):      # a semicolon ends no paragraph
            gap = "" if re.search(r"[A-Za-z0-9]/$", paras[-1].rstrip()) else " "      # a slash at a line end joins the next word ("DR 5/" "cold iron")
            joined = fix_hyphens(paras[-1].rstrip() + gap + s, vocab)
            joined = re.sub(I_CLOSE + r"\s+" + I_OPEN + r"(?=[,;.)])", "", joined)      # an italic run that a line end cut
            paras[-1] = re.sub(I_CLOSE + r"\s+" + I_OPEN, " ", joined)
        else:
            paras.append(s)
    return paras


def print_md(feat: PrintFeature, links: list[tuple[str, str]], vocab: set[str], entry_id: str = "",
             keep_marks: bool = False) -> tuple[str, list[str], list[str]]:
    """The printed paragraphs as Markdown, the link texts that found no place, and the notes (misprint fixes,
    dropped asterisks)."""
    paras = join_wrapped([clean_runs(runs) for runs in feat.paras], vocab)
    text = "\n\n".join(paras)
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
    # a page reference of the book ("Pathfinder RPG Core Rulebook page 469"): the corpus links instead
    text = re.sub(r"\s*\(" + I_OPEN + r"?Pathfinder RPG[^()]*?(?:page[\s_\x01\x02]*|[\s\x01\x02]+)\d+(?:[–-]\d+)?\)", "", text)
    # a "(see ...)" cross-reference stays (owner ruling 16 of 2026-11-24). A page citation of another book without
    # "see" ("(Core Rulebook 123)", "(page 83)"): the corpus links instead
    xref = re.sub(r"\s*\([\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-5])?|"
                  r"Ultimate (?:Magic|Combat|Equipment|Campaign)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures)"
                  r"[\x02_]*[,\s]*(?:page[\s_\x01\x02]*)?\d+(?:[–-]\d+)?\)", "", text)
    # a bare book citation at the end of a parenthesis ("(including the alchemist's bomb class ability; Advanced
    # Player's Guide 28)", owner ruling 26): the corpus links the named rule
    xref = re.sub(r";\s*[\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-5])?|"
                  r"Ultimate (?:Magic|Combat|Equipment|Campaign)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures)"
                  r"[\x02_]*[,\s]*(?:page[\s_\x01\x02]*)?\d+(?:[–-]\d+)?(?=\))", "", xref)
    # a book reference in front of or behind a level inside a list ("(Advanced Player's Guide 212; 4th)", "(14th, Ultimate Magic)",
    # "(Ultimate Combat, 2nd)", owner ruling 26): the level stays, the reference goes
    book = (r"[\x01_]*(?:Pathfinder (?:RPG|Roleplaying Game) )?(?:Core Rulebook|Advanced Player.s Guide|Bestiary(?: [2-5])?|"
            r"Ultimate (?:Magic|Combat|Equipment|Campaign)|Advanced Race Guide|Game[Mm]astery Guide|Monster Codex|Occult Adventures)[\x02_]*")
    xref = re.sub(r"\(" + book + r"(?:\s*\d+(?:[–-]\d+)?)?[;,]\s*(?=\d+(?:st|nd|rd|th))", "(", xref)
    xref = re.sub(r",\s*" + book + r"(?:\s*\d+(?:[–-]\d+)?)?(?=\))", "", xref)
    # a parenthesis that is only "page 83" or "Core Rulebook page 469" (a title of capitalized words, then the page): a
    # citation with words of its own ("as if he had cast greater magic aura; see page 219", "as lesser simulacrum on
    # page 238 of Ultimate Magic") has a rule or a pointer and stays (owner rulings 16 and 26)
    xref = re.sub(r"\s*\(\s*(?:[\x01_]*[A-Z][\w'\u2019:, \-]*?[\x02_]*\s+)?page[\s_\x01\x02]*\d+(?:[\u2013-]\d+)?\s*\)", "", xref)
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
        links = list(links)
        for label, target in list(links):
            phrase = CONTEXT_LINKS.get((entry_id, label))
            if phrase and phrase in text:
                text = text.replace(phrase, phrase[: -len(label)] + f"[{label}]({target})", 1)
                links.remove((label, target))
        text, lost = apply_links(text, links)
    return render_marks(text), lost, notes


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
}


def feature_links(entry_id: str, f, head: str) -> list[tuple[str, str]]:
    """The links of a feature in the import, retargeted where LINK_RETARGETS says so, plus the extra ones."""
    links = [(lb, LINK_RETARGETS.get((entry_id, lb), tg)) for lb, tg in old_links(f)]
    return links + EXTRA_LINKS.get((entry_id, anchor_of(head)), [])


# A misprint of an opening text, which the compare keeps from the import when the words agree: the entry and the note
# that the review table records (owner ruling 9).
OPENING_NOTES = {
    "ref/arc-bard/masked-performer": 'misprint fixed: print has "a entertainer" in the opening text, written "an entertainer" (the import has the article right)',
}


# A link of the import that belongs on one phrase of the text, not on the first occurrence of its word: the entry, the
# label and the words that end with it. Fey Caller (Ultimate Intrigue p. 71): the import links "fey" in "also counts as a
# fey", the first "fey" of the text is the name of the archetype.
CONTEXT_LINKS = {
    ("ref/arc-unchained-summoner/fey-caller", "fey"): "counts as a fey",
}


def marks_key_printed(pfeats: list[PrintFeature], vocab: set[str]) -> bool:
    """Whether the printed section holds a key of its asterisks (a sentence that names the asterisk and is not the
    book's "An asterisk (*) indicates ..." line): then its marks stay (owner ruling 10)."""
    for pf in pfeats:
        for runs in pf.paras:
            t = finish_text(clean_runs(runs), vocab)
            t = re.sub(r"(?:^|\n\n)(?:An asterisk \(\\\*\)|\\\*) [Ii]ndicates[^\n]*", "", t)
            if re.search(r"\basterisks?\b", t, re.I):
                return True
    return False


def compare_entry(e: Entry, section: list[Para], book: Book) -> dict:
    """The comparison of one archetype with its printed section: a row for each printed head, in print
    order, then one for each feature of the import that print lacks."""
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
    keep = marks_key_printed(pfeats, vocab)
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
                         "listed": not is_scaffold(head) and not is_option_head(head, pf.bold), "option": is_option_head(head, pf.bold),
                         "name": pf.head})
            continue
        f = feats[idx]
        draft = build_draft(f)
        text, lost, pnotes = print_md(pf, feature_links(e.id, f, head), vocab, e.id, keep)
        # a printed "(see ...)" cross-reference is kept in the text but is not a rule word: the corpus links instead
        cmp = compare_feature(draft, re.sub(r"\s*\([Ss]ee\b[^()]*\)", "", text), set(tokens(ABILITY_TAG.sub("", f.name))), title_tokens)
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
        row["listed"] = not is_scaffold(head) and not f.pseudo and not row["option"]
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
        o = apply_errata(joined, e.id, "opening", o_notes)
        opening.append(render_marks(o))
        if o_notes and rows:
            rows[0]["notes"] += o_notes
    problems += errata_unused(e.id)
    links = [(m.group(2), m.group(3)) for b in opening_imp for m in LINK.finditer(logical(b))]
    for i, f in enumerate(feats):
        if i not in used:
            links += old_links(f)
    kept = [o for o in opening if o]
    # the opening text follows print: when the import's words differ from the printed ones (an unprinted sentence, a
    # broken row, `Prerequisites` rows for printed prose), the printed paragraphs are written
    gone = unprinted_notes(opening_imp, kept)
    imp_words = Counter(tokens(" ".join(logical(b) for i, b in enumerate(opening_imp) if i not in gone)))
    print_words = Counter(tokens(" ".join(kept)))
    diff = sorted(((imp_words - print_words) + (print_words - imp_words)).elements())
    if not diff and "\u2014" in " ".join(kept) and "\u2014" not in " ".join(logical(b) for i, b in enumerate(opening_imp) if i not in gone):
        diff = ["\u2014"]          # the import writes the printed em dash as " - "
    return {"rows": rows, "problems": problems, "opening": kept, "opening_links": links,
            "opening_dropped": [logical(opening_imp[i]) for i in gone], "opening_diff": diff}


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
        verb = re.search(r"\b(replaces?|alters?|changes?)\b", sentence, re.I)
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
        if TRADE_SENTENCE.search(sent) or re.match(r"(?:This|These|It)\b.{0,60}?\b(?:replaces?|alters?|changes?)\b", sent, re.I):
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
    for f in listed:
        for sop, ph, bare in sentences[f["anchor"]]:
            if not bare and not any(sop == trade_name(t)[0] and covers(ph, trade_name(t)[1]) for t in trades):
                problems.append(f"{f['head']}: the sentence \"This ability {sop} {ph}\" names no trade")
    return by, problems


# A stored trade whose printed name the reader cannot match to the printed sentence takes the printed
# words (owner instruction of 2026-11-24; the `feature` link and the ids stay). The TSV note records it.
TRADE_RENAMES = {
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
    ('ref/arc-fighter/skirmisher', '2nd level fighter bonus feat'): 'Bonus feat the fighter normally receives at 2nd level',
    # Blood of the Ancients (ruling 22: the stored name is the printed wording)
    ("ref/arc-investigator/antiquarian", "Alchemy (including Extracts)"): "Alchemy",
    ("ref/arc-wizard/arcane-warden", "5th-, 10th-, 15th-, and 20th-level bonus feats"): "The bonus feats gained at 5th, 10th, 15th, and 20th levels",
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
}


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
    ("ref/arc-warpriest/divine-commander", "mount"),
}

LEVEL_IN_FIRST_PARAGRAPH = {
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
}


# A stored trade that print states in the prose of a feature and in no trade sentence (owner ruling 28 of 2026-11-25):
# the entry, the stored name, the feature whose text states it. The check accepts the prose of the feature as support.
TRADE_PROSE_BY = {
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
}


def dropped_trade_indices(e: Entry) -> set[int]:
    """The indices of the stored trades that repeat another one without a `feature`, and of those that print
    does not support."""
    out = set()
    for i, t in enumerate(trades_of(e)):
        key = trade_name(t)
        if key in TRADE_MERGED.get(e.id, []) or key in TRADE_REMOVALS.get(e.id, []):
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
        out.append((t2, i))
    return out + [(dict(t), None) for t in TRADE_ADDITIONS.get(e.id, [])]


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
    name = re.sub(r"\s+(?:\d+/\w+|\d+d\d+|[+\-]\d.*|\d+)$", "", name.strip())
    name = re.sub(r"^[a-z]+'s\s+", "", fold(name))                 # "witch's familiar" is the name familiar
    return " ".join(stem(w) for w in re.findall(r"[a-z0-9']+", name))


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
    cache[class_id] = keys
    return keys


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
        elif kind == "sidebar":
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
                opening = [apply_links(o, res.get("opening_links", []))[0] for o in res["opening"]]
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
    for r in rows:
        edit = res.get("edits", {}).get((e.id, r["anchor"]))
        if edit:
            r["print"] = edit[0]
            r["status"] = "print"
            r["notes"] = [edit[1]] + [n for n in r["notes"] if n.startswith(("print:", "level", "ruling"))]
    for add in res.get("adds", {}).get(e.id, []):
        row = {"anchor": add["anchor"], "span": "", "page": "", "pseudo": False, "draft": "", "level_import": None,
               "head": add["head"], "print": add["text"].strip("\n"), "status": "print", "notes": [add["note"]],
               "listed": False, "name": add["head"], "option": False, "parent": add["parent"] or None}
        at = next((i for i, x in enumerate(rows) if x["anchor"] == add["after"]), len(rows) - 1)
        rows.insert(at + 1, row)
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
        opening = [apply_links(o, res.get("opening_links", []))[0] for o in res["opening"]]
        rows[0]["notes"].append("opening text written from print: the import differs in " + ", ".join(res["opening_diff"][:12])
                                + (" ..." if len(res["opening_diff"]) > 12 else ""))
    res["opening"] = opening
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
    for i, (t, origin) in enumerate(effective_trades_origin(e)):
        if origin is None:
            anchors = by.get(i) or [rows[0]["anchor"]]
            where = f' (feature `{t["feature"]}`)' if "feature" in t else ""
            note = f'trade added: {trade_name(t)[0]} "{trade_name(t)[1]}"{where}, which print states and the entry did not store'
            next(r for r in rows if r["anchor"] == anchors[0])["notes"].append(note)
            continue
        old = trades_of(e)[origin]
        if t.get("_no_by"):
            rows[0]["notes"].append(f'trade without `by`: {trade_name(old)[0]} "{trade_name(old)[1]}" has only a bare printed sentence')
            t = {k: v for k, v in t.items() if k != "_no_by"}
        if t.get("_prose_by"):
            rows[0]["notes"].append(f'trade by prose (ruling 28): {trade_name(old)[0]} "{trade_name(old)[1]}" is stated in the text of `{t["_prose_by"]}`, in no trade sentence')
            t = {k: v for k, v in t.items() if k != "_prose_by"}
        if (e.id, trade_name(old)[1]) in TRADE_RELINKS:
            rows[0]["notes"].append(f'trade relinked: "{trade_name(old)[1]}" now names `{TRADE_RELINKS[(e.id, trade_name(old)[1])]}`, the feature that print says it replaces')
        if trade_name(old)[1] in TRADE_UNLINKS.get(e.id, []):
            rows[0]["notes"].append(f'trade unlinked: "{trade_name(old)[1]}" loses its `feature` and `levels`: a trade of the whole Bomb feature (print: "functions as and replaces the standard alchemist bomb class feature", p. 20) overlaps a trade of one level of it, so the printed level trade is one unlinked trade')
        if old != t:
            anchors = by.get(i) or [rows[0]["anchor"]]
            note = ""
            if trade_name(old)[0] != trade_name(t)[0]:
                note = f'trade op fixed: stored as {trade_name(old)[0]} "{trade_name(old)[1]}", print says {trade_name(t)[0]}'
            if trade_name(old)[1] != trade_name(t)[1]:
                note += ("; " if note else "") + f'trade renamed: "{trade_name(old)[1]}" to "{trade_name(t)[1]}" to match the printed sentence'
                if (e.id, trade_name(t)[1]) in TRADE_LEVELS:
                    note += f"; its levels are now {TRADE_LEVELS[(e.id, trade_name(t)[1])]}, the printed levels"
            next(r for r in rows if r["anchor"] == anchors[0])["notes"].append(note)
    for origin in sorted(dropped_trade_indices(e)):
        old = trades_of(e)[origin]
        if trade_name(old) in TRADE_REMOVALS.get(e.id, []):
            ruling = "ruling 39, which keeps the removal; ruling 17" if e.id in TRADE_REMOVAL_RULED else "ruling 17"
            rows[0]["notes"].append(f'trade dropped ({ruling}): {trade_name(old)[0]} "{trade_name(old)[1]}" has no printed support in any sentence')
            continue
        if trade_name(old) in TRADE_MERGED.get(e.id, []):
            rows[0]["notes"].append(f'trade merged: {trade_name(old)[0]} "{trade_name(old)[1]}" is the printed trade of the sentence that each feature prints with the same words; one trade names all three features')
            continue
        rows[0]["notes"].append(f'duplicate trade left out: {trade_name(old)[0]} "{trade_name(old)[1]}" was stored twice, once without its feature link')
    for r in rows:
        first = r["print"].split("\n\n", 1)[0] if r["print"] else ""
        r["level"] = lead_level(first)
        if r["level"] is None and r["listed"]:
            # a level that print states after a flavor sentence or inside the sentence (reviewed list)
            if (e.id, r["anchor"]) in LEVEL_IN_FIRST_PARAGRAPH:
                m = re.search(r"\b(?:At|Starting at|Beginning at)\s+(\d+)(st|nd|rd|th)\s+level\b", first, re.I)
                if m and 1 <= int(m.group(1)) <= 20 and m.group(2) == ordinal(int(m.group(1)))[len(m.group(1)):]:
                    r["level"] = int(m.group(1))
                    r["notes"].append(f"level {r['level']}: print says \"{m.group(0)}\" in its first paragraph, after an opening sentence")
        if r["level"] is None and r["listed"]:
            m = re.match(r"[^.]*?\bgains this ability at (\d+)(st|nd|rd|th) level\b", first)
            if m and 1 <= int(m.group(1)) <= 20 and m.group(2) == ordinal(int(m.group(1)))[len(m.group(1)):]:
                r["level"] = int(m.group(1))
                r["notes"].append(f"level {r['level']}: print says \"gains this ability at {ordinal(r['level'])} level\"")
        if r["level"] is None and r["listed"]:
            mine = [trades[i] for i, a in by.items() if a == [r["anchor"]]]
            levels = {tuple(t.get("levels") or ()) for t in mine}
            if mine and len(levels) == 1 and len(next(iter(levels))) == 1 and all("levels" in t for t in mine):
                r["level"] = next(iter(levels))[0]
                r["notes"].append("level from the trade")
            elif (e.id, r["anchor"]) in LEVEL_ONE_REPLACES:
                r["level"] = 1
                r["notes"].append("level 1 (ruling 35): replaces " + ", ".join(trade_name(t)[1] for t in mine) + ", a 1st-level feature of the class (the class table lists it as `Blessing (minor)`)")
            elif mine:
                # ruling 11: the feature replaces features that the base class gains at 1st level. Print states no level here, so
                # the import's level (a line of the feature's own text, "At 2nd Level: ...") does not stop the rule (final review of
                # batch 3); a differing import level is the hold below, which a hand decision settles.
                firsts = []
                for t in mine:
                    cls = t.get("class") or (e.classes[0] if e.classes else "")
                    # a trade of the 1st level: its `levels` include 1, or its name states "1st" ("bonus feats gained at 1st, 2nd,
                    # and 6th levels", "1st-, 7th-, and 15th-level deeds"), or the class table lists it at 1st level
                    firsts.append(1 in (t.get("levels") or ()) or bool(re.search(r"\b1st\b", trade_name(t)[1]))
                                  or (bool(cls) and first_level_key(trade_name(t)[1]) in class_first_level(corpus, cls, class_cache)))
                # ruling 35: level 1 when any feature that it replaces is a 1st-level feature, even if it also replaces later ones
                if any(f and trade_name(t)[0] == "replaces" for f, t in zip(firsts, mine)):
                    r["level"] = 1
                    named = any(f and (1 in (t.get("levels") or ()) or re.search(r"\b1st\b", trade_name(t)[1])) for f, t in zip(firsts, mine))
                    r["notes"].append("level 1: replaces " + ", ".join(trade_name(t)[1] for t in mine if trade_name(t)[0] == "replaces")
                                      + (", of which one is gained at 1st level (the printed level of the trade, or the class table)" if named
                                         else ", of which one is gained at 1st level in the class table"))
        if r["level"] is not None and r["level_import"] is not None and r["level"] != r["level_import"] and r["status"] != "hold" \
                and (e.id, r["anchor"]) not in decisions:
            r["status"] = "hold"
            r["notes"].append(f"level: corpus {ordinal(r['level_import'])}, print {ordinal(r['level'])}")
    if e.id in OPENING_NOTES:
        rows[0]["notes"].append(OPENING_NOTES[e.id])
    for text in res.get("opening_dropped", []):
        rows[0]["notes"].append("opening note that print does not have dropped (ruling 10): \u201c" + " ".join(text.split()[:9]) + " \u2026\u201d")
    return {"rows": rows, "problems": problems, "by": by, "opening": res["opening"], "dropped": dropped,
            "opening_from_print": opening_from_print}


def configure_book(book: str) -> None:
    """The layout switches of a book (the leaf tool `feature-prose-540-leaves.py` sets the same ones)."""
    ERRATA_CTX["book"] = book
    SKIP_TABLES["on"] = book == "advanced-race-guide"
    ILLUSTRATED["on"] = book in ("advanced-class-guide", "advanced-race-guide", "adventurers-guide", "ultimate-wilderness")
    SECTION_STOPS["on"] = book in ("adventurers-guide", "ultimate-wilderness")
    ANY_TITLE_ENDS["on"] = book in ("blood-of-the-ancients",)
    SMALL_CAP_TITLES["on"] = book in ("blood-of-the-ancients",)


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
    stops = {squash(x.title) for x in entries} | CLASS_TITLES | UNTYPED_ARCHETYPE_TITLES
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
            hits = [b for b in whole if b.kind == "title" and squash(b.plain()) in (squash(e.title), squash(e.title) + "archetype")]
            if len(hits) != 1:
                rows.append(entry_hold_row(e, f"no page cited, and the title is printed {len(hits)} times"))
                continue
            section = find_section(whole, e.title, stops)
        else:
            blocks = read_blocks(bk, max(1, page + 1 - 3), min(page + 1 + 4, top))
            section = find_section(blocks, e.title, stops)
        if section is None:
            rows.append(entry_hold_row(e, f"title not found near page {page}"))
            continue
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
    ("ref/arc-summoner/leshy-caller", "plant-eidolon-subtype"): "Plant Eidolon Subtype",
    ("ref/arc-unchained-summoner/leshy-caller", "plant-eidolon-subtype"): "Plant Eidolon Subtype",
}


def convert_text(e: Entry, prop: dict, rows: list[dict]) -> str:
    status = {r["anchor"]: r["status"] for r in rows if r["anchor"]}
    feats = prop["feature"]
    full = [dict(f, print=feature_text(f, status.get(f["anchor"], "print"))) for f in feats]
    by, problems = assign_by(effective_trades(e), with_children(full), opening_texts(full, prop.get("opening", [])))
    if problems:
        raise ValueError("; ".join(problems))
    probe = {namekey(f["head"]) for f in feats}
    opening, _ = parse_import(e.body, probe)
    parts = ["\n".join(b) for i, b in enumerate(opening) if i not in unprinted_notes(opening, prop.get("opening", []))]
    if prop.get("opening_from_print"):
        parts = list(prop["opening"])
    for f in feats:
        depth, up = 0, f
        while up.get("parent"):
            depth += 1
            up = next((x for x in feats if x["anchor"] == up["parent"]), {})
        head = HEAD_REWRITES.get((e.id, f["anchor"]), f["head"])
        parts.append(f"{'#' * (2 + depth)} {re.sub(r'(?<!\\)([*_])', r'\\\1', head)} {{#{f['anchor']}}}")
        text = feature_text(f, status.get(f["anchor"], "print"))
        parts += [p for p in text.split("\n\n") if p.strip()]
    front = edit_front(e.front, feats, by, len(trades_of(e)), TRADE_ADDITIONS.get(e.id), dropped_trade_indices(e))
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

# A printed trade sentence that states no trade on purpose (listed in the PR body): Weretouched's Lycanthrope Aspect says
# "This alters her other class features, as detailed in each relevant class feature", a cross-reference to the features that follow.
TRADE_GAPS_ALLOWED = {("ref/arc-shifter/weretouched", "her other class features, as detailed in each relevant class feature")}


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
        if head is None:
            continue
        for sop, ph, _bare in trade_sentences(part[m.end():], ABILITY_TAG.sub("", head).strip()):
            if re.match(r"(?:grants|to|does|do|not)\b", ph) or (e.id, ph) in TRADE_GAPS_ALLOWED:
                continue                    # "This change to spells doesn't apply", "This ability does not alter ...": no trade sentence
            if not any(op == sop and covers(ph, name) for op, name in trades):
                out.append(f'{head}: the sentence "This {sop} {ph}" has no stored trade')
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
            want = [(f["anchor"], f.get("level")) for f in fields["features"]]
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
    print(f"{book}: {len(entries)} archetypes, {converted} converted, {held} not converted")
    for err in errors:
        print("error:", err)
    return 1 if errors else 0


# ---- --self-test ----------------------------------------------------------------------------------------

def self_test() -> int:
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
    # a parenthesis that has words of its own stays, a bare page citation goes
    pf = PrintFeature("Hidden Magic (Sp)", [[("Items (as if he had cast greater magic aura; see page 219) and (page 83) and (Core Rulebook page 469) end.", False, False)]], 67)
    text, _, notes = print_md(pf, [], set(), "ref/arc-monk/black-asp")
    eq(text, "Items (as if he had cast greater magic aura; see page 219) and and end.", "a citation with words stays, a bare one goes")
    eq(is_scaffold("Weapon and Armor Proficiencies") and is_scaffold("Class Skills") and is_scaffold("Skill Ranks per Level"), True, "scaffold variants")
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
    eq(join_wrapped(["the vox's mesmerist spells use both", "thought and verbal components. Next."], set()), ["the vox's mesmerist spells use both thought and verbal components. Next."], "wrapped sidebar lines join")
    # ruling 11: the Special column of the class table, with its suffixes, never a spell-slot or fast-movement column
    import tempfile
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
    print(f"self-test: {ok} checks passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", nargs="?", default=str(ROOT))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--book", default=None, help="publication id (--check without it covers every book with a review TSV)")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    ap.add_argument("--only", default="")
    ap.add_argument("--forget-checker-holds", action="store_true",
                    help="--compare: forget the holds that an earlier --write recorded from the checker (after the script or the app changed)")
    ap.add_argument("--checker")
    args = ap.parse_args()
    global FORGET_CHECKER_HOLDS
    FORGET_CHECKER_HOLDS = args.forget_checker_holds
    if args.self_test:
        return self_test()
    if (args.compare or args.write) and not args.book:
        raise SystemExit("--compare and --write need --book ID")
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
            if not p.name.endswith((".decisions.tsv", ".queue.tsv")))
        status = 0
        for b in books:
            args.book = b
            status |= run_check(args)
        return status
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
