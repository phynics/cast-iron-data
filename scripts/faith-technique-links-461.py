#!/usr/bin/env python3
"""Replace the quoted Divine Fighting Technique of a faith with a link (phynics/cast-iron#461, S10).

    python3 scripts/faith-technique-links-461.py <corpus-dir> [--check]

Sixteen faith entries (`ref/faith/*`) quote their deity's divine fighting technique under the
heading `## [Divine Fighting Technique](ref/feat/divine-fighting-technique)`: a block quote that
starts `> ### <Technique>` and has its own `**Sources:**` line (Divine Anthology, or Weapon
Master's Handbook). The same text is a section `### <Technique>` of the feat entry. Owner ruling of
2026-11-24: the quote becomes a link to the technique, and the book then leaves the faith (the
`remove` rows of `scripts/membership-verdicts-461-s10.tsv`, applied by `membership-apply.py`).

For each faith whose quote has a `### <Technique>` section in the feat entry, the block quote is
replaced by one paragraph, `[<Technique>](ref/feat/divine-fighting-technique#sec-<slug>)`. The
slug is the one of the compiler (`sec-` and the lowercase letters and digits of the heading, one `-`
between words), and `corpus-check` proves that the anchor exists. A quote without such a section
(the feat entry holds no section for Iomedae or Norgorber) is left alone and listed: no entry holds
that technique, so there is nothing to link to. Running twice changes nothing.

`--check` writes nothing; it exits 1 while a quote that has a section is still in a faith entry.
Output has ids only.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FEAT = "entries/feat/divine-fighting-technique.md"
HEADING = re.compile(r"^## \\\[Divine Fighting Technique\\\]\(ref/feat/divine-fighting-technique\)\n\n", re.M)
QUOTE = re.compile(r"((?:>[^\n]*\n)+)")
BOOKS = ("Divine Anthology", "Weapon Master's Handbook")


def slug(text: str) -> str:
    return "-".join(re.findall(r"[a-z0-9]+", text.lower()))


def feat_sections(root: Path) -> set[str]:
    body = (root / FEAT).read_text(encoding="utf-8")
    return set(re.findall(r"^### ([^\n]+)$", body, re.M))


def plan(root: Path):
    sections = feat_sections(root)
    done, left = [], []
    for path in sorted((root / "entries" / "faith").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for h in HEADING.finditer(text):
            m = QUOTE.match(text, h.end())
            if not m:
                continue
            name = re.search(r"^> ### ([^\n]+)$", m.group(1), re.M)
            src = re.search(r"^> \*\*Sources?:\*\* ([^\n]+)$", m.group(1), re.M)
            if not name or not src or src.group(1).strip() not in BOOKS:
                continue
            title = name.group(1)
            fid = "ref/faith/" + path.stem
            if title in sections:
                link = f"[{title}](ref/feat/divine-fighting-technique#sec-{slug(title)})"
                done.append((fid, path, text[: h.end()] + link + "\n" + text[m.end():], title, src.group(1)))
            else:
                left.append((fid, title, src.group(1)))
            break
    return done, left


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    done, left = plan(a.corpus)
    for fid, title, book in left:
        print(f"no section for {title!r} in the feat entry, left alone: {fid} ({book})")
    if a.check:
        for fid, *_ in done:
            print(f"pending: {fid}")
        print(f"{len(done)} faiths pending, {len(left)} without a section")
        return 1 if done else 0
    for fid, path, new, title, book in done:
        path.write_text(new, encoding="utf-8")
        print(f"linked {fid}: {title} ({book})")
    print(f"{len(done)} faiths linked, {len(left)} left alone")
    return 0


if __name__ == "__main__":
    sys.exit(main())
