#!/usr/bin/env python3
"""Write creature and NPC statistics as stat blocks (cast-iron-data #166, with cast-iron #254).

A Pf Data monster prints its statistics as one bold-label paragraph per row, with the section
names as bold paragraphs:

    **Challenge rating:** 4          **Armor class:** 15      **Offense**
    **Initiative:** +5               **Touch:** 10            **Speed:** 30 ft.

The owner decisions of 2026-11-22 give every monster the same form: an untitled lead stat block,
then a `###` heading and an untitled stat block for each printed section (Defense, Offense,
Statistics, Ecology), with the spell sub-blocks as titled stat blocks:

    ::: statblock                    ### Defense              ### Offense
    Challenge rating: 4
    Initiative: +5                   ::: statblock            ::: statblock
    :::                              Armor class: 15          Speed: 30 ft.
                                     Touch: 10                :::
                                     :::

Labels and values stay byte for byte; rows keep the order they have now; `[fields]` is never
touched. What the script cannot convert by the rules below stays unchanged and is listed in
`scripts/stat-blocks-review-166.tsv` with the reason.

Usage (DIR defaults to the repository root):

    python3 scripts/stat-blocks-166.py [DIR]                 survey: counts, writes nothing
    python3 scripts/stat-blocks-166.py [DIR] --write         convert, and write the review TSV
    python3 scripts/stat-blocks-166.py [DIR] --check         exit 1 when a rerun of the applied
                                                             slices would change a file, a print
                                                             fix is not applied, or the TSV is stale
    python3 scripts/stat-blocks-166.py --self-test           run the built-in tests

    --pass creature[,npc,item]   which passes run (default: every pass this version implements)
    --pass fixes                 no conversion: `--write` applies the print fixes and writes the TSV
    --only a-d                   entry files whose name starts with a letter of the range(s)
    --only eq-misc,magic-ring    or the entries of the named folders (both kinds can be mixed)

Passes. `creature` (the folder `entries/monster`) and `npc` (`entries/npc`) are implemented. `item`
arrives with its own slices; this version refuses it rather than guess at its rules.

`--check` without `--pass` or `--only` checks the slices listed in `APPLIED` below. Each slice
PR adds its slice to that list, so the check on a PR head covers exactly what has been written.

Rules for the creature pass
---------------------------

C1  Scope. A file of `entries/monster` with `kind = "creature"` and exactly one
    `**Challenge rating:**` paragraph and one `**Armor class:**` paragraph. The statistics region
    runs from the start of the body to the first heading that is neither a footnote heading
    (`###### X {#footnote-x}`) nor `### Tactics`. Everything from that heading on is copied
    unchanged. A file that prints a second set of statistics after that heading (the elementals
    print one per size) is queued whole (`section-after-heading`).
C2  Row. A paragraph `**Label:** value` becomes the row `Label: value`. Wrapped lines join with
    one space. The label and the value are not edited, sorted or relabelled (`Spec Att`, `Dr`,
    `Sr` stay).
C3  Lead block. The rows before `**Armor class:**` become one untitled stat block.
C4  Paragraphs before the first row (the italic read-aloud line, a name line) stay where they are.
C5  Descriptor. One bold paragraph without a colon among the lead rows (`**Aasimar cleric 1**`)
    moves directly above the lead block, text unchanged. Two such paragraphs are queued.
C6  Defense. The rows from `**Armor class:**` to the next section become `### Defense` and an
    untitled stat block. `Defense` is the only word the pass adds to a body.
C7  Sections. `**Offense**`, `**Statistics**` and `**Ecology**` each become a `###` heading with
    that text, followed by an untitled stat block of the rows that follow. They must come in that
    order, each at most once.
C8  Spell sub-blocks. `**Spell-Like Abilities**`, `**Spells Known**`, `**Prepared Spells**`,
    `**Psychic Magic**` and `**Spellcasting**` each become a stat block with that title. The rows
    that follow belong to it until the next section or sub-block.
C9  List rows. A row with no value that is followed by a flat list takes the list items as its
    value, one per line, joined by breaks (`Per day: 1/day: daylight`).
C10 Footnotes. A footnote heading and its text inside the region stay where they are. They close
    the block they stand in; rows after them open an untitled block.
C11 Tactics. `### Tactics` and its paragraphs stay where they are, between the blocks.
C12 Anchors. A new heading takes the key `sec-<name>`. When the entry already has a heading with
    that key (a prose `### Ecology`), the new heading carries the explicit anchor `{#stat-<name>}`
    so no existing key moves.
C13 Queue. Anything else in the region queues the whole file, unchanged: a paragraph with several
    labels that C15 does not cover, a bold paragraph inside a section, prose between rows, a list
    that does not follow an empty row, a nested or escaped list, a fenced block, a section with no
    rows, a label that would need escaping, a `**Sources:**` citation line among the rows (it is
    not a statistic).
C14 The nine rows that cast-iron #254 left for a print check (`othersubs`, `tremorParens`,
    `blindsightParens`, `augment`) convert like any row and are listed in the TSV as `print-254`.
C15 Rows joined by a break. A paragraph whose lines end in a hard break (`\\`) becomes one row per
    segment, in order, when every segment on its own is a C2 row: it starts with its own
    `**Label:**`, its label needs no escaping, and its value holds no further `:**` and no edge
    escape. The breaks are dropped. If any segment fails, the whole file is queued. Two labels in
    one paragraph without a break between them are always queued.

Rules for the NPC pass (owner rulings of 2026-11-23)
----------------------------------------------------

An NPC prints its statistics as run-on lines under headings that already exist:

    **Challenge rating:** 5                           ### Defense
    **XP** 1,600\\
    Human evoker 6\\                                  **AC** 16, touch 12, flat-footed 14 (+2 Dex)\\
    N Medium humanoid\\                               **hp** 33 (6d6+12)\\
    **Init** +6; **Senses** Perception +6             **Fort** +3, **Ref** +4, **Will** +5

N1  Scope. A file of `entries/npc` with `kind = "creature"` and exactly one
    `**Challenge rating:**` paragraph. The statistics are the lead (everything before the first
    heading) and the sections `### Defense`, `### Offense`, `### Statistics` and `### Ecology`,
    each at most once. Every other section (`### Tactics`, `### Special Abilities`,
    `### Description`, a footnote) is copied unchanged, and no heading is added, removed or
    changed. An entry that prints a second set of statistics (a mount in a quote) is queued.
N2  Paragraphs before `**Challenge rating:**` (the read-aloud line) stay where they are.
N3  Unlabelled lead lines. The lines without a label that follow one another in the lead (the
    class line, then the alignment, size and type line) stay unchanged, break included, as one
    paragraph directly above the lead block. They get no `Alignment`, `Size` or `Type` rows.
N4  Rows. A line `**Label** value` becomes the row `Label: value`. A line with several labels
    becomes one row per label, in order, and the `;` before a label is dropped
    (`**Base Atk** +3; **CMB** +2; **CMD** 17`). A `,` before a label is dropped only before
    `Ref`, `Will`, `Dex`, `Con`, `Int`, `Wis`, `Cha` and `Reach` (`**Fort** +3, **Ref** +4`; the
    `Str` to `Cha` line becomes six rows). Text after the last label of a line stays in its value
    (`Will: +5; +2 vs. enchantments`). The lead block is `Challenge rating` and the lead rows; each
    section gets one untitled block.
N5  Spell lists. A line `**Title** (CL 6th; concentration +9)` followed by level lines opens a
    stat block with that title, as the monster spell blocks have. Its first rows are `CL: 6th` and
    `concentration: +9`: the parentheses and the `;` go. Each level line `_3rd_-fly, haste` becomes
    the row `3rd: fly, haste`: the emphasis markers and the dash go. The rows after the level lines
    (`Bloodline`, `Domains`, `Opposition Schools`) stay in that block, as in monsters (C8). A
    header with any other part (`arcane spell failure 10%`, `conc. +5`) is queued.
N6  The linked label `[Spell-Like Abilities](ref/umr/spell-like-abilities)` becomes the plain title
    `Spell-Like Abilities`; the link is dropped. Any other label with markup is queued.
N7  Queue. Anything else queues the whole file, unchanged: an unlabelled line outside N3 (an
    `Aura …` line after `Init`), two labels with no `;` between them, a `,` before another label,
    a level line outside a spell list, prose, a quote or a list in a statistics section, a
    section printed twice, a value with an edge escape.

The NPC word proof allows exactly the separators N4 to N6 drop, and only inside the statistics:
the `;` or `,` before a label, the parentheses and `;` of a spell list header, the `_ _-` of a
level label, and the one link of N6. A row adds the colon after its label. Every other word,
spell name, count and number must be found again, in order; the unlabelled lead lines are checked
as moved. `npc_proof_words` does this reading on its own, apart from the converter.

Proofs, run on every file before it is written (a failure aborts the run and writes nothing more):

- the front matter, `[fields]` included, is byte-identical;
- the text after the statistics region is byte-identical;
- the body has the same words in the same order, markup and row separators aside, except the one
  added heading word `Defense` and the moved descriptor line;
- every heading that existed keeps its key; the new headings have keys of their own.

A file is converted all or nothing, written to a temporary file in its directory and renamed.
The script is idempotent: a converted file reads as `already`.

Print fixes. Two entries would disagree with their `[fields]` once their rows are compared, so
`--write` corrects them from print first (`PRINT_FIXES`). They are listed in the TSV as
`print-fix`.
"""

