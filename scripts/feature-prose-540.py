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
ROOT = HERE.parent

TSV_HEADER = [
    "entry", "feature", "anchor", "listed", "level", "source", "status", "note", "page", "span_sha256",
]
STATUSES = ("pending", "print", "draft", "edit", "hold")
WRITABLE = ("print", "draft", "edit")

# Headings that scaffold a feature and are never features themselves (owner ruling of 2026-11-24 on
# phynics/cast-iron#540): never listed in `features`, never a `by` target.
SCAFFOLD = {
    "size", "speed", "attack", "ac", "abilityscores", "companiontype", "prerequisites", "effect", "use",
    "cost", "action", "bonusspells", "bonusfeats", "weaponandarmorproficiency", "weaponandarmorproficiencies",
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
    """Wrap the first whole-word occurrence of each old link text that is not inside a link already.
    The spans of the links already placed are found by their own shape (`[label](target)`, a target
    holds no parenthesis), so printed parentheses and brackets do not fool the test. Returns the text
    and the link texts that found no place."""
    lost = []
    for label, target in links:
        words = [re.escape(w) for w in label.replace("\\", "").split()]
        if not words:
            continue
        pat = re.compile(r"(?<![\w\[])" + r"\s+".join(words) + r"(?![\w\]])", re.I)
        spans = [(m.start(), m.end()) for m in LINK_SPAN.finditer(text)]
        done = False
        for m in pat.finditer(text):
            if any(a <= m.start() < b for a, b in spans):
                continue
            text = text[: m.start()] + f"[{m.group(0)}]({target})" + text[m.end():]
            done = True
            break
        if not done:
            lost.append(label)
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
    s = re.sub(r"(?<![\w)\]])–(?=\d)", "-", s)           # a minus sign
    s = re.sub(r"(?<=\w) – (?=\d)", " - ", s)             # a minus operator ("druid level – 2")
    s = fix_ligatures(s, vocab)
    s = fix_hyphens(s, vocab)
    # the extraction pads italic runs with blanks
    s = re.sub(I_OPEN + r"\s+", " " + I_OPEN, s)
    s = re.sub(r"\s+" + I_CLOSE, I_CLOSE + " ", s)
    s = re.sub(I_CLOSE + I_OPEN, "", s)
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
        both = f"{a}-{b}".lower()
        glued = f"{a}{b}".lower()
        if both in vocab:
            return f"{a}-{b}"
        if glued in vocab:
            return f"{a}{b}"
        return f"{a}-{b}"

    return re.sub(r"\b([A-Za-z]+)- (?=[a-z])([A-Za-z]+)\b", join, s)


def render_marks(s: str) -> str:
    return s.replace(I_OPEN, "_").replace(I_CLOSE, "_")


# ---- the print: pdftohtml -xml ------------------------------------------------------------------------

TEXT_EL = re.compile(r'<text top="(-?\d+)" left="(-?\d+)" width="(-?\d+)" height="(-?\d+)" font="(\d+)">(.*?)</text>', re.S)
FONT_EL = re.compile(r'<fontspec id="(\d+)" size="(\d+)" family="([^"]*)" color="([^"]*)"')
TAG_SPLIT = re.compile(r"(</?[bi]>)")
BODY_TOP = (95, 1075)
COL_SPLIT = 460
COL_LEFT = (108, 468)      # the left edge of the two columns of the Advanced Player's Guide


@dataclass
class Para:
    kind: str                                # para | title
    runs: list[tuple[str, bool, bool]]
    page: int                                # printed page
    col: int

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
    pages: dict[int, list[tuple[int, int, int, str]]]    # pdf page -> (top, left, font, raw)
    printed: dict[int, int]                              # pdf page -> printed page
    vocab: set[str]


def load_book(xml_path: Path) -> Book:
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
            if top > BODY_TOP[1] and plain.isdigit():
                printed[num] = int(plain)
            items.append((top, left, int(font), raw))
            for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", plain):
                words[w.lower()] += 1
                if "-" in w:
                    for part in w.lower().split("-"):
                        words[part] += 1
        pages[num] = items
    vocab = {w for w, _ in words.items()}
    return Book(fonts, pages, printed, vocab)


def page_lines(book: Book, num: int) -> list[dict]:
    by_col: dict[int, list] = {0: [], 1: []}
    for top, left, font, raw in book.pages.get(num, []):
        if BODY_TOP[0] <= top <= BODY_TOP[1]:
            by_col[0 if left < COL_SPLIT else 1].append((top, left, font, raw))
    lines = []
    for col in (0, 1):
        cur: list[dict] = []
        for top, left, font, raw in sorted(by_col[col], key=lambda x: (x[0], x[1])):
            if cur and abs(cur[-1]["top"] - top) <= 4:
                cur[-1]["parts"].append((left, raw))
                cur[-1]["size"] = max(cur[-1]["size"], book.fonts[str(font)])
            else:
                cur.append({"col": col, "top": top, "size": book.fonts[str(font)], "parts": [(left, raw)]})
        for ln in cur:
            ln["parts"].sort()
            ln["left"] = ln["parts"][0][0]
            runs: list = []
            for _, raw in ln["parts"]:
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
    for num in range(first, last + 1):
        if num not in book.pages:
            continue
        shown = book.printed.get(num, num - 1)
        for ln in page_lines(book, num):
            indent = ln["left"] - COL_LEFT[ln["col"]]
            if ln["size"] >= 16:
                if out and out[-1].kind == "title" and out[-1].col == ln["col"] and out[-1].page == shown:
                    out[-1].runs += [(" ", True, False)] + ln["runs"]
                else:
                    out.append(Para("title", list(ln["runs"]), shown, ln["col"]))
                continue
            if not out or out[-1].kind == "title" or indent >= 8:
                out.append(Para("para", list(ln["runs"]), shown, ln["col"]))
            else:
                out[-1].runs.append((" ", False, False))
                out[-1].runs += ln["runs"]
    for p in out:
        p.runs = merge_runs(p.runs)
    return out


def find_section(blocks: list[Para], title: str) -> list[Para] | None:
    key = squash(title)
    for i, b in enumerate(blocks):
        if b.kind == "title" and squash(b.plain()) == key:
            j = i + 1
            while j < len(blocks) and blocks[j].kind != "title":
                j += 1
            return blocks[i:j]
    return None


@dataclass
class PrintFeature:
    head: str
    paras: list[list[tuple[str, bool, bool]]]        # runs of each printed paragraph (the head cut off)
    page: int


def head_candidate(p: Para) -> tuple[str, list, bool] | None:
    """The leading bold (or italic) run before the colon of a paragraph, and the rest of its runs."""
    if not p.runs:
        return None
    first = p.runs[0]
    style = "bold" if first[1] else ("italic" if first[2] else "")
    if not style:
        return None
    i, head = 0, ""
    while i < len(p.runs) and (p.runs[i][1] if style == "bold" else p.runs[i][2]):
        head += p.runs[i][0]
        i += 1
    head = re.sub(r"\s+", " ", head).strip()
    rest = p.runs[i:]
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
            tail_ok = not rest or colon
            if tail_ok and (bold or (namekey(head) in want)):
                is_head = True
        if is_head:
            head, rest, _ = cand
            rest = list(rest)
            if rest and rest[0][0].lstrip().startswith(":"):
                t = rest[0][0].lstrip()[1:]
                rest[0] = (t, rest[0][1], rest[0][2])
            feats.append(PrintFeature(head, [rest] if rest else [[]], p.page))
        elif feats:
            feats[-1].paras.append(p.runs)
        else:
            opening.append(p.runs)
    return opening, feats


# ---- trade sentences ---------------------------------------------------------------------------------

TRADE_SENTENCE = re.compile(
    r"(?:^|(?<=[.!?]\s))((?:This|These|It)\b(?:\s+(?:ability|abilities|class|feature|features|power|powers|archetype|performance|performances|trick|tricks|talent|talents|hex|hexes|discovery|discoveries|revelation|revelations|mercy|mercies|deed|deeds|exploit|exploits|arcana|arcanum|feat|feats|also|otherwise|acts|works|functions|as|like|and))*\s+(replaces?|alters?)\b[^.]*\.)",
    re.I,
)


def trade_sentences(text: str) -> list[tuple[str, str, bool]]:
    """[(op, phrase, bare)] of the trade sentences of a text: "This ability replaces bravery." gives
    ("replaces", "bravery", False). A bare sentence ("These replace the normal attack roll bonus.") has no
    ability, feature, power or archetype in its subject: the app counts it only when it names a stored trade."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[\\_*]", "", text)
    out = []
    for m in TRADE_SENTENCE.finditer(text):
        op = "replaces" if m.group(2).lower().startswith("replace") else "alters"
        sentence = m.group(1)
        subject = re.match(r"^(?:This|These|It)\b(.*?)\b(?:replaces?|alters?)\b", sentence, re.I).group(1)
        bare = not re.search(r"\b(?:ability|abilities|feature|features|power|powers|archetype|performances?|tricks?|talents?|hex(?:es)?|discover(?:y|ies)|revelations?|merc(?:y|ies)|deeds?|exploits?|arcana|arcanum)\b", subject, re.I)
        phrase = re.sub(r"^(?:This|These|It)\b.*?\b(?:replaces?|alters?)\b", "", sentence, flags=re.I).strip().rstrip(".")
        out.append((op, phrase, bare))
    return out


def phrase_tokens(text: str) -> list[str]:
    text = fold(text).replace("'s", "")
    words = re.findall(r"[a-z0-9]+", text)
    return [stem(w) for w in words if w not in ("the", "a", "an", "standard", "ability", "feature", "class")]


def covers(phrase: str, trade_name: str) -> bool:
    """Whether the printed phrase of a trade sentence names the trade (a step list such as "armor training
    1, 2, 3, and 4" names the trade `Armor training 3`). The app's drift check is the authority; this
    only picks the features that print the trade."""
    p = phrase_tokens(phrase)
    t = phrase_tokens(ABILITY_TAG.sub("", trade_name))
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

LOOSE_TRADE = re.compile(r"(?:^|(?<=[.!?]\s))(?:This|These|It)\b[^.]{0,60}?\b(?:replaces?|alters?)\b[^.]*\.", re.I)
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
    r"increases?\s+by\s+\+?(\d+)[^.]*?(?:every|for every|per)\s+(\w+)\s+levels?\s+(?:after|beyond|above)\s+(\d+)(?:st|nd|rd|th)", re.I)

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
    for level in range(start, 21):
        printed = b + s_ * ((level - k) // n)
        stored = max(base_c + level * num // den, minimum)
        if printed != stored:
            return "differ", [f"at level {level} print gives +{printed}, the corpus {stored}"]
    return "equal", [f"+{b}", f"+{s_}", str(k), str(n)]


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
        for f in e.get("feature", []):
            out.append("\n[[entry.feature]]\n")
            out.append(f"anchor = {toml_str(f['anchor'])}\nhead = {toml_str(f['head'])}\nlisted = {str(f['listed']).lower()}\n")
            if f.get("level") is not None:
                out.append(f"level = {f['level']}\n")
            out.append(f"print = {toml_str(f['print'])}\n")
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
    ("ref/arc-ranger/horse-lord", "of the him", "of him", "the sentence needs no article before the pronoun"),
    ("ref/arc-monk/hungry-ghost-monk", "The ability replaces diamond soul", "This ability replaces diamond soul",
     "every other trade sentence of the book starts \"This ability\""),
    ("ref/arc-rogue/investigator", "thought reexamining", "thoughtful reexamining",
     "the advanced rogue talent is Thoughtful Reexamining, which the same book prints in full for the burglar"),
]


def is_scaffold(head: str) -> bool:
    k = namekey(head)
    return k in SCAFFOLD or k + "s" in SCAFFOLD or k.rstrip("s") in SCAFFOLD


def print_md(feat: PrintFeature, links: list[tuple[str, str]], vocab: set[str], entry_id: str = "") -> tuple[str, list[str], list[str]]:
    """The printed paragraphs as Markdown, the link texts that found no place, and the notes (misprint fixes,
    dropped asterisks)."""
    paras = []
    for runs in feat.paras:
        s = finish_text(clean_runs(runs), vocab)
        if s:
            paras.append(s)
    text = "\n\n".join(paras)
    notes: list[str] = []
    fixed = re.sub(r"^A (\d+(?:st|nd|rd|th) level\b)", r"At \1", text)
    if fixed != text:
        notes.append("misprint fixed: print has \"A " + text.split(" level", 1)[0][2:] + " level\", the lead is \"At " + text.split(" level", 1)[0][2:] + " level\"")
        text = fixed
    for eid, wrong, right, why in MISPRINTS:
        if eid == entry_id and wrong in text:
            text = text.replace(wrong, right)
            notes.append(f"misprint fixed: print has \"{wrong}\", written \"{right}\" ({why})")
    # a page reference of the book ("Pathfinder RPG Core Rulebook page 469"): the corpus links instead
    text = re.sub(r"\s*\(" + I_OPEN + r"?Pathfinder RPG[^()]*?(?:page[\s_\x01\x02]*|[\s\x01\x02]+)\d+(?:[–-]\d+)?\)", "", text)
    # print's asterisks mark a talent or a feat that has a prerequisite; the key is not printed here (ruling 10)
    stripped = re.sub(r"(?<=[\w)\]])\\\*", "", text)
    if stripped != text:
        notes.append("print asterisks without their key dropped")
        text = stripped
    lost: list[str] = []
    if links:
        text, lost = apply_links(text, links)
    return render_marks(text), lost, notes


def head_text(head: str) -> str:
    return re.sub(r"\s+", " ", head.replace("’", "'").replace("‘", "'")).strip()


def compare_entry(e: Entry, section: list[Para], book: Book) -> dict:
    """The comparison of one archetype with its printed section: a row for each printed head, in print
    order, then one for each feature of the import that print lacks."""
    plain_names = [m.group(1) for b in blocks_of(e.body) for m in [NAME_BLOCK.match(logical(b))] if m]
    probe = {namekey(h) for h in [head_of_para(p) for p in section[1:]] if h}
    opening_imp, feats = parse_import(e.body, probe)
    names = [f.name for f in feats]
    opening_print, pfeats = split_print(section, plain_names + [tail_name(n) for n in names])
    vocab = book.vocab | {w.lower() for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", e.body)} | {
        p.lower() for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)+", e.body) for p in w.split("-")}
    # match the heads in order, so a name that occurs twice is matched to its own printed head
    used: set[int] = set()
    last = -1
    matched: list[int | None] = []
    for pf in pfeats:
        key = namekey(pf.head)
        idx = next((i for i in range(last + 1, len(feats)) if i not in used and namekey(feats[i].name) == key), None)
        if idx is not None:
            used.add(idx)
            last = idx
        matched.append(idx)
    problems: list[str] = []
    lost_heads = [feats[i].name for i in range(len(feats)) if i not in used]
    if lost_heads:
        problems.append("head not printed: " + ", ".join(lost_heads))
    title_tokens = set(tokens(e.title)) | {w for c in e.classes for w in tokens(c.split("/")[-1].replace("-", " "))}
    rows = []
    for pf, idx in zip(pfeats, matched):
        if idx is None:
            text, _, pnotes = print_md(pf, [], vocab, e.id)
            rows.append({"anchor": anchor_of(pf.head), "span": "", "page": pf.page, "pseudo": False, "draft": "",
                         "level_import": None, "head": head_text(pf.head), "print": text, "status": "print",
                         "notes": ["head printed, not in the import: added from print"] + pnotes,
                         "listed": not is_scaffold(pf.head), "name": pf.head})
            continue
        f = feats[idx]
        draft = build_draft(f)
        text, lost, pnotes = print_md(pf, old_links(f), vocab, e.id)
        cmp = compare_feature(draft, text, set(tokens(ABILITY_TAG.sub("", f.name))), title_tokens)
        row = {"anchor": anchor_of(pf.head), "span": f.span_sha(), "page": pf.page, "pseudo": f.pseudo,
               "draft": draft.text, "level_import": draft.level, "head": head_text(pf.head), "print": text,
               "status": cmp.status, "notes": list(cmp.notes) + pnotes, "name": pf.head}
        if lost:
            row["notes"].append("link not placed: " + ", ".join(lost))
        row["listed"] = not is_scaffold(pf.head) and not f.pseudo
        if (e.id, row["anchor"]) in PRINT_WINS and row["status"] == "hold":
            row["status"], row["notes"] = "print", [PRINT_WINS[(e.id, row["anchor"])]] + pnotes
        rows.append(row)
    for i, f in enumerate(feats):
        if i not in used:
            rows.append({"anchor": anchor_of(f.name), "span": f.span_sha(), "page": "", "pseudo": f.pseudo,
                         "draft": build_draft(f).text, "level_import": None, "head": head_text(f.name), "print": "",
                         "status": "hold", "notes": ["head not printed"], "listed": False, "name": f.name})
    opening = [render_marks(finish_text(clean_runs(r), vocab)) for r in opening_print]
    return {"rows": rows, "problems": problems, "opening": [o for o in opening if o]}


def assign_by(trades: list[dict], listed: list[dict], opening: list[str]) -> tuple[dict[int, list[str]], list[str]]:
    """For each trade, the anchors of the listed features whose printed text states it. A trade that print
    states only in the opening text (the blocks before the first listed feature) gets no `by`. A trade that
    print never states in a sentence takes the listed feature of its own name that prints no trade sentence
    (owner ruling A of 2026-11-24: the feature prints the changed ability). Returns the map and the problems."""
    problems: list[str] = []
    by: dict[int, list[str]] = {}
    sentences = {f["anchor"]: trade_sentences(f["print"]) for f in listed}
    opening_sentences = [s for o in opening for s in trade_sentences(o)]
    for i, t in enumerate(trades):
        op, name = trade_name(t)
        anchors = [f["anchor"] for f in listed
                   if any(sop == op and covers(ph, name) for sop, ph, _ in sentences[f["anchor"]])]
        if anchors:
            by[i] = anchors
        elif any(sop == op and covers(ph, name) for sop, ph, _ in opening_sentences):
            by[i] = []
        else:
            own = [f["anchor"] for f in listed
                   if not sentences[f["anchor"]] and namekey(f["head"]) == namekey(name)]
            if own:
                by[i] = own
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
    ("ref/arc-druid/urban-druid", "Spontaneous casting"): "Ability to spontaneously cast summon nature's ally spells",
    ("ref/arc-ranger/skirmisher", "Spellcasting ability"): "Spells",
    ("ref/arc-monk/monk-of-the-empty-hand", "Weapon proficiencies"): "Normal monk weapon proficiencies",
}


def effective_trades(e: Entry) -> list[dict]:
    out = []
    for t in trades_of(e):
        op, name = trade_name(t)
        new = TRADE_RENAMES.get((e.id, name))
        out.append(dict(t, **{op: new}) if new else t)
    return out


def opening_texts(rows: list[dict], opening: list[str]) -> list[str]:
    """The text that the app reads as the opening: the printed opening and the unlisted sections before the
    first listed feature."""
    texts = list(opening)
    for r in rows:
        if r["listed"]:
            break
        texts.append(r["print"])
    return texts


def late_unlisted_sentences(rows: list[dict]) -> list[str]:
    """Trade sentences in an unlisted section after the first listed feature: the check refuses them."""
    seen, out = False, []
    for r in rows:
        if r["listed"]:
            seen = True
        elif seen and r["print"] and any(not bare for _, _, bare in trade_sentences(r["print"])):
            out.append(r["head"])
    return out


def class_first_level(corpus: Path, class_id: str, cache: dict) -> set[str]:
    """The name keys of the features that the class table of a base class lists at 1st level."""
    if class_id in cache:
        return cache[class_id]
    path = corpus / "entries" / (class_id.removeprefix("ref/") + ".md")
    keys: set[str] = set()
    if path.exists():
        for ln in path.read_text(encoding="utf-8").split("\n"):
            if ln.startswith("|1st|"):
                last = [c for c in ln.strip().strip("|").split("|") if c.strip()][-1]
                for item in last.split(","):
                    keys.add(namekey(re.sub(r"\s*[+\-]\d.*$", "", item)))
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
    for a, n in Counter(r["anchor"] for r in rows).items():
        if n > 1:
            problems.append(f"anchor `{a}` occurs {n} times")
    listed = [r for r in rows if r["listed"]]
    trades = effective_trades(e)
    by, more = assign_by(trades, listed, opening_texts(rows, res["opening"])) if all(r["print"] for r in listed) else ({}, [])
    problems += more
    for head in late_unlisted_sentences(rows):
        problems.append(f"{head}: a trade sentence under a heading that is not a feature, after the first feature")
    for i, t in enumerate(trades):
        old = trades_of(e)[i]
        if old != t:
            anchors = by.get(i) or [rows[0]["anchor"]]
            note = f'trade renamed: "{trade_name(old)[1]}" to "{trade_name(t)[1]}" to match the printed sentence'
            next(r for r in rows if r["anchor"] == anchors[0])["notes"].append(note)
    for r in rows:
        first = r["print"].split("\n\n", 1)[0] if r["print"] else ""
        r["level"] = lead_level(first)
        if r["level"] is None and r["listed"]:
            mine = [trades[i] for i, a in by.items() if a == [r["anchor"]]]
            levels = {tuple(t.get("levels") or ()) for t in mine}
            if mine and len(levels) == 1 and len(next(iter(levels))) == 1 and all("levels" in t for t in mine):
                r["level"] = next(iter(levels))[0]
                r["notes"].append("level from the trade")
            elif mine and r["level_import"] in (None, 1):
                # ruling 11: the feature replaces features that the base class gains at 1st level
                firsts = []
                for t in mine:
                    cls = t.get("class") or (e.classes[0] if e.classes else "")
                    firsts.append(bool(cls) and namekey(trade_name(t)[1]) in class_first_level(corpus, cls, class_cache))
                if all(firsts) and all(trade_name(t)[0] == "replaces" for t in mine):
                    r["level"] = 1
                    r["notes"].append("level 1: replaces " + ", ".join(trade_name(t)[1] for t in mine) + ", gained at 1st level in the class table")
        if r["level"] is not None and r["level_import"] is not None and r["level"] != r["level_import"] and r["status"] != "hold":
            r["status"] = "hold"
            r["notes"].append(f"level: corpus {ordinal(r['level_import'])}, print {ordinal(r['level'])}")
    return {"rows": rows, "problems": problems, "by": by, "opening": res["opening"]}


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    title = publication_title(corpus, book)
    pdf = find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = load_book(book_xml(pdf, Path(args.cache)))
    entries = load_entries(corpus, book, args.only)
    old_rows = read_tsv(tsv_path(corpus, book))
    old_props = read_proposals(proposals_path(corpus, book))
    done = {e.id for e in entries if e.converted}
    redo = {e.id for e in entries if not e.converted}
    rows: list[dict] = [r for r in old_rows if r["entry"] in done or r["entry"] not in redo]
    props: dict[str, dict] = {k: v for k, v in old_props.items() if k not in redo and k not in done}
    for e in entries:
        if e.converted:
            continue
        page = int(e.page) if e.page.isdigit() else None
        if page is None:
            rows.append(entry_hold_row(e, "no page cited"))
            continue
        top = max(bk.pages)
        blocks = read_blocks(bk, max(1, page + 1 - 3), min(page + 1 + 4, top))
        section = find_section(blocks, e.title)
        if section is None:
            rows.append(entry_hold_row(e, f"title not found near page {page}"))
            continue
        fin = finalize(e, compare_entry(e, section, bk))
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
        if prev and prev["status"] == "hold" and prev["note"].startswith("checker:") and prev["span_sha256"] == r["span"]:
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
        if r["level"] is not None and r["listed"]:
            f["level"] = r["level"]
        if edit is not None:
            f["edit"] = edit
        feats.append(f)
    return rows, {"id": e.id, "hold": hold, "opening": fin["opening"], "feature": feats}


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


def edit_front(front: str, feats: list[dict], by: dict[int, list[str]], n_trades: int) -> str:
    lines = front.split("\n")
    out, in_fields, in_trades, k = [], False, False, 0
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
            elif ln.strip().startswith("{"):
                m = re.match(r"^(\s*\{.*?) \},?\s*$", ln)
                if not m:
                    raise ValueError(f"trade line not understood: {ln}")
                if by.get(k):
                    anchors = ", ".join(f'"{a}"' for a in by[k])
                    ln = f"{m.group(1)}, by = [{anchors}] }},"
                k += 1
        out.append(ln)
    if k != n_trades:
        raise ValueError(f"{k} trade lines, want {n_trades}")
    return "\n".join(out)


def convert_text(e: Entry, prop: dict, rows: list[dict]) -> str:
    status = {r["anchor"]: r["status"] for r in rows if r["anchor"]}
    feats = prop["feature"]
    listed = [dict(f, print=feature_text(f, status.get(f["anchor"], "print"))) for f in feats if f["listed"]]
    by, problems = assign_by(effective_trades(e), listed, opening_texts([dict(f, print=feature_text(f, status.get(f["anchor"], "print"))) for f in feats], prop.get("opening", [])))
    if problems:
        raise ValueError("; ".join(problems))
    probe = {namekey(f["head"]) for f in feats}
    opening, _ = parse_import(e.body, probe)
    parts = ["\n".join(b) for b in opening]
    for f in feats:
        parts.append(f"## {f['head']} {{#{f['anchor']}}}")
        text = feature_text(f, status.get(f["anchor"], "print"))
        parts += [p for p in text.split("\n\n") if p.strip()]
    front = edit_front(e.front, feats, by, len(trades_of(e)))
    for (eid, old), new in TRADE_RENAMES.items():
        if eid == e.id:
            front = front.replace(f'"{old}"', f'"{new}"', 1)
    return "+++\n" + front + "\n+++\n\n" + "\n\n".join(parts) + "\n"


def stale_rows(e: Entry, rows: list[dict]) -> list[str]:
    """The rows whose import span changed since the compare (the entry was edited in between)."""
    probe = {namekey(r["feature"]) for r in rows if r["feature"]}
    _, feats = parse_import(e.body, probe)
    spans: dict[str, set[str]] = {}
    for f in feats:
        spans.setdefault(namekey(f.name), set()).add(f.span_sha())
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
        raise SystemExit("fmt failed:\n" + fmt.stderr[-2000:])
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
    eq(is_scaffold("Bonus Feat"), True, "scaffold singular")
    # front matter edit
    front = 'id = "x"\n\n[fields]\nkind = "archetype"\ntrades = [\n  { replaces = "Bravery", feature = "bravery" },\n  { replaces = "Armor training", feature = "armor-training" },\n]'
    got = edit_front(front, [{"anchor": "a", "level": 2, "listed": True}, {"anchor": "b", "listed": True}], {0: ["a"], 1: []}, 2)
    eq("features = [\n  { anchor = \"a\", level = 2 },\n  { anchor = \"b\" },\n]" in got, True, "features written")
    eq('{ replaces = "Bravery", feature = "bravery", by = ["a"] },' in got, True, "by written")
    eq('{ replaces = "Armor training", feature = "armor-training" },' in got, True, "no by for the opening text")
    for scaffold in ("Bonus Feats", "Weapon and Armor Proficiency", "Companion Type"):
        eq(namekey(scaffold) in SCAFFOLD, True, f"scaffold {scaffold}")
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
    ap.add_argument("--checker")
    args = ap.parse_args()
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
            p.name[len("feature-prose-540-"):-len(".tsv")] for p in (corpus / "scripts").glob("feature-prose-540-*.tsv"))
        status = 0
        for b in books:
            args.book = b
            status |= run_check(args)
        return status
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
