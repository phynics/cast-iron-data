#!/usr/bin/env python3
"""Drop the copied Legacy of Dragons spell rule from two faith pages (phynics/cast-iron#461, S11).

    python3 scripts/faith-unique-spell-rules-461-s11.py <corpus-dir>

Legacy of Dragons p. 31 prints the tail strike spell and one rule for the clerics, inquisitors,
oracles and warpriests of dragon deities. It never names Ardad Lili or Draghignazzo. The two faith
pages copy that rule as a `### Unique Spell Rules` block under `## Follower Options` (owner ruling 3
of 2026-11-24 on #461: a copied generic section is not a printing; the book and the copied text go).
The script removes the block, and the `## Follower Options` heading when nothing else stays under it.
Running again changes nothing. Output has ids only.
"""
import re
import sys
from pathlib import Path

ENTRIES = ["faith/ardad-lili", "faith/draghignazzo"]
BLOCK = re.compile(r"(?:>\n)?> ### Unique Spell Rules\n(?:>.*\n)*")


def main() -> int:
    root = Path(sys.argv[1])
    for e in ENTRIES:
        p = root / "entries" / (e + ".md")
        t = p.read_text(encoding="utf-8")
        if "> ### Unique Spell Rules" not in t:
            print(f"{e}: already")
            continue
        t = BLOCK.sub("", t, count=1)
        t = re.sub(r"## Follower Options\n\n+(?=## )", "", t)
        t = re.sub(r"(\n>)+\n\n## Description", "\n\n## Description", t)
        p.write_text(t, encoding="utf-8")
        print(f"{e}: removed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
