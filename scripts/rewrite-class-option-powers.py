#!/usr/bin/env python3
"""Rewrite class-option powers into the canonical row order (phynics/cast-iron-data#88).

The spec is the decision `2026-11-20-class-option-power-layout` of phynics/cast-iron (sections 1
and 2, "Rewrite and survey algorithm", "Fixtures"), its correction
`2026-11-21-class-option-power-counts` and the owner's answers
`2026-11-21-class-option-power-owner-cases` (the "What the data rewrite must change" list). The
app's `cast_iron_schema::power` is the one classifier and validator; `cargo xtask corpus-check`
runs it on this corpus. This script mirrors it over source text, rewrites what it can without
guessing, and queues everything else for print review with the whole span unchanged.

Everything that mirrors the app lives in one place, the section "the mirror of the app": the
labels, the ranks of the canonical order, the section labels that are never powers, the level
grammar, the classifier, candidate discovery and `validate`. When the app's rules change, change
that section and the "emit" step of `rewrite_run`, and nothing else.

Usage
-----
    scripts/rewrite-class-option-powers.py --self-test
    scripts/rewrite-class-option-powers.py [CORPUS]            dry run: print the counts
    scripts/rewrite-class-option-powers.py [CORPUS] --write    rewrite the entries, write the queue
    scripts/rewrite-class-option-powers.py [CORPUS] --write-queue   write the queue only
    scripts/rewrite-class-option-powers.py [CORPUS] --write --resolutions-only
                                                               apply the resolutions, nothing else
    scripts/rewrite-class-option-powers.py [CORPUS] --check    exit 1 unless a rerun changes nothing

CORPUS defaults to the repository that holds this script. `--families a,b` limits the rewrite
to the entry ids `ref/a/...` and `ref/b/...` (the queue file always covers the whole corpus).
`--write` leaves long lines: run `cargo xtask corpus-fmt <corpus>` after it.

Files
-----
`scripts/class-option-power-queue.tsv`
    One line per power that stays unchanged for hand review: entry id, original name as written
    (with any colon), occurrence among the candidates with that name in the entry, the SHA-256
    of the original span, and the reasons.

`power-exceptions.toml` (corpus root; read by `cargo xtask corpus-check` too)
    The powers that print cannot settle and that stay in a non-canonical form on purpose: one
    `[[exception]]` each with `id`, `name`, `occurrence`, `span_sha256` (the hash of the original
    span, as for a resolution), `reason` and `print` (book title and page, or why none exists).
    The app's check skips a failing power that this file names. The script checks the file:
    an exception applies only to the exact span it was made for; an exception whose span changed
    is stale, one that matches no candidate is orphaned, and one whose power passes validation
    is obsolete (an action-first pair passes validation, so it waits in the queue and is never an
    exception). `--check` and `--write` fail on each until it is removed or redone. An excepted
    power leaves the review queue. The file is read as strictly as the app reads it.

`scripts/class-option-power-resolutions.toml`
    The hand-made replacements, one `[[resolution]]` each: `id`, `name`, `occurrence`,
    `span_sha256`, `print` (book and page) and `replacement`: a power that passes validation,
    then any blocks that belong after it (a list that print sets as bullets). A resolution
    applies only when the current span hashes to `span_sha256`. A span that already equals the
    replacement is left alone. Any other span is a stale resolution, and `--check` and `--write`
    fail until it is removed or redone. If that span fails validation, the power is queued again
    with the reason `stale-resolution` and the automatic rewrite does not touch it; a stale span
    that already validates stays valid, and the stale resolution is only reported. A resolution
    whose key matches no candidate is orphaned, and one for a section label that is no longer a
    candidate (Base Evolutions, ...) is obsolete: both are reported, and `--check` and `--write`
    fail until they are removed.

Converted entries (phynics/cast-iron#540)
-----------------------------------------
An entry that the print rewrite (`scripts/feature-prose-540.py`) has converted holds no import rows
any more: no `Gained` or effect row, no `Action` row, no upgrade lead and no plain-text upgrade, so it
has no power candidate and is out of the scope of this script. The marker is that absence, not
`features`: a single-power class option has no `features` (owner ruling 1 of 2026-11-24), a multi-power
one has them, and an entry that never had import rows (the 705 kinetic talents, companions, and so on)
is out of scope the same way. A resolution or an exception whose entry is out of scope is `retired`,
not orphaned: `--check` reports the count and does not fail on it. A key whose entry has import rows
that do not match, or whose entry is gone from the corpus, is orphaned as before. The resolutions file
stays what it was, print-reviewed text in row form with its book and page (the verdict `reviewed-537`
of the print rewrite), until the final step of the plan removes it.

Span source text (what `span_sha256` hashes)
--------------------------------------------
The span is the name block and the run after it, up to the next boundary or name. Each block is
one logical line: its source lines are stripped and joined by a single space, and a line that ends
in a backslash (a hard break) keeps its break. Blocks are joined by one blank line. The text is
UTF-8 with no trailing newline. The hash does not change when `corpus-fmt` re-wraps a paragraph.

Rules of the rewrite, in short
------------------------------
Candidates, the explicit Action map, allowed crossings, continuation paragraphs, the canonical
order, the upgrade lead `**At Nth level,** <printed sentence>` and the lowercase list follow the
decision. A power may have two effect rows when the first is `Passive` or `Ability` and the
second an action (`Standard`, `Move`, `Swift`, `Immediate`, `Free`, `Full-round`); each keeps its
own continuation. `Choice` and `Info` stand after `Flavor`, before the effect. The unlabeled
paragraphs after a `Special` row continue it. Only identical original `Usage` rows are
deduplicated. Anything else the rewrite would have to guess goes to the queue with its whole
span unchanged. The replacement is validated, and when it fails, the original span is queued. A
second pass changes nothing.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import tomllib
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

# ==== the mirror of the app: cast_iron_schema::power =========================================
# Labels, ranks, section labels, level grammar, classifier, candidates and `validate`. Keep this
# section in step with the app's `crates/schema/src/power.rs`.

EFFECT_LABELS = (
    "Passive", "Ability", "Standard", "Move", "Swift", "Immediate", "Free", "Full-round", "Benefit",
)
# The effect labels of a pair: the first row is passive text, the second an action.
PASSIVE_EFFECT_LABELS = ("Passive", "Ability")
ACTION_EFFECT_LABELS = ("Standard", "Move", "Swift", "Immediate", "Free", "Full-round")
ALIAS_LABELS = {"Fullround": "Full-round", "Passive Ability": "Passive", "Standard Action": "Standard"}
ACTION_LABEL = "Action"
# Block names that are section labels, never powers (matched on the name without a trailing colon,
# white space folded, ASCII case ignored).
NON_POWER_LABELS = (
    "Base Evolutions", "Bonus Spells", "Discipline Powers", "Domain Spells", "Patron Spells",
    "Replacement Domain Spells",
)
# `Choice` and `Info` (the "preface" rows) stand after `Flavor`, before the effect, each at most
# once, in their source order.
PREFACE_LABELS = ("Choice", "Info")
SINGLETONS = ("Gained", "Flavor", "Choice", "Info", "Usage", "Prereq", "Replaces")
# The position of a row in the canonical order. `Choice` and `Info` share position 4.
RANK = {"Gained": 2, "Flavor": 3, "Choice": 4, "Info": 4, "Usage": 7, "Prereq": 9, "Replaces": 10}
RANK_EFFECT, RANK_UPGRADE, RANK_OTHER = 5, 8, 11
# The explicit map of an `Action` value. There is no catch-all.
ACTION_EFFECT = {
    "Ability": "Ability", "ability": "Ability",
    "Passive Ability": "Passive",
    "Standard Action": "Standard", "Standard": "Standard", "Standard.": "Standard",
    "Move Action": "Move",
    "Swift Action": "Swift",
    "Immediate Action": "Immediate",
    "Free Action": "Free",
    "Full-Round Action": "Full-round", "Full-round.": "Full-round",
}
# Rows that an `Action` row's effect paragraphs may cross.
CROSSABLE = frozenset(("Gained", "Flavor", "Choice", "Info", "Usage", "Prereq", "Replaces"))
# The first word of an upgrade sentence that the rewrite may lowercase.
LOWERCASE_FIRST = frozenset((
    "You", "Your", "The", "This", "These", "That", "Those", "Its", "It", "A", "An", "Any", "All",
    "Each", "In", "Once", "When", "Whenever", "While", "If", "As", "For", "Add", "By", "She", "He",
    "Her", "His", "They", "Their", "Instead", "Additionally", "Also", "Every", "Allies",
))
ABILITY_TAG = re.compile(r"\s*\((?:Ex|Su|Sp)(?:(?:, | or | and )(?:Ex|Su|Sp))*\)$")

QUEUE_FILE = "scripts/class-option-power-queue.tsv"
RESOLUTIONS_FILE = "scripts/class-option-power-resolutions.toml"
EXCEPTIONS_FILE = "power-exceptions.toml"
QUEUE_HEADER = "entry_id\toriginal_name\toccurrence\tspan_sha256\treasons"

# Seeded print items: (entry id, original name, occurrence) -> reason. The decision seeds
# Foretell: the corpus says "1 time/day per wizard level", while print gives a number of rounds
# per day equal to the wizard level, not consecutive. A seeded power is queued unless it is
# valid or a resolution applies to it.
PRINT_ITEMS = {
    ("ref/arcaneschool/divination", "Foretell (Su)", 1):
        "seeded print item: Usage says 1 time/day per wizard level; print gives rounds per day",
}


# ---- level grammar ---------------------------------------------------------------------------

def ordinal_suffix(level: int) -> str:
    return {1: "st", 2: "nd", 3: "rd"}.get(level, "th")


def ordinal(level: int) -> str:
    return f"{level}{ordinal_suffix(level)}"


def well_formed(digits: str, suffix: str) -> int | None:
    """A number from 1 to 20 with no leading zero and its English suffix."""
    if not digits or digits.startswith("0") or not digits.isascii() or not digits.isdigit():
        return None
    level = int(digits)
    return level if 1 <= level <= 20 and suffix == ordinal_suffix(level) else None


LEVEL_HEAD = re.compile(r"At ([0-9]+)(st|nd|rd|th) (level|Level)(.*)", re.S)


@dataclass(frozen=True)
class LevelHead:
    level: int | None
    lowercase: bool
    rest: str


def level_head(text: str) -> LevelHead | None:
    """Detection is broad: `At ` digits suffix space `Level` or `level`. `text` must start so."""
    m = LEVEL_HEAD.fullmatch(text)
    if not m:
        return None
    return LevelHead(well_formed(m.group(1), m.group(2)), m.group(3) == "level", m.group(4))


# ---- blocks ----------------------------------------------------------------------------------

@dataclass(frozen=True)
class Block:
    kind: str                # boundary | lead | row | name | legacy | para
    lines: tuple[str, ...]   # source lines
    start: int               # first source line (index into the body lines)
    text: str                # logical line (see "Span source text")
    label: str = ""          # row label without its colon, or the name
    content: str = ""        # row content, lead sentence, legacy upgrade text
    level: int | None = None
    lowercase: bool = False
    sep: str = ""

    @property
    def end(self) -> int:
        return self.start + len(self.lines)

    @property
    def empty(self) -> bool:
        return self.kind == "row" and not self.content.strip()


def logical(lines) -> str:
    """The lines as one logical line: a hard break (a trailing odd backslash) stays a line break."""
    out = []
    for i, line in enumerate(lines):
        stripped = line.strip(" \t")
        out.append(stripped)
        if i < len(lines) - 1:
            trailing = len(stripped) - len(stripped.rstrip("\\"))
            out.append("\n" if trailing % 2 == 1 else " ")
    return "".join(out)


def split_lines(lines: list[str]) -> list[tuple[int, int]]:
    """The (start, end) line ranges of the body blocks, as `crates/corpus` reads them."""
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if line.strip(" \t") == "":
            i += 1
            continue
        if line.startswith(":::"):
            j = i + 1
            while j < n and lines[j].strip(" \t") != ":::":
                j += 1
            out.append((i, min(j + 1, n)))
            i = j + 1
            continue
        if re.match(r"^(- |\d+\. )", line):
            j = i + 1
            while j < n:
                if lines[j].strip(" \t") == "":
                    k = j
                    while k < n and lines[k].strip(" \t") == "":
                        k += 1
                    if k < n and lines[k].startswith("  "):
                        j = k
                        continue
                    break
                j += 1
            out.append((i, j))
            i = j
            continue
        if line.startswith((">", "|")):
            j = i
            while j < n and lines[j].startswith(line[0]):
                j += 1
            out.append((i, j))
            i = j
            continue
        j = i
        while j < n and lines[j].strip(" \t") != "":
            j += 1
        out.append((i, j))
        i = j
    return out


STRONG = re.compile(r"\*\*([^*]+)\*\*")


def classify(lines: tuple[str, ...], start: int) -> Block:
    first = lines[0]
    if first.startswith(("#", ":::", ">", "|")) or re.match(r"^(- |\d+\. )", first):
        return Block("boundary", lines, start, "\n".join(lines))
    text = logical(lines)
    strong = STRONG.match(text)
    if strong:
        inner, rest = strong.group(1), text[strong.end():]
        head = level_head(inner)
        if head and head.rest == ",":
            return Block("lead", lines, start, text, label=inner, content=rest.strip(),
                         level=head.level, lowercase=head.lowercase)
        if inner.endswith(":"):
            return Block("row", lines, start, text, label=inner[:-1], content=rest.strip())
        if not rest.strip():
            return Block("name", lines, start, text, label=inner)
    head = level_head(text) if text.startswith("At ") else None
    if head and head.rest[:1] in (":", ","):
        after = head.rest[1:]
        return Block("legacy", lines, start, text, content=after[1:] if after.startswith(" ") else after,
                     level=head.level, lowercase=head.lowercase, sep=head.rest[0])
    return Block("para", lines, start, text)


def parse_blocks(lines: list[str]) -> list[Block]:
    return [classify(tuple(lines[a:b]), a) for a, b in split_lines(lines)]


def row_is_old_upgrade(b: Block) -> LevelHead | None:
    head = level_head(b.label) if b.kind == "row" else None
    return head if head and head.rest == "" else None


def is_numbered_effect_label(label: str) -> bool:
    base = label.rstrip("0123456789")
    return len(base) < len(label) and (
        base in EFFECT_LABELS or base in ALIAS_LABELS or base == ACTION_LABEL)


def is_power_marker(b: Block) -> bool:
    if b.kind in ("lead", "legacy"):
        return True
    if b.kind != "row":
        return False
    return (b.label in ("Gained", ACTION_LABEL) or b.label in EFFECT_LABELS
            or b.label in ALIAS_LABELS or is_numbered_effect_label(b.label)
            or row_is_old_upgrade(b) is not None)


# ---- candidates ------------------------------------------------------------------------------

@dataclass(frozen=True)
class Candidate:
    start: int         # index of the name block
    end: int           # one past the last block
    name: str          # the original name as written (with any colon)
    occurrence: int


def legacy_name(blocks: list[Block], i: int) -> bool:
    """For the rewrite only: an empty row that is the first block of the body or whose label ends
    in an ability tag is a name written with a colon (the magus arcana)."""
    b = blocks[i]
    return b.empty and (i == 0 or ABILITY_TAG.search(b.label) is not None)


def written_name(b: Block) -> str:
    return b.label if b.kind == "name" else b.label + ":"


def is_non_power_label(name: str) -> bool:
    """A section label that is never a power: trimmed, no trailing colon, white space folded."""
    folded = " ".join(name.strip().rstrip(":").split())
    return any(label.lower() == folded.lower() and folded.isascii() for label in NON_POWER_LABELS)


def candidates(blocks: list[Block], legacy_names: bool = False) -> list[Candidate]:
    """A name directly followed by a row, a lead or a legacy upgrade, then the run to the next
    boundary or name; the run holds a power marker. `legacy_names` adds the rewrite's names. A
    section label (`NON_POWER_LABELS`) is never a candidate, but it still ends the run before it."""
    out: list[Candidate] = []
    count: Counter[str] = Counter()
    i = 0
    while i < len(blocks):
        named = blocks[i].kind == "name" or (legacy_names and legacy_name(blocks, i))
        if (named and not is_non_power_label(blocks[i].label)
                and i + 1 < len(blocks) and blocks[i + 1].kind in ("row", "lead", "legacy")):
            j = i + 1
            while j < len(blocks) and blocks[j].kind not in ("boundary", "name"):
                j += 1
            if any(is_power_marker(b) for b in blocks[i + 1:j]):
                name = written_name(blocks[i])
                count[name] += 1
                out.append(Candidate(i, j, name, count[name]))
                i = j
                continue
        i += 1
    return out


# ---- validation (mirrors cast_iron_schema::power::validate_power) ----------------------------


def gained_level(content: str) -> int | None:
    head = level_head(content.strip())
    return head.level if head and head.rest == "" and not head.lowercase else None


def effect_class(label: str) -> str:
    """`passive` (Passive, Ability), `action` (Standard ... Full-round) or `neither` (Benefit).
    An alias counts as the label it becomes."""
    label = ALIAS_LABELS.get(label, label)
    if label in PASSIVE_EFFECT_LABELS:
        return "passive"
    return "action" if label in ACTION_EFFECT_LABELS else "neither"


def validate(run: list[Block]) -> list[str]:
    """The problems of one candidate (the name block, then its run), as slugs. Empty is valid."""
    problems: list[str] = []

    def note(slug: str) -> None:
        if slug not in problems:
            problems.append(slug)

    if run[0].kind != "name":
        note("not-a-name")
    body = run[1:]
    if any(b.kind in ("name", "boundary") for b in body):
        note("block-in-span")
    # The first `Gained` row that parses (the app takes the first parseable one).
    gained = next((lv for b in body if b.kind == "row" and b.label == "Gained"
                   and (lv := gained_level(b.content)) is not None), None)
    last_rank, seen, effect_rows, last_up = 1, set(), 0, None
    # What the unlabeled paragraphs that follow continue: None (nothing: stray), "effect",
    # "action", "dropped" (an effect row that is already a problem) or "special".
    continues: str | None = None
    first_class = "neither"
    for b in body:
        if b.kind == "row":
            label = b.label
            continues = None
            if b.empty:
                note("empty-row")
            if label in EFFECT_LABELS or label in ALIAS_LABELS:
                effect_rows += 1
                if label in ALIAS_LABELS:
                    note("legacy-label")
                cls = effect_class(label)
                # A pair is a passive row and an action row; print decides which comes first, so
                # the validator accepts both orders (the rewrite queues the action-first one).
                second_is_action = (effect_rows == 2
                                    and {first_class, cls} == {"passive", "action"})
                if effect_rows == 2 and not second_is_action:
                    note("multiple-effect-rows")
                elif effect_rows > 2:
                    note("multiple-effect-rows")
                if effect_rows == 1 or second_is_action:
                    if last_rank > RANK_EFFECT:
                        note("out-of-order")
                    last_rank = max(last_rank, RANK_EFFECT)
                if effect_rows == 1:
                    first_class = cls
                    continues = "effect"
                elif second_is_action:
                    continues = "action"
                else:
                    continues = "dropped"
                continue
            if is_numbered_effect_label(label):
                note("numbered-effect-label")
                continue
            if label == ACTION_LABEL or row_is_old_upgrade(b):
                note("legacy-label")
                continue
            rank = RANK.get(label, RANK_OTHER)
            if rank != RANK_OTHER:
                if label in seen:
                    note("second-singleton-row")
                    continue
                seen.add(label)
            if rank < last_rank:
                note("out-of-order")
            last_rank = max(last_rank, rank)
            if label == "Gained" and gained_level(b.content) is None:
                note("non-canonical-gained")
            if label == "Special":
                continues = "special"
        elif b.kind == "lead":
            continues = None
            if not (b.level is not None and b.lowercase and b.content):
                note("non-canonical-lead")
                continue
            if gained is not None and b.level <= gained:
                note("upgrade-not-above-gained")
            if last_up is not None and b.level == last_up:
                note("upgrade-at-same-level")
            elif last_up is not None and b.level < last_up:
                note("upgrades-not-ascending")
            last_up = b.level
            if last_rank > RANK_UPGRADE:
                note("out-of-order")
            last_rank = max(last_rank, RANK_UPGRADE)
        elif b.kind == "legacy":
            continues = None
            note("legacy-upgrade")
        elif b.kind == "para":
            if continues is None:
                note("stray-paragraph")
    if effect_rows == 0:
        note("no-effect-row")
    return problems


def map_action(content: str):
    """What the value of an `**Action:** value` row becomes: ("effect", label), ("gained", level)
    or ("unmapped", None). The value must be plain text."""
    if re.search(r"[*_\[\]\\`]", content):
        return "unmapped", None
    value = content.strip()
    if value in ACTION_EFFECT:
        return "effect", ACTION_EFFECT[value]
    head = level_head(value)
    if head and head.rest == "" and not head.lowercase and head.level is not None:
        return "gained", head.level
    return "unmapped", None


# ==== end of the mirror of the app ==========================================================


# ---- the rewrite -----------------------------------------------------------------------------

def lower_first(text: str) -> tuple[str, str | None]:
    """Lowercase the first word of an upgrade sentence when it is on the lowercase list. Returns
    the text and the word that keeps a capital (so the power is queued), or None."""
    m = re.match(r"[A-Za-z]+", text)
    if m:
        word = m.group(0)
        if word in LOWERCASE_FIRST:
            return word.lower() + text[len(word):], None
        return text, word if word[0].isupper() else None
    visible = re.sub(r"^[\[\]*_\\`(]+", "", text)
    return text, (visible.split(" ")[0] if visible[:1].isupper() else None)


@dataclass
class Item:
    kind: str                       # row | action | up | para
    label: str = ""
    content: str = ""
    level: int = 0
    block: Block | None = None
    lines: tuple[str, ...] = ()     # the emitted block, one entry per source line
    canonical_lead: bool = False


def rewrite_run(run: list[Block]) -> tuple[list[tuple[str, ...]] | None, list[str]]:
    """The canonical blocks of a failing candidate, or None and the reasons it is queued. A
    reason is `code` or `code: detail`. The run's blocks are never altered."""
    q: list[str] = []
    name_block = run[0]
    if name_block.kind == "name":
        name_lines = name_block.lines
    else:
        name_lines = (f"**{name_block.label}**",)

    # 1. Deduplicate identical original Usage rows. This is the only deduplication.
    body, seen_usage = [], set()
    for b in run[1:]:
        if b.kind == "row" and b.label == "Usage":
            if b.text in seen_usage:
                continue
            seen_usage.add(b.text)
        body.append(b)

    # 2. Map each block. Items keep their source order.
    items: list[Item] = []
    for b in body:
        if b.kind == "row":
            label = b.label
            if b.empty:
                q.append(f"empty-row: {label}")
                continue
            old = row_is_old_upgrade(b)
            if old is not None:
                if old.level is None:
                    q.append(f"ill-formed-level: {label}")
                else:
                    items.append(Item("up", content=b.content, level=old.level, block=b))
            elif label == ACTION_LABEL:
                kind, value = map_action(b.content)
                if kind == "gained":
                    text = f"**Gained:** At {ordinal(value)} Level"
                    items.append(Item("row", "Gained", f"At {ordinal(value)} Level", block=b, lines=(text,)))
                elif kind == "effect":
                    items.append(Item("action", value, block=b))
                else:
                    q.append(f"unmapped-action: {b.content.strip()}")
            elif is_numbered_effect_label(label):
                q.append(f"numbered-effect-label: {label}")
            elif label in ALIAS_LABELS:
                new = ALIAS_LABELS[label]
                items.append(Item("row", new, b.content, block=b, lines=(f"**{new}:** {b.content}",)))
            else:
                items.append(Item("row", label, b.content, block=b, lines=b.lines))
        elif b.kind == "lead":
            if b.level is None or not b.lowercase or not b.content:
                q.append("non-canonical-lead")
            else:
                items.append(Item("up", content=b.content, level=b.level, block=b, lines=b.lines,
                                  canonical_lead=True))
        elif b.kind == "legacy":
            if b.sep != ":":
                q.append("comma-upgrade")
            elif b.level is None:
                q.append("ill-formed-level")
            elif not b.content.strip():
                q.append("empty-upgrade")
            else:
                items.append(Item("up", content=b.content, level=b.level, block=b))
        else:
            items.append(Item("para", block=b, lines=b.lines))

    for singleton in SINGLETONS:
        if sum(1 for it in items if it.kind == "row" and it.label == singleton) > 1:
            q.append(f"conflicting-rows: {singleton}")
    effects = [k for k, it in enumerate(items)
               if (it.kind == "row" and it.label in EFFECT_LABELS) or it.kind == "action"]
    ups = [it for it in items if it.kind == "up"]
    has_gained = any(it.kind == "row" and it.label == "Gained" for it in items)
    if not effects:
        q.append("no-effect-row" + (": suggest the lowest upgrade as Gained level and base effect"
                                    if ups and not has_gained else ""))
    elif len(effects) == 2:
        # A passive row, then an action row, is the one valid pair. A legacy `Action` row in a pair
        # queues: its paragraph group cannot be assigned without a guess. An action first queues
        # for print; the script never reorders it.
        classes = [effect_class(items[k].label) for k in effects]
        if any(items[k].kind == "action" for k in effects):
            q.append("multiple-effect-rows: a legacy Action row in a pair of effect rows")
        elif classes == ["action", "passive"]:
            q.append("action-first-pair: print decides the order")
        elif classes != ["passive", "action"]:
            q.append("multiple-effect-rows")
    elif len(effects) > 2:
        q.append("multiple-effect-rows")

    # 3. Paragraph groups: consecutive unlabeled paragraphs. A group continues the row right
    # before it: an effect row, or a `Special` row. A group anywhere else queues. A legacy `Action`
    # row has no continuation of its own: its effect text is the one group that does not follow a
    # `Special` row.
    groups: list[list[int]] = []
    current: list[int] = []
    for k, it in enumerate(items):
        if it.kind == "para":
            current.append(k)
        elif current:
            groups.append(current)
            current = []
    if current:
        groups.append(current)
    legacy_action = len(effects) == 1 and items[effects[0]].kind == "action"
    continuation: dict[int, list[tuple[str, ...]]] = {}   # effect or `Special` item -> paragraphs
    loose: list[list[int]] = []                             # groups that follow no row they continue
    for group in groups:
        before = items[group[0] - 1] if group[0] > 0 else None
        if before is not None and before.kind == "row" and before.label == "Special":
            continuation[group[0] - 1] = [items[k].lines for k in group]
        elif (before is not None and group[0] - 1 in effects and before.kind == "row"
              and not legacy_action):
            continuation[group[0] - 1] = [items[k].lines for k in group]
        else:
            loose.append(group)
    effect_text: dict[int, tuple[str, ...]] = {}
    if legacy_action:
        e = effects[0]
        if len(loose) != 1 or loose[0][0] < e:
            q.append("action-without-one-group")
        elif any(not (items[k].kind == "row" and items[k].label in CROSSABLE)
                 for k in range(e + 1, loose[0][0])):
            q.append("action-group-crosses-row")
        else:
            group = loose[0]
            effect_text[e] = (f"**{items[e].label}:** {items[group[0]].block.text}",)
            continuation[e] = [items[k].lines for k in group[1:]]
    elif len(effects) in (1, 2) and loose and not any(
            x.startswith(("multiple-effect-rows", "action-first-pair")) for x in q):
        q.append("unlabeled-paragraphs-not-after-effect")

    # 4. Upgrades, ascending, with the printed sentence after the lead.
    gained = next((lv for it in items if it.kind == "row" and it.label == "Gained"
                   and (lv := gained_level(it.content)) is not None), None)
    levels = [it.level for it in ups]
    if len(set(levels)) != len(levels):
        q.append("two-upgrades-at-one-level")
    up_lines: list[tuple[str, ...]] = []
    for it in sorted(ups, key=lambda it: it.level):
        if gained is not None and it.level <= gained:
            q.append(f"upgrade-not-above-gained: {it.level}")
        if it.canonical_lead:
            up_lines.append(it.lines)
            continue
        text, capital = lower_first(it.content)
        if capital is not None:
            q.append(f"upgrade-keeps-capital: {capital}")
        up_lines.append((f"**At {ordinal(it.level)} level,** {text}",))
    if q:
        return None, q

    # 5. Emit (the canonical order of the mirror): name, Gained, Flavor, Choice and Info (source order), the effect
    # rows each with its continuation, Usage, upgrades, Prereq, Replaces, then the other rows in
    # source order, a `Special` row with its paragraphs.
    rows = [(k, it) for k, it in enumerate(items) if it.kind == "row"]
    pick = lambda label: [it.lines for _, it in rows if it.label == label]
    effect_blocks: list[tuple[str, ...]] = []
    for k in effects:
        effect_blocks.append(effect_text.get(k) or items[k].lines)
        effect_blocks.extend(continuation.get(k, []))
    tail: list[tuple[str, ...]] = []
    for k, it in rows:
        if it.label not in SINGLETONS and it.label not in EFFECT_LABELS:
            tail.append(it.lines)
            tail.extend(continuation.get(k, []))
    preface = [it.lines for _, it in rows if it.label in PREFACE_LABELS]   # source order
    out = ([name_lines] + pick("Gained") + pick("Flavor") + preface
           + effect_blocks + pick("Usage") + up_lines + pick("Prereq") + pick("Replaces") + tail)
    problems = validate(parse_blocks(join_blocks(out)))
    if problems:
        return None, ["replacement-fails-validation: " + ", ".join(problems)]
    return out, []