from __future__ import annotations

import collections
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

REVIEW_TSV = "scripts/stat-blocks-review-166.tsv"
TSV_HEADER = "path\tpass\treason\tdetail"
FRONT_MATTER_END = "\n+++\n"

# The slices already written to the corpus: (pass, --only value or None for the whole pass).
# `--check` with no scope arguments checks exactly these.
APPLIED: list[tuple[str, str | None]] = [("creature", None)]

PASS_FOLDERS = {"creature": ("monster",), "npc": ("npc",), "fixes": ()}
KNOWN_PASSES = ("creature", "npc", "item", "fixes")

SECTIONS = ("Defense", "Offense", "Statistics", "Ecology")
SUBSECTIONS = ("Spell-Like Abilities", "Spells Known", "Prepared Spells", "Psychic Magic", "Spellcasting")
PRINT_254_LABELS = ("othersubs", "tremorParens", "blindsightParens", "augment")

HEADING = re.compile(r"^(#{1,6}) (.*?)(?: \{#([A-Za-z0-9_.-]+)\})?$")
NOTE_HEADING = re.compile(r"^###### .*\{#footnote-[^}]+\}$")
TACTICS_HEADING = "### Tactics"
COLON_ROW = re.compile(r"^\*\*([^*\[\]]+?):\*\*(?: (.*))?$", re.S)
BOLD_ONLY = re.compile(r"^\*\*([^*:]+)\*\*$", re.S)
# An escape the writer adds only at the start of a paragraph line (a block marker, a leading
# blank). Inside a row it would not be canonical, so such a value is queued.
GUARDED = re.compile(r"\\[-+0-9: \t]")
RESERVED_KEYS = ("entry-related",)  # crates/schema/src/headings.rs RESERVED_ANCHOR_KEYS

# (path, publication and page, note, [(old text, new text, later forms of the new text...), ...]).
# Each old text occurs exactly once before the fix and never after it.
PRINT_FIXES = (
    (
        "entries/monster/elemental-lord-ymeri.md",
        "Planes of Power p. 54",
        "melee: `flaming burst` where the import left `EFB`",
        (
            (
                'melee = "+4 earth-outsider-bane ~EFB longsword +44/+39/+34/+29 (2d6+14 plus',
                'melee = "+4 earth-outsider-bane flaming burst longsword +44/+39/+34/+29 (2d6+14 plus',
            ),
            (
                "**Melee:** +4 earth-outsider-bane , EFB longsword +44/+39/+34/+29 (2d6+14 plus 1d6 fire/17-20), 3 +4\n"
                "earth-outsider-bane flaming burst longswords +40 (2d6+9 plus 1d6 fire/17-20), 2 claws +37 (1d8+5\n"
                "plus 1d10 fire plus trip)\n",
                "**Melee:** +4 earth-outsider-bane flaming burst longsword +44/+39/+34/+29 (2d6+14 plus 1d6\n"
                "fire/17-20), 3 +4 earth-outsider-bane flaming burst longswords +40 (2d6+9 plus 1d6 fire/17-20), 2\n"
                "claws +37 (1d8+5 plus 1d10 fire plus trip)\n",
                # The same line once the creature pass has made it a row.
                "\nMelee: +4 earth-outsider-bane flaming burst longsword +44/+39/+34/+29 (2d6+14 plus 1d6 "
                "fire/17-20), 3 +4 earth-outsider-bane flaming burst longswords +40 (2d6+9 plus 1d6 fire/17-20), 2 "
                "claws +37 (1d8+5 plus 1d10 fire plus trip)\n",
            ),
        ),
    ),
    (
        "entries/eq-weaponenh/brutally-weighted.md",
        "Adventurer's Armory 2 p. 10",
        "price: `+1,500 gp`; the field also held the weight",
        (('price = "+1,500 gp **Weight** +1 lb."\n', 'price = "+1,500 gp"\n'),),
    ),
)


class Queue(Exception):
    """The file stays unchanged; `reason` goes to the review TSV."""

    def __init__(self, reason: str, detail: str = ""):
        super().__init__(reason)
        self.reason = reason
        self.detail = detail


class ProofFailed(Exception):
    pass


# ---- reading ---------------------------------------------------------------------------------


def split_front(text: str) -> tuple[str, str]:
    if not text.startswith("+++\n"):
        raise ValueError("no front matter")
    end = text.index(FRONT_MATTER_END, 4) + len(FRONT_MATTER_END)
    return text[:end], text[end:]


def region_end(lines: list[str]) -> int:
    """Index of the first heading line that ends the statistics region, or len(lines)."""
    fenced = False
    for index, line in enumerate(lines):
        if line.startswith(":::"):
            fenced = line != ":::"
            continue
        if fenced:
            continue
        if HEADING.match(line) and not NOTE_HEADING.match(line) and line != TACTICS_HEADING:
            return index
    return len(lines)


def chunks(lines: list[str]) -> list[list[str]]:
    """Blank-line separated blocks. A heading line is a block of its own."""
    out: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if not line.strip():
            if current:
                out.append(current)
                current = []
            continue
        if HEADING.match(line) and not current:
            out.append([line])
            continue
        current.append(line)
    if current:
        out.append(current)
    return out


def join_wrapped(lines: list[str]) -> str:
    """A wrapped paragraph on one line. The writer wraps only at single spaces."""
    return " ".join(lines)


def flat_list(chunk: list[str]) -> list[str] | None:
    """The items of a flat list of one-paragraph items, each on one line; else None."""
    items: list[list[str]] = []
    for line in chunk:
        if line.startswith("- "):
            items.append([line[2:]])
        elif line.startswith("  ") and items and not line[2:].startswith((" ", "- ", "+ ")):
            items[-1].append(line[2:])
        else:
            return None
    values = [join_wrapped(item) for item in items]
    if any(value.endswith("\\") or GUARDED.match(value) or not value for value in values):
        return None
    return values


# ---- heading keys (crates/schema/src/headings.rs) -----------------------------------------------


def plain_text(inline: str) -> str:
    out = []
    index = 0
    while index < len(inline):
        ch = inline[index]
        if ch == "\\" and index + 1 < len(inline):
            out.append(inline[index + 1])
            index += 2
            continue
        if ch == "]" and inline.startswith("](", index):
            close = inline.find(")", index)
            if close != -1:
                index = close + 1
                continue
        if ch in "*_^~[":
            index += 1
            continue
        out.append(ch)
        index += 1
    return "".join(out)


def slugify(text: str) -> str:
    out = []
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


def heading_lines(body: str) -> list[str]:
    found = []
    fenced = False
    for line in body.split("\n"):
        if line.startswith(":::"):
            fenced = line != ":::"
            continue
        if fenced:
            continue
        stripped = re.sub(r"^(?:\s*(?:> ?|- ))*\s*", "", line)
        if HEADING.match(stripped):
            found.append(stripped)
    return found


