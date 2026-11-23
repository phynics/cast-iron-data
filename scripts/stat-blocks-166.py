#!/usr/bin/env python3
"""Write creature, NPC and item statistics as stat blocks (cast-iron-data #166, with cast-iron #254).

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

    --pass sources[,creature,npc,item,siege,shield]
                                 which passes run (default: every pass this version implements;
                                 `sources` runs first, so one `--write` moves the citation and then
                                 converts what it unblocked)
    --pass fixes                 no conversion: `--write` applies the print fixes and writes the TSV
    --only a-d                   entry files whose name starts with a letter of the range(s)
    --only eq-misc,magic-ring    or the entries of the named folders (both kinds can be mixed)

Passes. `sources` (the raw `**Sources:**` lines of the other three), `creature` (the folder
`entries/monster`), `npc` (`entries/npc`) and `item` (every entry with `kind = "item"` outside
`entries/carried`) are implemented. A survey (no `--write`, no `--check`) of the `sources` pass also
prints the counts of every raw citation line, by zone.

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
    stat block with that title, as the monster spell blocks have. Its first rows are the caster
    level and the concentration (N8): the parentheses and the `;` go. Each level line `_3rd_-fly, haste` becomes
    the row `3rd: fly, haste`: the emphasis markers and the dash go. The rows after the level lines
    (`Bloodline`, `Domains`, `Opposition Schools`) stay in that block, as in monsters (C8). A
    header with any other part (`arcane spell failure 10%`, `conc. +5`) is queued.
N6  The linked label `[Spell-Like Abilities](ref/umr/spell-like-abilities)` becomes the plain title
    `Spell-Like Abilities`; the link is dropped. Any other label with markup is queued.
N7  Queue. Anything else queues the whole file, unchanged: an unlabelled line outside N3 (an
    `Aura …` line after `Init`), two labels with no `;` between them, a `,` before another label,
    a level line outside a spell list, prose, a quote or a list in a statistics section, a
    section printed twice, a value with an edge escape.
N8  Spell block labels (owner ruling of 2026-11-23). The two header rows take the labels of the
    monster spell blocks: `CL 6th` becomes `Caster level: 6th` and `concentration +9` becomes
    `Concentration: +9`. These are the only two labels the pass renames; the values are kept.
    An NPC that was converted before this rule (rows `CL:` and `concentration:` under a block
    title) is relabelled in place: `--write` reports it as `relabelled`, after a line-by-line
    proof that nothing else changed.

The NPC word proof allows exactly the separators N4 to N6 drop, and only inside the statistics:
the `;` or `,` before a label, the parentheses and `;` of a spell list header, the `_ _-` of a
level label, the one link of N6, and the two renamed labels of N8. A row adds the colon after its label. Every other word,
spell name, count and number must be found again, in order; the unlabelled lead lines are checked
as moved. `npc_proof_words` does this reading on its own, apart from the converter.

Rules for the item pass (rulings of 2026-11-23)
-----------------------------------------------

An item prints its statistics as run-on lines:

    **Cost** 15 gp **Weight** 4 lbs.\
    **Damage** 1d6 (small), 1d8 (medium); **Critical** 19-20/×2; **Range** -; **Type** S\
    **[Weapon Group](ref/ability/weapon-groups)** Blades, Heavy

I1  Scope. An entry with `kind = "item"` outside `entries/carried`. An entry that already has a
    stat block reads as `already`. An entry with no lead and no Construction paragraph to convert
    is left alone (`no-statistics` in the counts). It is not in the review TSV for that; it is
    listed there only when I9 or I8 lists it (a bow whose statistics all stand under variant
    headings is listed as `variant-paragraphs`).
I2  Lead. The lead is the first statistics paragraph of the body: a paragraph that opens with a
    bold label and a value, with no `###` heading before it. It becomes one untitled stat block
    where it stands. Prose and a `##` title before it stay.
I3  Rows. A line `**Label** value` becomes the row `Label: value`; a line with several labels
    becomes one row per label, in order, and the `;` before a label is dropped. Labels and values
    are not edited. A label printed twice in one block queues the file.
I4  `**Cost** 15 gp **Weight** 4 lbs.` is the one pair that splits without a `;`. Any other label
    that follows a value without a `;` queues the file.
I5  Weapon Group. The linked label `[Weapon Group](ref/ability/weapon-groups)` becomes the plain
    label, and each group of the value becomes a link to the section of that group in the weapon
    groups entry: `Weapon Group: [Blades, Heavy](ref/ability/weapon-groups#sec-heavy-blades);
    [Close](ref/ability/weapon-groups#sec-close)`. The value is split at `; ` and every part must
    be in the closed list `WEAPON_GROUPS` (`Blades, Heavy` is one group); anything else (`Varies`)
    queues the file. The headings of those sections get their key as an explicit anchor.
    Any other linked label (`Hardness`, `Special Purpose`, `Spell-Like Abilities`, a set piece)
    queues the file.
I6  Sentences. The block ends before the first line of the lead whose value reads as sentences
    (`**Preparation** A bone reed must be pressed and dried. This process…`). That line and the
    lines after it stay a paragraph, unchanged, directly below the block. The sentence value must
    be the first of its line, or the file is queued. Each entry whose block ends this way is
    listed in the TSV as `block-ended-at-sentences`, with the first kept label.
I7  A paragraph that opens with a `**Label:**` (`**Benefit:**`, `**Note:**`, a set piece link)
    is prose and stays. A colon label inside the lead queues the file, as does a `**Sources:**`
    line inside the lead.
I8  Construction. The paragraph directly under the first `### Construction` heading, when it is
    a statistics paragraph and comes after the lead, becomes an untitled stat block under the
    heading, which stays. Its rows are the printed ones: `Requirements` and `Cost` in most
    entries, `Requirements` and `Price` in the rings and others. The sentence rule I6 does not
    apply to it. A Construction paragraph with a line that has no label (the technological items
    print `Craft Technological Item, …` so) stays prose, byte for byte: the lead still converts,
    no label is invented, and the entry is listed in the TSV as `construction-unlabelled`.
    When the lead is a stat block already, a Construction paragraph that reads as statistics
    converts alone: rule S moves a `**Sources:**` line out of it, and that line was what kept it
    prose.
I9  Variants. Every other statistics paragraph stays as it is: a variant of the item (its name
    alone on the first line, or under a `###` heading of its own), a second set of statistics, a
    recipe. A file may be converted and keep such paragraphs. Each entry that has them is listed
    in the TSV as `variant-paragraphs`, with the first label of each, before and after the
    conversion, as the queue of the later review slice.
I10 Queue. A file the rules do not cover is queued whole, unchanged: a line of the lead without
    a label, a label after a value without a `;` (I4), a linked label (I5),
    an unknown weapon group, a label that would need escaping, a value with an edge escape.

The item word proof reads the body the same way before and after (`item_words`): a statistics
paragraph and a stat block row are brought to one form, in which a bold label has lost the `;`
before it and gained the colon of a row. For the Weapon Group row it requires one link per
group and nothing else, checks that each link names the section of its own group, and then
removes only the link markup, so the value text is proven unchanged apart from the links. It
also proves where I6 cut: no row of the lead block holds a sentence value, and a kept tail opens
with one. Besides the words, every paragraph the pass did not convert
must be found again byte for byte, in order, and no heading may change.

Rules for the sources pass (owner ruling 1 of 2026-11-23)
---------------------------------------------------------

A raw `**Sources:**` line in the body of a creature or an item is a printed citation. It moves to
`[[sources]]` rows (book and page) and leaves the body. It never becomes a statistics row and is
never deleted without its row:

    **Sources:** Pathfinder RPG Bestiary pg 174\\         [[sources]]
    **Experience points:** 600                    publication = "bestiary"
                                                  page = "174"

S1  Scope. The creatures of `entries/monster` and `entries/npc` and the items outside
    `entries/carried`: the entries the three passes below read. The citation lines of other
    kinds (faith, skill, domain, rule, a blockquote, a list) are not in scope. A line is a
    `**Sources:**` label at the start of a line outside a stat block. Its zone is one of
    `statistics` (the statistics region of a creature, C1; the lead paragraph of an item that
    has no stat block yet), `construction` (the paragraph directly under the first
    `### Construction` of an item) or `variant` (every other line). Since owner ruling 1 of
    2026-11-23 the rule applies to every zone (`SOURCES_ZONES`, with the variant paragraphs
    included). A file with a line the rule cannot move is queued whole, as before, with the
    reason (`sources-page-conflict`, `sources-unparsed`, ...). `raw-sources-line` stays in the TSV
    code for a zone the rule is set not to apply to; it lists none at present.
S2  Line. `Book pg N[, Book pg N]` with each page `N` or `N-N`. Each book name is a title of
    `publications.toml` read exactly (`\\#` is `#`) or one of the two import spellings in
    `SOURCE_ALIASES` (`Pathfinder RPG Bestiary`, `PRPG Core Rulebook`). A line that wraps joins
    with one space. A name that does not map queues the file (`sources-unmapped-book`), as does
    any other form (`sources-unparsed`: no page, `pg. 159, 163`, a second page after a comma, markup).
S3  Body. The line leaves, with its hard break. A paragraph that held only the line goes with
    one adjoining blank line. When the line was the last of its paragraph, the line before it
    loses its break. A label that does not open a line, or a line that ends the paragraph with a
    break, queues the file (`sources-shape`).
S4  Rows. A book cited in the zones gets one row, `publication` and `page`, after the rows the
    entry has (and before any `[[expanded_in]]`), in the order the lines print. The same book
    on the same page twice gives one row. The book must be in the entry's `source_ids`, as
    `corpus-check` requires, or the file queues (`sources-book-not-in-source-ids`).
S5  Existing rows. A row the entry already has for the book is kept. Every page the line
    prints for that book must be covered by the `page` of one of the rows the entry has for the
    book: equal to it, or inside its range or its comma list (`14` is covered by `13-14`, or by a
    second row `14`). A page no row covers, a row without a page, or two pages for one new book
    queues the file (`sources-page-conflict`, with the pages): the page of a row is never edited
    by this rule, and it never adds a row for a book that already has one. A print fix adds such
    a row first, by hand.

The proof of rule S, run on every file before it is written (`prove_sources`, read apart from the
converter): the front matter differs from the old one by one inserted run of the added rows and
by nothing else, and its data differs only in `sources`, which grew by exactly those rows; the
body loses only lines that open with the label (and the blank line or the one break of S3), and
every other line is found again byte for byte, in order; reading the removed lines again gives
citations that each have a row in the new front matter with the printed page; no row is added that
no citation prints. A second run finds nothing to move (`--write` checks it).

Rules for the variant passes (owner ruling 2 of 2026-11-23, one pass for each variant kind)
-------------------------------------------------------------------------------------------

A variant sub-item of an entry (a size, a second set of statistics, a recipe) becomes a stat block
of its own. A titled block per variant, `title = "<printed variant name>"`; an untitled block under
an existing heading; a linked label moves onto the value; a variant row that only restates the
entry's own `Price` or `Slot` stays prose, so the drift check reads the entry's own value. Poison
affliction tails stay prose. A pass opens with one slice and stops for review.

`siege` (`entries/eq-siegeengine`, 20 entries): the size variants that print without a colon.

V1  Scope. A paragraph whose first line is `**Large**`, `**Huge**`, `**Gargantuan**` or
    `**Colossal**` alone with a break, followed by statistics lines. The sizes that print with a
    colon (`**Light:**`, 14 entries) and every other paragraph stay as they are.
V2  Block. The paragraph becomes one stat block where it stands, with the size as its `title` and
    one row for each label of the lines below, as the item rules I3 and I4 read them. The block of
    the entry's own lead (`Large:`), when there is one, is not touched.
V3  Queue. A paragraph with a line without a label, a sentence value, a label twice, a
    `**Sources:**` line, or a fence in the body queues the whole file.
    The proof (`prove_siege`) reads the words of the body before and after, with the title read as
    the bold size name, and finds every other paragraph again byte for byte, in order.

The other variant kinds share one driver (`convert_variants`) and one proof (`prove_variants`):

W1  A kind says which paragraphs it converts and with what title (`plan_*`); the driver makes one
    stat block for each, where the paragraph stands. Rows are read as in the item rules I3 to I5
    (`vrows`); a label with one link keeps its text and the link moves onto the value (`link_labels`);
    a `,` before the labels a kind lists (`Wis`, `Cha`) goes like a `;`.
W2  Queue (whole file, unchanged): a line without a label, a label twice, a sentence value, a
    `**Sources:**` line, a label that needs escaping, blank lines the reader would not write back,
    and a block that carries `Price`, `Weight`, `Slot`, `Aura` or `CL` while no block before it has
    that label (`no-lead-row`): the drift check reads the first row of each, so a variant must
    never become the first one.
W3  The proof, read apart from the converter: the new body is the old body with exactly the swapped
    paragraphs; for each swap the words are the same (links reduced to their text, a bold label read
    as `Label:`, the title read as a bold name) and the multiset of link targets is the same; a
    Weapon Group row is one link per group, each to its own section; no heading changes. A title
    that is the label of the paragraph above (`printed_before`) must be that label.

`shield` (`eq-armor`, `eq-armorenh`, 13 entries): the statistics of a shield bash. Twelve shields
print them as a paragraph directly under `**Shield Bash Attacks:**`, with no heading of their own;
the block is titled `Shield Bash Attacks`, the printed name of that paragraph, and the paragraph
above must open with it. The shield spikes print two paragraphs, `Light shield` and `Heavy shield`:
each becomes a block with its printed name as the title.

`recipe` (every item folder, 73 entries): the alchemical recipe paragraph, `**[Spontaneous
Alchemy](ref/rule/spontaneous-alchemy) Recipe** (6 quicksilver + 10 realgar)/distillation; **Craft
DC** 20` and the line of `Time`, `Tools` and `Type`. It is not a variant with a printed name, so
the block is untitled and stands where the paragraph stands. The label is plain and the link moves
onto the value (the recipe), as for the weapon groups; one entry (`poison-diffuser`) prints the
label without the link. The poison recipes print `**Craft** DC 13`,
with `DC` outside the bold; the row is kept as printed (`Craft: DC 13`).

`tearaway` (`eq-misc`, 37 entries): the outfits that print a `Tear-away clothing` variant, its name
alone on the first line and then `Price +5 gp; Weight -` and `Category`. The block takes the
printed name as its title. Its `Price` and `Weight` rows follow the entry's own block, which
the drift check reads first.

`intelligent` (every item folder, 65 entries): the statistics of an intelligent item, the paragraph
`**Alignment** …; **Ego** …`, `Senses`, `Int, Wis, Cha`, `Communication` and the lines after them, directly under
`### Statistics`. One untitled block under that heading, which stays. The `,` before `Wis` and
`Cha` goes (three rows, as the NPC `Str`…`Cha` line); a linked label (`Special Purpose`) is plain
and the link moves onto the value. A line without a label (the lists of a `Powers` or `Spell-Like
Abilities` line) queues the file, which stays prose for a hand review.

`ioun` (every item folder, 51 entries, all `magic-ioun`): the Construction of an ioun stone prints
under `#### Construction`, one level below the `### Construction` that item rule I8 reads. The
paragraph `**Requirements** …; **Cost** …` directly under it becomes an untitled block under that
heading, which stays. The `Flawed Ioun Stone` and `Cracked Ioun Stone` paragraphs (`**Price** 800 gp`
and a sentence) restate the entry's own `Price` and stay prose.

`spellbook` (`eq-spellbook`, 41 entries): the paragraph that opens with `**Opposition**`,
`**Protection**` or `**Value**` (any of them, in that order) under the `### Level N …` heading
of a spellbook. One untitled block where it stands. No other label is read, and the value of a
`Protection` may be a sentence (the books print their wards in prose), which the sentence rule
would otherwise refuse (`sentences`).

`figurine` (`magic-wondrous`, 23 entries, the figurines of wondrous power): after the list of the
Ivory Goats the book prints `**CL** 11th; Craft Wondrous Item, _animate objects_.` One untitled
block with the one row `CL`, whose value is kept as printed with its requirements tail; the label
is not renamed. The entry's own block (`CL: varies`) comes first, so the drift check keeps reading it.

`cost` (`eq-weapon`, `magic-fleshcraft`, 22 entries expected): a paragraph that opens with
`**Cost**`. The bows print `**Cost** 225 gp (+1), 325 gp (+2), …` under `### Composite Bows`: one
untitled block where the paragraph stands. The `Composite longbow +N` headings of the composite
bows print `**Cost** 200gp` and, at +0, the whole weapon: a file whose first block with `Cost` or
`Weight` would be one of those queues (`no-lead-row`), so a variant never becomes the first row. The
fleshcraft items print `**Cost** 1,000 gp` and then a line without a label (`Fleshwarper, Craft
(alchemy) 8 ranks; Heal DC 18; **Elixir Cost** 250 gp`) under `### Creation Requirements`: the
labelled lines become the block, and the line without a label stays a paragraph below it, unchanged,
as for the technological Construction (ruling 3). No label is invented.

Proofs of the conversion passes, run on every file before it is written (a failure aborts the run and writes nothing more):

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
import difflib
import os
import re
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

REVIEW_TSV = "scripts/stat-blocks-review-166.tsv"
TSV_HEADER = "path\tpass\treason\tdetail"
FRONT_MATTER_END = "\n+++\n"

# The slices already written to the corpus: (pass, --only value or None for the whole pass).
# `--check` with no scope arguments checks exactly these.
APPLIED: list[tuple[str, str | None]] = [
    ("sources", None),  # every zone, the variant paragraphs included
    ("creature", None),
    ("npc", None),
    ("item", None),
    ("siege", None),
]  # the variant kinds join it below

PASS_FOLDERS = {
    "sources": ("monster", "npc", "*"),
    "creature": ("monster",),
    "npc": ("npc",),
    "item": ("*",),
    "siege": ("eq-siegeengine",),
    "fixes": (),
}
PASS_KIND = {"creature": "creature", "npc": "creature", "item": "item", "siege": "item"}
NOT_ITEM_FOLDERS = ("carried", "monster", "npc")
KNOWN_PASSES = ("sources", "creature", "npc", "item", "siege", "fixes")  # the variant kinds join it below

# Rule S: the zones of a body whose raw `**Sources:**` lines the pass handles now, and the label.
SOURCES_LABEL = "**Sources:**"
ALL_ZONES = ("statistics", "construction", "variant")
SOURCES_ZONES = ALL_ZONES
SOURCE_PAGE = re.compile(r"\d+(?:-\d+)?")
# Printed names that are not a title in `publications.toml`: the two import spellings, as
# `scripts/sources-field.py` reviewed them.
SOURCE_ALIASES = {"Pathfinder RPG Bestiary": "bestiary", "PRPG Core Rulebook": "core-rulebook"}

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
    (
        "entries/magic-piercing/body-piercings-minor.md",
        "Champions of Corruption p. 28",
        "aura `faint transmutation` and caster level `3rd`; the import ran them together",
        (
            ('aura = "faint transmutation CL 3rd"\n', 'aura = "faint transmutation"\ncaster_level = "3rd"\n'),
            ("\nAura: faint transmutation CL 3rd\n", "\nAura: faint transmutation\nCL: 3rd\n"),
        ),
    ),
    (
        "entries/magic-wondrous/slashing-cloak.md",
        "Ultimate Equipment p. 268",
        "Construction: the cost printed once; the import left `; Cost 10,000 gp` twice",
        (
            (
                "[blade barrier](ref/spell/blade-barrier); **Cost** 10,000 gp; **Cost** 10,000 gp\n",
                "[blade barrier](ref/spell/blade-barrier); **Cost** 10,000 gp\n",
                # The same line once the item pass has made it rows.
                "\nRequirements: [Craft Wondrous Item](ref/feat/craft-wondrous-item), [blade barrier](ref/spell/blade-barrier)\n"
                "Cost: 10,000 gp\n:::\n",
            ),
        ),
    ),
    (
        "entries/magic-armor/planar-invasion-shield.md",
        "Ultimate Equipment p. 349",
        "Construction: the intended item `absorbing shield` as a link, without the emphasis that held the `;`",
        (
            (
                "**Requirements** _absorbing shield;_ **Cost** -\n",
                "**Requirements** [absorbing shield](ref/magic-armor/absorbing-shield); **Cost** -\n",
                "\nRequirements: [absorbing shield](ref/magic-armor/absorbing-shield)\nCost: -\n:::\n",
            ),
        ),
    ),
    (
        "entries/npc/winter-witch-cold-sister.md",
        "Irrisen, Land of Eternal Winter p. 62",
        "Spell-Like Abilities concentration: `+7`; the import left `+7s`",
        (("\nConcentration: +7s\n", "\nConcentration: +7\n"),),
    ),
    (
        "entries/magic-wondrous/cube-of-force.md",
        "Classic Treasures Revisited p. 11",
        "row `11`, the base item's own text; `13` and `14` stay as rows for the variant paragraphs of the body",
        ((
            "page = \"13\"\n\n[fields]",
            "page = \"11\"\n[[sources]]\npublication = \"classic-treasures-revisited\"\npage = \"13\"\n[[sources]]\npublication = \"classic-treasures-revisited\"\npage = \"14\"\n\n[fields]",
        ),),
    ),
    (
        "entries/magic-wondrous/cube-of-varied-force-walls.md",
        "Classic Treasures Revisited p. 13",
        "row `13` kept (its own text); row `14` added for the Construction paragraph of the body",
        ((
            "page = \"13\"\n\n[fields]",
            "page = \"13\"\n[[sources]]\npublication = \"classic-treasures-revisited\"\npage = \"14\"\n\n[fields]",
        ),),
    ),
    (
        "entries/magic-wondrous/discriminating-cube.md",
        "Classic Treasures Revisited p. 13",
        "row `13` kept (its own text); row `14` added for the Construction paragraph of the body",
        ((
            "page = \"13\"\n\n[fields]",
            "page = \"13\"\n[[sources]]\npublication = \"classic-treasures-revisited\"\npage = \"14\"\n\n[fields]",
        ),),
    ),
    (
        "entries/magic-wondrous/independent-cube-of-force.md",
        "Classic Treasures Revisited p. 13",
        "row `13` kept (its own text); row `14` added for the Construction paragraph of the body",
        ((
            "page = \"13\"\n\n[fields]",
            "page = \"13\"\n[[sources]]\npublication = \"classic-treasures-revisited\"\npage = \"14\"\n\n[fields]",
        ),),
    ),
    (
        "entries/magic-wondrous/rechargeable-cube-of-force.md",
        "Classic Treasures Revisited pp. 13-14",
        "row `13-14`: the item starts at the foot of p. 13 and its Construction is the first line of p. 14",
        ((
            "page = \"13\"\n\n[fields]",
            "page = \"13-14\"\n\n[fields]",
        ),),
    ),
    (
        "entries/magic-wondrous/remote-activation-cube.md",
        "Classic Treasures Revisited p. 14",
        "row `14` kept (its own text, the foot of the Rechargeable block to the Remote Activation block of p. 14); row `13` added for the variant paragraphs of the body",
        ((
            "page = \"14\"\n\n[fields]",
            "page = \"14\"\n[[sources]]\npublication = \"classic-treasures-revisited\"\npage = \"13\"\n\n[fields]",
        ),),
    ),
)


# The shadow piercings (Champions of Corruption pp. 28-29): the import ran the caster level into
# `aura` (`faint transmutation CL 3rd`). Print gives `AURA ...` and `CL n` apart, so `aura` loses
# the CL, `caster_level` holds it and a `CL:` row follows `Aura:`, as for `body-piercings-minor`.
# (slug, aura as printed, caster level, page the row holds now, printed page).
PIERCINGS = (
    ("body", "faint transmutation", "3rd", "28", "28"),
    ("chest", "faint transmutation", "3rd", "28", "29"),
    ("eye", "faint transmutation", "5th", "28", "29"),
    ("head", "faint transmutation", "5th", "28", "29"),
    (
        "suspension",
        "faint transmutation (minor and major), moderate transmutation (greater)",
        "7th",
        "29",
        "29",
    ),
)
EYE_PRICE = "6,000 gp (Minor), 18,000 gp (Major), 32,000 gp (Greater)"


def piercing_fixes() -> tuple:
    fixes = []
    for part, aura, level, old_page, page in PIERCINGS:
        for grade in ("minor", "major", "greater"):
            slug = f"{part}-piercings-{grade}"
            if slug == "body-piercings-minor":
                continue  # fixed by the first slice
            pairs = [
                (f'aura = "{aura} CL {level}"\n', f'aura = "{aura}"\ncaster_level = "{level}"\n'),
                (f"\nAura: {aura} CL {level}\n", f"\nAura: {aura}\nCL: {level}\n"),
            ]
            note = f"aura `{aura}`, caster level `{level}`; the import ran them together"
            if old_page != page:
                pairs.append((f'page = "{old_page}"\n\n[fields]', f'page = "{page}"\n\n[fields]'))
                note += f"; page row `{page}`: the entry prints on p. {page}, not p. {old_page}"
            if part == "eye":
                pairs.append(
                    (f"\nSlot: eye; Price {EYE_PRICE}\n", f"\nSlot: eye\nPrice: {EYE_PRICE}\n")
                )
                pairs.append(('category = "Piercings"\nslot = "eyes"\n', f'category = "Piercings"\nprice = "{EYE_PRICE}"\nslot = "eyes"\n'))
                note += "; the `Price` the import left in the `Slot` row, and the `price` field it lacked"
            fixes.append((f"entries/magic-piercing/{slug}.md", f"Champions of Corruption p. {page}", note, tuple(pairs)))
    return tuple(fixes)


PRINT_FIXES = PRINT_FIXES + piercing_fixes()


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


def words(text: str, drop_line: str | None = None, keep_bold: bool = False) -> list[str]:
    """The words of a body with the markup this pass adds or removes taken out. The creature pass
    turns bold labels into rows, so it drops `**`; the NPC proof reads labels itself and keeps it."""
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
        out.extend((line if keep_bold else line.replace("**", "")).split())
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
# N8: the header parts take the labels of the monster spell blocks.
NPC_HEADER_LABELS = {"CL": "Caster level", "concentration": "Concentration"}
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
        return "old-labels" if relabel_npc(body) != body else "already"
    raise Queue("challenge-rating-lines", str(count))


OLD_HEADER_ROWS = (("CL: ", "Caster level: "), ("concentration: ", "Concentration: "))


def relabel_npc(body: str) -> str:
    """N8 for an NPC that was converted with the labels `CL` and `concentration`: the two rows
    that open a titled block take the monster labels. Nothing else is read or changed."""
    lines = body.split("\n")
    for index, line in enumerate(lines):
        if not (line.startswith('title = "') and index and lines[index - 1] == "::: statblock"):
            continue
        for offset, (old, new) in enumerate(OLD_HEADER_ROWS, start=1):
            if index + offset < len(lines) and lines[index + offset].startswith(old):
                lines[index + offset] = new + lines[index + offset][len(old):]
            else:
                break
    new_body = "\n".join(lines)
    prove_relabel(body, new_body)
    return new_body


def prove_relabel(body: str, new_body: str) -> None:
    """Line by line: only a `CL: x` or `concentration: x` row changed, only into its new label with
    the same value, and only as the first or second row under a block title."""
    old_lines, new_lines = body.split("\n"), new_body.split("\n")
    if len(old_lines) != len(new_lines):
        raise ProofFailed("the relabel changed the number of lines")
    for index, (old_line, new_line) in enumerate(zip(old_lines, new_lines)):
        if old_line == new_line:
            continue
        allowed = False
        for offset, (old, new) in enumerate(OLD_HEADER_ROWS, start=1):
            under_title = index >= offset + 1 and old_lines[index - offset].startswith('title = "')
            under_title = under_title and old_lines[index - offset - 1] == "::: statblock"
            if under_title and old_line.startswith(old) and new_line == new + old_line[len(old):]:
                allowed = True
        if not allowed:
            raise ProofFailed(f"the relabel changed line {index + 1}: {old_line!r}")


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
                        add(NPC_HEADER_LABELS[named.group(1)], npc_value(named.group(1), named.group(2)))
                    if [label for label, _ in block[1]][:1] != ["Caster level"] or len(block[1]) > 2:
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
      and exactly `CL` becomes `Caster level:` and `concentration` becomes `Concentration:` (N8);
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
            out.extend(words(text, keep_bold=True))
            continue
        if not zone or not text.startswith("**"):
            out.extend(words(text, keep_bold=True))
            continue
        segments = text.split("\\\n")
        for position, segment in enumerate(segments):
            flat = " ".join(segment.split("\n"))
            for linked, plain in NPC_LINKED_LABELS.items():
                flat = flat.replace("**" + linked + "**", "**" + plain + "**")
            header = re.fullmatch(r"\*\*([^*]+)\*\* \(([^()]*)\)", flat)
            if header and position + 1 < len(segments) and segments[position + 1].startswith("_"):
                pieces = [
                    re.sub(r"^(CL|concentration) ", lambda name: NPC_HEADER_LABELS[name.group(1)] + ": ", piece)
                    for piece in header.group(2).split("; ")
                ]
                flat = header.group(1) + " " + " ".join(pieces)
            elif flat.startswith("_"):
                flat = re.sub(r"^_([^_]+)_-", r"\1: ", flat)  # bold in a value stays, and is compared
            else:
                flat = re.sub(r"[;,]?\s*\*\*([^*]+?):?\*\*", r" \1:", flat)
            out.extend(flat.split())
    return out


def prove_npc(body: str, new_body: str, moved: str | None) -> None:
    expected = npc_proof_words(body)
    if moved is not None:
        expected = move_run(expected, words(moved, keep_bold=True), ["Challenge", "rating:"])
    actual = words(new_body, keep_bold=True)
    if expected != actual:
        at = next((i for i, (a, b) in enumerate(zip(expected, actual)) if a != b), min(len(expected), len(actual)))
        raise ProofFailed(f"words differ at {at}: {expected[at:at + 6]} / {actual[at:at + 6]}")
    old = heading_lines(body)
    if heading_lines(new_body) != old:
        raise ProofFailed("a heading changed")


# ---- the item pass -------------------------------------------------------------------------------

WEAPON_GROUPS_ENTRY = "ref/ability/weapon-groups"
WEAPON_GROUP_LABEL = "[Weapon Group](" + WEAPON_GROUPS_ENTRY + ")"
# The closed list: the group as a weapon prints it, and the heading key of its section in the
# weapon groups entry (`### Heavy Blades` there).
WEAPON_GROUPS = {
    "Axes": "sec-axes",
    "Blades, Heavy": "sec-heavy-blades",
    "Blades, Light": "sec-light-blades",
    "Bows": "sec-bows",
    "Close": "sec-close",
    "Crossbows": "sec-crossbows",
    "Double": "sec-double",
    "Firearms": "sec-firearms",
    "Flails": "sec-flails",
    "Hammers": "sec-hammers",
    "Monk": "sec-monk",
    "Natural": "sec-natural",
    "Polearms": "sec-polearms",
    "Siege Engines": "sec-siege-engines",
    "Spears": "sec-spears",
    "Thrown": "sec-thrown",
    "Tribal": "sec-tribal",
}
# I5 links to these sections, and a linked heading carries its key as an explicit anchor
# (docs/corpus-format.md in the app). `--write` adds the anchors; the keys do not change.
WEAPON_GROUP_HEADINGS = {
    "sec-heavy-blades": "Heavy Blades",
    "sec-light-blades": "Light Blades",
}
ANCHOR_EDITS = (
    (
        "entries/ability/weapon-groups.md",
        None,
        "explicit anchors on the weapon group headings",
        tuple(
            (
                f"\n### {WEAPON_GROUP_HEADINGS.get(key, group)}\n",
                f"\n### {WEAPON_GROUP_HEADINGS.get(key, group)} {{#{key}}}\n",
            )
            for group, key in WEAPON_GROUPS.items()
        ),
    ),
)
CONSTRUCTION_HEADING = "### Construction"
ITEM_STAT_START = re.compile(r"\*\*(?!\*)(?:\[[^\]]+\]\([^)]+\))?[^*:\[\]]*\*\* ?\S")
ITEM_LABEL = re.compile(r"\*\*((?:\[[^\]]+\]\([^)]+\))?[^*]*)\*\*")
# I6: a value that reads as sentences. A lowercase word of three letters or more that ends a
# sentence, with another sentence after it or at the end of a value of eight words or more.
UNIT_WORDS = "lbs|lb|ft|oz|gp|sp|cp|pp|min|max|rd|hrs|sec"
SENTENCE_INSIDE = re.compile(r"\b(?!(?:" + UNIT_WORDS + r")\b)[a-z]{3,}[.!?] [A-Z]")
SENTENCE_END = re.compile(r"\b(?!(?:" + UNIT_WORDS + r")\b)[a-z]{3,}[.!?]$")


def is_sentences(value: str) -> bool:
    return bool(SENTENCE_INSIDE.search(value)) or (bool(SENTENCE_END.search(value)) and len(value.split()) >= 8)


def is_stat_paragraph(chunk: list[str]) -> bool:
    """A paragraph that opens with a bold label and a value: `**Price** 15 gp; **Weight** 4 lbs.`.
    A `**Label:**` paragraph and a bold line alone (a variant's name) are not."""
    return bool(ITEM_STAT_START.match(chunk[0])) and not chunk[0].startswith("**Sources:**")


def item_layout(body: str) -> tuple[list[list[str]], int | None, int | None]:
    """(chunks, index of the lead paragraph, index of the Construction paragraph).

    I2: the lead is the first statistics paragraph of the body, when no `###` heading comes
    before it. I8: the Construction paragraph is the paragraph directly under the first
    `### Construction` heading, when it is a statistics paragraph and comes after the lead."""
    cs = chunks(body.split("\n"))
    lead = None
    for index, chunk in enumerate(cs):
        if chunk[0].startswith("### "):
            break
        if is_stat_paragraph(chunk):
            lead = index
            break
    construction = construction_index(cs)
    if construction is not None and lead is not None and construction < lead:
        construction = None
    return cs, lead, construction


def construction_index(cs: list[list[str]]) -> int | None:
    """The statistics paragraph directly under the first `### Construction` heading, if any."""
    for index, chunk in enumerate(cs):
        if chunk[0] == CONSTRUCTION_HEADING:
            return index + 1 if index + 1 < len(cs) and is_stat_paragraph(cs[index + 1]) else None
    return None


def construction_unlabelled(cs: list[list[str]]) -> bool:
    """I8: the Construction paragraph has a line without a label (the technological items print
    `Craft Technological Item, …` so). It stays prose."""
    index = construction_index(cs)
    if index is None:
        return False
    try:
        for segment in "\n".join(cs[index]).split("\\\n"):
            item_rows(segment, True)
    except Queue as queued:
        return queued.reason == "unlabelled-line"
    return False


def weapon_group_value(value: str) -> str:
    """I5: every group of the value linked to its section; the text between the links unchanged."""
    groups = value.split("; ")
    if not value or any(group not in WEAPON_GROUPS for group in groups):
        raise Queue("weapon-group", value[:40])
    return "; ".join(f"[{group}]({WEAPON_GROUPS_ENTRY}#{WEAPON_GROUPS[group]})" for group in groups)


def item_rows(segment: str, construction: bool) -> list[tuple[str, str]]:
    """The rows of one line of a statistics paragraph."""
    flat = join_wrapped(segment.split("\n"))
    found = list(ITEM_LABEL.finditer(flat))
    if not found or found[0].start() != 0:
        raise Queue("unlabelled-line", flat[:40])
    rows = []
    for position, match in enumerate(found):
        raw = match.group(1)
        end = found[position + 1].start() if position + 1 < len(found) else len(flat)
        value = flat[match.end():end]
        if position + 1 < len(found):
            separator = re.search(r";\s*$", value)
            if separator:
                value = value[: separator.start()]
            elif not (raw == "Cost" and found[position + 1].group(1) == "Weight"):
                raise Queue("label-without-separator", found[position + 1].group(1)[:40])  # I4
        value = value.strip()
        if raw == WEAPON_GROUP_LABEL and not construction:
            rows.append(("Weapon Group", weapon_group_value(value)))
            continue
        if "](" in raw:
            raise Queue("linked-label", raw[:60])
        if raw.endswith(":"):
            raise Queue("colon-label", raw)
        label = npc_label(raw)
        if value.endswith("\\") or GUARDED.match(value):
            raise Queue("escaped-edge", label)
        rows.append((label, value))
    return rows


def classify_item(body: str) -> str:
    if re.search(r"^::: statblock$", body, re.M):
        # I8: a converted lead with a Construction paragraph that reads as statistics (a citation
        # line used to keep it prose) still converts that paragraph.
        cs = chunks(body.split("\n"))
        if construction_index(cs) is not None and not construction_unlabelled(cs):
            return "paragraphs"
        return "already"
    if re.search(r"^:::", body, re.M):
        raise Queue("fence-in-body")
    return "paragraphs"


def convert_item(body: str) -> str:
    """The converted body of an item, or the body unchanged when it has no statistics to convert.
    Raises Queue when a rule does not cover the file."""
    cs, lead, construction = item_layout(body)
    if construction is not None and construction_unlabelled(cs):
        construction = None  # I8: it stays prose; the lead still converts
    if lead is None and construction is None:
        return body
    out: list[str] = []
    for index, chunk in enumerate(cs):
        if index not in (lead, construction):
            out.append("\n".join(chunk))
            continue
        rows: list[tuple[str, list[str]]] = []
        segments = "\n".join(chunk).split("\\\n")
        tail_from = len(segments)
        for position, segment in enumerate(segments):
            if segment.startswith("**Sources:**"):
                raise Queue("sources-line-in-lead")
            found = item_rows(segment, index == construction)
            if index == lead and any(is_sentences(value) for _, value in found):
                # I6: the block ends before a line whose value is sentences.
                if not is_sentences(found[0][1]):
                    raise Queue("sentences-mid-line", found[0][0])
                tail_from = position
                break
            rows.extend((label, [value]) for label, value in found)
        if not rows:
            raise Queue("prose-lead", " ".join(segments[0].split())[:40])
        labels = [label for label, _ in rows]
        if len(set(labels)) != len(labels):
            raise Queue("label-twice", next(label for label in labels if labels.count(label) > 1))
        out.append(render_block(None, rows))
        if tail_from < len(segments):
            out.append("\\\n".join(segments[tail_from:]))
    new_body = "\n" + "\n\n".join(out) + "\n"
    prove_item(body, new_body)
    return new_body


def item_words(text: str) -> list[str]:
    """The words of an item body, read the same way before and after the pass.

    A statistics paragraph and a stat block row are brought to one form: a bold label loses the
    `;` before it and gains the colon of a row. The Weapon Group label loses its link (I5), and
    in a `Weapon Group:` row each link to a section of the weapon groups entry is reduced to its
    text, after a check that the section is the one of that group. Nothing else is touched, so a
    paragraph the pass left alone reads the same on both sides."""
    out: list[str] = []
    cs = chunks(text.split("\n"))
    for chunk in cs:
        if chunk[0] == "::: statblock":
            for line in chunk[1:-1]:
                if line.startswith("Weapon Group: "):
                    def unlink(match: re.Match) -> str:
                        if WEAPON_GROUPS.get(match.group(1)) != match.group(2):
                            raise ProofFailed("a weapon group links to another section: " + match.group(0))
                        return match.group(1)

                    link = r"\[([^\]]+)\]\(" + re.escape(WEAPON_GROUPS_ENTRY) + r"#([^)]+)\)"
                    # One link per group: the value is links joined by `; ` and nothing else.
                    if not re.fullmatch(f"{link}(?:; {link})*", line[len("Weapon Group: "):]):
                        raise ProofFailed("a weapon group row is not one link per group: " + line)
                    line = re.sub(link, unlink, line)
                out.extend(line.split())
            continue
        if not is_stat_paragraph(chunk):
            out.extend(words("\n".join(chunk), keep_bold=True))
            continue
        for segment in "\n".join(chunk).split("\\\n"):
            flat = " ".join(segment.split("\n")).replace("**" + WEAPON_GROUP_LABEL + "**", "**Weapon Group**")
            out.extend(re.sub(r";?\s*\*\*((?:\[[^\]]+\]\([^)]+\))?[^*]*?):?\*\*", r" \1:", flat).split())
    return out


def prove_item(body: str, new_body: str) -> None:
    expected, actual = item_words(body), item_words(new_body)
    if expected != actual:
        at = next((i for i, (a, b) in enumerate(zip(expected, actual)) if a != b), min(len(expected), len(actual)))
        raise ProofFailed(f"words differ at {at}: {expected[at:at + 6]} / {actual[at:at + 6]}")
    # Every paragraph the pass did not convert is there byte for byte, in order.
    cs, lead, construction = item_layout(body)
    if construction is not None and construction_unlabelled(cs):
        construction = None
    new_cs = chunks(new_body.split("\n"))
    if lead is not None:
        # I6: the lead block holds no sentence value, and a kept tail starts with one.
        block = new_cs[lead]
        if block[0] != "::: statblock" or block[-1] != ":::":
            raise ProofFailed("the lead is not a stat block")
        for row in block[1:-1]:
            if is_sentences(row.partition(":")[2].strip()):
                raise ProofFailed("a sentence value is inside the lead block: " + row[:60])
        if len(new_cs) == len(cs) + 1:
            tail = item_first_value(new_cs[lead + 1])
            if tail is None or not is_sentences(tail[1]):
                raise ProofFailed("the block was cut before a line that is not sentences")
        elif len(new_cs) != len(cs):
            raise ProofFailed("the number of paragraphs changed")
    kept = ["\n".join(chunk) for index, chunk in enumerate(cs) if index not in (lead, construction)]
    position = 0
    for chunk in chunks(new_body.split("\n")):
        if position < len(kept) and "\n".join(chunk) == kept[position]:
            position += 1
    if position != len(kept):
        raise ProofFailed("a paragraph outside the statistics changed: " + kept[position][:60])
    if heading_lines(new_body) != heading_lines(body):
        raise ProofFailed("a heading changed")


def item_first_value(chunk: list[str]) -> tuple[str, str] | None:
    """(first label, its value) of a statistics paragraph, or None."""
    if not is_stat_paragraph(chunk):
        return None
    flat = join_wrapped("\n".join(chunk).split("\\\n")[0].split("\n"))
    first = ITEM_LABEL.match(flat)
    following = ITEM_LABEL.search(flat, first.end())
    value = flat[first.end(): following.start() if following else len(flat)]
    return first.group(1), value.strip().rstrip(";").strip()


def item_sentence_cut(body: str) -> str | None:
    """I6: the first kept label when the lead block ends at a sentence line, read the same way
    before and after the conversion: the lines of the lead from the first sentence value on, or
    the statistics paragraph directly below the lead that opens with a sentence value."""
    cs = chunks(body.split("\n"))
    if "::: statblock" in body:
        lead = next((i for i, chunk in enumerate(cs) if chunk[0] == "::: statblock"), None)
        if lead is None or (lead and cs[lead - 1][0] == CONSTRUCTION_HEADING):
            return None
    else:
        lead = item_layout(body)[1]
        if lead is None:
            return None
        for segment in "\n".join(cs[lead]).split("\\\n")[1:]:
            first = item_first_value([segment])
            if first and is_sentences(first[1]):
                return first[0]
    if lead + 1 < len(cs):
        first = item_first_value(cs[lead + 1])
        if first and is_sentences(first[1]):
            return first[0]
    return None


def item_leftovers(body: str) -> list[str]:
    """I9: the first label of each statistics paragraph the pass leaves as a paragraph (a variant
    of the item, a recipe), before or after the conversion. Sentence lines (I6) are not counted."""
    cs, lead, construction = item_layout(body)
    converted = "::: statblock" in body
    unlabelled = construction_index(cs) if construction_unlabelled(cs) else None
    found = []
    for index, chunk in enumerate(cs):
        if (not converted and index in (lead, construction)) or index == unlabelled:
            continue
        name = None
        if is_stat_paragraph(chunk):
            first = ITEM_LABEL.match(join_wrapped(chunk))
            flat = join_wrapped("\n".join(chunk).split("\\\n")[0].split("\n"))
            following = ITEM_LABEL.search(flat, first.end())
            value = flat[first.end(): following.start() if following else len(flat)]
            if not is_sentences(value.strip().rstrip(";")):
                name = first.group(1)
        elif re.fullmatch(r"\*\*[^*:]+\*\*\\", chunk[0]) and len(chunk) > 1:
            name = chunk[0][2:-3]  # a variant: its name alone on the first line
        if name:
            found.append(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", name))
    return found


# ---- the siege size variants (variant kind 1 of the owner ruling 2 of 2026-11-23) -------------------

SIEGE_SIZES = ("Large", "Huge", "Gargantuan", "Colossal")
SIEGE_TITLE = re.compile(r"\*\*(" + "|".join(SIEGE_SIZES) + r")\*\*")


def siege_variants(cs: list[list[str]]) -> list[int]:
    """V1: the paragraphs whose first line is a size alone in bold, with a break (`**Huge**\\`)."""
    return [
        index
        for index, chunk in enumerate(cs)
        if len(chunk) > 1 and chunk[0].endswith("\\") and SIEGE_TITLE.fullmatch(chunk[0][:-1])
    ]


def classify_siege(body: str) -> str:
    if re.search(r"^:::(?! statblock$)(?!$)", body, re.M):
        raise Queue("fence-in-body")
    return "paragraphs" if siege_variants(chunks(body.split("\n"))) else "already"


def convert_siege(body: str) -> str:
    """V1 to V3: each size paragraph becomes a stat block titled with the size, where it stands.
    Raises Queue when a paragraph does not read as rows."""
    cs = chunks(body.split("\n"))
    variants = set(siege_variants(cs))
    out: list[str] = []
    for index, chunk in enumerate(cs):
        if index not in variants:
            out.append("\n".join(chunk))
            continue
        segments = "\n".join(chunk).split("\\\n")
        title = SIEGE_TITLE.fullmatch(segments[0]).group(1)
        rows: list[tuple[str, list[str]]] = []
        for segment in segments[1:]:
            if segment.startswith("**Sources:**"):
                raise Queue("sources-line-in-variant")
            found = item_rows(segment, False)
            if any(is_sentences(value) for _, value in found):
                raise Queue("sentences-in-variant", title)
            rows.extend((label, [value]) for label, value in found)
        labels = [label for label, _ in rows]
        if not rows or len(set(labels)) != len(labels):
            raise Queue("label-twice" if rows else "prose-variant", title)
        out.append(render_block(title, rows))
    new_body = "\n" + "\n\n".join(out) + "\n"
    prove_siege(body, new_body)
    return new_body


def siege_words(text: str) -> list[str]:
    """`item_words`, with the title line of a stat block read as the bold size name of a variant."""
    return item_words(re.sub(r'^title = "([^"]+)"$', r"\1:", text, flags=re.M)) if "::: statblock" in text else item_words(text)


def prove_siege(body: str, new_body: str) -> None:
    """The words are the same (the size becomes a title), every other paragraph is found again byte
    for byte and in order, no heading changes, and each converted paragraph is one titled block."""
    cs, new_cs = chunks(body.split("\n")), chunks(new_body.split("\n"))
    variants = siege_variants(cs)
    if len(cs) != len(new_cs):
        raise ProofFailed("the number of paragraphs changed")
    for index, (old, new) in enumerate(zip(cs, new_cs)):
        if index in variants:
            size = SIEGE_TITLE.fullmatch(old[0][:-1]).group(1)
            if new[0] != "::: statblock" or new[1] != f'title = "{size}"' or new[-1] != ":::":
                raise ProofFailed("a size paragraph is not a stat block with its size as title: " + size)
        elif old != new:
            raise ProofFailed("a paragraph outside the variants changed: " + old[0][:60])
    expected, actual = siege_words(body), siege_words(new_body)
    if expected != actual:
        at = next((i for i, (a, b) in enumerate(zip(expected, actual)) if a != b), min(len(expected), len(actual)))
        raise ProofFailed(f"words differ at {at}: {expected[at:at + 6]} / {actual[at:at + 6]}")
    if heading_lines(new_body) != heading_lines(body):
        raise ProofFailed("a heading changed")


# ---- the variant passes, shared part (owner ruling 2 of 2026-11-23) ---------------------------------

DRIFT_LABELS = ("Price", "Weight", "Slot", "Aura", "CL")  # the labels `drift.rs` reads from the first block that has them
LINK_MARKUP = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SECTION_HEADING = re.compile(r"#{1,6} ")


def vrows(segment: str, commas: tuple[str, ...] = (), link_labels: bool = False) -> list[tuple[str, str]]:
    """The rows of one line of a variant paragraph (item rules I3 to I5, plus two cases the
    variant kinds need: a `,` before the labels in `commas`, and with `link_labels` a label with
    one link in it, whose link moves onto the value)."""
    flat = join_wrapped(segment.split("\n"))
    found = list(ITEM_LABEL.finditer(flat))
    if not found or found[0].start() != 0:
        raise Queue("unlabelled-line", flat[:40])
    rows = []
    for position, match in enumerate(found):
        raw = match.group(1)
        following = found[position + 1].group(1) if position + 1 < len(found) else None
        end = found[position + 1].start() if following is not None else len(flat)
        value = flat[match.end():end]
        if following is not None:
            if re.search(r";\s*$", value):
                value = value[: re.search(r";\s*$", value).start()]
            elif following in commas and re.search(r",\s*$", value):
                value = value[: re.search(r",\s*$", value).start()]
            elif not (raw == "Cost" and following == "Weight"):
                raise Queue("label-without-separator", following[:40])
        value = value.strip()
        if raw == WEAPON_GROUP_LABEL:
            rows.append(("Weapon Group", weapon_group_value(value)))
            continue
        if "](" in raw:
            links = LINK_MARKUP.findall(raw)
            if not link_labels or len(links) != 1 or not value or "[" in value or "](" in value:
                raise Queue("linked-label", raw[:60])
            raw = LINK_MARKUP.sub(r"\1", raw)
            value = f"[{value}]({links[0][1]})"  # the link moves onto the value
        if raw.endswith(":"):
            raise Queue("colon-label", raw)
        label = npc_label(raw)
        if value.endswith("\\") or GUARDED.match(value):
            raise Queue("escaped-edge", label)
        rows.append((label, value))
    return rows


def variant_block(
    chunk: list[str],
    title: str | None = None,
    commas: tuple[str, ...] = (),
    link_labels: bool = False,
    sentences: bool = False,
    allowed: tuple[str, ...] = (),
) -> tuple[str, list[str]]:
    """(the stat block, its labels) for the lines of a statistics paragraph. `title` is the printed
    variant name. A `**Sources:**` line or a sentence value (unless `sentences`) queues the file, and
    so does a label outside `allowed` when that list is given."""
    rows: list[tuple[str, list[str]]] = []
    for segment in "\n".join(chunk).split("\\\n"):
        if segment.startswith("**Sources:**"):
            raise Queue("sources-line-in-variant")
        found = vrows(segment, commas, link_labels)
        if not sentences and any(is_sentences(value) for _, value in found):
            raise Queue("sentences-in-variant", found[0][0])
        rows.extend((label, [value]) for label, value in found)
    labels = [label for label, _ in rows]
    if not rows or len(set(labels)) != len(labels):
        raise Queue("label-twice" if rows else "prose-variant", labels[0] if labels else "")
    if allowed and any(label not in allowed for label in labels):
        raise Queue("unexpected-label", next(label for label in labels if label not in allowed))
    return render_block(title, rows), labels


def bold_title(line: str) -> str | None:
    """`**Name**` with a trailing break: the printed name of a variant alone on its line."""
    found = re.fullmatch(r"\*\*([^*:\[\]]+)\*\*\\", line)
    return found.group(1) if found else None


def variant_tokens(text: str, commas: tuple[str, ...] = ()) -> list[str]:
    """The words of a statistics paragraph or of stat blocks, in one form: links reduced to their
    text, a bold label read as `Label:`, the `;` (and the `,` of `commas`) before a label dropped,
    and the title line of a block read as the bold name of a variant."""
    text = LINK_MARKUP.sub(r"\1", text).replace("\\\n", "\n")
    text = re.sub(r"^::: statblock$|^:::$", "", text, flags=re.M)
    text = re.sub(r'^title = "([^"]+)"$', r"\1:", text, flags=re.M)
    for label in commas:
        text = re.sub(r",(\s*\*\*" + re.escape(label) + r"\*\*)", r"\1", text)
    text = re.sub(r";?\s*\*\*([^*]*?):?\*\*", r" \1:", text)
    return text.split()


def link_targets(text: str) -> list[str]:
    return sorted(target for _, target in LINK_MARKUP.findall(text))


def prove_variants(
    body: str,
    new_body: str,
    cs: list[list[str]],
    swaps: dict[int, list[str]],
    commas: tuple[str, ...],
    printed_before: dict[int, str] | None = None,
) -> None:
    """Every changed paragraph is one of `swaps` (old index -> the new paragraphs), the new body is
    the old one with exactly those swaps, the words and the link targets of each swap are the same
    before and after, and no heading changes. `printed_before` names the swaps whose title is the
    label of the paragraph above them (`**Shield Bash Attacks:**`): the title is then the one added
    word group, and the paragraph above must open with it."""
    printed_before = printed_before or {}
    texts = ["\n".join(chunk) for chunk in cs]
    rebuilt = "\n" + "\n\n".join("\n\n".join(swaps[i]) if i in swaps else text for i, text in enumerate(texts)) + "\n"
    if rebuilt != new_body:
        raise ProofFailed("the new body is not the old body with the swaps")
    for index, new in swaps.items():
        old_text, new_text = texts[index], "\n\n".join(new)
        added = []
        if index in printed_before:
            if not texts[index - 1].startswith(f"**{printed_before[index]}:**"):
                raise ProofFailed("the title is not the label of the paragraph above: " + printed_before[index])
            added = (printed_before[index] + ":").split()
        if added + variant_tokens(old_text, commas) != variant_tokens(new_text, commas):
            expected, actual = added + variant_tokens(old_text, commas), variant_tokens(new_text, commas)
            at = next((i for i, (a, b) in enumerate(zip(expected, actual)) if a != b), min(len(expected), len(actual)))
            raise ProofFailed(f"words differ at {at}: {expected[at:at + 6]} / {actual[at:at + 6]}")
        check_weapon_group_rows(new_text)
        if link_targets(old_text) != link_targets(new_text) and not weapon_group_swap(old_text, new_text):
            raise ProofFailed("the link targets changed in: " + old_text[:60])
    if heading_lines(new_body) != heading_lines(body):
        raise ProofFailed("a heading changed")


def check_weapon_group_rows(text: str) -> None:
    """Item rule I5 read again: a `Weapon Group:` row is one link per group, each to the section of
    its own group, and nothing else."""
    link = r"\[([^\]]+)\]\(" + re.escape(WEAPON_GROUPS_ENTRY) + r"#([^)]+)\)"
    for line in text.split("\n"):
        if not line.startswith("Weapon Group: "):
            continue
        if not re.fullmatch(f"{link}(?:; {link})*", line[len("Weapon Group: "):]):
            raise ProofFailed("a weapon group row is not one link per group: " + line)
        for name, target in re.findall(link, line):
            if WEAPON_GROUPS.get(name) != target:
                raise ProofFailed("a weapon group links to another section: " + name)


def weapon_group_swap(old: str, new: str) -> bool:
    """The Weapon Group label link (`ref/ability/weapon-groups`) becomes one link per group, each to
    a section of the same entry (item rule I5): the only change of link targets that is allowed
    apart from a label link moving onto its value."""
    drop = lambda text: [t for t in link_targets(text) if not t.startswith(WEAPON_GROUPS_ENTRY)]  # noqa: E731
    return drop(old) == drop(new) and WEAPON_GROUP_LABEL in old and "Weapon Group:" in new


def lead_first(chunks_out: list[str], index: int, labels: list[str], extra: tuple[str, ...] = ()) -> None:
    """Drift reads the first row of each of `DRIFT_LABELS` in the body: a variant block that
    carries one needs a block with it before it, or the file queues. A kind can name `extra`
    labels that need the same."""
    for label in labels:
        if label in DRIFT_LABELS + extra and not any(
            re.search(rf"^{re.escape(label)}:", chunk, re.M) for chunk in chunks_out[:index] if chunk.startswith("::: statblock")
        ):
            raise Queue("no-lead-row", label)


def convert_variants(body: str, plan, commas: tuple[str, ...] = ()) -> str:
    """The driver of a variant pass. `plan(cs)` returns {paragraph index: (title, block options)} for
    the paragraphs the kind converts, or raises Queue; the block is made by `variant_block`."""
    cs = chunks(body.split("\n"))
    texts = ["\n".join(chunk) for chunk in cs]
    if body != "\n" + "\n\n".join(texts) + "\n":
        raise Queue("blank-lines")
    chosen = plan(cs)
    if not chosen:
        return body
    swaps: dict[int, list[str]] = {}
    printed_before: dict[int, str] = {}
    out: list[str] = []
    for index, chunk in enumerate(cs):
        if index not in chosen:
            out.append(texts[index])
            continue
        spec = chosen[index]
        lines = chunk[1:] if spec.get("drop_first") else chunk
        tail = None
        if spec.get("tail"):
            # The lines up to the first one without a label are the block; the rest stays a paragraph below it.
            segments = "\n".join(lines).split("\\\n")
            keep = next((i for i, seg in enumerate(segments) if not ITEM_LABEL.match(join_wrapped(seg.split("\n")))), len(segments))
            if keep == 0:
                raise Queue("unlabelled-line", segments[0][:40])
            lines = "\\\n".join(segments[:keep]).split("\n")
            tail = "\\\n".join(segments[keep:]) if keep < len(segments) else None
        block, labels = variant_block(lines, spec.get("title"), spec.get("commas", commas), spec.get("link_labels", False), spec.get("sentences", False), spec.get("allowed", ()))
        lead_first(out, len(out), labels, spec.get("lead_labels", ()))
        swaps[index] = [block] + ([tail] if tail else [])
        if spec.get("printed_before"):
            printed_before[index] = spec["title"]
        out.append(block)
        if tail:
            out.append(tail)
    new_body = "\n" + "\n\n".join(out) + "\n"
    prove_variants(body, new_body, cs, swaps, commas, printed_before)
    return new_body


# ---- variant kind: shield bash (13) ---------------------------------------------------------------

def plan_shield(cs: list[list[str]]) -> dict[int, dict]:
    """K-shield. The statistics of a shield bash: the paragraph of `**Damage** ...` lines directly
    under the paragraph `**Shield Bash Attacks:**` (title `Shield Bash Attacks`, the printed name of
    the paragraph; no heading is printed there), and the two `**Light shield**` and `**Heavy
    shield**` paragraphs of the shield spikes (the printed names). A weapon group label is split as
    in item rule I5."""
    chosen: dict[int, dict] = {}
    for index, chunk in enumerate(cs):
        if bold_title(chunk[0]) in ("Light shield", "Heavy shield") and len(chunk) > 1:
            chosen[index] = {"title": bold_title(chunk[0]), "drop_first": True}
        elif chunk[0].startswith("**Damage** ") and index and cs[index - 1][0].startswith("**Shield Bash Attacks:**"):
            chosen[index] = {"title": "Shield Bash Attacks", "printed_before": True}
    return chosen


def classify_variant(plan, body: str) -> str:
    return "paragraphs" if plan(chunks(body.split("\n"))) else "already"


RECIPE_LABEL = "**[Spontaneous Alchemy](ref/rule/spontaneous-alchemy) Recipe**"


def plan_recipe(cs: list[list[str]]) -> dict[int, dict]:
    """K-recipe. The paragraph that opens with the linked label `Spontaneous Alchemy Recipe`
    (alchemical items, weapons and poisons): one untitled block where it stands. The link moves
    onto the value, which is the recipe itself (`(6 quicksilver + 10 realgar)/distillation`)."""
    return {
        index: {"link_labels": True}
        for index, chunk in enumerate(cs)
        if chunk[0].startswith((RECIPE_LABEL + " ", "**Spontaneous Alchemy Recipe** "))
    }


def plan_tearaway(cs: list[list[str]]) -> dict[int, dict]:
    """K-tearaway. The paragraph `**Tear-away clothing**` alone on its first line, then the lines
    `Price`, `Weight` and `Category`: a block titled with the printed name. The block carries
    `Price` and `Weight`, so the entry's own block must come first (`no-lead-row` otherwise)."""
    return {
        index: {"title": "Tear-away clothing", "drop_first": True}
        for index, chunk in enumerate(cs)
        if bold_title(chunk[0]) == "Tear-away clothing" and len(chunk) > 1
    }


def plan_intelligent(cs: list[list[str]]) -> dict[int, dict]:
    """K-intelligent. The paragraph directly under `### Statistics` that opens with `**Alignment**`
    (the statistics of an intelligent item): one untitled block under the existing heading. The
    `,` before `Wis` and `Cha` goes; a linked label (`Special Purpose`) keeps its text and the link
    moves onto the value."""
    return {
        index: {"link_labels": True, "commas": ("Wis", "Cha")}
        for index, chunk in enumerate(cs)
        if index and cs[index - 1] == ["### Statistics"] and chunk[0].startswith("**Alignment** ")
    }


def plan_ioun(cs: list[list[str]]) -> dict[int, dict]:
    """K-ioun. The paragraph directly under a `#### Construction` heading that opens with
    `**Requirements**` (the ioun stones print it one level below the `###` Construction of the
    other items): one untitled block under that heading, which stays. The rows are `Requirements`
    and `Cost`, as under `### Construction` (item rule I8)."""
    return {
        index: {}
        for index, chunk in enumerate(cs)
        if index and cs[index - 1] == ["#### Construction"] and chunk[0].startswith("**Requirements** ")
    }


SPELLBOOK_LABELS = ("Opposition", "Protection", "Value")


def plan_spellbook(cs: list[list[str]]) -> dict[int, dict]:
    """K-spellbook. The paragraph of a spellbook that opens with `**Opposition**`, `**Protection**`
    or `**Value**`: one untitled block where it stands, under the `### Level N …` heading. Only
    those three labels are read; the `Protection` of some books is a sentence, and that is expected."""
    return {
        index: {"sentences": True, "allowed": SPELLBOOK_LABELS}
        for index, chunk in enumerate(cs)
        if any(chunk[0].startswith(f"**{label}** ") for label in SPELLBOOK_LABELS)
    }


def plan_figurine(cs: list[list[str]]) -> dict[int, dict]:
    """K-figurine. The paragraph that opens with `**CL**` and goes on as prose (the figurines of
    wondrous power print the caster level and the requirements of the Ivory Goats after their list,
    `**CL** 11th; Craft Wondrous Item, _animate objects_.`): one untitled block with the row `CL`.
    The value is kept as printed, the requirements tail included; the label is not renamed. The
    block carries `CL`, so the entry's own block must come first."""
    return {index: {} for index, chunk in enumerate(cs) if chunk[0].startswith("**CL** ")}


def plan_cost(cs: list[list[str]]) -> dict[int, dict]:
    """K-cost. A paragraph that opens with `**Cost**`. Under `### Creation Requirements` (the
    fleshcraft items) the lines with a label are the block and the line without one stays a
    paragraph below it, unchanged (the same shape as the technological Construction of ruling 3).
    Anywhere else (the bows: `**Cost** 225 gp (+1), 325 gp (+2), …` under `### Composite Bows`, and
    the `Composite longbow +N` headings) the paragraph is one untitled block where it stands, and
    the entry needs a block with a `Cost` row before it, so a variant is never the first `Cost`."""
    chosen: dict[int, dict] = {}
    for index, chunk in enumerate(cs):
        if not chunk[0].startswith("**Cost** "):
            continue
        if index and cs[index - 1] == ["### Creation Requirements"]:
            chosen[index] = {"tail": True}
        else:
            chosen[index] = {"lead_labels": ("Cost",)}
    return chosen


# name -> (the folders of the pass, its plan, the labels that may follow a comma). A new kind is one line.
VARIANT_KINDS = {
    "cost": (("eq-weapon", "magic-fleshcraft"), plan_cost, ()),
    "figurine": (("magic-wondrous",), plan_figurine, ()),
    "spellbook": (("eq-spellbook",), plan_spellbook, ()),
    "ioun": (("*",), plan_ioun, ()),
    "intelligent": (("*",), plan_intelligent, ("Wis", "Cha")),
    "tearaway": (("eq-misc",), plan_tearaway, ()),
    "recipe": (("*",), plan_recipe, ()),
    "shield": (("eq-armor", "eq-armorenh"), plan_shield, ()),
}
VARIANT_PLANS = {name: plan for name, (_, plan, _) in VARIANT_KINDS.items()}
VARIANT_COMMAS = {name: commas for name, (_, _, commas) in VARIANT_KINDS.items()}
for _name, (_folders, _, _) in VARIANT_KINDS.items():
    PASS_FOLDERS[_name] = _folders
    PASS_KIND[_name] = "item"
    APPLIED.append((_name, None))
KNOWN_PASSES = KNOWN_PASSES[:-1] + tuple(VARIANT_KINDS) + ("fixes",)


# ---- the sources pass ------------------------------------------------------------------------------


def source_names(root: Path) -> dict[str, str]:
    """Printed book name -> publication id: the exact titles of `publications.toml`, with `\\#`
    unescaped as it is in a body, and the closed list `SOURCE_ALIASES`."""
    data = tomllib.loads((root / "publications.toml").read_text(encoding="utf-8"))
    names = {row["title"]: row["id"] for row in data["publication"]}
    for name, publication in SOURCE_ALIASES.items():
        if publication not in names.values():
            raise ProofFailed(f"the alias `{name}` names the unknown publication `{publication}`")
        names[name] = publication
    return names


def parse_sources_text(text: str, names: dict[str, str]) -> list[tuple[str, str, str]]:
    """S2: `Book pg N[, Book pg N]` as (printed name, publication id, page). Raises Queue."""
    text = text.replace("\\#", "#")
    ordered = sorted(names, key=len, reverse=True)
    cites: list[tuple[str, str, str]] = []
    rest = text
    while rest:
        for name in ordered:
            if rest.startswith(name + " pg "):
                page = SOURCE_PAGE.match(rest, len(name) + 4)
                if page and (page.end() == len(rest) or rest.startswith(", ", page.end())):
                    cites.append((name, names[name], page.group()))
                    rest = rest[page.end() + 2 :] if page.end() < len(rest) else ""
                    break
        else:
            unknown = re.match(r"(.+?) pg (\d+(?:-\d+)?)(?:, |$)", rest)
            if unknown:
                raise Queue("sources-unmapped-book", unknown.group(1)[:60])
            raise Queue("sources-unparsed", rest[:60])
    if not cites:
        raise Queue("sources-unparsed", text[:60])
    return cites


def paragraph_spans(lines: list[str]) -> list[tuple[int, int]]:
    """(first line, line after the last) of each block `chunks` returns, in the same order."""
    spans: list[tuple[int, int]] = []
    start = None
    for index, line in enumerate(lines):
        if not line.strip():
            if start is not None:
                spans.append((start, index))
                start = None
            continue
        if HEADING.match(line) and start is None:
            spans.append((index, index + 1))
            continue
        if start is None:
            start = index
    if start is not None:
        spans.append((start, len(lines)))
    return spans


def sources_zones(lines: list[str], kind: str) -> list[str]:
    """S1: the zone of each line: `statistics`, `construction`, `variant` or `` (no zone)."""
    spans = paragraph_spans(lines)
    cs = chunks(lines)
    if [lines[a:b] for a, b in spans] != cs:
        raise ProofFailed("paragraph_spans disagrees with chunks")
    zone = [""] * len(lines)
    if kind == "creature":
        end = region_end(lines)
        for index in range(len(lines)):
            zone[index] = "statistics" if index < end else "variant"
        return zone
    _, lead, _ = item_layout("\n".join(lines))
    if "::: statblock" in lines:
        lead = None  # the lead is a stat block already; a bold paragraph before a heading is a variant
    under = None
    for index, chunk in enumerate(cs):
        if chunk[0] == CONSTRUCTION_HEADING:
            under = index + 1 if index + 1 < len(cs) and not HEADING.match(cs[index + 1][0]) else None
            break
    for index, (first, last) in enumerate(spans):
        name = "statistics" if index == lead else "construction" if index == under else "variant"
        for line in range(first, last):
            zone[line] = name
    return zone


def page_ranges(page: str) -> list[tuple[int, int]] | None:
    """`11`, `13-14`, `11, 13-14` as (first, last) pairs; None for any other text."""
    ranges = []
    for part in page.split(","):
        found = re.fullmatch(r"\s*(\d+)(?:-(\d+))?\s*", part)
        if not found:
            return None
        first = int(found.group(1))
        ranges.append((first, int(found.group(2) or first)))
    return ranges


def page_covers(row_page: str | None, page: str) -> bool:
    """S5: whether a row's `page` holds every page of a printed citation (`N` or `N-N`)."""
    if row_page is None:
        return False
    held, wanted = page_ranges(row_page), page_ranges(page)
    if held is None or wanted is None:
        return row_page == page
    return all(any(a <= first and last <= b for a, b in held) for first, last in wanted)


def sources_front_rows(front: str) -> list[dict]:
    return tomllib.loads(front.replace("+++\n", "", 2)).get("sources", [])


def insert_source_rows(front: str, rows: list[tuple[str, str]]) -> str:
    """The front matter with `rows` added after the last `[[sources]]` row (S5)."""
    lines = front.split("\n")
    fields = lines.index("[fields]") if "[fields]" in lines else -1
    if fields < 1 or lines[fields - 1] != "":
        raise Queue("sources-front-shape")
    at = lines.index("[[expanded_in]]") if "[[expanded_in]]" in lines else fields - 1
    new: list[str] = []
    for publication, page in rows:
        new += ["[[sources]]", f'publication = "{publication}"', f'page = "{page}"']
    return "\n".join(lines[:at] + new + lines[at:])


def plan_sources(
    text: str, kind: str, names: dict[str, str], zones: tuple[str, ...] = SOURCES_ZONES
) -> tuple[str, str, str]:
    """(status, detail, new text) for the rule S of the sources pass. Status: converted, skipped
    (no raw `**Sources:**` line in `zones`) or `queue:` and a reason. A queued file stays unchanged."""
    try:
        return move_sources(text, kind, names, zones)
    except Queue as queued:
        return "queue:" + queued.reason, queued.detail, text


def move_sources(text: str, kind: str, names: dict[str, str], zones: tuple[str, ...]) -> tuple[str, str, str]:
    front, body = split_front(text)
    lines = body.split("\n")
    zone_of = sources_zones(lines, kind)
    spans = paragraph_spans(lines)
    found = []  # (first line, last line, has break, chunk span, cites)
    fenced = False
    for first, last in spans:
        for index in range(first, last):
            line = lines[index]
            if line.startswith(":::"):
                fenced = line != ":::"
            if fenced or not line.startswith(SOURCES_LABEL) or zone_of[index] not in zones:
                continue
            if index > first and not lines[index - 1].endswith("\\"):
                raise Queue("sources-shape", "the label does not open a line")
            end = index
            while not lines[end].endswith("\\") and end + 1 < last:
                end += 1
            has_break = lines[end].endswith("\\")
            if has_break and end + 1 == last:
                raise Queue("sources-shape", "a break ends the paragraph")
            if has_break and lines[end].endswith("\\\\"):
                raise Queue("sources-shape", "an escaped backslash ends the line")
            citation = " ".join(part.strip() for part in lines[index : end + 1])[len(SOURCES_LABEL) :].strip()
            if has_break:
                citation = citation[:-1].rstrip()
            found.append((index, end, has_break, (first, last), parse_sources_text(citation, names)))
    # Two logical lines may not overlap (a label inside a wrapped line).
    found.sort()
    for before, after in zip(found, found[1:]):
        if after[0] <= before[1]:
            raise Queue("sources-shape", "two labels in one line")
    if not found:
        return "skipped", "", text

    # S4: the rows. One row per book, in print order. An existing row is kept; its page must
    # agree with every page printed for that book (S5).
    have = sources_front_rows(front)
    source_ids = tomllib.loads(front.replace("+++\n", "", 2)).get("source_ids", [])
    added: list[tuple[str, str]] = []
    for _, _, _, _, cites in found:
        for _, publication, page in cites:
            if publication not in source_ids:
                raise Queue("sources-book-not-in-source-ids", publication)
            held = [row.get("page") for row in have if row["publication"] == publication]
            new_pages = [row_page for row_publication, row_page in added if row_publication == publication]
            if held:
                if not any(page_covers(row_page, page) for row_page in held):
                    raise Queue("sources-page-conflict", f"{publication}: {', '.join(str(p) for p in held)} / {page}")
            elif not new_pages:
                added.append((publication, page))
            elif set(new_pages) != {page}:
                raise Queue("sources-page-conflict", f"{publication}: {', '.join(new_pages)} / {page}")

    # S3: the lines leave the body.
    drop: set[int] = set()
    cut_break: set[int] = set()  # a line that lost the break before a removed last line
    removed_text: list[str] = []
    for first_index, end, has_break, (first, last), _ in found:
        removed_text.append("\n".join(lines[first_index : end + 1]))
    by_chunk: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for index, end, _, span, _ in found:
        by_chunk.setdefault(span, []).append((index, end))
    for (first, last), cuts in by_chunk.items():
        gone = {line for index, end in cuts for line in range(index, end + 1)}
        keep = [line for line in range(first, last) if line not in gone]
        if not keep:
            drop.update(range(first, last))
            after = last if last < len(lines) - 1 and not lines[last].strip() else None
            if after is not None:
                drop.add(after)
            elif first > 0 and not lines[first - 1].strip():
                drop.add(first - 1)
            continue
        drop.update(gone)
        if max(gone) == last - 1:  # the paragraph ended in removed lines: its last line loses its break
            tail = keep[-1]
            if not lines[tail].endswith("\\") or lines[tail].endswith("\\\\"):
                raise Queue("sources-shape", "the line before the last label has no break")
            cut_break.add(tail)
    new_lines = [
        lines[index][:-1] if index in cut_break else lines[index] for index in range(len(lines)) if index not in drop
    ]
    new_body = "\n".join(new_lines)
    new_front = insert_source_rows(front, added) if added else front
    prove_sources(front, new_front, body, new_body, removed_text, added, names)
    return "converted", "", new_front + new_body


def prove_sources(
    front: str,
    new_front: str,
    body: str,
    new_body: str,
    removed: list[str],
    added: list[tuple[str, str]],
    names: dict[str, str],
) -> None:
    """The proof of rule S (read apart from the converter): the front matter gains exactly the
    added rows, and the body loses exactly the citation lines."""
    # Front matter: the same text apart from the inserted row lines, and the same data apart from
    # the `sources` list, which gains the added rows after the old ones.
    old_lines, new_lines = front.split("\n"), new_front.split("\n")
    grown = 3 * len(added)
    if len(new_lines) != len(old_lines) + grown:
        raise ProofFailed("the front matter changed by more than the added rows")
    start = next((i for i, (a, b) in enumerate(zip(old_lines, new_lines)) if a != b), len(old_lines))
    if new_lines[start + grown :] != old_lines[start:] or new_lines[:start] != old_lines[:start]:
        raise ProofFailed("the front matter changed outside one inserted run of rows")
    old_data = tomllib.loads(front.replace("+++\n", "", 2))
    new_data = tomllib.loads(new_front.replace("+++\n", "", 2))
    rows = [{"publication": publication, "page": page} for publication, page in added]
    if new_data.pop("sources", []) != old_data.pop("sources", []) + rows or new_data != old_data:
        raise ProofFailed("the front matter data changed apart from `sources`")
    # Body: every line that left was part of a citation, and the lines that stayed are the same
    # bytes, in order, apart from one removed break at the end of a paragraph.
    old_body, new_body_lines = body.split("\n"), new_body.split("\n")
    matcher = difflib.SequenceMatcher(None, old_body, new_body_lines, autojunk=False)
    runs: list[list[str]] = []  # the old lines that left, one run for each place they left from
    breaks = 0
    for tag, a1, a2, b1, b2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if tag == "delete":
            runs.append(old_body[a1:a2])
            continue
        # A paragraph that ended in removed lines may lose the break of its new last line.
        old_slice, new_slice = old_body[a1:a2], new_body_lines[b1:b2]
        at = 0
        run: list[str] = []
        for line in new_slice:
            while at < len(old_slice) and old_slice[at] not in (line, line + "\\"):
                run.append(old_slice[at])
                at += 1
            if at == len(old_slice):
                raise ProofFailed(f"the body changed apart from the citation lines: {old_slice!r}")
            breaks += old_slice[at] != line
            at += 1
        runs.append(run + old_slice[at:])
    if breaks > len(removed):
        raise ProofFailed("more breaks were removed than citations")
    citation_lines = [line for text in removed for line in text.split("\n")]
    leftover = list(citation_lines)
    for run in runs:
        # A run is citation lines, with one blank line at one end when a whole paragraph left.
        core = run
        if core and not core[0].strip():
            core = core[1:]
        elif core and not core[-1].strip():
            core = core[:-1]
        if not core:
            raise ProofFailed("a blank line left the body apart from a removed paragraph")
        for line in core:
            if line not in leftover:
                raise ProofFailed(f"a line other than a citation left the body: {line!r}")
            leftover.remove(line)
    if leftover:
        raise ProofFailed(f"a citation line did not leave the body: {leftover[0]!r}")
    # Citations: reading the removed lines again gives rows that the front matter holds, with the
    # pages as printed, and every added row comes from a citation.
    held = [(row["publication"], row.get("page")) for row in sources_front_rows(new_front)]
    seen: list[tuple[str, str]] = []
    for text in removed:
        if not text.startswith(SOURCES_LABEL):
            raise ProofFailed("a removed line does not open with the label")
        flat = " ".join(part.strip() for part in text.split("\n"))[len(SOURCES_LABEL) :].strip().rstrip("\\").rstrip()
        for _, publication, page in parse_sources_text(flat, names):
            if not any(book == publication and page_covers(row_page, page) for book, row_page in held):
                raise ProofFailed(f"a citation has no row: {publication} pg {page}")
            seen.append((publication, page))
    if any(row not in seen for row in added):
        raise ProofFailed("a row was added that no citation prints")
    if len(set(added)) != len(added):
        raise ProofFailed("a row was added twice")


def sources_kind(path: Path, text: str) -> str | None:
    """`creature` for a creature of `entries/monster` or `entries/npc`, `item` for an item of any
    other folder but `entries/carried`, else None (S1)."""
    kind = "creature" if path.parent.name in ("monster", "npc") else "item"
    if kind == "item" and path.parent.name in NOT_ITEM_FOLDERS:
        return None
    return kind if re.search(r'^kind = "' + kind + r'"$', split_front(text)[0], re.M) else None


def sources_survey(root: Path, names: dict[str, str], out=sys.stdout) -> None:
    """Counts of every raw `**Sources:**` line, by zone, and what rule S would do with it in every
    zone (the slices apply `SOURCES_ZONES` only). Writes nothing."""
    lines_by_zone: collections.Counter = collections.Counter()
    files_by_zone: collections.Counter = collections.Counter()
    handled: collections.Counter = collections.Counter()
    queued: collections.Counter = collections.Counter()
    unmapped: collections.Counter = collections.Counter()
    in_scope = 0
    files = set()
    for path in pass_files(root, "sources"):
        text = path.read_text(encoding="utf-8")
        kind = sources_kind(path, text)
        if kind is None:
            continue
        body = split_front(text)[1]
        lines = body.split("\n")
        zone_of = sources_zones(lines, kind)
        zones = collections.Counter(
            zone_of[index] for index, line in enumerate(lines) if line.startswith(SOURCES_LABEL)
        )
        if not zones:
            continue
        files.add(path)
        in_scope += sum(zones.values())
        for zone, count in zones.items():
            lines_by_zone[zone] += count
            files_by_zone[zone] += 1
        for label, scope in (("now", SOURCES_ZONES), ("every zone", ALL_ZONES)):
            status, detail, _ = plan_sources(text, kind, names, scope)
            if status == "converted":
                handled[label, "files"] += 1
                handled[label, "lines"] += sum(zones[zone] for zone in scope)
            elif status.startswith("queue:"):
                queued[label, status[6:]] += 1
                if label == "every zone" and status == "queue:sources-unmapped-book":
                    unmapped[detail] += 1
    print(f"sources survey: {in_scope} raw `**Sources:**` lines in {len(files)} creature and item entries", file=out)
    for zone in ALL_ZONES:
        print(f"  zone {zone}: {lines_by_zone[zone]} lines in {files_by_zone[zone]} files", file=out)
    for label in ("now", "every zone"):
        zones = ", ".join(SOURCES_ZONES) if label == "now" else "every zone"
        print(
            f"  rule S in {zones}: would convert {handled[label, 'files']} files ({handled[label, 'lines']} lines); queues "
            + (", ".join(f"{reason} {count}" for (kind, reason), count in sorted(queued.items()) if kind == label) or "none"),
            file=out,
        )
    for name, count in unmapped.most_common():
        print(f"  unmapped book: {name} ({count})", file=out)
    other = collections.Counter()
    for path in sorted((root / "entries").rglob("*.md")):
        if path not in files and re.search(r"^\*\*Sources:\*\*", path.read_text(encoding="utf-8"), re.M):
            other[path.relative_to(root / "entries").parts[0]] += 1
    print(f"  outside the pass (other kinds, carried entries): {sum(other.values())} files with raw lines", file=out)


def sources_leftovers(body: str, kind: str) -> list[str]:
    """The books and pages of the raw `**Sources:**` lines in zones the pass does not handle yet."""
    lines = body.split("\n")
    zone_of = sources_zones(lines, kind)
    out = []
    fenced = False
    for index, line in enumerate(lines):
        if line.startswith(":::"):
            fenced = line != ":::"
        if not fenced and line.startswith(SOURCES_LABEL) and zone_of[index] not in SOURCES_ZONES:
            out.append(re.sub(r"\\$", "", line[len(SOURCES_LABEL) :].strip()).replace("\\#", "#"))
    return out


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
    if name == "sources":
        return sorted({path for part in ("creature", "npc", "item") for path in pass_files(root, part)})
    out = []
    for folder in PASS_FOLDERS[name]:
        out.extend(sorted((root / "entries").glob(folder + "/*.md")))
    if name == "item":
        # Every folder but the carried PSRD entries and the creature folders; `plan_file` skips
        # what is not an item.
        out = [path for path in sorted(out) if path.parent.name not in NOT_ITEM_FOLDERS]
    return out


def plan_file(text: str, name: str = "creature") -> tuple[str, str, str]:
    """(status, detail, new text). Status: converted, already, skipped or a queue reason."""
    front, body = split_front(text)
    if not re.search(r'^kind = "' + PASS_KIND[name] + r'"$', front, re.M):
        return "skipped", "", text
    try:
        classify, convert = {
            "creature": (classify_monster, convert_monster),
            "npc": (classify_npc, convert_npc),
            "item": (classify_item, convert_item),
            "siege": (classify_siege, convert_siege),
            **{
                kind: (
                    lambda body, plan=plan: classify_variant(plan, body),
                    lambda body, plan=plan, kind=kind: convert_variants(body, plan, VARIANT_COMMAS.get(kind, ())),
                )
                for kind, plan in VARIANT_PLANS.items()
            },
        }[name]
        state = classify(body)
        if state == "already":
            return "already", "", text
        if state == "old-labels":
            return "relabelled", "", front + relabel_npc(body)
        new_body = convert(body)
        if new_body == body:
            return "no-statistics", "", text
    except Queue as queued:
        return "queue:" + queued.reason, queued.detail, text
    new_text = front + new_body
    if split_front(new_text) != (front, new_body) or not new_text.startswith(front):
        raise ProofFailed("the front matter changed")
    return "converted", "", new_text


def plan_any(path: Path, name: str, names: dict[str, str]) -> tuple[str, str, str]:
    """`plan_file` for the conversion passes, `plan_sources` for the sources pass."""
    text = path.read_text(encoding="utf-8")
    if name != "sources":
        return plan_file(text, name)
    kind = sources_kind(path, text)
    return plan_sources(text, kind, names) if kind else ("skipped", "", text)


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
    names = source_names(root)
    for rel, citation, note, _ in PRINT_FIXES:
        kind = {"monster": "creature", "npc": "npc"}.get(rel.split("/")[1], "item")
        rows.append((rel, kind, "print-fix", f"{note} ({citation})"))
    for name in passes:
        for path in pass_files(root, name):
            rel = path.relative_to(root).as_posix()
            text = path.read_text(encoding="utf-8")
            if name == "sources":
                # Rule S lists what stays raw: a queued file, and the lines in zones not handled yet.
                kind = sources_kind(path, text)
                if kind is None:
                    continue
                status, detail, _ = plan_sources(text, kind, names)
                shown = {"monster": "creature", "npc": "npc"}.get(path.parent.name, "item")
                if status.startswith("queue:"):
                    rows.append((rel, shown, status[6:], detail))
                left = sources_leftovers(split_front(text)[1], kind)
                if left:
                    # What rule S would do with every line of the file: the queue of the variant slices.
                    outcome = plan_sources(text, kind, names, ALL_ZONES)[0]
                    outcome = "movable" if outcome == "converted" else outcome.replace("queue:", "")
                    cited = "; ".join(dict.fromkeys(left))
                    rows.append((rel, shown, "raw-sources-line", f"{len(left)} in variant paragraphs: {cited} (rule S in every zone: {outcome})"))
                continue
            status, detail, _ = plan_file(text, name)
            if status.startswith("queue:"):
                rows.append((rel, name, status[6:], detail))
            elif name == "item" and status != "skipped":
                body = split_front(text)[1]
                left = item_leftovers(body)
                if left:
                    rows.append((rel, name, "variant-paragraphs", "; ".join(left)))
                cut = item_sentence_cut(body)
                if cut:
                    rows.append((rel, name, "block-ended-at-sentences", cut))
                if construction_unlabelled(chunks(body.split("\n"))):
                    rows.append((rel, name, "construction-unlabelled", ""))
            if PASS_KIND.get(name) == "item":
                continue
            for row in print_254_rows(split_front(text)[1]):
                rows.append((rel, name, "print-254", row))
    rows.sort()
    return [TSV_HEADER] + ["\t".join(row) for row in rows]


def run(root: Path, mode: str, passes: list[str], only_value: str | None, out=sys.stdout) -> int:
    counts: collections.Counter = collections.Counter()
    changed = 0
    names = source_names(root)
    for fix in PRINT_FIXES + ANCHOR_EDITS:
        state, fixed = fix_state(root, fix)
        print(f"{'print fix' if fix[1] else 'anchors'} {fix[0]}: {state}", file=out)
        if state == "unknown":
            print(f"error: {fix[0]} matches neither side of its edit", file=sys.stderr)
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
            status, detail, new_text = plan_any(path, name, names)
            if status == "skipped":
                continue
            counts[(name, status)] += 1
            if status in ("converted", "relabelled"):
                changed += 1
                if mode == "write":
                    write_atomic(path, new_text)
                    if name == "sources":
                        again = plan_sources(new_text, sources_kind(path, new_text), names)[0]
                        if again != "skipped":
                            raise ProofFailed(f"{path}: a second run still finds a citation to move ({again})")
                    elif plan_file(new_text, name)[0] != "already":
                        raise ProofFailed(f"{path}: the written file does not read as converted")
                elif mode == "check":
                    print(f"would change: {path.relative_to(root).as_posix()}", file=out)
    if any(PASS_FOLDERS[name] for name, _ in scopes) and not only_shown:
        print("no file matches the scope", file=out)

    verb = {"write": "converted", "check": "would convert", "survey": "would convert"}[mode]
    for (name, status), count in sorted(counts.items()):
        label = verb if status == "converted" else status.replace("queue:", "queued: ")
        if status == "relabelled" and mode != "write":
            label = "would relabel"
        print(f"{name}\t{label}\t{count}", file=out)

    if mode == "survey" and "sources" in passes:
        sources_survey(root, names, out)
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
            unittest.defaultTestLoader.loadTestsFromTestCase(case) for case in (SelfTest, NpcSelfTest, ItemSelfTest, SiegeSelfTest, VariantSelfTest, RecipeSelfTest, TearawaySelfTest, IntelligentSelfTest, IounSelfTest, SpellbookSelfTest, FigurineSelfTest, CostSelfTest, SourcesSelfTest)
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
            (root / "publications.toml").write_text(SOURCES_PUBLICATIONS, encoding="utf-8")
            for rel, _, _, pairs in PRINT_FIXES + ANCHOR_EDITS:
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
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
Caster level: 6th
Concentration: +9
6/day: dehydrating touch
:::

::: statblock
title = "Wizard Spells Prepared"
Caster level: 6th
Concentration: +9
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
            NPC_EXPECTED.replace("Concentration: +9\n3rd", "Concentration: +8\n3rd"),  # a number changed
            NPC_EXPECTED.replace("Caster level: 6th\nConcentration: +9\n3rd", "Caster level: 5th\nConcentration: +9\n3rd"),
            NPC_EXPECTED.replace("Caster level: 6th\nConcentration: +9\n3rd", "CL: 6th\nconcentration: +9\n3rd"),  # N8 not applied
            NPC_EXPECTED.replace("Caster level: 6th\nConcentration: +9\n3rd", "Level: 6th\nConcentration: +9\n3rd"),  # another label
            NPC_EXPECTED.replace("**[haste](ref/spell/haste)**", "[haste](ref/spell/haste)"),  # bold lost in a level row
            NPC_EXPECTED.replace("**[haste](ref/spell/haste)**", "**[haste](ref/spell/haste)"),
            NPC_EXPECTED.replace("fly, ", "**fly**, "),  # bold added in a level row
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

    def test_an_npc_with_the_old_header_labels_is_relabelled_and_nothing_else(self):
        old = NPC_EXPECTED.replace("Caster level: 6th\nConcentration: +9", "CL: 6th\nconcentration: +9")
        # Rows with the same labels that do not open a titled block stay.
        old = old.replace("Speed: 30 ft.\n", "CL: 3rd\nconcentration: +1\nSpeed: 30 ft.\n").replace("D: Domain spell", "CL: stays")
        expected = old.replace("CL: 6th\nconcentration: +9", "Caster level: 6th\nConcentration: +9")
        self.assertEqual(old.count("CL: 6th"), 2)
        self.assertEqual(classify_npc(old), "old-labels")
        self.assertEqual(plan_file(FRONT + old, "npc"), ("relabelled", "", FRONT + expected))
        self.assertEqual(plan_file(FRONT + expected, "npc")[0], "already")
        self.assertEqual(plan_file(FRONT + NPC_EXPECTED, "npc")[0], "already")
        prove_relabel(old, expected)
        for broken in (
            expected.replace("Caster level: 6th", "Caster level: 7th", 1),
            expected.replace("Concentration: +9", "Concentration: +8", 1),
            expected.replace("CL: 3rd", "Caster level: 3rd"),
            expected.replace("CL: stays", "Caster level: stays"),
            expected.replace("fly, ", ""),
            expected + "\n",
        ):
            with self.assertRaises(ProofFailed):
                prove_relabel(old, broken)


ITEM_SAMPLE = r"""
## Klar

This shield is a short blade bound to a skull.

**Cost** 12 gp **Weight** 6 lbs.\
**Damage** 1d4 (small), 1d6 (medium); **Critical** ×2; **Range** -; **Type** S; **Special** see
text\
**Category** [One-Handed](ref/rule/one-handed); **Proficiency** Martial\
**[Weapon Group](ref/ability/weapon-groups)** Blades, Heavy; Close\
**Preparation** The skull must be dried. This process takes 8 hours.\
**Use** It is strapped on.

**Note:** Stats are an extrapolation.

### Construction

**Requirements** [Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor), creator must
be a dwarf; **Cost** 6 gp

**Tear-away klar**\
**Sources:** Adventurer's Armory pg 19\
**Price** +5 gp; **Weight** -

### Variants

**Cost** 20 gp; **Weight** 7 lbs.
"""

ITEM_EXPECTED = r"""
## Klar

This shield is a short blade bound to a skull.

::: statblock
Cost: 12 gp
Weight: 6 lbs.
Damage: 1d4 (small), 1d6 (medium)
Critical: ×2
Range: -
Type: S
Special: see text
Category: [One-Handed](ref/rule/one-handed)
Proficiency: Martial
Weapon Group: [Blades, Heavy](ref/ability/weapon-groups#sec-heavy-blades); [Close](ref/ability/weapon-groups#sec-close)
:::

**Preparation** The skull must be dried. This process takes 8 hours.\
**Use** It is strapped on.

**Note:** Stats are an extrapolation.

### Construction

::: statblock
Requirements: [Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor), creator must be a dwarf
Cost: 6 gp
:::

**Tear-away klar**\
**Sources:** Adventurer's Armory pg 19\
**Price** +5 gp; **Weight** -

### Variants

**Cost** 20 gp; **Weight** 7 lbs.
"""

ITEM_FRONT = FRONT.replace("creature", "item")


class ItemSelfTest(unittest.TestCase):
    def queued(self, body: str) -> str:
        with self.assertRaises(Queue) as caught:
            classify_item(body)
            convert_item(body)
        return caught.exception.reason

    def test_an_item_converts_by_the_rules(self):
        self.assertEqual(convert_item(ITEM_SAMPLE), ITEM_EXPECTED)

    def test_a_converted_item_reads_as_already_and_keeps_its_variant_queue(self):
        status, _, text = plan_file(ITEM_FRONT + ITEM_SAMPLE, "item")
        self.assertEqual((status, text), ("converted", ITEM_FRONT + ITEM_EXPECTED))
        self.assertEqual(plan_file(text, "item"), ("already", "", text))
        self.assertEqual(plan_file(FRONT + ITEM_SAMPLE, "item")[0], "skipped")
        self.assertEqual(item_leftovers(ITEM_SAMPLE), ["Tear-away klar", "Cost"])
        self.assertEqual(item_leftovers(ITEM_EXPECTED), ["Tear-away klar", "Cost"])

    def test_an_item_without_a_lead_is_left_alone(self):
        prose = "\nA metal.\n\n**Note:** No statistics.\n\n|A|B|\n| --- | --- |\n|1|2|\n"
        self.assertEqual(plan_file(ITEM_FRONT + prose, "item")[0], "no-statistics")
        under_heading = "\nA bow.\n\n### Composite\n\n**Cost** 5 gp; **Weight** 1 lb.\n"
        self.assertEqual(plan_file(ITEM_FRONT + under_heading, "item")[0], "no-statistics")
        self.assertEqual(item_leftovers(under_heading), ["Cost"])
        self.assertEqual(item_leftovers(prose), [])

    def test_only_the_cost_weight_pair_splits_without_a_separator(self):
        self.assertEqual(self.queued(ITEM_SAMPLE.replace("**Critical** ×2; **Range**", "**Critical** ×2 **Range**")), "label-without-separator")
        self.assertEqual(self.queued(ITEM_SAMPLE.replace("**Cost** 12 gp **Weight**", "**Price** 12 gp **Weight**")), "label-without-separator")

    def test_weapon_groups_come_from_the_closed_list(self):
        self.assertEqual(
            weapon_group_value("Blades, Heavy; Blades, Light; Thrown"),
            "[Blades, Heavy](ref/ability/weapon-groups#sec-heavy-blades); "
            "[Blades, Light](ref/ability/weapon-groups#sec-light-blades); [Thrown](ref/ability/weapon-groups#sec-thrown)",
        )
        for value in ("Varies", "Blades, Heavy, Close", "Blades; Close", "Close;Monk", "Close; see text", ""):
            with self.subTest(value=value):
                self.assertEqual(self.queued(ITEM_SAMPLE.replace("Blades, Heavy; Close", value)), "weapon-group")

    def test_what_the_item_rules_do_not_cover_is_queued(self):
        cases = [
            ("linked-label", ITEM_SAMPLE.replace("**Category**", "**[Hardness](ref/umr/hardness)**")),
            ("linked-label", ITEM_SAMPLE.replace("**Requirements**", "**[Weapon Group](ref/ability/weapon-groups)**")),
            ("unlabelled-line", ITEM_SAMPLE.replace("**Category** [One-Handed]", "[One-Handed]")),
            ("label-without-separator", ITEM_SAMPLE.replace("be a dwarf; **Cost** 6 gp", "be a dwarf **Cost** 6 gp")),
            ("sentences-mid-line", ITEM_SAMPLE.replace("**Category** [One-Handed](ref/rule/one-handed); **Proficiency** Martial", "**Category** One; **Proficiency** It must be learned. This takes a year.")),
            ("colon-label", ITEM_SAMPLE.replace("**Category** [One", "**Category:** [One")),
            ("sources-line-in-lead", ITEM_SAMPLE.replace("**Category** [One", "**Sources:** Book pg 1\\\n**Category** [One")),
            ("label-twice", ITEM_SAMPLE.replace("**Proficiency** Martial", "**Type** Martial")),
            ("label-needs-escape", ITEM_SAMPLE.replace("**Proficiency**", "**Profi_ciency**")),
            ("escaped-edge", ITEM_SAMPLE.replace("**Proficiency** Martial", "**Proficiency** \\- Martial")),
            ("prose-lead", ITEM_SAMPLE.replace("**Cost** 12 gp **Weight** 6 lbs.", "**Cost** The cost is high. Very high.")),
            ("fence-in-body", ITEM_SAMPLE + "\n::: entry-link\ntarget = \"ref/x/y\"\n:::\n"),
        ]
        for reason, body in cases:
            with self.subTest(reason=reason, body=body[60:140]):
                self.assertNotEqual(body, ITEM_SAMPLE)
                self.assertEqual(self.queued(body), reason)

    def test_a_construction_paragraph_with_an_unlabelled_line_stays_prose(self):
        tech = ITEM_SAMPLE.replace("be a dwarf; **Cost** 6 gp", "be a dwarf\\\nCraft Technological Item, production lab")
        new = convert_item(tech)
        expected = ITEM_EXPECTED.replace(
            "::: statblock\nRequirements: [Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor), creator must be a dwarf\nCost: 6 gp\n:::",
            "**Requirements** [Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor), creator must\n"
            "be a dwarf\\\nCraft Technological Item, production lab",
        )
        self.assertNotEqual(expected, ITEM_EXPECTED)
        self.assertEqual(new, expected)
        for body in (tech, new):
            self.assertTrue(construction_unlabelled(chunks(body.split("\n"))))
            self.assertEqual(item_leftovers(body), ["Tear-away klar", "Cost"])  # not a variant
        self.assertFalse(construction_unlabelled(chunks(ITEM_SAMPLE.split("\n"))))
        self.assertFalse(construction_unlabelled(chunks(ITEM_EXPECTED.split("\n"))))
        # Only when the lead converts: a lead the rules cannot read still queues the file.
        self.assertEqual(self.queued(tech.replace("**Category** [One-Handed]", "[One-Handed]")), "unlabelled-line")

    def test_the_proof_requires_one_link_for_each_weapon_group(self):
        for row in (
            "[Blades, Heavy](ref/ability/weapon-groups#sec-heavy-blades); Close",
            "Blades, Heavy; [Close](ref/ability/weapon-groups#sec-close)",
            "Blades, Heavy; Close",
            "[Blades, Heavy; Close](ref/ability/weapon-groups#sec-heavy-blades)",
            "[Blades, Heavy](ref/ability/weapon-groups#sec-heavy-blades); [Close](ref/ability/weapon-groups#sec-close) ",
        ):
            text = re.sub(r"(?m)^Weapon Group: .*$", lambda _: "Weapon Group: " + row, ITEM_EXPECTED)
            with self.subTest(row=row):
                self.assertNotEqual(text, ITEM_EXPECTED)
                with self.assertRaises(ProofFailed):
                    prove_item(ITEM_SAMPLE, text)

    def test_the_proof_fixes_where_the_sentence_rule_cuts_the_block(self):
        # Late: a sentence line taken into the block.
        late = ITEM_EXPECTED.replace(
            ":::\n\n**Preparation** The skull must be dried. This process takes 8 hours.\\\n**Use**",
            "Preparation: The skull must be dried. This process takes 8 hours.\n:::\n\n**Use**",
        )
        # Early: a row left out of the block, in front of the sentence lines.
        early = ITEM_EXPECTED.replace(
            "Weapon Group: [Blades, Heavy](ref/ability/weapon-groups#sec-heavy-blades); [Close](ref/ability/weapon-groups#sec-close)\n:::\n\n",
            ":::\n\n**[Weapon Group](ref/ability/weapon-groups)** Blades, Heavy; Close\\\n",
        )
        # No cut at all: the whole tail made rows.
        none = ITEM_EXPECTED.replace(
            ":::\n\n**Preparation** The skull must be dried. This process takes 8 hours.\\\n**Use** It is strapped on.",
            "Preparation: The skull must be dried. This process takes 8 hours.\nUse: It is strapped on.\n:::",
        )
        for name, text in (("late", late), ("early", early), ("none", none)):
            with self.subTest(name=name):
                self.assertNotEqual(text, ITEM_EXPECTED)
                self.assertEqual(item_words(text), item_words(ITEM_SAMPLE))  # the words alone do not show it
                with self.assertRaises(ProofFailed):
                    prove_item(ITEM_SAMPLE, text)

    def test_the_sentence_cut_is_listed_before_and_after(self):
        self.assertEqual(item_sentence_cut(ITEM_SAMPLE), "Preparation")
        self.assertEqual(item_sentence_cut(ITEM_EXPECTED), "Preparation")
        plain = ITEM_SAMPLE.replace("\\\n**Preparation** The skull must be dried. This process takes 8 hours.\\\n**Use** It is strapped on.", "")
        self.assertEqual(item_sentence_cut(plain), None)
        self.assertEqual(item_sentence_cut(convert_item(plain)), None)
        cut_at_second_line = "\n**Price** 5 gp\\\n**Use** It must be worn on the arm for a full day to work.\n"
        self.assertEqual(convert_item(cut_at_second_line), "\n::: statblock\nPrice: 5 gp\n:::\n\n**Use** It must be worn on the arm for a full day to work.\n")
        self.assertEqual(item_sentence_cut(cut_at_second_line), "Use")
        self.assertEqual(item_sentence_cut(convert_item(cut_at_second_line)), "Use")

    def test_sentences_end_the_block_and_units_do_not(self):
        for value in ("4 lbs.", "1d6 (small), 1d8 (medium)", "see text.", "5 ft. (10 ft. with lance)", "30 gp. Masterwork"):
            self.assertFalse(is_sentences(value), value)
        for value in ("The skull must be dried. This process takes 8 hours.", "It must be worn on the arm for a full day to work."):
            self.assertTrue(is_sentences(value), value)

    def test_the_item_proof_fails_on_any_other_change(self):
        prove_item(ITEM_SAMPLE, ITEM_EXPECTED)
        broken = [
            ITEM_EXPECTED.replace("Critical: ×2\n", ""),
            ITEM_EXPECTED.replace("Weight: 6 lbs.", "Weight: 6 lb."),
            ITEM_EXPECTED.replace("Cost: 6 gp", "Cost: 7 gp"),
            ITEM_EXPECTED.replace("Category: [One-Handed](ref/rule/one-handed)", "Category: One-Handed"),
            ITEM_EXPECTED.replace("[Blades, Heavy](ref/ability/weapon-groups#sec-heavy-blades)", "[Blades, Light](ref/ability/weapon-groups#sec-light-blades)"),
            ITEM_EXPECTED.replace("#sec-heavy-blades", "#sec-light-blades"),  # the right text on the wrong section
            ITEM_EXPECTED.replace("[Close](ref/ability/weapon-groups#sec-close)", "[Close](ref/rule/close)"),
            ITEM_EXPECTED.replace("; [Close](ref/ability/weapon-groups#sec-close)", ""),
            ITEM_EXPECTED.replace("; [Close]", ", [Close]"),
            ITEM_EXPECTED.replace("**Price** +5 gp; **Weight** -", "**Price** +5 gp **Weight** -"),  # a paragraph the pass must not touch
            ITEM_EXPECTED.replace("**Note:** Stats", "**Note** Stats"),
            ITEM_EXPECTED.replace("**Use** It is strapped on.", "**Use** It is strapped."),
            ITEM_EXPECTED.replace("### Construction", "### Constructions"),
            ITEM_EXPECTED.replace("This shield is", "This  shield is"),
        ]
        for number, text in enumerate(broken):
            with self.subTest(number=number):
                self.assertNotEqual(text, ITEM_EXPECTED)
                with self.assertRaises(ProofFailed):
                    prove_item(ITEM_SAMPLE, text)

    def test_the_weapon_group_headings_get_their_keys_as_anchors(self):
        pairs = dict(ANCHOR_EDITS[0][3])
        self.assertEqual(pairs["\n### Heavy Blades\n"], "\n### Heavy Blades {#sec-heavy-blades}\n")
        self.assertEqual(pairs["\n### Siege Engines\n"], "\n### Siege Engines {#sec-siege-engines}\n")
        for old, new in pairs.items():
            self.assertEqual(heading_keys([old.strip()]), heading_keys([new.strip()]))
        self.assertEqual(len(pairs), len(WEAPON_GROUPS))

SOURCES_PUBLICATIONS = """
[[publication]]
id = "bestiary"
title = "Bestiary"

[[publication]]
id = "ultimate-equipment"
title = "Ultimate Equipment"

[[publication]]
id = "core-rulebook"
title = "Core Rulebook"

[[publication]]
id = "pathfinder-93-forge"
title = "Pathfinder #93: Forge"
"""

SOURCES_FRONT = (
    '+++\nid = "ref/monster/x"\nkind = "creature"\ntitle = "X"\n'
    'source_ids = ["bestiary", "ultimate-equipment", "core-rulebook", "pathfinder-93-forge"]\n'
    'provenance = [\n  { dataset = "d", record = "x", path = "j.json" },\n]\n'
    '[[sources]]\npublication = "bestiary"\npage = "10"\n\n[fields]\nkind = "creature"\n+++\n'
)

SOURCES_CREATURE = """
**Challenge rating:** 2

**Sources:** Bestiary pg 10\\
**Experience points:** 600

**Armor class:** 13

**Offense**

**Speed:** 40 ft.

### Description

Text.

**Sources:** Bestiary pg 11\\
**Type:** animal
"""

SOURCES_ITEM_FRONT = SOURCES_FRONT.replace("creature", "item").replace('"ref/monster/x"', '"ref/magic-wondrous/x"')

SOURCES_ITEM = """
::: statblock
Price: 1 gp
:::

Text.

### Construction

**Sources:** Ultimate Equipment pg 302, PRPG Core Rulebook pg 525\\
**Requirements** [Craft Wondrous Item](ref/feat/craft-wondrous-item); **Cost** 1,250 gp

### Variant

**Sources:** Ultimate Equipment pg 99\\
**Price** +5 gp
"""


class SiegeSelfTest(unittest.TestCase):
    BODY = (
        "\n## Ram\n\nA ram hits.\n\n::: statblock\nLarge:\nCost: 500 gp\nWeight: -\n:::\n\n"
        "**Huge**\\\n**Cost** 1,000 gp **Weight** -\\\n**Damage** 3d6; **Critical** ×3; **Range** -; **Type** B\\\n"
        "**Category** Close Assault; **Proficiency** Siege Engine\n\n"
        "**Colossal**\\\n**Cost** 5,000 gp **Weight** -\\\n**Damage** 10d6\n"
    )

    def test_each_size_becomes_a_block_titled_with_it_and_the_lead_stays(self):
        self.assertEqual(classify_siege(self.BODY), "paragraphs")
        new = convert_siege(self.BODY)
        self.assertEqual(
            new,
            "\n## Ram\n\nA ram hits.\n\n::: statblock\nLarge:\nCost: 500 gp\nWeight: -\n:::\n\n"
            '::: statblock\ntitle = "Huge"\nCost: 1,000 gp\nWeight: -\nDamage: 3d6\nCritical: ×3\nRange: -\nType: B\n'
            "Category: Close Assault\nProficiency: Siege Engine\n:::\n\n"
            '::: statblock\ntitle = "Colossal"\nCost: 5,000 gp\nWeight: -\nDamage: 10d6\n:::\n',
        )
        self.assertEqual(classify_siege(new), "already")  # idempotent

    def test_the_cases_the_rules_do_not_cover_queue(self):
        cases = {
            "label-twice": "**Huge**\\\n**Cost** 1 gp **Weight** -\\\n**Cost** 2 gp",
            "unlabelled-line": "**Huge**\\\n**Cost** 1 gp **Weight** -\\\nA plain line",
            "sources-line-in-variant": "**Huge**\\\n**Sources:** Bestiary pg 1\\\n**Cost** 1 gp",
            "sentences-in-variant": "**Huge**\\\n**Cost** A ram is hauled by a crew. It then charges.",
            "label-without-separator": "**Huge**\\\n**Damage** 3d6 **Critical** ×3",
        }
        for reason, paragraph in cases.items():
            with self.subTest(reason=reason):
                with self.assertRaises(Queue) as caught:
                    convert_siege("\n" + paragraph + "\n")
                self.assertEqual(caught.exception.reason, reason)
        with self.assertRaises(Queue):
            classify_siege("\n:::: quote\n**Huge**\\\n**Cost** 1 gp\n::::\n")

    def test_a_size_with_a_colon_and_other_paragraphs_stay(self):
        body = "\n**Light:**\\\n**Cost** 1 gp\n\n**Huge**\nA sentence.\n"
        self.assertEqual(classify_siege(body), "already")

    def test_the_proof_catches_a_changed_value_a_dropped_row_and_a_wrong_title(self):
        good = convert_siege(self.BODY)
        for name, bad in {
            "value": good.replace("Cost: 1,000 gp", "Cost: 1,001 gp"),
            "row": good.replace("Weight: -\nDamage: 3d6", "Damage: 3d6"),
            "title": good.replace('title = "Huge"', 'title = "Large"'),
            "prose": good.replace("A ram hits.", "A ram hit."),
        }.items():
            with self.subTest(name=name):
                with self.assertRaises(ProofFailed):
                    prove_siege(self.BODY, bad)


class VariantSelfTest(unittest.TestCase):
    """The shared part of the variant passes and the kinds, one test group for each kind."""

    SHIELD = (
        "\n::: statblock\nCost: 20 gp\nWeight: 15 lbs.\n:::\n\nA shield.\n\n"
        "**Shield Bash Attacks:** You can bash an opponent.\n\n"
        "**Damage** 1d3 (small), 1d4 (medium); **Critical** ×2; **Range** -; **Type** B; **Special**\n"
        "[performance](ref/misc/performance)\\\n"
        "**Category** One-Handed; **Proficiency** Martial\\\n"
        "**[Weapon Group](ref/ability/weapon-groups)** Blades, Light; Close\n"
    )

    def test_a_shield_bash_becomes_a_block_titled_with_the_printed_paragraph_name(self):
        self.assertEqual(classify_variant(plan_shield, self.SHIELD), "paragraphs")
        new = convert_variants(self.SHIELD, plan_shield)
        self.assertIn(
            '::: statblock\ntitle = "Shield Bash Attacks"\nDamage: 1d3 (small), 1d4 (medium)\nCritical: ×2\nRange: -\nType: B\n'
            "Special: [performance](ref/misc/performance)\nCategory: One-Handed\nProficiency: Martial\n"
            "Weapon Group: [Blades, Light](ref/ability/weapon-groups#sec-light-blades); [Close](ref/ability/weapon-groups#sec-close)\n:::\n",
            new,
        )
        self.assertTrue(new.startswith(self.SHIELD.split("**Damage**")[0]))
        self.assertEqual(classify_variant(plan_shield, new), "already")

    def test_the_shield_cases_the_rules_do_not_cover(self):
        # No `Shield Bash Attacks:` paragraph above: nothing to convert.
        self.assertEqual(classify_variant(plan_shield, self.SHIELD.replace("**Shield Bash Attacks:**", "**Bash:**")), "already")
        with self.assertRaises(Queue) as caught:
            convert_variants(self.SHIELD.replace("Blades, Light; Close", "Varies"), plan_shield)
        self.assertEqual(caught.exception.reason, "weapon-group")
        with self.assertRaises(Queue) as caught:
            convert_variants(self.SHIELD.replace("**Category**", "A plain line\\\n**Category**"), plan_shield)
        self.assertEqual(caught.exception.reason, "unlabelled-line")

    def test_the_proof_catches_a_changed_value_a_wrong_group_and_a_title_without_its_paragraph(self):
        cs = chunks(self.SHIELD.split("\n"))
        swap = {3: [convert_variants(self.SHIELD, plan_shield).split("\n\n")[-1].rstrip("\n")]}
        good = convert_variants(self.SHIELD, plan_shield)
        for name, bad in {
            "value": good.replace("Type: B", "Type: P"),
            "group": good.replace("sec-close", "sec-heavy-blades"),
            "extra link": good.replace("Special: [performance](ref/misc/performance)", "Special: [performance](ref/misc/other)"),
        }.items():
            with self.subTest(name=name):
                with self.assertRaisesRegex(ProofFailed, "words differ|links to another|link targets"):
                    prove_variants(self.SHIELD, bad, cs, {3: [bad.split("\n\n")[-1].rstrip("\n")]}, (), {3: "Shield Bash Attacks"})
        with self.assertRaisesRegex(ProofFailed, "label of the paragraph above"):  # the paragraph above does not print the title
            prove_variants(self.SHIELD, good, cs, swap, (), {3: "Shield Bash"})

    def test_a_block_that_carries_a_drift_label_needs_a_block_with_it_before(self):
        lead = "\n::: statblock\nPrice: 1 gp\n:::\n\n"
        paragraph = "**Price** 5 gp; **Weight** -\n"
        plan = lambda cs: {i: {} for i, chunk in enumerate(cs) if chunk[0].startswith("**Price**")}  # noqa: E731
        with self.assertRaises(Queue) as caught:
            convert_variants(lead + paragraph, plan)
        self.assertEqual((caught.exception.reason, caught.exception.detail), ("no-lead-row", "Weight"))
        convert_variants(lead.replace("Price: 1 gp", "Price: 1 gp\nWeight: 2 lbs.") + paragraph, plan)
        with self.assertRaises(Queue) as caught:
            convert_variants("\nA line.\n\n" + paragraph, plan)
        self.assertEqual(caught.exception.reason, "no-lead-row")

    def test_a_label_link_moves_onto_the_value_and_a_comma_before_a_listed_label_goes(self):
        rows = vrows("**[Spontaneous Alchemy](ref/rule/spontaneous-alchemy) Recipe** (6 realgar)/distillation; **Craft DC** 20", (), True)
        self.assertEqual(rows, [("Spontaneous Alchemy Recipe", "[(6 realgar)/distillation](ref/rule/spontaneous-alchemy)"), ("Craft DC", "20")])
        with self.assertRaises(Queue):
            vrows("**[Spontaneous Alchemy](ref/rule/spontaneous-alchemy) Recipe** 1", (), False)
        with self.assertRaises(Queue):  # a value that has a link already cannot take a second one
            vrows("**[A](ref/x/a) B** see [c](ref/x/c)", (), True)
        self.assertEqual(vrows("**Int** 14, **Wis** 16, **Cha** 14", ("Wis", "Cha")), [("Int", "14"), ("Wis", "16"), ("Cha", "14")])
        with self.assertRaises(Queue):
            vrows("**Int** 14, **Wis** 16", ())


class RecipeSelfTest(unittest.TestCase):
    BODY = (
        "\n::: statblock\nPrice: 30 gp\nWeight: -\n:::\n\nThe liquid.\n\n"
        "**[Spontaneous Alchemy](ref/rule/spontaneous-alchemy) Recipe** (6 quicksilver + 10\n"
        "realgar)/distillation; **Craft DC** 20\\\n"
        "**Time** 10 minutes; **Tools** [retort](ref/eq-misc/retort); **Type** alchemical tool\n"
    )

    def test_a_recipe_becomes_an_untitled_block_and_the_link_moves_onto_the_recipe(self):
        new = convert_variants(self.BODY, plan_recipe)
        self.assertTrue(new.endswith(
            "::: statblock\nSpontaneous Alchemy Recipe: [(6 quicksilver + 10 realgar)/distillation](ref/rule/spontaneous-alchemy)\n"
            "Craft DC: 20\nTime: 10 minutes\nTools: [retort](ref/eq-misc/retort)\nType: alchemical tool\n:::\n"
        ), new)
        self.assertEqual(classify_variant(plan_recipe, new), "already")

    def test_a_wrapped_label_and_the_craft_dc_split_read_as_printed(self):
        wrapped = self.BODY.replace("**Craft DC**", "**Craft\nDC**")
        self.assertIn("Craft DC: 20\n", convert_variants(wrapped, plan_recipe))
        unlinked = self.BODY.replace("**[Spontaneous Alchemy](ref/rule/spontaneous-alchemy) Recipe**", "**Spontaneous Alchemy Recipe**")
        self.assertIn("Spontaneous Alchemy Recipe: (6 quicksilver + 10 realgar)/distillation\n", convert_variants(unlinked, plan_recipe))
        poison = self.BODY.replace("**Craft DC** 20", "**Craft** DC 13")
        self.assertIn("Craft: DC 13\n", convert_variants(poison, plan_recipe))

    def test_what_the_rule_does_not_cover_queues(self):
        for reason, body in {
            "label-twice": self.BODY.replace("**Time** 10 minutes", "**Craft DC** 9"),
            "linked-label": self.BODY.replace("realgar)/distillation;", "[realgar](ref/eq-misc/realgar))/distillation;"),
            "unlabelled-line": self.BODY.replace("**Time**", "Time"),
        }.items():
            with self.subTest(reason=reason):
                with self.assertRaises(Queue) as caught:
                    convert_variants(body, plan_recipe)
                self.assertEqual(caught.exception.reason, reason)


class TearawaySelfTest(unittest.TestCase):
    BODY = (
        "\n::: statblock\nPrice: 1 gp\nWeight: 4 lbs.\nCategory: Clothing\n:::\n\nAn outfit.\n\n"
        "**Tear-away clothing**\\\n**Price** +5 gp; **Weight** -\\\n**Category** Clothing\n\nSneaks know it.\n"
    )

    def test_the_variant_becomes_a_titled_block_after_the_entrys_own(self):
        new = convert_variants(self.BODY, plan_tearaway)
        self.assertIn(
            '::: statblock\ntitle = "Tear-away clothing"\nPrice: +5 gp\nWeight: -\nCategory: Clothing\n:::\n\nSneaks know it.\n', new
        )
        self.assertEqual(classify_variant(plan_tearaway, new), "already")

    def test_without_a_block_before_it_the_file_queues_because_the_variant_would_be_the_first_price(self):
        with self.assertRaises(Queue) as caught:
            convert_variants("\nAn outfit.\n\n" + self.BODY.split("An outfit.\n\n")[1], plan_tearaway)
        self.assertEqual((caught.exception.reason, caught.exception.detail), ("no-lead-row", "Price"))


class IntelligentSelfTest(unittest.TestCase):
    BODY = (
        "\n::: statblock\nAura: strong\nCL: 8th\n:::\n\nAn item.\n\n### Statistics\n\n"
        "**Alignment** neutral; **Ego** 14\\\n**Senses** 120 ft., [darkvision](ref/rule/darkvision)\\\n"
        "**Int** 14, **Wis** 16, **Cha** 14\\\n**Communication** telepathy (Aklo, Common)\\\n"
        "**[Special Purpose](ref/rule/special-purpose-items)** defeat dwarves\n"
    )

    def test_the_statistics_become_one_untitled_block_under_the_heading(self):
        new = convert_variants(self.BODY, plan_intelligent, ("Wis", "Cha"))
        self.assertTrue(new.endswith(
            "### Statistics\n\n::: statblock\nAlignment: neutral\nEgo: 14\nSenses: 120 ft., [darkvision](ref/rule/darkvision)\n"
            "Int: 14\nWis: 16\nCha: 14\nCommunication: telepathy (Aklo, Common)\n"
            "Special Purpose: [defeat dwarves](ref/rule/special-purpose-items)\n:::\n"
        ), new)
        self.assertEqual(classify_variant(plan_intelligent, new), "already")

    def test_a_list_line_without_a_label_queues_and_a_paragraph_elsewhere_is_not_touched(self):
        with self.assertRaises(Queue) as caught:
            convert_variants(self.BODY.replace("defeat dwarves", "defeat dwarves\\\n3/day-fly"), plan_intelligent, ("Wis", "Cha"))
        self.assertEqual(caught.exception.reason, "unlabelled-line")
        self.assertEqual(classify_variant(plan_intelligent, self.BODY.replace("### Statistics", "### Details")), "already")


class IounSelfTest(unittest.TestCase):
    BODY = (
        "\n::: statblock\nAura: moderate abjuration\nCL: 12th\nPrice: 10,000 gp\n:::\n\n#### Description\n\nA stone.\n\n"
        "#### Construction\n\n**Requirements** [Craft Wondrous Item](ref/feat/craft-wondrous-item),\n"
        "[resistance](ref/spell/resistance), creator must be 12th level; **Cost** 5,000 gp\n\n"
        "### Flawed Ioun Stone\n\n**Price** 6,000 gp\\\nThis stone grants a bonus.\n"
    )

    def test_the_construction_under_four_hashes_becomes_a_block_and_the_flawed_price_stays(self):
        new = convert_variants(self.BODY, plan_ioun)
        self.assertIn(
            "#### Construction\n\n::: statblock\nRequirements: [Craft Wondrous Item](ref/feat/craft-wondrous-item), "
            "[resistance](ref/spell/resistance), creator must be 12th level\nCost: 5,000 gp\n:::\n\n### Flawed Ioun Stone\n\n"
            "**Price** 6,000 gp\\\nThis stone grants a bonus.\n",
            new,
        )
        self.assertEqual(classify_variant(plan_ioun, new), "already")
        self.assertEqual(classify_variant(plan_ioun, self.BODY.replace("#### Construction", "#### Making")), "already")


class SpellbookSelfTest(unittest.TestCase):
    BODY = (
        "\n### Level 11 Evoker\n\n_A white cover._\n\n"
        "**Opposition** Illusion, necromancy\\\n**Protection** [Fire trap](ref/spell/fire-trap) (DC 19). The edges are warded.\\\n"
        "**Value** 2,300 gp (3,300 gp with the preparation ritual)\n\n#### Spells\n\n- 1st-[shield](ref/spell/shield)\n"
    )

    def test_the_three_rows_become_one_block_and_a_sentence_protection_is_kept(self):
        new = convert_variants(self.BODY, plan_spellbook)
        self.assertIn(
            "_A white cover._\n\n::: statblock\nOpposition: Illusion, necromancy\n"
            "Protection: [Fire trap](ref/spell/fire-trap) (DC 19). The edges are warded.\n"
            "Value: 2,300 gp (3,300 gp with the preparation ritual)\n:::\n\n#### Spells\n",
            new,
        )
        self.assertEqual(classify_variant(plan_spellbook, new), "already")

    def test_another_label_queues(self):
        with self.assertRaises(Queue) as caught:
            convert_variants(self.BODY.replace("**Value**", "**Worth**"), plan_spellbook)
        self.assertEqual((caught.exception.reason, caught.exception.detail), ("unexpected-label", "Worth"))


class FigurineSelfTest(unittest.TestCase):
    BODY = (
        "\n::: statblock\nAura: varies\nCL: varies\n:::\n\n**Ivory Goats:** These come in threes.\n\n"
        "- **The Goat of Travail:** A mount.\n\n"
        "**CL** 11th; Craft Wondrous Item, _[animate objects](ref/spell/animate-objects)._\n"
    )

    def test_the_cl_tail_becomes_a_one_row_block_as_printed(self):
        new = convert_variants(self.BODY, plan_figurine)
        self.assertTrue(new.endswith(
            "::: statblock\nCL: 11th; Craft Wondrous Item, _[animate objects](ref/spell/animate-objects)._\n:::\n"
        ), new)
        self.assertEqual(classify_variant(plan_figurine, new), "already")

    def test_without_the_entrys_own_cl_row_before_it_the_file_queues(self):
        with self.assertRaises(Queue) as caught:
            convert_variants("\n" + self.BODY.split("\n\n", 2)[2], plan_figurine)
        self.assertEqual((caught.exception.reason, caught.exception.detail), ("no-lead-row", "CL"))


class CostSelfTest(unittest.TestCase):
    BOW = (
        "\n::: statblock\nCost: 125 gp (+0)\nWeight: 2 lbs.\n:::\n\n### Composite Bows\n\nAll composite bows have a rating.\n\n"
        "**Cost** 225 gp (+1), 325 gp (+2)\n"
    )
    FLESH = (
        "\n::: statblock\nPrice: gp\n:::\n\n### Creation Requirements\n\n**Cost** 1,000 gp\\\n"
        "[Fleshwarper](ref/feat/fleshwarper), Craft (alchemy) 8 ranks; Heal DC 18; **Elixir Cost** 250 gp\n"
    )

    def test_a_bow_cost_list_becomes_a_one_row_block_after_the_entrys_own_cost(self):
        new = convert_variants(self.BOW, plan_cost)
        self.assertTrue(new.endswith("::: statblock\nCost: 225 gp (+1), 325 gp (+2)\n:::\n"), new)
        with self.assertRaises(Queue) as caught:  # a file whose own block has no Cost row
            convert_variants(self.BOW.replace("Cost: 125 gp (+0)\n", ""), plan_cost)
        self.assertEqual((caught.exception.reason, caught.exception.detail), ("no-lead-row", "Cost"))

    def test_a_composite_bow_without_an_own_block_queues_because_the_variant_would_be_first(self):
        body = (
            "\n### Composite longbow +0\n\n**Cost** 100 gp **Weight** 3 lbs.\\\n**Damage** 1d6\n\n"
            "### Composite longbow +1\n\n**Cost** 200gp\n"
        )
        with self.assertRaises(Queue) as caught:
            convert_variants(body, plan_cost)
        self.assertEqual(caught.exception.reason, "no-lead-row")

    def test_the_fleshcraft_cost_is_the_block_and_the_line_without_a_label_stays_below(self):
        new = convert_variants(self.FLESH, plan_cost)
        self.assertTrue(new.endswith(
            "### Creation Requirements\n\n::: statblock\nCost: 1,000 gp\n:::\n\n"
            "[Fleshwarper](ref/feat/fleshwarper), Craft (alchemy) 8 ranks; Heal DC 18; **Elixir Cost** 250 gp\n"
        ), new)
        self.assertEqual(classify_variant(plan_cost, new), "already")


class SourcesSelfTest(unittest.TestCase):
    names = {
        "Bestiary": "bestiary",
        "Ultimate Equipment": "ultimate-equipment",
        "Core Rulebook": "core-rulebook",
        "PRPG Core Rulebook": "core-rulebook",
        "Pathfinder #93: Forge": "pathfinder-93-forge",
    }

    def plan(self, front: str, body: str, kind: str = "creature", zones=("statistics", "construction")):
        return plan_sources(front + body, kind, self.names, zones)

    def test_a_creature_citation_leaves_the_statistics_and_the_agreeing_row_stays(self):
        status, _, text = self.plan(SOURCES_FRONT, SOURCES_CREATURE)
        self.assertEqual(status, "converted")
        self.assertEqual(text, SOURCES_FRONT + SOURCES_CREATURE.replace("**Sources:** Bestiary pg 10\\\n", "", 1))
        self.assertEqual(self.plan(text.split("\n\n")[0] + "\n\n" + text.split("\n\n", 1)[1], "")[0], "skipped")
        self.assertEqual(plan_sources(text, "creature", self.names, ("statistics", "construction"))[0], "skipped")

    def test_an_item_citation_in_construction_gains_rows_after_the_old_ones(self):
        narrow = ("statistics", "construction")
        status, _, text = self.plan(SOURCES_ITEM_FRONT, SOURCES_ITEM, "item", narrow)
        self.assertEqual(status, "converted")
        self.assertIn(
            '[[sources]]\npublication = "bestiary"\npage = "10"\n'
            '[[sources]]\npublication = "ultimate-equipment"\npage = "302"\n'
            '[[sources]]\npublication = "core-rulebook"\npage = "525"\n\n[fields]',
            text,
        )
        self.assertEqual(text.split("+++\n", 2)[2], SOURCES_ITEM.replace("**Sources:** Ultimate Equipment pg 302, PRPG Core Rulebook pg 525\\\n", "", 1))
        self.assertEqual(plan_sources(text, "item", self.names, narrow)[0], "skipped")  # idempotent
        # The variant line is outside the narrow zones; in every zone (the default) it conflicts on the page.
        self.assertEqual(self.plan(text, "", "item", narrow)[0], "skipped")
        self.assertEqual(plan_sources(text, "item", self.names)[0], "queue:sources-page-conflict")
        self.assertEqual(sources_leftovers(SOURCES_ITEM, "item"), [])
        # A variant line whose page a row holds moves like any other.
        agreeing = SOURCES_ITEM.replace("Ultimate Equipment pg 99", "Ultimate Equipment pg 302")
        moved = plan_sources(text.split("+++\n", 2)[0] + "+++\n" + text.split("+++\n", 2)[1] + "+++\n" + agreeing, "item", self.names)
        self.assertEqual(moved[0], "converted")
        self.assertNotIn("**Sources:**", moved[2])

    def test_the_rows_go_before_expanded_in_and_into_a_front_without_rows(self):
        head = (
            '+++\nid = "ref/magic-wondrous/x"\nkind = "item"\ntitle = "X"\n'
            'source_ids = ["bestiary", "ultimate-equipment"]\n'
            'provenance = [\n  { dataset = "d", record = "x", path = "j.json" },\n]\n'
        )
        tail = "\n[fields]\nkind = \"item\"\n+++\n"
        item = "\n### Construction\n\n**Sources:** Ultimate Equipment pg 5\\\n**Cost** 5 gp\n"
        row = '[[sources]]\npublication = "ultimate-equipment"\npage = "5"\n'
        with_expanded = head + '[[expanded_in]]\npublication = "pathfinder-93-forge"\n' + tail
        text = self.plan(with_expanded, item, "item")[2]
        self.assertTrue(text.startswith(head + row + "[[expanded_in]]\n"), text)
        text = self.plan(head + tail, item, "item")[2]
        self.assertTrue(text.startswith(head + row + "\n[fields]\n"), text)
        after = head + '[[sources]]\npublication = "bestiary"\npage = "1"\n[[expanded_in]]\npublication = "pathfinder-93-forge"\n' + tail
        text = self.plan(after, item, "item")[2]
        self.assertIn('page = "1"\n' + row + "[[expanded_in]]", text)
        self.assertEqual(self.plan(head + tail.replace("[fields]", "[other]"), item, "item")[0], "queue:sources-front-shape")

    def test_a_paragraph_of_one_line_goes_with_one_blank_and_a_last_line_loses_the_break_before_it(self):
        front = SOURCES_FRONT
        own = "\n**Challenge rating:** 2\n\n**Sources:** Bestiary pg 10\n\n**Armor class:** 13\n"
        self.assertEqual(self.plan(front, own)[2], front + "\n**Challenge rating:** 2\n\n**Armor class:** 13\n")
        end = "\n**Challenge rating:** 2\n\n**Sources:** Bestiary pg 10\n"
        self.assertEqual(self.plan(front, end)[2], front + "\n**Challenge rating:** 2\n")
        last = "\n**Challenge rating:** 2\\\n**Sources:** Bestiary pg 10\n\n**Armor class:** 13\n"
        self.assertEqual(self.plan(front, last)[2], front + "\n**Challenge rating:** 2\n\n**Armor class:** 13\n")
        wrapped = "\n**Challenge rating:** 2\n\n**Sources:** Bestiary pg 10, Ultimate\nEquipment pg 5\\\n**Type:** animal\n"
        status, _, text = self.plan(front, wrapped)
        self.assertEqual((status, text.endswith("\n**Type:** animal\n")), ("converted", True))
        self.assertIn('publication = "ultimate-equipment"\npage = "5"', text)

    def test_two_lines_for_one_book_make_one_row_when_the_pages_agree(self):
        body = "\n**Sources:** Ultimate Equipment pg 5\\\n**A:** 1\n\n**Sources:** Ultimate Equipment pg 5\\\n**B:** 2\n"
        status, _, text = self.plan(SOURCES_FRONT, body)
        self.assertEqual(status, "converted")
        self.assertEqual(text.count("[[sources]]"), 2)
        self.assertEqual(text.split("+++\n", 2)[2], "\n**A:** 1\n\n**B:** 2\n")

    def test_what_the_rule_does_not_cover_is_queued_and_the_file_stays(self):
        cases = [
            ("sources-unmapped-book", "**Sources:** Dragon Magazine pg 5\\\n**A:** 1"),
            ("sources-unparsed", "**Sources:** Blood of the Coven\\\n**A:** 1"),
            ("sources-unparsed", "**Sources:** PRPG Core Rulebook pg. 159, 163\\\n**A:** 1"),
            ("sources-unparsed", "**Sources:** Bestiary pg 5, 6\\\n**A:** 1"),
            ("sources-unmapped-book", "**Sources:** _Bestiary_ pg 5\\\n**A:** 1"),
            ("sources-book-not-in-source-ids", "**Sources:** Pathfinder #93: Forge pg 5\\\n**A:** 1".replace("Pathfinder #93: Forge", "Pathfinder \\#93: Forge")),
            ("sources-page-conflict", "**Sources:** Bestiary pg 11\\\n**A:** 1"),
            ("sources-page-conflict", "**Sources:** Ultimate Equipment pg 5, Ultimate Equipment pg 6\\\n**A:** 1"),
            ("sources-shape", "**Sources:** Bestiary pg 10\\\n"),
            ("sources-shape", "Text **Sources:** Bestiary pg 10\n**Sources:** Bestiary pg 10\\\nline"),
        ]
        for reason, body in cases:
            with self.subTest(reason=reason, body=body):
                front = SOURCES_FRONT
                if reason == "sources-book-not-in-source-ids":
                    front = SOURCES_FRONT.replace(', "pathfinder-93-forge"', "")
                if reason == "sources-shape" and body.startswith("Text"):
                    body = "A\\\nB **Sources:** Bestiary pg 10\\\nC\n\nD\n**Sources:** Bestiary pg 10\\\nE"
                    result = self.plan(front, "\n" + body + "\n")
                    self.assertEqual(result[0], "queue:sources-shape")  # a label inside a line is not the label of a line
                    continue
                text = front + "\n" + body + "\n"
                status, _, new = plan_sources(text, "creature", self.names)
                self.assertEqual((status, new), ("queue:" + reason, text))
        # The same book twice with other pages, and a row with no page.
        no_page = SOURCES_FRONT.replace('page = "10"\n', "")
        self.assertEqual(self.plan(no_page, "\n**Sources:** Bestiary pg 10\\\n**A:** 1\n")[0], "queue:sources-page-conflict")

    def test_a_printed_page_is_covered_by_a_row_that_holds_it_and_never_adds_a_row_for_a_known_book(self):
        self.assertTrue(page_covers("13-14", "14") and page_covers("11, 13-14", "13") and page_covers("10", "10"))
        self.assertFalse(page_covers("13", "14") or page_covers("11, 13", "12") or page_covers(None, "1"))
        self.assertFalse(page_covers("13-14", "14-15"))
        rows = lambda *pages: SOURCES_FRONT.replace(  # noqa: E731
            '[[sources]]\npublication = "bestiary"\npage = "10"\n',
            "".join(f'[[sources]]\npublication = "bestiary"\npage = "{page}"\n' for page in pages),
        )
        body = "\n**Sources:** Bestiary pg 11\\\n**A:** 1\n"
        converted = self.plan(rows("10-12"), body)
        self.assertEqual(converted[0], "converted")
        self.assertEqual(converted[2].count("[[sources]]"), SOURCES_FRONT.count("[[sources]]"))  # no row added
        self.assertEqual(self.plan(rows("10", "11"), body)[0], "converted")  # a second row holds it
        self.assertEqual(self.plan(rows("10", "12"), body)[0], "queue:sources-page-conflict")

    def test_a_page_range_and_an_escaped_hash_read(self):
        self.assertEqual(
            parse_sources_text("Bestiary pg 10-12, Pathfinder \\#93: Forge pg 4", self.names),
            [("Bestiary", "bestiary", "10-12"), ("Pathfinder #93: Forge", "pathfinder-93-forge", "4")],
        )
        # A name that is the start of a longer one must not match it.
        names = dict(self.names, **{"Bestiary 2": "bestiary-2"})
        self.assertEqual(parse_sources_text("Bestiary 2 pg 5", names), [("Bestiary 2", "bestiary-2", "5")])

    def test_zones_follow_the_statistics_region_and_the_construction_paragraph(self):
        lines = SOURCES_CREATURE.split("\n")
        zones = sources_zones(lines, "creature")
        found = [zones[i] for i, line in enumerate(lines) if line.startswith(SOURCES_LABEL)]
        self.assertEqual(found, ["statistics", "variant"])
        lines = SOURCES_ITEM.split("\n")
        zones = sources_zones(lines, "item")
        found = [zones[i] for i, line in enumerate(lines) if line.startswith(SOURCES_LABEL)]
        self.assertEqual(found, ["construction", "variant"])
        # A lead paragraph that is still prose, before any stat block, is the statistics zone.
        bare = "\n**Price** 1 gp\\\n**Sources:** Bestiary pg 1\\\n**Weight** 1 lb.\n"
        self.assertEqual(sources_zones(bare.split("\n"), "item")[3], "statistics")

    def test_the_proof_rejects_a_front_matter_or_body_that_moved_by_more_than_the_citation(self):
        body = SOURCES_ITEM
        status, _, text = self.plan(SOURCES_ITEM_FRONT, body, "item")
        front, new_body = split_front(text)
        removed = ["**Sources:** Ultimate Equipment pg 302, PRPG Core Rulebook pg 525\\"]
        added = [("ultimate-equipment", "302"), ("core-rulebook", "525")]
        prove_sources(SOURCES_ITEM_FRONT, front, body, new_body, removed, added, self.names)  # the real one
        broken = [
            (front.replace('page = "302"', 'page = "303"'), new_body, added),
            (front.replace('page = "10"', 'page = "11"'), new_body, added),
            (front.replace('title = "X"', 'title = "Y"'), new_body, added),
            (SOURCES_ITEM_FRONT, new_body, []),
            (front, new_body, added + [("bestiary", "1")]),
            (front, new_body.replace("Text.", "Text!"), added),
            (front, new_body.replace("**Cost** 1,250 gp", "**Cost** 1,250 gp."), added),
            (front, new_body.replace("### Construction", "### Construct"), added),
            (front, body.replace("**Sources:** Ultimate Equipment pg 302, PRPG Core Rulebook pg 525\\\n", "", 1).replace("\n\n### Variant", "\n### Variant"), added),
            (front, body, added),
        ]
        for number, (new_front, new_text, rows) in enumerate(broken):
            with self.subTest(number=number):
                with self.assertRaises(ProofFailed):
                    prove_sources(SOURCES_ITEM_FRONT, new_front, body, new_text, removed, rows, self.names)

    def test_a_run_moves_the_citation_then_the_passes_it_unblocked_convert(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "entries/magic-wondrous").mkdir(parents=True)
            (root / "scripts").mkdir()
            (root / "publications.toml").write_text(SOURCES_PUBLICATIONS, encoding="utf-8")
            for rel, _, _, pairs in PRINT_FIXES + ANCHOR_EDITS:
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / rel).write_text(ITEM_FRONT + "".join(pair[0] for pair in pairs), encoding="utf-8")
            path = root / "entries/magic-wondrous/x.md"
            path.write_text(SOURCES_ITEM_FRONT + SOURCES_ITEM.replace("pg 99", "pg 302"), encoding="utf-8")
            sink = open(os.devnull, "w")
            self.addCleanup(sink.close)
            self.assertEqual(run(root, "check", ["sources"], None, sink), 1)
            self.assertEqual(run(root, "write", ["sources", "item"], None, sink), 0)
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("**Sources:** Ultimate Equipment pg 302", text)
            self.assertIn("::: statblock\nRequirements: [Craft Wondrous Item](ref/feat/craft-wondrous-item)\nCost: 1,250 gp\n:::", text)
            self.assertEqual(run(root, "check", ["sources", "item"], None, sink), 0)
            tsv = (root / REVIEW_TSV).read_text(encoding="utf-8")
            self.assertNotIn("raw-sources-line", tsv)
            self.assertNotIn("**Sources:**", text)
            before = path.read_bytes()
            self.assertEqual(run(root, "write", ["sources", "item"], None, sink), 0)
            self.assertEqual(before, path.read_bytes())


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