def join_blocks(blocks) -> list[str]:
    """Source lines of blocks, separated by one blank line."""
    lines: list[str] = []
    for k, b in enumerate(blocks):
        if k:
            lines.append("")
        lines.extend(b)
    return lines


def span_text(run: list[Block]) -> str:
    return "\n\n".join(b.text for b in run)


def span_sha(run: list[Block]) -> str:
    return hashlib.sha256(span_text(run).encode()).hexdigest()


# ---- resolutions -----------------------------------------------------------------------------

@dataclass(frozen=True)
class Resolution:
    id: str
    name: str
    occurrence: int
    span_sha256: str
    print: str
    replacement: str


def load_resolutions(path: Path) -> dict[tuple[str, str, int], Resolution]:
    if not path.exists():
        return {}
    data = tomllib.loads(path.read_text())
    out: dict[tuple[str, str, int], Resolution] = {}
    for r in data.get("resolution", []):
        res = Resolution(r["id"], r["name"], r["occurrence"], r["span_sha256"], r["print"], r["replacement"])
        key = (res.id, res.name, res.occurrence)
        if key in out:
            raise SystemExit(f"{path}: two resolutions for {key}")
        out[key] = res
    return out


@dataclass(frozen=True)
class PowerException:
    id: str
    name: str
    occurrence: int
    span_sha256: str
    reason: str
    print: str


