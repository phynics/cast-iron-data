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
import difflib
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


NUMERIC = re.compile(r"^(?:[+\-\u2013\u2014]?\d+(?:/[+\-\u2013\u2014]?\d+)*(?:st|nd|rd|th)?|[\u2014\u2013-]|\+\d+)[,.]?$")


def is_table_para(text: str) -> bool:
    """A paragraph that is the cells of a class table: most of its words are numbers, dashes or ordinals, or it is the header row of the table (Fort, Ref and
    Will saves). Print sets the class table in the middle of the text and the reader makes paragraphs of the cells."""
    toks = text.split()
    if len(toks) >= 4 and re.search(r"\bFort\b.*\bRef(?:lex)?\b.*\bWill\b", text):
        return True
    if re.search(r"\d\s*\+\s*\d+\s+per\s+\w+|\bper\s+\d+\s+levels?\b", text):
        return False                                      # "1 + 1 per 3 levels": a progression in a sentence, not cells
    if re.fullmatch(r"\s*(?:spells|extracts|formulae)\s+(?:per\s+day|known)\s*", text, re.I):
        return True                                       # the title of the spell columns of a class table
    if len(toks) >= 3 and all(NUMERIC.match(x) for x in toks):
        return True                                       # "1st 2nd 3rd 4th": the ordinals over the columns
    return len(toks) >= 5 and sum(bool(NUMERIC.match(x)) for x in toks) / len(toks) >= 0.5


def section_behind(blocks: list, win: list, lacking: set[str]) -> list:
    """The sections that follow the class features in print under a title that is a head of the corpus (`lacking`): the title and its blocks up to the next
    title. The cells of a table in them are left out as in the window."""
    last = blocks.index(win[-1]) if win and win[-1] in blocks else 0
    out: list = []
    on = False
    for b in blocks[last + 1:]:
        if b.kind == "title" and not b.plain().strip().lower().startswith("table"):
            on = fp.squash(b.plain()) in lacking
            if on:
                out.append(b)
            continue
        if on and not (b.kind == "para" and is_table_para(b.plain())):
            out.append(b)
    return out


def last_cell_end(toks: list[str]) -> int:
    """The index of the last token of the cells of a class table in a paragraph: the numbers that stand right after the "20th" of the last row; else the last
    numeric token. A number in the sentence after the table ("for 24 hours") is not the end of the cells."""
    last20 = max((n for n, x in enumerate(toks) if x == "20th"), default=-1)
    if last20 >= 0:
        j = last20 + 1
        while j < len(toks) and NUMERIC.match(toks[j]):
            j += 1
        return j - 1
    return max((n for n, x in enumerate(toks) if NUMERIC.match(x)), default=-1)


def prose_after_cells(text: str, tail: str = "") -> str:
    """The text of a sentence that shares a paragraph with the cells of a table: after the leading numbers ("6 6 6 6 due to encumbrance. At 5th level, ...") or
    after the last cell of a table ("... 6 6 6 4 \u2014 with the summoner. Effects that cause death ..."), when it holds a sentence (a full stop), else
    nothing (a row of a table with words in its cells)."""
    toks = text.split()
    cands = []
    i = 0
    while i < len(toks) and NUMERIC.match(toks[i]):
        i += 1
    if i > 0:
        cands.append(" ".join(toks[i:]))
    k = last_cell_end(toks)
    if 0 <= k < len(toks) - 1:
        cands.append(" ".join(toks[k + 1:]))
    for prose in cands:
        if tail and prose.lower().startswith(tail.lower() + " "):
            prose = prose[len(tail):].lstrip()              # the Special cell of the last row of the table stands between the cells and the sentence that goes on
        if len(prose.split()) >= 4 and re.search(r"[a-z]{3}[^.]*\.\s", prose + " ") and not re.search(r"\b(?:Fort|Ref|Will)\b", prose):
            return prose
    return ""


TABLE_RUN = re.compile(r"^\s*(?:spells|extracts|formulae)\s+(?:per\s+day|known)|^\s*base\s+attack|^\s*level\s+(?:bonus|1st)", re.I)


TABLE_ANY = re.compile(r"\bBase Attack\b|\b(?:Spells|Extracts|Formulae) (?:per Day|Known)\s+(?:\d|1st|[\u2014\u2013])")


def cut_runs(runs: list, offset: int) -> list:
    """The runs of a paragraph up to the character `offset` of its text."""
    out, seen = [], 0
    for txt, bold, it in runs:
        if seen + len(txt) <= offset:
            out.append((txt, bold, it))
        else:
            if offset > seen:
                out.append((txt[:offset - seen], bold, it))
            break
        seen += len(txt)
    return out


def split_table_runs(b, tail: str = ""):
    """The paragraphs that stay of a paragraph that holds the header and the cells of a class table after its text ("Witch's Familiar (Ex): At 1st level, ...
    [bold] Spells per Day 0 3 1 -- ..."): the text before the first bold run that is a table header, and a sentence that follows the cells. When the header
    is not a run of its own ("... granted by the spirit Base Attack Fort Ref Will ..."), the text before the header's first word. None when the paragraph
    has no table header."""
    for n, (txt, bold, _it) in enumerate(b.runs):
        if n > 0 and bold and TABLE_RUN.match(txt):
            keep = [fp.Para("para", list(b.runs[:n]), b.page, b.col, 0)]
            rest = "".join(x[0] for x in b.runs[n:])
            prose = prose_after_cells(rest, tail)
            if prose:
                keep.append(fp.Para("para", [(prose, False, False)], b.page, b.col, 0))
            return keep
    text = "".join(x[0] for x in b.runs)
    m = TABLE_ANY.search(text)
    if m and m.start() > 0:
        keep = [fp.Para("para", cut_runs(list(b.runs), m.start()), b.page, b.col, 0)]
        prose = prose_after_cells(text[m.start():], tail)
        if prose:
            keep.append(fp.Para("para", [(prose, False, False)], b.page, b.col, 0))
        return keep
    return None


LEADING_CELLS = re.compile(r"^\s*(?:(?:[+\u2013-]?\d+(?:/[+\u2013-]?\d+)*(?:st|nd|rd|th)?|[\u2014\u2013])\s+){3,}")


def strip_leading_cells(b, tail: str = ""):
    """A paragraph that starts with the last cells of a class table ("+15/+10/+5 +12 +12 +6 Grand discovery Acid bomb*: When ...") without them (and without the
    Special cell of the last row), so that the head after them is the head of the paragraph. None when it does not start with cells."""
    if b.runs and b.runs[0][1] and TABLE_RUN.match(b.runs[0][0].strip()) and len(b.runs) > 1:
        return strip_leading_cells(fp.Para("para", list(b.runs[1:]), b.page, b.col, 0), tail) or fp.Para("para", list(b.runs[1:]), b.page, b.col, 0)      # the bold header of a table ("Spells per Day")
    text = "".join(x[0] for x in b.runs)
    m = LEADING_CELLS.match(text)
    if not m:
        # the Special cell of the last row alone in front of a head ("Final revelation Deaf: You cannot hear ...")
        if tail and text.lower().startswith(tail.lower() + " ") and text[len(tail) + 1:len(tail) + 2].isupper():
            m = re.match(r"", text)
            cut = len(tail) + 1
        else:
            return None
    else:
        cut = m.end()
    if m.end() == cut and tail and text[cut:].lower().startswith(tail.lower() + " "):
        cut += len(tail) + 1
    runs, seen = [], 0
    for txt, bold, it in b.runs:
        if seen + len(txt) <= cut:
            seen += len(txt)
            continue
        runs.append((txt[max(0, cut - seen):], bold, it))
        seen += len(txt)
    return fp.Para("para", runs, b.page, b.col, 0)


def table_tail(body: str) -> str:
    """The Special cell of the last row of the class table (the words that the text layer sets between the cells of the table and a sentence that the table
    broke): "Unholy champion"."""
    col, last = None, ""
    for ln in body.split("\n"):
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if col is None and ln.startswith("|Level|") and "Special" in cells:
            col = cells.index("Special")
        elif col is not None and re.match(r"\|\d+(?:st|nd|rd|th)\|", ln) and col < len(cells):
            last = cells[col]
            if ln.startswith("|20th|"):
                break                                        # the first table only (a spells-known table has no Special column)
    return last.split(",")[0].strip() if last and last != "\u2014" else ""


def window(blocks: list, heads: set[str] | frozenset = frozenset(), raw: bool = False, tail: str = "") -> list:
    """The blocks of the section "Class Features" of the class: after that title, up to the next subsection or class title. A class table (its title and its
    cells) and a sidebar title (set larger, 24) do not end it; the cells of the table are not text of a feature."""
    at = next((i for i, b in enumerate(blocks) if b.kind == "title" and fp.squash(b.plain()) == "classfeatures"), None)
    if at is None:
        return []
    out = []
    for b in blocks[at + 1:]:
        if b.kind == "title" and not b.plain().strip().lower().startswith("table") and (b.size == 18 or b.size >= 38) and fp.squash(b.plain()) not in heads:
            break                                          # a subsection title ends the window, unless the corpus has it as a feature head (Patron Spells)
        if b.kind == "title" and b.plain().strip().lower().startswith("table"):
            continue                                       # the title of a class table is not text of a feature
        if raw:                                            # the coverage check reads print without the table handling: only paragraphs that are cells alone go
            if not (b.kind == "para" and is_table_para(b.plain()) and sum(not NUMERIC.match(x) for x in b.plain().split()) <= 12):
                out.append(b)
            continue
        if b.kind == "para":
            cut = split_table_runs(b, tail)
            if cut is not None:                            # prose, then the header and the cells of a class table in one paragraph
                out += cut
                continue
        if b.kind == "para" and not is_table_para(b.plain()):
            stripped = strip_leading_cells(b, tail)
            if stripped is not None:                       # the last cells of a table in front of the next feature
                out.append(stripped)
                continue
        if b.kind == "para" and is_table_para(b.plain()):
            prose = prose_after_cells(b.plain(), tail)
            if prose:                                      # the cells ran into the text of a sentence that the table broke: the sentence stays
                out.append(fp.Para("para", [(prose, False, False)], b.page, b.col, 0))
            continue
        out.append(b)
    return join_across_tables(out)


def bold_option_heads(blocks: list, names: set[str]) -> list:
    """A paragraph that starts with the name of an option of the class and a colon in a plain run ("Acid bomb*: When ...": the text layer leaves the head of
    a star-marked option unstyled) gets a bold head, as the other options have."""
    out = []
    for b in blocks:
        if b.kind == "para" and fp.head_candidate(b) is None:
            text = "".join(x[0] for x in b.runs)
            m = re.match(r"^\s*([A-Z][^:.]{1,45}?\*?)(?=:\s)", text)
            if m and fp.namekey(m.group(1)) in names:
                n = m.end()
                runs, seen = [(text[:n], True, False)], 0
                for txt, bold, it in b.runs:
                    if seen + len(txt) > n:
                        runs.append((txt[max(0, n - seen):], bold, it))
                    seen += len(txt)
                b = fp.Para("para", runs, b.page, b.col, b.size)
        out.append(b)
    return out


