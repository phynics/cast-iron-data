#!/usr/bin/env python3
"""Class options as printed prose (phynics/cast-iron#540, the class-options phase).

A companion of `feature-prose-540.py`, which it loads as a library: the print reader (`read_blocks`, `compare_entry`, `print_md`,
the OCR and layout switches of a book) is the one of the archetype pass, so the two never read print differently. The archetype
rules of #540 (rulings 1 to 58) apply to class options as far as they fit; what is new is the shape of the entry.

Shapes (owner rulings of 2026-11-24 on the data plan)
-----------------------------------------------------
- **single** (1,597 entries): one power whose name repeats the entry title. The converted body is the printed paragraphs, with no
  head that repeats the title and no `features` (ruling Q1).
- **multi** (about 465): several powers, 360 of them under section headings ("### Revelations"). Each power becomes a head one level
  below its section heading (`####`), or `##` with no section, with an explicit `{#anchor}`; the entry gets `features`, in print order,
  with a `level` only when print gives it (the archetype rule, Q4). The blocks that are no power (Deities, Bonus Spells, ...) stay.
- **none** (705 entries): no import row. They are out of the rewrite; `--compare` and `--check` only report them (ruling Q2).

An entry converts all or nothing, and a converted entry has no import row left, which is also what takes it out of the scope of
`rewrite-class-option-powers.py --check` (its resolutions and exceptions are then `retired`).

Files (per book, in `scripts/class-options/`, which the archetype scripts' `scripts/feature-prose-540-*` glob does not reach)
-------------------------------------------------------------------------------------------------------------------------
`540-<book>.tsv`
    One row per power (the ledger): entry, feature, anchor, shape, section, book, page, level_import, level, by, ability_tag, verdict,
    reviewed_537, status, links_lost, print_sha256, span_sha256, note. `verdict`: `agree` (the rule draft equals print), `differ` (wording
    only), `hold`, `missing-head`, `nopage`, `nobook`; `reviewed_537` is `yes` when a resolution of #537 reaches the power (the verdict stays
    the print compare's). `status`: `draft` or `print` (settled), `hold`, `written` (settled and written into the entry; the row stays, and
    `--check` reads the entry against it). `ability_tag` is the printed (Ex)/(Su)/(Sp) of a single-power option (ruling 63).
`540-<book>.proposals.toml`
    The printed text of each power, written ones included (a TSV cannot hold it).
`540-<book>.decisions.tsv`
    entry, anchor, decision, note. `print` settles a held power as print has it (an errata check done, an owner ruling); a hold settles by a
    row here, not by a change of the script.

What holds an entry (every power of it): import rows outside the powers (Details, Spells, Gained class skills: not transcribed from print
yet), a trade row (Replaces/Alters), an anchor that collides, a single power whose name is not the title.

Usage
-----
    feature-prose-540-class-options.py --self-test
    feature-prose-540-class-options.py [CORPUS] --compare --book ID [--families a,b] [--books DIR --cache DIR]
    feature-prose-540-class-options.py [CORPUS] --write --book ID [--families a,b] [--checker BIN]   writes, marks `written`, runs `fmt`
    feature-prose-540-class-options.py [CORPUS] --check [--book ID]      no PDF needed; exit 1 on a stale row, a settled entry that is not
                                                                         written, a written entry that holds an import label or lacks its text
    feature-prose-540-class-options.py [CORPUS] --headings --book ID ...  ruling 61 for the evolutions that are written
    feature-prose-540-class-options.py [CORPUS] --neighbours --book ID ...  before a book batch: the printed titles and heads each multi-power window holds that are not its own, and whether it ends
    feature-prose-540-class-options.py [CORPUS] --compare ... --variants   ruling 65: settle variant sections (held by default)
    feature-prose-540-class-options.py [CORPUS] --ability-type --book ID  ruling 63: off until the app reads `ability_type`
"""

from __future__ import annotations

import argparse
import csv
import dataclasses
import difflib
import hashlib
import importlib.util
import re
import sys
import tempfile
import tomllib
import unicodedata
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


fp = _load("feature_prose_540", "feature-prose-540.py")
rw = _load("rewrite_class_option_powers", "rewrite-class-option-powers.py")
fp.LOOSE_ITEMS["on"] = True      # ruling 60: the loose reading of a prerequisite item (every word, any order, a sentence with "must" or "only available")
fp.IMPORT_HEAD_FIXES[("ref/vigtalent/expose-weaknesses", "Expose Weaknesses (Ex)")] = "Expose Weakness (Ex)"  # print p. 14; the entry title agrees with print
fp.IMPORT_HEAD_FIXES[("ref/vigtalent/environmental-weapon", "Environmental Weapon (Ex)")] = "Environment Weapon (Ex)"  # print p. 14; the import head has an extra syllable

HEADER = ["entry", "feature", "anchor", "shape", "section", "book", "page", "level_import", "level", "by", "ability_tag", "verdict",
          "reviewed_537", "status", "links_lost", "print_sha256", "span_sha256", "note"]
SETTLED = ("draft", "print")              # settled, not written yet
LEDGER = "written"                        # settled and written into the entry: the row stays, the check reads the entry against it
DIR = "class-options"                     # `scripts/class-options/`: the archetype scripts glob `scripts/feature-prose-540-*`, so these files stay out of it