EXCEPTION_KEYS = {"id", "name", "occurrence", "span_sha256", "reason", "print"}
HEX64 = re.compile(r"[0-9a-f]{64}")


def load_exceptions(path: Path) -> dict[tuple[str, str, int], PowerException]:
    """`power-exceptions.toml`. A missing file holds no exception. The file is read as strictly
    as the app's check reads it: no unknown key, a required `span_sha256` of 64 lowercase hex
    digits, an integer `occurrence` from 1, and a text for `reason` and `print`."""
    if not path.exists():
        return {}
    data = tomllib.loads(path.read_text())
    if set(data) - {"exception"}:
        raise SystemExit(f"{path}: unknown top-level key {sorted(set(data) - {'exception'})}")
    out: dict[tuple[str, str, int], PowerException] = {}
    for r in data.get("exception", []):
        where = f"{path}: the exception {r.get('name')!r} of {r.get('id')!r}"
        if set(r) != EXCEPTION_KEYS:
            raise SystemExit(f"{where} needs exactly the keys {sorted(EXCEPTION_KEYS)}")
        if not all(isinstance(r[k], str) for k in ("id", "name", "span_sha256", "reason", "print")):
            raise SystemExit(f"{where}: id, name, span_sha256, reason and print are strings")
        if not isinstance(r["occurrence"], int) or isinstance(r["occurrence"], bool) or r["occurrence"] < 1:
            raise SystemExit(f"{where}: occurrence is an integer from 1")
        if not HEX64.fullmatch(r["span_sha256"]):
            raise SystemExit(f"{where}: span_sha256 is 64 lowercase hex digits")
        exc = PowerException(r["id"], r["name"], r["occurrence"], r["span_sha256"], r["reason"], r["print"])
        key = (exc.id, exc.name, exc.occurrence)
        if key in out:
            raise SystemExit(f"{path}: two exceptions for {key}")
        if not exc.reason.strip() or not exc.print.strip():
            raise SystemExit(f"{where} needs a reason and a print reference")
        out[key] = exc
    return out


