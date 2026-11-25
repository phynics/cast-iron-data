#!/usr/bin/env python3
"""Faction traits of the two Pathfinder Society guides (cast-iron-data#285).

Two subcommands:

  extract  Read the faction pages of a guide PDF and write the reviewed transcription as a TSV.
           Needs `pdftotext` (poppler) on PATH and the PDF; a reviewer who has no PDF reads the
           committed TSV instead.
  generate Write one entry file per row of the TSV, under entries/trait/. Idempotent: a second
           run changes no byte. `--check` writes nothing and fails when a file differs.

The TSV (scripts/faction-traits-285.tsv) has one row per printed trait, in print order:

  guide <TAB> faction <TAB> name <TAB> page <TAB> text

`guide` is `v80` (Pathfinder Society Roleplaying Guild Guide, Version 8.0) or `v43` (Guide to
Pathfinder Society Organized Play, Version 4.3). `text` is the printed paragraph after the
`Name: ` label, with the line breaks of the column joined by one space and a hyphen kept only
where the printed word is hyphenated (the `HYPHENS` table below names each decision).

Id and title scheme (see the pull request of #285): a trait whose printed name occurs in both
guides takes the suffix of its guide in the title and the id, `Name (Guild Guide 8.0)` and
`Name (Organized Play 4.3)`, `ref/trait/<slug>-guild-guide-8-0` and
`ref/trait/<slug>-organized-play-4-3`. A name that occurs in one guide only, and in no other trait
of the corpus, keeps its printed title.
"""
import argparse
import re
import subprocess
import sys
import textwrap
from pathlib import Path

GUIDES = {
    "v80": {
        "publication": "pathfinder-society-roleplaying-guild-guide-8-0",
        "suffix": "Guild Guide 8.0",
        "slug": "guild-guide-8-0",
        "first": 28,
        "last": 31,
    },
    "v43": {
        "publication": "guide-to-pathfinder-society-organized-play-4-3",
        "suffix": "Organized Play 4.3",
        "slug": "organized-play-4-3",
        "first": 13,
        "last": 20,
    },
}

# A line-end hyphen that the print keeps (a compound word). Every other line-end hyphen is
# a soft break, and the two halves are joined without it. Keyed by the two halves.
HYPHENS = {
    ("spell", "like"): "-",
    ("self", "reliant"): "-",
    ("self", "determination"): "-",
    ("good", "aligned"): "-",
    ("like", "minded"): "-",
    ("full", "round"): "-",
    ("one", "handed"): "-",
}

LABELS = {
    "Faction Leader", "Faction Leaders", "Motto", "Objectives", "Objective", "Goal", "Goals",
    "Season 8 Goal", "Season 8 Goals", "Season 4 Goals",
}

START = re.compile(r"^\s*([A-Z][\w’'-]*(?: [A-Za-z][\w’'-]*){0,5}): (?=\S)")
HEADER = re.compile(
    r"^\s*(GUIDE TO PATHFINDER SO.*|OCIETY ORGANIZED PLAY.*|PATHFINDER SOCIETY RO.*"
    r"|OLEPLAYING GUILD GUIDE.*|PATHFINDER SO.*|GUIDE TO.*|\d{1,2})\s*$"
)


def column_text(pdf, page, half):
    x, w = (0, 301) if half == 0 else (301, 302)
    out = subprocess.run(
        ["pdftotext", "-layout", "-x", str(x), "-y", "0", "-W", str(w), "-H", "783",
         "-f", str(page), "-l", str(page), str(pdf), "-"],
        check=True, capture_output=True, text=True,
    ).stdout
    return out.split("\f")[0]


def blocks_of(text):
    """Runs of non-blank lines, with the printed header and folio lines left out."""
    blocks, cur = [], []
    for line in text.split("\n"):
        if HEADER.match(line) or not line.strip():
            if cur:
                blocks.append(cur)
                cur = []
            continue
        cur.append(line.strip())
    if cur:
        blocks.append(cur)
    return blocks