def join_across_tables(blocks: list) -> list:
    """A sentence that print breaks for a class table (the table stands in the middle of it) continues in the next paragraph, in lower case: the two
    are one paragraph. Only a paragraph that does not end in terminal punctuation, followed by one that starts in lower case, is joined."""
    out: list = []
    for b in blocks:
        if (out and b.kind == "para" and out[-1].kind == "para" and not co.paragraph_complete(out[-1].plain())
                and b.plain().strip()[:1].islower() and fp.head_candidate(b) is None):
            a = out.pop()
            out.append(fp.Para("para", list(a.runs) + [(" ", False, False)] + list(b.runs), a.page, a.col, 0))
        else:
            out.append(b)
    return out


HEAD_RE = re.compile(r"^#### (.*?)(?: \{#([^}]+)\})?\s*$")
WRITE_FEATURES = True         # the `features` of a class (owner call 5 answered: the app accepts them on `kind = "class"`; `class_features`, `with_features`)
# The printed name of a head that the corpus names otherwise and that no plural or tag rule reaches: (class entry, key) -> print's head
PRINT_NAMES: dict[tuple[str, str], str] = {}


# Items of a list that print sets in italics under the feature, and that have no entry of their own (the nine judgments of the Inquisitor, p. 40: Piercing, Purity and
# Smiting are set in italics, the others in bold): their names are heads of unlisted sections under the feature.
EXTRA_HEADS: dict[str, list[str]] = {"ref/class/inquisitor": ["Piercing", "Purity", "Smiting"]}
# Where an unlisted section stands when print sets it away from its feature (the sidebar of the Witch's Familiar is in the next column, after Major Hex):
# (class entry, key) -> (the key of the feature it belongs under, its level: one level below the feature head, ruling 15)
PLACE_UNDER: dict[tuple[str, str], tuple[str, int]] = {}
# A box that print sets inside a feature and that the corpus has once, as a `###` section after the class features (ruling 41): the sections that its head and its
# sub-heads would make are not written a second time. (class entry, key of the section) -> the heading of the corpus section that holds the box.
BOX_AS_SECTION: dict[tuple[str, str], str] = {
    ("ref/class/witch", key): "### Adding Spells to a Witch's Familiar"
    for key in ("adding-spells-to-a-witch-s-familiar", "spells-gained-at-a-new-level", "familiar-teaching-familiar", "learn-from-a-scroll")}
# A box that interrupts a feature in print and that the corpus has as a `###` section: (class entry, key of the box) -> the key of the feature that its last
# paragraph ends (the Antipaladin's box "Fall From Grace" stands inside Spells, p. 121)
SIDEBAR_TAILS: dict[tuple[str, str], str] = {("ref/class/antipaladin", "fall-from-grace"): "spells"}
# Text of another owner book that the class entry carries (owner ruling 32): the battle standards of the Cavalier are printed in Chronicle of Legends p. 4 (the
# box "Flying the Flag of War"), not in Advanced Player's Guide; the corpus words them as heads of its own. Each section is print's text, typed from the other book
# and checked against it (`OTHER_TEXT`, every word of the text must stand in that page of the book), under a head that names the book and the page (as the
# class-option sections of ruling 32 do). A key that the corpus has as a head is reused (no key moves); the heads the corpus has twice (`-2`) go.
# (class entry) -> (book, the pdf page that holds the text, the key of the item that the sections stand before, [(key, head, text)])
OTHER_BOOK: dict[str, list[tuple[str, int, str, list[tuple[str, str, str]]]]] = {
    "ref/class/cavalier": [("chronicle-of-legends", 6, "bonus-feat", [
        ("flying-the-flag-of-war", "Flying the Flag of War (Chronicle of Legends page 4)",
         "Some knights inspire and direct their allies with specialized tactics. A cavalier or samurai can select one of the following battle standards upon "
         "gaining the banner class feature, and its benefits replace the normal benefits of the banner and greater banner class features. A battle standard "
         "functions as the banner or greater banner class feature except where otherwise noted. A cavalier or samurai who replaces the banner or greater "
         "banner class feature via an archetype cannot select a battle standard, with the following exception: a standard bearer cavalier can select a "
         "battle standard at 1st level, and its effects increase as per the standard bearer's banner."),
        ("fleet-standard", "Fleet Standard (Ex) (Chronicle of Legends page 4)",
         "These banners are common among Jininese samurai. An ally who benefits from this standard increases her land speed by 5 feet and gains a +1 dodge "
         "bonus to AC during any round in which she moved at least 10 feet. This increase to land speed is an enhancement bonus. At 10th level and every 5 "
         "levels thereafter, the bonus to speed increases by 5 feet. At 14th level, an ally benefiting from the banner gains a +2 morale bonus on Reflex "
         "saving throws against effects that target an area, such as [fireball](ref/spell/fireball) or [breath weapons](ref/umr/breath-weapon). When the cavalier or samurai waves this standard, each "
         "ally within 60 feet can move up to her speed as an immediate action."),
        ("jinx-standard", "Jinx Standard (Ex) (Chronicle of Legends page 4)",
         "These grim fetishes are common among Jadwiga cavaliers. An ally who benefits from this standard gains a +1 bonus on caster level checks to bypass "
         "[spell resistance](ref/rule/spell-resistance) and a +1 bonus to the DC of her hexes and necromancy or enchantment spell she casts. At 10th level and every 5 levels "
         "thereafter, the bonus on caster level checks increases by 1. At 14th level, an ally benefiting from the banner gains a +2 morale bonus on saving "
         "throws against spells or effects that deal hit point damage. When the cavalier or samurai waves this standard, a number of allies equal to the "
         "cavalier or samurai's Charisma modifier (minimum 1) within 60 feet can attempt an Intimidate check to demoralize a foe as an immediate action."),
        ("knave-standard", "Knave Standard (Ex) (Chronicle of Legends page 4)",
         "The knave standard is common among cavaliers of the River Kingdoms. An ally who benefits from this standard gains a +2 dodge bonus to AC against "
         "attacks of opportunity provoked by movement and a +1 morale bonus on attack rolls that benefit from [flanking](ref/rule/flanking). At 10th level and every 5 levels "
         "thereafter, the bonus to AC increases by 1. At 14th level, an ally benefiting from the banner gains [sneak attack](ref/ability/sneak-attack) +1d6; this stacks with other "
         "sources of sneak attack. When the cavalier or samurai waves this standard, a number of allies equal to the cavalier or samurai's Charisma "
         "modifier (minimum 1) within 60 feet can each attempt a [feint](ref/rule/feint) against a foe she threatens as an immediate action."),
        ("stalwart-standard", "Stalwart Standard (Ex) (Chronicle of Legends page 4)",
         "These banners are common among the dwarven defenders of Kraggodan. An ally who benefits from this standard gains a +2 morale bonus to CMD and a "
         "+1 morale bonus on attack rolls to creatures threatening an ally. At 10th level and every 5 levels thereafter, the bonus to CMD increases by +1. "
         "At 14th level, an ally benefiting from the banner is treated as one size category larger for the purposes of determining which creatures can "
         "affect him with combat maneuvers. When the cavalier or samurai waves this standard, each ally within 60 feet can move up to 10 feet without "
         "provoking attacks of opportunities and ignoring [difficult terrain](ref/rule/terrain-and-obstacles) as an immediate action."),
    ]),
        # the mounts that other owner books add to the Mount of the Cavalier: Wilderness Origins p. 23 and Ultimate Wilderness p. 178 (the corpus has them as rows of the feature)
        ("wilderness-origins", 25, "order", [
            ("cavalier-mounts-wilderness-origins", "Cavalier Mounts (Wilderness Origins page 23)",
             "A Medium cavalier can select an [axe beak](ref/companion/axe-beak), [elk](ref/companion/elk), [giant tortoise](ref/companion/tortoise-giant), "
             "[giant seahorse](ref/companion/seahorse-giant), or [giraffe](ref/companion/giraffe) as a mount. A Small cavalier can select an "
             "[antelope](ref/companion/antelope), [giant weasel](ref/companion/weasel-giant), [kangaroo](ref/companion/kangaroo), lizard "
             "([giant gecko](ref/companion/lizard-giant-gecko)), [ram](ref/companion/ram), or [stag](ref/companion/stag) as a mount. The augmented companion, "
             "bodyguard, bully, daredevil, draconic companion, racer, and wrecker companion archetypes are all particularly appropriate for a cavalier's mount."),
        ]),
        ("ultimate-wilderness", 179, "order", [
            ("cavalier-mounts-ultimate-wilderness", "Cavalier Mounts (Ultimate Wilderness page 178)",
             "A Medium cavalier can select a [zebra](ref/companion/zebra) as a mount. A Small cavalier can select a [capybara](ref/companion/capybara), "
             "[reindeer](ref/companion/reindeer), or [wolfdog](ref/companion/wolfdog) as a mount."),
        ]),
    ],
}
OTHER_TEXT: dict[tuple[str, int], str] = {}      # (book, pdf page) -> the squashed text of the pages that `OTHER_BOOK` cites, filled by `load_other_books`


def load_other_books(corpus: Path, books_dir: str, cache: str, main_book: str) -> None:
    """Read the pages of the other owner books that `OTHER_BOOK` cites, so that each section can be checked against print."""
    for book, page, _before, _secs in (x for xs in OTHER_BOOK.values() for x in xs):
        if (book, page) in OTHER_TEXT:
            continue
        fp.configure_book(book)
        pdf = fp.find_pdf(Path(books_dir), fp.publication_title(corpus, book))
        if not pdf:
            raise SystemExit(f"no copy of the book {book} under {books_dir}")
        bk = fp.load_book(fp.book_xml(pdf, Path(cache)))
        text = " ".join(b.plain() for b in fp.read_blocks(bk, page, page))
        OTHER_TEXT[(book, page)] = fp.squash(re.sub(r"(?<=[a-z])(?:B[1-6]|UW|UC|UM|APG|ARG)(?=[\s,.;):])", "", text))      # the book markers after a name (ruling 26)
    fp.configure_book(main_book)


def other_book_sections(e_id: str, items: list[dict]) -> None:
    """Put the sections of another owner book into the plan (see `OTHER_BOOK`): the corpus head of the same key becomes the section (text and head from
    print), the other sections stand before `before`. A text that is not in the other book's page is a hold."""
    for book, page, before, secs in OTHER_BOOK.get(e_id, []):
        seen = OTHER_TEXT.get((book, page))
        firsts = [n for n, x in enumerate(items) if x["key"] in {k for k, _, _ in secs}]            # a first run: the corpus heads of the standards are in the plan
        at = min(firsts) if firsts else next((n for n, x in enumerate(items) if x["key"] == before), len(items))
        for key, head, text in secs:
            status, notes = "print", [f"text of another owner book (owner ruling 32): {book}, checked against that print"]
            if seen is None or fp.squash(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)) not in seen:
                status = "hold"
                notes = [f"the text is not found on the page of {book} that it cites"]
            old = next((x for x in items if x["key"] == key), None)
            sec = {"key": key, "line": -1, "head": head, "print": text, "status": status, "notes": notes, "level": 5, "unlisted": True}
            if old is not None:
                old.update(sec, line=old["line"], drop=False)
                at = items.index(old) + 1
            else:
                items.insert(at, sec)
                at += 1


