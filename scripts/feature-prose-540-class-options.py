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
    feature-prose-540-class-options.py [CORPUS] --ability-type --book ID  ruling 63: off until the app reads `ability_type`
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import re
import sys
import tomllib
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
                                 section_of(blocks, i), e.book or "", e.page))
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


INVERTED_HEAD = re.compile(r"^(.+?),\s*(Lesser|Greater|Improved|Mass)(\s*\([A-Za-z]{2}\))?\s*:?$")


VARIANT_FIRST = re.compile(r"^(Lesser|Greater|Improved|Mass) ")


def inverted(name: str) -> str:
    m = re.match(r"^(Lesser|Greater|Improved|Mass) (.+?)(\s*\([A-Za-z]{2}\))?$", name)
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


def install_split(names: list[str]) -> None:
    """The print reader takes an italic paragraph start as a head only when the entry expects that name. A page of class options sets
    the powers of other entries beside the entry's own (the evolutions are italic heads in one list), so every name of the book is
    expected, and a power's text ends at the next power of the page."""
    EXTRA_NAMES[:] = list(names) + [inverted(n) for n in names if VARIANT_FIRST.match(n)]      # print sets the variant behind the name, in italics
    if not getattr(fp.split_print, "_class_options", False):
        orig = fp.split_print

        def wrapped(section, expected):
            # a printed section heading ("2-Point Evolutions", "Base Forms") ends the text of the power above it: it stands as a head of its own
            section = section[:1] + [title_as_head(q) for q in section[1:]]
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


TAG = re.compile(r"\s*\(([^()]*)\)\s*:?$")
TAG_WORDS = re.compile(r"(?:Ex|Su|Sp)(?:\s*(?:,|or|and|/)\s*(?:Ex|Su|Sp))*")
TRADE_LABEL = re.compile(r"^\*\*(?:Replaces?|Alters?|Modifies):\*\*", re.M)
LABEL_ROW = re.compile(r"^\*\*[^*\n]+:\*\*", re.M)           # an import row: a bold label with its colon
WRITE_ABILITY_TYPE = False                                   # ruling 63: `[fields] ability_type`; off until the app reads the key


def ability_tag_of(name: str) -> str:
    """The printed ability tag of a power name, without the parentheses: "Su", "Ex or Sp", "Su, Sp"; "" when the name has none."""
    m = TAG.search(name)
    return m.group(1).strip() if m and TAG_WORDS.fullmatch(m.group(1).strip()) else ""


def with_ability_type(front: str, tag: str) -> str:
    """The `[fields]` of an entry with `ability_type = "<tag>"` after `kind` (ruling 63); an entry that has it is left."""
    if not tag or re.search(r"^ability_type = ", front, re.M):
        return front
    out, n = re.subn(r'(^\[fields\]\nkind = "class_option"\n)', lambda m: m.group(1) + f'ability_type = "{tag}"\n', front, count=1, flags=re.M)
    assert n == 1, "a class option has `[fields]` with its kind"
    return out


def outside_rows(body: str) -> list[str]:
    """The labels of the import rows that stand outside every power (Details, Spells, Gained class skills, ...): a power rewrite does not
    reach them, and they would stay in a converted entry (no transcription from print yet)."""
    blocks = rw.parse_blocks(body.split("\n"))
    inside = {i for c in rw.candidates(blocks, True) for i in range(c.start, c.end)}
    return sorted({b.label for i, b in enumerate(blocks) if b.kind == "row" and i not in inside})


def section_of(blocks, start: int) -> str:
    """The text of the nearest section heading above a block ("" before the first)."""
    for i in range(start - 1, -1, -1):
        if blocks[i].kind == "boundary" and blocks[i].text.startswith("#"):
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
        if any(f"]({target})" in text[a:b] for a, b in sentences):
            continue                                                            # the prerequisite sentence links the item already
        hit = (in_frame or plain or [None])[0]
        if hit:
            text = text[:hit.start()] + f"[{hit.group(0)}]({target})" + text[hit.end():]
        elif not any(f"]({target})" in text[a:b] for a, b in spans):
            lost.append(name)
    return text, lost


