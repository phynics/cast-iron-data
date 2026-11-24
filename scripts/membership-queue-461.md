# The membership queue (phynics/cast-iron#461)

`scripts/membership-queue-461.tsv` lists every book membership that the cleanup of #461 has to
decide, with the evidence the screen found and the verdict once someone has decided. It never holds
book text, PDF names or paths. Cite books by title and page only.

| File | What it does |
|---|---|
| `membership-screen.py` | Reads the owner's PDFs; finds memberships whose book may not print the entry. `--status-out` also writes every screened membership. Only the person with the PDFs runs it |
| `membership-queue-461.py` | Keeps the queue complete from the corpus, the old queue and a fresh screen (`--screen-all`). `--check` needs no screen and proves the queue against the corpus |
| `membership-apply.py` | Applies the verdicts `remove` and `cite`. `--check` lists what is still pending |
| `expansion-credits-apply.py` | `page`, `add` and `expanded_in` actions (#459) |
| `hub-topic-lists-461.py` | S10: puts the dropped `subtopics` list of the 14 navigation hubs back as `::: entry-link` blocks (`--list`, `--apply`, `--check`; needs a checkout of the pinned dataset) |
| `hub-verdicts-461.py` | S10: derives the `hub-link` and `hub-no-evidence` verdicts of the hub rows, writes them and the reviewed rows of `membership-verdicts-461-s10.tsv` into the queue (`--write`, `--check`), and refreshes `in_warning`, `body_line` and `group` after the apply scripts (`--refresh-warning`) |
| `faith-technique-links-461.py` | S10: replaces the quoted divine fighting technique of a faith with a link to its section of the feat entry (`--check`) |
| `membership-verdicts-461-s10.tsv` | The reviewed S10 verdicts that the scripts do not derive: cites, listed-link removals, the reads, the faith removals |
| `membership-citation-audit-461.tsv` | Releases a `[[sources]]` row whose membership goes (class `wrong-credit`, `family-ref`, `mention`) |

## What is in the queue

A row is a (book, entry) pair. It is in the queue when it is

1. in the `corpus-check` warning: the book is in `source_ids`, is not the first book, and the entry
   has no `[[sources]]` row for it (`uncited_memberships` in the checker),
2. a **figurine** membership: the 23 Figurine of Wondrous Power variants carry the same non-first
   books with identical rows, so the warning does not see them, and the screen passes them because
   it drops the parenthetical (the variant name) from the title,
3. in the screen's queue (`cite-off`, `review`, `hub-keep`, family leaks), or
4. an old row. Old rows stay for good: a decided row is the record of the decision.

The screen counts a title on two or more pages of a book as printed, and generic titles (Medium,
Languages, Rogue, Dwarf) always pass that test. For a hub or a generic title the `status` column
means nothing; the `group` says how to decide the row.

## Groups

`group` has one value per row, the first that fits. It is a function of the entry, so
`membership-queue-461.py --check` recomputes it. The `ruling` column names the owner ruling that
decides a row with no verdict (`hub-design-a`, `faith-link`); nothing in the queue waits for a
ruling any more.

| Group | What it is | How it is decided | Slice |
|---|---|---|---|
| `standard-racial-trait` | A `racial_trait` of one of the 7 core races with `alternate = false` (Medium, Languages, Defensive Training, ...) that carries all the books of its race | Read the book's section for the race, once per race and book. A book that does not print the trait there: `remove`, evidence `race-section-read-no-trait` (as in batches 1 and 2) | S1 dwarf, elf; S2 gnome, half-elf; S3 half-orc, halfling, human |
| `figurine` | A Figurine of Wondrous Power variant, in any non-first book | Read the book's figurine page: keep the variants it prints, remove the rest (`wrong-credit` or `family-ref` rows in the audit file) | S4a, S4b (seven books each, in book order) |
| `single-entry` | A spell, item, trait, creature, affliction, skill, class option, archetype or feat | Per entry: `remove`, `family-ref`, or `cite` | S5 |
| `class-hub` | An `ref/class/*` entry, or one of the 11 `ref/rule/class-*/*` mirror entries | Owner ruling 1: keep a book only when it prints a section of the class body itself (alternate capstones; the Archetypes introduction, Advanced Player's Guide p. 72) and `cite` its page. A book that only adds an archetype goes: the archetype entry carries that book | S6 (A-M), S7 (N-Z), S8 (mirrors) |
| `race-hub` | An `ref/race/*` entry | Owner ruling 2: remove a book whose race material has its own entries (Dwarf in Heroes of the Wild); a book that prints only a favored class line becomes an `expanded_in` credit (Half-Orc in Ultimate Wilderness p. 31) | S9 |
| `faith-excerpt` | A `ref/faith/*` entry whose body quotes a section (the deity's Divine Fighting Technique) under a `**Source**` line that names the book | Owner ruling of 2026-11-24 (`ruling = faith-link`): replace the quoted section with a link to the technique's own entry (for example Lamashtu's Carving, Divine Anthology pp. 28-31); the book then leaves the faith. Where no entry for the technique exists, report it instead of guessing | S10 |
| `hub-cited` | Another `rule` entry (hub, ability) whose body has a `**Source**` line that names the book | `cite` with the line's page, after one check against print. `--convert-body` turns the line into the row | S10 |
| `link-only-hub` | Another `rule` entry without such a line: Gamemastery, Specific Campaign Types, Specific Rulesets, Optional Subsystems, Advanced GM Topics. One or two sentences and links | Owner ruling of 2026-11-24, design (a) (`ruling = hub-design-a`): a hub keeps only its home book. The 14 navigation hubs first get their topic lists back as `::: entry-link` blocks (137 blocks); then their non-first books go: removed where a listed entry carries the book (`hub-link <target>`) or nothing does (`hub-no-evidence`), cited where the body prints a section, read in print where the design table says so. The muted book label on each listed row is an app change. The hubs' home book is post-v1 (phynics/cast-iron-data#277), and so are the 545 other dropped subtopic lists (#276) | S10 |
| `no-pdf` | Any other entry, in a book that is not among the owner's PDFs (Adventure Path volumes, Player's Guides, one blog post). A `rule` entry there is `no-pdf` too, unless it is a collector hub that no body line cites | Owner ruling 4: keep with a row that carries the page of the corpus's own body or dataset citation. Evidence `unverified-no-pdf`, so a later check can find them | S12 |

The three structural groups (standard racial traits, class hubs, race hubs) come before `no-pdf`:
the elf traits in Pathfinder #124 and the class hubs in Pathfinder #101 are decided by their rules,
with or without a PDF.

At S0 (data `main` `dc1a2e653`; the warning is 1,471 memberships in 355 entries):

| Group | In the warning | Rows without a verdict (all) |
|---|---:|---:|
| `standard-racial-trait` | 638 | 638 |
| `class-hub` | 410 | 410 |
| `race-hub` | 147 | 147 |
| `faith-excerpt` | 16 | 22 |
| `hub-cited` | 35 | 51 |
| `link-only-hub` | 77 | 93 |
| `single-entry` | 104 | 314 |
| `no-pdf` | 44 | 44 |
| `figurine` | 0 | 304 |

A row **outside the warning** (it has a row already, or it is a first book) is `S11`, whatever its
group: `cite-off` rows need a page correction (`page` action of `expansion-credits-apply.py`),
`review` rows need a reading. S11 runs after the running slice of #215 has merged, because both edit
`[[sources]]` pages. A decided row has slice `done` (batches 1-4 and #98) or `S0` (decided by the
rules of the queue script).

## Verdicts and actions

| `verdict` | Meaning | Applied by |
|---|---|---|
| `remove` | The book does not print the entry. Out of `source_ids`, out of the book's placements. The `[[sources]]` row goes only when the audit file releases it | `membership-apply.py` |
| `cite` | The book prints the entry and stays. The entry gets a `[[sources]]` row with `print_page` (the evidence is in `evidence`). `--convert-body` also takes the book out of a body `**Source**` line | `membership-apply.py` |
| `expands` | The book expands the entry and the text has no entry of its own: an `[[expanded_in]]` credit | `expansion-credits-apply.py` |
| `keep` | The book prints the entry and the entry has its row already. Nothing to apply; `membership-apply.py --check` reports a `keep` whose row is missing | none |
| `resolved` | Another change settled the pair: the book is out of `source_ids` (`out-of-source-ids`), or it is out and the entry credits it in `expanded_in` (`expanded-in-row`) | none |

`print_page` is the printed page that decides the row, and `evidence` is a short code for what the
print check found (the codes are in the docstring of `membership-screen.py`). New codes of S0:
`title-on-cited-page` (keep: the screen found the title on the cited page itself; for a title with a
parenthetical, the parenthetical as well), `out-of-source-ids`, `expanded-in-row`.
Two codes record a standard racial trait whose book does not print the trait text:
`race-section-read-no-trait` (the book's section for the race was read in print and prints only
alternate racial traits with "replaces" lines, favored class options, archetypes or background) and
`no-pdf-structural-rule` (owner ruling of 2026-11-24 on #461: the book is not among the owner's PDFs,
the corpus has no page for it, and other print evidence shows that the book prints only alternate
traits; `print_page` is the page of that other evidence, for example Heroes from the Fringe p. 11
citing Pathfinder #124 p. 79 for the Spiresworn elves; the same code covers the class hubs of
Pathfinder #101: the corpus lists that volume on no archetype or class option entry of those
classes and has no page for it, so `print_page` is `none`). `class-options-only` records a class hub whose book prints archetypes, favored class
options, feats, spells or class options for the class and no section of the class body (owner
ruling 1 of 2026-11-23; S6 of #461). `generic-archetype-intro` records the Advanced Player's Guide
on a class hub of a class it does not print (owner ruling of 2026-11-24): its p. 72 Archetypes
introduction is generic and names only the core classes, so the book stays only on the six core
classes. `hub-link <target>`, `hub-no-evidence <record>` and `listed-link <target>` record the design (a) verdicts
of S10 (a hub keeps only its home book): a listed entry carries the book, no listed entry does, or a
sentence or table row of the page links an entry of that book. `copied-generic-section` records a book whose only trace on the entry was a source line over text that the entry copied (generic text, or a sentence that names other entries); the line and the text left the body together with the book (owner ruling of 2026-11-24, as the Moon Hag in S5). `technique-linked` records a faith whose
quoted technique is a link now. `expansion-no-entry` is a `expands` row whose text no entry holds.
`membership-apply.py` lets a `hub-keep` row go only with `hub-link`, `listed-link` or `hub-no-evidence`
evidence. A removal still
needs the print check, a page and the audit row that its class asks for. The queue is a list of
hypotheses, not proof.
A book can print an entry on its inside cover, which has no number. The page is then `inside cover`,
the form the corpus uses already, and `membership-apply.py` accepts it as a page.

S11 (rows the warning cannot see) records its verdicts in `membership-verdicts-461-s11.tsv`, one row
per (book, entry), and `membership-verdicts-461-s11.py` writes them into the queue, the audit file
and `expansion-credits-461-s11.tsv` (the `page` actions that `expansion-credits-apply.py` applies; a
row without a page gets its page). Verdict `page` is for an entry outside the queue. New evidence codes:
`page-corrected` (the book prints the entry on another page than the row said; `print_page` is the
printed page: the page of the item's description, or of the table when the book has no description),
`page-confirmed` (the cited page prints the entry), `home-book-kept` (the first book of a hub stays, owner ruling 3 of 2026-11-24, home books are post-v1 in phynics/cast-iron-data#277). Three first-book
removals whose new first book is not among the owner's PDFs (Conditional Curse, Swampseer Poison, Yak) stay undecided with the evidence note `waits for S12`
(owner ruling of 2026-11-24). `faith-unique-spell-rules-461-s11.py` removes the copied spell rule from two faith pages.

## Slices

Each slice records its verdicts in the queue (`print_page`, `evidence`), applies them with the apply
scripts, runs `corpus-fmt --check` and `corpus-check`, and states the warning count before and after.
Slices touch only `source_ids`, `[[sources]]`, `[[expanded_in]]` and placements.

| Slice | Rows | Order |
|---|---|---|
| S0 | Tooling and this queue. No entry changes | 1 |
| S1, S2, S3 | Standard racial traits: no ruling needed, about 640 pairs | 2 |
| S4a, S4b | Figurines (owner-flagged) | 3 |
| S5 | Single entries. Take the 17 traits book by book after #215 has passed those books | 4 |
| S6, S7, S8 | Class hubs and mirrors, under ruling 1 | 5 |
| S9 | Race hubs, under ruling 2 | 5 |
| S10 | `hub-cited` rows (cite); `link-only-hub` rows (restore the lists of the 14 navigation hubs, then remove, cite or read: design (a)); `faith-excerpt` rows (replace the section with a link) | 5 |
| S11 | Rows outside the warning: page corrections, `review` rows | 6 |
| S12 | Books without an owner PDF, under ruling 4 | 7 |

After S12 the warning is 0. An app PR then turns it into an error, and the issue closes when every
row of the queue has a verdict (figurines and page rows included).

## Regenerate the queue

```
# 1. screen the PDFs (needs pdftotext and the owner's PDFs; writes text outside any repository)
python3 scripts/membership-screen.py <corpus> --pdf-dir <pdfs> --text-cache <dir> \
    --out screen-queue.tsv --status-out screen-all.tsv
# 2. merge: warning pairs, figurines, groups, slices, verdicts kept
python3 scripts/membership-queue-461.py <corpus> --screen-all screen-all.tsv
# 3. prove the queue against the corpus (no PDFs needed; run it after every slice)
python3 scripts/membership-queue-461.py <corpus> --check
# 4. after a slice: the apply scripts have nothing left to do
python3 scripts/membership-apply.py <corpus> --check
```

Tests: `python3 scripts/test-membership-apply.py`, `python3 scripts/test-membership-queue-461.py`.