# The end of a feature's text that print sets in the paragraph of another feature (a box sits in the middle of a feature's paragraph and the text layer joins the
# rest of that paragraph to the last paragraph of the box): (class entry, key of the feature whose paragraph holds it) -> (the words that it starts with, the entry that
# it belongs to: an option of the feature that the box interrupted, which is a link; the class-option pass of the book reads its text from print). The Witch's box "Adding Spells to a Witch's
# Familiar" stands inside the Hag's Eye hex (p. 68).
TAIL_OF_LINKED: dict[tuple[str, str], tuple[str, str]] = {("ref/class/witch", "learn-from-a-scroll"): ("witches within 10 feet", "ref/hex/hags-eye")}
# Sections that print sets behind the class features and that the corpus has inside a feature (the Antipaladin's code of conduct is a row of its
# proficiencies): they become unlisted sections of their own, so the text stays where print has it.
SECTIONS_BEHIND: dict[str, set[str]] = {"ref/class/antipaladin": {"codeofconduct", "associates"}}
TABLE_LEAK = re.compile(r"\b(?:Spells|Extracts) per Day\s+(?:\d|1st|[\u2014\u2013])|\bBase Attack\b|(?:(?:[\u2014\u2013]|[+\u2013-]?\d+(?:/[+\u2013-]?\d+)*(?:st|nd|rd|th)?)\s+){6,}")


# Print's layout puts a class table beside the text, and the text layer of the page runs words of the table's Special column into a sentence. Known cases:
# (class entry, key) -> [(what the layer has, what the sentence says)], each checked against the page.
LAYOUT_FIXES: dict[tuple[str, str], list[tuple[str, str]]] = {
    ("ref/class/summoner", "eidolon"): [("the Twin eidolon summoner's class level", "the summoner's class level")],
    ("ref/class/inquisitor", "slayer"): [("cannot be changed for the remainder of the judgment", "cannot be changed for the remainder of the judgment.")],     # print's sentence has no full stop (errata row of ruling 43)
    ("ref/class/antipaladin", "fiendish-boon"): [("re:Spells per Day 1st 2nd 3rd 4th(?: [\u2014\u2013\\d]+)+ ", "")],             # the cells of Table 2-13 (Advanced Player's Guide, Antipaladin p. 121)
    ("ref/class/inquisitor", "solo-tactics"): [("re:Spells per Day(?: \\d+)+ ", "")],                                              # the cells of Table 2-4 (Inquisitor p. 40)
    ("ref/class/summoner", "life-link"): [("more than 1,000 feet Spells per Day 5 5 5 5 5 5 away", "more than 1,000 feet away")],       # the cells of Table 2-8 (Advanced Player's Guide, Summoner p. 56)   # Table 2-7 lists "Twin eidolon" at 20th level (Advanced Player's Guide, Summoner p. 55)
}


def stem(name: str) -> str:
    """A head without its tag, in lower case, the last word in the singular ("Weapon and Armor Proficiencies" and "... Proficiency" are one head)."""
    s = " ".join(fp.ABILITY_TAG.sub("", name).strip().rstrip(":").strip().lower().split())        # print sets some heads with double spaces
    s = re.sub(r"ies$", "y", s)
    return re.sub(r"(?<!s)s$", "", s)