STOP_TITLES: set[str] = set()          # squash of the title of every class option: another one ends a section


def anchor_section(blocks: list, title: str) -> list | None:
    """The blocks of a multi-power entry from the printed title of the entry to the next title of another class option (or any larger
    title): the window is anchored at the title, so a head of a neighbour that follows on the page is not read as the entry's power. None
    when the title is not printed on those pages."""
    key = fp.squash(re.sub(r"\s*\((?:[A-Z]{2,4}|HotW)\)\s*$", "", title))
    at = next((i for i, b in enumerate(blocks) if b.kind == "title" and fp.squash(b.plain()) in (key, key + "bloodline", key + "mystery", key + "school")), None)
    if at is None:
        return None
    for j in range(at + 1, len(blocks)):
        b = blocks[j]
        if b.kind == "title" and (fp.squash(b.plain()) in STOP_TITLES - {key} or b.size > blocks[at].size):
            return blocks[at + 1:j]
    return blocks[at + 1:]


HEADING_FAMILIES = {"evolution"}     # ruling 61: an evolution opens with the printed sentence of its group heading ("2-Point Evolutions: The following ...")


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


def compare_one(e, book, bk, other=None) -> list[dict]:
    """The rows of one entry: one per power, from the shared print comparison of the archetype pass."""
    shape, n = shape_of(e.body)
    base = {"entry": e.id, "shape": shape, "page": e.page, "span": "", "note": ""}
    powers = powers_of(e)
    _, feats = fp.parse_import(e.body, set())
    by_name: dict[str, list] = {}
    for f in feats:
        by_name.setdefault(re.sub(r":$", "", f.name), []).append(f)
    if not e.page.isdigit():
        return [dict(base, feature=n_, anchor=fp.anchor_of(n_), verdict="nopage", status="hold", level_import="", level="",
                     note="no page is cited", span_sha256=sha) for n_, sha in powers]
    page = int(e.page)
    last = page + (3 if shape == "multi" else 1)
    blocks = fp.read_blocks(bk, max(1, page + fp.PAGE_OFFSET[0] - 1), min(last + fp.PAGE_OFFSET[0], max(bk.pages)))
    unanchored = False
    if shape == "multi":
        anchored = anchor_section(blocks, e.title)
        if anchored is None:
            unanchored = True
        else:
            blocks = anchored
    section = [fp.Para("title", [(e.title, True, False)], page, 0, 20)] + blocks
    res = fp.compare_entry(e, section, bk)
    by_span = {r["span"]: r for r in res["rows"] if r["span"]}
    where = {}                                       # span -> "Publication p. N" of a power that another source of the entry prints
    for src in (e.data.get("sources") or [])[1:]:
        pub, pg = src.get("publication"), str(src.get("page", ""))
        def not_printed(sp):                    # no row, or the print comparison found no head on the cited pages
            return sp not in by_span or any("head not printed" in n_ for n_ in by_span[sp]["notes"])
        missing = [f for f in feats if not_printed(f.span_sha())]
        if not missing or other is None or not pg.isdigit():
            continue
        got = other(pub, int(pg), e, shape)
        if got is None:
            continue
        for sp, r2 in got.items():
            if not_printed(sp) and not any("head not printed" in n_ for n_ in r2["notes"]):
                by_span[sp] = r2
                where[sp] = (pub, pg)
    rows, seen = [], Counter()
    blocks_b = rw.parse_blocks(e.body.split("\n"))
    cands = rw.candidates(blocks_b, True)
    promo = promoted(blocks_b, cands)
    info = {rw.span_sha(blocks_b[c.start:c.end]): (section_of(blocks_b, c.start), promo.get(c.start - 1)) for c in cands}
    problems = []                                       # what holds every power of the entry
    if unanchored:
        problems.append("the printed title of the entry is not on the cited pages: the window is not anchored")
    outside = outside_rows(e.body)
    if outside:
        problems.append("import rows outside the powers (" + ", ".join(outside[:4]) + ") are not transcribed from print yet")
    if TRADE_LABEL.search(e.body):
        problems.append("a trade row (Replaces/Alters): class-option trades are not written yet")
    taken = set(re.findall(r"\{#([^}]+)\}", e.body))
    plinks = prereq_links(e.body)
    anchors_seen: Counter = Counter()
    for name, sha in powers:
        seen[name] += 1
        f = by_name.get(name, [None] * seen[name])[seen[name] - 1] if name in by_name else None
        r = by_span.get(f.span_sha()) if f is not None else None
        if r is not None and f.span_sha() in where:
            r = dict(r, notes=[f"printed in {where[f.span_sha()][0]} p. {where[f.span_sha()][1]}"] + list(r["notes"]))
        section, pr = info.get(sha, ("", None))
        src = where.get(f.span_sha()) if f is not None else None           # a power that another source of the entry prints has its own book and page
        common = dict(base, feature=name, section=section, book=src[0] if src else book, by="", ability_tag=ability_tag_of(name) if shape == "single" else "",
                      reviewed_537="yes" if (e.id, sha) in REVIEWED else "", links_lost="", span_sha256=sha)
        if r is None:
            rows.append(dict(common, anchor=fp.anchor_of(name), verdict="missing-head", status="hold", level_import="",
                             level="", note="head not printed on the cited page and the next ones", print="", print_sha256=""))
            continue
        verdict = {"draft": "agree", "print": "differ", "hold": "hold"}[r["status"]]
        note_r = f"resolution of #537: {REVIEWED[(e.id, sha)]}" if (e.id, sha) in REVIEWED else ""
        notes = [n_ for n_ in r["notes"] if n_] + ([note_r] if note_r else [])
        status, printed = r["status"], r["print"]
        anchor = pr[1] if pr else r["anchor"]
        anchors_seen[anchor] += 1
        if anchors_seen[anchor] > 1 or (anchor in taken and not pr):
            notes.append(f"anchor collision: {anchor}")
            status = "hold"
        if shape == "single" and fp.namekey(name) != fp.namekey(e.title) and fp.namekey(inverted(name)) != fp.namekey(e.title):
            notes.append("the power's name differs from the title of the entry")
            status = "hold"
        if problems:
            notes += problems
            status = "hold"
        if src:
            common["page"] = src[1]
        if shape == "single":
            printed, lost = place_links(printed, plinks)
            common["links_lost"] = "|".join(lost)
        if shape == "single" and e.id.split("/")[1] in HEADING_FAMILIES:
            gh = group_map(bk).of(e.title, page)
            if gh is None:
                notes.append("no group heading found above the head")
                status = "hold"
            elif gh[1] > page:
                notes.append(f"the group heading is on p. {gh[1]}, after the cited p. {page}")
                status = "hold"
            else:
                printed = gh[0] + "\n\n" + printed
                if gh[1] < page:
                    common["page"] = f"{gh[1]}-{page}"           # the sentence is on the page before: the entry cites both (ruling 61)
        decided = DECISIONS.get((e.id, anchor))
        if decided and decided[0] == "print" and status == "hold" and r["status"] == "hold" and not problems:
            status = "print"
            notes.append(f"decision: {decided[1]}")
        rows.append(dict(common, anchor=anchor, verdict=verdict, status=status,
                         level_import=r["level_import"] if r["level_import"] is not None else "",
                         level=level_of(r["print"]) or "", note="; ".join(notes)[:400], print=printed,
                         print_sha256=hashlib.sha256(printed.encode()).hexdigest()))
    return rows


