#!/usr/bin/env python3
"""Find feats whose typed `prerequisites` field is not the feat's own printed line.

A feat states its prerequisites twice: the typed `prerequisites` field in the
front matter, and the `**Prerequisites:**` line in the body. The field describes
the feat itself, so it must hold the first printed line of the body. A feat may
print more lines: variants of the same feat, or the prerequisites of the options
a feat grants (Beast Speaker prints one for each beast companion). Those later
lines are not the feat's own, and reading one of them is drift — the field then
repeats a companion's prerequisites instead of the feat's.

Both sides are compared as the corpus tool compares them: links keep their
label, Markdown emphasis and escapes are dropped, and case, whitespace and the
end punctuation do not decide. A feat with no typed field is skipped.

Usage (from the corpus root, read-only, no edits):

    python3 scripts/scan-feat-prerequisite-text.py [--count]

It prints one line per entry, sorted, and exits 1 when a field disagrees with
the body. `--count` prints only the number of entries.
"""

import argparse
import re
import sys
import tomllib
from pathlib import Path

PREREQ = re.compile(r"\*\*Prerequisites?:\*\*(.*?)(?:\\\n|\n\n|\*\*)", re.S)
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def read(path):
    head, _, body = path.read_text(encoding="utf-8").partition("\n+++\n")
    return tomllib.loads(head[4:]), body


def normalize(text):
    text = text.replace("&times;", "×").replace("&dagger;", "†").replace("&amp;", "&")
    text = LINK.sub(r"\1", text)
    text = re.sub(r"\\(.)", r"\1", text)
    text = text.replace("*", "").replace("_", "")
    return re.sub(r"\s+", " ", text).strip().lower().rstrip(".;")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--count", action="store_true")
    ap.add_argument("root", nargs="?", default=".")
    args = ap.parse_args()
    root = Path(args.root)
    rows = []
    for path in sorted((root / "entries" / "feat").rglob("*.md")):
        data, body = read(path)
        typed = data.get("fields", {}).get("prerequisites", "")
        if not typed:
            continue
        printed = [m.group(1) for m in PREREQ.finditer(body)]
        if not printed:
            continue
        if normalize(printed[0]) != normalize(typed):
            rows.append((data["id"], typed, printed[0]))
    if args.count:
        print(len(rows))
    else:
        for entry, typed, stated in rows:
            print(f"{entry}: typed {typed!r} != printed {normalize(stated)!r}")
    return 1 if rows else 0


if __name__ == "__main__":
    sys.exit(main())