def resolution_blocks(res: Resolution) -> list[Block]:
    return parse_blocks(res.replacement.strip("\n").split("\n"))


def resolution_power_text(res: Resolution) -> str:
    """The span text of the power that the replacement starts with (what the corpus holds once the
    resolution is applied: the blocks after the power are not part of its span)."""
    blocks = resolution_blocks(res)
    cands = candidates(blocks)
    return span_text(blocks[cands[0].start:cands[0].end]) if cands else span_text(blocks)


def check_resolution(res: Resolution) -> list[str]:
    """A replacement starts with a candidate, and every candidate in it passes validation. Blocks
    after the last candidate's boundary are free: a power that print sets as a bulleted list keeps
    the list after the power (Utility Shot)."""
    blocks = resolution_blocks(res)
    cands = candidates(blocks)
    if not cands or cands[0].start != 0:
        return ["the replacement does not start with a power"]
    out = []
    for c in cands:
        problems = validate(blocks[c.start:c.end])
        if problems:
            out.append(f"{blocks[c.start].label}: {', '.join(problems)}")
    return out


# ---- one entry -------------------------------------------------------------------------------

@dataclass
class Outcome:
    entry_id: str
    name: str
    occurrence: int
    status: str            # valid | rewritten | queued | resolved | resolution-noop | stale
                           # | excepted | stale-exception | obsolete-exception
    reasons: list[str]
    sha: str


def action_first_pair(run: list[Block]) -> bool:
    """Two effect rows, an action row before a passive one. The validator accepts it, but print
    decides the order, so the power waits in the queue for a print lookup."""
    labels = [ALIAS_LABELS.get(b.label, b.label) for b in run[1:]
              if b.kind == "row" and (b.label in EFFECT_LABELS or b.label in ALIAS_LABELS)]
    return len(labels) == 2 and [effect_class(x) for x in labels] == ["action", "passive"]


def process_body(entry_id: str, lines: list[str], resolutions,
                 rewrite: bool = True, exceptions=None) -> tuple[list[str], list[Outcome]]:
    """The new body lines and one outcome per candidate. With `rewrite` off, only resolutions
    change the text; the outcomes still say what the rewrite would do."""
    blocks = parse_blocks(lines)
    outcomes: list[Outcome] = []
    out: list[str] = []
    cursor = 0   # the next source line not yet copied
    for c in candidates(blocks, legacy_names=True):
        run = blocks[c.start:c.end]
        sha = span_sha(run)
        key = (entry_id, c.name, c.occurrence)
        replacement: list[tuple[str, ...]] | None = None
        status, reasons = "valid", []
        res = resolutions.get(key)
        exc = (exceptions or {}).get(key)
        if exc and res:
            status, reasons = "queued", ["both-exception-and-resolution"]
        elif exc and exc.span_sha256 != sha:
            status, reasons = "queued", ["stale-exception"]
            outcomes.append(Outcome(entry_id, c.name, c.occurrence, "stale-exception", ["stale-exception"], sha))
        elif exc:
            # Excepted: the power stays as it is. An exception for a power that passes is obsolete.
            if not validate(run):
                status = "obsolete-exception"
            else:
                status = "excepted"
        elif res and res.span_sha256 == sha:
            replacement = [tuple(b.lines) for b in resolution_blocks(res)]
            status = "resolved"
        elif res and span_text(run) == resolution_power_text(res):
            status = "resolution-noop"
        else:
            if res:
                # A stale resolution: the span is not the one the resolution was made for. Report
                # it, and queue the power again; the automatic rewrite does not touch it.
                outcomes.append(Outcome(entry_id, c.name, c.occurrence, "stale", ["stale-resolution"], sha))
            if not validate(run):
                if action_first_pair(run):
                    status, reasons = "queued", ["action-first-pair: print decides the order"]
                else:
                    status = "valid"
            elif res:
                status, reasons = "queued", ["stale-resolution"]
            elif key in PRINT_ITEMS:
                status, reasons = "queued", ["print-review: " + PRINT_ITEMS[key]]
            else:
                new, reasons = rewrite_run(run)
                if reasons:
                    status = "queued"
                else:
                    status, replacement = "rewritten", new
        outcomes.append(Outcome(entry_id, c.name, c.occurrence, status, reasons, sha))
        if replacement is not None and (rewrite or status == "resolved"):
            out.extend(lines[cursor:run[0].start])
            out.extend(join_blocks(replacement))
            cursor = run[-1].end
    out.extend(lines[cursor:])
    return out, outcomes


# ---- the corpus ------------------------------------------------------------------------------

def class_option_entries(corpus: Path):
    """(entry id, path, text) of every class-option entry, in id order."""
    found = []
    for path in sorted((corpus / "entries").rglob("*.md")):
        text = path.read_text()
        if 'kind = "class_option"' not in text:
            continue
        parts = text.split("+++\n", 2)
        if len(parts) != 3:
            continue
        front = tomllib.loads(parts[1])
        if front.get("kind") == "class_option":
            found.append((front["id"], path, parts))
    found.sort(key=lambda e: e[0])
    return found


def run_corpus(corpus: Path, resolutions, families=None, write=False, rewrite=True, exceptions=None):
    outcomes: list[Outcome] = []
    changed: list[Path] = []
    for entry_id, path, parts in class_option_entries(corpus):
        body = parts[2].split("\n")
        new, found = process_body(entry_id, body, resolutions, rewrite, exceptions)
        outcomes.extend(found)
        family = entry_id.split("/")[1]
        if new != body and (families is None or family in families):
            changed.append(path)
            if write:
                path.write_text(parts[0] + "+++\n" + parts[1] + "+++\n" + "\n".join(new))
    return outcomes, changed


def unused_resolutions(resolutions, outcomes: list[Outcome]):
    """(orphaned, obsolete): the resolutions whose key matches no candidate. A resolution that is
    already applied counts as used even when it renamed its power (a legacy name loses its colon):
    the entry then holds a candidate with the span of the replacement. A resolution for a
    section label (`NON_POWER_LABELS`), which is no candidate any more, is obsolete."""
    used = {(o.entry_id, o.name, o.occurrence) for o in outcomes}
    present = {(o.entry_id, o.sha) for o in outcomes}
    orphaned, obsolete = [], []
    for key in sorted(set(resolutions) - used):
        res = resolutions[key]
        applied = (key[0], hashlib.sha256(resolution_power_text(res).encode()).hexdigest()) in present
        if applied:
            continue
        (obsolete if is_non_power_label(key[1]) else orphaned).append(key)
    return orphaned, obsolete


def unused_exceptions(exceptions, outcomes: list[Outcome]):
    """The exceptions whose key matches no candidate."""
    used = {(o.entry_id, o.name, o.occurrence) for o in outcomes}
    return sorted(set(exceptions) - used)


def entry_in_scope(body_lines: list[str]) -> bool:
    """An entry is in the scope of this script while its body holds an import row (a power marker): a
    `Gained`, effect or `Action` row, an upgrade lead or a plain-text upgrade. A converted entry holds none."""
    # printed prose says "At 5th level, a druid gains ...": a plain upgrade in the comma form is no import row, the colon form is
    return any(is_power_marker(b) and not (b.kind == "legacy" and b.sep == ",") for b in parse_blocks(body_lines))