def tsv_file(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / DIR / f"540-{book}.tsv"


def proposals_file(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / DIR / f"540-{book}.proposals.toml"


def decisions_file(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / DIR / f"540-{book}.decisions.tsv"


DECISION_HEADER = ["entry", "anchor", "decision", "note"]


def read_decisions(path: Path) -> dict[tuple[str, str], tuple[str, str]]:
    """The decisions of a book: (entry, anchor) -> (decision, note). `print` settles a held power as print has it (an errata check done, an
    owner ruling); anything else is read as a hold. A hold settles by a row here, not by a change of the script."""
    if not path.exists():
        return {}
    lines = path.read_text(encoding="utf-8").split("\n")
    assert lines[0].split("\t") == DECISION_HEADER, f"{path}: header is not {DECISION_HEADER}"
    out = {}
    for ln in lines[1:]:
        if ln.strip():
            r = dict(zip(DECISION_HEADER, ln.split("\t")))
            out[(r["entry"], r["anchor"])] = (r["decision"], r.get("note", ""))
    return out


# ---- the entries ---------------------------------------------------------------------------------

def load_entries(corpus: Path, kind: str = "class_option", book: str | None = None, families: set[str] | None = None) -> list:
    """The entries of a kind (the archetype `Entry` type), in id order, whose first source is `book`. `class_option` is the pilot's kind;
    `class` (the base classes: heads and anchors exist already) and `none` (the 33 rule entries, `[fields] kind = "none"`) take the same
    loader, with their own power extractor (`power_records`)."""
    out = []
    for path in sorted((corpus / "entries").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if f'kind = "{kind}"' not in text[:4000]:
            continue
        front, body = fp.split_entry(text)
        data = tomllib.loads(front)
        if (data.get("fields") or {}).get("kind") != kind:
            continue
        sources = data.get("sources") or []
        first = sources[0]["publication"] if sources else (data.get("source_ids") or [None])[0]
        if book and first != book:
            continue
        if families and data["id"].split("/")[1] not in families:
            continue
        page = str(sources[0].get("page", "")) if sources else ""
        out.append(fp.Entry(path, data["id"], data["title"], kind, front, body, data, first, page, []))
    return out


def load_class_options(corpus: Path, book: str | None = None, families: set[str] | None = None) -> list:
    return load_entries(corpus, "class_option", book, families)


@dataclass
class Power:
    """One power of an entry, whatever the kind: where it is in the body, what it is called, and where print has it."""
    name: str
    span_sha: str                  # hash of its span in the body (the key of the ledger)
    anchor: str                    # the URL key: derived from the name, or the explicit one of an existing head
    head_level: int = 0            # 0: no head yet (an import name); else the number of # of its head
    section: str = ""              # the section heading above it
    book: str = ""                 # the publication that prints it (the first source unless the entry cites a second)
    page: str = ""


def power_records(e, kind: str = "class_option") -> list[Power]:
    """The powers of an entry as records, with one extractor per kind: `class_option` the bold names over import rows (the candidates of
    the rewrite script), `class` the `####` heads that exist already (their explicit anchors are kept), `none` (a rule entry) is a copy of
    the converted parent and has none of its own."""
    blocks = rw.parse_blocks(e.body.split("\n"))
    if kind == "class_option":
        return [Power(re.sub(r":$", "", c.name), rw.span_sha(blocks[c.start:c.end]), fp.anchor_of(c.name), 0, section_of(blocks, c.start), e.book or "", e.page)
                for c in rw.candidates(blocks, True)]
    if kind == "class":
        out = []
        for i, b in enumerate(blocks):
            m = re.match(r"^(#{3,6})\s+(.*?)(?:\s*\{#([^}]+)\})?\s*$", b.text)
            if m and len(m.group(1)) == 4:
                end = next((j for j in range(i + 1, len(blocks)) if blocks[j].kind == "boundary" and blocks[j].text.startswith("#")), len(blocks))
                out.append(Power(m.group(2), rw.span_sha(blocks[i:end]), m.group(3) or fp.slugify(fp.ABILITY_TAG.sub("", m.group(2))), 4,
                                 section_of(blocks, i, 4), e.book or "", e.page))
        return out
    return []


def shape_of(body: str) -> tuple[str, int]:
    """(shape, powers): `none` when the body holds no import row, `single` for one power, `multi` for several."""
    lines = body.split("\n")
    if not rw.entry_in_scope(lines):
        return "none", 0
    n = len(rw.candidates(rw.parse_blocks(lines), True))
    return ("single" if n == 1 else "multi"), n


def census(entries: list) -> dict:
    """The counts that `--check` and `--compare` report for a set of entries (the 705 are only reported)."""
    shapes = Counter(shape_of(e.body)[0] for e in entries)
    none_by_family = Counter(e.id.split("/")[1] for e in entries if shape_of(e.body)[0] == "none")
    return {"single": shapes["single"], "multi": shapes["multi"], "none": shapes["none"], "none_by_family": none_by_family}


# ---- the comparison ------------------------------------------------------------------------------

def level_of(text: str) -> int | None:
    return fp.lead_level(text.split("\n\n", 1)[0]) if text else None


EXTRA_NAMES: list[str] = []          # the names of every class option of the book: an italic head of a neighbour ends a power's text


INVERTED_HEAD = re.compile(r"^(.+?),\s*(Lesser|Greater|Improved|Mass|Arcing|Clinging|Thunderous)(\s*\([A-Za-z]{2}\))?\s*:?$")
INVERTED_SUFFIX_VARIANTS = {"Arcing", "Clinging", "Thunderous"}


VARIANT_FIRST = re.compile(r"^(Lesser|Greater|Improved|Mass) ")


def inverted(name: str) -> str:
    m = re.match(r"^(Lesser|Greater|Improved|Mass|Arcing|Clinging|Thunderous) (.+?)(\s*\([A-Za-z]{2}\))?$", name)
    return f"{m.group(2)}, {m.group(1)}{m.group(3) or ''}" if m else name


TABLE_TITLE = re.compile(r"^table\b", re.I)


def title_as_head(q):
    """A printed section heading stands as a head of its own (it ends the power above it); the title of a table is the text of the power
    that holds the table (ruling 62: the span runs over tables and lists up to the next name or heading), so it stays a paragraph."""
    if q.kind != "title":
        return q
    if TABLE_TITLE.match(q.plain().strip()):
        return fp.Para("para", [(q.plain().strip(), False, False)], q.page, q.col, 0)
    return fp.Para("para", [(q.plain().strip(), True, False)], q.page, q.col, 0)


# the bold header of a class table that print sets in the middle of the text ("Spells per Day", "1st 2nd 3rd 4th", "Extracts per Day"): no feature head
TABLE_HEAD_RE = re.compile(r"^(?:(?:0\s+)?\d+(?:st|nd|rd|th)(?:\s+\d+(?:st|nd|rd|th))+\s*|(?:spells|extracts|formulae|powers)(?: known| per day|\s+per\s+\w+)\s*)$", re.I)
TABLE_HEADS: set[str] = set()          # squash of the header row of each table of the entry that is compared


def table_head_as_text(q):
    """The bold header row of a table that the corpus has ("Disguise Time") is no head of a feature: it stays text with its rows (ruling 62)."""
    if q.kind == "para" and (fp.squash(q.plain()) in TABLE_HEADS or TABLE_HEAD_RE.match(q.plain().strip())):
        return fp.Para("para", [(q.plain(), False, False)], q.page, q.col, 0)
    return q


def install_split(names: list[str], book: str = "") -> None:
    """The print reader takes an italic paragraph start as a head only when the entry expects that name. A page of class options sets
    the powers of other entries beside the entry's own (the evolutions are italic heads in one list), so every name of the book is
    expected, and a power's text ends at the next power of the page."""
    names = [print_match_title(book, f"ref/talent/{fp.anchor_of(name)}", name) for name in names]
    EXTRA_NAMES[:] = list(names) + [inverted(n) for n in names if VARIANT_FIRST.match(n) or n.split(" ", 1)[0] in INVERTED_SUFFIX_VARIANTS]  # print can place a variant after its base name
    if not getattr(fp.split_print, "_class_options", False):
        orig = fp.split_print

        def wrapped(section, expected):
            # a printed section heading ("2-Point Evolutions", "Base Forms") ends the text of the power above it: it stands as a head of its own
            section = section[:1] + [table_head_as_text(title_as_head(q)) for q in section[1:]]
            opening, feats = orig(section, list(expected) + EXTRA_NAMES)
            for f in feats:                      # print sets "Beast Totem, Greater (Su)" for the corpus title "Greater Beast Totem"
                m = INVERTED_HEAD.match(f.head)
                if m:
                    f.head = f"{m.group(2)} {m.group(1)}{m.group(3) or ''}"
            return opening, feats
        wrapped._class_options = True
        fp.split_print = wrapped


def reviewed_spans(corpus: Path) -> dict[tuple[str, str], str]:
    """The 423 hand replacements of #537 as (entry id, span hash) -> print reference: print-reviewed text in row form. A power whose
    current span still hashes to a resolution's `span_sha256` has a reviewed source; its verdict is `reviewed-537`, and the wording is
    print's (a resolution never overrides the print compare)."""
    out: dict[tuple[str, str], str] = {}
    for r in rw.load_resolutions(corpus / rw.RESOLUTIONS_FILE).values():
        out[(r.id, r.span_sha256)] = r.print                                                    # the span as the import had it
        out[(r.id, hashlib.sha256(rw.resolution_power_text(r).encode()).hexdigest())] = r.print   # the span once the resolution is applied (the corpus today)
    return out


REVIEWED: dict[tuple[str, str], str] = {}


def powers_of(e) -> list[tuple[str, str]]:
    """The powers of an entry as (name, span hash): the candidates of `rewrite-class-option-powers.py` (a bold name that stands over
    import rows), in body order, with its hash of the span. A bold name over other rows (Deities, Bonus Spells) is no power."""
    blocks = rw.parse_blocks(e.body.split("\n"))
    return [(re.sub(r":$", "", c.name), rw.span_sha(blocks[c.start:c.end])) for c in rw.candidates(blocks, True)]


TAG = re.compile(r"\(([^()]*)\)\s*:?$")
TAG_WORDS = re.compile(r"(?:Ex|Su|Sp)(?:(?:, or |, and |, | or | and )(?:Ex|Su|Sp))*")      # the rule of `is_ability_tag_text` (schema), as the heading splitter reads a tag
TRADE_LABEL = re.compile(r"^\*\*(?:Replaces?|Alters?|Modifies):\*\*", re.M)
LABEL_ROW = re.compile(r"^\*\*([^*\n]+):\*\*", re.M)           # an import row: a bold label with its colon
WRITE_ABILITY_TYPE = True                                    # ruling 63: `[fields] ability_type`; on since the app reads the key (app #749)


def ability_tag_of(name: str) -> str:
    """Read a final ability tag only when its words match the app's closed tag grammar."""
    m = TAG.search(name)
    return m.group(1) if m and TAG_WORDS.fullmatch(m.group(1)) else ""


def ability_tag_of_printed_head(head: str) -> str:
    """Read the tag from print's head, allowing source marks around the tag without deleting the tag itself."""
    clean = re.sub(r"[\*†‡]+\s*$", "", head).strip()
    clean = re.sub(r"[\*†‡]+\s*(?=\([^()]+\)\s*$)", "", clean).strip()
    return ability_tag_of(clean)


def ability_tag_for_option(book: str, imported_head: str, printed_head: str) -> tuple[str, bool]:
    """Read tags from print in the audited books; retain the established matcher elsewhere."""
    if book in {"ultimate-combat", "ultimate-intrigue", "core-rulebook", "pathfinder-unchained"}:
        imported, printed = ability_tag_of(imported_head), ability_tag_of_printed_head(printed_head)
        return printed, bool(imported and printed and imported != printed)
    return ability_tag_pair(imported_head, printed_head)


INTRO_MARK_SPECS = {
    "ultimate-magic": {"discovery": ("Discoveries that modify bombs and are marked with a single asterisk", "stack")},
    "advanced-class-guide": {
        "invtalent": ("Investigator talents marked with an asterisk", "damage is dealt"),
    },
    "ultimate-combat": {
        "discovery": ("Discoveries that modify bombs and are marked with a single asterisk", "stack"),
        "talent": ("Talents marked with an asterisk", "sneak attack"),
        "ninjatrick": ("Tricks marked with an asterisk", "sneak attack"),
    },
    "ultimate-intrigue": {
        "vigtalent": ("marked with an asterisk", "hidden strike"),
    },
    "core-rulebook": {
        "talent": ("Talents marked with an asterisk", "sneak attack"),
    },
    "pathfinder-unchained": {
        "talent": ("Talents marked with an asterisk", "sneak attack"),
    },
}
INTRO_MARK_TEXT: dict[tuple[str, str], tuple[str, int]] = {}
MARKED_HEAD_ENTRIES: set[str] = set()
INTRO_MARK = {"by": {}}
BLOOD_PREREQUISITE_INTROS = {
    "middle": "The middle blood rage power (that without “lesser” or “greater” in the title) can only be taken by a 6th level or higher barbarian that already has the lesser blood rage power of its group.",
    "greater": "A greater blood rage power can only be taken by a 10th level or higher barbarian that already has the middle blood rage power.",
}


def marked_head_intro(book: str, entry_id: str) -> str:
    """The printed intro sentence for a marked head, read from its book during --compare."""
    text, _ = INTRO_MARK_TEXT.get((book, entry_id.split("/")[1]), INTRO_MARK.get("by", {}).get(entry_id.split("/")[1], ("", 0)))
    text = text.replace("(*)", r"(\*)")
    return text.replace("’", "'") if book == "ultimate-intrigue" else text


def marked_head_page(book: str, entry_id: str) -> int:
    return INTRO_MARK_TEXT.get((book, entry_id.split("/")[1]), INTRO_MARK.get("by", {}).get(entry_id.split("/")[1], ("", 0)))[1]


def prepend_intro(body: str, intro: str) -> str:
    """Replace an old marked-head intro or add the printed one once, preserving literal stars as text."""
    if not intro:
        return body
    if body.startswith(intro):
        body = body[len(intro):].lstrip("\n")
        return intro + "\n\n" + body
    legacy = intro.replace(r"\*", "*")
    if legacy != intro and body.startswith(legacy):
        body = body[len(legacy):].lstrip("\n")
    elif body:
        first, sep, rest = body.partition("\n\n")
        if "marked with" in first and "asterisk" in first:
            body = rest if sep else ""
    return intro + "\n\n" + body.lstrip("\n")


def drop_marked_intro(body: str) -> str:
    first, sep, rest = body.partition("\n\n")
    if "marked with" in first and "asterisk" in first:
        return rest if sep else ""
    return body


def drop_unkeyed_link_marks(entry_id: str, body: str) -> str:
    """Ultimate Combat p. 27 prints doubled cross-reference marks with no key on the page."""
    if entry_id == "ref/ragepower/greater-ground-breaker":
        return body.replace("[ground breaker](ref/ragepower/ground-breaker)\\*\\*", "[ground breaker](ref/ragepower/ground-breaker)")
    if entry_id == "ref/ragepower/greater-guarded-life":
        return body.replace("[guarded life](ref/ragepower/guarded-life)\\*\\*", "[guarded life](ref/ragepower/guarded-life)")
    return body
def ability_tag_pair(import_name: str, print_head: str) -> tuple[str, bool]:
    """Ruling 63: the ability tag is print's. The printed head often carries it when the import's name does not ("Blinding Bomb (Su)" against
    "Blinding Bomb", Ultimate Magic p. 15); a tag that both state must agree, or the power holds."""
    itag = ability_tag_of(import_name)
    ptag = ability_tag_of(print_head or "")
    return (ptag or itag), bool(itag and ptag and itag != ptag)


def with_ability_type(front: str, tag: str) -> str:
    """Synchronize `[fields] ability_type` with the printed tag; a blank tag removes a stale key (ruling 63)."""
    if 'kind = "class_option"' not in front:
        return front
    if not tag:
        without = re.sub(r"^ability_type = [^\n]*\n?", "", front, flags=re.M)
        return re.sub(r"\n{2,}$", "\n", without)
    if not TAG_WORDS.fullmatch(tag) or re.search(r"^ability_type = ", front, re.M):
        return front
    out, n = re.subn(r'(^group = "[^"]*")(\n|\Z)', lambda m: m.group(1) + f'\nability_type = "{tag}"\n', front, count=1, flags=re.M)
    assert n == 1, "a class option has a `group` row to put the key after"
    return out


def outside_rows(body: str) -> list[str]:
    """The labels of the import rows that stand outside every power (Details, Spells, Gained class skills, ...): a power rewrite does not
    reach them, and they would stay in a converted entry (no transcription from print yet)."""
    blocks = rw.parse_blocks(body.split("\n"))
    inside = {i for c in rw.candidates(blocks, True) for i in range(c.start, c.end)}
    return sorted({b.label for i, b in enumerate(blocks) if b.kind == "row" and i not in inside})


def section_of(blocks, start: int, below: int = 7) -> str:
    """The text of the nearest section heading above a block ("" before the first); with `below`, the nearest of a level above that."""
    for i in range(start - 1, -1, -1):
        if blocks[i].kind == "boundary" and blocks[i].text.startswith("#") and len(blocks[i].text) - len(blocks[i].text.lstrip("#")) < below:
            return blocks[i].text.lstrip("#").strip()
    return ""


def promoted(blocks, cands) -> dict[int, tuple[int, str]]:
    """A power whose name is the heading right above it (`### Final Revelation` over `**Final Revelation**`): the heading becomes the head
    of the power and keeps its derived key, written out (`{#sec-final-revelation}`), so that its URL does not move (rule 3 of AGENTS.md).
    Maps the block index of the heading to (its level, the key)."""
    out = {}
    for c in cands:
        i = c.start - 1
        if i >= 0 and blocks[i].kind == "boundary" and blocks[i].text.startswith("#"):
            head = blocks[i].text.lstrip("#").strip()
            if fp.slugify(head) == fp.slugify(fp.ABILITY_TAG.sub("", re.sub(r":$", "", c.name))):
                out[i] = (len(blocks[i].text) - len(blocks[i].text.lstrip("#")), "sec-" + fp.slugify(head))
    return out


def prereq_links(body: str) -> list[tuple[str, str]]:
    m = re.search(r"^\*\*Prereq(?:uisites?)?:\*\*(.*)$", body, re.M)
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", m.group(1)) if m else []


def place_links(text: str, links: list[tuple[str, str]]) -> tuple[str, list[str]]:
    """Ruling 60: the item of a `Prereq` row is a link in print's prerequisite sentence ("must possess the [claws](ref/evolution/claws)
    evolution to select this evolution"), whether or not the text links it earlier. The sentence is the one that has a prerequisite frame;
    with none, the first plain occurrence outside a link. The items found nowhere are returned (the `links_lost` column)."""
    lost = []
    for name, target in links:
        spans = [m.span() for m in re.finditer(r"\[[^\]]*\]\([^)]*\)", text)]
        word = re.compile(r"(?<![\w\[])" + re.escape(name) + r"(?![\w\]])", re.I)
        plain = [m for m in word.finditer(text) if not any(a <= m.start() < b for a, b in spans)]
        sentences = [m.span() for m in fp.ITEM_SENTENCE.finditer(text) if fp.ITEM_FRAME.search(m.group(0))]
        in_frame = [m for m in plain if any(a <= m.start() < b for a, b in sentences)]
        linked_in_frame = any(f"]({target})" in text[a:b] for a, b in sentences)       # the prerequisite sentence links the item already
        hit = None if linked_in_frame else (in_frame or plain or [None])[0]
        if hit:
            text = text[:hit.start()] + f"[{hit.group(0)}]({target})" + text[hit.end():]
        elif not linked_in_frame and not any(f"]({target})" in text[a:b] for a, b in spans):
            lost.append(name)
        # every plain "<item> evolution" (rage power, hex) is the same link, as it is where the text names the option again
        # ("an equal number of the tail evolution")
        again = re.compile(r"(?<![\w\[])(" + re.escape(name) + r")(?=\s+(?:evolutions?|rage powers?|hex(?:es)?)\b)", re.I)
        for m in reversed(list(again.finditer(text))):
            spans = [x.span() for x in re.finditer(r"\[[^\]]*\]\([^)]*\)", text)]
            if not any(a_ <= m.start() < b_ for a_, b_ in spans):
                text = text[:m.start()] + f"[{m.group(1)}]({target})" + text[m.end():]
    return text, lost


def link_intrigue_class_prerequisites(text: str) -> str:
    """Link printed vigilante and specialization prerequisites to their class entries."""
    out = []
    for match in re.finditer(r"[^.!?]*[.!?]?", text):
        sentence = match.group(0)
        if re.search(r"\bonly an? stalker vigilante\b", sentence, re.I) and re.search(r"\bcan select this talent\b", sentence, re.I):
            sentence = re.sub(r"\bstalker vigilante\b", "[stalker vigilante](ref/class/vigilante#stalker)", sentence, count=1, flags=re.I)
        elif re.search(r"\bonly an? avenger vigilante\b", sentence, re.I) and re.search(r"\bcan select this talent\b", sentence, re.I):
            sentence = re.sub(r"\bavenger vigilante\b", "[avenger vigilante](ref/class/vigilante#avenger)", sentence, count=1, flags=re.I)
        elif re.search(r"\ba vigilante must\b", sentence, re.I):
            sentence = re.sub(r"\bvigilante\b", "[vigilante](ref/class/vigilante)", sentence, count=1, flags=re.I)
        out.append(sentence)
    return "".join(out)


def repair_intrigue_italic_link_boundary(text: str) -> str:
    """Repair the two empty emphasis artifacts left at linked italic commas in this book."""
    text = re.sub(r"(\]\([^)]*\))_, __ (a caster level check)", r"\1,_ \2", text)
    return re.sub(r"(\]\([^)]*\))_, __ (and he can say it)", r"\1_, \2", text)
CROSS_GROUP = re.compile(r"\[([^\]]*)\]\((ref/[^)]+)\)")
CORPUS_ROOT: Path | None = None          # the tree the entry files are read from (the target group of a printed item, ruling 52)
GROUP_OF_TARGET: dict[str, tuple[str, str] | None] = {}


def target_kind_group(target: str) -> tuple[str, str] | None:
    """The kind and group in the front matter of the entry a link points at, or None when the tree has no such entry."""
    if target in GROUP_OF_TARGET:
        return GROUP_OF_TARGET[target]
    out = None
    if CORPUS_ROOT is not None:
        path = Path(CORPUS_ROOT) / "entries" / (target[4:] + ".md")
        if path.exists():
            head = path.read_text(encoding="utf-8").split("\n+++\n", 1)[0]
            kind = re.search(r'^kind = "([^"]*)"', head, re.M)
            group = re.search(r'^group = "([^"]*)"', head, re.M)
            out = (kind.group(1) if kind else "", group.group(1) if group else "")
    GROUP_OF_TARGET[target] = out
    return out


OPTION_NOUNS = {
    "deed": "deed", "deeds": "deed", "hex": "hex", "hexes": "hex", "talent": "talent", "talents": "talent",
    "arcana": "arcana", "exploit": "exploit", "exploits": "exploit", "discovery": "discovery", "discoveries": "discovery",
    "power": "power", "powers": "power", "mystery": "mystery", "mysteries": "mystery", "bloodline": "bloodline",
    "bloodlines": "bloodline", "order": "order", "orders": "order", "spirit": "spirit", "spirits": "spirit",
    "judgment": "judgment", "judgments": "judgment", "evolution": "evolution", "evolutions": "evolution",
    "domain": "domain", "domains": "domain", "blessing": "blessing", "blessings": "blessing",
    "inquisition": "inquisition", "inquisitions": "inquisition", "revelation": "revelation", "revelations": "revelation",
    "curse": "curse", "curses": "curse", "patron": "patron", "patrons": "patron", "school": "school", "schools": "school",
    "focus": "focus", "foci": "focus", "discipline": "discipline", "disciplines": "discipline",
    "implement": "implement", "implements": "implement", "aspect": "aspect", "aspects": "aspect",
}


LINK_OR_WORD = re.compile(r"\[[^\]]*\]\([^)]*\)|\band\b|\bor\b|[A-Za-z][A-Za-z'-]*|[,;]")


def link_kind_mismatches(text: str) -> list[tuple[str, str, str, str]]:
    """Ruling 52, as narrowed by the review of #373: a printed reference may name another class's option on purpose (the two
    swashbuckler deeds that Flamboyant Arcana grants, the investigator talents the cognatogens name, the witch's cackle), so a link
    is checked only for a disagreement with print's own words. Print's noun for the name is the option noun that follows it, across
    a printed list ("the amazing inspiration, eidetic recollection, and expanded inspiration investigator talents") and at most one
    class word ("investigator talents"); any other word between the name and a noun means print attaches no such noun, and the link
    stays. A class print names must be the target's class. The names that agree with print stay linked."""
    bad: list[tuple[str, str, str, str]] = []
    classes = {c.casefold() for c in fp.CLASS_NAMES}
    for m in CROSS_GROUP.finditer(text):
        name, target = m.group(1), m.group(2)
        pair = target_kind_group(target)
        if not pair:
            continue
        a = text.rfind(". ", 0, m.start())
        b = text.find(". ", m.end())
        sent = text[a + 2 if a >= 0 else 0: b + 1 if b >= 0 else len(text)]
        link = f"]({target})"
        at = sent.find(link)
        after = sent[at + len(link):] if at >= 0 else ""
        noun = None
        seen_class = False
        for t in LINK_OR_WORD.finditer(after):
            word = t.group(0)
            if word.startswith("["):
                continue                                     # another name of the same printed list
            if word in (",", ";") or word.casefold() in ("and", "or"):
                continue
            low = word.casefold()
            if low in OPTION_NOUNS:
                noun = OPTION_NOUNS[low]
                break
            if low in classes and not seen_class:
                seen_class = True
                continue
            break                                            # print says something else here: no noun of this kind
        if noun and (pair[0] != "class_option" or not pair[1] or noun != pair[1].rsplit("-", 1)[-1]):
            bad.append((name, target, pair[1] or pair[0], noun))
            continue
        if pair[0] == "class_option" and pair[1]:
            # A class name elsewhere in the sentence does not govern this link. Use its local clause.
            left = max(sent.rfind(";", 0, at), sent.rfind(":", 0, at), sent.rfind(", but", 0, at), sent.rfind(", while", 0, at))
            right_candidates = [x for x in (sent.find(";", at), sent.find(":", at), sent.find(", but", at), sent.find(", while", at)) if x >= 0]
            clause = sent[left + 1:min(right_candidates) if right_candidates else len(sent)]
            prefix = pair[1].split("-")[0]
            mentioned = {w for w in classes if re.search(r"\b" + re.escape(w) + r"\b", clause, re.I)}
            if prefix in classes and mentioned and prefix not in mentioned:
                bad.append((name, target, pair[1], "class " + prefix))
    return bad


def option_link_kind_mismatches(book: str, text: str) -> list[tuple[str, str, str, str]]:
    """Run the option-link check for books whose class-option prose has been reviewed for it."""
    return link_kind_mismatches(text) if book in {"advanced-class-guide", "core-rulebook", "pathfinder-unchained"} else []


def printed_claim_key(row: dict[str, str]) -> tuple[str, str, str, str]:
    """A Pathfinder Unchained option is claimed only against the same printed page, not a repeated eidolon entry."""
    page = row["page"] if row["book"] == "pathfinder-unchained" else ""
    return row["book"], page, fp.namekey(row["feature"]), row["print_sha256"]


def print_match_title(book: str, entry_id: str, title: str) -> str:
    """Drop the Unchained Rogue catalog suffix when matching its printed talent head."""
    if book == "pathfinder-unchained" and entry_id.startswith("ref/talent/"):
        return re.sub(r"\s*\(Unchained Rogue\)(?=\s*\((?:Ex|Su|Sp)\)$|$)", "", title)
    return title


def print_match_body(book: str, entry_id: str, body: str) -> str:
    """Normalize the Unchained Rogue title suffix on imported power labels for print matching."""
    if book == "pathfinder-unchained" and entry_id.startswith("ref/talent/"):
        return body.replace(" (Unchained Rogue)", "")
    return body


def pathfinder_unchained_links(entry_id: str, text: str) -> str:
    """Link references to the book's own Grab evolution instead of the monster-rule ability."""
    if entry_id in {"ref/unchevolution/constrict", "ref/unchevolution/swallow-whole"}:
        text = re.sub(r"\[grab\]\(ref/(?:carried/bestiary/rules/universal-monster-rules/)?grab\)",
                      "[grab](ref/unchevolution/grab)", text, flags=re.I)
    return text


HARD_HOLD_NOTE_PREFIXES = (
    "anchor collision:",
    "the power's name differs from the title of the entry",
    "print text may be cut at a page or column break:",
    "print sentences that the written text lacks (",
    "the second-source window has no end title:",
    "ruling 52:",
    "no group heading found above the head",
    "the group heading is on p.",
)


def print_decision_may_settle(notes_tag: list[str], problems: list[str], row: dict) -> bool:
    """A reviewed print decision may settle a tag disagreement only when the row has no independent hard hold."""
    hard = any(note.startswith(HARD_HOLD_NOTE_PREFIXES) for note in row.get("notes", []))
    return bool(notes_tag) and not problems and not hard


STOP_TITLES: set[str] = set()          # squash of the title of every class option: another one ends a section


SUFFIXES = ("", "bloodline", "mystery", "school")
# The words that a printed neighbour can carry after the name of an option ("Earth", "Earth School", "Earth Bloodline"). A group with another
# printed suffix ("Domain", "Order", "Patron", ...) needs it added here before its batch: until then its window does not end at that neighbour
# (the entry holds, "no end title", or the neighbour shows in `--neighbours`), which is safe but not settled.


def group_kind(e) -> str:
    """The kind word of the entry's group ("arcane-school" is a school, "druid-domain" a domain): a printed title may carry it in a
    parenthesis after the entry's name ("METAL (ELEMENTAL SCHOOL)")."""
    group = str((((getattr(e, "data", {}) or {}).get("fields") or {}).get("group") or ""))
    return group.split("-")[-1] if group else ""


def single_name_matches_title(entry_id: str, title: str, name: str) -> bool:
    imported = fp.import_name(entry_id, name)
    imported = print_match_title("pathfinder-unchained", entry_id, imported)
    title = print_match_title("pathfinder-unchained", entry_id, title)
    return fp.namekey(imported) == fp.namekey(title) or fp.namekey(inverted(imported)) == fp.namekey(title)


def anchor_section(blocks: list, title: str, own: frozenset | set = frozenset(), kind: str = "") -> tuple[list, bool] | None:
    """The blocks of a multi-power entry from the printed title of the entry to the next title of another class option (or any larger title),
    and whether that end was found: the window is anchored at the title, so a head of a neighbour that follows on the page is not read as the
    entry's power. None when the title is not printed on those pages. A neighbour is a title or a bold head that is another option's name
    (with the same suffixes in both: "Earth", "Earth School", "Earth Bloodline"); the names of the entry's own powers (`own`) are none."""
    key = fp.squash(re.sub(r"\s*\((?:[A-Z]{2,4}|HotW)\)\s*$", "", title))
    # the printed title may carry its type in a parenthesis and in capitals ("METAL (ELEMENTAL SCHOOL)", Ultimate Magic p. 87): the name is
    # what stands before it, and only when the parenthesis names the entry's own kind of option ("SCHOOL" for a school; "FIRE (SUBDOMAIN)"
    # is no title of an entry named Fire)
    def is_own(text: str) -> bool:
        m = re.match(r"^(.*?)\s*\(([^()]*)\)\s*$", text)
        if not m or not kind:
            return False
        words = {w.casefold() for w in re.findall(r"[A-Za-z]+", m.group(2))}
        if kind.casefold() not in words:
            return False
        return fp.squash(m.group(1)) in {key + s for s in SUFFIXES}
    at = next((i for i, b in enumerate(blocks) if b.kind == "title" and (fp.squash(b.plain()) in {key + s for s in SUFFIXES} or is_own(b.plain()))), None)
    if at is None:
        return None
    others = STOP_TITLES - {key} - set(own)
    stops = {o + s for o in others for s in SUFFIXES}
    for j in range(at + 1, len(blocks)):
        b = blocks[j]
        if b.kind == "title" and (fp.squash(b.plain()) in stops or b.size > blocks[at].size):
            return blocks[at + 1:j], True
        head = fp.head_of_para(b) if b.kind == "para" else None             # the next option may be a bold head, not a title ("Earth School")
        if head and fp.squash(head) in stops:
            return blocks[at + 1:j], True
    return blocks[at + 1:], False


HEADING_FAMILIES = {"evolution"}  # ruling 61
INTRO_MARKS_BOOKS = ("ultimate-magic", "advanced-class-guide", "core-rulebook", "pathfinder-unchained")
FAMILY_WORDS = (("investigator", "invtalent"), ("slayer", "slayertalent"), ("rage power", "ragepower"), ("bloodrage", "ragepower"), ("discover", "discovery"), ("hex", "shamanhex"), ("deed", "swashdeed"), ("arcana", "arcana"), ("evolution", "evolution"))
class IntroMarkMap:
    """Resolve marked-head intro sentences from print, by family or explicit rule."""

    def __init__(self, bk, marker=None, prefer=None):
        self.by_family = {}
        self.text, self.page = "", 0
        best = None
        marker_re = re.compile(r"(?<!\w)" + re.escape(marker) + r"(?!\w)", re.I) if marker else None
        for block in fp.read_blocks(bk, 1, max(bk.pages)):
            if block.kind != "para":
                continue
            text = " ".join(block.plain().split())
            sentences = re.split(r"(?<=[.!?])\s+", text)
            if "asterisk" in text.casefold():
                for i, sentence in enumerate(sentences):
                    if "marked with" in sentence.casefold() and "asterisk" in sentence.casefold():
                        family = next((fam for word, fam in FAMILY_WORDS if word in text.casefold()), None)
                        if family and family not in self.by_family:
                            self.by_family[family] = (" ".join(sentences[i:]).strip(), block.page)
                        break
            if marker_re and marker_re.search(text):
                at = next(i for i, sentence in enumerate(sentences) if marker_re.search(sentence))
                candidate = (" ".join(sentences[at:]).strip(), block.page)
                if best is None or (prefer and prefer.casefold() in candidate[0].casefold()):
                    best = candidate
                if prefer and prefer.casefold() in candidate[0].casefold():
                    break
        if best:
            self.text, self.page = best

class GroupMap:
    """Ruling 61, per book: every group heading of the book with its intro sentence ("2-Point Evolutions: The following evolutions cost 2
    points from the eidolon's evolution pool.") and the printed page it stands on, from one read of the whole book. The group of a power is
    the last heading above its head in reading order."""

    def __init__(self, bk):
        self.blocks = fp.read_blocks(bk, 1, max(bk.pages))
        self.headings: list[tuple[int, str, int]] = []                         # (index of the title block, text, printed page)
        for i, b in enumerate(self.blocks[:-1]):
            nxt = self.blocks[i + 1]
            if b.kind == "title" and nxt.kind == "para":
                text, _, _ = fp.print_md(fp.PrintFeature("", [nxt.runs], nxt.page, False), [], set())
                if text.strip().startswith("The following"):
                    self.headings.append((i, f"{re.sub(chr(10), ' ', b.plain()).strip()}: {text.strip()}", b.page))

    def of(self, title: str, page: int) -> tuple[str, int] | None:
        """(the heading paragraph, its page) for the power printed as `title` on the cited page or next to it, or None."""
        want = fp.namekey(title)
        at = next((i for i, p in enumerate(self.blocks) if p.kind == "para" and abs(p.page - page) <= 1
                   and (c := fp.head_candidate(p)) and fp.namekey(c[0]) == want), None)
        if at is None:
            return None
        before = [h for h in self.headings if h[0] < at]
        if not before or self.blocks[at].page - before[-1][2] > 6:
            return None
        return before[-1][1], before[-1][2]


GMAPS: dict[int, GroupMap] = {}


def group_map(bk) -> GroupMap:
    if id(bk) not in GMAPS:
        GMAPS[id(bk)] = GroupMap(bk)
    return GMAPS[id(bk)]


def group_heading(e, blocks) -> tuple[str, int] | None:
    """The group heading of a power from a list of blocks (a window of print): the last title above the head of the entry and the paragraph
    under it when that starts "The following". `GroupMap` is the same for a whole book."""
    want = fp.namekey(e.title)
    at = next((i for i, p in enumerate(blocks) if p.kind == "para" and (c := fp.head_candidate(p)) and fp.namekey(c[0]) == want), None)
    if at is None:
        return None
    ti = next((i for i in range(at - 1, -1, -1) if blocks[i].kind == "title"), None)
    if ti is None or ti + 1 >= at:
        return None
    para = blocks[ti + 1]
    text, _, _ = fp.print_md(fp.PrintFeature("", [para.runs], para.page, False), [], set())
    text = text.strip()
    if not text.startswith("The following"):
        return None
    return f"{re.sub(chr(10), ' ', blocks[ti].plain()).strip()}: {text}", blocks[ti].page


def variant_section(blocks: list, bk2, e, missing: list, expected: list[str]):
    """Ruling 65: the section of another book that prints a variant of the entry under its own title (an elemental bloodline of Advanced
    Player's Guide that Ultimate Magic p. 71 prints as "Envenomed"). The section is the first title of the window whose heads include one of
    the missing powers (a "Replacement Bloodline Arcana" is print's "Bloodline Arcana" there). Returns (title, text, heads, replacement rows)
    or None when the heads stand under the entry's own title. A title that is another option of the corpus is skipped."""
    specific = {fp.namekey(f.name) for f in missing if not f.name.startswith("Replacement ")}      # "Water Blast", not the generic "Bloodline Arcana"
    want = specific or {fp.namekey(re.sub(r"^Replacement\s+", "", f.name)) for f in missing}
    titles = [i for i, b in enumerate(blocks) if b.kind == "title"]
    for n, i in enumerate(titles):
        j = titles[n + 1] if n + 1 < len(titles) else len(blocks)
        op, pfs = fp.split_print([blocks[i]] + blocks[i + 1:j], expected)
        heads = {fp.namekey(fp.head_text(f.head)): f for f in pfs}
        if not set(heads) & want:
            continue
        if fp.squash(blocks[i].plain()) in STOP_TITLES - {fp.squash(e.title)}:
            continue                       # the title of another option of the corpus is no variant of this one
        if fp.squash(blocks[i].plain()) == fp.squash(e.title):
            return None
        parts = fp.join_wrapped([fp.clean_runs(r) for r in op], bk2.vocab)
        for f in pfs:
            text, _, _ = fp.print_md(f, [], bk2.vocab, e.id)
            first, *rest = text.split("\n\n")
            parts += [f"**{fp.head_text(f.head)}:** {first}"] + rest
        title = re.sub(r"\s+", " ", blocks[i].plain()).strip().title()
        replaced = {}
        for f in missing:
            if f.name.startswith("Replacement "):
                pf = heads.get(fp.namekey(re.sub(r"^Replacement\s+", "", f.name)))
                if pf is not None:
                    text, _, _ = fp.print_md(pf, [], bk2.vocab, e.id)
                    cmp = fp.compare_feature(fp.build_draft(f), text, set(fp.tokens(fp.ABILITY_TAG.sub("", f.name))), set())
                    replaced[f.span_sha()] = {"anchor": fp.anchor_of(f.name), "span": f.span_sha(), "status": cmp.status, "notes": list(cmp.notes) + ["print's "
                                              + fp.head_text(pf.head) + " in the variant"], "print": text, "level_import": None, "head": f.name, "name": f.name}
        return title, "\n\n".join(parts), replaced, blocks[i].page, n + 1 < len(titles)       # the last: whether another title ends the section
    return None


MULTI_FENCE = False                  # a multi-power entry holds until its window is anchored at the printed title of the entry (the item-3 PR lifts this)


def fence(rows: list[dict], shape: str) -> list[dict]:
    """Every row of a multi-power entry holds while the fence is up: the window of the cited page and the next three reads another entry's
    head as this entry's power."""
    if MULTI_FENCE and shape == "multi":
        for r in rows:
            r["status"] = "hold"
            r["note"] = (r["note"] + "; " if r["note"] else "") + "multi-power window not anchored yet"
    return rows


def apply_multi_decisions(rows: list[dict], entry_id: str) -> list[dict]:
    """Apply explicit hold decisions after section rows have been added to a multi-power entry."""
    for row in rows:
        decision = DECISIONS.get((entry_id, row.get("anchor", "")))
        if decision and decision[0] == "hold":
            row["status"] = "hold"
            marker = f"held by decision: {decision[1]}"
            if marker not in row.get("note", ""):
                row["note"] = "; ".join(x for x in (row.get("note", ""), marker) if x)
    return rows


def print_decision_resolves(decision, status: str, source_status: str, problems: list[str], hard: bool) -> bool:
    """A print decision resolves a comparison hold only when no independent blocker remains."""
    return bool(decision and decision[0] == "print" and status == "hold" and (source_status in SETTLED or source_status == "hold") and not problems and not hard)


RULE_8_PRINTED_PROGRESSIONS = {
    ("ref/vigtalent/environmental-weapon", "environment-weapon"):
        ("At 5th, 10th, 15th, and 20th levels, the vigilante can select an additional type of terrain.",
         "At and 20th levels, the vigilante can select an additional type of terrain."),
}


def ruling8_progression_decision(book: str, entry_id: str, anchor: str, decision, missing: list[str], print_text: str) -> bool:
    """An explicit ruling-8 decision can settle only the reviewed printed progression sentence."""
    expected = RULE_8_PRINTED_PROGRESSIONS.get((entry_id, anchor))
    return bool(book == "ultimate-intrigue" and expected and decision and decision[0] == "print"
                and "ruling 8" in decision[1].lower() and missing == [expected[1]] and expected[0] in print_text)


def headings_as_names(body: str) -> str:
    """The body with each Markdown heading as a bold name (`### Order Abilities` as `**Order Abilities**`), so that the print comparison reads
    it as a feature of its own."""
    return re.sub(r"(?m)^#{1,6}[ \t]+(.*?)(?:[ \t]*\{#[^}]+\})?[ \t]*$", r"**\1**", body)


TERMINAL = re.compile(r"[.!?:][)\]\"'\u2019\u201d_*]*$")


def paragraph_complete(par: str) -> bool:
    """Completeness guard: a printed paragraph ends in terminal punctuation (`.`, `!`, `?`, `:`, with a closing quote, parenthesis, italic mark
    or link after it), or it is a list item or a table row. A paragraph that stops in the middle of a sentence is a window that ended at a page or
    column break ("... declare a moment of triumph. For 1")."""
    p = " ".join(par.split())
    if not p or p.startswith(("#", "|", "- ", "* ", ">", ":::")) or re.match(r"^\d+[.)] ", p):
        return True
    p = re.sub(r"\]\([^)]*\)$", "]", p)                      # a link at the end: its text is the word
    return bool(TERMINAL.search(p))


def incomplete_paragraph(text: str) -> str:
    """The end of the first paragraph of a printed text that is cut, or "" when every paragraph is complete."""
    for par in text.split("\n\n"):
        if not paragraph_complete(par):
            return " ".join(par.split())[-60:]
    return ""


def corpus_tables(body: str) -> list[list[str]]:
    """The Markdown tables of a body, each as its lines."""
    out, cur = [], []
    for ln in body.split("\n"):
        if ln.startswith("|"):
            cur.append(ln)
        elif cur:
            out.append(cur)
            cur = []
    return out + ([cur] if cur else [])


def adopt_tables(printed: str, body: str) -> tuple[str, int]:
    """Ruling 62: a table inside a class option's own text stays a Markdown table. Print sets its rows as paragraphs ("Disguise Time",
    "Minor details only 1 full-round action"); where those paragraphs are, cell by cell, the rows of a table of the corpus, they are replaced by
    that table. Returns the text and the number of tables adopted."""
    pars = printed.split("\n\n")
    n = 0
    for tab in corpus_tables(body):
        rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in tab if not re.match(r"^\|\s*:?-{3,}", ln)]
        want = [" ".join(" ".join(r).split()) for r in rows]
        norm_pars = [" ".join(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", x).split()) for x in pars]
        at = next((i for i in range(len(pars) - len(want) + 1) if norm_pars[i:i + len(want)] == want), None)
        if at is not None:
            pars[at:at + len(want)] = ["\n".join(tab)]
            n += 1
            continue
        joined = " ".join(want)                                   # the reader may run the rows together as one paragraph
        at = next((i for i, x in enumerate(norm_pars) if joined in x and "](" not in pars[i]), None)       # a paragraph with links is left (they would be lost)
        if at is not None:
            before, _, after = norm_pars[at].partition(joined)
            pars[at:at + 1] = [x for x in (before.strip(), "\n".join(tab), after.strip()) if x]
            n += 1
    return "\n\n".join(pars), n


PAGE_SEARCH: dict = {"blocks": None}
FAMILY_OF_TITLE: dict[str, str] = {}      # a printed head name -> the family of the class option it titles (for a page search)


def printed_page(e, bk) -> int | None:
    """The printed page of an entry that cites none: the page of the one paragraph of the book that is the entry's head ("Acid Jet (Su):"),
    or None when the head is printed more than once or not at all."""
    if PAGE_SEARCH["blocks"] is None:
        PAGE_SEARCH["blocks"] = fp.read_blocks(bk, 1, max(bk.pages))
    want = fp.namekey(e.title)
    kind = group_kind(e)
    blocks = PAGE_SEARCH["blocks"]
    hits = []
    for i, p in enumerate(blocks):
        if p.kind != "para":
            continue
        cand = fp.head_candidate(p)                  # a bold head, and an italic one ("Acid Jet (Su):", the arcanist exploits)
        if not cand or not cand[1] or not cand[1][0][0].lstrip().startswith(":"):
            continue
        if fp.namekey(cand[0]) == want:
            hits.append(i)
    if len(hits) == 1:
        return blocks[hits[0]].page
    if not hits:
        return None
    # two lists print the same head ("Familiar", "Quick Study" are an arcanist exploit and a magus arcana or an investigator talent): the
    # section title above the head names the list, and the entry's own kind decides
    family = e.id.split("/")[1]
    for i in hits:
        # the head beside it names the list it stands in: the next head of the book (or the one before) is another option of the same family
        near = [j for j in range(i + 1, min(i + 8, len(blocks))) if blocks[j].kind == "para" and fp.head_candidate(blocks[j])]
        near = near or [j for j in range(i - 1, max(i - 8, -1), -1) if blocks[j].kind == "para" and fp.head_candidate(blocks[j])]
        for j in near[:1]:
            h = fp.head_candidate(blocks[j])
            if h and FAMILY_OF_TITLE.get(fp.namekey(h[0])) == family:
                return blocks[i].page
    return None


def full_printed_head(bk, title: str, page: int) -> str:
    """Return the full headed paragraph from the printed block, even when split_print clipped a cross-column continuation."""
    lo = max(1, page + fp.PAGE_OFFSET[0] - 1)
    hi = min(page + 2 + fp.PAGE_OFFSET[0], max(bk.pages))
    for block in fp.read_blocks(bk, lo, hi):
        if block.kind != "para":
            continue
        head = fp.head_candidate(block)
        if not head:
            continue
        printed_name = fp.namekey(head[0])
        if printed_name not in {fp.namekey(title), fp.namekey(inverted(title))} and fp.namekey(inverted(head[0])) != fp.namekey(title):
            continue
        return clean_full_printed_head("".join(run[0] for run in head[1]).strip().lstrip(": ").replace("Ref lex", "Reflex"))
    return ""


def clean_full_printed_head(text: str) -> str:
    """Apply the ordinary whitespace and apostrophe cleanup to a raw full-head fallback."""
    return re.sub(r"\s+", " ", text).strip().replace("’", "'").replace("‘", "'")
SENTENCE_END = re.compile(r"(?<=[.!?])[\"\u201d\u2019)]*\s+(?=[A-Z\u201c\"(+\u2013\d])")
CELL = re.compile(r"^(?:[+\-\u2013\u2014]?\d+(?:/[+\-\u2013\u2014]?\d+)*(?:st|nd|rd|th)?|[\u2014\u2013-])[,.]?$")


NEGATIONS = re.compile(r"\b(?:not|no|never|cannot|neither|nor)\b|n[\'\u2018\u2019]t", re.I)
SEE_REF = re.compile(r"\s*\([Ss]ee\s+([^()\d]{1,60})\)")


def strip_see(text: str) -> str:
    """A printed cross-reference "(see the atonement spell)" is kept in the text but the corpus may link the thing instead (ruling 16): a short one (at most six
    words, no number) is no difference. Any other parenthetical is text."""
    return SEE_REF.sub(lambda m: "" if len(m.group(1).split()) <= 6 else m.group(0), text)


def letter_edits(a: str, b: str) -> int:
    """The letters that differ between two texts (the longer side of each differing stretch)."""
    return sum(max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if tag != "equal")


NUMBER_TOKEN = re.compile(r"(?<!\w)[+\-]?\d+(?:[,./]\d+)*(?:st|nd|rd|th)?(?!\w)")


def number_tokens(text: str) -> list[str]:
    """The numbers of a text as tokens with their sign, "/", "," and "." kept ("+2", "1/2", "1,000", "10th"), the dashes of print and of the corpus alike."""
    return NUMBER_TOKEN.findall(text.replace("\u2212", "-").replace("\u2013", "-").replace("\u2014", "-"))


def squash_map(text: str) -> tuple[str, list[int]]:
    """The squashed text (letters and digits, lower case: `fp.squash`) and, for each of its characters, the place in the original text."""
    out, idx = [], []
    for i, ch in enumerate(text):
        for c in unicodedata.normalize("NFKD", ch).lower().replace("\u2019", "'"):
            if c.isascii() and c.isalnum():
                out.append(c)
                idx.append(i)
    return "".join(out), idx


def stands_in(sentence: str, written: str, sq_w: tuple[str, list[int]] | None = None) -> bool:
    """Whether the letters and digits of a printed sentence stand in the written text, on word boundaries, and the numbers of the stretch that matches are the
    numbers of the sentence, token by token, with sign, "/" and "," ("5" is not in "15", "1/2" is not "12", "+2" is not "-2")."""
    sq = fp.squash(sentence)
    if not sq:
        return True
    swq, idx = sq_w or squash_map(written)
    want = number_tokens(sentence)
    k = swq.find(sq)
    while k >= 0:
        a, b = idx[k], idx[k + len(sq) - 1] + 1
        left_ok = a == 0 or not written[a - 1].isalnum()
        right_ok = b >= len(written) or not written[b].isalnum()
        if left_ok and right_ok and number_tokens(written[a:b]) == want:
            return True
        k = swq.find(sq, k + 1)
    return False


def sentence_words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", unicodedata.normalize("NFKD", text).lower().replace("\u2019", "'"))


def one_misprint(a: str, b: str) -> bool:
    """Whether two words are one misprint apart: the same first letter and one letter replaced, left out, added, or two neighbours swapped ("anitpaladin",
    "elixer"). A change at the start of a word ("increase"/"decrease", "unable"/"enable", "either"/"neither") and two letters changed inside it ("minimum"/"maximum")
    make another word, not a misprint (review of #380, 2026-11-27)."""
    if a == b or a[:1] != b[:1]:
        return False
    if len(a) == len(b):
        diff = [i for i in range(len(a)) if a[i] != b[i]]
        return len(diff) == 1 or (len(diff) == 2 and diff[1] == diff[0] + 1 and a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]])
    if abs(len(a) - len(b)) != 1:
        return False
    short, long_ = (a, b) if len(a) < len(b) else (b, a)
    return any(long_[:i] + long_[i + 1:] == short for i in range(len(long_)))


def near_exact(sentence: str, written: list[str]) -> bool:
    """Whether a printed sentence is one of the written sentences up to a misprint: the same words, the same numbers (as tokens), the same number of negations
    (not, no, never, cannot, neither, nor, n't), and one word that is one misprint apart (`one_misprint`), **in a word of six letters or more** (a misprint of
    print that the corpus corrected, a ligature). A change of word identity (his/her, may/can, able/unable, valid/invalid, increase/decrease, minimum/maximum) is a loss."""
    ws = sentence_words(sentence)
    nums, negs = number_tokens(sentence), len(NEGATIONS.findall(sentence))
    for w in written:
        ww = sentence_words(w)
        if len(ww) != len(ws):
            continue
        diff = [(a, b) for a, b in zip(ws, ww) if a != b]
        if (len(diff) == 1 and len(diff[0][0]) >= 6 and len(diff[0][1]) >= 6 and one_misprint(*diff[0])
                and number_tokens(w) == nums and len(NEGATIONS.findall(w)) == negs):
            return True
    return False


PUBLICATION_TITLES: list[str] = []


def citation_re() -> re.Pattern:
    """A parenthetical citation of a book of `publications.toml` and a page: "(Core Rulebook 443)", "(Pathfinder RPG Bestiary 305)". Nothing else is a citation."""
    if not PUBLICATION_TITLES:
        path = HERE.parent / "publications.toml"
        data = tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        PUBLICATION_TITLES.extend(sorted({x["title"] for x in data.get("publication", []) if x.get("title")}, key=len, reverse=True))
    alt = "|".join(re.escape(x) for x in PUBLICATION_TITLES) or "(?!)"
    return re.compile(r"\s*\((?:Pathfinder RPG |Pathfinder Roleplaying Game |Pathfinder )?(?:" + alt + r") \d+(?:[-\u2013]\d+)?\)")


ERRATA_ROWS: dict[str, list[tuple[str, str]]] = {}


def errata_fixes(corpus: Path, entry_id: str) -> list[tuple[str, str]]:
    """The corrections of `scripts/errata.tsv` for an entry that the entry keeps (decision `misprint-fix` or `keep`): (printed value, kept value). The audit applies
    them to the printed text before it compares: a misprint that the corpus corrects on purpose (owner ruling 43) is no loss."""
    key = str(corpus)
    if key not in ERRATA_ROWS:
        rows: dict[str, list[tuple[str, str]]] = {}
        path = corpus / "scripts" / "errata.tsv"
        if path.exists():
            lines = path.read_text(encoding="utf-8").split("\n")
            head = lines[0].split("\t")
            for ln in lines[1:]:
                r = dict(zip(head, ln.split("\t")))
                if r.get("decision") in ("misprint-fix", "keep") and r.get("kept_value") and r.get("printed_value"):
                    rows.setdefault(r["entry"], []).append((r["printed_value"], r["kept_value"]))
        ERRATA_ROWS[key] = rows
    return ERRATA_ROWS[key].get(entry_id, [])


def apply_fixes(text: str, fixes: list[tuple[str, str]]) -> str:
    """The printed text with the corrections of the errata file applied (the printed value is found up to blanks and curly quotes)."""
    text = text.replace("\u2019", "'")
    for old, new in fixes:
        pat = r"\s*".join(re.escape(c) for c in "".join(old.replace("\u2019", "'").split()))       # the layer breaks a word here and there ("Ref lex", "f lames")
        text = re.sub(pat, new.replace("\\", "\\\\"), text)
    return text


def print_lost(printed: str, written: str, fixes: list[tuple[str, str]] | None = None) -> list[str]:
    """Print-coverage check (review of #373): the printed sentences (at least 12 letters) of a power's span that the written text lacks. A sentence is there when
    its letters and digits stand in the written text, or when it is one written sentence up to noise (`near_exact`); runs of three numeric tokens in a printed
    sentence (cells of a table that the text layer set inside it) are not words of it; a short printed cross-reference is no difference; a citation of a book and
    a page in parentheses ("(Core Rulebook 443)") is no difference when the written sentence has a link in its place (owner ruling 26); the corrections of the
    errata file are applied to the printed text first (`fixes`). The words of the whole text give no allowance."""
    if fixes:
        printed = apply_fixes(printed, fixes)
    plain = strip_see(re.sub(r"[_*>]|^\s*[-\u2022]\s+", "", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", written), flags=re.M))
    have = fp.squash(plain)
    wsents = SENTENCE_END.split(" ".join(plain.split()))
    sq_w = squash_map(plain)
    linked: dict[str, list[str]] = {}                                  # a written sentence with links: its letters, and the texts of its links
    for x in SENTENCE_END.split(" ".join(re.sub(r"[_*>]", "", written).split())):
        if "](" in x:
            linked.setdefault(fp.squash(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", x)), []).extend(m.group(1) for m in re.finditer(r"\[([^\]]*)\]\([^)]*\)", x))
    citation = citation_re()
    out = []
    for s in SENTENCE_END.split(" ".join(strip_see(printed).split())):
        if len(re.sub(r"[^A-Za-z]", "", s)) < 12:
            continue
        s = re.sub(r"^\((?:Ex|Su|Sp)(?:(?:, or |, and |, | or | and )(?:Ex|Su|Sp))*\):\s*", "", s)
        toks, kept, run = s.split(), [], []
        for x in toks + [""]:
            if x and CELL.match(x):
                run.append(x)
                continue
            if len(run) < 3:
                kept += run
            run = []
            if x:
                kept.append(x)
        s = " ".join(kept)
        if re.fullmatch(r"(?:Spells|Extracts|Formulae|Powers)\s+(?:per\s+Day|Known)", s.strip(), re.I):
            continue                                        # the title of the spell columns of a class table, its cells gone
        if stands_in(s, plain, sq_w) or near_exact(s, wsents):
            continue
        m = citation.search(s)
        if m and fp.squash(citation.sub("", s)) in linked:
            near = [x.lower() for x in re.findall(r"[A-Za-z0-9']+", s[:m.start()])[-4:]]          # the citation followed these words
            if any(w in near for x in linked[fp.squash(citation.sub("", s))] for w in re.findall(r"[a-z0-9']+", x.lower())):
                continue                                    # ruling 26: the citation went where a link stands, on a word of the phrase that it followed
        out.append(s)
    return out


def compare_one(e, book, bk, other=None) -> list[dict]:
    """The rows of one entry: one per power, from the shared print comparison of the archetype pass."""
    shape, n = shape_of(e.body)
    base = {"entry": e.id, "shape": shape, "page": e.page, "span": "", "note": ""}
    powers = powers_of(e)
    e0 = e                               # the entry as it is: its body is what the writer reads
    title = print_match_title(book, e.id, e.title)
    body = print_match_body(book, e.id, e.body)
    if title != e.title or body != e.body:
        e = dataclasses.replace(e, title=title, body=body)
    if shape == "multi":                 # a heading of the import is a head that print sets ("Order Abilities"): its paragraph is its own, not the one above's
        e = dataclasses.replace(e, body=headings_as_names(e.body))
    _, feats = fp.parse_import(e.body, set())
    by_name: dict[str, list] = {}
    for f in feats:
        by_name.setdefault(re.sub(r":$", "", f.name), []).append(f)
    for name, _ in powers:
        print_name = print_match_title("pathfinder-unchained", e.id, name)
        if print_name != name and print_name in by_name:
            by_name[name] = by_name[print_name]
    if not e.page.isdigit():
        # This batch’s missing-page recovery is scoped to the Advanced Class Guide.
        found = printed_page(e, bk) if book == "advanced-class-guide" else None
        if found is None:
            return [dict(base, feature=n_, anchor=fp.anchor_of(n_), verdict="nopage", status="hold", level_import="", level="",
                         note="no page is cited, and the head is not printed once in the book", span_sha256=sha) for n_, sha in powers]
        page = found
        page_found = True
    else:
        page = int(e.page)
        page_found = False
    last = page + (3 if shape == "multi" else 2)         # a power at the end of a page or column goes on over the next page
    blocks = fp.read_blocks(bk, max(1, page + fp.PAGE_OFFSET[0] - 1), min(last + fp.PAGE_OFFSET[0], max(bk.pages)))
    if book == "core-rulebook":
        blocks = core_rulebook_table_heads(blocks)
    unanchored = False
    if shape == "multi":
        anchored = anchor_section(blocks, e.title, {fp.squash(fp.ABILITY_TAG.sub("", n_)) for n_, _ in powers}, group_kind(e))
        if anchored is None or not anchored[1]:
            unanchored = True                      # no title, or no end title: the window runs to the end of the pages
        if anchored is not None:
            blocks = anchored[0]
    section = [fp.Para("title", [(e.title, True, False)], page, 0, 20)] + blocks
    TABLE_HEADS.clear()
    TABLE_HEADS.update(fp.squash(" ".join(c.strip() for c in tab[0].strip().strip("|").split("|"))) for tab in corpus_tables(e0.body))
    res = fp.compare_entry(e, section, bk)
    by_span = {r["span"]: r for r in res["rows"] if r["span"]}
    if page_found:
        for r_ in res["rows"]:
            r_["notes"] = list(r_.get("notes") or []) + [f"no page is cited; the head is printed on p. {page}"]
    where = {}                                       # span -> "Publication p. N" of a power that another source of the entry prints
    noend: set[str] = set()                          # spans found in a second-source window that has no end title: they hold
    variants: list[tuple[str, str, tuple]] = []      # (book, page, (title, text, replaced rows)) of a variant section (ruling 65)
    for src in (e.data.get("sources") or [])[1:]:
        pub, pg = src.get("publication"), str(src.get("page", ""))
        def not_printed(sp):                    # no row, or the print comparison found no head on the cited pages
            return sp not in by_span or any("head not printed" in n_ for n_ in by_span[sp]["notes"])
        missing = [f for f in feats if not_printed(f.span_sha())]
        if not missing or other is None or not pg.isdigit():
            continue
        power_keys = {fp.namekey(n_) for n_, _ in powers}
        got = other(pub, int(pg), e, shape, [f for f in missing if fp.namekey(f.name) in power_keys], [f.name for f in feats])      # the variant is found by powers, not by section labels
        if got is None:
            continue
        got, var, ended2 = got
        if var:
            variants.append((pub, pg, var))
            got = dict(got, **var[2])
        for sp, r2 in got.items():
            if not_printed(sp) and not any("head not printed" in n_ for n_ in r2["notes"]):
                by_span[sp] = r2
                where[sp] = (pub, pg)
                if not ended2:
                    noend.add(sp)
    rows, seen = [], Counter()
    _, raw_pfs = fp.split_print(section, [f.name for f in feats])               # the printed span of each power, before the comparison cuts or joins anything
    raw_text = {fp.namekey(fp.head_text(pf.head)): " ".join("".join(x[0] for x in para) for para in pf.paras) for pf in raw_pfs}
    if book == "core-rulebook":
        raw_text = {key: clean_core_rulebook_print(e.id, value) for key, value in raw_text.items()}
    blocks_b = rw.parse_blocks(e0.body.split("\n"))
    cands = rw.candidates(blocks_b, True)
    promo = promoted(blocks_b, cands)
    info = {rw.span_sha(blocks_b[c.start:c.end]): (section_of(blocks_b, c.start), promo.get(c.start - 1)) for c in cands}
    problems = []                                       # what holds every power of the entry
    if unanchored:
        problems.append("the printed title of the entry is not on the cited pages, or its section has no end: the window is not anchored")
    outside = outside_rows(e0.body) if shape == "single" else []        # a multi-power entry's other sections are rows of their own (below)
    if outside:
        problems.append("import rows outside the powers (" + ", ".join(outside[:4]) + ") are not transcribed from print yet")
    if TRADE_LABEL.search(e0.body):
        problems.append("a trade row (Replaces/Alters): class-option trades are not written yet")
    taken = set(re.findall(r"\{#([^}]+)\}", e0.body))
    plinks = prereq_links(e0.body)
    anchors_seen: Counter = Counter()
    for name, sha in powers:
        seen[name] += 1
        f = by_name.get(name, [None] * seen[name])[seen[name] - 1] if name in by_name else None
        r = by_span.get(f.span_sha()) if f is not None else None
        if r is not None and f.span_sha() in where:
            r = dict(r, notes=[f"printed in {where[f.span_sha()][0]} p. {where[f.span_sha()][1]}"] + list(r["notes"]))
        section, pr = info.get(sha, ("", None))
        src = where.get(f.span_sha()) if f is not None else None           # a power that another source of the entry prints has its own book and page
        # ruling 63: the tag is print's. The import's head may lack it (the alchemist discoveries of Ultimate Magic print "(Su)" over a name
        # the import wrote without a tag), so the printed head is read; a tag that print and the import both state must agree, else the power holds
        tag, disagree = ability_tag_for_option(book, name, (r or {}).get("head", "")) if shape == "single" else ("", False)
        notes_tag = [f"print's tag differs from the import's: {r.get('head', '')!r} against {name!r}"] if disagree else []
        common = dict(base, feature=name, section=section, book=src[0] if src else book, by="", ability_tag=tag,
                      reviewed_537="yes" if (e.id, sha) in REVIEWED else "", links_lost="", span_sha256=sha)
        if book == "advanced-class-guide" and (r is None or ("head not printed" in r.get("notes", []) and not r.get("print"))):
            rows.append(dict(common, anchor=fp.anchor_of(name), verdict="missing-head", status="hold", level_import="",
                             level="", note="head not printed on the cited page and the next ones", print="", print_sha256=""))
            continue
        if r is None:
            rows.append(dict(common, anchor=fp.anchor_of(name), verdict="missing-head", status="hold", level_import="",
                             level="", note="head not printed on the cited page and the next ones", print="", print_sha256=""))
            continue
        verdict = {"draft": "agree", "print": "differ", "hold": "hold"}[r["status"]]
        note_r = f"resolution of #537: {REVIEWED[(e.id, sha)]}" if (e.id, sha) in REVIEWED else ""
        notes = [n_ for n_ in r["notes"] if n_] + ([note_r] if note_r else []) + notes_tag
        if page_found:
            common["page"] = str(page)
        status, printed = r["status"], clean_acg_print(e.id, r["print"])
        if book == "core-rulebook":
            printed = clean_core_rulebook_print(e.id, printed)
        if book == "pathfinder-unchained":
            printed = pathfinder_unchained_links(e.id, clean_pathfinder_unchained_print(printed))
        if book == "core-rulebook":
            printed = fp.render_marks(printed)   # keep print's italic markers as TOML-safe Markdown, not internal control bytes
        blood_intro = ""
        if book == "advanced-class-guide" and e.id.startswith("ref/ragepower/"):
            power = e.id.rsplit("/", 1)[-1]
            greater = power.startswith("greater-")
            suffix = power.removeprefix("greater-") if greater else power
            if suffix.endswith("-blood") and not suffix.startswith("lesser-"):
                blood_intro = BLOOD_PREREQUISITE_INTROS["greater" if greater else "middle"]
                target_name = suffix if greater else "lesser-" + suffix
                phrase = "middle blood rage power" if greater else "lesser blood rage power"
                target = f"ref/ragepower/{target_name}"
                printed = printed.replace(phrase, f"[{phrase}]({target})", 1)
                raw_key = fp.namekey(fp.head_text(r["head"])) if r.get("head") else ""
                if raw_key:
                    complete = raw_text.get(raw_key, "")
                    if incomplete_paragraph(printed):
                        complete = full_printed_head(bk, e.title, page) or complete
                    if incomplete_paragraph(printed) and complete and not incomplete_paragraph(complete):
                        printed = complete.replace(phrase, f"[{phrase}]({target})", 1)
                        notes = [note for note in notes if not note.startswith("print text may be cut at a page or column break:")]
                    raw_text[raw_key] = blood_intro + " " + (complete or raw_text.get(raw_key, ""))
                printed = blood_intro + "\n\n" + printed
        if notes_tag:
            status = "hold"
        anchor = pr[1] if pr else r["anchor"]
        anchors_seen[anchor] += 1
        hard = False                                    # an explicit print decision may settle a tag difference under ruling 63
        if anchors_seen[anchor] > 1 or (anchor in taken and not pr):
            notes.append(f"anchor collision: {anchor}")
            status, hard = "hold", True
        if shape == "single" and not single_name_matches_title(e.id, e.title, name):
            notes.append("the power's name differs from the title of the entry")
            status, hard = "hold", True
        if "dropped table" in " ".join(notes) and shape == "single":
            printed2, adopted = adopt_tables(printed, e0.body)
            only_table = not any(n_.startswith(("rule word", "number", "hand review")) for n_ in notes)
            if adopted and only_table:
                printed = printed2
                notes = [n_ for n_ in notes if not n_.startswith("dropped table")] + ["ruling 62: the table of the corpus is print's rows, cell by cell: kept as a table"]
                if status == "hold" and r["status"] == "hold" and not hard and not problems:
                    status = "print"
        cut = incomplete_paragraph(printed)
        if cut:
            notes.append(f"print text may be cut at a page or column break: ...{cut}")
            status, hard = "hold", True
        lost_s = print_lost(raw_text.get(fp.namekey(fp.head_text(r["head"])), ""), printed) if r.get("head") else []
        if lost_s:
            notes.append(f"print sentences that the written text lacks ({len(lost_s)}): " + " | ".join(x[:60] for x in lost_s[:2]))
            status = "hold"
            if not ruling8_progression_decision(book, e.id, anchor, DECISIONS.get((e.id, anchor)), lost_s, printed):
                hard = True
        if problems:
            notes += problems
            status = "hold"
        if src:
            common["page"] = src[1]
        if f is not None and f.span_sha() in noend:
            notes.append("the second-source window has no end title: the text may run into another option")
            status, hard = "hold", True
        intro = marked_head_intro(book, e.id) if shape == "single" and (r.get("marked") or e.id in MARKED_HEAD_ENTRIES) else ""
        intro_page = marked_head_page(book, e.id) if intro else 0
        if intro:
            printed = intro + "\n\n" + printed
            notes.append("opens with print's sentence about the mark (the section intro)")
            if intro_page and intro_page < page:
                common["page"] = f"{intro_page}-{page}"
        if shape == "single":
            printed, lost = place_links(printed, plinks)
            if book == "ultimate-intrigue":
                printed = link_intrigue_class_prerequisites(printed)
                printed = repair_intrigue_italic_link_boundary(printed)
            if book == "core-rulebook":
                printed = core_rulebook_links(e.id, printed)
            crossed = option_link_kind_mismatches(book, printed)
            if crossed:
                notes.append("ruling 52: " + "; ".join(
                    f"\"{name}\" names a {target} ({group}) but print says {word}" for name, target, group, word in crossed))
                status, hard = "hold", True
            common["links_lost"] = "|".join(lost)
            printed = drop_unkeyed_link_marks(e.id, printed)
        if blood_intro and not hard:
            prerequisite_only = ("number: corpus", "rule 3: the prerequisite row", "link not placed:")
            if notes and all(note.startswith(prerequisite_only) for note in notes):
                notes = ["opens with print's section-intro prerequisite (Advanced Class Guide p. 80)"]
                status = "print"
        if shape == "single" and e.id.split("/")[1] in HEADING_FAMILIES:
            gh = group_map(bk).of(e.title, page)
            if gh is None:
                notes.append("no group heading found above the head")
                status, hard = "hold", True
            elif gh[1] > page:
                notes.append(f"the group heading is on p. {gh[1]}, after the cited p. {page}")
                status, hard = "hold", True
            else:
                printed = gh[0] + "\n\n" + printed
                if gh[1] < page:
                    common["page"] = f"{gh[1]}-{page}"           # the sentence is on the page before: the entry cites both (ruling 61)
        decided = DECISIONS.get((e.id, anchor))
        if print_decision_resolves(decided, status, r["status"], problems, hard):
            status = "print"
            notes.append(f"decision: {decided[1]}")
        elif decided and decided[0] == "print" and print_decision_may_settle(notes_tag, problems, {"notes": notes}):
            status = r["status"]                 # print's tag is the rule (ruling 63): the lead may settle a disagreement
            notes.append(f"decision: {decided[1]}")
        elif decided and decided[0] == "print" and status == "hold" and r["status"] == "hold" and not problems and not hard:
            status = "print"
            notes.append(f"decision: {decided[1]}")
        elif decided and decided[0] == "hold":
            status = "hold"                                  # held by decision: an errata check, a ruling that has not landed
            notes.append(f"held by decision: {decided[1]}")
        printed = prepend_intro(printed, marked_head_intro(book, e.id) if shape == "single" and (r.get("marked") or e.id in MARKED_HEAD_ENTRIES) else "")
        rows.append(dict(common, anchor=anchor, verdict=verdict, status=status,
                         level_import=r["level_import"] if r["level_import"] is not None else "",
                         level=level_of(r["print"]) or "", note="; ".join(notes)[:400], print=printed,
                         print_sha256=hashlib.sha256(printed.encode()).hexdigest()))
    if shape == "multi":
        rows = add_sections(e0, rows, res, feats, powers, by_name, base, book, problems, anchors_seen, variants)
        rows = apply_multi_decisions(rows, e0.id)
    return fence(rows, shape)


VARIANTS_ON = False                  # ruling 65 variants stay held until a reviewer has read the first settled one (`--variants` turns this on)
PRINT_ONLY_OK = {"classskill", "classskills", "bonusspells", "bonusfeats", "deities"}      # the sections that print sets for every class option of a kind


def add_sections(e, power_rows: list[dict], res: dict, feats: list, powers: list, by_name: dict, base: dict, book: str,
                 problems: list[str], anchors_seen: Counter, variants: list | None = None) -> list[dict]:
    """A multi-power entry is its opening, the sections that print sets (Class Skill, Bonus Spells, Bonus Feats, a section label like
    "Bloodline Powers") and its powers, in print order: the rows of the print comparison that no power owns are rows of their own
    (`shape` "section", `anchor` "opening" for the opening text), and the converted body is those rows in order."""
    by_sha = {sha: r for (name, sha), r in zip(powers, power_rows)}
    f_spans = {}
    seen: Counter = Counter()
    for name, sha in powers:
        seen[name] += 1
        f = by_name.get(name, [None] * seen[name])[seen[name] - 1] if name in by_name else None
        if f is not None:
            f_spans[f.span_sha()] = sha
    ordered: list[dict] = []
    opening = "\n\n".join(res.get("opening") or [])
    sec = dict(base, shape="section", book=book, by="", ability_tag="", reviewed_537="", links_lost="", level_import="", level="", section="")
    if opening:
        ocut = incomplete_paragraph(opening)
        ordered.append(dict(sec, feature="(opening)", anchor="opening", verdict="agree", status="hold" if ocut else "print", span_sha256="",
                            note="the opening text of print" + (f"; print text may be cut at a page or column break: ...{ocut}" if ocut else ""),
                            print=opening, print_sha256=hashlib.sha256(opening.encode()).hexdigest()))
    used = set()
    for r_ in res["rows"]:
        sha = f_spans.get(r_["span"]) if r_["span"] else None
        if sha is not None and sha in by_sha:
            ordered.append(by_sha[sha])
            used.add(sha)
            continue
        if "head not printed" in r_["notes"] and not r_["print"]:
            continue                                                   # an import head that print lacks: no section to write
        anchors_seen[r_["anchor"]] += 1
        status = r_["status"] if not problems and anchors_seen[r_["anchor"]] == 1 else "hold"
        notes = list(r_["notes"]) + ([f"anchor collision: {r_['anchor']}"] if anchors_seen[r_["anchor"]] > 1 else []) + problems
        label = r_["head"]
        if "head printed, not in the import" in " ".join(r_["notes"]) and fp.squash(re.sub(r"\s*\(.*$", "", label)) not in PRINT_ONLY_OK:
            notes.append("a section that print sets and the import lacks: not settled (a bold head of a table or of another option can read as one)")
            status = "hold"
        if re.search(r"[a-z][A-Z]", label):
            notes.append("the label has capitals inside a word (OCR small capitals): not settled")
            status = "hold"
        cut = incomplete_paragraph(r_["print"])
        if cut:
            notes.append(f"print text may be cut at a page or column break: ...{cut}")
            status = "hold"
        if re.match(r"^(?:- |\* |\||\d+[.)] )", r_["print"].lstrip()):
            notes.append("the section opens with a list or a table: not settled (the run-in label cannot lead it)")
            status = "hold"
        ordered.append(dict(sec, feature=r_["head"], anchor=r_["anchor"], verdict={"draft": "agree", "print": "differ", "hold": "hold"}[r_["status"]],
                            status=status, span_sha256=r_["span"], note="; ".join(notes)[:400], print=r_["print"],
                            print_sha256=hashlib.sha256(r_["print"].encode()).hexdigest()))
    ordered += [r for sha, r in by_sha.items() if sha not in used]       # a power that print has nowhere on the pages (a hold)
    olds = old_heading_levels(e.body)
    for pub, pg, (vtitle, vtext, _, vpage, vended) in variants or []:             # ruling 65: the variant is its own unlisted section, with its book and the printed page
        theirs = [r for r in ordered if r["shape"] == "multi" and r["book"] == pub]
        inside = bool(theirs) and all(norm(r["print"]) in norm(vtext) for r in theirs if r["print"])        # every power that it holds lies inside its text (and it holds one)
        vslug = fp.anchor_of(vtitle)
        # the import has a heading for it ("### Seaborn (Wildblooded Mutation)"): the section keeps that heading's key, written out
        old = next((s for s in olds if s == vslug or s.startswith(vslug + "-")), vslug)
        ordered.append(dict(sec, shape="variant", feature=vtitle, anchor=old, book=pub, page=str(vpage), verdict="agree",
                            status="hold" if (any(r["status"] == "hold" for r in theirs) or problems or not inside or not vended or not VARIANTS_ON or incomplete_paragraph(vtext)) else "print",
                            span_sha256="",
                            note=f"a variant that {pub} p. {vpage} prints under its own title" + ("" if inside else "; no power of the entry is inside its text, or one is not")
                            + ("" if vended else "; its section has no end title") + ("" if VARIANTS_ON else "; variants are held until a reviewer has read the first settled one (--variants)")
                            + (f"; print text may be cut: ...{incomplete_paragraph(vtext)}" if incomplete_paragraph(vtext) else ""), print=vtext,
                            print_sha256=hashlib.sha256(vtext.encode()).hexdigest()))
    have = {fp.slugify(fp.ABILITY_TAG.sub("", r["feature"])) for r in ordered} | {r["anchor"] for r in ordered if r["shape"] == "variant"}
    for slug in olds:
        if slug not in have:
            for r in ordered:
                r["status"] = "hold"
                r["note"] = (r["note"] + "; " if r["note"] else "") + f"the heading `{slug}` of the import has no row in print: its key would move"
            break
    return ordered


DECISIONS: dict[tuple[str, str], tuple[str, str]] = {}


def run_audit(args) -> int:
    """The print-coverage check over the class options of a book that are written already (the rule of #380 on #364's and later conversions): for each
    written entry the printed span of each of its heads, read again from the pages, against the entry's body. Prints the sentence and its printed head for every
    entry that the check holds. Read only."""
    corpus = Path(args.corpus).resolve()
    book = args.book
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), fp.publication_title(corpus, book))
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    install_split([x.title for x in load_class_options(corpus)] + (["Master Strike (Ex)"] if book == "core-rulebook" else []), book)
    held, n, skipped = 0, 0, 0
    others = [print_match_title(book, x.id, x.title) for x in load_class_options(corpus, book)]  # a printed head of another option ends the span
    rows = read_tsv(tsv_file(corpus, book))
    written = {eid for eid in {r["entry"] for r in rows} if all(r["status"] == LEDGER for r in rows if r["entry"] == eid)}
    for e in load_class_options(corpus, book):
        page = first_page(e.page)
        if e.id not in written or page is None:
            continue
        head_page = last_page(e.page) or page
        print_title = print_match_title(book, e.id, e.title)
        heads = [print_title] + re.findall(r"^#{2,6}\s+(.*?)(?:\s*\{#[^}]*\})?\s*$", e.body, re.M) + re.findall(r"^\*\*([^*\n]{2,60}?):?\*\*", e.body, re.M)
        multi = len(re.findall(r"^#{2,6}\s+", e.body, re.M)) > 1
        last = head_page + (3 if multi else 2)
        blocks = fp.read_blocks(bk, max(1, page + fp.PAGE_OFFSET[0] - 1), min(last + fp.PAGE_OFFSET[0], max(bk.pages)))
        if book == "core-rulebook":
            blocks = core_rulebook_table_heads(blocks)
        if multi:
            anchored = anchor_section(blocks, e.title, {fp.squash(fp.ABILITY_TAG.sub("", h)) for h in heads}, group_kind(e))
            if anchored is not None:
                blocks = anchored[0]
        _, pfs = fp.split_print([fp.Para("title", [(print_title, True, False)], page, 0, 20)] + blocks, heads + others)
        want = {fp.namekey(fp.ABILITY_TAG.sub("", h)) for h in heads} | {fp.namekey(inverted(h)) for h in heads}
        mine, seen = [], set()
        for pf in pfs:
            k = fp.namekey(fp.ABILITY_TAG.sub("", fp.head_text(pf.head)))
            if k in want and k not in seen:                  # the first head of each name: the next entry's "Edicts" is not this one's
                seen.add(k)
                mine.append(pf)
        n += 1
        if not mine:
            skipped += 1
            print(f"  {e.id}: no printed head found on the cited pages")
            continue
        for pf in mine:
            printed = " ".join("".join(x[0] for x in para) for para in pf.paras)
            if book == "core-rulebook":
                printed = clean_core_rulebook_print(e.id, printed)
            if book == "pathfinder-unchained":
                printed = pathfinder_unchained_links(e.id, clean_pathfinder_unchained_print(printed))
            lost = print_lost(printed, e.body, errata_fixes(corpus, e.id))
            if lost:
                held += 1
                print(f"{e.id} ({book} p. {e.page}), head {fp.head_text(pf.head)!r}: {len(lost)} printed sentences that the entry lacks")
                for s in lost[:4]:
                    print("    " + s[:240])
    print(f"audit of {book}: {n} written entries read, {skipped} with no printed head found on the pages, {held} heads held by the check")
    return 0


def run_compare(args) -> int:
    global CORPUS_ROOT
    corpus = Path(args.corpus).resolve()
    CORPUS_ROOT = corpus
    GROUP_OF_TARGET.clear()
    book = args.book
    title = fp.publication_title(corpus, book)
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    FAMILY_OF_TITLE.clear()
    FAMILY_OF_TITLE.update({fp.namekey(x.title): x.id.split("/")[1] for x in load_class_options(corpus)})
    INTRO_MARK["by"] = {}
    if book in INTRO_MARKS_BOOKS:
        INTRO_MARK["by"] = IntroMarkMap(bk).by_family
    INTRO_MARK_TEXT.clear()
    for family, (marker, prefer) in INTRO_MARK_SPECS.get(book, {}).items():
        intro = IntroMarkMap(bk, marker, prefer)
        INTRO_MARK_TEXT[(book, family)] = (intro.text, intro.page)
    families = set(args.families.split(",")) if args.families else None
    everything = load_class_options(corpus, book)
    MARKED_HEAD_ENTRIES.clear()
    for entry in everything:
        family = entry.id.split("/")[1]
        if family not in INTRO_MARK_SPECS.get(book, {}):
            continue
        page_match = re.match(r"\d+", entry.page)
        if not page_match:
            continue
        page = int(page_match.group())
        blocks = fp.read_blocks(bk, max(1, page + fp.PAGE_OFFSET[0] - 1), min(page + 2 + fp.PAGE_OFFSET[0], max(bk.pages)))
        section = [fp.Para("title", [(entry.title, True, False)], page, 0, 20)] + blocks
        _, printed_heads = fp.split_print(section, [entry.title])
        title_key = fp.namekey(entry.title)
        if any((pf.marked or re.search(r"[*†‡]", fp.head_text(pf.head))) and fp.namekey(fp.ABILITY_TAG.sub("", re.sub(r"[*†‡]", "", fp.head_text(pf.head)))) == title_key
               for pf in printed_heads):
            MARKED_HEAD_ENTRIES.add(entry.id)
    # Re-check marked heads already written in earlier runs; the imported head may no
    # longer be available to the print-head scan after the entry has been rewritten.
    MARKED_HEAD_ENTRIES.update(
        row["entry"] for row in read_tsv(tsv_file(corpus, book))
        if row.get("status") == LEDGER and "opens with print's sentence about the mark" in row.get("note", "")
    )
    names: list[str] = []
    acg_written: dict[str, list[str]] = {}
    acg_ids = {x.id for x in load_class_options(corpus, "advanced-class-guide")}
    for row in read_tsv(tsv_file(corpus, "advanced-class-guide")):
        if row["entry"] in acg_ids and row["status"] == LEDGER:
            acg_written.setdefault(row["entry"], []).append(row["feature"])
    for x in load_class_options(corpus):
        names.append(x.title)                      # a converted option has no import row left, but its italic head still ends the text above it
        if shape_of(x.body)[0] != "none":
            for f in fp.parse_import(x.body, set())[1]:
                names += [f.name, fp.tail_name(f.name)]
        elif x.book == "advanced-class-guide":
            # Written ACG entries no longer expose imported feature names in the body. Keep them
            # in the same order as before conversion so this batch does not change other books.
            for feature in acg_written.get(x.id, []):
                names += [feature, fp.tail_name(feature)]
    install_split(names + (["Master Strike (Ex)"] if book == "core-rulebook" else []), book)
    STOP_TITLES.clear()
    STOP_TITLES.update(fp.squash(re.sub(r"\s*\((?:[A-Z]{2,4}|HotW)\)\s*$", "", x.title)) for x in load_class_options(corpus))
    fp.KNOWN_OPTIONS[:] = [fp.item_tokens(x.title) for x in load_class_options(corpus)]      # ruling 60: a sentence that names a longer option holds
    REVIEWED.update(reviewed_spans(corpus))
    DECISIONS.clear()
    DECISIONS.update(read_decisions(decisions_file(corpus, book)))
    books_seen: dict[str, object] = {}

    def other(pub: str, pg: int, e, shape: str, missing: list, expected: list[str]):
        """The comparison of an entry against another book that prints some of its powers (an elemental bloodline is in Advanced Player's
        Guide p. 136 and Ultimate Magic p. 72): its rows by span, or None when there is no copy of that book."""
        if pub not in books_seen:
            fp.configure_book(pub)
            pdf2 = fp.find_pdf(Path(args.books), fp.publication_title(corpus, pub))
            books_seen[pub] = fp.load_book(fp.book_xml(pdf2, Path(args.cache))) if pdf2 else None
            fp.configure_book(book)                  # the book at hand again: a source with no copy must not leave its switches on
        bk2 = books_seen[pub]
        if bk2 is None:
            return None
        fp.configure_book(pub)
        try:
            last2 = pg + (3 if shape == "multi" else 1)
            blocks2 = fp.read_blocks(bk2, max(1, pg + fp.PAGE_OFFSET[0] - 1), min(last2 + fp.PAGE_OFFSET[0], max(bk2.pages)))
            anchored2 = anchor_section(blocks2, e.title, {fp.squash(fp.ABILITY_TAG.sub("", n_)) for n_ in expected}, group_kind(e))
            win = anchored2[0] if anchored2 is not None else blocks2          # the second source's section of the same title, else the whole window (a variant has its own title)
            res2 = fp.compare_entry(e, [fp.Para("title", [(e.title, True, False)], pg, 0, 20)] + win, bk2)
            return ({r["span"]: r for r in res2["rows"] if r["span"]}, variant_section(blocks2, bk2, e, missing, expected),
                    anchored2[1] if anchored2 is not None else True)           # a window with no end title holds
        finally:
            fp.configure_book(book)
    entries = [x for x in everything if not families or x.id.split("/")[1] in families]
    cen = census(entries)
    rows, props = [], {}
    for e in entries:
        if shape_of(e.body)[0] == "none":
            continue
        for r in compare_one(e, book, bk, other):
            if r.get("print"):
                r["print"] = proposal_print(book, r["print"])
                props.setdefault(e.id, {"id": e.id, "feature": []})["feature"].append(
                    {"anchor": r["anchor"], "print": class_option_errata(corpus, e.id, r["print"])})
            rows.append(r)
    twice: dict[tuple[str, str, str, str], set[str]] = {}
    ledger_before = read_tsv(tsv_file(corpus, book))
    ledger_props = read_props(proposals_file(corpus, book))
    for r in ledger_before:                         # the written entries count too: a paragraph that one of them has is claimed
        if counts_for_duplicate_check(r) and r["status"] == LEDGER and r["entry"] not in {x["entry"] for x in rows} and ledger_props.get((r["entry"], r["anchor"])):
            twice.setdefault(printed_claim_key(r), set()).add(r["entry"])
    for r in rows:                                  # one printed paragraph claimed by two entries holds both: an owner decides whose it is
        if r.get("print") and counts_for_duplicate_check(r):
            twice.setdefault(printed_claim_key(r), set()).add(r["entry"])
    for r in rows:
        if r.get("print") and counts_for_duplicate_check(r) and len(twice[printed_claim_key(r)]) > 1:
            r["note"] = (r["note"] + "; " if r["note"] else "") + "the print head matches more than one entry: " + ", ".join(sorted(twice[printed_claim_key(r)]))[:120]
            r["status"] = "hold" if r["status"] in SETTLED else r["status"]
    old = read_tsv(tsv_file(corpus, book))
    old_props = read_props(proposals_file(corpus, book))
    compared = {r["entry"] for r in rows}
    kept = [r for r in old if r["status"] == LEDGER and r["entry"] not in compared]       # the ledger of the entries written already
    for r in kept:
        original = old_props.get((r["entry"], r["anchor"]))
        if original is None:
            continue
        printed = refresh_written_proposal(corpus, book, r, original)
        props.setdefault(r["entry"], {"id": r["entry"], "feature": []})["feature"].append(
            {"anchor": r["anchor"], "print": printed})
    write_tsv(tsv_file(corpus, book), sorted(kept + rows, key=lambda r: r["entry"]))
    write_props(proposals_file(corpus, book), dict(sorted(props.items())))
    print(report(rows, cen))
    print(f"ledger: {len({r['entry'] for r in kept})} entries written before and kept")
    return 0


def report(rows: list[dict], cen: dict) -> str:
    verdicts = Counter(r["verdict"] for r in rows)
    per_entry: dict[str, list[dict]] = {}
    for r in rows:
        per_entry.setdefault(r["entry"], []).append(r)
    held = sum(1 for rs in per_entry.values() if any(r["status"] == "hold" for r in rs))
    reach = sum(1 for r in rows if "resolution of #537" in r.get("note", ""))
    lines = [f"resolutions of #537 that reach these powers: {reach}",
             f"entries: {cen['single']} single-power, {cen['multi']} multi-power, {cen['none']} without import rows (out of the rewrite)",
             f"powers: {len(rows)}; verdicts: " + ", ".join(f"{k} {v}" for k, v in sorted(verdicts.items())),
             f"entries with a hold: {held} of {len(per_entry)}"]
    if cen["none"]:
        lines.append("without import rows by family: " + ", ".join(f"{k} {v}" for k, v in sorted(cen["none_by_family"].items(), key=lambda kv: -kv[1])))
    return "\n".join(lines)


def counts_for_duplicate_check(row: dict) -> bool:
    """An unanchored multi-power window is held and cannot claim a head from its whole citation range."""
    return not (row.get("book") == "ultimate-intrigue" and row.get("shape") in {"multi", "section", "variant"} and row.get("status") == "hold"
                and "window is not anchored" in row.get("note", ""))


def write_atomic(path: Path, text: str) -> None:
    """A temp file, then a rename: a crash leaves the old file, never half of a new one."""
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["\t".join(HEADER)]
    for r in rows:
        lines.append("\t".join(str(r.get(k, "")).replace("\t", " ").replace("\n", " ") for k in HEADER))
    write_atomic(path, "\n".join(lines) + "\n")                  # a crash leaves the old ledger, not half of one


def read_tsv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").split("\n")
    assert lines[0].split("\t") == HEADER, f"{path}: header is not {HEADER}"
    return [dict(zip(HEADER, ln.split("\t"))) for ln in lines[1:] if ln]


def write_props(path: Path, props: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = ["# The printed text of the powers of the class options of the book, written ones included (the check reads an entry against it). Generated: never edit by hand.", ""]
    for e in props.values():
        for f in e["feature"]:
            out += ["[[entry]]", f"id = {fp.toml_str(e['id'])}", f"anchor = {fp.toml_str(f['anchor'])}", f"print = {fp.toml_str(f['print'])}", ""]
    write_atomic(path, "\n".join(out))


def read_props(path: Path) -> dict[tuple[str, str], str]:
    if not path.exists():
        return {}
    return {(x["id"], x["anchor"]): x["print"] for x in tomllib.loads(path.read_text(encoding="utf-8")).get("entry", [])}


def apply_errata_text(text: str, fixes: list[tuple[str, str]]) -> str:
    """Apply only exact, reviewed print corrections; leave unmatched near misses unchanged."""
    for printed, corrected in fixes:
        count = text.count(printed)
        if count == 1:
            text = text.replace(printed, corrected, 1)
        elif count == 0:
            continue
        else:
            raise ValueError(f"errata text occurs {count} times")
    return text


def class_option_errata(corpus: Path, entry_id: str, text: str) -> str:
    path = corpus / "scripts" / "errata.tsv"
    if not path.exists():
        return text
    with path.open(encoding="utf-8", newline="") as f:
        fixes = [(r["printed_value"], r["kept_value"]) for r in csv.DictReader(f, delimiter="\t")
                 if r["entry"] == entry_id and r["decision"] == "misprint-fix"]
    return apply_errata_text(text, fixes)


# ---- writing -------------------------------------------------------------------------------------

def convert_body(e, texts: dict[str, str], levels: dict[str, int | None], anchors: dict[str, str],
                 shape: str | None = None) -> tuple[str, list[tuple[str, int | None]]]:
    """The converted body and the `features` of a multi-power entry. `texts` maps the span hash of each power to its printed
    text, `levels` to its level, `anchors` to its anchor. The path goes by the shape of the entry: one power is the single-power form
    (no head, no features) whatever else the body holds; several powers get a head each, at the level of the section they stand in,
    and a power before the first section takes the level of that section (it must not nest the section inside it)."""
    lines = e.body.split("\n")
    blocks = rw.parse_blocks(lines)
    cands = rw.candidates(blocks, True)
    shape = shape or ("single" if len(cands) == 1 else "multi")
    if shape == "single":
        c = cands[0]
        text = texts[rw.span_sha(blocks[c.start:c.end])]
        printed_key = prose_key(text)
        keep_before = [b.text for b in blocks[:c.start] if not (b.text.startswith("|") and b.text in text)
                       and not duplicate_print_block(b.text, printed_key)]
        keep_after = [b.text for b in blocks[c.end:] if not (b.text.startswith("|") and b.text in text)
                      and not duplicate_print_block(b.text, printed_key)]
        return "\n" + "\n\n".join(keep_before + [text] + keep_after).strip("\n") + "\n", []
    out, features, i = [], [], 0
    by_start = {c.start: c for c in cands}
    promo = promoted(blocks, cands)
    levels_of_sections = [len(b.text) - len(b.text.lstrip("#")) for b in blocks if b.kind == "boundary" and b.text.startswith("#")]
    first_section = levels_of_sections[0] if levels_of_sections else 0
    heading = 0                                          # the level of the section that the block stands in (0: before the first)
    while i < len(blocks):
        b = blocks[i]
        if i in promo:
            i += 1                                       # the heading becomes the head of the power below it
            continue
        if b.kind == "boundary" and b.text.startswith("#"):
            heading = len(b.text) - len(b.text.lstrip("#"))
        c = by_start.get(i)
        if c:
            sha = rw.span_sha(blocks[c.start:c.end])
            name = re.sub(r"[:]$", "", c.name)
            anchor = anchors[sha]
            if i - 1 in promo:
                level_h = promo[i - 1][0]
            elif heading:
                level_h = heading + 1
            else:
                level_h = first_section if first_section else 2
            out.append("#" * level_h + f" {name} {{#{anchor}}}")
            out.append(texts[sha])
            features.append((anchor, levels.get(sha)))
            i = c.end
            continue
        out.append(b.text)
        i += 1
    return "\n" + "\n\n".join(out).strip("\n") + "\n", features


def features_front(front: str, features: list[tuple[str, int | None]]) -> str:
    items = "".join("  { anchor = \"%s\"%s },\n" % (a, f", level = {l}" if l else "") for a, l in features)
    out, n = re.subn(r"(^group = \"[^\"]*\")(\n|\Z)", lambda m: m.group(1) + "\nfeatures = [\n" + items + "]\n", front, count=1, flags=re.M)
    assert n == 1, "an entry with features has a group row to put them after"
    return out


def with_page(text: str, page: str) -> str:
    """Set the page on the first source row, adding the field when absent."""
    lines = text.splitlines(keepends=True)
    start = next((i for i, line in enumerate(lines) if line.strip() == "[[sources]]"), None)
    if start is None:
        return text
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("[[sources]]") or lines[i].startswith("[fields]")), len(lines))
    for i in range(start + 1, end):
        if re.match(r"page\s*=", lines[i]):
            lines[i] = f'page = "{page}"\n'
            return "".join(lines)
    publication = next((i for i in range(start + 1, end) if lines[i].startswith("publication = ")), start)
    lines.insert(publication + 1, f'page = "{page}"\n')
    return "".join(lines)


def first_page(page: str) -> int | None:
    """The start folio of a single page or intro-to-head range."""
    match = re.match(r"\d+", page)
    return int(match.group()) if match else None


def last_page(page: str) -> int | None:
    """The last folio in a single page or intro-to-head range."""
    match = re.search(r"(?:^|-)\s*(\d+)\s*$", page)
    return int(match.group(1)) if match else None


def clean_acg_print(entry_id: str, text: str) -> str:
    """Clean ACG extraction artifacts and apply reviewed option-link corrections."""
    if entry_id == "ref/exploit/arcane-weapon":
        text = re.sub(r"_spell_\s*Table 1[–-]1:.*?Magical supremacy\s*_storing_", "_spell storing_", text, flags=re.S)
    if entry_id in {"ref/exploit/see-magic", "ref/exploit/spell-tinkerer"}:
        text = re.sub(r"\s*\n\s*", " ", text).strip()
    if entry_id in {"ref/exploit/greater-spell-resistance", "ref/exploit/resistance-drain"}:
        text = text.replace("[spell resistance](ref/spell/spell-resistance) exploit",
                            "[spell resistance](ref/exploit/spell-resistance) exploit", 1)
    if (not any(line.lstrip().startswith("|") for line in text.splitlines())
            and len(re.findall(r"[ \t]{2,}", text)) >= 4):
        text = clean_full_printed_head(text)
    return text


def core_rulebook_table_heads(blocks: list) -> list:
    """Separate the CRB bard table from Suggestion and terminate Feat at Master Strike."""
    want = {fp.namekey(name) for name in EXTRA_NAMES}
    out = []
    for block in blocks:
        if block.kind != "para":
            out.append(block)
            continue
        split_at = None
        for i, (text, bold, italic) in enumerate(block.runs):
            head = text.strip().rstrip(":").strip()
            if (bold or italic) and fp.namekey(head) == fp.namekey("Master Strike (Ex)"):
                split_at = i
                break
            if ("spells known" in block.plain().casefold() and (bold or italic)
                    and fp.namekey(head) in want and ability_tag_of(head)):
                split_at = i
                break
        if split_at is None:
            out.append(block)
            continue
        head = block.runs[split_at][0].strip().rstrip(":").strip()
        if fp.namekey(head) == fp.namekey("Master Strike (Ex)"):
            if split_at:
                out.append(fp.Para("para", list(block.runs[:split_at]), block.page, block.col, block.size))
            out.append(fp.Para("para", list(block.runs[split_at:]), block.page, block.col, block.size))
        else:
            if out and out[-1].kind == "title" and re.match(r"Table 3[–-]4:\s*Bard Spells Known", out[-1].plain(), re.I):
                out.pop()
            # Everything before the embedded option head is the table title and its cells, not option prose.
            out.append(fp.Para("para", list(block.runs[split_at:]), block.page, block.col, block.size))
    return out


def clean_core_rulebook_print(entry_id: str, text: str) -> str:
    """Remove only the two Bard tables that the CRB text layer interleaves with these power spans."""
    if entry_id == "ref/performance/countersong":
        text = re.sub(r"\s*Spells per Day\b.*?(?=\s*\(including\s+the\s+bard\s+himself\s*\))", " ", text, flags=re.S)
    if entry_id == "ref/performance/inspire-competence":
        text = re.sub(r"\s*Table 3[–-]4:\s*Bard Spells Known\b.*?(?=\s*_?Suggestion \(Sp\)_?)", " ", text, flags=re.S)
    if entry_id == "ref/talent/feat":
        text = re.sub(r"\s*Master Strike\s+_?\(Ex\)_?\s*:\s*.*$", "", text, flags=re.S)
    if entry_id == "ref/ragepower/animal-fury":
        text = text.replace("base attack bonus -5", "base attack bonus –5")
    if entry_id == "ref/performance/fascinate":
        text = text.replace("takes a -4 penalty", "takes a –4 penalty")
    return re.sub(r"\s+", " ", text).strip()


def clean_pathfinder_unchained_print(text: str) -> str:
    """Preserve print's en dash for negative numeric values, without changing fractional notation."""
    return re.sub(r"(?<!\S)-(?=\d)", "–", text)


CRB_PRINT_LINKS = {
    "ref/performance/soothing-performance": [("fatigued", "ref/misc/fatigued"), ("sickened", "ref/misc/sickened"), ("shaken", "ref/misc/shaken")],
    "ref/ragepower/internal-fortitude": [("sickened", "ref/misc/sickened"), ("nauseated", "ref/misc/nauseated")],
    "ref/ragepower/intimidating-glare": [("Intimidate", "ref/skill/intimidate")],
    "ref/performance/deadly-performance": [("perform", "ref/skill/perform-any")],
    "ref/ragepower/night-vision": [("racial trait", "ref/rule/low-light-vision")],
}


def core_rulebook_links(entry_id: str, text: str) -> str:
    links = CRB_PRINT_LINKS.get(entry_id, [])
    return fp.apply_links(text, links)[0] if links else text


def proposal_print(book: str, text: str) -> str:
    """Store Core Rulebook italics as Markdown instead of the print reader's internal markers."""
    return fp.render_marks(text) if book == "core-rulebook" else text


def refresh_written_proposal(corpus: Path, book: str, row: dict, original: str) -> str:
    """Refresh a retained written proposal from print while preserving its marked-head intro."""
    entry_id = row["entry"]
    printed = clean_acg_print(entry_id, drop_unkeyed_link_marks(entry_id, original))
    if book == "core-rulebook":
        printed = clean_core_rulebook_print(entry_id, printed)
        printed = core_rulebook_links(entry_id, printed)
    if book == "pathfinder-unchained":
        printed = pathfinder_unchained_links(entry_id, clean_pathfinder_unchained_print(printed))
    printed = class_option_errata(corpus, entry_id, printed)
    intro = marked_head_intro(book, entry_id) if entry_id in MARKED_HEAD_ENTRIES else ""
    if intro:
        printed = prepend_intro(printed, intro)
        intro_page = marked_head_page(book, entry_id)
        head_page = int(re.match(r"\d+", row["page"]).group()) if re.match(r"\d+", row["page"]) else 0
        if intro_page and head_page and intro_page < head_page:
            row["page"] = f"{intro_page}-{head_page}"
        if "opens with print's sentence about the mark" not in row["note"]:
            row["note"] = (row["note"] + "; " if row["note"] else "") + "opens with print's sentence about the mark (the section intro)"
    else:
        printed = drop_marked_intro(printed)
    row["print_sha256"] = hashlib.sha256(printed.encode()).hexdigest()
    return proposal_print(book, printed)


def run_headings(args) -> int:
    """Ruling 61 for the entries that are converted already: each evolution entry opens with the printed sentence of its group heading
    (it is idempotent: an entry that has the sentence is left). An entry whose heading is on another page than the cited one is reported."""
    corpus = Path(args.corpus).resolve()
    book = args.book
    title = fp.publication_title(corpus, book)
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    done = skipped = 0
    for e in load_class_options(corpus, book):
        if e.id.split("/")[1] not in HEADING_FAMILIES or shape_of(e.body)[0] != "none" or not e.page.isdigit():
            continue
        page = int(e.page)
        gh = group_map(bk).of(e.title, page)
        if gh is None or gh[1] > page:
            print(f"  {e.id}: " + ("no group heading found above the head" if gh is None else f"the group heading is on p. {gh[1]}, after the cited p. {page}"))
            skipped += 1
            continue
        if gh[0] in e.body:
            continue
        body = "\n" + gh[0] + "\n\n" + e.body.lstrip("\n")
        text = e.path.read_text(encoding="utf-8").replace(e.body, body, 1)
        if gh[1] < page:
            text = with_page(text, f"{gh[1]}-{page}")           # the sentence is on the page before: the entry cites both (ruling 61)
        write_atomic(e.path, text)
        done += 1
    print(f"group headings: {done} entries changed, {skipped} not changed")
    return 0


def old_heading_levels(body: str) -> dict[str, int]:
    """The headings of an import body that have no explicit key: derived slug -> level. Their keys must stay."""
    out = {}
    for ln in body.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.*?)\s*$", ln)
        if m and "{#" not in m.group(2):
            out[fp.slugify(fp.ABILITY_TAG.sub("", m.group(2)))] = len(m.group(1))
    return out


def convert_multi(eid: str, rows: list[dict], props: dict, old_keys: frozenset | set = frozenset(), old_levels: dict | None = None,
                  entry_book: str = "") -> tuple[str, list[tuple[str, int | None]]]:
    """The body of a multi-power entry from its rows, in print order (rulings 64 and 65):
    - the opening text as paragraphs;
    - a **power** of the entry's own book as a `##` head with its explicit key; `features` lists these, with the level that print gives;
    - any other **section** that print sets as a paragraph that opens with the bold printed label ("**Edicts:** The cavalier must ..."), with
      no head, no key and no `features` entry; a section that was a heading in the import (`### Bloodline Powers`) stays that heading at its
      level, so its key does not move (rule 3 of AGENTS.md);
    - a **variant** that another book prints under its own title is its own unlisted `##` section, whose paragraphs are print's, each power
      of the variant a run-in paragraph; the import powers that it holds are not written twice.
    A power or heading that had a key before keeps it (`sec-<slug>`, written out)."""
    old_levels = old_levels or {}
    has_variant = any(r["shape"] == "variant" for r in rows)
    parts: list[str] = []
    features: list[tuple[str, int | None]] = []
    for r in rows:
        text = props[(eid, r["anchor"])]
        if r["shape"] == "section" and r["anchor"] == "opening":
            parts.append(text)
            continue
        head = re.sub(r"(?<!\\)([*_])", r"\\\1", r["feature"])
        if r["shape"] == "multi" and has_variant and entry_book and r["book"] != entry_book:
            continue                                            # held by the variant section
        if r["shape"] == "section":
            level = old_levels.get(fp.slugify(fp.ABILITY_TAG.sub("", r["feature"])))
            if level:
                parts += ["#" * level + " " + head, text]
            else:
                first, *rest = text.split("\n\n")
                parts += [f"**{head}:** {first}"] + rest
            continue
        key = "sec-" + r["anchor"] if ("sec-" + r["anchor"]) in old_keys and r["anchor"] not in old_keys else r["anchor"]
        parts += [f"## {head} {{#{key}}}", text]
        if r["shape"] == "multi":
            features.append((key, int(r["level"]) if r["level"] else None))
    return "\n" + "\n\n".join(parts).strip("\n") + "\n", features


def heading_keys(body: str) -> set[str]:
    """The URL keys of the headings of a body: an explicit `{#key}`, else the derived key of the heading text."""
    keys = set()
    for ln in body.split("\n"):
        m = re.match(r"^#{1,6}\s+(.*?)(?:\s*\{#([^}]+)\})?\s*$", ln)
        if m:
            keys.add(m.group(2) or "sec-" + fp.slugify(m.group(1)))              # a heading without a key has the derived key `sec-<slug>`
    return keys


def run_neighbours(args) -> int:
    """A report before a book batch: for each multi-power entry of the book, the printed titles and bold heads that its window holds and that are
    not its own (its powers and sections are), and whether the window found an end. A lead reads it to check the printed neighbours."""
    corpus = Path(args.corpus).resolve()
    book = args.book
    title = fp.publication_title(corpus, book)
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    everything = load_class_options(corpus)
    STOP_TITLES.clear()
    STOP_TITLES.update(fp.squash(re.sub(r"\s*\((?:[A-Z]{2,4}|HotW)\)\s*$", "", x.title)) for x in everything)
    install_split([x.title for x in everything], book)
    families = set(args.families.split(",")) if args.families else None
    bad = 0
    for e in load_class_options(corpus, book, families):
        shape, _ = shape_of(e.body)
        if shape != "multi" or not e.page.isdigit():
            continue
        page = int(e.page)
        blocks = fp.read_blocks(bk, max(1, page + fp.PAGE_OFFSET[0] - 1), min(page + 3 + fp.PAGE_OFFSET[0], max(bk.pages)))
        _, feats = fp.parse_import(headings_as_names(e.body), set())
        own = {fp.squash(fp.ABILITY_TAG.sub("", f.name)) for f in feats} | PRINT_ONLY_OK
        anch = anchor_section(blocks, e.title, own, group_kind(e))
        if anch is None:
            print(f"{e.id} (p. {page}): the printed title is not on the pages")
            bad += 1
            continue
        win, ended = anch
        others = []
        for b in win:
            if b.kind == "title":
                label = b.plain().strip()
            else:
                label = (fp.head_of_para(b) or "") if b.kind == "para" else ""
            if label and fp.squash(fp.ABILITY_TAG.sub("", label)) not in own:
                others.append(("title " if b.kind == "title" else "head ") + re.sub(r"\s+", " ", label))
        bad += 0 if ended else 1
        print(f"{e.id} (p. {page}): {len(win)} blocks, end {'found' if ended else 'NOT FOUND'}; not its own: " + ("; ".join(others) if others else "none"))
    print(f"neighbours: {bad} entries without a title or an end")
    return 0


def run_write(args) -> int:
    """Writes the entries whose rows are all settled, marks their rows `written` (the ledger), and runs the corpus formatter when
    `--checker` is given. An entry that is written has no import row, so a second run changes nothing."""
    corpus = Path(args.corpus).resolve()
    book = args.book
    families = set(args.families.split(",")) if args.families else None
    rows = read_tsv(tsv_file(corpus, book))
    props = read_props(proposals_file(corpus, book))
    by_entry: dict[str, list[dict]] = {}
    for r in rows:
        by_entry.setdefault(r["entry"], []).append(r)
    converted = 0
    for e in load_class_options(corpus, book, families):
        mine = by_entry.get(e.id)
        shape = shape_of(e.body)[0]
        if shape == "none" and mine and all(r["status"] == LEDGER for r in mine):
            proposal = props.get((e.id, mine[0]["anchor"]), "")
            if book == "pathfinder-unchained" and mine[0]["shape"] == "single":
                # This book's print cleanup may refine a retained written span; use the refreshed proposal on rerun.
                body = drop_unkeyed_link_marks(e.id, proposal)
                body = class_option_errata(corpus, e.id, body)
            else:
                intro = proposal.split("\n\n", 1)[0]
                has_intro = bool(re.match(r"^(?:Discoveries|Talents|Tricks|Investigator talents).*marked with .*asterisk", intro)) or (
                    book == "ultimate-intrigue" and any("opens with print's sentence about the mark" in r.get("note", "") for r in mine)
                )
                if has_intro:
                    assert proposal.startswith(intro), f"{e.id}: proposal lacks the printed intro for its marked head"
                    body = prepend_intro(e.body, intro)
                else:
                    body = drop_marked_intro(e.body)
                body = drop_unkeyed_link_marks(e.id, body)
                body = class_option_errata(corpus, e.id, body)
            front = e.front
            own = [r for r in mine if r["book"] == book]
            if own and own[0]["page"] and own[0]["page"] != e.page:
                front = with_page(front, own[0]["page"])
            if body != e.body or front != e.front:
                write_atomic(e.path, "+++\n" + front.strip("\n") + "\n+++\n" + body)
                converted += 1
            continue
        if shape == "none" or not mine or any(r["status"] not in SETTLED for r in mine):
            continue
        blocks = rw.parse_blocks(e.body.split("\n"))
        texts, levels, anchors = {}, {}, {}
        for r in mine:
            if r["shape"] == "section":
                continue
            texts[r["span_sha256"]] = props[(e.id, r["anchor"])]
            levels[r["span_sha256"]] = int(r["level"]) if r["level"] else None
            anchors[r["span_sha256"]] = r["anchor"]
        if shape == "multi":
            body, features = convert_multi(e.id, mine, props, heading_keys(e.body), old_heading_levels(e.body), book)
        else:
            body, features = convert_body(e, texts, levels, anchors, shape)
        keep = heading_keys(e.body)
        new_keys = heading_keys(body)
        lost = keep - new_keys
        assert not lost, f"{e.id}: the keys {sorted(lost)} would move"                  # rule 3 of AGENTS.md: the keys of the headings stay
        front = features_front(e.front, features) if features else e.front
        if WRITE_ABILITY_TYPE and shape == "single":
            tag = mine[0]["ability_tag"]
            if book != "ultimate-combat":
                tag = tag or ability_tag_of(mine[0]["feature"])
            front = with_ability_type(front, tag)
        own = [r for r in mine if r["book"] == book]
        if own and own[0]["page"] and own[0]["page"] != e.page:
            front = with_page(front, own[0]["page"])
        write_atomic(e.path, "+++\n" + front.strip("\n") + "\n+++\n" + body)
        for r in mine:
            r["status"] = LEDGER
        write_tsv(tsv_file(corpus, book), rows)               # per entry: a failure on a later entry leaves the ledger as true as the entries
        converted += 1
    print(f"converted {converted} entries")
    if converted and args.checker:
        import subprocess
        subprocess.run([args.checker, "fmt", str(corpus)], check=True)
    return 0


def run_ability_type(args) -> int:
    """Ruling 63 for the written single-power entries: `[fields] ability_type = "Su"` from the ledger's `ability_tag`. Off until the app
    reads the key (`WRITE_ABILITY_TYPE`): data CI fails on a key that the reader does not know."""
    if not WRITE_ABILITY_TYPE:
        print("ability_type is off: the app does not read the key yet (WRITE_ABILITY_TYPE)")
        return 0
    corpus = Path(args.corpus).resolve()
    rows = read_tsv(tsv_file(corpus, args.book))
    done = untagged = 0
    for e in load_class_options(corpus, args.book):
        mine = [r for r in rows if r["entry"] == e.id and r["status"] == LEDGER and r["shape"] == "single"]
        tag = mine[0]["ability_tag"] if mine else ""
        if mine and args.book != "ultimate-combat":
            tag = tag or ability_tag_of(mine[0]["feature"])
        if mine and not tag:
            untagged += 1
        if mine:
            new = with_ability_type(e.front, tag)
            current = e.path.read_text(encoding="utf-8")
            canonical = "+++\n" + new.strip("\n") + "\n+++\n" + e.body
            if new != e.front or (not tag and current != canonical):
                if current != canonical:
                    write_atomic(e.path, canonical)
                    done += 1
    print(f"ability_type: {done} entries changed, {untagged} written single-power entries have no printed tag (no key)")
    return 0


# ---- the check -----------------------------------------------------------------------------------

def norm(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)).strip()