DECISIONS: dict[tuple[str, str], tuple[str, str]] = {}


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    title = fp.publication_title(corpus, book)
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    families = set(args.families.split(",")) if args.families else None
    everything = load_class_options(corpus, book)
    names: list[str] = []
    for x in load_class_options(corpus):
        names.append(x.title)                      # a converted option has no import row left, but its italic head still ends the text above it
        if shape_of(x.body)[0] != "none":
            for f in fp.parse_import(x.body, set())[1]:
                names += [f.name, fp.tail_name(f.name)]
    install_split(names)
    STOP_TITLES.clear()
    STOP_TITLES.update(fp.squash(re.sub(r"\s*\((?:[A-Z]{2,4}|HotW)\)\s*$", "", x.title)) for x in load_class_options(corpus))
    fp.KNOWN_OPTIONS[:] = [fp.item_tokens(x.title) for x in load_class_options(corpus)]      # ruling 60: a sentence that names a longer option holds
    REVIEWED.update(reviewed_spans(corpus))
    DECISIONS.clear()
    DECISIONS.update(read_decisions(decisions_file(corpus, book)))
    books_seen: dict[str, object] = {}

    def other(pub: str, pg: int, e, shape: str):
        """The comparison of an entry against another book that prints some of its powers (an elemental bloodline is in Advanced Player's
        Guide p. 136 and Ultimate Magic p. 72): its rows by span, or None when there is no copy of that book."""
        if pub not in books_seen:
            fp.configure_book(pub)
            pdf2 = fp.find_pdf(Path(args.books), fp.publication_title(corpus, pub))
            books_seen[pub] = fp.load_book(fp.book_xml(pdf2, Path(args.cache))) if pdf2 else None
        bk2 = books_seen[pub]
        if bk2 is None:
            return None
        fp.configure_book(pub)
        try:
            last2 = pg + (3 if shape == "multi" else 1)
            blocks2 = fp.read_blocks(bk2, max(1, pg + fp.PAGE_OFFSET[0] - 1), min(last2 + fp.PAGE_OFFSET[0], max(bk2.pages)))
            res2 = fp.compare_entry(e, [fp.Para("title", [(e.title, True, False)], pg, 0, 20)] + blocks2, bk2)
            return {r["span"]: r for r in res2["rows"] if r["span"]}
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
                props.setdefault(e.id, {"id": e.id, "feature": []})["feature"].append({"anchor": r["anchor"], "print": r["print"]})
            rows.append(r)
    twice: dict[tuple[str, str, str], set[str]] = {}
    for r in rows:                                  # one printed paragraph claimed by two entries holds both: an owner decides whose it is
        if r["print_sha256"]:
            twice.setdefault((r["book"], fp.namekey(r["feature"]), r["print_sha256"]), set()).add(r["entry"])
    for r in rows:
        if r["print_sha256"] and len(twice[(r["book"], fp.namekey(r["feature"]), r["print_sha256"])]) > 1:
            r["note"] = (r["note"] + "; " if r["note"] else "") + "the print head matches more than one entry: " + ", ".join(sorted(twice[(r["book"], fp.namekey(r["feature"]), r["print_sha256"])]))[:120]
            r["status"] = "hold" if r["status"] in SETTLED else r["status"]
    old = read_tsv(tsv_file(corpus, book))
    old_props = read_props(proposals_file(corpus, book))
    compared = {r["entry"] for r in rows}
    kept = [r for r in old if r["status"] == LEDGER and r["entry"] not in compared]       # the ledger of the entries written already
    for r in kept:
        if (r["entry"], r["anchor"]) in old_props:
            props.setdefault(r["entry"], {"id": r["entry"], "feature": []})["feature"].append(
                {"anchor": r["anchor"], "print": old_props[(r["entry"], r["anchor"])]})
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


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["\t".join(HEADER)]
    for r in rows:
        lines.append("\t".join(str(r.get(k, "")).replace("\t", " ").replace("\n", " ") for k in HEADER))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
    path.write_text("\n".join(out), encoding="utf-8")