def heading_keys(lines: list[str]) -> list[str | None]:
    bases: list[str | None] = []
    for line in lines:
        match = HEADING.match(line)
        if match.group(3):
            bases.append(match.group(3))
        else:
            slug = slugify(plain_text(match.group(2)))
            bases.append("sec-" + slug if slug else None)
    literal = {base for base in bases if base}
    used = set(RESERVED_KEYS)
    keys: list[str | None] = []
    for base in bases:
        if base is None:
            keys.append(None)
            continue
        key = base
        if key in used:
            suffix = 2
            while f"{base}-{suffix}" in literal or f"{base}-{suffix}" in used:
                suffix += 1
            key = f"{base}-{suffix}"
        used.add(key)
        keys.append(key)
    return keys


# ---- the creature pass ---------------------------------------------------------------------------


def render_block(title: str | None, rows: list[tuple[str, list[str]]]) -> str:
    out = ["::: statblock"]
    if title is not None:
        out.append(f'title = "{title}"')
    for label, values in rows:
        text = label + ":" + (" " + values[0] if values[0] else "")
        out.append("\\\n".join([text] + values[1:]))
    out.append(":::")
    return "\n".join(out)


def words(text: str, drop_line: str | None = None) -> list[str]:
    """The words of a body with the markup this pass adds or removes taken out."""
    out: list[str] = []
    dropped = drop_line is None
    in_block = False
    for line in text.split("\n"):
        if not dropped and line == drop_line:
            dropped = True
            continue
        if line == "::: statblock":
            in_block = True
            continue
        if line == ":::":
            in_block = False
            continue
        if in_block:
            title = re.fullmatch(r'title = "(.*)"', line)
            if title:
                line = title.group(1)
        else:
            heading = HEADING.match(line)
            if heading:
                line = heading.group(2)
            elif line.startswith("- "):
                line = line[2:]
        if line.endswith("\\") and not line.endswith("\\\\"):
            line = line[:-1]
        out.extend(line.replace("**", "").split())
    return out


def classify_monster(body: str) -> str:
    """`paragraphs`, `already`, or raises Queue."""
    count = len(re.findall(r"^\*\*Challenge rating:\*\*", body, re.M))
    if count == 1:
        return "paragraphs"
    if count == 0 and re.search(r"^::: statblock\nChallenge rating:", body, re.M) and "\n### Defense" in body:
        return "already"
    if count > 1:
        raise Queue("section-after-heading", f"{count} Challenge rating lines")
    raise Queue("challenge-rating-lines", "0")


def convert_monster(body: str) -> str:
    """The converted body. Raises Queue when a rule does not cover the file."""
    lines = body.split("\n")
    end = region_end(lines)
    region, rest = lines[:end], lines[end:]
    rest_text = "\n".join(rest)
    for marker in ("**Offense**", "**Statistics**", "**Ecology**"):
        if re.search(r"^" + re.escape(marker) + r"$", rest_text, re.M):
            raise Queue("section-after-heading", marker.strip("*"))
    for marker in ("**Challenge rating:**", "**Armor class:**"):
        if re.search(r"^" + re.escape(marker), rest_text, re.M):
            raise Queue("section-after-heading", marker.strip("*:"))
    if any(line.startswith(":::") for line in region):
        raise Queue("fence-in-region")
    if len(re.findall(r"^\*\*Armor class:\*\*", "\n".join(region), re.M)) != 1:
        raise Queue("armor-class-lines")

    parts: list[tuple[str, object]] = []  # ("raw", text) | ("heading", name) | ("block", (title, rows))
    block: list | None = None  # [title, rows, is_continuation]
    seen: list[str] = []
    started = False
    lead_at: int | None = None  # index in `parts` where the lead block goes
    descriptor: str | None = None

    def close() -> None:
        nonlocal block
        if block is None:
            return
        title, rows, continuation = block
        if rows:
            parts.append(("block", (title, rows)))
        elif not continuation:
            raise Queue("empty-section", title or (seen[-1] if seen else "lead"))
        block = None

    cs = chunks(region)
    index = 0
    while index < len(cs):
        chunk = cs[index]
        text = "\n".join(chunk)
        index += 1
        if chunk[0] == TACTICS_HEADING:
            close()
            parts.append(("raw", text))
            while index < len(cs):
                nxt = "\n".join(cs[index])
                if COLON_ROW.match(nxt) or BOLD_ONLY.match(nxt) or HEADING.match(cs[index][0]):
                    break
                parts.append(("raw", nxt))
                index += 1
            block = [None, [], True]
            continue
        if NOTE_HEADING.match(chunk[0]):
            if not started:
                raise Queue("note-before-rows")
            close()
            parts.append(("raw", text))
            if index < len(cs) and not cs[index][0].startswith(("**", "#", "- ")):
                parts.append(("raw", "\n".join(cs[index])))
                index += 1
            else:
                raise Queue("note-without-text")
            block = [None, [], True]
            continue
        if HEADING.match(chunk[0]):
            raise Queue("heading-in-region", chunk[0])
        row = COLON_ROW.match(text)
        if row:
            # C15: a hard break ends a row when every segment is a row of its own.
            segments = text.split("\\\n")
            found: list[tuple[str, list[str]]] = []
            for segment in segments:
                part = COLON_ROW.match(segment)
                if part is None:
                    raise Queue("multi-label-paragraph", row.group(1))
                label, value = part.group(1), part.group(2) or ""
                if "\n**" in segment or ":**" in value:
                    raise Queue("multi-label-paragraph", label)
                if label == "Sources":
                    raise Queue("sources-line-in-region")
                if "\\" in label or ":" in label or label != label.strip():
                    raise Queue("label-needs-escape", label)
                value = join_wrapped(value.split("\n"))
                if value.endswith("\\") or GUARDED.match(value):
                    raise Queue("escaped-edge", label)
                found.append((label, [value]))
            if len(found) == 1 and not found[0][1][0] and index < len(cs) and cs[index][0].startswith("- "):
                listed = flat_list(cs[index])
                if listed is None:
                    raise Queue("unflat-list", found[0][0])
                found[0] = (found[0][0], listed)
                index += 1
            for label, values in found:
                if label == "Armor class":
                    if seen:
                        raise Queue("armor-class-after-section")
                    close()
                    parts.append(("heading", "Defense"))
                    seen.append("Defense")
                    block = [None, [], False]
                elif block is None:
                    if seen or started:
                        raise Queue("row-outside-block", label)
                    lead_at = len(parts)
                    block = [None, [], False]
                block[1].append((label, values))
                started = True
            continue
        bold = BOLD_ONLY.match(text)
        if bold:
            name = bold.group(1)
            if name in SECTIONS[1:]:
                if not seen or SECTIONS.index(name) <= SECTIONS.index(seen[-1]):
                    raise Queue("section-order", name)
                close()
                parts.append(("heading", name))
                seen.append(name)
                block = [None, [], False]
                continue
            if name in SUBSECTIONS:
                if not seen:
                    raise Queue("sub-block-in-lead", name)
                close()
                block = [name, [], False]
                continue
            if not started:
                parts.append(("raw", text))
                continue
            if not seen:
                if descriptor is not None:
                    raise Queue("two-descriptors")
                descriptor = text
                continue
            raise Queue("bold-paragraph-in-section", " ".join(name.split()))
        if text.startswith("- "):
            raise Queue("list-without-empty-row")
        if not started and not text.startswith("**"):
            parts.append(("raw", text))
            continue
        if text.startswith("**"):
            raise Queue("multi-label-paragraph", text[2:].split("**")[0])
        raise Queue("prose-in-region", " ".join(text.split())[:40])
    close()
    if seen[:1] != ["Defense"] or lead_at is None:
        raise Queue("no-lead-or-defense")
    if descriptor is not None:
        parts.insert(lead_at, ("raw", descriptor))

    # C12: keys for the new headings.
    old_headings = heading_lines(body)
    old_keys = heading_keys(old_headings)
    taken = {key for key in old_keys if key}
    rendered: list[str] = []
    new_lines: list[str] = []
    for kind, payload in parts:
        if kind == "raw":
            rendered.append(payload)
        elif kind == "block":
            rendered.append(render_block(*payload))
        else:
            slug = slugify(payload)
            line = "### " + payload
            if "sec-" + slug in taken:
                if "stat-" + slug in taken:
                    raise Queue("anchor-taken", "stat-" + slug)
                line += " {#stat-" + slug + "}"
            new_lines.append(line)
            rendered.append(line)
    new_body = "\n" + "\n\n".join(rendered) + "\n"
    if rest:
        new_body += "\n" + rest_text

    prove_monster(body, new_body, rest_text, descriptor, new_lines)
    return new_body


