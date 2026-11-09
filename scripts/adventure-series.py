#!/usr/bin/env python3
"""Fill the optional series fields in publications.toml from publication titles.

The corpus stores three Adventure series groupings (#159):

  * Adventure Paths, grouped by path name and volume;
  * Modules, one line ordered by publication date;
  * Pathfinder Society, grouped by season and scenario.

Run from the corpus root:

    python3 scripts/adventure-series.py

The script rewrites only the affected publication rows, keeps every other byte, and is
idempotent. It prints a count per grouping and every Adventure it cannot parse, so a
reviewer can decide what to add to the title table.

Adventure Path volume ranges
----------------------------
Source: the Paizo Pathfinder Adventure Path product line and the volume list at
https://en.wikipedia.org/wiki/List_of_Pathfinder_Adventure_Paths (PF1, volumes #1-#144).
The ranges are declared here because the titles name only the volume, never the path.
`series_number` is the issue within the path (for example, global #85 is issue 1 of Iron
Gods), not the global Pathfinder volume.
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

PUBLICATIONS = Path("publications.toml")
BLOCK = "[[publication]]"

# (first volume, last volume, printed path name), inclusive.
ADVENTURE_PATHS = [
    (1, 6, "Rise of the Runelords"),
    (7, 12, "Curse of the Crimson Throne"),
    (13, 18, "Second Darkness"),
    (19, 24, "Legacy of Fire"),
    (25, 30, "Council of Thieves"),
    (31, 36, "Kingmaker"),
    (37, 42, "Serpent's Skull"),
    (43, 48, "Carrion Crown"),
    (49, 54, "Jade Regent"),
    (55, 60, "Skull & Shackles"),
    (61, 66, "Shattered Star"),
    (67, 72, "Reign of Winter"),
    (73, 78, "Wrath of the Righteous"),
    (79, 84, "Mummy's Mask"),
    (85, 90, "Iron Gods"),
    (91, 96, "Giantslayer"),
    (97, 102, "Hell's Rebels"),
    (103, 108, "Hell's Vengeance"),
    (109, 114, "Strange Aeons"),
    (115, 120, "Ironfang Invasion"),
    (121, 126, "Ruins of Azlant"),
    (127, 132, "War for the Crown"),
    (133, 138, "Return of the Runelords"),
    (139, 144, "Tyrant's Grasp"),
]

SERIES_KEYS = ("series_kind", "series", "series_number", "season")

AP_TITLE = re.compile(r"^Pathfinder #(\d+)(?::|\s)")
SOCIETY_TITLE = re.compile(
    r"^Pathfinder Society (?:Scenario #|S)(\d+)-(\d+)(?::|\s|$)", re.IGNORECASE
)


def adventure_path_issue(volume: int) -> tuple[str, int] | None:
    """Return (path name, issue within the path) for a global Pathfinder volume."""
    for first, last, name in ADVENTURE_PATHS:
        if first <= volume <= last:
            return name, volume - first + 1
    return None


def parse(title: str, category: str | None) -> tuple[dict[str, object] | None, bool]:
    """Return (fields, in_scope) for one publication.

    ``fields`` is None for an Adventure the title does not parse.
    """
    in_scope = category in ("Adventure Path", "Module", "Society")
    if category == "Adventure Path":
        match = AP_TITLE.match(title)
        if not match:
            return None, True
        volume = int(match.group(1))
        path = adventure_path_issue(volume)
        if path is None:
            return None, True
        name, issue = path
        return {
            "series_kind": "adventure-path",
            "series": name,
            "series_number": str(issue),
        }, True

    if category == "Module":
        return {"series_kind": "module"}, True

    match = SOCIETY_TITLE.match(title)
    if match:
        season = int(match.group(1))
        scenario = int(match.group(2))
        return {
            "series_kind": "society",
            "series_number": f"{season}-{scenario:02d}",
            "season": season,
        }, True

    if category == "Society":
        return None, True
    return None, in_scope


def toml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def format_fields(fields: dict[str, object]) -> list[str]:
    lines = []
    for key in SERIES_KEYS:
        if key not in fields:
            continue
        value = fields[key]
        if isinstance(value, int):
            lines.append(f"{key} = {value}\n")
        else:
            lines.append(f"{key} = {toml_string(str(value))}\n")
    return lines


def split_blocks(text: str) -> list[list[str]]:
    blocks: list[list[str]] = []
    current: list[str] | None = None
    for line in text.splitlines(keepends=True):
        if line.strip() == BLOCK:
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        blocks.append(current)
    return blocks


def main() -> int:
    path = PUBLICATIONS
    if not path.is_file():
        print(f"error: {path} not found; run from the corpus root", file=sys.stderr)
        return 2

    blocks = split_blocks(path.read_text(encoding="utf-8"))
    counts = {"adventure-path": 0, "module": 0, "society": 0}
    unparsed: list[tuple[str, str, str]] = []
    output: list[str] = []

    for block in blocks:
        text = "".join(block)
        parsed = tomllib.loads(text)
        row = parsed["publication"][0]
        title = row.get("title", "")
        category = row.get("category")
        publication_id = row.get("id", "")

        fields, in_scope = parse(title, category)
        if fields is not None:
            counts[fields["series_kind"]] += 1
        elif in_scope:
            unparsed.append((publication_id, title, category or ""))

        # Remove any previous series line, so a rerun replaces rather than repeats.
        kept = [
            line
            for line in block
            if line.split("=", 1)[0].strip() not in SERIES_KEYS
        ]
        if fields is None:
            output.extend(kept)
            continue

        insert_at = 1
        for wanted in ("publication_date", "category", "copyright", "title"):
            found = next(
                (
                    index
                    for index, line in enumerate(kept)
                    if line.split("=", 1)[0].strip() == wanted
                ),
                None,
            )
            if found is not None:
                insert_at = found + 1
                break
        output.extend(kept[:insert_at])
        output.extend(format_fields(fields))
        output.extend(kept[insert_at:])

    path.write_text("".join(output), encoding="utf-8")

    print(
        "Series fields written: "
        f"{counts['adventure-path']} adventure path volumes, "
        f"{counts['module']} modules, "
        f"{counts['society']} society scenarios."
    )
    print(f"Adventures left unparsed: {len(unparsed)}")
    for publication_id, title, category in unparsed:
        print(f"  - {publication_id} | {category or '-'} | {title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
