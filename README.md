# Cast Iron data

The curated Pathfinder First Edition rules corpus behind [Cast Iron](https://github.com/phynics/cast-iron),
an offline-first reference app. One Markdown file holds each rules entry, so a fix is an ordinary
edit to one file, reviewed as an ordinary diff.

This project is not published, endorsed, or specifically approved by Paizo Inc. It makes no claim
of official status or compatibility.

## What is here

| Path | Contents |
|---|---|
| `entries/<kind>/<slug>.md` | One rules entry per file: 31,106 entries (spells, feats, creatures, items, classes, races, rules, traps, haunts, and more) |
| `corpus.toml` | The format version and the defaults entries omit |
| `publications.toml` | Publication metadata |
| `books/<publication-id>.toml` | The printed chapter order of a book that has one (16 books). Every other book is built from the `[[sources]]` pages of its entries |
| `legal.toml` | Licenses, Product Identity declaration, and Section 15 notices |
| `aliases.toml` | Legacy ids that resolve to current ids, so old bookmarks keep working |
| `exclusions.toml` | What the import left out and why. Rows are only appended |
| `history.toml` | Frozen results of the import. Never edited |
| `examples/` | One example entry for each kind, to copy when you add an entry |
| `CONTRIBUTING.md` | How to edit the corpus: three rules, the tool, and a recipe for each common edit |

Each entry's path is its permanent id without the `ref/` prefix: `ref/spell/fog-cloud` is
`entries/spell/fog-cloud.md`. Ids never change and files never move.

## License

Several licenses apply, each to its own part: MIT for the format, kit, examples, and repository
structure; the Open Game License v1.0a for the Open Game Content in the entries; and Paizo's
Community Use Policy for Paizo Product Identity. [LICENSE.md](LICENSE.md) states which covers what.
The full OGL text with every Section 15 notice is in [LICENSES/OGL-1.0a.md](LICENSES/OGL-1.0a.md).

## Edit an entry

Open the entry in a text editor, change it, and run the check below. The recipes (fix a typo, fix a
link, split a paragraph, add a table row, change a stat value, add an entry) are in
[CONTRIBUTING.md](CONTRIBUTING.md). The format specification is
[`docs/corpus-format.md`](https://github.com/phynics/cast-iron/blob/main/docs/corpus-format.md)
in the Cast Iron repository.

## Check locally

Two tools from the Cast Iron repository read the corpus: `cast-iron-corpus` (check and format) and
`cast-iron-compile` (the app's content build). You need the Rust toolchain that Cast Iron's
`rust-toolchain.toml` names (1.99.1 today); `cargo install --git` uses the toolchain you have
selected, not that file. Install both from the current `main` of Cast Iron, the revision that
`.github/workflows/corpus.yml` builds. CI builds `main` on every run, so run the command again
(it replaces the installed binaries) before you check a change, and whenever CI disagrees with
your result:

```sh
cargo install --locked --git https://github.com/phynics/cast-iron cast-iron-corpus cast-iron-content-compiler
```

Then, from the root of this repository:

```sh
cast-iron-corpus check .          # read every file; list broken links, ids, and sources
cast-iron-corpus fmt .            # rewrite every file into its one canonical form
cast-iron-corpus fmt --check .    # change nothing; name the first line that is not canonical
```

To run the app's content build as well (published ids still resolve, every book has a slot, every
entry is reachable), clone Cast Iron for its two lists and run, from the root of this repository:

```sh
git clone --depth 1 https://github.com/phynics/cast-iron ../cast-iron
cast-iron-compile --corpus . --out /tmp/content --reports /tmp/reports \
  --published ../cast-iron/sources/published-ids.txt \
  --book-slots ../cast-iron/sources/published-books.txt
```

A new publication needs a line in the app's `sources/published-books.txt` first: in Cast Iron, run
`cargo xtask published-books` against a pin that holds the publication and commit the added lines.
Until then the content build, and so the `corpus` workflow, fails for that pull request.

A pull request must pass `fmt --check` and the content build, which runs `check` first. The `corpus`
workflow runs both.

## Versions

A frozen version of the corpus is a Git tag named `vX.Y.Z`. Cast Iron pins a tag by its commit and
by a SHA-256 tree hash over the extracted files (`sources/corpus.toml` in Cast Iron), so a build
always reads the same content. The archive bytes are not pinned, because GitHub does not promise
that a generated archive stays byte-identical. Tags are never moved. A fix ships as a new tag:

- Until the app declares v1, every tag is the next `v0.1.N`, whatever it changes: entry
  corrections, added or retired entries (a retired id stays an alias), and corpus format
  changes (`corpus.toml` `format`; format 3 shipped in `v0.1.36`, format 4 in `v0.1.45`).
  The tag message says what changed, and Cast Iron's pin reads the format from `corpus.toml`.

The first tag, `v0.1.0`, is the corpus exactly as it was exported from Cast Iron.

## Report a problem

Report a mistake in an entry with the [problem form](https://github.com/phynics/cast-iron-data/issues/new?template=data-problem.yml).
Issues with the label `data` are fixed in this repository: [CONTRIBUTING.md](CONTRIBUTING.md)
explains how an issue becomes a fix. A fix reaches the app when Cast Iron bumps its pin to a new
tag. Until then, the app shows the previous text.

Problems with the app itself (layout, search, install, offline use) go to the
[Cast Iron issues](https://github.com/phynics/cast-iron/issues). Report a licensing concern as a
plain issue here.