def prove_monster(body: str, new_body: str, rest_text: str, descriptor: str | None, new_lines: list[str]) -> None:
    if rest_text.strip("\n") and not new_body.endswith("\n\n" + rest_text):
        raise ProofFailed("the text after the statistics region changed")
    # Words: the old body with the descriptor moved, against the new body without `### Defense`.
    expected = words(body)
    if descriptor is not None:
        moved = words(descriptor)
        first = words("**Challenge rating:**")
        expected = move_run(expected, moved, first)
    actual = words(new_body, drop_line=new_lines[0])
    if expected != actual:
        at = next((i for i, (a, b) in enumerate(zip(expected, actual)) if a != b), min(len(expected), len(actual)))
        raise ProofFailed(f"words differ at {at}: {expected[at:at + 6]} / {actual[at:at + 6]}")
    # Headings: every old key survives, in order; the new ones are distinct additions.
    old_keys = heading_keys(heading_lines(body))
    lines = heading_lines(new_body)
    keys = heading_keys(lines)
    pending = list(new_lines)
    kept = []
    added = []
    for line, key in zip(lines, keys):
        if pending and line == pending[0]:
            pending.pop(0)
            added.append(key)
        else:
            kept.append(key)
    if pending or kept != old_keys:
        raise ProofFailed("a heading key moved")
    if len(set(added)) != len(added) or any(key is None or key in old_keys for key in added):
        raise ProofFailed("a new heading has no key of its own")


def move_run(sequence: list[str], run: list[str], before: list[str]) -> list[str]:
    """`sequence` with the first occurrence of `run` moved to just before the first `before`."""
    target = find_run(sequence, before, 0)
    start = find_run(sequence, run, target)
    if target < 0 or start < 0:
        raise ProofFailed("the descriptor line is not where the pass read it")
    return sequence[:target] + run + sequence[target:start] + sequence[start + len(run):]


def find_run(sequence: list[str], run: list[str], start: int) -> int:
    for index in range(max(start, 0), len(sequence) - len(run) + 1):
        if sequence[index:index + len(run)] == run:
            return index
    return -1


def print_254_rows(body: str) -> list[str]:
    """`label: value` for each cast-iron #254 print row, as a paragraph or as a stat block row."""
    found = []
    for label in PRINT_254_LABELS:
        pattern = r"^(?:\*\*" + label + r":\*\* ((?:.+\n?)+)|" + label + r": (.+)$)"
        for match in re.finditer(pattern, body, re.M):
            value = match.group(1) if match.group(1) is not None else match.group(2)
            found.append(f"{label}: {' '.join(value.split())}")
    return found


# ---- the NPC pass --------------------------------------------------------------------------------

NPC_SECTIONS = ("### Defense", "### Offense", "### Statistics", "### Ecology")
NPC_LABEL = re.compile(r"\*\*([^*]+)\*\*")
NPC_LEVEL = re.compile(r"_([^_]+)_-(.+)", re.S)
NPC_HEADER = re.compile(r"\*\*([^*]+)\*\* \(([^()]*)\)")
NPC_HEADER_PART = re.compile(r"(CL|concentration) (\S+)")
# The labels that print after a comma, not a semicolon: `**Fort** +3, **Ref** +4, **Will** +5`.
NPC_COMMA_LABELS = ("Ref", "Will", "Dex", "Con", "Int", "Wis", "Cha", "Reach")
NPC_LINKED_LABELS = {"[Spell-Like Abilities](ref/umr/spell-like-abilities)": "Spell-Like Abilities"}
NPC_CR = re.compile(r"\*\*Challenge rating:\*\* (\S.*)")


def npc_segments(chunk: list[str]) -> list[str]:
    """The lines of a paragraph that its hard breaks end, each as written (wraps kept)."""
    return "\n".join(chunk).split("\\\n")


def npc_label(raw: str) -> str:
    label = NPC_LINKED_LABELS.get(raw, raw)
    if re.search(r"[\\:\[\]_*^~{}<>|#]", label) or label != label.strip() or '"' in label:
        raise Queue("label-needs-escape", raw)
    return label


def npc_value(label: str, value: str) -> str:
    value = value.strip()
    if value.endswith("\\") or GUARDED.match(value):
        raise Queue("escaped-edge", label)
    return value


def npc_rows(segment: str) -> list[tuple[str, str]]:
    """The rows of one labelled line: `**A** x; **B** y` gives (A, x), (B, y)."""
    flat = join_wrapped(segment.split("\n"))
    found = list(NPC_LABEL.finditer(flat))
    rows = []
    for position, match in enumerate(found):
        label = npc_label(match.group(1))
        if position + 1 == len(found):
            rows.append((label, npc_value(label, flat[match.end():])))
            continue
        following = found[position + 1]
        value = flat[match.end():following.start()]
        separator = re.search(r"([;,])\s*$", value)
        if separator is None:
            raise Queue("label-without-separator", following.group(1))
        if separator.group(1) == "," and following.group(1) not in NPC_COMMA_LABELS:
            raise Queue("comma-before-label", following.group(1))
        rows.append((label, npc_value(label, value[: separator.start()])))
    return rows


def classify_npc(body: str) -> str:
    count = len(re.findall(r"^\*\*Challenge rating:\*\*", body, re.M))
    if count == 1:
        return "paragraphs"
    if count == 0 and re.search(r"^::: statblock\nChallenge rating:", body, re.M):
        return "already"
    raise Queue("challenge-rating-lines", str(count))


def convert_npc(body: str) -> str:
    """The converted body of an NPC. Raises Queue when a rule does not cover the file."""
    lines = body.split("\n")
    if any(line.startswith(":::") for line in lines):
        raise Queue("fence-in-body")
    parts: list[str] = []
    zone = "lead"
    seen: set[str] = set()
    block: list | None = None  # [title, rows]
    spell_rows = False  # the open block is a spell list that still takes level rows
    lead_state = "before"  # before | rating | done
    unlabelled: list[str] = []
    moved: str | None = None

    def close() -> None:
        nonlocal block, spell_rows
        if block is not None:
            if not block[1]:
                raise Queue("empty-spell-list", block[0] or "")
            parts.append(render_block(block[0], block[1]))
        block = None
        spell_rows = False

    def add(label: str, value: str) -> None:
        nonlocal block
        if block is None:
            block = [None, []]
        block[1].append((label, [value]))

    for chunk in chunks(lines):
        text = "\n".join(chunk)
        if HEADING.match(chunk[0]):
            close()
            if zone == "lead" and lead_state != "done":
                raise Queue("no-lead-paragraph")
            if chunk[0] in NPC_SECTIONS:
                if chunk[0] in seen:
                    raise Queue("section-twice", chunk[0][4:])
                seen.add(chunk[0])
                zone = "section"
            else:
                zone = "other"
            parts.append(text)
            continue
        if zone == "other":
            parts.append(text)
            continue
        if zone == "lead" and lead_state == "before":
            rating = NPC_CR.fullmatch(text)
            if rating:
                add("Challenge rating", npc_value("Challenge rating", rating.group(1)))
                lead_state = "rating"
            elif text.startswith(("**", "- ", ">", "|")):
                raise Queue("lead-shape", " ".join(text.split())[:40])
            else:
                parts.append(text)  # N2: the read-aloud line stays
            continue
        if zone == "lead" and lead_state == "done":
            raise Queue("extra-lead-paragraph", " ".join(text.split())[:40])
        if not text.startswith("**"):
            reason = "quote-in-section" if text.startswith(">") else "prose-in-section"
            raise Queue(reason, " ".join(text.split())[:40])
        segments = npc_segments(chunk)
        for position, segment in enumerate(segments):
            flat = join_wrapped(segment.split("\n"))
            if flat.startswith("**"):
                header = NPC_HEADER.fullmatch(flat)
                levels_follow = position + 1 < len(segments) and segments[position + 1].startswith("_")
                if levels_follow:
                    # N5: a spell list opens a titled block.
                    if header is None or zone == "lead":
                        raise Queue("spell-header", flat[:60])
                    close()
                    block = [npc_label(header.group(1)), []]
                    for piece in header.group(2).split("; "):
                        named = NPC_HEADER_PART.fullmatch(piece)
                        if named is None:
                            raise Queue("spell-header", flat[:60])
                        add(named.group(1), npc_value(named.group(1), named.group(2)))
                    if [label for label, _ in block[1]][:1] != ["CL"] or len(block[1]) > 2:
                        raise Queue("spell-header", flat[:60])
                    spell_rows = True
                    continue
                spell_rows = False
                for label, value in npc_rows(segment):
                    add(label, value)
                continue
            level = NPC_LEVEL.fullmatch(flat)
            if flat.startswith("_") and level:
                if not spell_rows:
                    raise Queue("spell-header", flat[:40])
                label = npc_label(level.group(1))
                add(label, npc_value(label, level.group(2)))
                continue
            contiguous = not unlabelled or segments[position - 1] is unlabelled[-1]
            if zone == "lead" and contiguous and flat and not flat.startswith(("_", "- ", ">")):
                unlabelled.append(segment)  # N3
                continue
            raise Queue("unlabelled-line", flat[:40])
        if zone == "lead":
            lead_state = "done"
            if unlabelled:
                if len(unlabelled) > 3 or unlabelled[-1].endswith("\\"):
                    raise Queue("lead-shape", "unlabelled lines")
                moved = "\\\n".join(unlabelled)
                parts.append(moved)
            close()
    close()
    if lead_state != "done" or "### Defense" not in seen or "### Statistics" not in seen:
        raise Queue("no-lead-or-defense")
    new_body = "\n" + "\n\n".join(parts) + "\n"
    prove_npc(body, new_body, moved)
    return new_body