def join(lines):
    out = ""
    for line in lines:
        if not out:
            out = line
        elif out.endswith("-") and out[-2:-1].isalpha() and line[:1].islower():
            left = re.search(r"([A-Za-z]+)-$", out).group(1).lower()
            right = re.match(r"[A-Za-z]+", line).group(0).lower()
            keep = HYPHENS.get((left, right), "")
            out = out[:-1] + keep + line
            if (left, right) not in HYPHENS:
                print(f"note: line-end hyphen joined: {left}-{right}", file=sys.stderr)
        else:
            out += " " + line
    return out


def extract(pdf, guide):
    g = GUIDES[guide]
    faction = None
    rows = []  # [faction, name, first_page, last_page, lines]
    in_traits = False  # inside a "<Faction> Traits" list
    for page in range(g["first"], g["last"] + 1):
        for half in (0, 1):
            blocks = blocks_of(column_text(pdf, page, half))
            for index, block in enumerate(blocks):
                last_block = index == len(blocks) - 1
                heading = re.match(r"^(.+) Traits$", block[0])
                if heading and not START.match(block[0]):
                    faction, in_traits = heading.group(1), True
                    block = block[1:]
                    # the intro sentence runs to the first trait or to the end of the block
                    while block and not START.match(block[0]):
                        block = block[1:]
                    if not block:
                        continue
                    cur = None
                elif not in_traits:
                    continue
                else:
                    cur = None
                    if index == 0 and rows and not START.match(block[0]):
                        prev = rows[-1][4][-1]
                        if not re.search(r"[.!?)”\"]$", prev):
                            cur = rows[-1]  # a trait that runs on from the column before
                        else:
                            print(f"REVIEW: page {page} half {half} starts {block[0]!r} after "
                                  f"{rows[-1][1]}", file=sys.stderr)
                for line in block:
                    m = START.match(line)
                    if m and m.group(1) in LABELS:
                        in_traits, cur = False, None
                        break
                    if m:
                        cur = [faction, m.group(1), page, page, [line[m.end():].strip()]]
                        rows.append(cur)
                    elif cur is not None:
                        cur[4].append(line)
                        cur[3] = page
                    else:
                        in_traits = False
                        break
                else:
                    # the list goes on in the next column only if this block ended the column
                    in_traits = in_traits and last_block
    out = []
    for faction, name, p1, p2, lines in rows:
        page = str(p1) if p1 == p2 else f"{p1}-{p2}"
        out.append((guide, faction, name, page, join(lines)))
    return out


def straight(text):
    """The corpus writes the straight apostrophe (96 per cent of its trait files)."""
    return text.replace("’", "'")


def slugify(name):
    s = name.lower().replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def read_tsv(path):
    rows = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("guide\t") or not line.strip():
            continue
        guide, faction, name, page, text = line.split("\t")
        rows.append(dict(guide=guide, faction=straight(faction), name=straight(name),
                         page=page, text=straight(text)))
    return rows


def titles_and_ids(rows, taken_titles):
    """The scheme: a printed name that occurs in both guides, or in another trait of the corpus,
    takes the suffix of its guide; every other name keeps its printed title."""
    count = {}
    for r in rows:
        count.setdefault(r["name"], set()).add(r["guide"])
    for r in rows:
        shared = len(count[r["name"]]) > 1 or r["name"] in taken_titles
        g = GUIDES[r["guide"]]
        if shared:
            r["title"] = f'{r["name"]} ({g["suffix"]})'
            r["slug"] = f'{slugify(r["name"])}-{g["slug"]}'
        else:
            r["title"] = r["name"]
            r["slug"] = slugify(r["name"])
        r["id"] = f'ref/trait/{r["slug"]}'
    return rows


