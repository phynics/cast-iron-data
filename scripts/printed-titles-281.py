#!/usr/bin/env python3
"""Set the title of entries whose printed title differs to the printed title (#281).

The review table printed-titles-281.tsv has one row per entry of the issue:

  id, old_title   the entry id and the title it had before this script
  new_title       the printed title (for `first-book` the title is unchanged; for
                  `owner-question` it is the printed form that was NOT applied)
  book, page      the publication and the printed page where the title was read
  status          rewrite         the script sets the entry `title`, and the `title` of every
                                  curated book contents node (books/*.toml) that points at the
                                  entry and carries the old title, to new_title
                  first-book      the entry is printed in several books under different titles;
                                  the first book prints the title the entry has, so nothing changes
                  owner-question  print and entry differ, but the form is not a plain slip
                                  (see the pull request); nothing changes until the owner rules

Only titles change. Ids, files and aliases never change, even where an id carries the old
spelling.

  --check   list the rows whose entry or book nodes differ from the table; exit 1 when any
            is pending
  --write   set the pending titles, then run --check
"""
import argparse
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = HERE.parent
TABLE = HERE / 'printed-titles-281.tsv'
STATUSES = {'rewrite', 'first-book', 'owner-question'}
TITLE = re.compile(r'^title = "(.*)"$', re.M)


def rows():
    with TABLE.open(newline='') as f:
        table = list(csv.DictReader(f, delimiter='\t'))
    for row in table:
        if row['status'] not in STATUSES:
            sys.exit(f"{row['id']}: unknown status {row['status']!r}")
        if row['status'] != 'rewrite' and row['status'] != 'owner-question' \
                and row['old_title'] != row['new_title']:
            sys.exit(f"{row['id']}: first-book row must keep its title")
    return table


def entry_path(entry_id):
    assert entry_id.startswith('ref/')
    return CORPUS / 'entries' / f'{entry_id[4:]}.md'


def front_title(text):
    """The title line of the front matter (the first `title = ` line of the file)."""
    return TITLE.search(text)


def node_pattern(row):
    return re.compile(
        r'(^title = ")' + re.escape(row['old_title']) + r'("\nentry = "' + re.escape(row['id']) + r'"$)',
        re.M)


def book_nodes(row):
    """(path, text) of every curated book whose node for the entry still has the old title."""
    pat = node_pattern(row)
    for path in sorted((CORPUS / 'books').glob('*.toml')):
        text = path.read_text()
        if pat.search(text):
            yield path, text, pat


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--write', action='store_true')
    args = parser.parse_args()

    table = rows()
    if args.write:
        for row in table:
            if row['status'] != 'rewrite':
                continue
            path = entry_path(row['id'])
            text = path.read_text()
            match = front_title(text)
            if match.group(1) == row['old_title']:
                text = text[:match.start(1)] + row['new_title'] + text[match.end(1):]
                path.write_text(text)
            for node_path, node_text, pat in list(book_nodes(row)):
                node_path.write_text(pat.sub(lambda m: m.group(1) + row['new_title'] + m.group(2),
                                             node_text))

    pending = []
    for row in table:
        path = entry_path(row['id'])
        if not path.exists():
            pending.append(f"{row['id']}: no entry file")
            continue
        title = front_title(path.read_text()).group(1)
        want = row['new_title'] if row['status'] == 'rewrite' else row['old_title']
        if title != want:
            pending.append(f"{row['id']}: title {title!r}, table wants {want!r}")
        if row['status'] == 'rewrite':
            for node_path, _, _ in book_nodes(row):
                pending.append(f"{row['id']}: book node in {node_path.name} still has {row['old_title']!r}")
    for line in pending:
        print(line)
    print(f'{len(pending)} pending of {len(table)} rows')
    return 1 if pending else 0


if __name__ == '__main__':
    sys.exit(main())