def npc_proof_words(body: str) -> list[str]:
    """The words of an unconverted NPC body, with exactly the separators the NPC rules drop taken
    out of its statistics. Written apart from `convert_npc` so that it checks it.

    In the lead and in the Defense, Offense, Statistics and Ecology sections only:
    - a bold label loses the `;` or `,` before it and gains the colon of a row;
    - a spell list header `**Title** (CL 6th; concentration +9)` loses its parentheses and the `;`,
      and `CL` and `concentration` gain the colon of a row;
    - a spell level label `_3rd_-` loses its emphasis markers and its dash for the colon of a row;
    - the linked label `[Spell-Like Abilities](…)` loses its link.
    Nothing else is touched: every other character of every word must be found again.
    """
    out: list[str] = []
    zone = True
    for chunk in chunks(body.split("\n")):
        text = "\n".join(chunk)
        if HEADING.match(chunk[0]):
            zone = chunk[0] in NPC_SECTIONS
            out.extend(words(text))
            continue
        if not zone or not text.startswith("**"):
            out.extend(words(text))
            continue
        segments = text.split("\\\n")
        for position, segment in enumerate(segments):
            flat = " ".join(segment.split("\n"))
            for linked, plain in NPC_LINKED_LABELS.items():
                flat = flat.replace("**" + linked + "**", "**" + plain + "**")
            header = re.fullmatch(r"\*\*([^*]+)\*\* \(([^()]*)\)", flat)
            if header and position + 1 < len(segments) and segments[position + 1].startswith("_"):
                pieces = [re.sub(r"^(\S+) ", r"\1: ", piece) for piece in header.group(2).split("; ")]
                flat = header.group(1) + " " + " ".join(pieces)
            elif flat.startswith("_"):
                flat = re.sub(r"^_([^_]+)_-", r"\1: ", flat).replace("**", "")  # bold in a value stays
            else:
                flat = re.sub(r"[;,]?\s*\*\*([^*]+?):?\*\*", r" \1:", flat)
            out.extend(flat.split())
    return out


def prove_npc(body: str, new_body: str, moved: str | None) -> None:
    expected = npc_proof_words(body)
    if moved is not None:
        expected = move_run(expected, words(moved), ["Challenge", "rating:"])
    actual = words(new_body)
    if expected != actual:
        at = next((i for i, (a, b) in enumerate(zip(expected, actual)) if a != b), min(len(expected), len(actual)))
        raise ProofFailed(f"words differ at {at}: {expected[at:at + 6]} / {actual[at:at + 6]}")
    old = heading_lines(body)
    if heading_lines(new_body) != old:
        raise ProofFailed("a heading changed")


# ---- running -------------------------------------------------------------------------------------


def parse_only(value: str | None):
    """(letters, folders) or None."""
    if value is None:
        return None
    letters: set[str] = set()
    folders: set[str] = set()
    for token in value.split(","):
        token = token.strip().lower()
        if re.fullmatch(r"[a-z0-9]", token):
            letters.add(token)
        elif re.fullmatch(r"[a-z0-9]-[a-z0-9]", token) and token[0] <= token[2]:
            letters.update(chr(code) for code in range(ord(token[0]), ord(token[2]) + 1))
        elif token:
            folders.add(token)
    return letters, folders


def selected(path: Path, only) -> bool:
    if only is None:
        return True
    letters, folders = only
    if folders and path.parent.name not in folders:
        return False
    return not letters or path.name[0].lower() in letters


def pass_files(root: Path, name: str) -> list[Path]:
    out = []
    for folder in PASS_FOLDERS[name]:
        out.extend(sorted((root / "entries" / folder).glob("*.md")))
    return out


def plan_file(text: str, name: str = "creature") -> tuple[str, str, str]:
    """(status, detail, new text). Status: converted, already, skipped or a queue reason."""
    front, body = split_front(text)
    if not re.search(r'^kind = "creature"$', front, re.M):
        return "skipped", "", text
    try:
        classify, convert = (classify_npc, convert_npc) if name == "npc" else (classify_monster, convert_monster)
        if classify(body) == "already":
            return "already", "", text
        new_body = convert(body)
    except Queue as queued:
        return "queue:" + queued.reason, queued.detail, text
    new_text = front + new_body
    if split_front(new_text) != (front, new_body) or not new_text.startswith(front):
        raise ProofFailed("the front matter changed")
    return "converted", "", new_text


def write_atomic(path: Path, text: str) -> None:
    handle, temp = tempfile.mkstemp(dir=path.parent, prefix="." + path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="") as out:
            out.write(text)
        os.replace(temp, path)
    except BaseException:
        if os.path.exists(temp):
            os.unlink(temp)
        raise


def fix_state(root: Path, fix) -> tuple[str, str]:
    """(`pending` | `applied` | `unknown`, the text with the fix applied)."""
    rel, _, _, pairs = fix
    text = (root / rel).read_text(encoding="utf-8")
    if all(text.count(pair[0]) == 0 and sum(text.count(new) for new in pair[1:]) == 1 for pair in pairs):
        return "applied", text
    if all(text.count(pair[0]) == 1 for pair in pairs):
        for pair in pairs:
            text = text.replace(pair[0], pair[1])
        return "pending", text
    return "unknown", text


def review_rows(root: Path, passes: list[str]) -> list[str]:
    """The review TSV for the whole corpus: the same before and after a conversion."""
    rows = []
    for rel, citation, note, _ in PRINT_FIXES:
        kind = "creature" if "/monster/" in rel else "item"
        rows.append((rel, kind, "print-fix", f"{note} ({citation})"))
    for name in passes:
        for path in pass_files(root, name):
            rel = path.relative_to(root).as_posix()
            text = path.read_text(encoding="utf-8")
            status, detail, _ = plan_file(text, name)
            if status.startswith("queue:"):
                rows.append((rel, name, status[6:], detail))
            for row in print_254_rows(split_front(text)[1]):
                rows.append((rel, name, "print-254", row))
    rows.sort()
    return [TSV_HEADER] + ["\t".join(row) for row in rows]