def render(r):
    g = GUIDES[r["guide"]]
    page = r["page"]
    return (
        "+++\n"
        f'id = "{r["id"]}"\n'
        'kind = "trait"\n'
        f'title = "{r["title"]}"\n'
        f'source_ids = ["{g["publication"]}"]\n'
        "[[sources]]\n"
        f'publication = "{g["publication"]}"\n'
        f'page = "{page}"\n'
        "\n"
        "[fields]\n"
        'kind = "trait"\n'
        'category = "Campaign"\n'
        "+++\n"
        "\n"
        f'**Prerequisite:** Member of the {r["faction"]} faction\n'
        "\n"
        f'**Campaign:** Pathfinder Society\n'
        "\n"
        # the corpus formatter wraps a paragraph at 100 columns
        + "\n".join(textwrap.wrap(r["text"], width=100, break_long_words=False,
                                  break_on_hyphens=False))
        + "\n"
    )


def corpus_titles(corpus):
    """Titles of the traits of the corpus that this set did not write."""
    own = {g["publication"] for g in GUIDES.values()}
    taken = set()
    for f in (corpus / "entries" / "trait").glob("*.md"):
        text = f.read_text(encoding="utf-8")
        sources = re.search(r"^source_ids = \[(.*)\]$", text, re.M)
        if sources and any(f'"{p}"' in sources.group(1) for p in own):
            continue
        t = re.search(r'^title = "(.*)"$', text, re.M)
        if t:
            taken.add(t.group(1))
    return taken


def taken_ids(corpus, app_ids):
    """Every id the corpus holds or ever published, for the no-collision guard."""
    ids = set()
    for f in (corpus / "entries").rglob("*.md"):
        m = re.search(r'^id = "(.*)"$', f.read_text(encoding="utf-8"), re.M)
        if m:
            ids.add(m.group(1))
    alias = corpus / "aliases.toml"
    if alias.exists():
        ids.update(re.findall(r'"(ref/[^"]+)"', alias.read_text(encoding="utf-8")))
        ids.update(re.findall(r'^"?([^"=\s]+)"? *=', alias.read_text(encoding="utf-8"), re.M))
    if app_ids:
        ids.update(l.strip() for l in Path(app_ids).read_text().splitlines()
                   if l.strip() and not l.startswith("#"))
    return ids


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract")
    e.add_argument("--pdf", required=True)
    e.add_argument("--guide", required=True, choices=sorted(GUIDES))
    g = sub.add_parser("generate")
    g.add_argument("--tsv", default="scripts/faction-traits-285.tsv")
    g.add_argument("--corpus", default=".")
    g.add_argument("--check", action="store_true")
    g.add_argument("--published-ids", help="sources/published-ids.txt of the app, for the guard")
    args = ap.parse_args()
    if args.cmd == "extract":
        for row in extract(args.pdf, args.guide):
            print("\t".join(row))
        return
    corpus = Path(args.corpus)
    rows = titles_and_ids(read_tsv(args.tsv), corpus_titles(corpus))
    own = {g["publication"] for g in GUIDES.values()}
    used = taken_ids(corpus, args.published_ids)
    seen = set()
    for r in rows:
        path = corpus / "entries" / "trait" / f'{r["slug"]}.md'
        if r["id"] in seen:
            sys.exit(f'duplicate id in this set: {r["id"]}')
        seen.add(r["id"])
        if r["id"] in used:
            # allowed only when the file is this set's own, written by an earlier run
            held = path.read_text(encoding="utf-8") if path.exists() else ""
            src = re.search(r"^source_ids = \[(.*)\]$", held, re.M)
            if not (src and any(f'"{p}"' in src.group(1) for p in own)):
                sys.exit(f'id already taken: {r["id"]} (a corpus entry, an alias or a published id)')
    bad = 0
    for r in rows:
        path = corpus / "entries" / "trait" / f'{r["slug"]}.md'
        text = render(r)
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                print(f"differs: {path}", file=sys.stderr)
                bad += 1
        else:
            path.write_text(text, encoding="utf-8")
    if bad:
        sys.exit(1)
    print(f"{len(rows)} entries", file=sys.stderr)


if __name__ == "__main__":
    main()