def prose_key(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", text).casefold())


def duplicate_print_block(block: str, printed_key: str) -> bool:
    key = prose_key(block)
    return len(key) >= 80 and key in printed_key


def written_tag_error(entry_id: str, expected: str, actual: str) -> str | None:
    return f"{entry_id}: ability_type {actual!r} differs from the printed tag {expected!r}" if actual != expected else None

def run_check(args) -> int:
    corpus = Path(args.corpus).resolve()
    books = [args.book] if args.book else sorted(p.name[len("540-"):-len(".tsv")] for p in (corpus / "scripts" / DIR).glob("540-*.tsv")
                                                  if not p.name.endswith((".decisions.tsv",)))
    errors: list[str] = []
    for book in books:
        rows = read_tsv(tsv_file(corpus, book))
        props = read_props(proposals_file(corpus, book))
        entries = {e.id: e for e in load_class_options(corpus, book)}
        by_entry: dict[str, list[dict]] = {}
        for r in rows:
            by_entry.setdefault(r["entry"], []).append(r)
        written = {eid for eid, rs in by_entry.items() if all(r["status"] == LEDGER for r in rs)}
        cen = census([e for eid, e in entries.items() if eid not in written])
        pending = 0
        for eid, e in entries.items():
            shape, _ = shape_of(e.body)
            mine = by_entry.get(eid)
            if eid in written:
                # a section is a run-in paragraph with its printed label (ruling 64), a variant section holds run-in paragraphs of print's own:
                # those labels are print's; any other bold label is an import row
                allowed = {r["feature"] for r in mine if r["shape"] == "section"}
                for r in mine:
                    if r["shape"] == "variant":
                        allowed |= set(LABEL_ROW.findall(props.get((eid, r["anchor"]), "")))
                stray = [m for m in LABEL_ROW.findall(e.body) if m not in allowed]
                if shape != "none" or stray:
                    errors.append(f"{eid}: written, but the entry still holds an import row or label" + (f" ({stray[0]})" if stray else ""))
                for par in e.body.strip().split("\n\n"):
                    if not paragraph_complete(par):
                        errors.append(f"{eid}: written, but a paragraph ends mid-sentence (a page or column break?): ...{' '.join(par.split())[-50:]}")
                body = norm(e.body)
                for r in mine:
                    text = props.get((eid, r["anchor"]))
                    if text is not None and norm(text) not in body:
                        errors.append(f"{eid}: written, but the printed text of `{r['anchor']}` is not in the entry")
                singles = [r for r in mine if r["shape"] == "single"]
                if singles:
                    compact = lambda value: re.sub(r"\s+", " ", value).strip()
                    proposal = props.get((eid, singles[0]["anchor"]))
                    if args.book and proposal is not None and compact(proposal) != compact(e.body):
                        errors.append(f"{eid}: written single-power body differs from its complete print proposal")
                    expected_tag = singles[0]["ability_tag"]
                    actual_tag = (e.data.get("fields") or {}).get("ability_type", "")
                    tag_error = written_tag_error(eid, expected_tag, actual_tag)
                    if tag_error:
                        errors.append(tag_error)
                # ruling 63: the ability tag is print's, so a written single-power entry whose printed head has one carries it
                single = [r for r in mine if r["shape"] == "single"]
                continue
            if shape == "none":
                if mine and any(r["status"] != LEDGER for r in mine):
                    errors.append(f"{eid}: no import row is left, but the table has a row that is not `written`")
                continue
            if not mine:
                pending += 1                  # a part of the book that no batch has compared yet: reported, not an error
                continue
            have = {r["span_sha256"] for r in mine if r["shape"] not in ("section", "variant")}
            if have != {sha for _, sha in powers_of(e)}:
                errors.append(f"{eid}: the table is stale (the spans of the import rows changed)")
            elif all(r["status"] in SETTLED for r in mine):
                errors.append(f"{eid}: settled but not written (run --write)")
        print(f"{book}: {len(entries)} class options: {len(written)} written (ledger), {cen['single']} single-power and {cen['multi']} multi-power "
              f"not converted, {cen['none']} without import rows (reported, not rewritten); {pending} with import rows not compared yet")
    for line in errors:
        print("error:", line)
    return 1 if errors else 0


# ---- self-test -----------------------------------------------------------------------------------

def self_test() -> int:
    global CORPUS_ROOT
    ok, bad = 0, []

    def eq(a, b, what):
        nonlocal ok
        if a == b:
            ok += 1
        else:
            bad.append(f"{what}: {a!r} != {b!r}")

    eq(inverted("Greater Beast Totem (Su)"), "Beast Totem, Greater (Su)", "print sets the variant behind the name")
    eq(inverted("Beast Totem"), "Beast Totem", "a name without a variant stays")
    eq(counts_for_duplicate_check({"book": "ultimate-intrigue", "shape": "section", "status": "hold", "note": "window is not anchored"}), False, "Ultimate Intrigue's unanchored held multi-power section cannot claim a single head")
    eq(counts_for_duplicate_check({"shape": "multi", "status": "hold", "note": "a printed window is anchored"}), True, "an anchored multi-power hold still claims its print text")
    eq(counts_for_duplicate_check({"book": "ultimate-magic", "shape": "section", "status": "hold", "note": "window is not anchored"}), True, "other books keep their prior duplicate-window behavior")
    eq(counts_for_duplicate_check({"shape": "single", "status": "hold", "note": "window is not anchored"}), True, "a single-power hold still participates in duplicate checks")
    eq(fp.import_name("ref/vigtalent/expose-weaknesses", "Expose Weaknesses (Ex)"), "Expose Weakness (Ex)", "Ultimate Intrigue p. 14: printed singular head matches its entry title")
    eq(fp.import_name("ref/vigtalent/environmental-weapon", "Environmental Weapon (Ex)"), "Environment Weapon (Ex)", "Ultimate Intrigue p. 14: the misspelled import head matches the entry title")
    eq(single_name_matches_title("ref/vigtalent/expose-weaknesses", "Expose Weakness", "Expose Weaknesses (Ex)"), True, "a printed singular head can match the exact entry title through its import-head correction")
    eq(single_name_matches_title("ref/vigtalent/environmental-weapon", "Environment Weapon", fp.import_name("ref/vigtalent/environmental-weapon", "Environmental Weapon (Ex)")), True, "Ultimate Intrigue p. 14: the printed title matches after the import-head correction")
    eq(INVERTED_HEAD.match("Beast Totem, Greater (Su)").groups(), ("Beast Totem", "Greater", " (Su)"), "the inverted head is read")
    eq(INVERTED_HEAD.match("Pool Strike, Arcing (Su)").groups(), ("Pool Strike", "Arcing", " (Su)"), "an inverted Pool Strike head is read")
    eq(inverted("Arcing Pool Strike (Su)"), "Pool Strike, Arcing (Su)", "the title's variant moves behind its base name")
    eq(inverted("Weapon Training (Ex)"), "Weapon Training (Ex)", "a non-variant title remains unchanged")
    eq(ability_tag_for_option("core-rulebook", "Fast Stealth", "Fast Stealth (Ex)"), ("Ex", False),
       "Core Rulebook ability tag comes from print's head")
    eq(ability_tag_for_option("core-rulebook", "Fast Stealth (Ex)", "Fast Stealth"), ("", False),
       "Core Rulebook does not inherit an unprinted tag")
    eq(ability_tag_for_option("pathfinder-unchained", "Bite", "Bite (Ex)"), ("Ex", False),
       "Pathfinder Unchained ability tag comes from print's head")
    eq(ability_tag_for_option("pathfinder-unchained", "Bite (Su)", "Bite (Ex)"), ("Ex", True),
       "Pathfinder Unchained printed tag disagrees with an imported tag")
    pu_claim = {"book": "pathfinder-unchained", "page": "35", "feature": "Climb (Ex)", "print_sha256": "same"}
    eq(printed_claim_key(pu_claim) == printed_claim_key({**pu_claim, "page": "31"}), False,
       "Pathfinder Unchained repeated text on another page is not a duplicate claim")
    eq(printed_claim_key(pu_claim) == printed_claim_key({**pu_claim, "page": "35"}), True,
       "Pathfinder Unchained duplicate claims on the same page still hold")
    eq(INTRO_MARK_SPECS["core-rulebook"]["talent"], ("Talents marked with an asterisk", "sneak attack"),
       "Core Rulebook marked talent intro is registered")
    eq(INTRO_MARK_SPECS["pathfinder-unchained"]["talent"], ("Talents marked with an asterisk", "sneak attack"),
       "Pathfinder Unchained marked talent intro is registered")
    old_intro = INTRO_MARK_TEXT.get(("core-rulebook", "talent"))
    INTRO_MARK_TEXT[("core-rulebook", "talent")] = ("Talents marked with an asterisk add effects to sneak attack.", 68)
    eq(marked_head_intro("core-rulebook", "ref/talent/bleeding-attack"),
       "Talents marked with an asterisk add effects to sneak attack.", "Core Rulebook marked intro is read")
    eq(marked_head_page("core-rulebook", "ref/talent/bleeding-attack"), 68, "Core Rulebook marked intro start page")
    if old_intro is None:
        INTRO_MARK_TEXT.pop(("core-rulebook", "talent"), None)
    else:
        INTRO_MARK_TEXT[("core-rulebook", "talent")] = old_intro
    old_intro = INTRO_MARK_TEXT.get(("pathfinder-unchained", "talent"))
    INTRO_MARK_TEXT[("pathfinder-unchained", "talent")] = ("Talents marked with an asterisk add effects to a rogue's sneak attack.", 20)
    eq(marked_head_intro("pathfinder-unchained", "ref/talent/bleeding-attack-unchained-rogue"),
       "Talents marked with an asterisk add effects to a rogue's sneak attack.",
       "Pathfinder Unchained marked talent intro is read")
    eq(marked_head_page("pathfinder-unchained", "ref/talent/bleeding-attack-unchained-rogue"), 20,
       "Pathfinder Unchained marked intro page")
    if old_intro is None:
        INTRO_MARK_TEXT.pop(("pathfinder-unchained", "talent"), None)
    else:
        INTRO_MARK_TEXT[("pathfinder-unchained", "talent")] = old_intro
    errata_print = "The alchemist's Intelligent modifier applies."
    errata_kept = "The alchemist's Intelligence modifier applies."
    eq(apply_errata_text(errata_print, [("Intelligent modifier", "Intelligence modifier")]), errata_kept,
       "an exact reviewed misprint is corrected")
    eq(apply_errata_text(errata_kept, [("Intelligent modifier", "Intelligence modifier")]), errata_kept,
       "a reviewed correction is idempotent")
    eq(proposal_print("core-rulebook", "The \x01Core Rulebook\x02 applies."), "The _Core Rulebook_ applies.",
       "Core Rulebook proposal text uses Markdown italics")
    try:
        near_miss = "The alchemist's intellegent modifier applies."
        eq(apply_errata_text(near_miss, [("Intelligent modifier", "Intelligence modifier")]), near_miss,
           "a near-miss misprint stays unchanged")
    except ValueError:
        eq(False, True, "a near-miss misprint stays unchanged")
    eq(features_front('id = "x"\ngroup = "order"', [("a", None)]), 'id = "x"\ngroup = "order"\nfeatures = [\n  { anchor = "a" },\n]\n', "a front that ends at the group row gets its features")
    P = fp.Para
    E = type("E", (), {"title": "Wing Buffet"})()
    blk = [P("title", [("1-Point Evolutions", True, False)], 60, 0, 18),
           P("para", [("The following evolutions cost 1 point from the eidolon\u2019s evolution pool.", False, False)], 60, 0),
           P("para", [("Bite (Ex)", True, False), (": An eidolon bites.", False, False)], 60, 0),
           P("para", [("Wing Buffet (Ex)", True, False), (": An eidolon buffets.", False, False)], 61, 1),
           P("title", [("2-Point Evolutions", True, False)], 61, 1, 18),
           P("para", [("The following evolutions cost 2 points from the eidolon\u2019s evolution pool.", False, False)], 61, 1)]
    gh = group_heading(E, blk)
    eq(gh and gh[0], "1-Point Evolutions: The following evolutions cost 1 point from the eidolon's evolution pool.", "ruling 61: the heading above the head and its sentence")
    eq(gh and gh[1], 60, "ruling 61: the page of the heading")
    eq(group_heading(type("E", (), {"title": "Nothing"})(), blk), None, "ruling 61: a head that is not printed has no heading")
    eq(group_heading(type("E", (), {"title": "Bite"})(), blk[2:]), None, "ruling 61: no title above the head, no heading")
    eq(with_page('[[sources]]\npublication = "x"\npage = "62"\n\n[fields]\n', "61-62"), '[[sources]]\npublication = "x"\npage = "61-62"\n\n[fields]\n', "ruling 61: the page row becomes a range")
    eq(with_page('[[sources]]\npublication = "x"\n\n[fields]\n', "12"), '[[sources]]\npublication = "x"\npage = "12"\n\n[fields]\n', "a missing source page is added")
    eq(first_page("68-70"), 68, "range-page audit starts at the cited intro page")
    eq(first_page("70"), 70, "single-page audit starts at its page")
    eq(first_page("intro"), None, "page audit skips an invalid page")
    eq([last_page("68-70"), last_page("70")], [70, 70], "range-page audit reads through the printed head page")
    eq("Table 1" in clean_acg_print("ref/exploit/arcane-weapon", "_spell_ Table 1–1: rows Magical supremacy _storing_"), False,
       "ACG Arcane Weapon drops its interleaved class table")
    eq("Spells per Day" in clean_core_rulebook_print("ref/performance/countersong", "An effect. Spells per Day 1st 1 2nd 2 (including the bard himself) uses Perform."), False,
       "CRB Countersong drops interleaved Table 3–3 rows")
    eq("Table 3–4" in clean_core_rulebook_print("ref/performance/inspire-competence", "A bonus. Table 3–4: Bard Spells Known rows _Suggestion (Sp)_: prose."), False,
       "CRB Inspire Competence drops interleaved Table 3–4 rows")
    eq("Master Strike" in clean_core_rulebook_print("ref/talent/feat", "A rogue gains a feat. Master Strike _(Ex)_: A class feature."), False,
       "CRB Feat stops before the Master Strike class feature")
    eq(clean_core_rulebook_print("ref/ragepower/animal-fury", "base attack bonus -5"), "base attack bonus –5",
       "CRB Animal Fury preserves print's en dash")
    eq(clean_pathfinder_unchained_print("the penalty is -5, and damage is 1-1/2 times the modifier"),
       "the penalty is –5, and damage is 1-1/2 times the modifier",
       "Pathfinder Unchained negative values use print's en dash while fractions keep their hyphen")
    eq(pathfinder_unchained_links("ref/unchevolution/swallow-whole",
       "using the [grab](ref/carried/bestiary/rules/universal-monster-rules/grab) ability"),
       "using the [grab](ref/unchevolution/grab) ability", "an evolution named in print links to the Unchained evolution")
    eq(clean_core_rulebook_print("ref/performance/fascinate", "takes a -4 penalty"), "takes a –4 penalty",
       "CRB Fascinate preserves print's en dash")
    eq(core_rulebook_links("ref/performance/soothing-performance", "removes fatigued, sickened, and shaken."),
       "removes [fatigued](ref/misc/fatigued), [sickened](ref/misc/sickened), and [shaken](ref/misc/shaken).",
       "Core Rulebook links its printed conditions")
    eq(core_rulebook_links("ref/ragepower/night-vision", "or a racial trait"),
       "or a [racial trait](ref/rule/low-light-vision)", "Core Rulebook links the named racial trait")
    old_extra = list(EXTRA_NAMES)
    EXTRA_NAMES[:] = ["Suggestion (Sp)"]
    P = fp.Para
    table_blocks = [P("title", [("Table 3–4: Bard Spells Known", True, False)], 37, 1, 16),
                    P("para", [("Spells Known Level 0 1st", True, False), (" 4 2 ", False, False),
                               ("Suggestion (Sp)", False, True), (": A bard can suggest.", False, False)], 37, 1)]
    split_blocks = core_rulebook_table_heads(table_blocks)
    eq([b.plain() for b in split_blocks], ["Suggestion (Sp): A bard can suggest."],
       "CRB table-plus-italic head is split before comparison")
    feat_blocks = [P("para", [("A rogue gains a feat. ", False, False),
                               ("Master Strike (Ex)", False, True), (": A class feature.", False, False)], 68, 1)]
    feat_split = core_rulebook_table_heads(feat_blocks)
    eq([b.plain() for b in feat_split], ["A rogue gains a feat. ", "Master Strike (Ex): A class feature."],
       "CRB Master Strike terminates the Feat option span")
    EXTRA_NAMES[:] = old_extra
    eq(clean_acg_print("ref/exploit/greater-spell-resistance", "the [spell resistance](ref/spell/spell-resistance) exploit"),
       "the [spell resistance](ref/exploit/spell-resistance) exploit", "the printed spell resistance exploit links to the option")
    eq(clean_acg_print("ref/exploit/resistance-drain", "the [spell resistance](ref/spell/spell-resistance) exploit"),
       "the [spell resistance](ref/exploit/spell-resistance) exploit", "Resistance Drain links the named exploit")
    eq(clean_acg_print("ref/exploit/see-magic", "First sentence.\n\nSecond sentence."), "First sentence. Second sentence.",
       "ACG art-wrapped power paragraphs rejoin")
    with tempfile.TemporaryDirectory() as temp:
        old_root, old_targets = CORPUS_ROOT, dict(GROUP_OF_TARGET)
        CORPUS_ROOT = Path(temp)
        GROUP_OF_TARGET.clear()
        target = Path(temp) / "entries" / "talent" / "test-option.md"
        target.parent.mkdir(parents=True)
        target.write_text('+++\nid = "ref/talent/test-option"\n[fields]\nkind = "class_option"\ngroup = "rogue-talent"\n+++\n', encoding="utf-8")
        eq(option_link_kind_mismatches("core-rulebook", "A rogue selects [test option](ref/talent/test-option) hex."),
           [("test option", "ref/talent/test-option", "rogue-talent", "hex")], "Core Rulebook link-kind check catches a wrong option noun")
        eq(option_link_kind_mismatches("core-rulebook", "A rogue selects [test option](ref/talent/test-option) talent."), [],
           "Core Rulebook link-kind check keeps the matching option kind")
        eq(option_link_kind_mismatches("pathfinder-unchained", "A rogue selects [test option](ref/talent/test-option) hex."),
           [("test option", "ref/talent/test-option", "rogue-talent", "hex")],
           "Pathfinder Unchained link-kind check catches a wrong option noun")
        eq(option_link_kind_mismatches("pathfinder-unchained", "A rogue selects [test option](ref/talent/test-option) talent."), [],
           "Pathfinder Unchained link-kind check keeps the matching option kind")
        eq(option_link_kind_mismatches("advanced-players-guide", "A rogue selects [test option](ref/talent/test-option) hex."), [],
           "the Core Rulebook link check stays book-gated")
        CORPUS_ROOT = old_root
        GROUP_OF_TARGET.clear()
        GROUP_OF_TARGET.update(old_targets)
    DECISIONS.clear()
    DECISIONS[("ref/x/y", "z")] = ("hold", "an errata check")
    DECISIONS[("ref/x/y", "w")] = ("print", "settled")
    eq((DECISIONS[("ref/x/y", "z")][0], DECISIONS[("ref/x/y", "w")][0]), ("hold", "print"), "a decision is a hold or print")
    eq(print_decision_resolves(("print", "printed tag"), "hold", "hold", [], False), True,
       "ruling 63: an explicit print decision can use the printed tag")
    eq(print_decision_resolves(("print", "printed tag"), "hold", "draft", [], False), True,
       "ruling 63: a tag-only hold can settle an otherwise matching draft")
    eq(print_decision_resolves(("print", "printed tag"), "hold", "hold", [], True), False,
       "a print decision cannot clear an independent hard blocker")
    eq(print_decision_resolves(("print", "printed tag"), "hold", "hold", ["number difference"], False), False,
       "a print decision cannot clear a number difference")
    env_decision = ("print", "Ultimate Intrigue p. 14: progression values agree under ruling 8")
    env_sentence = "At 5th, 10th, 15th, and 20th levels, the vigilante can select an additional type of terrain."
    env_lost = "At and 20th levels, the vigilante can select an additional type of terrain."
    eq(ruling8_progression_decision("ultimate-intrigue", "ref/vigtalent/environmental-weapon", "environment-weapon", env_decision, [env_lost], env_sentence), True,
       "Ultimate Intrigue p. 14: ruling 8 settles the reviewed Repeat progression")
    eq(ruling8_progression_decision("ultimate-intrigue", "ref/vigtalent/environmental-weapon", "environment-weapon", env_decision, [env_lost.replace("20th", "19th")], env_sentence), False,
       "ruling 8 decision does not clear a changed progression level")
    eq(ruling8_progression_decision("ultimate-intrigue", "ref/vigtalent/environmental-weapon", "environment-weapon", env_decision, [env_lost], env_sentence.replace("20th", "19th")), False,
       "ruling 8 decision does not clear when the printed sentence changed")
    eq(ruling8_progression_decision("ultimate-magic", "ref/vigtalent/environmental-weapon", "environment-weapon", env_decision, [env_lost], env_sentence), False,
       "the Ultimate Intrigue progression decision does not affect another book")
    DECISIONS.clear()
    eq(print_match_title("pathfinder-unchained", "ref/talent/ledge-walker-unchained-rogue", "Ledge Walker (Unchained Rogue)"),
       "Ledge Walker", "Unchained rogue talent matching drops its corpus-only suffix")
    eq(print_match_title("pathfinder-unchained", "ref/talent/ledge-walker-unchained-rogue", "Ledge Walker (Unchained Rogue) (Ex)"),
       "Ledge Walker (Ex)", "Unchained rogue talent matching preserves the printed ability tag")
    eq(print_match_title("advanced-players-guide", "ref/talent/ledge-walker-unchained-rogue", "Ledge Walker (Unchained Rogue)"),
       "Ledge Walker (Unchained Rogue)", "talent title normalization stays Pathfinder Unchained-gated")
    eq(print_match_body("pathfinder-unchained", "ref/talent/ledge-walker-unchained-rogue", "**Ledge Walker (Unchained Rogue) (Ex)**"),
       "**Ledge Walker (Ex)**", "Unchained rogue talent labels match their printed heads")
    eq(print_match_body("core-rulebook", "ref/talent/ledge-walker-unchained-rogue", "**Ledge Walker (Unchained Rogue) (Ex)**"),
       "**Ledge Walker (Unchained Rogue) (Ex)**", "talent label normalization stays Pathfinder Unchained-gated")
    eq((title_as_head(fp.Para("title", [("Table 2\u20139: Eidolon Base Statistics", True, False)], 59, 0, 18)).runs[0][1],
        title_as_head(fp.Para("title", [("2-Point Evolutions", True, False)], 61, 0, 18)).runs[0][1]), (False, True),
       "ruling 62: the title of a table stays in the text of the power, a section heading ends it")
    cls = type("C", (), {"body": "\n### Class Features\n\n#### Alchemy (Su) {#alchemy}\n\nAt 1st level, an alchemist.\n\n#### Swift Alchemy (ex)\n\nAt 4th level.\n", "book": "x", "page": "1"})()
    eq([(q.name, q.anchor, q.head_level, q.section) for q in power_records(cls, "class")],
       [("Alchemy (Su)", "alchemy", 4, "Class Features"), ("Swift Alchemy (ex)", "swift-alchemy", 4, "Class Features")], "the powers of a base class are its #### heads, with their keys")
    eq([(q.name, q.head_level) for q in power_records(type("S", (), {"body": "\n**Animal Fury (Ex)**\n\n**Ability:** A bite attack.\n", "book": "x", "page": "1"})(), "class_option")], [("Animal Fury (Ex)", 0)], "the powers of a class option are its import names")
    eq(power_records(cls, "none"), [], "a rule entry has no power of its own")
    mrows = [{"shape": "section", "anchor": "opening", "feature": "(opening)", "level": ""}, {"shape": "section", "anchor": "edicts", "feature": "Edicts", "level": ""},
             {"shape": "multi", "anchor": "calling", "feature": "Calling (Ex)", "level": "2"}, {"shape": "multi", "anchor": "retribution", "feature": "Retribution (Ex)", "level": ""}]
    mprops = {("ref/order/x", "opening"): "Cavaliers who join.", ("ref/order/x", "edicts"): "Protect the faith.", ("ref/order/x", "calling"): "At 2nd level, a prayer.",
              ("ref/order/x", "retribution"): "Once a day."}
    mbody, mfeats = convert_multi("ref/order/x", mrows, mprops)
    eq(mbody, "\nCavaliers who join.\n\n**Edicts:** Protect the faith.\n\n## Calling (Ex) {#calling}\n\nAt 2nd level, a prayer.\n\n## Retribution (Ex) {#retribution}\n\nOnce a day.\n",
       "ruling 64: a multi-power body is the opening, the sections as run-in paragraphs and the powers as heads, in print order")
    eq(mfeats, [("calling", 2), ("retribution", None)], "features list the powers only, with a level when print gives one")
    kb, kf = convert_multi("ref/order/x", mrows, mprops, {"sec-edicts", "sec-retribution"}, {"edicts": 3})
    eq(("### Edicts\n\nProtect the faith." in kb, "**Edicts:**" in kb, "## Retribution (Ex) {#sec-retribution}" in kb, kf[-1]), (True, False, True, ("sec-retribution", None)),
       "ruling 64: a section that was a heading stays that heading, so its key does not move; a power that had one keeps its key")
    eq(heading_keys("\n### Edicts\n\nx\n\n### Retribution\n") <= heading_keys(kb), True, "ruling 64: no heading key of the import moves")
    vrows = mrows + [{"shape": "multi", "anchor": "envenom", "feature": "Envenom (Su)", "level": "3", "book": "ultimate-magic"},
                     {"shape": "variant", "anchor": "envenomed", "feature": "Envenomed", "level": "", "book": "ultimate-magic"}]
    vprops = {**mprops, ("ref/order/x", "envenom"): "At 3rd level, a lick.", ("ref/order/x", "envenomed"): "Print's variant.\n\n**Envenom (Su):** At 3rd level, a lick."}
    for r in vrows[:4]:
        r["book"] = "advanced-players-guide"
    vb, vf = convert_multi("ref/order/x", vrows, vprops, set(), {}, "advanced-players-guide")
    eq(("## Envenomed {#envenomed}" in vb, "## Envenom (Su)" in vb, [a for a, _ in vf]), (True, False, ["calling", "retribution"]),
       "ruling 65: a variant of another book is its own unlisted section, its powers are not written twice and not listed")
    eq(headings_as_names("\n### Order Abilities\n\nAn order.\n\n## Done {#done}\n"), "\n**Order Abilities**\n\nAn order.\n\n**Done**\n", "a heading is a bold name, the lines around it stay")
    eq(old_heading_levels("\n### Bloodline Powers\n\n## Done {#done}\n"), {"bloodline-powers": 3}, "the headings of an import without a key")
    class EE:
        body = "\n**Edicts**\n"
    def sect(head, text, notes, status="print"):
        return {"span": "", "head": head, "anchor": fp.anchor_of(head), "status": status, "notes": notes, "print": text}
    fake = {"opening": [], "rows": [sect("Class Skill", "Swim.", ["head printed, not in the import: added from print"]),
                                    sect("Will", "+2 +3", ["head printed, not in the import: added from print"]),
                                    sect("FoCused arCane sChools", "Fire.", []),
                                    sect("Bonus Spells", "- a\n- b", []),
                                    sect("Edicts", "Protect.", [])]}
    got = {r["feature"]: r["status"] for r in add_sections(EE, [], fake, [], [], {}, {"entry": "x", "shape": "multi", "page": "1", "note": ""}, "b", [], Counter(), [])}
    eq(got, {"Class Skill": "print", "Will": "hold", "FoCused arCane sChools": "hold", "Bonus Spells": "hold", "Edicts": "print"},
       "a print-only section settles only when its label is on the short list; an OCR-cased label and a list-first section hold")
    eq(sorted(r["status"] for r in add_sections(type("E4", (), {"body": "\n### Revelations\n\nText.\n"}), [], {"opening": [], "rows": [sect("Edicts", "Protect.", [])]}, [], [], {},
                                                {"entry": "x", "shape": "multi", "page": "1", "note": ""}, "b", [], Counter(), [])), ["hold"],
       "a heading of the import that print has no row for holds, its key would move")
    ptxt = "A talent.\n\nThe table:\n\nDisguise Time\n\nMinor details only 1 full-round action\n\nDisguise as a different race 1 minute\n\nA tail."
    cbody = "\nA talent.\n\n|Disguise|Time|\n| --- | --- |\n|Minor details only|1 full-round action|\n|Disguise as a different race|1 minute|\n"
    eq(adopt_tables(ptxt, cbody), ("A talent.\n\nThe table:\n\n|Disguise|Time|\n| --- | --- |\n|Minor details only|1 full-round action|\n|Disguise as a different race|1 minute|\n\nA tail.", 1),
       "ruling 62: print's rows, cell by cell, are the table of the corpus")
    eq(adopt_tables("A talent. Disguise Time Minor details only 1 full-round action Disguise as a different race 1 minute", cbody)[0],
       "A talent.\n\n|Disguise|Time|\n| --- | --- |\n|Minor details only|1 full-round action|\n|Disguise as a different race|1 minute|", "ruling 62: the rows run together as one paragraph are the table")
    eq(adopt_tables(ptxt.replace("1 minute", "2 minutes"), cbody)[1], 0, "ruling 62: a row that differs is no table")
    # the fences of the re-check: sections meet the guard in compare, a variant is not another option, an empty `theirs` is no proof, the second source ends
    import types
    VE = types.SimpleNamespace(title="Aquatic", id="ref/sorcbloodline/aquatic")
    vb = [P("title", [("Seaborn", True, False)], 72, 1, 18), P("para", [("Water Blast (Sp)", True, False), (": A bolt of water.", False, False)], 72, 1),
          P("title", [("Sage", True, False)], 72, 1, 18), P("para", [("Dull (Su)", True, False), (": Dull.", False, False)], 72, 1)]
    bk2 = types.SimpleNamespace(vocab=set())
    miss = [fp.ImportFeature("Water Blast (Sp)")]
    STOP_TITLES.clear()
    got = variant_section(vb, bk2, VE, miss, ["Water Blast (Sp)"])
    eq((got[0], got[3], got[4]), ("Seaborn", 72, True), "ruling 65: the variant is the title whose section holds the power; the page is the printed one; another title ends it")
    eq(variant_section(vb[:2], bk2, VE, miss, ["Water Blast (Sp)"])[4], False, "a variant section with no end title says so")
    STOP_TITLES.update({"seaborn"})
    eq(variant_section(vb, bk2, VE, miss, ["Water Blast (Sp)"]), None, "a title that is another option of the corpus is no variant")
    STOP_TITLES.clear()
    eq(add_sections.__defaults__ is not None, True, "add_sections takes the variants")
    cutsec = {"opening": ["Cavaliers who join. For 1"], "rows": [sect("Edicts", "Protect the faith. And", [])]}
    got2 = add_sections(EE, [], cutsec, [], [], {}, {"entry": "x", "shape": "multi", "page": "1", "note": ""}, "b", [], Counter(), [])
    eq([(r["feature"], r["status"]) for r in got2], [("(opening)", "hold"), ("Edicts", "hold")], "the completeness guard holds a cut opening and a cut section in compare")
    vr = [{"shape": "multi", "book": "ultimate-magic", "status": "print", "print": "At 3rd level, a lick.", "feature": "Envenom (Su)", "anchor": "envenom", "level": ""}]
    vv = [("ultimate-magic", "71", ("Envenomed", "Print's variant.\n\n**Envenom (Su):** At 3rd level, a lick.", {}, 71, True))]
    sec0 = lambda rows, v: [r for r in add_sections(EE, rows, {"opening": [], "rows": []}, [], [("Envenom (Su)", "s1")] if rows else [], {}, {"entry": "x", "shape": "multi", "page": "1", "note": ""}, "b", [], Counter(), v) if r["shape"] == "variant"]
    eq(sec0(vr, vv)[0]["status"], "hold", "ruling 65: a variant is held while the switch is off")
    globals()["VARIANTS_ON"] = True
    eq((sec0(vr, vv)[0]["status"], sec0([], vv)[0]["status"]), ("print", "hold"), "ruling 65: with the switch on a variant that holds its power settles; one that holds none does not (not vacuous)")
    globals()["VARIANTS_ON"] = False
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td) / "x.md"
        tp.write_text("old")
        write_atomic(tp, "new")
        eq((tp.read_text(), sorted(x.name for x in Path(td).iterdir())), ("new", ["x.md"]), "an atomic write leaves the new file and no temp file")
    # ruling 63 (review of #374): the tag is print's; a tag that print and the import both state must agree
    eq([ability_tag_pair(n, h) for n, h in (("Blinding Bomb", "Blinding Bomb (Su)"), ("Blinding Bomb (Su)", "Blinding Bomb (Su)"),
                                            ("Agony (Su)", "Agony (Ex)"), ("Agony (Su)", "Agony"), ("Plain", "Plain"))],
       [("Su", False), ("Su", False), ("Ex", True), ("Su", False), ("", False)],
       "the ability tag comes from print's head, and a disagreement holds")
    # the title of a multi-power option may carry its kind in a parenthesis (§ review of #374): only its own kind matches
    school = [P("title", [("METAL (ELEMENTAL SCHOOL)", True, False)], 87, 0, 18), P("para", [("Metal Magic: Add spells.", True, False)], 87, 0),
              P("title", [("WOOD", True, False)], 87, 1, 18), P("para", [("Wood Magic: Add spells.", True, False)], 87, 1)]
    # a class option that cites no page: its head is looked for in the whole book (one hit only)
    _pg = fp.Book({"30": 13}, {1: [(120, 108, 30, "<b>Acid Jet (Su)</b>: A jet of acid.", 300),
                                     (200, 108, 30, "<b>Arcane Barrier (Su)</b>: A barrier.", 300)]}, {1: 13}, set())
    _pg2 = fp.Book({"30": 13}, {1: [(100, 120, 30, "<b>Acid Jet (Su)</b>: A jet.", 300), (200, 120, 30, "<b>Familiar (Ex)</b>: A familiar.", 300)],
                                 2: [(100, 120, 30, "<b>Acid Jet (Su)</b>: Again.", 300), (200, 120, 30, "<b>Flame Arc (Su)</b>: A flame.", 300)]}, {1: 9, 2: 13}, set())
    _e = type("E", (), {"title": "Acid Jet", "id": "ref/exploit/acid-jet"})()
    PAGE_SEARCH["blocks"] = None
    eq(printed_page(_e, _pg), 13, "a head printed once gives its page")
    PAGE_SEARCH["blocks"] = None
    FAMILY_OF_TITLE.clear()
    eq(printed_page(_e, _pg2), None, "a head printed twice gives none when no neighbour names its list")
    FAMILY_OF_TITLE.update({"flamearc": "exploit", "familiar": "arcana"})
    eq(printed_page(_e, _pg2), 13, "the neighbouring head of the same family points to the list")
    PAGE_SEARCH["blocks"] = None
    eq(printed_page(type("E", (), {"title": "No Such", "id": "ref/exploit/x"})(), _pg), None, "a head printed nowhere gives none")
    PAGE_SEARCH["blocks"] = None
    STOP_TITLES.clear()
    STOP_TITLES.update({"metal", "wood"})
    eq(anchor_section(school, "Metal", kind="school")[1], True, "a printed title with its own kind in a parenthesis anchors the window")
    eq([q.plain()[:4] for q in anchor_section(school, "Metal", kind="school")[0]], ["Meta"], "and the window starts after it")
    eq(anchor_section(school, "Metal", kind="domain"), None, "(ELEMENTAL SCHOOL) is no title of a domain entry")
    fire = [P("title", [("FIRE (SUBDOMAIN)", True, False)], 90, 0, 18), P("para", [("Fire Domain: A rule.", True, False)], 90, 0)]
    eq(anchor_section(fire, "Fire", kind="domain"), None, "FIRE (SUBDOMAIN) is no title of the entry Fire of a domain")
    # the intro sentence of a marked head comes from the book's own intro, by the family it names
    ib = fp.Book({"30": 13, "40": 40}, {1: [(200, 108, 40, "DISCOVERIES", 100),
                              (240, 108, 30, "The following new discoveries can be taken by any alchemist who meets the prerequisites. Discoveries that modify bombs and are marked with a single asterisk (*) do not stack. Only one such discovery can be applied to an individual bomb.", 320),
                              (300, 108, 40, "Slayer", 100),
                              (320, 108, 30, "Talents marked with an asterisk add effects to a slayer's sneak attack. Only one of these talents can be applied to an individual attack.", 320)]}, {1: 15}, set())
    eq(IntroMarkMap(ib).by_family.get("discovery"), ("Discoveries that modify bombs and are marked with a single asterisk (*) do not stack. Only one such discovery can be applied to an individual bomb.", 15),
       "the intro sentence of a marked family is read from the book")
    eq(IntroMarkMap(ib).by_family.get("slayertalent"), ("Talents marked with an asterisk add effects to a slayer's sneak attack. Only one of these talents can be applied to an individual attack.", 15),
       "each family takes the intro that names it")
    nointro = fp.Book({"30": 13}, {1: [(200, 108, 30, "Plain text without a mark.", 300)]}, {1: 4}, set())
    eq(IntroMarkMap(nointro).by_family, {}, "a book with no such intro gives no sentence (near miss: a paragraph with no mark)")
    # the intro sentence of a marked head comes from the book's own intro (a fake page: the paragraph that names the mark)
    ib = fp.Book({"30": 13, "40": 40}, {1: [(200, 108, 30, "DISCOVERIES", 100), (240, 108, 30, "The following new discoveries can be taken by any alchemist who meets the prerequisites. "
                               "Discoveries that modify bombs and are marked with a single asterisk (*) do not stack. Only one such discovery can be "
                               "applied to an individual bomb.", 320),
                              (300, 108, 40, "Alchemical Simulacrum (Su)", 200)]}, {1: 15}, set())
    eq(IntroMarkMap(ib, "Discoveries that modify bombs and are marked with a single asterisk", "stack").text, "Discoveries that modify bombs and are marked with a single asterisk (*) do not stack. Only one such discovery can be applied to an individual bomb.",
       "the intro sentence of a marked group is read from the book")
    eq(IntroMarkMap(ib, "Discoveries that modify bombs and are marked with a single asterisk", "stack").page, 15, "and its printed page")
    nointro = fp.Book({"30": 13}, {1: [(200, 108, 30, "Plain text without a mark.", 300)]}, {1: 4}, set())
    eq((IntroMarkMap(nointro, "marked with an asterisk", "sneak attack").text, IntroMarkMap(nointro, "marked with an asterisk", "sneak attack").page), ("", 0), "a book with no such intro gives no sentence (near miss: a paragraph with no mark)")
    two = fp.Book({"30": 13, "40": 40}, {1: [(120, 108, 30, "Discoveries marked with a single asterisk (*) first appear in this book.", 300),
                                              (200, 108, 40, "DISCOVERIES", 100),
                                              (240, 108, 30, "The following new discoveries can be taken by any alchemist who meets the prerequisites. Discoveries that modify bombs "
                                                             "and are marked with a single asterisk (*) do not stack. Only one such discovery can be applied to an individual bomb.", 320)]},
                  {1: 15}, set())
    eq((IntroMarkMap(two, "Discoveries that modify bombs and are marked with a single asterisk", "stack").text.startswith("Discoveries that modify bombs"), IntroMarkMap(two, "Discoveries that modify bombs and are marked with a single asterisk", "stack").page), (True, 15),
       "the rule sentence is preferred over the chapter's mention of the mark")
    intro_entry = "ref/invtalent/blinding-strike"
    intro_key = ("advanced-class-guide", "invtalent")
    intro_text = ("Investigator talents marked with an asterisk (*) add effects to an investigator’s studied combat or studied strike. "
                  "Only one of these talents can be applied to an individual attack, but the decision can be made when the damage is dealt.")
    previous_intro = INTRO_MARK_TEXT.get(intro_key)
    INTRO_MARK_TEXT[intro_key] = (intro_text, 32)
    MARKED_HEAD_ENTRIES.add(intro_entry)
    refreshed_row = {"entry": intro_entry, "page": "33", "note": "", "print_sha256": ""}
    refreshed = refresh_written_proposal(HERE.parent, "advanced-class-guide", refreshed_row,
                                         "Investigator talents marked with an asterisk (*) old text.\n\nThe strike text.")
    expected_intro = intro_text.replace("(*)", r"(\*)")
    eq(refreshed, expected_intro + "\n\nThe strike text.", "a written ACG row refresh keeps the current marked intro")
    eq((refreshed_row["page"], "opens with print's sentence about the mark" in refreshed_row["note"]),
       ("32-33", True), "a written marked intro refresh also retains its page and note")
    MARKED_HEAD_ENTRIES.remove(intro_entry)
    if previous_intro is None:
        del INTRO_MARK_TEXT[intro_key]
    else:
        INTRO_MARK_TEXT[intro_key] = previous_intro
    eq(clean_full_printed_head(" While  raging, the barbarian’s  breath weapon. "),
       "While raging, the barbarian's breath weapon.", "a full-head fallback receives normal spacing and apostrophe cleanup")
    uc_book = lambda text: fp.Book({"30": 13}, {1: [(200, 108, 30, text, 320)]}, {1: 14}, set())
    expected_intros = {
        "ninjatrick": "Tricks marked with an asterisk (*) add effects to a ninja's sneak attack. Only one of these tricks can be applied to an individual attack and the decision must be made before the attack is made.",
        "talent": "Talents marked with an asterisk (*) add effects to a rogue's sneak attack. Only one of these talents can be applied to an individual attack, and the decision must be made before the roll is made.",
        "discovery": "Discoveries that modify bombs and are marked with a single asterisk (*) do not stack. Only one such discovery can be applied to an individual bomb.",
    }
    for family, expected in expected_intros.items():
        marker, prefer = INTRO_MARK_SPECS["ultimate-combat"][family]
        discovered = IntroMarkMap(uc_book(expected), marker, prefer)
        eq(discovered.text, expected, f"Ultimate Combat {family} marked-head intro equals the printed text word for word")
    ui_sentence = ("A stalker vigilante can apply only one talent marked with an asterisk (*) to a given hidden strike, and only when that hidden strike is dealt against a foe that is unaware of the stalker vigilante’s presence (or who considers him an ally), unless otherwise noted.")
    ui_intro = fp.Book({"30": 13}, {1: [(200, 108, 30, ui_sentence, 300)]}, {1: 13}, set())
    ui_marker, ui_prefer = INTRO_MARK_SPECS["ultimate-intrigue"]["vigtalent"]
    eq((IntroMarkMap(ui_intro, ui_marker, ui_prefer).text, IntroMarkMap(ui_intro, ui_marker, ui_prefer).page),
       (ui_sentence, 13), "Ultimate Intrigue p. 13: the marked-talent intro is extracted word for word")
    ui_intro_key = ("ultimate-intrigue", "vigtalent")
    previous_ui_intro = INTRO_MARK_TEXT.get(ui_intro_key)
    INTRO_MARK_TEXT[ui_intro_key] = (ui_sentence, 13)
    eq(marked_head_intro("ultimate-intrigue", "ref/vigtalent/foe-collision"),
       ui_sentence.replace("(*)", r"(\*)").replace("’", "'"), "Ultimate Intrigue marked-talent intros use straight apostrophes")
    if previous_ui_intro is None:
        del INTRO_MARK_TEXT[ui_intro_key]
    else:
        INTRO_MARK_TEXT[ui_intro_key] = previous_ui_intro
    ui_near_miss = fp.Book({"30": 13}, {1: [(200, 108, 30, "An unmarked with an asterisk phrase is not a mark rule.", 300)]}, {1: 13}, set())
    eq((IntroMarkMap(ui_near_miss, ui_marker, ui_prefer).text, IntroMarkMap(ui_near_miss, ui_marker, ui_prefer).page),
       ("", 0), "the Ultimate Intrigue intro matcher rejects a near miss inside unmarked")
    STOP_TITLES.clear()
    STOP_TITLES.update({"aquatic", "boreal", "deepearth"})
    ab = [P("title", [("Aquatic", True, False)], 136, 0, 18), P("para", [("Dehydrating Touch (Sp)", True, False), (": A touch.", False, False)], 136, 0),
          P("title", [("Boreal", True, False)], 136, 1, 18), P("para", [("Freezing Bolt (Sp)", True, False), (": A bolt.", False, False)], 136, 1)]
    eq(([q.plain()[:8] for q in anchor_section(ab, "Aquatic")[0]], anchor_section(ab, "Aquatic")[1]), (["Dehydrat"], True), "item 3: the section of an entry ends at the title of the next class option")
    eq(anchor_section(ab[2:], "Boreal")[1], False, "a window with no end title reports it")
    eq(anchor_section(ab[:2], "Aquatic")[1], False, "the last option of the pages has no end")
    eq(anchor_section(ab, "Serpentine"), None, "item 3: a title that is not printed gives no window")
    eq([q.plain()[:6] for q in anchor_section(ab, "Boreal")[0]], ["Freezi"], "item 3: the window starts at the entry's own title")
    sfx = [P("title", [("Aquatic", True, False)], 136, 0, 18), P("para", [("Dehydrating Touch (Sp)", True, False), (": A touch.", False, False)], 136, 0),
           P("title", [("Boreal Bloodline", True, False)], 136, 1, 18), P("para", [("Freezing Bolt (Sp)", True, False), (": A bolt.", False, False)], 136, 1)]
    eq(anchor_section(sfx, "Aquatic"), ([sfx[1]], True), "a neighbour title with the suffix bloodline ends the window")
    bh = [sfx[0], sfx[1], P("para", [("Boreal Bloodline", True, False), (": Cold.", False, False)], 136, 1), sfx[3]]
    eq(anchor_section(bh, "Aquatic"), ([bh[1]], True), "a neighbour set as a bold head with the suffix ends the window")
    STOP_TITLES.add("dehydratingtouch")
    eq(anchor_section(ab[:1] + [P("para", [("Dehydrating Touch (Sp)", True, False), (": A touch.", False, False)], 136, 0)] + ab[2:], "Aquatic", {"dehydratingtouch"})[1], True, "an own power name is no neighbour")
    eq(anchor_section([ab[0], P("title", [("Dehydrating Touch", True, False)], 136, 0, 18)] + ab[2:], "Aquatic", {"dehydratingtouch"})[0][0].plain(), "Dehydrating Touch", "an own power name does not end the window (a title of another option with the name of a power)")
    STOP_TITLES.discard("dehydratingtouch")
    STOP_TITLES.clear()
    mr = [{"status": "print", "note": ""}, {"status": "draft", "note": "x"}]
    globals()["MULTI_FENCE"] = True
    eq([r["status"] for r in fence([dict(r) for r in mr], "multi")], ["hold", "hold"], "the fence holds every row of a multi-power entry")
    eq([r["status"] for r in fence([dict(r) for r in mr], "single")], ["print", "draft"], "the fence leaves a single power")
    eq(fence([dict(mr[0])], "multi")[0]["note"], "multi-power window not anchored yet", "the fence says why")
    globals()["MULTI_FENCE"] = False
    DECISIONS.clear()
    DECISIONS[("ref/x/multi", "power")] = ("hold", "multi-power: separate reviewed batch")
    md = apply_multi_decisions([{"anchor": "power", "status": "print", "note": "printed"}, {"anchor": "power", "status": "draft", "note": ""}], "ref/x/multi")
    eq([(x["status"], x["note"]) for x in md], [("hold", "printed; held by decision: multi-power: separate reviewed batch"),
                                                   ("hold", "held by decision: multi-power: separate reviewed batch")],
       "a multi-power hold applies to added rows with the same anchor")
    eq(apply_multi_decisions([{"anchor": "other", "status": "print", "note": ""}], "ref/x/multi")[0]["status"], "print",
       "a multi-power decision does not hold a different anchor")
    DECISIONS.clear()
    eq(HEADING_FAMILIES, {"evolution"}, "the group-heading rule is on with the per-book map")
    # an import label row inside a power's span is part of the draft: print without it holds, print with it agrees (never dropped silently)
    inner = "**Gift (Su)**\n\n**Ability:** A gift of sight.\n\n**Details:** Gorum guards it.\n"
    _, ff = fp.parse_import(inner, set())
    dd = fp.build_draft(ff[0])
    eq((fp.compare_feature(dd, "A gift of sight.", set(), set()).status, fp.compare_feature(dd, "A gift of sight. Gorum guards it.", set(), set()).status), ("hold", "draft"),
       "a label row inside a power's span holds when print lacks it")
    eq([paragraph_complete(x) for x in ("A cry. For 1", "A cry that all allies hear.", "He said \u201cyes.\u201d", "A bonus (see text.)", "It grants _haste._", "It uses [fireball](ref/spell/fireball).",
                                        "The following:", "- one\n- two", "| a | b |", "1. one", "A cry,")],
       [False, True, True, True, True, True, True, True, True, True, False], "the completeness guard: a cut paragraph, a closing quote or parenthesis, a link at the end, a list, a table row")
    eq((incomplete_paragraph("A whole.\n\nCut here"), incomplete_paragraph("A whole.\n\nAnother whole.")), ("Cut here", ""), "the guard names the end of the paragraph that is cut")
    single = "\n**Animal Fury (Ex)**\n\n**Ability:** A bite attack.\n\n**Special:** A grapple.\n"
    multi = ("\n**Deities**\n\n**Details:** Gorum.\n\n### Revelations\n\nAn oracle can choose from the following.\n\n"
             "**Battlecry (Ex)**\n\n**Standard:** A cry.\n\n**Usage:** 1 time/day\n\n**At 10th level,** more.\n\n"
             "**Clarity (Ex)**\n\n**Immediate:** A reroll.\n")
    none = "\nA kinetic talent prints a stat line.\n\nBurn: 1\n"
    eq(shape_of(single), ("single", 1), "a single-power option")
    eq(shape_of(multi), ("multi", 2), "a multi-power option under a section")
    eq(shape_of(none), ("none", 0), "an option without import rows")
    eq(shape_of("\n## Battlecry (Ex) {#battlecry}\n\nAt 1st level, a cry.\n")[0], "none", "a converted entry has no import row")

    def sha(body, i):
        blocks = rw.parse_blocks(body.split("\n"))
        c = rw.candidates(blocks, True)[i]
        return rw.span_sha(blocks[c.start:c.end])

    class E:                              # the fields `convert_body` reads
        body = single
    tabbody = "\n**Gift (Ex)**\n\n**Ability:** A gift.\n\n|A|B|\n| --- | --- |\n|1|2|\n"
    class ET:
        body = tabbody
    tb, _ = convert_body(ET, {sha(tabbody, 0): "A gift.\n\n|A|B|\n| --- | --- |\n|1|2|"}, {}, {})
    eq(tb.count("|A|B|"), 1, "ruling 62: a table that the written text holds is not kept twice")
    body, feats = convert_body(E, {sha(single, 0): "At 1st level, a bite."}, {}, {})
    eq(body.strip(), "At 1st level, a bite.", "a single-power body is the printed paragraphs, no head, no features")
    eq(feats, [], "a single-power option gets no `features`")
    duplicate = "- **Blast Lock:** The gunslinger makes an attack roll against a lock with enough detail to cross the threshold and be an exact duplicate of the text that print supplies."
    printed = "_Blast Lock_: The gunslinger makes an attack roll against a lock with enough detail to cross the threshold and be an exact duplicate of the text that print supplies."
    eq(duplicate_print_block(duplicate, prose_key(printed)), True, "a single-power writer drops a duplicated imported list item")
    eq((duplicate_print_block("a" * 79, "a" * 100), duplicate_print_block("b" * 80, "a" * 100)),
       (False, False), "duplicate imported blocks need 80 characters and must occur in print")
    eq((written_tag_error("ref/x/y", "Su", "Su"), written_tag_error("ref/x/y", "Su", "")),
       (None, "ref/x/y: ability_type '' differs from the printed tag 'Su'"), "run_check requires exact printed ability_tag equality")
    E.body = multi
    texts = {sha(multi, 0): "A cry that all allies hear.", sha(multi, 1): "At 7th level, a reroll."}
    levels = {sha(multi, 0): None, sha(multi, 1): 7}
    anchors = {sha(multi, 0): "battlecry", sha(multi, 1): "clarity"}
    body, feats = convert_body(E, texts, levels, anchors)
    eq("#### Battlecry (Ex) {#battlecry}" in body and "#### Clarity (Ex) {#clarity}" in body, True, "heads are one level below the section heading")
    eq(feats, [("battlecry", None), ("clarity", 7)], "the features of a multi-power option, with a level only when print gives it")
    eq("**Deities**" in body and "### Revelations" in body, True, "the blocks that are no power stay")
    eq(rw.entry_in_scope(body.split("\n")), False, "a converted body has no import row")
    front = 'id = "ref/mystery/battle"\n[fields]\nkind = "class_option"\ngroup = "oracle-mystery"\n'
    eq(features_front(front, feats).split("\n")[4:8], ["features = [", '  { anchor = "battlecry" },', '  { anchor = "clarity", level = 7 },', "]"],
       "`features` follow `group`")
    rows = [{"entry": "ref/x/a", "verdict": "agree", "status": "draft", "note": ""}, {"entry": "ref/x/b", "verdict": "hold", "status": "hold", "note": "resolution of #537: Book p. 1"}]
    out = report(rows, {"single": 2, "multi": 0, "none": 1, "none_by_family": Counter({"talent": 1})})
    eq("entries with a hold: 1 of 2" in out and "reach these powers: 1" in out and "talent 1" in out, True, "the report counts holds, resolutions and the options without import rows")
    eq(level_of("At 7th level, a reroll."), 7, "the level of a printed lead")
    eq(level_of("Once per day, a reroll."), None, "no printed lead, no level")
    # ruling 63, the ledger, the shape path, the heading levels
    eq([ability_tag_of(n) for n in ("Agony (Su)", "Foo (Ex or Sp)", "Bar (Su, Sp)", "Plain", "Note (see text)")], ["Su", "Ex or Sp", "Su, Sp", "", ""], "the printed ability tag")
    eq(with_ability_type('id = "x"\n[fields]\nkind = "class_option"\ngroup = "hex"\nfeatures = [\n]\n', "Su"), 'id = "x"\n[fields]\nkind = "class_option"\ngroup = "hex"\nability_type = "Su"\nfeatures = [\n]\n', "ruling 63: the key follows group")
    eq(with_ability_type('[fields]\nkind = "class_option"\ngroup = "hex"', "Ex or Sp"), '[fields]\nkind = "class_option"\ngroup = "hex"\nability_type = "Ex or Sp"\n', "ruling 63: a combined tag, a front that ends at group")
    eq(with_ability_type('[fields]\nkind = "class_option"\ngroup = "hex"\n', ""), '[fields]\nkind = "class_option"\ngroup = "hex"\n', "ruling 63: an entry whose print has no tag gets no key")
    eq(with_ability_type('[fields]\nkind = "class_option"\ngroup = "hex"\nability_type = "Ex"\n', ""), '[fields]\nkind = "class_option"\ngroup = "hex"\n', "ruling 63: an unprinted imported tag is removed")
    eq(with_ability_type('[fields]\nkind = "class_option"\ngroup = "hex"\nability_type = "Ex"\n\n', ""), '[fields]\nkind = "class_option"\ngroup = "hex"\n', "removing a stale tag leaves canonical front matter spacing")
    eq([with_ability_type('[fields]\nkind = "class_option"\ngroup = "hex"\n', x) for x in ("su", " Su", "(Su)", "see text")] == ['[fields]\nkind = "class_option"\ngroup = "hex"\n'] * 4, True, "ruling 63: a value that is no printed tag fails the same rule as the app's")
    eq(with_ability_type('[fields]\nkind = "archetype"\ngroup = "x"\n', "Su"), '[fields]\nkind = "archetype"\ngroup = "x"\n', "ruling 63: only on a class option")
    eq([ability_tag_of(n) for n in ("Foo (su)", "Foo (Su, Sp)", "Foo (Ex, or Sp)", "Foo (Ex/Sp)", "Foo (Ex and Su)")], ["", "Su, Sp", "Ex, or Sp", "", "Ex and Su"], "ruling 63: the separators of the app's rule")
    eq([ability_tag_of_printed_head(n) for n in ("Blast Bomb* (Ex)", "Blast Bomb (Ex)*", "Blast Bomb (Ex)†", "Blast Bomb (ex)*", "Blast Bomb (Explanatory)*", "Blast Bomb (Ex/Sp)*", "Blast Bomb*")], ["Ex", "Ex", "Ex", "", "", "", ""], "source marks never strip a printed ability tag; malformed near misses stay untagged")
    eq((ability_tag_for_option("ultimate-combat", "Foo (Ex)", "Foo (Su)"), ability_tag_for_option("ultimate-combat", "Foo (Ex)", "Foo"), ability_tag_for_option("advanced-players-guide", "Foo (Ex)", "Foo"), ability_tag_for_option("ultimate-intrigue", "Foo", "Foo (Su)")), (("Su", True), ("", False), ("Ex", False), ("Su", False)), "Ultimate Combat and Intrigue take tags from print; established behavior for other books stays")
    eq(prepend_intro("The power text.", "Printed intro."), "Printed intro.\n\nThe power text.", "a marked-head intro opens the entry")
    eq(prepend_intro("Printed intro.\n\nThe power text.", "Printed intro."), "Printed intro.\n\nThe power text.", "a marked-head intro is idempotent")
    eq(prepend_intro("Marked with *\n\nThe power text.", r"Marked with \*"), r"Marked with \*" + "\n\nThe power text.", "a marked-head intro escapes and replaces the unescaped near miss")
    eq(drop_unkeyed_link_marks("ref/ragepower/greater-ground-breaker", r"[ground breaker](ref/ragepower/ground-breaker)\*\* rage power"),
       "[ground breaker](ref/ragepower/ground-breaker) rage power", "an unkeyed double mark after a link is dropped")
    eq(drop_unkeyed_link_marks("ref/ragepower/greater-ground-breaker", r"[ground breaker](ref/ragepower/ground-breaker)\* key"),
       r"[ground breaker](ref/ragepower/ground-breaker)\* key", "a near miss with one marked star is preserved")
    INTRO_MARK_TEXT[("ultimate-combat", "discovery")] = (IntroMarkMap(ib, "Discoveries that modify bombs and are marked with a single asterisk", "stack").text, IntroMarkMap(ib, "Discoveries that modify bombs and are marked with a single asterisk", "stack").page)
    eq(marked_head_intro("ultimate-combat", "ref/discovery/breath-weapon-bomb").startswith("Discoveries that modify bombs"), True, "the bomb-mark key is scoped to the printed discovery")
    eq(marked_head_intro("advanced-players-guide", "ref/discovery/breath-weapon-bomb"), "", "a marked-head intro never changes another book")
    eq(with_ability_type('[fields]\nkind = "class_option"\nability_type = "Ex"\n', "Su"), '[fields]\nkind = "class_option"\nability_type = "Ex"\n', "ruling 63: a key that is there stays")
    eq(WRITE_ABILITY_TYPE, True, "ruling 63: the writer is on, the app reads the key")
    eq(outside_rows(multi), ["Details"], "the import rows outside the powers are listed")
    eq(outside_rows(single), [], "a single power has no row outside")
    eq(bool(TRADE_LABEL.search("**Replaces:** a thing\n")), True, "a trade row is found")
    sec = "\n**Bloodline Arcana**\n\n**Passive:** A bonus.\n\n### Bloodline Powers\n\n**Touch (Su)**\n\n**Standard:** A touch.\n\n### Final Revelation\n\n**Final Revelation (Su)**\n\n**Passive:** At 20th level, more.\n"
    bl = rw.parse_blocks(sec.split("\n"))
    cs = rw.candidates(bl, True)
    eq(sorted(v[1] for v in promoted(bl, cs).values()), ["sec-final-revelation"], "a heading over a power of its own name is promoted, its key written out")
    def shas(body):
        b2 = rw.parse_blocks(body.split("\n"))
        return [rw.span_sha(b2[c.start:c.end]) for c in rw.candidates(b2, True)]
    s3 = shas(sec)
    class E2:
        body = sec
    body3, f3 = convert_body(E2, {s3[0]: "A bonus.", s3[1]: "A touch.", s3[2]: "At 20th level, more."}, {s3[2]: 20},
                             {s3[0]: "bloodline-arcana", s3[1]: "touch", s3[2]: "sec-final-revelation"})
    eq("### Bloodline Arcana {#bloodline-arcana}" in body3 and "#### Touch (Su) {#touch}" in body3, True, "a power before the first section takes the section's level")
    eq("### Final Revelation (Su) {#sec-final-revelation}" in body3 and "### Final Revelation\n" not in body3, True, "the Final Revelation heading is the head of the power")
    eq(heading_keys(sec) <= heading_keys(body3), True, "the keys of the headings stay (the promoted one by its written, derived key)")
    one = "\n### Special\n\n**Gift (Su)**\n\n**Ability:** A gift.\n"
    class E3:
        body = one
    body4, f4 = convert_body(E3, {shas(one)[0]: "A gift."}, {}, {}, "single")
    eq((f4, "####" in body4, "### Special" in body4), ([], False, True), "one power under a heading is the single-power form: no head, no features")
    eq(place_links("The eidolon must have the claws evolution.", [("claws", "ref/evolution/claws")]),
       ("The eidolon must have the [claws](ref/evolution/claws) evolution.", []), "ruling 60: the item is linked in print's sentence")
    eq(place_links("It has [claws](ref/evolution/claws). The eidolon must possess the claws evolution to select this evolution.", [("claws", "ref/evolution/claws")]),
       ("It has [claws](ref/evolution/claws). The eidolon must possess the [claws](ref/evolution/claws) evolution to select this evolution.", []),
       "ruling 60: the prerequisite sentence links the item even when the text links it earlier")
    eq(place_links("It needs the tail evolution to take this evolution. It needs an equal number of the tail evolution.", [("tail", "ref/evolution/tail")])[0],
       "It needs the [tail](ref/evolution/tail) evolution to take this evolution. It needs an equal number of the [tail](ref/evolution/tail) evolution.", "ruling 60: every plain mention of the option is linked")
    eq(place_links("It has a [tail slap attack](ref/umr/natural-attacks). It needs the tail evolution to take this evolution.", [("tail", "ref/evolution/tail")])[0],
       "It has a [tail slap attack](ref/umr/natural-attacks). It needs the [tail](ref/evolution/tail) evolution to take this evolution.", "a link of another rule stays")
    eq(place_links("It has [claws](ref/evolution/claws).", [("claws", "ref/evolution/claws"), ("tail", "ref/evolution/tail")]),
       ("It has [claws](ref/evolution/claws).", ["tail"]), "ruling 60: an item that stands nowhere is reported")
    eq(link_intrigue_class_prerequisites("Only a stalker vigilante can select this talent."),
       "Only a [stalker vigilante](ref/class/vigilante#stalker) can select this talent.",
       "Ultimate Intrigue: a printed specialization prerequisite links to that specialization")
    eq(link_intrigue_class_prerequisites("Only an avenger vigilante can select this talent."),
       "Only an [avenger vigilante](ref/class/vigilante#avenger) can select this talent.",
       "Ultimate Intrigue: the other printed specialization prerequisite links to its specialization")
    eq(link_intrigue_class_prerequisites("A vigilante must be at least 3rd level."),
       "A [vigilante](ref/class/vigilante) must be at least 3rd level.",
       "Ultimate Intrigue: a printed level prerequisite links to the class")
    eq(link_intrigue_class_prerequisites("A stalker vigilante can use this ability."),
       "A stalker vigilante can use this ability.",
       "Ultimate Intrigue: an ordinary class reference is not treated as a prerequisite")
    eq(repair_intrigue_italic_link_boundary("_[deathwatch](ref/spell/deathwatch)_, __ a caster level check"),
       "_[deathwatch](ref/spell/deathwatch),_ a caster level check",
       "Ultimate Intrigue: a link does not split the printed italic comma")
    eq(repair_intrigue_italic_link_boundary("_[deathwatch](ref/spell/deathwatch)_, __ not a caster level check"),
       "_[deathwatch](ref/spell/deathwatch)_, __ not a caster level check",
       "Ultimate Intrigue: italic repair does not rewrite unrelated text")
    eq(repair_intrigue_italic_link_boundary("_[discern lies](ref/spell/discern-lies)_, __ and he can say it"),
       "_[discern lies](ref/spell/discern-lies)_, and he can say it",
       "Ultimate Intrigue p. 13: linked italic punctuation has no empty bold run")
    eq(repair_intrigue_italic_link_boundary("_[discern lies](ref/spell/discern-lies)_, __ and she can say it"),
       "_[discern lies](ref/spell/discern-lies)_, __ and she can say it",
       "Ultimate Intrigue: italic repair leaves a near miss unchanged")
    # ruling 52, as narrowed by the review of #373: another class's option may be linked on purpose; a link is wrong only when
    # print's own noun or class disagrees with the target (print says "deed" and the target is a hex)
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        for rel, kind, group in (("swashdeed/derring-do", "class_option", "swashbuckler-deed"),
                                 ("swashdeed/opportune-parry-and-riposte", "class_option", "swashbuckler-deed"),
                                 ("hex/cackle", "class_option", "witch-hex"),
                                 ("invtalent/item-lore", "class_option", "investigator-talent"),
                                 ("invtalent/tenacious-inspiration", "class_option", "investigator-talent"),
                                 ("discovery/inspiring-cognatogen", "class_option", "alchemist-discovery"),
                                 ("spell/fireball", "spell", ""),
                                 ("spell/spell-resistance", "spell", "")):
            f = root / "entries" / (rel + ".md")
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(f'id = "ref/{rel}"\nkind = "{kind}"\n[fields]\nkind = "{kind}"\ngroup = "{group}"\n\n+++\n\nText.\n', encoding="utf-8")
        old_root = CORPUS_ROOT
        CORPUS_ROOT = root
        GROUP_OF_TARGET.clear()
        eq(link_kind_mismatches("A magus gains the [derring-do](ref/swashdeed/derring-do) and [opportune parry and riposte](ref/swashdeed/opportune-parry-and-riposte) deeds from the swashbuckler's list of deeds."), [],
           "ruling 52: the deeds of a printed list, named by print as deeds, agree (a cross-group link is no error)")
        eq(link_kind_mismatches("A shaman cannot select both this hex and the witch's [cackle](ref/hex/cackle) hex."), [],
           "ruling 52: another class's hex linked where print says hex agrees")
        eq(link_kind_mismatches("It grants the effects of the [item lore](ref/invtalent/item-lore), [tenacious inspiration](ref/invtalent/tenacious-inspiration) investigator talents."), [],
           "ruling 52: print's class and noun agree across a list")
        eq(link_kind_mismatches("The alchemist's [inspiring cognatogen](ref/discovery/inspiring-cognatogen) now grants a bonus and the item lore talents."), [],
           "ruling 52: a name whose noun comes in another clause attaches no noun (near miss: talents belong to the later item)")
        eq(link_kind_mismatches("The slayer gains a bonus, while the [item lore](ref/invtalent/item-lore) talent remains available."), [],
           "ruling 52: a class named in another clause does not govern the linked option")
        eq(link_kind_mismatches("It grants the effects of the [item lore](ref/invtalent/item-lore) judgment."),
           [("item lore", "ref/invtalent/item-lore", "investigator-talent", "judgment")],
           "ruling 52: print says judgment and the target is an investigator talent (the wrong-name case of the review)")
        eq(link_kind_mismatches("The following [cackle](ref/hex/cackle) deeds can be selected."),
           [("cackle", "ref/hex/cackle", "witch-hex", "deed")], "ruling 52: print says deed and the target is a hex")
        eq(link_kind_mismatches("The slayer gains the [item lore](ref/invtalent/item-lore) talent."),
           [("item lore", "ref/invtalent/item-lore", "investigator-talent", "class investigator")],
           "ruling 52: print names the slayer and the target is an investigator talent")
        eq(link_kind_mismatches("It is a [fireball](ref/spell/fireball) spell."), [], "ruling 52: a spell keeps its link (near miss: not a class option)")
        eq(link_kind_mismatches("The arcanist uses the [spell resistance](ref/spell/spell-resistance) exploit."),
           [("spell resistance", "ref/spell/spell-resistance", "spell", "exploit")],
           "ruling 52: an option noun cannot point at a non-option target")
        eq(link_kind_mismatches("It names [x](ref/hex/missing)."), [], "ruling 52: a target the tree lacks keeps its link (near miss: no front matter)")
        eq(link_kind_mismatches("The [cackle](ref/hex/cackle) hex."), [], "ruling 52: no class named, the noun agrees")
        eq(print_decision_may_settle(["tag differs"], [], {"notes": []}), True, "a reviewed print decision can settle a tag disagreement")
        hard_rows = (
            ("cut", {"entry": "ref/exploit/acid-jet", "status": "hold", "notes": ["print text may be cut at a page or column break: ..."]}),
            ("anchor collision", {"entry": "ref/exploit/arcane-weapon", "status": "hold", "notes": ["anchor collision: acid-jet"]}),
            ("name mismatch", {"entry": "ref/exploit/consume-magic-items", "status": "hold", "notes": ["the power's name differs from the title of the entry"]}),
            ("link mismatch", {"entry": "ref/exploit/spell-resistance", "status": "hold", "notes": ["ruling 52: spell resistance names a spell but print says exploit"]}),
            ("missing group heading", {"entry": "ref/evolution/acid", "status": "hold", "notes": ["no group heading found above the head"]}),
            ("second-source window", {"entry": "ref/exploit/acid-jet", "status": "hold", "notes": ["the second-source window has no end title: the text may run into another option"]}),
        )
        for hard_reason, row in hard_rows:
            eq(print_decision_may_settle(["tag differs"], [], row), False,
               f"a print decision cannot clear the {hard_reason} hard-hold row")
        CORPUS_ROOT = old_root
        GROUP_OF_TARGET.clear()
    for line in bad:
        print("FAIL", line)
    eq(print_lost("Whenever she uses it, she can invoke true judgment on a foe. Regardless of whether the save is made, the target is immune for 24 hours.", "Whenever she uses it, she can invoke true judgment on a foe."),
       ["Regardless of whether the save is made, the target is immune for 24 hours."], "the coverage check names a printed sentence that the written text lacks")
    eq(print_lost("The alchemist can brew an elixir of life once per day at sixteenth level.", "An elixir of life: the alchemist can brew once. The alchemist has per day sixteenth level."),
       ["The alchemist can brew an elixir of life once per day at sixteenth level."], "a sentence whose words stand elsewhere in the text is still lost")
    eq(print_lost("While this deed is active, you gain a +2 dodge bonus to AC against attacks of opportunity made by any creature that you threaten.", "While this deed is active, you gain a +3 dodge bonus to AC against attacks of opportunity made by any creature that you threaten."),
       ["While this deed is active, you gain a +2 dodge bonus to AC against attacks of opportunity made by any creature that you threaten."], "a changed digit is a loss")
    eq(print_lost("The creature can be affected by this spell if it fails the save against the effect.", "The creature cannot be affected by this spell if it fails the save against the effect."),
       ["The creature can be affected by this spell if it fails the save against the effect."], "a negation that differs is a loss")
    eq(NEGATIONS.findall("The creature isn’t affected by this spell."), ["n’t"], "the curly apostrophe in n’t is a negation")
    eq(print_lost("While raging and mounted, the barbarian's mount gains the trample special attack (Pathfinder RPG Bestiary 305).", "While raging and mounted, the barbarian's mount gains the [trample](ref/umr/trample) special attack."), [],
       "ruling 26: a citation of a book and a page goes where a link stands")
    eq(print_lost("While raging and mounted, the barbarian's mount gains the trample special attack (Pathfinder RPG Bestiary 305).", "While raging and mounted, the barbarian's mount gains the trample special attack."),
       ["While raging and mounted, the barbarian's mount gains the trample special attack (Pathfinder RPG Bestiary 305)."], "a citation with no link in its place is a loss")
    eq(print_lost("While raging and mounted, the barbarian's mount gains the trample special attack (Pathfinder RPG Bestiary 305).", "While raging and mounted, the barbarian's mount gains the [trample](ref/umr/trample) special attack (Pathfinder RPG Bestiary 306)."),
       ["While raging and mounted, the barbarian's mount gains the trample special attack (Pathfinder RPG Bestiary 305)."], "a citation with another page is no match")
    eq(print_lost("The barbarian can make an overrun attempt against any creature that she charges at the end of her move, as a free action (Core Rulebook 443).",
                  "The [barbarian](ref/class/barbarian) can make an overrun attempt against any creature that she charges at the end of her move, as a free action."),
       ["The barbarian can make an overrun attempt against any creature that she charges at the end of her move, as a free action (Core Rulebook 443)."],
       "a link far from the citation does not take it")
    eq(print_lost("The target is sickened for 1 round per level (DC 15) of the caster.", "The target is sickened for 1 round per level of the caster."), ["The target is sickened for 1 round per level (DC 15) of the caster."], "(DC 15) is no citation")
    eq(print_lost("The target is [sickened](ref/misc/sickened) for 1 round per level (Wisdom 13) of the caster.", "The target is sickened for 1 round per level of the caster."),
       ["The target is [sickened](ref/misc/sickened) for 1 round per level (Wisdom 13) of the caster."], "(Wisdom 13) is no citation")
    # the exact rules: signs, separators, digit edges, word identity
    base = "The creature takes a {} penalty on all saving throws made against effects that the caster creates with this spell."
    for old, new, what in (("+2", "-2", "a sign"), ("1/2", "12", "a slash"), ("1,000", "10,00", "a comma"), ("5", "15", "a digit edge")):
        eq(print_lost(base.format(old), base.format(new)), [base.format(old)], f"the numbers are compared as tokens: {what} differs")
    eq(print_lost("A creature of DC 1 or lower is not affected by this ability of the witch or any other creature of the kind.", "A creature of DC 15 or lower is not affected by this ability of the witch or any other creature of the kind."),
       ["A creature of DC 1 or lower is not affected by this ability of the witch or any other creature of the kind."], "DC 1 is not DC 15")
    swap = "The antipaladin can use this ability on {} creature within sight of the weapon that the spirit has made for him."
    for old, new in (("his", "her"), ("any", "all"), ("able", "unable"), ("valid", "invalid"), ("aware", "unaware"), ("may", "can")):
        eq(print_lost(swap.format(old), swap.format(new)), [swap.format(old)], f"a word of another identity is a loss: {old}/{new}")
    near = "The antipaladin can use this ability to {} the bonus of the weapon that the spirit has made for him."
    for old, new in (("increase", "decrease"), ("minimum", "maximum"), ("unable", "enable"), ("either", "neither")):
        eq(print_lost(near.format(old), near.format(new)), [near.format(old)], f"a near-antonym is a loss, not a misprint: {old}/{new}")
    for old, new in (("elixer", "elixir"), ("anitpaladin", "antipaladin"), ("weaopn", "weapon")):
        eq(print_lost(near.format(old), near.format(new)), [], f"one misprint inside a word is no loss: {old}/{new}")
    eq(print_lost("She can strike the foe, or she can flee from the field of battle at once.", "She can strike the foe, nor she can flee from the field of battle at once."),
       ["She can strike the foe, or she can flee from the field of battle at once."], "nor is a negation")
    eq(print_lost("She can use either of the two weapons that she holds in her hands at any time.", "She can use neither of the two weapons that she holds in her hands at any time."),
       ["She can use either of the two weapons that she holds in her hands at any time."], "neither is a negation")
    eq([one_misprint("minimum", "maximum"), one_misprint("increase", "decrease"), one_misprint("either", "neither"), one_misprint("elixer", "elixir"), one_misprint("anitpaladin", "antipaladin"),
        one_misprint("weapon", "weapons")], [False, False, False, True, True, True], "one misprint: a letter, a swap, a letter more or less; never the first letter or two letters inside")
    eq(print_lost("The antipaladin can use this ability on an anitpaladin within sight of the weapon that the spirit has made for him.", "The antipaladin can use this ability on an antipaladin within sight of the weapon that the spirit has made for him."), [],
       "a misprint of two letters in a long word is no loss")
    ligature = [("a Reflex save (DC = 10 + 1/2 the alchemist's level + the alchemist's Intelligent modifier) halves the damage.", "a Reflex save (DC = 10 + 1/2 the alchemist's level + the alchemist's Intelligence modifier) halves the damage.")]
    eq(print_lost("Each creature takes damage, but succeeding at a Ref lex save (DC = 10 + 1/2 the alchemist's level + the alchemist's Intelligent modifier) halves the damage.",
                  "Each creature takes damage, but succeeding at a Reflex save (DC = 10 + 1/2 the alchemist's level + the alchemist's Intelligence modifier) halves the damage.", ligature), [],
       "a correction of the errata file is found in the printed text up to the breaks that the layer sets inside a word")
    fixes = [("she can attempt to save again again 1 round later at the same DC.", "she can attempt to save again 1 round later at the same DC.")]
    eq(print_lost("If she fails a saving throw against an illusion that is not to disbelieve, she can attempt to save again again 1 round later at the same DC.",
                  "If she fails a saving throw against an illusion that is not to disbelieve, she can attempt to save again 1 round later at the same DC.", fixes), [], "a misprint that the errata file corrects is no loss")
    eq(print_lost("If she fails a saving throw against an illusion that is not to disbelieve, she can attempt to save again again 1 round later at the same DC.",
                  "If she fails a saving throw against an illusion that is not to detect, she can attempt to save again 1 round later at the same DC.", fixes),
       ["If she fails a saving throw against an illusion that is not to disbelieve, she can attempt to save again 1 round later at the same DC."], "the fix applies and another word changes too: the sentence is a loss")
    eq(print_lost("If she fails a saving throw against an illusion that is not to disbelieve, she can attempt to save again again 2 rounds later at the same DC.",
                  "If she fails a saving throw against an illusion that is not to disbelieve, she can attempt to save again 1 round later at the same DC.", fixes),
       ["If she fails a saving throw against an illusion that is not to disbelieve, she can attempt to save again again 2 rounds later at the same DC."], "the correction does not cover another change")
    eq(print_lost("The creature can see the fiendish light that shines from the weapon of the antipaladin.", "The creature can hear the fiendish light that shines from the weapon of the antipaladin."),
       ["The creature can see the fiendish light that shines from the weapon of the antipaladin."], "one swapped word in a long sentence is a loss")
    eq(print_lost("The creature regains the use of its class (see the atonement spell) after a week of prayer.", "The creature regains the use of its class after a week of prayer."), [], "a short cross-reference is no difference")
    eq(print_lost("The creature regains the use of its class (but only in daylight) after a week of prayer.", "The creature regains the use of its class after a week of prayer."),
       ["The creature regains the use of its class (but only in daylight) after a week of prayer."], "another parenthetical is text")
    eq(print_lost("The alchemist can brew an elixer of life once per day at sixteenth level.", "The alchemist can brew an elixir of life once per day at sixteenth level."), [], "a letter differs: the sentence is there")
    eq(print_lost("This ability 4 4 3 3 is the equivalent of a spell of a level equal to one-third the level.", "This ability is the equivalent of a spell of a level equal to one-third the level."), [], "cells inside a printed sentence are no words of it")
    eq(print_lost("(Su): The witch can create a magic sensor that she can see through.", "The [witch](ref/x) can create a magic sensor that she can see through."), [], "the tag of a head and a link are not differences")
    eq([bool(TABLE_HEAD_RE.match(x)) for x in ("1st 2nd 3rd 4th", "0 1st 2nd 3rd", "Spells per Day", "Extracts per Day", "2-Point Evolutions", "3rd-Level Spells", "1st-Level Witch Spells", "1 Point Evolutions", "4th Level")],
       [True, True, True, True, False, False, False, False, False], "the header of a class table is no head; a group heading that starts with a number or an ordinal is (near misses)")
    for line in bad:
        print("FAIL", line)
    print(f"self-test: {ok} checks passed" if not bad else f"self-test: {len(bad)} failures")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(HERE.parent))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--headings", action="store_true", help="ruling 61: put the printed group heading in the converted evolution entries")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--audit", action="store_true", help="the print-coverage check over the written class options of --book (read only)")
    ap.add_argument("--neighbours", action="store_true", help="a report before a book batch: for each multi-power entry, the printed titles and heads its window holds that are not its own, and whether it found an end (needs --book, --books, --cache)")
    ap.add_argument("--variants", action="store_true", help="ruling 65: settle variant sections (held by default until a reviewer has read the first settled one)")
    ap.add_argument("--ability-type", action="store_true", help="ruling 63: write ability_type for the written single-power entries (off until the app reads the key)")
    ap.add_argument("--checker", help="the cast-iron-corpus binary: `--write` runs its `fmt` afterwards")
    ap.add_argument("--book")
    ap.add_argument("--families")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.audit:
        return run_audit(args)
    if args.compare:
        return run_compare(args)
    if args.variants:
        global VARIANTS_ON
        VARIANTS_ON = True
    if args.neighbours:
        return run_neighbours(args)
    if args.ability_type:
        return run_ability_type(args)
    if args.headings:
        return run_headings(args)
    if args.write:
        return run_write(args)
    if args.check:
        return run_check(args)
    ap.error("one of --self-test, --compare, --write, --check")


if __name__ == "__main__":
    sys.exit(main())