def references(corpus: Path, class_id: str, key: str) -> list[str]:
    """The entries that point at a head of a base class: a trade of an archetype of the class (`feature = "<key>"`, in `entries/arc-<class>/`) or a link to
    `<class id>#<key>` anywhere, a deep link in `aliases.toml` or `history.toml`, or an option group of the class tied to it (`feature =` in `option-groups.toml`). A head that print does not set may be dropped only when nothing points at its key."""
    cls = class_id.rsplit("/", 1)[1]
    out = []
    for p in sorted((corpus / "entries").rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        if f"{class_id}#{key})" in text or (p.parent.name == f"arc-{cls}" and f'feature = "{key}"' in text):
            out.append(p.stem)
    for name in ("aliases.toml", "history.toml"):                # a deep link of an old id or a retired page can name the head: `<class id>#<key>`
        path = corpus / name
        if path.exists() and re.search(re.escape(class_id) + "#" + re.escape(key) + r"(?![\w-])", path.read_text(encoding="utf-8")):
            out.append(name)
    if key in {f for f in class_groups(corpus, class_id).values() if f}:           # an option group points at the feature (`feature =` in option-groups.toml)
        out.append("option-groups.toml")
    return out


def overlap(a: str, b: str) -> int:
    wa = set(re.findall(r"[a-z']{4,}", a.lower()))
    return len(wa & set(re.findall(r"[a-z']{4,}", b.lower())))


def split_between(paras: list[str], first_corpus: str, second_corpus: str) -> int:
    """Where a printed feature ends and the next feature of the corpus (that print sets inside it, as text) begins: the paragraph index that gives the best
    overlap of words, the first part with the corpus text of the first feature and the rest with the second (at least one paragraph each)."""
    best, at = -1, len(paras)
    for k in range(1, len(paras)):
        s = sum(overlap(x, first_corpus) for x in paras[:k]) + sum(overlap(x, second_corpus) for x in paras[k:])
        if s > best:
            best, at = s, k
    return at


def corpus_heads(lines: list[str], region: tuple[int, int]) -> list[tuple[int, str, str]]:
    """(line, head text, key) of each `####` head of the region."""
    out = []
    for i in range(region[0], region[1]):
        m = HEAD_RE.match(lines[i])
        if m:
            out.append((i, m.group(1), m.group(2) or fp.slugify(fp.ABILITY_TAG.sub("", m.group(1)))))
    return out


def option_title_keys(corpus: Path) -> dict[str, list[tuple[str, str]]]:
    """namekey -> [(entry id, group)] of every class option: an item of an option list in print (a curse, a mystery) that has its own entry is linked.
    Titles repeat across groups ("Tongues" is an oracle curse and a shaman hex), so the group of the list decides (`pick_options`)."""
    out: dict[str, list[tuple[str, str]]] = {}
    for x in co.load_class_options(corpus):
        out.setdefault(fp.namekey(x.title), []).append((x.id, (x.data.get("fields") or {}).get("group", "")))
    return out


def option_names(options: dict, own: dict) -> list[str]:
    """The names (as `namekey`) of the options of the class's own groups: print sets some of them in a plain run ("Acid bomb*: When ..."), and the split of the
    printed features expects them as heads."""
    return sorted(k for k, cands in options.items() if any(g in own for _, g in cands))


def class_groups(corpus: Path, class_id: str) -> dict[str, str | None]:
    """The option groups that the class owns (`option-groups.toml`: `classes`), each with the class feature that the group is tied to (`feature`, or None)."""
    import tomllib
    path = corpus / "option-groups.toml"
    data = tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    return {name: g.get("feature") for name, g in (data.get("groups") or {}).items() if class_id in (g.get("classes") or [])}


def own_candidates(cands: list[tuple[str, str]], own: dict[str, str | None], feature: str) -> list[tuple[str, str]]:
    """The entries of an option name that the list may link: those in a group that the class owns, and whose group is not tied to another feature of the class
    (the Inquisitor's inquisition "Justice" is no judgment). Never an entry of another class, whatever its place in the list of candidates."""
    return [(i, g) for i, g in cands if g in own and own[g] in (None, feature)]


def pick_options(items: list[tuple[str, list[tuple[str, str]]]]) -> tuple[list[tuple[str, str]], list[str]]:
    """The links of one option list: (name, entry id) for each name, from the group that most of its items belong to, and the names that stay ambiguous
    (two entries of the chosen group, or none in it). No fallback to another group: an item without a candidate of its class is no link."""
    groups = Counter(g for _, cands in items for _, g in cands)
    top = {g for g, c in groups.items() if c == max(groups.values())} if groups else set()      # groups with as many items as the most common one: a tie has no winner
    out, unsure = [], []
    for name, cands in items:
        pool = sorted({i for i, g in cands if g in top})
        if len(pool) == 1:
            out.append((name, pool[0]))
        else:
            unsure.append(name)
    return out, unsure


def class_decisions(corpus: Path, book: str) -> dict[tuple[str, str], tuple[str, str]]:
    """The decisions of the book's class options file for classes: (class id, key) -> (decision, note); `print` settles a hold as print has it (the corpus
    wording is the import's paraphrase, or print has text that the corpus lacks), `hold` keeps it for an errata check."""
    return co.read_decisions(co.decisions_file(corpus, book))


SENTENCE_END = re.compile(r"(?<=[.!?])[\"\u201d\u2019)]*\s+(?=[A-Z\u201c\"(+\u2013\d])")
MARKDOWN = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def sentences(text: str) -> list[str]:
    """The printed sentences of a text (at least 12 letters), for the coverage check."""
    text = " ".join(text.split())
    return [s for s in SENTENCE_END.split(text) if len(re.sub(r"[^A-Za-z]", "", s)) >= 12]


def plain_text(md: str) -> str:
    """Written Markdown as the words that print has: links to their names, emphasis, bullets and the tags of heads gone."""
    return re.sub(r"[_*>]|^\s*[-\u2022]\s+", "", MARKDOWN.sub(r"\1", md), flags=re.M)


def drop_cell_runs(sentence: str) -> str:
    """The sentence without the runs of three or more numeric tokens in it (cells of a class table that the text layer set inside it: "This ability 4 4 3 3 is")."""
    toks, out, run = sentence.split(), [], []
    for x in toks + [""]:
        if x and NUMERIC.match(x):
            run.append(x)
            continue
        if len(run) < 3:
            out += run
        run = []
        if x:
            out.append(x)
    return " ".join(out)


HEADER_TOKENS = {"ref", "fort", "will", "save", "base", "attack", "bonus", "level", "special"}


def table_word(token: str, table_words: frozenset | set) -> bool:
    letters = re.sub(r"[^a-z]", "", token.lower())
    return (len(letters) >= 4 and letters in table_words) or letters in HEADER_TOKENS


def split_junk(tokens: list[str], table_words: frozenset | set) -> list[list[str]] | None:
    """The prose of a sentence that the text layer ran a class table into: the words before the header of the table ("Base Attack Fort Ref Will ...", "Spells per Day"
    followed by its columns) and after its last row (the numbers after the "20th", then the words of the last Special cell). None when the sentence has no such
    header. The two stretches must stand in the written text as they are: a number in them is a number of the sentence."""
    n = len(tokens)
    for i in range(n):
        low = [re.sub(r"[^A-Za-z]", "", x).lower() for x in tokens[i:i + 2]]
        nxt3 = tokens[i + 3] if i + 3 < n else ""
        header = low == ["base", "attack"] or (low[:1] in (["spells"], ["extracts"], ["formulae"]) and ((low[1:2] == ["per"] and NUMERIC.match(nxt3 or "x") is not None)
                                                                                                   or (low[1:2] == ["known"] and (NUMERIC.match(tokens[i + 2] if i + 2 < n else "x") is not None or (tokens[i + 2:i + 3] or [""])[0] == "Level"))))
        if header:
            end = i + last_cell_end(tokens[i:]) + 1
            if end <= i + 2:
                end = i + 3
            while end < n and table_word(tokens[end], table_words):
                end += 1                                                    # the Special cell of the last row
            return [tokens[:i], tokens[end:]]
    return None


def junk_free(sentence: str, table_words: frozenset | set) -> list[str]:
    """The stretches of prose of a sentence that a class table was run into (`split_junk`), as strings; [] when it has no table."""
    pieces = split_junk(sentence.split(), table_words)
    return [" ".join(p) for p in (pieces or []) if p]


def lost_sentences(printed: str, written: str, table_words: frozenset | set = frozenset()) -> list[str]:
    """The printed sentences that the written text lacks. A sentence is there when its letters and digits stand in the written text, or when it is one written
    sentence up to noise (`co.near_exact`: the same digits, the same negations, at most two letters that differ). A sentence with a class table run into it is
    there when the words before the table and the words after it each stand in the written text as they are, numbers included. No allowance is made by the
    words of the whole text."""
    plain = co.strip_see(plain_text(written))                     # a short printed "(see ...)" cross-reference is kept in the text but the corpus may link the thing (ruling 16)
    have = fp.squash(plain)
    wsents = sentences(plain)
    out = []
    for s in sentences(co.strip_see(printed)):
        s = re.sub(r"^\((?:Ex|Su|Sp)(?:(?:, or |, and |, | or | and )(?:Ex|Su|Sp))*\):\s*", "", s)       # the tag of a head stands in the head
        pieces = split_junk(s.split(), table_words)
        if pieces is not None:
            if all(not piece or fp.squash(" ".join(drop_cell_runs(" ".join(piece)).split())) in have for piece in pieces):
                continue
            out.append(s)
            continue
        s = drop_cell_runs(s)
        if fp.squash(s) in have or co.near_exact(s, wsents):
            continue
        out.append(s)
    return out


def print_text(pf) -> str:
    return " ".join("".join(r[0] for r in para) for para in pf.paras)


def covered_loosely(sentence: str, text: str) -> bool:
    """Whether the sentence is, in its words, one sentence of the text of an option that has an entry of its own (the entry still words it as the import did,
    until the class-option pass of the book converts it): the best single sentence of that text shares at least four fifths of its words in order."""
    ws = re.findall(r"[a-z0-9']+", sentence.lower().replace("\u2019", "'"))
    for other in sentences(plain_text(text)):
        wo = re.findall(r"[a-z0-9']+", other.lower().replace("\u2019", "'"))
        if (ws and wo and re.findall(r"\d+", sentence) == re.findall(r"\d+", other) and len(co.NEGATIONS.findall(sentence)) == len(co.NEGATIONS.findall(other))
                and difflib.SequenceMatcher(None, ws, wo, autojunk=False).ratio() >= 0.8):
            return True
    return False


def table_words(body: str) -> set[str]:
    """The words (four letters or more) of the rows of the Markdown tables of a class body."""
    return set(re.findall(r"[a-z]{4,}", " ".join(ln for ln in body.split("\n") if ln.startswith("|")).lower().replace("\u2019", "'")))


# The section of a class chapter from which print sets what other entries hold (the spell list: each spell has its class level; the orders, the mysteries,
# the eidolon rules and the evolutions: entries of their own): the gap check stops at that title. (class entry) -> the squashed title.
GAP_STOP: dict[str, str] = {
    "ref/class/alchemist": "alchemistformulae", "ref/class/cavalier": "cavalierorders", "ref/class/inquisitor": "inquisitorspells", "ref/class/oracle": "mysteries",
    "ref/class/summoner": "eidolons", "ref/class/witch": "witchspells"}


def cut_tails(class_id: str, text: str) -> str:
    """The text without the end of an option's paragraph that print sets after a box (`TAIL_OF_LINKED`): it belongs to the link's own entry."""
    text = " ".join(text.split())
    for (c, _k), (marker, _eid) in TAIL_OF_LINKED.items():
        if c == class_id and marker in text:
            text = re.sub(re.escape(marker) + r".*?\bincrements\.", "", text)
    return text


def gap_blocks(blocks: list, win: list, lacking: set[str], stop: str = "") -> list:
    """The blocks between the end of the class window (a subsection title ends it) and the next title that is a head the corpus lacks (`lacking`, read by
    `section_behind`), or the next large title: the sections that neither reading covers (the Witch's box "Witch's Familiar", p. 69)."""
    last = blocks.index(win[-1]) if win and win[-1] in blocks else 0
    out = []
    for b in blocks[last + 1:]:
        if b.kind == "title" and not b.plain().strip().lower().startswith("table") and (fp.squash(b.plain()) in lacking or b.size >= 38 or (stop and fp.squash(b.plain()) == stop)):
            break
        if b.kind == "para" and not is_table_para(b.plain()):
            out.append(b)
    return out


def coverage_check(corpus: Path, e, items: list[dict], blocks: list, title, heads: list, lacking: set[str], region: tuple[int, int], lines: list[str], options: dict, own: dict) -> list[str]:
    """Print-coverage check (independent of the comparison's own reading): every printed sentence of the span of a feature, read from the blocks of the page
    without the table handling of `window`, must stand in the written text of the class. The feature holds otherwise, with the sentences in its notes.
    A sentence of a printed head that has no item (a box, a section of its own) must stand somewhere in the written entry (features, unlisted sections,
    the text outside the feature region)."""
    rwin0 = bold_option_heads(window(blocks, raw=True), set(option_names(options, own)))
    rwin = rwin0 + section_behind(blocks, rwin0, lacking | SECTIONS_BEHIND.get(e.id, set()))
    _, rpfs = fp.split_print([title] + rwin, [h for _, h, _ in heads] + option_names(options, own) + EXTRA_HEADS.get(e.id, []))
    linked_text = []
    for x in items:
        for _, eid in x.get("links", []):                       # the text of a linked option is the text of its entry
            path = corpus / "entries" / (eid.removeprefix("ref/") + ".md")
            if path.exists():
                linked_text.append(path.read_text(encoding="utf-8").split("\n+++\n", 1)[-1])
    union = "\n".join([feature_text(x) for x in items if not x.get("drop")] + lines[:region[0]] + lines[region[1]:] + linked_text)
    cells = table_words(e.body)
    linked = {fp.namekey(n) for x in items for n, _ in x.get("links", [])}      # an item of an option list that has an entry of its own: its text is that entry's
    gap = gap_blocks(blocks, rwin0, lacking | SECTIONS_BEHIND.get(e.id, set()), GAP_STOP.get(e.id, ""))
    gap_text = cut_tails(e.id, " ".join(" ".join(b.plain().split()) for b in gap))
    gap_lost = lost_sentences(gap_text, union, cells)
    problems: list[str] = []
    if gap_lost and not items:
        problems.append(f"{len(gap_lost)} printed sentences between the class features and the next head that the corpus lacks, and no feature to hold: " + " | ".join(s[:70] for s in gap_lost[:3]))
    if gap_lost and items:
        host = next((x for x in items if not x.get("drop")), items[0])
        host["status"] = "hold"
        host["notes"].insert(0, f"print sections between the class features and the next head that the corpus lacks are not in the written entry ({len(gap_lost)} sentences): "
                             + " | ".join(s[:70] for s in gap_lost[:3]))
        host["lost"] = gap_lost
    for pf in rpfs:
        name = fp.head_text(pf.head)
        if fp.namekey(fp.ABILITY_TAG.sub("", name)) in linked or fp.namekey(name) in linked:
            continue
        it = next((x for x in items if not x.get("drop") and (fp.namekey(fp.ABILITY_TAG.sub("", x["head"])) == fp.namekey(fp.ABILITY_TAG.sub("", name))
                                                             or stem(x["head"]) == stem(name))), None)
        lost = lost_sentences(cut_tails(e.id, print_text(pf)), feature_text(it) if it else "", cells)
        if os.environ.get("COVDEBUG") and lost:
            print("COV", e.id, repr(name), "->", it["key"] if it else None, "|", [s[:90] for s in lost][:6])
        lost = lost_sentences(" ".join(lost), union, cells) if it is None else [s for s in lost if s in lost_sentences(s, union, cells)]
        lost = [s for x in lost for s in (junk_free(x, cells) or [x]) if not covered_loosely(s, " ".join(linked_text))]      # the entry of a linked option words its text as the import did
        if lost:
            if it is None:
                it = next((x for x in items if x.get("unlisted")), items[0] if items else None)
            if it is not None:
                it["status"] = "hold"
                it["notes"].insert(0, f"print sentences that the written text lacks ({len(lost)}): " + " | ".join(s[:70] for s in lost[:3]))
                it["lost"] = lost
            else:
                problems.append(f"{len(lost)} printed sentences of `{name}` are not in the entry and no feature holds them: " + " | ".join(s[:70] for s in lost[:3]))
    return problems


def compare_class(corpus: Path, e, bk, cache: dict, options: dict | None = None, decisions: dict | None = None) -> dict:
    """The comparison of one base class, as a plan for the writer: one item per `####` head of the class (its key, print's head text, print's text and
    status), the print heads that the corpus has no head for (`extra`), the heads that print does not have (`missing`), and the items of option lists
    (owner call 4: an item that has an entry of its own is a link, the feature keeps print's lead-in)."""
    region = feature_region(e.body)
    if region is None or not e.page.isdigit():
        return {"items": [], "extra": [], "missing": [], "window": 0, "problems": ["no `####` head, or no page"], "region": None}
    lines = e.body.split("\n")
    heads = corpus_heads(lines, region)
    own = class_groups(corpus, e.id)
    page = int(e.page)
    blocks = fp.read_blocks(bk, page, min(page + 12, max(bk.pages)))
    class_tail = table_tail(e.body)
    opt_names = set(option_names(options or {}, own))
    win = bold_option_heads(window(blocks, tail=class_tail), opt_names)
    title = fp.Para("title", [(e.title, True, False)], page, 0, 20)
    expected = [h for _, h, _ in heads] + option_names(options or {}, own) + EXTRA_HEADS.get(e.id, [])
    _, pfs = fp.split_print([title] + win, expected)
    printed = {fp.namekey(fp.head_text(f.head)): fp.head_text(f.head) for f in pfs}
    # a corpus head that print sets as the title of a section behind the class features ("Patron Spells" over the patrons of the Witch, p. 70): that
    # section is read as the text of the head
    lacking = {fp.squash(fp.ABILITY_TAG.sub("", h)) for _, h, _ in heads if fp.namekey(h) not in printed and not any(stem(ph) == stem(h) for ph in printed.values())}
    win = win + section_behind(blocks, win, lacking | SECTIONS_BEHIND.get(e.id, set()))
    _, pfs = fp.split_print([title] + win, expected)
    printed = {fp.namekey(fp.head_text(f.head)): fp.head_text(f.head) for f in pfs}
    names = {}                                                    # key -> the name that the pseudo body gives the head
    for _, text, key in heads:
        want = PRINT_NAMES.get((e.id, key))
        if want is None and fp.namekey(text) not in printed:
            want = next((ph for ph in printed.values() if stem(ph) == stem(text)), None)       # "Proficiency" for "Proficiencies"
        names[key] = (want or text).rstrip(":").strip()            # "Order (Ex):" is a name without its colon (a name that ends in one is no feature name)
    pseudo_lines = []
    in_section = False
    for ln in lines[region[0]:region[1]]:
        if re.match(r"^#{5,} ", ln):
            in_section = True                                      # an unlisted section of an earlier write: written again from print, not part of the text of the feature
            continue
        if in_section and not HEAD_RE.match(ln):
            continue
        in_section = False
        m = HEAD_RE.match(ln)
        pseudo_lines.append(f"**{names[m.group(2) or fp.slugify(fp.ABILITY_TAG.sub('', m.group(1)))]}**" if m else ln)
    pseudo = "\n".join(pseudo_lines)
    probe = {fp.namekey(h) for h in (fp.head_of_para(p_) for p_ in win) if h}                  # as the print comparison reads the import: a row that print sets as a head is split off
    _, feats_all = fp.parse_import(pseudo, probe)
    feats = [f for f in feats_all if not f.pseudo]
    if len(feats) != len(heads):
        return {"items": [], "extra": [], "missing": [], "window": len(win), "problems": [f"{len(heads)} heads but {len(feats)} features read from them"], "region": region}
    e2 = dataclasses.replace(e, body=pseudo)
    old_heads = fp.ITALIC_HEADS.get(e.id)
    fp.ITALIC_HEADS[e.id] = list(old_heads or []) + option_names(options or {}, own) + EXTRA_HEADS.get(e.id, [])      # the options of the class's groups are heads even when print sets them in a plain run
    try:
        res = fp.compare_entry(e2, [title] + win, bk)
    finally:
        if old_heads is None:
            fp.ITALIC_HEADS.pop(e.id, None)
        else:
            fp.ITALIC_HEADS[e.id] = old_heads
    by_span = {r["span"]: r for r in res["rows"] if r["span"]}
    items, missing = [], []
    all_spans = {f.span_sha() for f in feats_all}
    for (line, text, key), f in zip(heads, feats):
        r = by_span.get(f.span_sha())
        if r is None or "head not printed" in r["notes"]:
            missing.append(key)
            items.append({"key": key, "line": line, "head": text, "print": "", "status": "hold", "notes": ["head not printed"]})
        else:
            status, notes = r["status"], list(r["notes"])
            dec = (decisions or {}).get((e.id, key))
            if dec and dec[0] == "print" and status == "hold":
                status = "print"
                notes.append(f"decision: {dec[1]}")
            head, text = r["head"], r["print"]
            tag = re.match(r"^\(((?:Ex|Su|Sp)(?:(?:, or |, and |, | or | and )(?:Ex|Su|Sp))*)\):\s*", text)
            if tag:                                       # the tag of the head ("Summon Monster I" "(Sp):") stands in the first run: it belongs to the head
                head = f"{head} ({tag.group(1)})" if not re.search(r"\((?:Ex|Su|Sp)[^)]*\)\s*$", head) else head
                text = text[tag.end():]
            for old, new in LAYOUT_FIXES.get((e.id, key), []):
                fix = (lambda s, o=old, n=new: re.sub(o[3:], n, s)) if old.startswith("re:") else (lambda s, o=old, n=new: s.replace(o, n))
                if fix(" ".join(text.split())) != " ".join(text.split()):
                    text = "\n\n".join(fix(" ".join(x.split())) for x in text.split("\n\n"))
                    notes.append(f"layout: words or cells of a class table are in the sentence ({old[:50]!r})")
            leak = TABLE_LEAK.search(" ".join(text.split()))
            if leak:                                      # cells of a class table in the sentence: a layout fix (`LAYOUT_FIXES`) must name them
                status = "hold"
                notes.append(f"cells of a class table are in the text: ...{' '.join(text.split())[max(0, leak.start() - 40):leak.end() + 30]}...")
            cut = co.incomplete_paragraph(text)
            if cut:                                       # the completeness guard: the window ended, or a table stands in the sentence
                status = "hold"
                notes.append(f"print text may be cut at a page or column break: ...{cut}")
            items.append({"key": key, "line": line, "head": head, "print": text, "status": status, "notes": notes})
    ends = [h[0] for h in heads[1:]] + [region[1]]
    for (ln, _txt, _key), end, it in zip(heads, ends, items):
        it["corpus"] = "\n".join(lines[ln + 1:end])
    for n, it in enumerate(items):
        if "head not printed" not in it["notes"]:
            continue
        refs = references(corpus, e.id, it["key"])
        prev = next((x for x in reversed(items[:n]) if "head not printed" not in x["notes"]), None)
        if not refs:
            it["drop"] = True                                     # nothing points at the key: print sets the text inside another feature, written once, there
            it["status"] = "print"
            it["notes"] = [f"dropped: no trade or link points at `{it['key']}`; print sets its text inside the feature above it"]
        elif prev is not None and prev["print"]:
            paras = prev["print"].split("\n\n")
            if len(paras) > 1:
                k = split_between(paras, prev["corpus"], it["corpus"])
                prev["print"], it["print"] = "\n\n".join(paras[:k]), "\n\n".join(paras[k:])
                it["status"] = "hold"
                it["notes"] = [f"print sets this head's text inside `{prev['key']}` (split by the corpus text); referenced by {refs[:3]}"]
                it["split_from"] = prev["key"]
                dec = (decisions or {}).get((e.id, it["key"]))
                if dec and dec[0] == "print":
                    it["status"] = "print"
                    it["notes"].append(f"decision: {dec[1]}")
    extra, options = [], options or {}                          # the items of an option list are collected, then linked from one group
    last = None
    # keys that an unlisted section must not take: the keys of the heads, and the anchors outside the feature region (a rerun finds the unlisted sections of
    # an earlier write inside the region, which the write replaces)
    outside = "\n".join(lines[:region[0]] + lines[region[1]:])
    head_keys = {k for _, _, k in heads}
    taken = set(re.findall(r"\{#([^}]+)\}", outside)) | head_keys | {fp.slugify(fp.ABILITY_TAG.sub("", t_)) for _, t_, _ in heads}
    title_heads = {fp.squash(b.plain()) for b in win if b.kind == "title"}
    new_after: dict[str, str | None] = {}
    problems_extra: list[str] = []
    new_items: list[tuple[str | None, dict]] = []                # (key of the item before it in print, the unlisted section)
    for r in res["rows"]:
        if r["span"] and r["span"] in all_spans:
            if fp.squash(r["head"]) in SECTIONS_BEHIND.get(e.id, set()) and r["print"].strip() and fp.slugify(r["head"].rstrip(":").strip()) not in head_keys:
                # a row of the corpus (its code of conduct, under the proficiencies) that print sets as a paragraph of its own behind the last feature
                head = r["head"].rstrip(":").strip()
                key = fp.slugify(head)
                status, notes = r["status"], list(r["notes"]) + ["printed behind the class features, a row of the proficiencies in the corpus: an unlisted section"]
                if key in taken:
                    status = "hold"
                    notes.append(f"the new key `{key}` is a key of the class already")
                taken.add(key)
                new_items.append((items[-1]["key"], {"key": key, "line": -1, "head": head, "print": r["print"], "status": status, "notes": notes,
                                                      "level": 4, "unlisted": True}))
            last = r
            continue
        it = next((x for x in items if last is not None and x["head"] == last["head"]), None)
        opt = own_candidates(options.get(fp.namekey(r["head"])) or [], own, it["key"] if it else "")
        if opt and it is not None:                                  # an item of an option list that has its own entry (in a group of this class): a link under the feature
            it.setdefault("candidates", []).append((r["head"].rstrip("*").strip(), opt))      # the star after a name is print's book marker (ruling 26): the link replaces it
            continue
        if "head printed, not in the import" in " ".join(r["notes"]) and not is_table_para(r["head"]):
            # a printed head that the corpus lacks: an unlisted section, one level below the feature (a sub-head, ruling 15) or a rules box at the level
            # of the features (a sidebar title, ruling 41), with a new explicit key that no key of the class has
            head = r["head"]
            key = fp.slugify(fp.ABILITY_TAG.sub("", head))
            if (e.id, key) in BOX_AS_SECTION:
                if not re.search("^" + re.escape(BOX_AS_SECTION[(e.id, key)]) + r"\s*$", outside, re.M):
                    problems_extra.append(f"the box `{key}` is not the section `{BOX_AS_SECTION[(e.id, key)]}` of the corpus")
                continue                                          # the box is the corpus section `###`: written once, there (its text is checked by the coverage check)
            status, notes = r["status"], list(r["notes"])
            if key in taken:
                status = "hold"
                notes.append(f"the new key `{key}` is a key of the class already")
            taken.add(key)
            cut = co.incomplete_paragraph(r["print"])
            if cut:
                status = "hold"
                notes.append(f"print text may be cut at a page or column break: ...{cut}")
            prev = next((x for x in items if last is not None and x["head"] == last["head"]), None)
            after = prev["key"] if prev else (new_after.get(last["head"]) if last is not None else None)       # a section after an unlisted section stands after the same feature
            new_after[r["head"]] = after
            new_items.append((after, {"key": key, "line": -1, "head": head, "print": r["print"], "status": status, "notes": notes,
                                                          "level": 4 if fp.squash(head) in title_heads else 5, "unlisted": True}))
            if (e.id, key) not in PLACE_UNDER:
                last = r                                         # a sidebar that stands inside a list (the Witch's familiar box in the major hexes) leaves the list open
    for it in items:
        if it.get("candidates"):
            it["links"], unsure = pick_options(it.pop("candidates"))
            if unsure:
                it["status"] = "hold"
                it["notes"].insert(0, "option names with more than one entry of the class's groups: " + ", ".join(unsure))
        if re.search(r"[a-z][A-Z]", it["head"]) and fp.namekey(it["head"]) in {fp.namekey(t_) for _, t_, _ in heads}:
            it["head"] = next(t_ for _, t_, _ in heads if fp.namekey(t_) == fp.namekey(it["head"]))      # small capitals in the text layer ("Patron sPells")
    for after, sec in list(new_items):
        tail_to = SIDEBAR_TAILS.get((e.id, sec["key"]))
        if tail_to:
            # a sidebar that the corpus has as a section of its own after the class features (`### Fall from Grace`): not a second copy. The paragraph after
            # the box in the text layer is the end of the feature that the box interrupts; it goes back there. The rest of the box must be the section's text.
            sect = re.search(r"^### " + re.escape(sec["head"]) + r"\s*\n(.*?)(?=^### |\Z)", e.body, re.M | re.S | re.I)
            want = fp.squash(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", sect.group(1))) if sect else ""
            sents = re.split(r"(?<=[.!?])\s+", sec["print"].strip())
            host = next((x for x in items if x["key"] == tail_to), None)
            scored = [(difflib.SequenceMatcher(None, fp.squash(" ".join(sents[:k])), want).ratio(), k) for k in range(1, len(sents))]
            ratio, cut = max(scored, default=(0.0, 0))             # the end of the box that fits the section's text best
            if ratio < 0.97 or host is None:
                sec["status"] = "hold"
                sec["notes"].append(f"the box does not match the section `### {sec['head']}` of the corpus (ratio {ratio:.3f})")
                continue
            tail = " ".join(sents[cut:])
            host["print"] = host["print"].rstrip() + "\n\n" + tail
            host["notes"].append(f"print sets the last sentences of this feature after the box `{sec['head']}`")
            new_items.remove((after, sec))
            continue
        placed = PLACE_UNDER.get((e.id, sec["key"]))
        if placed:
            after, sec["level"] = placed
        at = next((n for n, x in enumerate(items) if x["key"] == after), len(items) - 1)
        while at + 1 < len(items) and items[at + 1].get("unlisted"):
            at += 1                                              # after the sections that already follow the feature, in print order
        items.insert(at + 1, sec)
    missing = [i["key"] for i in items if "head not printed" in i["notes"] and not i.get("drop") and not i.get("split_from")]      # a head that no rule resolved
    for it in items:
        tail_of = TAIL_OF_LINKED.get((e.id, it["key"]))
        if tail_of and tail_of[0] in it["print"]:
            cut = it["print"].index(tail_of[0])
            it["notes"].append(f"the end of the paragraph ({tail_of[0]}...) is the end of `{tail_of[1]}`, a link: it belongs to that entry, not here")
            it["print"] = it["print"][:cut].rstrip()
    cov_problems = coverage_check(corpus, e, items, blocks, title, heads, lacking, region, lines, options or {}, own)
    unresolved = {i["key"] for i in items if "head not printed" in i["notes"] and not i.get("drop") and not i.get("split_from")}
    problems = [x for x in res["problems"] if not (x.startswith("head not printed: ") and fp.slugify(x.split(": ", 1)[1]) not in unresolved and
                                                    not any(fp.namekey(i["head"]) == fp.namekey(x.split(": ", 1)[1]) and "head not printed" in i["notes"] for i in items))]
    return {"items": items, "extra": extra, "missing": missing, "window": len(win), "problems": problems + problems_extra + cov_problems, "region": region,
            "levels": fp.class_table_levels(corpus, e.id, cache)}


def bulletize(text: str) -> str:
    """The printed bullets of a paragraph as a Markdown list (ruling 45): the text layer sets each bullet as an italic run "_\u2022 Fatigued_: The target ...", all of
    them in the paragraph of the lead-in. The lead-in stays a paragraph; each bullet is an item "- Fatigued: The target ..."."""
    out = []
    for para in text.split("\n\n"):
        para = re.sub(r"_\u2022\s+", "_\u2022 ", para)
        if "_\u2022 " not in para:
            out.append(para)
            continue
        lead, *bullets = re.split(r"\s*_\u2022 ", para)
        if lead.strip():
            out.append(lead.strip())
        items = []
        for b in bullets:
            m = re.match(r"([^_]*)_:\s*(.*)$", " ".join(b.split()), re.S)
            items.append(f"- {m.group(1).strip()}: {m.group(2).strip()}" if m else "- " + " ".join(b.split()))
        out.append("\n".join(items))
    return "\n\n".join(out)


def feature_text(it: dict) -> str:
    """The text under a head: print's paragraphs; the items of an option list that have entries of their own are links after the lead-in."""
    text = re.sub(r"_([,;.:)]+) __(?=\s)", r"\1_", bulletize(it["print"].strip()))       # an empty emphasis after a punctuation mark: the punctuation belongs to the italics
    if it.get("links"):
        text += "\n\n" + "\n".join(f"- [{name}]({eid})" for name, eid in it["links"])
    return text


# The headings that structure a page and are no class features (`NOT_FEATURE_HEADINGS` of the app's `check_features.rs`): they stay out of `features`.
NOT_FEATURE_HEADINGS = {fp.squash(x) for x in (
    "Size", "Speed", "Attack", "AC", "Ability Scores", "Companion Type", "Prerequisites", "Effect", "Use", "Cost", "Action", "Bonus Spells", "Bonus Feats",
    "Weapon and Armor Proficiency", "Skills", "Alignment", "Weapon and Armor Proficiencies", "Weapon Proficiencies", "Armor Proficiency", "Armor Proficiencies",
    "Skill Ranks per Level", "Class Skills", "Armor Proficiency and Class Skills")}
# Level-4 sections that print sets behind the class features: sections of the page, no class features: (class entry, key)
NOT_CLASS_FEATURES = {("ref/class/antipaladin", "code-of-conduct"), ("ref/class/antipaladin", "associates")}
LEVEL_LEAD = re.compile(r"^(?:starting at |beginning at |starting with |at )(\d+)(?:st|nd|rd|th)\s+level\b", re.I)


def level_lead(text: str) -> int | None:
    """The level of an "At Nth level" or "Starting at Nth level" lead at the start of a paragraph (the app's `level_lead`)."""
    m = LEVEL_LEAD.match(text.strip())
    return int(m.group(1)) if m else None


def class_features(class_id: str, body: str, levels: dict[str, int]) -> list[tuple[str, int | None]]:
    """The `features` of a class, read from its body: (key, level) for each `####` head with its explicit anchor, in body order. A scaffold heading
    (proficiencies, skills) and a section that print sets behind the features are left out. The level is the one of an "At Nth level" lead in the
    first paragraph (the checker holds a stated level to it), else the lowest level at which the Special column of the class table lists the feature
    (`class_table_levels`; ruling 57), else none."""
    region = feature_region(body)
    if region is None:
        return []
    lines = body.split("\n")
    out: list[tuple[str, int | None]] = []
    for line, head, key in corpus_heads(lines, region):
        if fp.squash(fp.ABILITY_TAG.sub("", head)) in NOT_FEATURE_HEADINGS or (class_id, key) in NOT_CLASS_FEATURES:
            continue
        para = []
        for ln in lines[line + 1:region[1]]:
            if not ln.strip():
                if para:
                    break
                continue
            para.append(ln.strip())
        lead = level_lead(" ".join(para))
        out.append((key, lead if lead else levels.get(fp.first_level_key(head))))
    return out


def with_features(front: str, features: list[tuple[str, int | None]]) -> str:
    """The front matter with the `features` of the class as the last rows of `[fields]` (the rows of a class end the front matter; an earlier list is replaced)."""
    front = re.sub(r"^features = \[\n(?:  \{[^\n]*\},\n)*\]\n?", "", front.strip("\n") + "\n", flags=re.M).rstrip("\n")
    items = "".join("  { anchor = \"%s\"%s },\n" % (a, f", level = {l}" if l else "") for a, l in features)
    return front + "\nfeatures = [\n" + items + "]\n"


def settled(plan: dict) -> bool:
    return bool(plan["items"]) and not plan["extra"] and not plan["missing"] and not plan.get("problems") and all(i["status"] in ("print", "draft") for i in plan["items"] if not i.get("drop"))


def converted_body(body: str, plan: dict) -> str:
    """The class body with the text under each head replaced by print's, the head as print has it with the key written out, the class table and every
    other line as they were (rule 3 of AGENTS.md: no key moves)."""
    lines = body.split("\n")
    a, b = plan["region"]
    out = []
    for it in plan["items"]:
        if it.get("drop"):
            continue
        out += ["#" * it.get("level", 4) + f" {it['head']} {{#{it['key']}}}", "", feature_text(it), ""]
    return "\n".join(lines[:a] + out + lines[b:]) if out else body


def keys_that_move(class_id: str, old_body: str, new_body: str, plan: dict) -> list[str]:
    """The heading keys of the old body that the new body lacks, apart from the dropped heads (nothing points at them) and the keys of a box that the corpus has
    as a section (`BOX_AS_SECTION`). A key is public (AGENTS rule 3): the write stops when one would move."""
    gone = co.heading_keys(old_body) - co.heading_keys(new_body)
    allowed = {"sec-" + it["key"] for it in plan["items"] if it.get("drop")} | {it["key"] for it in plan["items"] if it.get("drop")}
    allowed |= {k for (c, k) in BOX_AS_SECTION if c == class_id}
    return sorted(gone - allowed)


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), fp.publication_title(corpus, book))
    if not pdf:
        raise SystemExit(f"no copy of the book {book} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    co.install_split([x.title for x in co.load_class_options(corpus)])
    options = option_title_keys(corpus)
    wanted = set(args.classes.split(",")) if args.classes else None
    total, cache, written = Counter(), {}, 0
    plans = []
    for e in co.load_entries(corpus, "class", book):
        if not e.id.startswith("ref/class/") or (wanted and e.id.rsplit("/", 1)[1] not in wanted):
            continue
        plans.append((e, compare_class(corpus, e, bk, cache, options, class_decisions(corpus, book))))
    # the other books are read after the class pages (reading another book first changes how the window of a class page is read)
    load_other_books(corpus, args.books, args.cache, book)
    for e, plan in plans:
        other_book_sections(e.id, plan["items"])
        c = Counter(x["status"] for x in plan["items"])
        total.update(c)
        links = sum(len(x.get("links", [])) for x in plan["items"])
        print(f"{e.id}: window {plan['window']} blocks; " + ", ".join(f"{k} {v}" for k, v in sorted(c.items()))
              + f"; heads not printed {len(plan['missing'])}; print heads not in the corpus {len(plan['extra'])}" + (f"; option links {links}" if links else ""))
        for x in plan["items"]:
            if x["status"] == "hold":
                print(f"    hold {x['head'][:34]}: {(x['notes'] or [''])[0][:100]}")
        if plan["extra"]:
            print("    print heads not in the corpus: " + ", ".join(plan["extra"][:8]))
        if args.write and settled(plan):
            body2 = converted_body(e.body, plan)
            moved = keys_that_move(e.id, e.body, body2, plan)
            if moved:
                raise SystemExit(f"{e.id}: the heading keys {moved} would move (only a dropped head without a reference may go)")
            front2 = with_features(e.front, class_features(e.id, body2, plan.get("levels", {}))) if WRITE_FEATURES else e.front.strip("\n") + "\n"
            co.write_atomic(e.path, "+++\n" + front2 + "+++\n" + body2)
            written += 1
            print("    written")
    print("total: " + ", ".join(f"{k} {v}" for k, v in sorted(total.items())) + (f"; {written} classes written" if args.write else ""))
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

    body = "Intro.\n\n### Class Features and Spells Per Day\n\n|Level|\n| --- |\n|1st|\n\n#### Spells {#spells}\n\n**Ability:** A.\n\n#### Mystery {#mystery}\n\nB.\n\n### Alternate Capstones\n\nC.\n"
    r = feature_region(body)
    eq(body.split("\n")[r[0]:r[1]][0], "#### Spells {#spells}", "the region starts at the first head")
    eq("### Alternate Capstones" in "\n".join(body.split("\n")[r[0]:r[1]]), False, "the region ends at the next ### heading")
    eq(feature_region("No heads here.\n"), None, "a class with no head has no region")
    eq((stem("Weapon and Armor Proficiencies"), stem("Weapon  and  Armor  Proficiency")), ("weapon and armor proficiency",) * 2, "a head in the plural and in the singular, with double spaces, is one head")
    eq(stem("Oracle's Curse (Ex)"), "oracle's curse", "a tag is not part of the stem")
    cl = "Intro.\n\n### Class Features\n\n|L|\n\n#### Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}\n\n**Weapons:** Simple.\n\n#### Mystery {#mystery}\n\nOld.\n\n### Alternate Capstones\n\nC.\n"
    reg = feature_region(cl)
    eq([(h, k) for _, h, k in corpus_heads(cl.split("\n"), reg)], [("Weapon and Armor Proficiencies", "weapon-and-armor-proficiencies"), ("Mystery", "mystery")], "the heads of the region with their keys")
    plan = {"region": reg, "items": [{"key": "weapon-and-armor-proficiencies", "head": "Weapon and Armor Proficiency", "print": "Oracles are proficient with simple weapons.", "status": "print"},
                                     {"key": "mystery", "head": "Mystery", "print": "Each oracle draws.", "status": "print", "links": [("Clouded Vision", "ref/oraclecurse/clouded-vision")]}],
            "extra": [], "missing": []}
    nb = converted_body(cl, plan)
    eq(("#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}" in nb, "**Weapons:**" in nb, "- [Clouded Vision](ref/oraclecurse/clouded-vision)" in nb, "### Alternate Capstones" in nb),
       (True, False, True, True), "owner calls 1, 2 and 4: print's head with the old key, no invented row, an option item as a link, the rest of the class as it was")
    eq("\n\n### Alternate Capstones" in nb, True, "a blank line stands before the next heading")
    eq(co.heading_keys(cl) <= co.heading_keys(nb), True, "no heading key of the class moves")
    eq(pick_options([("Concussive bomb", [("ref/discovery/concussive-bomb", "alchemist-discovery")])])[0], [("Concussive bomb", "ref/discovery/concussive-bomb")], "an option name has no star in its link text")
    eq(pick_options([("Clouded Vision", [("ref/oraclecurse/clouded-vision", "oracle-curse")]), ("Tongues", [("ref/shamanhex/tongues", "shaman-hex"), ("ref/oraclecurse/tongues", "oracle-curse")]),
                     ("Lame", [("ref/oraclecurse/lame", "oracle-curse")])])[0],
       [("Clouded Vision", "ref/oraclecurse/clouded-vision"), ("Tongues", "ref/oraclecurse/tongues"), ("Lame", "ref/oraclecurse/lame")], "owner call 4: a title that two groups share is linked from the group of the list")
    eq(LAYOUT_FIXES[("ref/class/summoner", "eidolon")][0][1], "the summoner's class level", "a known layout fix names the words of the table that the layer ran into a sentence")
    eq(WRITE_FEATURES, True, "owner call 5 answered: the `features` are written")
    body = "#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}\n\nAre proficient.\n\n#### Mystery {#mystery}\n\nAt 1st level, an oracle.\n\n#### Bomb (Su) {#bomb}\n\nA\nbomb.\n\n#### Spells {#spells}\n\nAt 4th level, an antipaladin casts.\n\n#### Code of Conduct {#code-of-conduct}\n\nText.\n\n### Next\n"
    eq(class_features("ref/class/oracle", body, {fp.first_level_key("Mystery"): 3, fp.first_level_key("Bomb"): 2}),
       [("mystery", 1), ("bomb", 2), ("spells", 4), ("code-of-conduct", None)], "a stated level wins over the class table, the table gives the level otherwise, scaffold heads are left out")
    eq(class_features("ref/class/antipaladin", body, {})[-1][0], "spells", "a section behind the features is no feature")
    eq(with_features("id = \"x\"\n[fields]\nskill_ranks = \"2\"\n", [("a", 1), ("b", None)]), 'id = "x"\n[fields]\nskill_ranks = "2"\nfeatures = [\n  { anchor = "a", level = 1 },\n  { anchor = "b" },\n]\n', "features are the last rows of the front")
    eq(with_features(with_features("[fields]\nx = 1\n", [("a", 1)]), [("a", 1)]), with_features("[fields]\nx = 1\n", [("a", 1)]), "an earlier list is replaced, not doubled")
    eq(re.match(r"^\(((?:Ex|Su|Sp)[^)]*)\):\s*", "(Sp): Starting at 1st level, a summoner").group(1), "Sp", "the tag that print leaves in the first run is found")
    eq((settled(plan), settled(dict(plan, extra=["X"])), settled(dict(plan, missing=["mystery"]))), (True, False, False), "a class is written all or nothing")
    P = fp.Para
    blocks = [P("title", [("Oracle", True, False)], 42, 1, 38), P("title", [("Class Features", True, False)], 42, 1, 18),
              P("para", [("Spells: A.", False, False)], 42, 1), P("title", [("Table 2–5: Oracle", True, False)], 44, 0, 24), P("para", [("1st +0", False, False)], 44, 0),
              P("para", [("Orisons: B.", False, False)], 45, 0), P("title", [("Alternate Capstones", True, False)], 46, 0, 18), P("para", [("Late.", False, False)], 46, 0)]
    eq([b.plain() for b in window(blocks)], ["Spells: A.", "1st +0", "Orisons: B."], "the window runs over a table (its title is no text) and ends at the next title")
    side = blocks[:3] + [P("title", [("Fall From Grace", True, False)], 46, 0, 24), P("para", [("Sidebar.", False, False)], 46, 0), P("title", [("Ex-Antipaladins", True, False)], 46, 0, 18)]
    eq([b.plain() for b in window(side)], ["Spells: A.", "Fall From Grace", "Sidebar."], "a sidebar title (larger) does not end the window, the next subsection does")
    eq(window([blocks[0]]), [], "a page without the Class Features title has no window")
    eq((prose_after_cells("6 6 6 6 6 6 due to encumbrance. At 5th level, you are immune to fatigue."), prose_after_cells("1st +0 +0 +0 +2 Mystery, oracle's curse, orisons 3 \u2014 \u2014")),
       ("due to encumbrance. At 5th level, you are immune to fatigue.", ""), "a sentence that the cells ran into stays, a table row with words in its cells does not")
    cutp = [P("para", [("A damage remains", False, False)], 44, 0), P("para", [("with the summoner. Effects", False, False)], 45, 0), P("para", [("Next: B.", True, False)], 45, 0)]
    eq([b.plain() for b in join_across_tables(cutp)], ["A damage remains with the summoner. Effects", "Next: B."], "a sentence that a table broke is joined, a new paragraph is not")
    mixed = P("para", [("Witch's Familiar (Ex)", True, False), (": At 1st level, a witch forms a bond.", False, False), ("    Spells per Day 0", True, False), (" 3 1 \u2014 \u2014 \u2014 \u2014 \u2014 \u2014 \u2014", False, False)], 67, 0)
    eq([x.plain() for x in split_table_runs(mixed)], ["Witch's Familiar (Ex): At 1st level, a witch forms a bond."], "a paragraph with prose and then a table keeps its prose")
    eq(split_table_runs(P("para", [("Plain: text.", False, False)], 1, 0)), None, "a paragraph without a table header run is left")
    eq((is_table_para("6 6 6 6 6 6 6 6 6"), is_table_para("1st +0 +0 +0 +2 Mystery, oracle's curse, orisons 3 \u2014 \u2014 \u2014"), is_table_para("Base Attack Fort Ref Will Level Bonus Save Save Save Special"),
        is_table_para("An oracle casts divine spells drawn from the cleric spell lists.")), (True, True, True, False), "the cells of a class table are no text of a feature")
    # the coverage check and the table handling (review of #373)
    eq(sentences("Short one. This sentence has enough letters to count. Another long enough sentence follows here."),
       ["This sentence has enough letters to count.", "Another long enough sentence follows here."], "sentences of at least twelve letters")
    eq(lost_sentences("Whenever an inquisitor uses her judgment ability, she can invoke true judgment. Regardless of whether the save is made, the target is immune for 24 hours.",
                      "Whenever an inquisitor uses her judgment ability, she can invoke true judgment."),
       ["Regardless of whether the save is made, the target is immune for 24 hours."], "a sentence that the written text lacks is lost (a cut in the middle of a paragraph)")
    eq(lost_sentences("This ability 4 4 3 3 is the equivalent of a spell of a level equal to one-third the level.", "This ability is the equivalent of a spell of a level equal to one-third the level."),
       [], "cells inside a sentence are no words of it")
    eq(lost_sentences("(Sp): Starting at 1st level, a summoner can cast summon monster.", "Starting at 1st level, a summoner can cast summon monster."), [], "the tag of a head stands in the head")
    eq(lost_sentences("Spells per Day 1 2 3 4 5 6 7 8 Whenever an inquisitor uses her judgment ability, she can invoke true judgment.", "Whenever an inquisitor uses her judgment ability, she can invoke true judgment.", {"spells"}),
       [], "a sentence behind the cells of a table is there when its words are")
    eq(last_cell_end("20th +15/+10/+5 +12 +6 +12 Unholy champion are determined for 24 hours".split()), 4, "the cells end after the numbers that follow the 20th of the last row, not at a number of the sentence")
    eq(last_cell_end("a b 3 4 c 24 hours".split()), 5, "without a last row, the last numeric token")
    eq(table_tail("|Level|Base Attack Bonus|Special|\n| --- | --- | --- |\n|1st|+0|Alchemy|\n|20th|+15|Grand discovery, x|\n\n|Level|0|1st|\n|20th|9|5|\n"), "Grand discovery", "the tail is the Special cell of the first table only")
    pb = fp.Para("para", [("+15/+10/+5 +12 +12 +6 Grand discovery Acid bomb*: When it", False, False)], 1, 0, 0)
    eq(strip_leading_cells(pb, "Grand discovery").plain(), "Acid bomb*: When it", "the last cells of a table and its last Special cell in front of a head go")
    eq(strip_leading_cells(fp.Para("para", [("Final revelation Deaf: You cannot hear", False, False)], 1, 0, 0), "Final revelation").plain(), "Deaf: You cannot hear", "the Special cell alone in front of a head goes")
    eq(strip_leading_cells(fp.Para("para", [("Unholy champion are determined", False, False)], 1, 0, 0), "Unholy champion"), None, "a tail in front of a lowercase word is a sentence that goes on")
    eq(strip_leading_cells(fp.Para("para", [("Spells per Day", True, False), (" away but closer", False, False)], 1, 0, 0), "").plain(), " away but closer", "the bold header of a table goes")
    eq((is_table_para("1 + 1 per 3 levels"), is_table_para("1st 2nd 3rd 4th"), is_table_para("Spells per Day"), is_table_para("6 6 6 6 6 6 5 5 4")), (False, True, True, True), "a progression in a sentence is no cells; ordinals and headers are")
    eq(bulletize("Choose from these. _\u2022 Fatigued_: The target is [fatigued](ref/misc/fatigued). _\u2022\nShaken_: The target is shaken."),
       "Choose from these.\n\n- Fatigued: The target is [fatigued](ref/misc/fatigued).\n- Shaken: The target is shaken.", "printed bullets are a Markdown list (ruling 45)")
    eq(bulletize("No bullets here."), "No bullets here.", "a paragraph without bullets stays")
    eq(re.sub(r"_([,;.:)]+) __(?=\s)", r"\1_", "use _[detect good](ref/x)_, __ as the spell"), "use _[detect good](ref/x),_ as the spell", "an empty emphasis after a comma is repaired")
    # option lists: only entries of the class's own groups, no fallback to another group
    own = {"inquisition": "domain", "bane": None}
    eq(own_candidates([("ref/blessing/destruction", "blessing"), ("ref/inquisition/justice", "inquisition")], own, "judgment"), [], "no entry of another class's group; a group tied to another feature is no list of this one")
    eq(own_candidates([("ref/inquisition/justice", "inquisition")], own, "domain"), [("ref/inquisition/justice", "inquisition")], "a group tied to this feature is linked")
    eq(own_candidates([("ref/x/a", "bane")], own, "judgment"), [("ref/x/a", "bane")], "a group of the class that is tied to no feature is linked from any list")
    eq(pick_options([("Tongues", [("ref/shamanhex/tongues", "shaman-hex"), ("ref/oraclecurse/tongues", "oracle-curse")]), ("Lame", [("ref/oraclecurse/lame", "oracle-curse")])]),
       ([("Tongues", "ref/oraclecurse/tongues"), ("Lame", "ref/oraclecurse/lame")], []), "the group of the list decides")
    eq(pick_options([("X", [("ref/a/x", "g1"), ("ref/b/x", "g2")])])[1], ["X"], "two entries in two groups, none chosen by the list: ambiguous, never the first")
    eq(pick_options([("X", [("ref/a/x", "g1"), ("ref/a/x2", "g1")])])[1], ["X"], "two entries of the chosen group: ambiguous")
    # keys: the write stops when a public key would go; a dropped head without a reference may go
    old = "#### A {#a}\n\ntext\n\n#### B {#b}\n\ntext\n"
    eq(keys_that_move("ref/class/x", old, "#### A {#a}\n\ntext\n", {"items": [{"key": "b"}]}), ["b"], "a key that goes without a drop is stopped")
    eq(keys_that_move("ref/class/x", old, "#### A {#a}\n\ntext\n", {"items": [{"key": "b", "drop": True}]}), [], "a dropped head goes")
    eq(keys_that_move("ref/class/witch", "#### A {#a}\n\n##### Learn from a Scroll {#learn-from-a-scroll}\n", "#### A {#a}\n", {"items": []}), [], "the keys of a box that the corpus has as a section go")
    # references: trades, links, deep links, option groups
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        cd = Path(td)
        (cd / "entries" / "arc-x").mkdir(parents=True)
        (cd / "entries" / "arc-x" / "a.md").write_text('trades = [{ feature = "alpha" }]\n', encoding="utf-8")
        (cd / "aliases.toml").write_text('old = "ref/class/x#beta"\n', encoding="utf-8")
        (cd / "history.toml").write_text('page = "ref/class/x#gamma"\n', encoding="utf-8")
        (cd / "option-groups.toml").write_text('[groups.g]\nclasses = ["ref/class/x"]\nfeature = "delta"\n', encoding="utf-8")
        eq([references(cd, "ref/class/x", k) for k in ("alpha", "beta", "gamma", "delta", "none")], [["a"], ["aliases.toml"], ["history.toml"], ["option-groups.toml"], []],
           "a trade, an old deep link, a retired page and an option group each point at a head; nothing else does")
    eq(settled({"items": [{"status": "print", "notes": []}], "extra": [], "missing": [], "problems": ["a problem of the comparison"]}), False, "a problem of the comparison holds the class")
    eq(sorted(NOT_FEATURE_HEADINGS), sorted(fp.squash(x) for x in ("Size", "Speed", "Attack", "AC", "Ability Scores", "Companion Type", "Prerequisites", "Effect", "Use", "Cost", "Action",
       "Bonus Spells", "Bonus Feats", "Weapon and Armor Proficiency", "Skills", "Alignment", "Weapon and Armor Proficiencies", "Weapon Proficiencies", "Armor Proficiency", "Armor Proficiencies",
       "Skill Ranks per Level", "Class Skills", "Armor Proficiency and Class Skills")), "the scaffold headings are the app's NOT_FEATURE_HEADINGS (check_features.rs)")
    # the gaps of the coverage check (review of #373)
    Pp = fp.Para
    gblocks = [Pp("title", [("Class Features", True, False)], 1, 0, 18), Pp("para", [("Last feature text.", False, False)], 1, 0), Pp("title", [("Box", True, False)], 1, 0, 18),
               Pp("para", [("A printed section between the features and the next head that the corpus lacks.", False, False)], 1, 0), Pp("title", [("Patron Spells", True, False)], 1, 0, 18),
               Pp("para", [("Patron text.", False, False)], 1, 0)]
    gap = gap_blocks(gblocks, gblocks[:2], {"patronspells"})
    eq([b.plain() for b in gap], ["A printed section between the features and the next head that the corpus lacks."], "the gap is the text between the window end and the next head that the corpus lacks")
    eq(gap_blocks(gblocks, gblocks[:2], {"patronspells"}, "box"), [], "the gap stops at a title whose section other entries hold (GAP_STOP)")
    eq(lost_sentences(" ".join(b.plain() for b in gap), "Last feature text. Patron text.", set()), ["A printed section between the features and the next head that the corpus lacks."],
       "a printed section that the entry lacks is lost")
    eq(lost_sentences("The alchemist can brew an elixir of life once per day at sixteenth level.", "An elixir of life: the alchemist can brew once. The alchemist has per day sixteenth level. At the level, brew life."), ["The alchemist can brew an elixir of life once per day at sixteenth level."],
       "a lost sentence whose words all stand elsewhere in the text is still lost (no allowance by the word set of the whole text)")
    eq(lost_sentences("The alchemist can brew an elixer of life once per day at sixteenth level.", "The alchemist can brew an elixir of life once per day at sixteenth level."), [],
       "a sentence that is nearly one written sentence (a letter differs) is there")
    eq(lost_sentences("The alchemist can brew an elixir of life once per day at sixteenth level.", "The alchemist can brew an elixir of life twice per day at sixteenth level."), ["The alchemist can brew an elixir of life once per day at sixteenth level."],
       "a changed word is not a misprint: the sentence is lost")
    eq(lost_sentences("This is the end (see the atonement spell), as appropriate to the case at hand.", "This is the end, as appropriate to the case at hand."), [], "a printed cross-reference is no difference")
    eq(pick_options([("Aid", [("ref/a/aid", "g1")]), ("Bar", [("ref/b/bar", "g2")]), ("Cat", [("ref/c/cat", "g1")])])[1], ["Bar"], "an item whose only entry is in another group than the list's is no link and no fallback")
    # the exact rules of the coverage check (review of #380): one character must not pass in a long sentence
    long_s = "While this dare is active, you gain a +2 dodge bonus to AC against attacks of opportunity made by any creature that you threaten in melee."
    eq(lost_sentences(long_s, long_s.replace("+2", "+3")), [long_s], "a changed digit is a loss (a ratio would pass it)")
    eq(lost_sentences("The creature can be affected by this spell if it fails the save against the effect.", "The creature cannot be affected by this spell if it fails the save against the effect."),
       ["The creature can be affected by this spell if it fails the save against the effect."], "a dropped or added negation is a loss")
    eq(lost_sentences("The creature can see the fiendish light that shines from the weapon of the antipaladin.", "The creature can hear the fiendish light that shines from the weapon of the antipaladin."),
       ["The creature can see the fiendish light that shines from the weapon of the antipaladin."], "one swapped word in a long sentence is a loss")
    eq(lost_sentences("An antipaladin who atones regains the abilities of his class (see the atonement spell).", "An antipaladin who atones regains the abilities of his class."), [], "a short cross-reference is no difference")
    eq(lost_sentences("An antipaladin who atones regains the abilities of his class (but not his weapon bond).", "An antipaladin who atones regains the abilities of his class."),
       ["An antipaladin who atones regains the abilities of his class (but not his weapon bond)."], "another parenthetical is text")
    eq(lost_sentences("An antipaladin who atones regains the abilities of his class (see page 41 of the book).", "An antipaladin who atones regains the abilities of his class."),
       ["An antipaladin who atones regains the abilities of his class (see page 41 of the book)."], "a reference with a number is text")
    table = "Base Attack Fort Ref Will Level Bonus Save Save Save Special 1st +0 +2 +0 +2 Aura 20th +15/+10/+5 +12 +6 +12 True judgment"
    eq(lost_sentences("The character gains a 6 bonus on checks " + table + " purpose of overcoming damage.", "The character gains a 3 bonus on checks. Purpose of overcoming damage."),
       ["The character gains a 6 bonus on checks " + table + " purpose of overcoming damage."], "a number before a class table in the sentence is compared too")
    eq(lost_sentences("The character gains a 3 bonus on checks " + table + " purpose of overcoming damage.", "The character gains a 3 bonus on checks. Purpose of overcoming damage.", {"aura", "true", "judgment"}), [],
       "the words before and after a class table stand in the text: the sentence is there")
    eq(lost_sentences("The character gains a bonus " + table + " the end.", "The character gains a bonus."), ["The character gains a bonus " + table + " the end."], "a short run after the table must stand too")
    gb = [Pp("title", [("Class Features", True, False)], 1, 0, 18), Pp("para", [("Last feature text.", False, False)], 1, 0), Pp("para", [("1st +0 +2 +0 +2 2nd +1 +3 +0 +3", False, False)], 1, 0),
          Pp("para", [("Text of a section.", False, False)], 1, 0), Pp("title", [("Next Class", True, False)], 2, 0, 38), Pp("para", [("Next class text.", False, False)], 2, 0)]
    eq([b.plain() for b in gap_blocks(gb, gb[:2], set(), "")], ["Text of a section."], "the gap skips the paragraph of cells and stops at a large title")
    eq([b.plain() for b in gap_blocks(gb, gb[:2], set(), "")] == [b.plain() for b in gap_blocks(gb, gb[:2], set())], True, "an empty stop title stops nothing")
    for line in bad:
        print("FAIL", line)
    print(f"self-test: {ok} checks passed" if not bad else f"self-test: {len(bad)} failures")
    return 1 if bad else 0


def run_features(args) -> int:
    """The `features` of the base classes that are written already, read from their bodies (no print needed). Idempotent."""
    corpus = Path(args.corpus).resolve()
    wanted = set(args.classes.split(",")) if args.classes else None
    cache: dict = {}
    n = 0
    for e in co.load_entries(corpus, "class", args.book):
        if not e.id.startswith("ref/class/") or (wanted and e.id.rsplit("/", 1)[1] not in wanted):
            continue
        feats = class_features(e.id, e.body, fp.class_table_levels(corpus, e.id, cache))
        front2 = with_features(e.front, feats)
        if front2 != e.front.strip("\n") + "\n":
            co.write_atomic(e.path, "+++\n" + front2 + "+++\n" + e.body)
            n += 1
        print(f"{e.id}: {len(feats)} features, levels " + ", ".join(f"{k}={l}" for k, l in feats if l)[:300] + "; none: " + ", ".join(k for k, l in feats if not l))
    print(f"{n} entries changed")
    if n and args.checker:
        import subprocess
        subprocess.run([args.checker, "fmt", str(corpus)], check=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(HERE.parent))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--book")
    ap.add_argument("--classes")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    ap.add_argument("--features", action="store_true", help="write the `features` of the written classes of --book from their bodies")
    ap.add_argument("--write", action="store_true", help="write the classes whose items are all settled (the others are reported)")
    ap.add_argument("--checker", help="the cast-iron-corpus binary: `fmt` runs after a write")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.features:
        return run_features(args)
    if args.compare:
        return run_compare(args)
    ap.error("one of --self-test, --compare, --features")


if __name__ == "__main__":
    sys.exit(main())
