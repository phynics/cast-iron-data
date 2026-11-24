#!/usr/bin/env python3
"""Rewrite the Effect line of every disease entry to the printed words (#272, ruling 1).

The review table disease-effects-272.tsv has one row per entry of entries/disease/: the
entry id, the book and printed page of the stat block, the printed Effect words, and a status.

  printed_effect  the words of the printed Effect line, up to the `; Cure` clause that the
                  entry keeps in its own Cure line. Typography follows the corpus: the minus
                  sign is a hyphen-minus and apostrophes are straight.
  status          matches        the entry already carries the printed words
                  rewrite        the script replaces the entry's Effect value
                                 (The Tainted Plague prints `damage 1d6 Con and 1d6 Wis` under
                                 the label `damage`; the owner ruled the Effect value
                                 `1d6 Con and 1d6 Wis damage`.)
                  tail-in-body   print continues the Effect line with a clause that the entry
                                 already holds as a paragraph below the block; the Effect
                                 value takes the stat words and the paragraph stays
                  no-pdf         the book is not among the books read; the entry stays

Only the Effect value changes. No typed field mirrors it (`[fields] kind = "none"`).

  --check   list the rows whose entry differs from print; exit 1 when any is pending, or when
            an entry has no row or a row has no entry
  --write   rewrite the pending Effect values, then run --check
"""
import argparse
import csv
import re
import sys
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = HERE.parent
TABLE = HERE / 'disease-effects-272.tsv'
STATUSES = {'matches', 'rewrite', 'tail-in-body', 'no-pdf'}
EFFECT = re.compile(r'^\*\*(Effect|Initial effect):\*\* (.*?)(?=\n\n)', re.S | re.M)
WIDTH = 100


def rows():
    with TABLE.open(newline='') as f:
        table = list(csv.DictReader(f, delimiter='\t'))
    for row in table:
        if row['status'] not in STATUSES:
            sys.exit(f"{row['id']}: unknown status {row['status']!r}")
        if (row['status'] == 'no-pdf') != (row['printed_effect'] == ''):
            sys.exit(f"{row['id']}: printed_effect and status no-pdf disagree")
    return table


def entry_path(entry_id):
    return CORPUS / 'entries' / 'disease' / f'{entry_id}.md'


def current(text):
    match = EFFECT.search(text)
    if not match:
        return None, None
    return match, re.sub(r'\s*\n\s*', ' ', match.group(2))


def wrapped(label, value):
    return '\n'.join(textwrap.wrap(f'**{label}:** {value}', width=WIDTH,
                                   break_long_words=False, break_on_hyphens=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--write', action='store_true')
    args = parser.parse_args()

    table = rows()
    ids = {r['id'] for r in table}
    files = {p.stem for p in (CORPUS / 'entries' / 'disease').glob('*.md')}
    problems = [f'entry without a row: {i}' for i in sorted(files - ids)]
    problems += [f'row without an entry: {i}' for i in sorted(ids - files)]

    pending = []
    for row in table:
        if row['status'] == 'no-pdf' or row['id'] not in files:
            continue
        path = entry_path(row['id'])
        text = path.read_text()
        match, value = current(text)
        if match is None:
            problems.append(f"{row['id']}: no Effect line")
            continue
        if value != row['printed_effect']:
            pending.append((row, path, text, match))

    if args.write:
        for row, path, text, match in pending:
            label = match.group(1)
            text = text[:match.start()] + wrapped(label, row['printed_effect']) + text[match.end():]
            path.write_text(text)
        print(f'rewrote {len(pending)} Effect lines')
        pending = []

    for row, _path, _text, match in pending:
        print(f"pending {row['id']}: {row['book']} p. {row['page']}")
    for problem in problems:
        print(problem)
    counts = {s: sum(r['status'] == s for r in table) for s in sorted(STATUSES)}
    print(f'{len(table)} rows; {len(pending)} pending; {counts}')
    return 1 if pending or problems else 0


if __name__ == '__main__':
    sys.exit(main())
