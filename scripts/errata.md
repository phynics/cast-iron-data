# Errata review file (`scripts/errata.tsv`)

The shared record of every place where the corpus text and the owner's printing of a book are
compared and the result needs a reason (phynics/cast-iron-data#309, owner rulings of 2026-11-24).
`scripts/errata.py --check` validates it; the data workflow runs that check.

## The rule it records

The corpus follows the owner's printing of each book, plus recorded errata. A difference from print
is an import error or a paraphrase unless errata is shown. A misprint is recorded and corrected.

An errata marker (in the import record or elsewhere) is evidence only when it is checked against a
**Paizo errata document** for the book. Cite such a document as "Paizo errata for <book title>":
never by address, file name or path. The printing is a property of the book, not of the row: write
"Ultimate Magic (second printing) p. 27" in review text, and the printing in the `printing` column.

## Columns

One row per `(entry, field)`, sorted by `(entry, field)`. Tab-separated, no tab or line break inside
a field, no leading or trailing white space.

| Column | Meaning |
|---|---|
| `entry` | The entry id, for example `ref/arc-bard/sound-striker`. The id never changes, so a row stays valid when a title does. |
| `field` | What differs: a feature anchor (`weird-words`), `title`, or another field name. |
| `book` | The publication id of the printed source (`publications.toml`). |
| `page` | The printed page (the number in the footer, not the PDF page). |
| `printing` | The printing of the owner's copy, as the front matter states it ("Second printing, January 2012"), or `Not stated` when the copy prints no printing line. |
| `printed_value` | The printed text, as one line, in the corpus's typography (straight quotes, `-` for a dash). It starts and ends where the compared span does: it may leave out the level phrase or the "This ability replaces" sentence that the entry holds as a label. |
| `kept_value` | The text the corpus keeps against print. Filled for `keep` and `misprint-fix`, empty for `print`. |
| `class` | Why the corpus and print differ: see below. |
| `evidence` | What the class rests on: "Paizo errata for <book title>", a later book that reprints the rule ("later book: <title> p. N"), print's own contradiction, or what was searched without a result. |
| `decision` | What the corpus holds: `print`, `keep` or `misprint-fix`. |
| `printed_sha256` | SHA-256 of `printed_value` after NFC and white space collapsed to single spaces (UTF-8). A script that finds another printed text for the row holds it again. |
| `note` | The competing value (what the import had), the ruling and its date, and anything a reader needs. May be empty. |

## Classes

- `import-error`: the import has a wrong value, a garbled or dropped text, an invented or inherited
  field, or a wrong page.
- `paraphrase`: the same rule and values, in other words or another order.
- `errata`: a Paizo errata document (or a later printing that the owner holds) changes the printed
  text, and the corpus keeps the changed text.
- `misprint`: print contradicts itself, a formula or the rest of the book; the corpus keeps the
  correct value and the row records the misprint.
- `unknown`: a real rule or name difference with no evidence either way.

## Decisions

| `decision` | The corpus holds | `kept_value` | Allowed `class` |
|---|---|---|---|
| `print` | the printed value | empty | `import-error`, `paraphrase`, `unknown` |
| `keep` | a value that differs from print | the kept text | `errata` only, and `evidence` starts with "Paizo errata for " or, when the library has no document for a later printing that the corpus follows (owner ruling 68, the Shifter), "Later printing of " |
| `misprint-fix` | the corrected value | the corrected text | `misprint` only |

A `print` row of class `unknown` is a ruling without evidence: a later errata document reopens it.
When the owner's copy is already the printing that a Paizo errata document brings the book to, the
print already includes that errata, so no row is needed for it.

## What `errata.py --check` verifies

The header; the number of fields; that every required field is filled; `class`, `decision` and the
pair; that `(entry, field)` is unique and the rows are sorted; that `book` is in `publications.toml`;
that `printed_sha256` matches `printed_value`; that the entry exists; and that the entry text (front
matter and body, links, emphasis and white space ignored, case folded) contains `printed_value` for
`print` and `kept_value` for `keep` and `misprint-fix`. It does not read a PDF. `--self-test` checks
the checker.

## How a compare script reads it

A script that compares corpus text with print (`feature-prose-540.py`, `disease-effects-272.py`,
`printed-titles-281.py`, the citation scripts) reads `scripts/errata.tsv` before it reports a hold.
Key a row by `(entry, field)`, where `field` is the feature anchor or `title`.

1. A difference that a `keep` row covers is reported as `errata`, not as a hold, and the kept text is
   written. A `misprint-fix` row is reported as `misprint` the same way.
2. A `print` row is applied like any print fix, and the script writes the printed text.
3. When the printed text the script reads no longer hashes to `printed_sha256` (after the
   normalization above), the row is stale and the script holds the difference again.
4. A changed number or rule word with no row stays a hold. The hand review gives it a class, and it
   gets a row when it is `errata`, `misprint` or `unknown`.