def read_props(path: Path) -> dict[tuple[str, str], str]:
    if not path.exists():
        return {}
    return {(x["id"], x["anchor"]): x["print"] for x in tomllib.loads(path.read_text(encoding="utf-8")).get("entry", [])}


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
        keep_before = [b.text for b in blocks[:c.start]]
        keep_after = [b.text for b in blocks[c.end:]]
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
    """The first `[[sources]]` page row of the entry file set to `page`."""
    return re.sub(r'(\[\[sources\]\]\n(?:[^\n]*\n)*?page = )"[^"]*"', lambda m: m.group(1) + f'"{page}"', text, count=1)


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
        e.path.write_text(text, encoding="utf-8")
        done += 1
    print(f"group headings: {done} entries changed, {skipped} not changed")
    return 0


def heading_keys(body: str) -> set[str]:
    """The URL keys of the headings of a body: an explicit `{#key}`, else the derived key of the heading text."""
    keys = set()
    for ln in body.split("\n"):
        m = re.match(r"^#{1,6}\s+(.*?)(?:\s*\{#([^}]+)\})?\s*$", ln)
        if m:
            keys.add(m.group(2) or fp.slugify(m.group(1)))
    return keys


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
        if shape == "none" or not mine or any(r["status"] not in SETTLED for r in mine):
            continue
        blocks = rw.parse_blocks(e.body.split("\n"))
        texts, levels, anchors = {}, {}, {}
        for r in mine:
            texts[r["span_sha256"]] = props[(e.id, r["anchor"])]
            levels[r["span_sha256"]] = int(r["level"]) if r["level"] else None
            anchors[r["span_sha256"]] = r["anchor"]
        body, features = convert_body(e, texts, levels, anchors, shape)
        keep = heading_keys(e.body)
        lost = keep - heading_keys(body)
        assert not lost, f"{e.id}: the keys {sorted(lost)} would move"                  # rule 3 of AGENTS.md: the keys of the headings stay
        front = features_front(e.front, features) if features else e.front
        own = [r for r in mine if r["book"] == book]
        if own and own[0]["page"] and own[0]["page"] != e.page:
            front = with_page(front, own[0]["page"])
        e.path.write_text("+++\n" + front.strip("\n") + "\n+++\n" + body, encoding="utf-8")
        for r in mine:
            r["status"] = LEDGER
        converted += 1
    if converted:
        write_tsv(tsv_file(corpus, book), rows)
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
    done = 0
    for e in load_class_options(corpus, args.book):
        mine = [r for r in rows if r["entry"] == e.id and r["status"] == LEDGER and r["shape"] == "single" and r["ability_tag"]]
        if mine:
            new = with_ability_type(e.front, mine[0]["ability_tag"])
            if new != e.front:
                e.path.write_text(e.path.read_text(encoding="utf-8").replace(e.front, new, 1), encoding="utf-8")
                done += 1
    print(f"ability_type: {done} entries changed")
    return 0