def run(root: Path, mode: str, passes: list[str], only_value: str | None, out=sys.stdout) -> int:
    counts: collections.Counter = collections.Counter()
    changed = 0
    for fix in PRINT_FIXES:
        state, fixed = fix_state(root, fix)
        print(f"print fix {fix[0]}: {state}", file=out)
        if state == "unknown":
            print(f"error: {fix[0]} matches neither side of its print fix", file=sys.stderr)
            return 2
        if state == "pending":
            if mode == "write":
                write_atomic(root / fix[0], fixed)
            elif mode == "check":
                changed += 1

    scopes = [(name, only_value) for name in passes]
    if mode == "check" and only_value is None and passes == implemented_passes():
        scopes = list(APPLIED)
    only_shown = False
    for name, value in scopes:
        only = parse_only(value)
        for path in pass_files(root, name):
            if not selected(path, only):
                continue
            only_shown = True
            text = path.read_text(encoding="utf-8")
            status, detail, new_text = plan_file(text, name)
            counts[(name, status)] += 1
            if status == "converted":
                changed += 1
                if mode == "write":
                    write_atomic(path, new_text)
                    if plan_file(new_text, name)[0] != "already":
                        raise ProofFailed(f"{path}: the written file does not read as converted")
                elif mode == "check":
                    print(f"would change: {path.relative_to(root).as_posix()}", file=out)
    if any(PASS_FOLDERS[name] for name, _ in scopes) and not only_shown:
        print("no file matches the scope", file=out)

    verb = {"write": "converted", "check": "would convert", "survey": "would convert"}[mode]
    for (name, status), count in sorted(counts.items()):
        label = verb if status == "converted" else status.replace("queue:", "queued: ")
        print(f"{name}\t{label}\t{count}", file=out)

    tsv = "\n".join(review_rows(root, implemented_passes())) + "\n"
    tsv_path = root / REVIEW_TSV
    current = tsv_path.read_text(encoding="utf-8") if tsv_path.exists() else None
    if mode == "write":
        if current != tsv:
            write_atomic(tsv_path, tsv)
        print(f"review TSV: {tsv.count(chr(10)) - 1} rows", file=out)
        return 0
    stale = current != tsv
    print(f"review TSV: {tsv.count(chr(10)) - 1} rows, {'stale' if stale else 'current'}", file=out)
    if mode == "check":
        return 1 if changed or stale else 0
    return 0


def implemented_passes() -> list[str]:
    return [name for name in KNOWN_PASSES if PASS_FOLDERS.get(name)]


def main(argv: list[str]) -> int:
    args = list(argv)
    if "--self-test" in args:
        suite = unittest.TestSuite(
            unittest.defaultTestLoader.loadTestsFromTestCase(case) for case in (SelfTest, NpcSelfTest)
        )
        return 0 if unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful() else 1
    mode = "survey"
    passes = implemented_passes()
    only = None
    root = Path(__file__).resolve().parent.parent
    index = 0
    while index < len(args):
        arg = args[index]
        index += 1
        if arg in ("--write", "--check"):
            if mode != "survey":
                print("error: --write and --check exclude each other", file=sys.stderr)
                return 2
            mode = arg[2:]
        elif arg in ("--pass", "--only") or arg.startswith(("--pass=", "--only=")):
            if "=" in arg:
                arg, value = arg.split("=", 1)
            elif index < len(args):
                value = args[index]
                index += 1
            else:
                print(f"error: {arg} needs a value", file=sys.stderr)
                return 2
            if arg == "--only":
                only = value
                continue
            passes = [name.strip() for name in value.split(",") if name.strip()]
            for name in passes:
                if name not in KNOWN_PASSES:
                    print(f"error: unknown pass `{name}`", file=sys.stderr)
                    return 2
                if name not in PASS_FOLDERS:
                    print(f"error: the `{name}` pass is not in this version of the script; it arrives with its slice", file=sys.stderr)
                    return 2
        elif arg.startswith("--"):
            print(f"error: unknown option {arg}", file=sys.stderr)
            return 2
        else:
            root = Path(arg)
    if not (root / "entries").is_dir():
        print(f"error: {root} has no entries/ directory", file=sys.stderr)
        return 2
    try:
        return run(root, mode, passes, only)
    except ProofFailed as failure:
        print(f"error: proof failed, stopped: {failure}", file=sys.stderr)
        return 2


# ---- self-test -----------------------------------------------------------------------------------

SAMPLE = """
_A read-aloud line that is long._

**Challenge rating:** 1/2

**Aasimar [cleric](ref/class/cleric) 1**

**Type:** outsider

**othersubs:** Herald

**Armor class:** 15

**Touch:** 10

**Offense**

**Speed:** 30 ft.

**Melee:** heavy mace -1 (1d8-1) and a second attack that the writer
wrapped onto another line

**Spell-Like Abilities**

**Caster level:** 1

**Per day:**

- 1/day: daylight
- 3/day: a spell whose line is long enough that the writer wrapped it onto a
  second line

**Domains:** Good

###### D {#footnote-d}

Domain spell

**Statistics**

**Ability scores:** Str 8, Dex 10

### Tactics

**During Combat** It fights.

**Ecology**

**Treasure:**

### Description

Prose with **Bold:** words.
"""

EXPECTED = """
_A read-aloud line that is long._

**Aasimar [cleric](ref/class/cleric) 1**

::: statblock
Challenge rating: 1/2
Type: outsider
othersubs: Herald
:::

### Defense

::: statblock
Armor class: 15
Touch: 10
:::

### Offense

::: statblock
Speed: 30 ft.
Melee: heavy mace -1 (1d8-1) and a second attack that the writer wrapped onto another line
:::

::: statblock
title = "Spell-Like Abilities"
Caster level: 1
Per day: 1/day: daylight\\
3/day: a spell whose line is long enough that the writer wrapped it onto a second line
Domains: Good
:::

###### D {#footnote-d}

Domain spell

### Statistics

::: statblock
Ability scores: Str 8, Dex 10
:::

### Tactics

**During Combat** It fights.

### Ecology

::: statblock
Treasure:
:::

### Description

Prose with **Bold:** words.
"""

FRONT = '+++\nid = "ref/monster/x"\nkind = "creature"\n\n[fields]\nkind = "creature"\ncr = "1/2"\n+++\n'