def retired_entries(corpus: Path) -> set[str]:
    """The class-option entries with no import row: converted by the print rewrite, or never import-shaped."""
    return {entry_id for entry_id, _path, parts in class_option_entries(corpus) if not entry_in_scope(parts[2].split("\n"))}


def bold_only_names(corpus: Path, retired: set[str]) -> dict[str, set[str]]:
    """For each retired entry, the names that still stand as a bold-only block (`**Name**`): an entry that has no import row but still has
    such a name is not converted (the print rewrite makes heads), so a key of that name is orphaned, not retired (#362 follow-up)."""
    out: dict[str, set[str]] = {}
    for entry_id, _path, parts in class_option_entries(corpus):
        if entry_id in retired:
            out[entry_id] = {re.sub(r"[^a-z0-9]", "", re.sub(r"\s*\((?:Ex|Su|Sp)[^)]*\)\s*:?$", "", written_name(b)).lower()) for b in parse_blocks(parts[2].split("\n")) if b.kind == "name"}
    return out


def split_retired(keys, retired: set[str]):
    """(live, retired) keys: a resolution or exception whose entry is out of scope is retired, not orphaned."""
    live = [k for k in keys if k[0] not in retired]
    return live, [k for k in keys if k[0] in retired]


def queue_text(outcomes: list[Outcome]) -> str:
    rows = [QUEUE_HEADER]
    for o in outcomes:
        if o.status == "queued":
            reasons = re.sub(r"\s+", " ", "; ".join(o.reasons))
            rows.append("\t".join((o.entry_id, o.name, str(o.occurrence), o.sha, reasons)))
    return "\n".join(rows) + "\n"


def summarize(outcomes: list[Outcome], changed: list[Path]) -> str:
    status = Counter(o.status for o in outcomes)
    reasons: Counter[str] = Counter()
    for o in outcomes:
        if o.status == "queued":
            for code in {r.split(":")[0] for r in o.reasons}:
                reasons[code] += 1
    lines = [f"candidates (rewrite discovery): "
             f"{sum(v for k, v in status.items() if k not in ('stale', 'stale-exception'))}"]
    for key in ("valid", "rewritten", "queued", "resolved", "resolution-noop", "excepted", "stale"):
        lines.append(f"  {key}: {status.get(key, 0)}")
    lines.append(f"entries changed: {len(changed)}")
    lines.append("queued by reason (a power can have several):")
    lines.extend(f"  {code}: {n}" for code, n in sorted(reasons.items(), key=lambda kv: (-kv[1], kv[0])))
    return "\n".join(lines)


# ---- self-test: the fixtures of the decision ---------------------------------------------------
# Each body has the structure of the named corpus entry (same rows, same order, same defect) with
# short placeholder wording, so the test does not depend on the corpus, which the rewrite changes.
# The occurrence is the position among the candidates with the same name in the entry.

HAUNT = (
    "**Haunt Channeler (Su)**\n\n**Gained:** At 1st Level\n\n**Ability:** You channel a haunt.\n\n"
    "**Haunt Channeler (Su)**\n\n**Ability:** You channel.\n\n**Ability2:** You channel more.\n\n"
    "**Standard:** You channel a third way.\n")

# (entry id, original name, occurrence, expected, reason code, body). `valid` is the decision's
# `canonical`: the span already passes validation and stays unchanged.
FIXTURES = [
    ("ref/discovery/elixir-of-life", "Elixir of Life", 1, "valid", None,
     "**Elixir of Life**\n\n**Ability:** First paragraph.\n\nOne continuation paragraph.\n\n"
     "**Prereq:** Level 11\n"),
    ("ref/arcaneschool/abjuration", "Resistance (Ex)", 1, "rewritten", None,
     "**Resistance (Ex)**\n\n**At 11th Level:** This resistance increases to 10.\n\n"
     "**At 20th Level:** This resistance changes to immunity.\n\n**Gained:** At 1st Level\n\n"
     "**Passive:** You gain resistance 5.\n"),
    # Counterspell Mastery was queued (two effect rows). Since the owner's answer of 2026-11-21 an
    # `Ability` row, then an action row, is the valid pair: only the place of `Gained` changes.
    ("ref/arcaneschool/abjuration", "Counterspell Mastery", 1, "rewritten", None,
     "**Counterspell Mastery**\n\n**Ability:** You can counter.\n\n**Gained:** At 8th Level\n\n"
     "**Immediate:** You counter a spell.\n"),
    ("ref/aspect/giant-wasp", "Minor Form", 1, "rewritten", None,
     "**Minor Form**\n\n**Passive:** You gain a sting.\n\nAt 8th level: The sting grows.\n\n"
     "At 12th level: The sting grows again.\n"),
    ("ref/deed/utility-shot", "Utility Shot (Ex)", 1, "queued", "empty-row",
     "**Utility Shot (Ex)**\n\n**Ability:** You choose one shot.\n\n**Blast Lock:**\n\n"
     "**Scoot Unattended Object:**\n\n**Stop Bleeding:**\n"),
    ("ref/blrgbloodline/fey", "One with Nature (Su)", 1, "queued", "unmapped-action",
     "**One with Nature (Su)**\n\n**Action:** Move-Equivalent Action\n\nYou become one with nature.\n"),
    ("ref/hex/coven", "Coven (Ex)", 1, "queued", "numbered-effect-label",
     "**Coven (Ex)**\n\n**Ability:** One effect.\n\n**Ability2:** Another effect.\n"),
    ("ref/mystery/flame", "Firestorm (Su)", 1, "rewritten", None,
     "**Firestorm (Su)**\n\n**Gained:** At 15th Level\n\n**Usage:** 1/day\n\n"
     "**Prereq:** 15th-level oracle\n\n**Standard:** You call fire.\n\n**Usage:** 1/day\n"),
    ("ref/mystery/reaper", "Haunt Channeler (Su)", 1, "valid", None, HAUNT),
    ("ref/mystery/reaper", "Haunt Channeler (Su)", 2, "queued", "numbered-effect-label", HAUNT),
    ("ref/arcaneschool/divination", "Foretell (Su)", 1, "queued", "print-review",
     "**Foretell (Su)**\n\n**Action:** Standard Action\n\n**Gained:** At 8th Level\n\n"
     "**Usage:** 1 time/day per wizard level\n\nYou foretell.\n"),
    ("ref/arcaneschool/divination", "Forewarned (Su)", 1, "queued", "upgrade-keeps-capital",
     "**Forewarned (Su)**\n\n**At 20th Level:** Anytime you roll initiative, you act.\n\n"
     "**Gained:** At 1st Level\n\n**Passive:** You are forewarned.\n"),
    ("ref/ragepower/auspicious-mark", "Auspicious Mark (Su)", 1, "rewritten", None,
     "**Auspicious Mark (Su)**\n\n**Flavor:** The mark glows.\n\n**Usage:** Once per rage\n\n"
     "**Swift:** You mark a foe.\n\n**Special:** Stacks.\n\n**Usage:** Once per rage\n"),
    ("ref/hex/evil-eye", "Evil Eye (Su)", 1, "rewritten", None,
     "**Evil Eye (Su)**\n\n**Ability:** You curse a foe.\n\n**Flavor:** Your gaze is cold.\n\n"
     "At 8th level: The penalty grows.\n"),
    ("ref/hex/flight", "Flight (Su)", 1, "queued", "no-effect-row",
     "**Flight (Su)**\n\n**At 1st Level:** You fly.\n\n**At 5th Level:** You fly faster.\n"),
    ("ref/domain/fire", "Fire Resistance (Ex)", 1, "queued", "no-effect-row",
     "**Fire Resistance (Ex)**\n\n**At 6th Level:** You gain fire resistance 10.\n"),
    # Since the owner's answer 2 of 2026-11-21 the paragraph after `Special` continues the note, so
    # the `Action` row has no group of its own (it was "the group crosses Special").
    ("ref/hex/blight", "Blight (Su)", 1, "queued", "action-without-one-group",
     "**Blight (Su)**\n\n**Action:** Standard Action\n\n**Special:** A limit.\n\nYou blight a plant.\n"),
    ("ref/arcana/accurate-strike", "Accurate Strike (Ex):", 1, "rewritten", None,
     "**Accurate Strike (Ex):**\n\n**Ability:** You strike accurately.\n"),
    ("ref/talent/black-market-connections", "Black Market Connection (Ex)", 1, "rewritten", None,
     "**Black Market Connection (Ex)**\n\n**Action:** Ability\n\nYou know a dealer.\n"),
    ("S1", "Twin Strike (Ex)", 1, "queued", "multiple-effect-rows",
     "**Twin Strike (Ex)**\n\n**Fullround:** You strike twice.\n\n**Full-round:** You strike twice.\n"),
    ("S2", "Quiet Step (Ex)", 1, "queued", "empty-row",
     "**Quiet Step (Ex)**\n\n**Ability:** You move silently.\n\n**Usage:**\n"),
    ("S3", "Resistance (Ex)", 1, "valid", None,
     "**Resistance (Ex)**\n\n**Gained:** At 1st Level\n\n**Passive:** You gain resistance 5.\n\n"
     "**At 11th level,** this resistance increases to 10.\n"),
    # The owner's answers of 2026-11-21 (the fixtures of crates/schema/tests/power_fixtures.rs).
    # Decision 1: Noble Visage, a passive row then an action row; `Replaces` moves after `Usage`.
    ("ref/domain/nobility", "Noble Visage (Su)", 1, "rewritten", None,
     "**Noble Visage (Su)**\n\n**Passive:** You gain a bonus.\n\n**Replaces:** The inspiring word ability\n\n"
     "**Standard:** You touch an ally.\n\n**Usage:** 3 + Wisdom modifier times/day\n"),
    # Decision 1: each row of a pair keeps its own continuation, in source order.
    ("P1", "Pair (Su)", 1, "rewritten", None,
     "**Pair (Su)**\n\n**Passive:** The passive.\n\nPassive continuation.\n\n**Standard:** The action.\n\n"
     "Action continuation.\n\n**Flavor:** The intro.\n"),
    # Decision 1, queued: two passive rows, two actions, an action first, three rows, `Benefit`.
    ("P2", "Two Passives (Su)", 1, "queued", "multiple-effect-rows",
     "**Two Passives (Su)**\n\n**Ability:** One.\n\n**Passive:** Two.\n"),
    ("P3", "Two Actions (Su)", 1, "queued", "multiple-effect-rows",
     "**Two Actions (Su)**\n\n**Standard:** One.\n\n**Swift:** Two.\n"),
    ("P4", "Action First (Su)", 1, "queued", "action-first-pair",
     "**Action First (Su)**\n\n**Immediate:** One.\n\n**Passive:** Two.\n"),
    ("P5", "Three Rows (Su)", 1, "queued", "multiple-effect-rows",
     "**Three Rows (Su)**\n\n**Passive:** One.\n\n**Standard:** Two.\n\n**Swift:** Three.\n"),
    ("P6", "Benefit Beside (Su)", 1, "queued", "multiple-effect-rows",
     "**Benefit Beside (Su)**\n\n**Passive:** One.\n\n**Benefit:** Two.\n"),
    # A pair with a legacy `Action` row queues: its paragraph group cannot be assigned.
    ("P7", "Legacy Pair (Su)", 1, "queued", "multiple-effect-rows",
     "**Legacy Pair (Su)**\n\n**Passive:** One.\n\n**Action:** Standard Action\n\nTwo.\n"),
    # A paragraph that follows neither an effect row nor `Special` queues.
    ("P8", "Loose Paragraph (Su)", 1, "queued", "unlabeled-paragraphs-not-after-effect",
     "**Loose Paragraph (Su)**\n\n**Passive:** One.\n\n**Usage:** Once.\n\nLoose.\n"),
    # Decision 2: Natural Spell Combat, paragraphs after `Special` continue it (already valid).
    ("ref/arcana/natural-spell-combat", "Natural Spell Combat (Ex)", 1, "valid", None,
     "**Natural Spell Combat (Ex)**\n\n**Ability:** The effect.\n\n**Special:** The note.\n\n"
     "First more.\n\nSecond more.\n"),
    # Decision 2: the same, after the rewrite moved `Special`'s neighbours: the paragraphs go with it.
    ("P9", "Special First (Ex)", 1, "rewritten", None,
     "**Special First (Ex)**\n\n**Special:** The note.\n\nNote continues.\n\n**Passive:** The effect.\n"),
    # Decision 4: Basic Magic, `Choice` after the effect moves before it.
    ("ref/evolution/basic-magic", "Basic Magic (Sp)", 1, "rewritten", None,
     "**Basic Magic (Sp)**\n\n**Flavor:** An eidolon learns a spell.\n\n**Ability:** Cast it daily.\n\n"
     "**Choice:** Select one spell.\n\n**At 4th level,** three times per day.\n\n**Special:** Repeatable.\n"),
    # Decision 4: a second `Choice` row conflicts; `Choice` and `Info` keep their source order.
    ("P10", "Two Choices (Ex)", 1, "queued", "conflicting-rows",
     "**Two Choices (Ex)**\n\n**Ability:** x.\n\n**Choice:** a.\n\n**Choice:** b.\n"),
    # Decision 5: the witch patron's `Patron Spells` is a row of the power (an "other row"), not a
    # name; `Info` goes before the effect, the spell rows keep their place.
    ("ref/patron/empath", "Empath", 1, "rewritten", None,
     "**Empath**\n\n**Ability:** You gain a hex.\n\n**Info:** The patron is a manifestation.\n\n"
     "**Spells:** Burst of insight (2nd)\n\n**Patron Spells:** This unique patron grants these spells.\n"),
    # Decision 5, answer B: Class Skill and Bonus Feat of the Glory subdomain stay powers.
    ("ref/domain/glory", "Class Skill", 1, "valid", None,
     "**Class Skill**\n\n**Passive:** Add a skill to your class skills.\n"),
    ("P11", "Info Last (Ex)", 1, "rewritten", None,
     "**Info Last (Ex)**\n\n**Passive:** x.\n\n**Info:** i.\n\n**Choice:** c.\n"),
]

