#!/usr/bin/env python3
"""Set `race_group` on every typed race record from the Advanced Race Guide chapters.

The Advanced Race Guide prints its player races in three chapters: Core Races, Featured
Races, and Uncommon Races. `books.toml` already places each typed `ref/race/*` record in
that printed tree, so the chapter decides `core_race`, `featured_race`, or
`uncommon_race`. Every race outside those chapters is `other_race`.

Run from the corpus root:

    python3 scripts/race-groups.py

The script rewrites only the `race_group` line of `entries/race/*.md`, keeps every other
byte, and is idempotent. It prints the count per group so a reviewer can compare the
result with the corpus total.
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

GROUP_BY_CHAPTER = {
    "Core Races": "core_race",
    "Featured Races": "featured_race",
    "Uncommon Races": "uncommon_race",
}
OTHER = "other_race"
ENTRY_LINE = re.compile(r'entry\s*=\s*"(ref/race/[^"]+)"')
ID_LINE = re.compile(r'^id\s*=\s*"(ref/race/[^"]+)"')


def arg_placements(root: Path) -> dict[str, str]:
    """The group each typed race gets from its Advanced Race Guide chapter."""
    with (root / "books.toml").open("rb") as handle:
        books = tomllib.load(handle)["books"]
    arg = next(book for book in books if book.get("source") == "advanced-race-guide")

    def walk(nodes: list[dict], group: str) -> dict[str, str]:
        found: dict[str, str] = {}
        for node in nodes:
            entry = node.get("entry")
            if entry and entry.startswith("ref/race/"):
                found[entry] = group
            found.update(walk(node.get("children", []), group))
        return found

    placements: dict[str, str] = {}
    for chapter in arg["chapters"]:
        group = GROUP_BY_CHAPTER.get(chapter.get("title", ""))
        if group:
            placements.update(walk(chapter.get("children", []), group))
    return placements


def front_matter(lines: list[str]) -> range:
    """The indexes between the two `+++` lines."""
    fences = [i for i, line in enumerate(lines) if line.rstrip("\n") == "+++"]
    if len(fences) < 2:
        raise ValueError("entry front matter is not closed")
    return range(fences[0] + 1, fences[1])


def entry_id(lines: list[str]) -> str:
    for i in front_matter(lines):
        match = ID_LINE.search(lines[i])
        if match:
            return match.group(1)
    raise ValueError("entry has no id")


def set_group(text: str, group: str) -> str:
    lines = text.splitlines(keepends=True)
    body = front_matter(lines)
    for i in body:
        if lines[i].lstrip().startswith("race_group"):
            indent = lines[i][: len(lines[i]) - len(lines[i].lstrip())]
            lines[i] = f'{indent}race_group = "{group}"\n'
            return "".join(lines)

    # Schema order: after the last header key that is present before `provenance`.
    anchor = None
    for i in body:
        key = lines[i].lstrip()
        if key.startswith(("tags =", "parent =", "section =", "source_ids =")):
            anchor = i
        if key.startswith("provenance ="):
            break
    if anchor is None:
        raise ValueError("entry has no header key to place race_group after")
    indent = lines[anchor][: len(lines[anchor]) - len(lines[anchor].lstrip())]
    lines.insert(anchor + 1, f'{indent}race_group = "{group}"\n')
    return "".join(lines)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    placements = arg_placements(root)
    counts: dict[str, int] = {}
    written = 0

    for path in sorted((root / "entries" / "race").glob("*.md")):
        text = path.read_text()
        lines = text.splitlines(keepends=True)
        group = placements.get(entry_id(lines), OTHER)
        updated = set_group(text, group)
        if updated != text:
            path.write_text(updated)
            written += 1
        counts[group] = counts.get(group, 0) + 1

    for group in ("core_race", "featured_race", "uncommon_race", OTHER):
        print(f"{group}: {counts.get(group, 0)}")
    print(f"entries: {sum(counts.values())}; files rewritten: {written}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