class SelfTest(unittest.TestCase):
    def queued(self, body: str) -> str:
        with self.assertRaises(Queue) as caught:
            classify_monster(body)
            convert_monster(body)
        return caught.exception.reason

    def test_a_monster_converts_by_the_rules(self):
        self.assertEqual(convert_monster(SAMPLE), EXPECTED)

    def test_rows_joined_by_breaks_split_into_rows(self):
        joined = SAMPLE.replace("**Type:** outsider\n\n", "**Type:** outsider\\\n")
        self.assertNotEqual(joined, SAMPLE)
        self.assertEqual(convert_monster(joined), EXPECTED)
        three = SAMPLE.replace("**Armor class:** 15\n\n", "**Armor class:** 15\\\n").replace(
            "**Type:** outsider\n\n**othersubs:** Herald\n\n", "**Type:** outsider\\\n**othersubs:** Herald\\\n"
        )
        self.assertEqual(convert_monster(three), EXPECTED)

    def test_a_body_that_ends_with_the_statistics_converts(self):
        body = SAMPLE[: SAMPLE.index("### Description")]
        self.assertEqual(convert_monster(body), EXPECTED[: EXPECTED.index("\n### Description")])

    def test_a_converted_file_reads_as_already_and_the_front_matter_is_kept(self):
        status, _, text = plan_file(FRONT + SAMPLE)
        self.assertEqual(status, "converted")
        self.assertEqual(text, FRONT + EXPECTED)
        self.assertEqual(plan_file(text), ("already", "", text))

    def test_a_taken_key_gives_the_new_heading_an_explicit_anchor(self):
        body = SAMPLE + "\n### Ecology\n\nIt lives.\n\n### Ecology\n\nAgain.\n"
        new = convert_monster(body)
        self.assertIn("\n### Ecology {#stat-ecology}\n", new)
        self.assertIn("\n### Defense\n", new)
        keys = heading_keys(heading_lines(new))
        self.assertEqual(keys[-2:], ["sec-ecology", "sec-ecology-2"])
        self.assertEqual(self.queued(body + "\n### Other {#stat-ecology}\n\nText.\n"), "anchor-taken")

    def test_heading_keys_follow_the_schema_rules(self):
        lines = ["## A b", "## A b", "### A b {#sec-a-b-2}", "## [Link](ref/x/y) *it*", "## !!!", "## Entry {#entry-related}"]
        self.assertEqual(
            heading_keys(lines), ["sec-a-b", "sec-a-b-3", "sec-a-b-2", "sec-link-it", None, "entry-related-2"]
        )

    def test_what_the_rules_do_not_cover_is_queued(self):
        cases = [
            # C15 refused: a segment that is not a row, two labels with no break, a label inside a value.
            ("multi-label-paragraph", SAMPLE.replace("**Type:** outsider\n", "**Type:** outsider\\\n_Kinetic blast_ +5\n")),
            ("multi-label-paragraph", SAMPLE.replace("**Type:** outsider\n\n", "**Type:** outsider\n")),
            ("multi-label-paragraph", SAMPLE.replace("**Type:** outsider", "**Type:** outsider **Subtype:** Native")),
            ("multi-label-paragraph", SAMPLE.replace("**Type:** outsider\n\n", "**Type:** outsider **Subtype:** x\\\n")),
            ("multi-label-paragraph", SAMPLE.replace("**Type:**", "**[Type](ref/rule/type):**")),
            ("label-needs-escape", SAMPLE.replace("**Type:** outsider\n\n**othersubs:**", "**Type:** outsider\\\n**other: subs:**")),
            ("escaped-edge", SAMPLE.replace("**Type:** outsider\n", "**Type:** outsider\\\n")),
            ("escaped-edge", SAMPLE.replace("**Type:** outsider\n\n**othersubs:** Herald", "**Type:** outsider\\\n**othersubs:** \\- Herald")),
            ("list-without-empty-row", SAMPLE.replace("**Caster level:** 1\n\n", "**Caster level:** 1\\\n")),
            ("sources-line-in-region", SAMPLE.replace("**Type:** outsider\n", "**Sources:** Bestiary pg 174\\\n**Type:** outsider\n")),
            ("note-before-rows", SAMPLE.replace("**Challenge rating:** 1/2", "###### D {#footnote-d}\n\nDomain spell\n\n**Challenge rating:** 1/2", 1)),
            ("note-without-text", SAMPLE.replace("Domain spell\n\n", "")),
            ("bold-paragraph-in-section", SAMPLE.replace("**Speed:** 30 ft.", "**Swarm form**\n\n**Speed:** 30 ft.")),
            ("two-descriptors", SAMPLE.replace("**Type:** outsider", "**Second line**\n\n**Type:** outsider")),
            ("section-order", SAMPLE.replace("**Statistics**", "**Ecology**")),
            ("empty-section", SAMPLE.replace("**Ability scores:** Str 8, Dex 10\n\n", "")),
            ("list-without-empty-row", SAMPLE.replace("**Per day:**\n", "**Per day:** x\n")),
            ("unflat-list", SAMPLE.replace("- 1/day: daylight", "- 1/day: daylight\n  - nested")),
            ("prose-in-region", SAMPLE.replace("**Touch:** 10", "**Touch:** 10\n\nA sentence.")),
            ("challenge-rating-lines", SAMPLE.replace("**Challenge rating:** 1/2\n\n", "")),
            ("section-after-heading", SAMPLE + "\n**Challenge rating:** 3\n"),
            ("section-after-heading", SAMPLE + "\n**Offense**\n\n**Speed:** 5 ft.\n"),
            ("armor-class-lines", SAMPLE.replace("**Touch:** 10", "**Armor class:** 10")),
            ("fence-in-region", SAMPLE.replace("**Touch:** 10", "::: statblock\nTouch: 10\n:::")),
            ("label-needs-escape", SAMPLE.replace("**Touch:**", "**Touch: x:**")),
        ]
        for reason, body in cases:
            with self.subTest(reason=reason):
                self.assertEqual(self.queued(body), reason)

    def test_the_word_proof_fails_on_a_lost_or_added_word(self):
        new = convert_monster(SAMPLE)
        lines = ["### Defense", "### Offense", "### Statistics", "### Ecology"]
        descriptor = "**Aasimar [cleric](ref/class/cleric) 1**"
        rest = "### Description\n\nProse with **Bold:** words.\n"
        prove_monster(SAMPLE, new, rest, descriptor, lines)
        for broken in (new.replace("Touch: 10", "Touch: 11"), new.replace("Good", "Good, Evil"), new.replace("Speed: 30 ft.\n", "")):
            with self.assertRaises(ProofFailed):
                prove_monster(SAMPLE, broken, rest, descriptor, lines)
        with self.assertRaises(ProofFailed):
            prove_monster(SAMPLE, new.replace("with **Bold:**", "with"), rest, descriptor, lines)
        with self.assertRaises(ProofFailed):
            prove_monster(SAMPLE, new.replace("### Tactics", "### Tactics {#sec-defense}"), rest, descriptor, lines)

    def test_only_reads_letter_ranges_and_folders(self):
        self.assertEqual(parse_only("a-c,x"), ({"a", "b", "c", "x"}, set()))
        self.assertEqual(parse_only("eq-misc,magic-ring"), (set(), {"eq-misc", "magic-ring"}))
        self.assertTrue(selected(Path("entries/monster/dragon.md"), parse_only("a-d")))
        self.assertFalse(selected(Path("entries/monster/owlbear.md"), parse_only("a-d")))
        self.assertFalse(selected(Path("entries/npc/acolyte.md"), parse_only("monster,a-d")))

    def test_print_254_rows_are_found_in_both_forms(self):
        self.assertEqual(print_254_rows(SAMPLE), ["othersubs: Herald"])
        self.assertEqual(print_254_rows(EXPECTED), ["othersubs: Herald"])

    def test_a_run_writes_checks_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "entries/monster").mkdir(parents=True)
            (root / "entries/eq-weaponenh").mkdir(parents=True)
            (root / "scripts").mkdir()
            for rel, _, _, pairs in PRINT_FIXES:
                (root / rel).write_text(FRONT.replace("creature", "item") + "".join(pair[0] for pair in pairs), encoding="utf-8")
            (root / "entries/monster/aasimar.md").write_text(FRONT + SAMPLE, encoding="utf-8")
            (root / "entries/monster/zombie.md").write_text(FRONT + SAMPLE.replace("**Touch:** 10", "Prose."), encoding="utf-8")
            sink = open(os.devnull, "w")
            self.addCleanup(sink.close)
            self.assertEqual(run(root, "check", ["creature"], "a-d", sink), 1)
            self.assertEqual(run(root, "write", ["creature"], "a-d", sink), 0)
            self.assertEqual((root / "entries/monster/aasimar.md").read_text(encoding="utf-8"), FRONT + EXPECTED)
            tsv = (root / REVIEW_TSV).read_text(encoding="utf-8")
            self.assertIn("entries/monster/zombie.md\tcreature\tprose-in-region\tProse.\n", tsv)
            self.assertIn("entries/monster/aasimar.md\tcreature\tprint-254\tothersubs: Herald\n", tsv)
            self.assertIn("\tprint-fix\t", tsv)
            self.assertEqual(run(root, "check", ["creature"], "a-d", sink), 0)
            before = {path: path.read_bytes() for path in root.rglob("*.md")}
            self.assertEqual(run(root, "write", ["creature"], None, sink), 0)
            self.assertEqual(before, {path: path.read_bytes() for path in root.rglob("*.md")})
            self.assertEqual(sorted(path.name for path in root.rglob("*.tmp")), [])
            for fix in PRINT_FIXES:
                self.assertEqual(fix_state(root, fix)[0], "applied")
                path = root / fix[0]
                for pair in fix[3]:
                    for later in pair[2:]:
                        path.write_text(path.read_text(encoding="utf-8").replace(pair[1], later), encoding="utf-8")
                self.assertEqual(fix_state(root, fix)[0], "applied")