# The exact text of the rewritten fixtures: (entry id, name, expected lines).
EXACT = {
    ("ref/arcaneschool/abjuration", "Counterspell Mastery"): (
        "**Counterspell Mastery**\n\n**Gained:** At 8th Level\n\n**Ability:** You can counter.\n\n"
        "**Immediate:** You counter a spell.\n"),
    ("ref/domain/nobility", "Noble Visage (Su)"): (
        "**Noble Visage (Su)**\n\n**Passive:** You gain a bonus.\n\n**Standard:** You touch an ally.\n\n"
        "**Usage:** 3 + Wisdom modifier times/day\n\n**Replaces:** The inspiring word ability\n"),
    ("P1", "Pair (Su)"): (
        "**Pair (Su)**\n\n**Flavor:** The intro.\n\n**Passive:** The passive.\n\nPassive continuation.\n\n"
        "**Standard:** The action.\n\nAction continuation.\n"),
    ("P9", "Special First (Ex)"): (
        "**Special First (Ex)**\n\n**Passive:** The effect.\n\n**Special:** The note.\n\nNote continues.\n"),
    ("ref/evolution/basic-magic", "Basic Magic (Sp)"): (
        "**Basic Magic (Sp)**\n\n**Flavor:** An eidolon learns a spell.\n\n**Choice:** Select one spell.\n\n"
        "**Ability:** Cast it daily.\n\n**At 4th level,** three times per day.\n\n**Special:** Repeatable.\n"),
    ("ref/patron/empath", "Empath"): (
        "**Empath**\n\n**Info:** The patron is a manifestation.\n\n**Ability:** You gain a hex.\n\n"
        "**Spells:** Burst of insight (2nd)\n\n**Patron Spells:** This unique patron grants these spells.\n"),
    ("P11", "Info Last (Ex)"): (
        "**Info Last (Ex)**\n\n**Info:** i.\n\n**Choice:** c.\n\n**Passive:** x.\n"),
    ("ref/arcaneschool/abjuration", "Resistance (Ex)"): (
        "**Resistance (Ex)**\n\n**Gained:** At 1st Level\n\n**Passive:** You gain resistance 5.\n\n"
        "**At 11th level,** this resistance increases to 10.\n\n"
        "**At 20th level,** this resistance changes to immunity.\n"),
    ("ref/aspect/giant-wasp", "Minor Form"): (
        "**Minor Form**\n\n**Passive:** You gain a sting.\n\n**At 8th level,** the sting grows.\n\n"
        "**At 12th level,** the sting grows again.\n"),
    ("ref/mystery/flame", "Firestorm (Su)"): (
        "**Firestorm (Su)**\n\n**Gained:** At 15th Level\n\n**Standard:** You call fire.\n\n"
        "**Usage:** 1/day\n\n**Prereq:** 15th-level oracle\n"),
    ("ref/ragepower/auspicious-mark", "Auspicious Mark (Su)"): (
        "**Auspicious Mark (Su)**\n\n**Flavor:** The mark glows.\n\n**Swift:** You mark a foe.\n\n"
        "**Usage:** Once per rage\n\n**Special:** Stacks.\n"),
    ("ref/hex/evil-eye", "Evil Eye (Su)"): (
        "**Evil Eye (Su)**\n\n**Flavor:** Your gaze is cold.\n\n**Ability:** You curse a foe.\n\n"
        "**At 8th level,** the penalty grows.\n"),
    ("ref/arcana/accurate-strike", "Accurate Strike (Ex):"): (
        "**Accurate Strike (Ex)**\n\n**Ability:** You strike accurately.\n"),
    ("ref/talent/black-market-connections", "Black Market Connection (Ex)"): (
        "**Black Market Connection (Ex)**\n\n**Ability:** You know a dealer.\n"),
}


def run_fixture(entry_id, name, occurrence, body):
    """(outcome, new body, index of the candidate), for one fixture."""
    lines = body.split("\n")
    new, outcomes = process_body(entry_id, lines, {})
    found = [o for o in outcomes if o.status != "stale"]
    for index, o in enumerate(found):
        if o.name == name and o.occurrence == occurrence:
            return o, new, index
    raise AssertionError(f"{name} #{occurrence} is not a candidate")