# ---- the check -----------------------------------------------------------------------------------

def norm(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)).strip()


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
                if shape != "none" or LABEL_ROW.search(e.body):
                    errors.append(f"{eid}: written, but the entry still holds an import row or label")
                body = norm(e.body)
                for r in mine:
                    text = props.get((eid, r["anchor"]))
                    if text is not None and norm(text) not in body:
                        errors.append(f"{eid}: written, but the printed text of `{r['anchor']}` is not in the entry")
                continue
            if shape == "none":
                if mine and any(r["status"] not in SETTLED + (LEDGER,) for r in mine):
                    errors.append(f"{eid}: no import row is left, but the table has an unsettled row")
                continue
            if not mine:
                pending += 1                  # a part of the book that no batch has compared yet: reported, not an error
                continue
            have = {r["span_sha256"] for r in mine}
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
    ok, bad = 0, []

    def eq(a, b, what):
        nonlocal ok
        if a == b:
            ok += 1
        else:
            bad.append(f"{what}: {a!r} != {b!r}")

    eq(inverted("Greater Beast Totem (Su)"), "Beast Totem, Greater (Su)", "print sets the variant behind the name")
    eq(inverted("Beast Totem"), "Beast Totem", "a name without a variant stays")
    eq(INVERTED_HEAD.match("Beast Totem, Greater (Su)").groups(), ("Beast Totem", "Greater", " (Su)"), "the inverted head is read")
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
    eq((title_as_head(fp.Para("title", [("Table 2\u20139: Eidolon Base Statistics", True, False)], 59, 0, 18)).runs[0][1],
        title_as_head(fp.Para("title", [("2-Point Evolutions", True, False)], 61, 0, 18)).runs[0][1]), (False, True),
       "ruling 62: the title of a table stays in the text of the power, a section heading ends it")
    cls = type("C", (), {"body": "\n### Class Features\n\n#### Alchemy (Su) {#alchemy}\n\nAt 1st level, an alchemist.\n\n#### Swift Alchemy (ex)\n\nAt 4th level.\n", "book": "x", "page": "1"})()
    eq([(q.name, q.anchor, q.head_level, q.section) for q in power_records(cls, "class")],
       [("Alchemy (Su)", "alchemy", 4, "Class Features"), ("Swift Alchemy (ex)", "swift-alchemy", 4, "Class Features")], "the powers of a base class are its #### heads, with their keys")
    eq([(q.name, q.head_level) for q in power_records(type("S", (), {"body": "\n**Animal Fury (Ex)**\n\n**Ability:** A bite attack.\n", "book": "x", "page": "1"})(), "class_option")], [("Animal Fury (Ex)", 0)], "the powers of a class option are its import names")
    eq(power_records(cls, "none"), [], "a rule entry has no power of its own")
    STOP_TITLES.clear()
    STOP_TITLES.update({"aquatic", "boreal", "deepearth"})
    ab = [P("title", [("Aquatic", True, False)], 136, 0, 18), P("para", [("Dehydrating Touch (Sp)", True, False), (": A touch.", False, False)], 136, 0),
          P("title", [("Boreal", True, False)], 136, 1, 18), P("para", [("Freezing Bolt (Sp)", True, False), (": A bolt.", False, False)], 136, 1)]
    eq([q.plain()[:8] for q in anchor_section(ab, "Aquatic")], ["Dehydrat"], "item 3: the section of an entry ends at the title of the next class option")
    eq(anchor_section(ab, "Serpentine"), None, "item 3: a title that is not printed gives no window")
    eq([q.plain()[:6] for q in anchor_section(ab, "Boreal")], ["Freezi"], "item 3: the window starts at the entry's own title")
    STOP_TITLES.clear()
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
    body, feats = convert_body(E, {sha(single, 0): "At 1st level, a bite."}, {}, {})
    eq(body.strip(), "At 1st level, a bite.", "a single-power body is the printed paragraphs, no head, no features")
    eq(feats, [], "a single-power option gets no `features`")
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
    eq(with_ability_type('id = "x"\n[fields]\nkind = "class_option"\ngroup = "hex"', "Su"), 'id = "x"\n[fields]\nkind = "class_option"\nability_type = "Su"\ngroup = "hex"', "ruling 63: the key follows the kind")
    eq(with_ability_type('[fields]\nkind = "class_option"\nability_type = "Ex"\n', "Su"), '[fields]\nkind = "class_option"\nability_type = "Ex"\n', "ruling 63: a key that is there stays")
    eq(WRITE_ABILITY_TYPE, False, "ruling 63: the writer is off until the app reads the key")
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
    eq(heading_keys(sec) <= heading_keys(body3) | {"final-revelation"}, True, "the keys of the headings stay (the promoted one by its written key)")
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
    eq(place_links("It has [claws](ref/evolution/claws).", [("claws", "ref/evolution/claws"), ("tail", "ref/evolution/tail")]),
       ("It has [claws](ref/evolution/claws).", ["tail"]), "ruling 60: an item that stands nowhere is reported")
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
    ap.add_argument("--ability-type", action="store_true", help="ruling 63: write ability_type for the written single-power entries (off until the app reads the key)")
    ap.add_argument("--checker", help="the cast-iron-corpus binary: `--write` runs its `fmt` afterwards")
    ap.add_argument("--book")
    ap.add_argument("--families")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.compare:
        return run_compare(args)
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