NPC_SAMPLE = r"""
_A read-aloud line._

**Challenge rating:** 5

**XP** 1,600\
Human [evoker](ref/class/wizard) 6 with a class line that is long enough for the writer to wrap it
onto a second line\
N Medium humanoid (human)\
**Init** +6; **Senses** [low-light vision](ref/rule/low-light-vision); Perception +6

### Defense

**AC** 16, touch 12, flat-footed 14 (+4 mage armor, +2 Dex)\
**hp** 33 (6d6+12)\
**Fort** +3, **Ref** +4, **Will** +5; +2 vs. enchantments\
**Defensive Abilities** evasion; **DR** 10/magic

### Offense

**Speed** 30 ft.\
**Space** 5 ft., **Reach** 5 ft. (10 ft. with lance)\
**[Spell-Like Abilities](ref/umr/spell-like-abilities)** (CL 6th; concentration +9)\
_6/day_-dehydrating touch\
**Wizard Spells Prepared** (CL 6th; concentration +9)\
_3rd_-[dispel magic](ref/spell/dispel-magic), fly, **[haste](ref/spell/haste)**,
[fireball](ref/spell/fireball) (2) (DC 17)\
_0 (at will)_-light^D^\
**D** Domain spell; **Domains** Fire

### Tactics

**Before Combat** The mage casts _mage armor_.\
**Base Statistics** Without it, **AC** 12, touch 12.

### Statistics

**Str** 9, **Dex** 14, **Con** 12, **Int** 17, **Wis** 10, **Cha** 13\
**Base Atk** +3; **CMB** +2; **CMD** 17

### Description

Prose with **Bold** words; and _3rd_-level slots.
"""

NPC_EXPECTED = r"""
_A read-aloud line._

Human [evoker](ref/class/wizard) 6 with a class line that is long enough for the writer to wrap it
onto a second line\
N Medium humanoid (human)

::: statblock
Challenge rating: 5
XP: 1,600
Init: +6
Senses: [low-light vision](ref/rule/low-light-vision); Perception +6
:::

### Defense

::: statblock
AC: 16, touch 12, flat-footed 14 (+4 mage armor, +2 Dex)
hp: 33 (6d6+12)
Fort: +3
Ref: +4
Will: +5; +2 vs. enchantments
Defensive Abilities: evasion
DR: 10/magic
:::

### Offense

::: statblock
Speed: 30 ft.
Space: 5 ft.
Reach: 5 ft. (10 ft. with lance)
:::

::: statblock
title = "Spell-Like Abilities"
CL: 6th
concentration: +9
6/day: dehydrating touch
:::

::: statblock
title = "Wizard Spells Prepared"
CL: 6th
concentration: +9
3rd: [dispel magic](ref/spell/dispel-magic), fly, **[haste](ref/spell/haste)**, [fireball](ref/spell/fireball) (2) (DC 17)
0 (at will): light^D^
D: Domain spell
Domains: Fire
:::

### Tactics

**Before Combat** The mage casts _mage armor_.\
**Base Statistics** Without it, **AC** 12, touch 12.

### Statistics

::: statblock
Str: 9
Dex: 14
Con: 12
Int: 17
Wis: 10
Cha: 13
Base Atk: +3
CMB: +2
CMD: 17
:::

### Description

Prose with **Bold** words; and _3rd_-level slots.
"""


class NpcSelfTest(unittest.TestCase):
    def queued(self, body: str) -> str:
        with self.assertRaises(Queue) as caught:
            classify_npc(body)
            convert_npc(body)
        return caught.exception.reason

    def test_an_npc_converts_by_the_rules(self):
        self.assertEqual(convert_npc(NPC_SAMPLE), NPC_EXPECTED)

    def test_a_converted_npc_reads_as_already(self):
        status, _, text = plan_file(FRONT + NPC_SAMPLE, "npc")
        self.assertEqual((status, text), ("converted", FRONT + NPC_EXPECTED))
        self.assertEqual(plan_file(text, "npc"), ("already", "", text))

    def test_what_the_npc_rules_do_not_cover_is_queued(self):
        cases = [
            ("unlabelled-line", NPC_SAMPLE.replace("Perception +6\n", "Perception +6\\\nAura courage (10 ft.)\n", 1)),
            ("unlabelled-line", NPC_SAMPLE.replace("**hp** 33", "hp 33")),
            ("unlabelled-line", NPC_SAMPLE.replace("**D** Domain spell", "D Domain spell")),
            ("spell-header", NPC_SAMPLE.replace("concentration +9)\\\n_3rd_", "concentration +9; arcane spell failure 10%)\\\n_3rd_")),
            ("spell-header", NPC_SAMPLE.replace("(CL 6th; concentration +9)\\\n_3rd_", "(CL 6th, concentration +9)\\\n_3rd_")),
            ("spell-header", NPC_SAMPLE.replace("(CL 6th; concentration +9)\\\n_3rd_", "(CL 6th; conc. +9)\\\n_3rd_")),
            ("spell-header", NPC_SAMPLE.replace("**Speed** 30 ft.\\\n", "**Speed** 30 ft.\\\n_3rd_-fly\\\n")),
            ("spell-header", NPC_SAMPLE.replace("**D** Domain spell; **Domains** Fire", "**Domains** Fire\\\n_1st_-bless")),
            ("unlabelled-line", NPC_SAMPLE.replace("_0 (at will)_-light^D^", "_0 (at will)_ light^D^")),
            ("label-without-separator", NPC_SAMPLE.replace("**Speed** 30 ft.\\\n", "**Speed** 30 ft. **Melee** bite +1\\\n")),
            ("comma-before-label", NPC_SAMPLE.replace("evasion; **DR**", "evasion, **DR**")),
            ("label-needs-escape", NPC_SAMPLE.replace("**Speed**", "**[Speed](ref/rule/speed)**")),
            ("label-needs-escape", NPC_SAMPLE.replace("_6/day_-", "_6/day: x_-")),
            ("section-twice", NPC_SAMPLE + "\n### Defense\n\n**AC** 10\n"),
            ("quote-in-section", NPC_SAMPLE.replace("**Str** 9", "> **Str** 9")),
            ("prose-in-section", NPC_SAMPLE.replace("**Str** 9", "Str 9")),
            ("extra-lead-paragraph", NPC_SAMPLE.replace("### Defense\n\n", "**Aura** fear\n\n### Defense\n\n", 1)),
            ("lead-shape", NPC_SAMPLE.replace("_A read-aloud line._", "**Name**")),
            ("challenge-rating-lines", NPC_SAMPLE.replace("**Challenge rating:** 5\n\n", "")),
            ("no-lead-or-defense", NPC_SAMPLE.replace("### Defense", "### Defenses")),
            ("escaped-edge", NPC_SAMPLE.replace("**hp** 33", "**hp** \\- 33")),
            ("fence-in-body", NPC_SAMPLE + "\n::: statblock\nA: b\n:::\n"),
        ]
        for reason, body in cases:
            with self.subTest(reason=reason, body=body[-60:]):
                self.assertNotEqual(body, NPC_SAMPLE)
                self.assertEqual(self.queued(body), reason)

    def test_the_npc_word_proof_allows_only_the_dropped_separators(self):
        moved = NPC_EXPECTED.split("\n\n")[1]
        prove_npc(NPC_SAMPLE, NPC_EXPECTED, moved)
        broken = [
            NPC_EXPECTED.replace("fly, ", ""),  # a spell name lost
            NPC_EXPECTED.replace("(2) (DC 17)", "(DC 17)"),  # a count lost
            NPC_EXPECTED.replace("CL: 6th\nconcentration: +9\n3rd", "CL: 6th\nconcentration: +8\n3rd"),  # a number changed
            NPC_EXPECTED.replace("6/day: dehydrating", "5/day: dehydrating"),
            NPC_EXPECTED.replace("Will: +5; +2 vs. enchantments", "Will: +5"),
            NPC_EXPECTED.replace("Fort: +3", "Fort: +3,"),  # a separator kept inside a value
            NPC_EXPECTED.replace("Senses: [low-light vision](ref/rule/low-light-vision); Perception", "Senses: low-light vision; Perception"),
            NPC_EXPECTED.replace("3rd_-level slots", "3rd: level slots"),  # prose is not covered by the allowance
            NPC_EXPECTED.replace("**Base Statistics** Without it, **AC** 12", "Base Statistics: Without it AC: 12"),
            NPC_EXPECTED.replace("N Medium humanoid (human)", "N Medium humanoid"),
            NPC_EXPECTED.replace("### Tactics", "### Tactic"),
        ]
        for text in broken:
            with self.subTest(text=text[:0] + str(broken.index(text))):
                self.assertNotEqual(text, NPC_EXPECTED)
                with self.assertRaises(ProofFailed):
                    prove_npc(NPC_SAMPLE, text, moved)
        with self.assertRaises(ProofFailed):  # the unlabelled lines left where they were
            prove_npc(NPC_SAMPLE, NPC_EXPECTED, None)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