def self_test() -> int:
    failures: list[str] = []

    def expect(ok: bool, message: str) -> None:
        if not ok:
            failures.append(message)

    for entry_id, name, occ, expected, code, body in FIXTURES:
        label = f"{entry_id} {name} #{occ}"
        o, new, index = run_fixture(entry_id, name, occ, body)
        expect(o.status == expected, f"{label}: expected {expected}, got {o.status} {o.reasons}")
        if code:
            expect(any(r.split(":")[0] == code for r in o.reasons),
                   f"{label}: expected reason {code}, got {o.reasons}")
        blocks = parse_blocks(new)
        cands = candidates(blocks, legacy_names=True)
        span = blocks[cands[index].start:cands[index].end]
        if expected == "queued":
            # The whole span stays unchanged: here, the whole body.
            expect(new == body.split("\n"), f"{label}: a queued body must stay unchanged")
        else:
            expect(not validate(span), f"{label}: the result must validate: {validate(span)}")
        if expected == "valid":
            expect(new == body.split("\n"), f"{label}: a valid body must stay unchanged")
        if (entry_id, name) in EXACT:
            expect("\n".join(new) == EXACT[(entry_id, name)],
                   f"{label}: wrong output:\n" + "\n".join(new))
        if expected in ("valid", "rewritten"):
            again, outs = process_body(entry_id, new, {})
            expect(again == new, f"{label}: a second pass changed the text")
            expect(outs[index].status == "valid", f"{label}: the second pass must find it valid")

    # The lowercase list: a listed first word is lowercased, `Anytime` is not listed (Forewarned).
    new, _ = process_body("x", "**P (Su)**\n\n**Passive:** Text.\n\nAt 5th level: You gain a bonus.\n".split("\n"), {})
    expect("**At 5th level,** you gain a bonus." in new, f"lowercase list: {new}")
    o, _, _ = run_fixture("x", "P (Su)", 1, "**P (Su)**\n\n**Passive:** Text.\n\nAt 5th level: Anytime you gain.\n")
    expect(o.status == "queued" and o.reasons == ["upgrade-keeps-capital: Anytime"], f"Anytime: {o}")
    # The comma form and an ill-formed ordinal are queued.
    o, _, _ = run_fixture("x", "P (Su)", 1, "**P (Su)**\n\n**Passive:** Text.\n\nAt 5th level, you gain.\n")
    expect(o.status == "queued" and o.reasons == ["comma-upgrade"], f"comma form: {o}")
    o, _, _ = run_fixture("x", "P (Su)", 1, "**P (Su)**\n\n**Passive:** Text.\n\n**At 5st Level:** you gain.\n")
    expect(o.status == "queued" and o.reasons[0].startswith("ill-formed-level"), f"ordinal: {o}")

    # Resolutions: the Foretell seed holds until a resolution matches the exact span hash; an applied
    # resolution is a no-op; a changed span is a stale resolution, queued again.
    foretell = FIXTURES[10][5]
    body = foretell.split("\n")
    blocks = parse_blocks(body)
    c = candidates(blocks, True)[0]
    text = ("**Foretell (Su)**\n\n**Gained:** At 8th Level\n\n**Standard:** You foretell.\n\n"
            "**Usage:** Rounds per day equal to your level\n")
    res = Resolution("ref/arcaneschool/divination", "Foretell (Su)", 1, span_sha(blocks[c.start:c.end]),
                     "a book and page", text)
    resolutions = {(res.id, res.name, 1): res}
    expect(not check_resolution(res), f"the resolution must validate: {check_resolution(res)}")
    new, outs = process_body(res.id, body, resolutions)
    expect(outs[0].status == "resolved" and "\n".join(new) == text, f"a matching resolution applies: {outs}")
    again, outs = process_body(res.id, new, resolutions)
    expect(again == new and [o.status for o in outs] == ["resolution-noop"],
           f"an applied resolution is a no-op: {outs}")
    changed = [line.replace("1 time/day", "2 times/day") for line in body]
    again, outs = process_body(res.id, changed, resolutions)
    expect(again == changed and [o.status for o in outs][0] == "stale", f"a changed span is stale: {outs}")
    expect(outs[1].status == "queued", f"a stale resolution is queued again: {outs}")
    bad = Resolution(res.id, res.name, 1, res.span_sha256, "x", "**Foretell (Su)**\n\n**Gained:** At 8th Level\n")
    expect(check_resolution(bad) != [], "a replacement that fails validation is refused")
    listed = Resolution(res.id, res.name, 1, res.span_sha256, "x", text + "\n- **Option:** A bullet of print.\n")
    expect(check_resolution(listed) == [], "a valid power followed by a list is accepted")
    new, outs = process_body(res.id, (listed.replacement.strip("\n")).split("\n"), {(res.id, res.name, 1): listed})
    expect([o.status for o in outs] == ["resolution-noop"], f"an applied list resolution is a no-op: {outs}")
    bare = Resolution(res.id, res.name, 1, res.span_sha256, "x", "A paragraph.\n\n" + text)
    expect(check_resolution(bare) != [], "a replacement must start with a power")

    # With the automatic rewrite off, a resolution still applies and a rewritable power stays put.
    mixed = (foretell + "\n" + FIXTURES[1][5]).split("\n")
    new, outs = process_body(res.id, mixed, resolutions, rewrite=False)
    expect("Rounds per day" in "\n".join(new) and "**At 11th Level:**" in "\n".join(new),
           f"resolutions-only: {outs}")
    expect([o.status for o in outs] == ["resolved", "rewritten"], f"resolutions-only statuses: {outs}")

    # Decision 5: section labels are never candidates, whatever the case, colon or spacing; a name
    # that only starts with one is a power. A label still ends the run before it.
    for label in ("Base Evolutions", "base  evolutions", "Discipline Powers:", "Patron Spells",
                  "Bonus Spells", "Domain Spells", "Replacement Domain Spells"):
        body = f"**Real Power (Su)**\n\n**Passive:** x.\n\n**{label}**\n\n**At 1st Level:** Label line.\n"
        _, outs = process_body("ref/eidolon/x", body.split("\n"), {})
        expect([o.name for o in outs] == ["Real Power (Su)"], f"{label} is no candidate: {outs}")
    _, outs = process_body("x", "**Base Evolutions (Su)**\n\n**At 1st Level:** A line.\n".split("\n"), {})
    expect([o.name for o in outs] == ["Base Evolutions (Su)"], f"a longer name is a power: {outs}")
    for body in ("**Base Evolutions**\n\n**At 1st Level:** A line.\n\n**At 4th Level:** Another.\n",
                 "**Discipline Powers**\n\n**At 1st Level:** A line.\n"):
        _, outs = process_body("ref/eidolon/agathion", body.split("\n"), {})
        expect(outs == [], f"a section label span is no candidate: {outs}")
    _, outs = process_body("x", "**Granted Powers**\n\n**Ability:** Bonus feats.\n".split("\n"), {})
    expect([o.status for o in outs] == ["valid"], f"Granted Powers stays a power: {outs}")

    # The combinations of the owner's answer 1, straight through `validate`.
    def slugs(body: str) -> list[str]:
        blocks = parse_blocks(body.split("\n"))
        c = candidates(blocks)
        return sorted(validate(blocks[c[0].start:c[0].end]))
    expect(slugs("**P**\n\n**Passive:** a.\n\n**Standard:** b.\n") == [], "passive then action is valid")
    expect(slugs("**P**\n\n**Ability:** a.\n\n**Full-round:** b.\n") == [], "ability then action is valid")
    expect(slugs("**P**\n\n**Passive:** a.\n\n**Usage:** u.\n\n**Standard:** b.\n") == ["out-of-order"],
           "a row between the pair is out of order")
    expect(slugs("**P**\n\n**Passive:** a.\n\n**Choice:** c.\n\n**Standard:** b.\n") == ["out-of-order"],
           "Choice between the pair is out of order")
    expect(slugs("**P**\n\n**Passive:** a.\n\n**Fullround:** b.\n") == ["legacy-label"],
           "an alias is the label it becomes, and still a legacy label")
    expect(slugs("**P**\n\n**Passive:** a.\n\n**Usage:** u.\n\nLoose.\n") == ["stray-paragraph"],
           "a paragraph after Usage is stray")
    expect(slugs("**P**\n\n**Passive:** a.\n\n**Special:** s.\n\nOne.\n\nTwo.\n\n**Penalty:** p.\n\nStray.\n")
           == ["stray-paragraph"], "only Special has continuation")

    # An applied resolution that renamed its power (a legacy name loses its colon) is not orphaned.
    legacy = "**Pool Ray:**\n\n**Standard:** Infuse.\n\n**Free:** Release.\n"
    blocks = parse_blocks(legacy.split("\n"))
    c = candidates(blocks, True)[0]
    renamed = Resolution("ref/arcana/pool-ray", "Pool Ray:", 1, span_sha(blocks[c.start:c.end]), "a book and page",
                         "**Pool Ray**\n\n**Standard:** Infuse.\n\nRelease.\n")
    keyed = {("ref/arcana/pool-ray", "Pool Ray:", 1): renamed}
    after, outs = process_body("ref/arcana/pool-ray", legacy.split("\n"), keyed)
    expect(outs[0].status == "resolved" and after[0] == "**Pool Ray**", f"the rename applies: {outs}")
    again, outs = process_body("ref/arcana/pool-ray", after, keyed)
    expect(unused_resolutions(keyed, outs) == ([], []), "an applied, renamed resolution is not orphaned")

    # The upgrade level is checked against the first `Gained` row that parses.
    expect("upgrade-not-above-gained" in slugs(
        "**P**\n\n**Gained:** soon\n\n**Gained:** At 5th Level\n\n**Passive:** a.\n\n**At 3rd level,** b.\n"),
        "the first parseable Gained row sets the level")

    # A stale resolution is queued again and the automatic rewrite leaves the power alone.
    rewritable = "**Resistance (Ex)**\n\n**At 11th Level:** Increases.\n\n**Gained:** At 1st Level\n\n**Passive:** Base.\n"
    blocks = parse_blocks(rewritable.split("\n"))
    c = candidates(blocks, True)[0]
    other = Resolution("ref/x/y", "Resistance (Ex)", 1, "0" * 64, "a book and page",
                       "**Resistance (Ex)**\n\n**Passive:** Something else.\n")
    stale_new, stale_outs = process_body("ref/x/y", rewritable.split("\n"), {("ref/x/y", "Resistance (Ex)", 1): other})
    expect(stale_new == rewritable.split("\n"), "a stale resolution leaves the power unchanged")
    expect([(o.status, o.reasons) for o in stale_outs] == [("stale", ["stale-resolution"]),
                                                         ("queued", ["stale-resolution"])],
           f"a stale resolution is reported and queued again: {stale_outs}")
    # A matching resolution key, a key that matches nothing, and a section label that is no power.
    used = {("ref/x/y", "Resistance (Ex)", 1): other}
    gone = Resolution("ref/x/gone", "Gone (Su)", 1, "0" * 64, "x", other.replacement)
    label = Resolution("ref/eidolon/x", "Base Evolutions", 1, "0" * 64, "x", other.replacement)
    allres = dict(used)
    allres[("ref/x/gone", "Gone (Su)", 1)] = gone
    allres[("ref/eidolon/x", "Base Evolutions", 1)] = label
    orphaned, obsolete = unused_resolutions(allres, stale_outs)
    expect(orphaned == [("ref/x/gone", "Gone (Su)", 1)], f"an orphaned resolution is reported: {orphaned}")
    expect(obsolete == [("ref/eidolon/x", "Base Evolutions", 1)], f"an obsolete one too: {obsolete}")

    # Hash: it does not depend on how a paragraph is wrapped.
    wrapped = parse_blocks("**N (Su)**\n\n**Passive:** one two\nthree four\n".split("\n"))
    flat = parse_blocks("**N (Su)**\n\n**Passive:** one two three four\n".split("\n"))
    expect(span_sha(wrapped[:2]) == span_sha(flat[:2]), "the span hash must not depend on wrapping")

    # Exceptions: a failing power that an exception names (with the right span hash) is excepted,
    # is left unchanged and leaves the queue; a changed span is stale and queued; a power that
    # passes is obsolete; a key that matches no candidate is orphaned.
    failing_body = "**Reckoning**\n\n**Benefit:** A bonus.\n\n**Reckoning:** Do it.\n\nProse about the order.\n"
    failing_run = parse_blocks(failing_body.split("\n"))
    sha = span_sha(failing_run[:4])
    key = ("ref/hkorder/x", "Reckoning", 1)

    def exc(span):
        return {key: PowerException(*key, span, "print cannot settle it", "Some Book p. 1")}
    new, outs = process_body(key[0], failing_body.split("\n"), {}, exceptions=exc(sha))
    expect([o.status for o in outs] == ["excepted"] and new == failing_body.split("\n"),
           f"an exception leaves the failing power unchanged: {outs}")
    expect(queue_text(outs) == QUEUE_HEADER + "\n", "an excepted power is not queued")
    new, outs = process_body(key[0], failing_body.split("\n"), {}, exceptions=exc("0" * 64))
    expect([o.status for o in outs] == ["stale-exception", "queued"], f"a changed span is stale: {outs}")
    passing_body = "**Reckoning**\n\n**Benefit:** A bonus.\n"
    new, outs = process_body(key[0], passing_body.split("\n"), {},
                             exceptions=exc(span_sha(parse_blocks(passing_body.split("\n")))))
    expect([o.status for o in outs] == ["obsolete-exception"], f"a passing power is obsolete: {outs}")
    expect(unused_exceptions(exc(sha), outs) == [], "a matched exception is not orphaned")
    expect(unused_exceptions({("ref/gone", "Gone", 1): None}, outs) == [("ref/gone", "Gone", 1)],
           "an orphaned exception is reported")

    # Converted entries (#540): an entry without import rows is out of scope, so its resolutions and exceptions are
    # retired, while a key of an entry that still has import rows (or of an entry that is gone) stays orphaned.
    converted = "## Resistance (Ex) {#resistance}\n\nAt 1st level, you gain resistance 5.\n"
    single = "You gain a +2 bonus on saves against fear.\n"
    stale_import = "**Resistance (Ex)**\n\n**Passive:** You gain resistance 5.\n"
    expect(not entry_in_scope(converted.split("\n")), "headed printed prose has no import row")
    expect(not entry_in_scope(single.split("\n")), "a single-power option without features has no import row")
    expect(entry_in_scope(stale_import.split("\n")), "labeled rows are import rows")
    expect(entry_in_scope("**P**\n\n**At 11th level,** more.\n".split("\n")), "an upgrade lead is an import row")
    expect(entry_in_scope("**P**\n\nAt 5th level: more.\n".split("\n")), "a plain-text upgrade in the colon form is an import row")
    expect(not entry_in_scope("A druid gains a bonus.\n\nAt 5th level, the bonus grows.\n".split("\n")), "printed prose with an upgrade sentence is none")
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        for name, body in (("converted", converted), ("single", single), ("live", stale_import), ("named", "**Resistance (Ex)**\n\nAt 1st level, you gain resistance 5.\n")):
            d = Path(tmp) / "entries" / "a"
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{name}.md").write_text(f'+++\nid = "ref/a/{name}"\nkind = "class_option"\ntitle = "{name}"\n\n[fields]\nkind = "class_option"\n+++\n\n{body}')
        expect(retired_entries(Path(tmp)) == {"ref/a/converted", "ref/a/single", "ref/a/named"}, f"retired entries of a mini corpus: {retired_entries(Path(tmp))}")
        standing = bold_only_names(Path(tmp), retired_entries(Path(tmp)))
        expect("resistance" in standing.get("ref/a/named", set()) and "resistance" not in standing.get("ref/a/converted", set()),
               f"a retired entry whose power name still stands as a bold-only block is found: {standing}")
    keys = [("ref/a/converted", "Resistance (Ex)", 1), ("ref/a/live", "Resistance (Ex)", 1), ("ref/a/gone", "Resistance (Ex)", 1)]
    live, ret = split_retired(keys, {"ref/a/converted"})
    expect(live == keys[1:] and ret == keys[:1], f"retired and orphaned keys are told apart: {live} {ret}")

    # An action-first pair passes validation: an exception for it is obsolete, as in the app.
    pair_body = "**Pair (Su)**\n\n**Standard:** Act.\n\n**Passive:** Be.\n"
    pair_key = ("ref/x/pair", "Pair (Su)", 1)
    pair_sha = span_sha(parse_blocks(pair_body.split("\n"))[:3])
    new, outs = process_body(pair_key[0], pair_body.split("\n"), {},
                             exceptions={pair_key: PowerException(*pair_key, pair_sha, "r", "p")})
    expect([o.status for o in outs] == ["obsolete-exception"], f"an action-first pair is obsolete: {outs}")

    # The loader accepts the app's file and nothing else.
    import tempfile
    good = ('[[exception]]\nid = "ref/a/b"\nname = "N"\noccurrence = 1\n'
            f'span_sha256 = "{"a" * 64}"\nreason = "r"\nprint = "p"\n')
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "power-exceptions.toml"
        path.write_text(good)
        expect(len(load_exceptions(path)) == 1, "a valid exceptions file loads")
        for broken in (good.replace("occurrence = 1", "occurrence = 0"),
                       good.replace("occurrence = 1", 'occurrence = "1"'),
                       good.replace("a" * 64, "A" * 64),
                       good.replace("a" * 64, "ab"),
                       good + "extra = 1\n",
                       good.replace('span_sha256 = "%s"\n' % ("a" * 64), ""),
                       good.replace('reason = "r"', 'reason = " "')):
            path.write_text(broken)
            try:
                load_exceptions(path)
                expect(False, f"a broken exceptions file must be refused: {broken!r}")
            except SystemExit:
                pass

    for message in failures:
        print("FAIL", message)
    print(f"self-test: {len(FIXTURES)} fixtures, {len(failures)} failures")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--write", action="store_true", help="rewrite the entries and write the queue file")
    ap.add_argument("--write-queue", action="store_true", help="write the queue file only")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--resolutions-only", action="store_true",
                    help="apply the resolutions and nothing else (the automatic rewrite stays off)")
    ap.add_argument("--families", help="comma-separated families to rewrite, e.g. mystery,oraclecurse")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    corpus = Path(args.corpus)
    families = set(args.families.split(",")) if args.families else None
    resolutions = load_resolutions(corpus / RESOLUTIONS_FILE)
    exceptions = load_exceptions(corpus / EXCEPTIONS_FILE)
    bad = [f"{r.id} {r.name} #{r.occurrence}: {m}" for r in resolutions.values() for m in check_resolution(r)]
    if bad:
        print("\n".join("invalid resolution: " + b for b in bad))
        return 1
    # Dry run first: nothing is written while a resolution is stale, orphaned or obsolete.
    outcomes, changed = run_corpus(corpus, resolutions, families, write=False,
                                   rewrite=not args.resolutions_only, exceptions=exceptions)
    print(summarize(outcomes, changed))
    stale = [o for o in outcomes if o.status == "stale"]
    orphaned, obsolete = unused_resolutions(resolutions, outcomes)
    retired = retired_entries(corpus)
    orphaned, retired_resolutions = split_retired(orphaned, retired)
    obsolete, dropped_obsolete = split_retired(obsolete, retired)
    unused = unused_exceptions(exceptions, outcomes)
    unused, retired_exceptions = split_retired(unused, retired)
    standing = bold_only_names(corpus, retired)
    still_named = [k for k in retired_resolutions + retired_exceptions if re.sub(r"[^a-z0-9]", "", re.sub(r"\s*\((?:Ex|Su|Sp)[^)]*\)\s*:?$", "", k[1]).lower()) in standing.get(k[0], set())]
    retired_resolutions = [k for k in retired_resolutions if k not in still_named]
    retired_exceptions = [k for k in retired_exceptions if k not in still_named]
    print(f"retired (entry converted or without import rows): {len(retired_resolutions)} resolutions, {len(retired_exceptions)} exceptions; "
          f"{len(dropped_obsolete)} obsolete keys of retired entries dropped")
    problems = ["orphaned resolution or exception (the entry has no import row, but the power's name still stands as a bold-only block): %s %s #%d" % k
                for k in still_named]
    for o in stale:
        problems.append(f"stale resolution: {o.entry_id} {o.name} #{o.occurrence}")
    for key in orphaned:
        problems.append("orphaned resolution (matches no candidate): %s %s #%d" % key)
    for key in obsolete:
        problems.append("obsolete resolution (a section label is no power): %s %s #%d" % key)
    for o in outcomes:
        if o.status == "stale-exception":
            problems.append(f"stale exception (the span changed): {o.entry_id} {o.name} #{o.occurrence}")
        elif o.status == "obsolete-exception":
            problems.append(f"obsolete exception (the power passes): {o.entry_id} {o.name} #{o.occurrence}")
        elif o.reasons == ["both-exception-and-resolution"]:
            problems.append(f"an exception and a resolution for one power: {o.entry_id} {o.name} #{o.occurrence}")
    for key in unused:
        problems.append("orphaned exception (matches no candidate): %s %s #%d" % key)
    for line in problems:
        print(line)
    queue = corpus / QUEUE_FILE
    if args.write or args.write_queue:
        if problems:
            print("nothing written: fix the resolutions first")
            return 1
        if args.write:
            run_corpus(corpus, resolutions, families, write=True, rewrite=not args.resolutions_only,
                       exceptions=exceptions)
        queue.write_text(queue_text(outcomes))
        return 0
    if args.check:
        current = queue.read_text() if queue.exists() else ""
        extra = []
        if changed:
            extra.append(f"{len(changed)} entries would change")
        if current != queue_text(outcomes):
            extra.append(f"{QUEUE_FILE} is out of date")
        for line in extra:
            print("check:", line)
        return 1 if problems or extra else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
