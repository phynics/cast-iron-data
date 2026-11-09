#!/usr/bin/env python3
"""Convert a leading `**Sources:**` paragraph into `[[sources]]` rows.

The script is rerunnable. It changes only entry files whose first Sources paragraph is part of
the entry header (a stat block, a heading, a note quote, or the printed header lines) and whose
every citation parses and maps to a publication already listed in `source_ids`. Everything else
is left in place and reported.

Run from the corpus root:

    python3 scripts/sources-field.py [--dry-run]

Then format and check the corpus with the cast-iron tool:

    cargo xtask corpus-fmt <dir>
    cargo xtask corpus-check <dir>
"""

from __future__ import annotations

import argparse
import re
import tomllib
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLICATIONS = ROOT / "publications.toml"
ENTRIES = ROOT / "entries"

# Printed titles that do not equal a `publications.toml` title. Reviewed by hand.
ALIASES = {
    "prpg core rulebook": "core-rulebook",
    "pathfinder rpg bestiary": "bestiary",
    "gamemastery guide": "game-mastery-guide",
    "pathfinder campaign setting": "pathfinder-campaign-setting",
    "tome of horrors complete": "tome-of-horrors-complete-pf",
    "pathfinder #125 tower of the drowned dead": "pathfinder-125-tower-of-the-drowned-dead",
    "pathfinder #125: tower of the drowned dead": "pathfinder-125-tower-of-the-drowned-dead",
    "the first world": "the-first-world-realm-of-the-fey",
    "sargava": "sargava-the-lost-colony",
}

SOURCES_RE = re.compile(r"^\*\*Sources?:\*\*(.*)$")
PAGE_RE = re.compile(r"^(?:pg\.?|p\.?|page)\s*([^,]+)", re.IGNORECASE)
SLASH_PAGE_RE = re.compile(r"^/([0-9][^,]*)")
CONTINUATION_RE = re.compile(r"^\s*,\s*(\d+(?:-\d+)?)\s*")


def normalize(value: str) -> str:
    """Collapse whitespace and unescape the corpus escapes used in a citation."""
    value = value.replace("\\#", "#")
    value = re.sub(r"\\(.)", r"\1", value)
    return re.sub(r"\s+", " ", value).strip()


def toml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def load_publications() -> dict[str, str]:
    data = tomllib.loads(PUBLICATIONS.read_text(encoding="utf-8"))
    return {row["id"]: row["title"] for row in data["publication"]}


def title_map(publications: dict[str, str]) -> dict[str, str]:
    mapping = {normalize(title).lower(): pid for pid, title in publications.items()}
    mapping.update(ALIASES)
    return mapping


class Citation:
    __slots__ = ("publication", "page")

    def __init__(self, publication: str, page: str | None) -> None:
        self.publication = publication
        self.page = page

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Citation)
            and self.publication == other.publication
            and self.page == other.page
        )

    def __repr__(self) -> str:
        return f"Citation({self.publication!r}, {self.page!r})"


def parse_citations(text: str, titles: dict[str, str]) -> tuple[list[Citation], list[str]]:
    """Parse a Sources line into citations. Returns the citations and unmapped title candidates."""
    text = re.sub(r"^\*\*Sources?:\*\*\s*", "", normalize(text))
    ordered = sorted(titles, key=len, reverse=True)
    citations: list[Citation] = []
    unmapped: list[str] = []
    index = 0
    while index < len(text):
        while index < len(text) and text[index] in " ,;":
            index += 1
        if index >= len(text):
            break
        rest = text[index:].lower()
        found = None
        for title in ordered:
            if rest.startswith(title):
                tail = rest[len(title) :]
                if (
                    tail == ""
                    or tail[0] in " ,;/"
                    or tail.startswith("pg")
                    or tail.startswith("p.")
                ):
                    found = title
                    break
        if found is None:
            end = text.find(",", index)
            if end == -1:
                end = len(text)
            unmapped.append(text[index:end].strip())
            index = end
            continue
        publication = titles[found]
        index += len(found)
        while index < len(text) and text[index] == " ":
            index += 1
        page = None
        match = SLASH_PAGE_RE.match(text[index:])
        if match:
            page = match.group(1).strip().rstrip(".")
            index += match.end()
        else:
            match = PAGE_RE.match(text[index:])
            if match:
                page = match.group(1).strip().rstrip(" .,;")
                index += match.end()
        if page is not None:
            # `Title pg. 56, 58` gives one citation whose page list is `56, 58`.
            while True:
                match = CONTINUATION_RE.match(text[index:])
                if not match:
                    break
                page += ", " + match.group(1)
                index += match.end()
        else:
            while index < len(text) and text[index] == " ":
                index += 1
        citations.append(Citation(publication, page))
    return citations, unmapped


def split_front(text: str) -> tuple[str, list[str]]:
    lines = text.split("\n")
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == "+++")
        end = next(i for i, line in enumerate(lines) if i > start and line.strip() == "+++")
    except StopIteration:
        raise ValueError("no front matter")
    return "\n".join(lines[start + 1 : end]), lines[end + 1 :]


def split_blocks(body: list[str]) -> list[list[str]]:
    blocks: list[list[str]] = []
    current: list[str] = []
    in_fence = False
    for line in body:
        stripped = line.strip()
        if stripped.startswith(":::"):
            current.append(line)
            if stripped == ":::":
                blocks.append(current)
                current = []
                in_fence = False
            else:
                in_fence = True
            continue
        if not in_fence and stripped == "":
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line)
    if current:
        blocks.append(current)
    return blocks


def sources_index(blocks: list[list[str]]) -> int | None:
    for index, block in enumerate(blocks):
        first = block[0].strip() if block else ""
        match = SOURCES_RE.match(first)
        if match:
            return index
    return None


def is_header_block(block: list[str]) -> bool:
    first = block[0].strip() if block else ""
    if first.startswith(("#", ">", "|", ":::")):
        return True
    if re.match(r"^(-|\d+\.) ", first):
        return True
    # Printed header lines are bold labels (`**Type:** dragon`) or an italic flavour sentence.
    return first.startswith(("**", "_"))


def sources_text(block: list[str]) -> tuple[str, list[str]]:
    """The citation text of a Sources block and the block's remaining lines."""
    for index, line in enumerate(block):
        if line.rstrip().endswith("\\"):
            head = block[:index] + [line.rstrip()[:-1]]
            return "\n".join(head), block[index + 1 :]
    return "\n".join(block), []


def front_sources(front: str) -> list[dict]:
    return tomllib.loads(front).get("sources", [])


def insert_sources(front: str, citations: list[Citation]) -> str:
    rows: list[str] = []
    for citation in citations:
        rows.append("[[sources]]")
        rows.append(f"publication = {toml_string(citation.publication)}")
        if citation.page is not None:
            rows.append(f"page = {toml_string(citation.page)}")
    lines = front.split("\n")
    at = next(
        (index for index, line in enumerate(lines) if line.strip() == "[fields]"),
        len(lines),
    )
    if at > 0 and lines[at - 1].strip() != "":
        rows.insert(0, "")
    rows.append("")
    lines[at:at] = rows
    return "\n".join(lines)


def convert(path: Path, titles: dict[str, str], dry_run: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT).as_posix()
    try:
        front, body = split_front(text)
    except ValueError:
        return {"kind": "unreadable", "path": relative}
    blocks = split_blocks(body)
    existing = front_sources(front)
    # Rerunnable: rows are the migration's own output, so never add a second set.
    if existing:
        return {"kind": "already-converted", "path": relative}
    index = sources_index(blocks)
    if index is None:
        return {"kind": "no-sources", "path": relative}
    if not all(is_header_block(block) for block in blocks[:index]):
        return {"kind": "mid-body", "path": relative}
    citation_text, remainder = sources_text(blocks[index])
    citations, unmapped = parse_citations(citation_text, titles)
    if unmapped:
        return {"kind": "unparsed", "path": relative, "unmapped": unmapped}
    data = tomllib.loads(front)
    source_ids = set(data.get("source_ids", []))
    missing = [c.publication for c in citations if c.publication not in source_ids]
    if missing:
        return {"kind": "mismatch", "path": relative, "missing": missing}
    new_blocks = list(blocks)
    if remainder:
        new_blocks[index] = remainder
    else:
        del new_blocks[index]
    new_body = "\n\n".join("\n".join(block) for block in new_blocks)
    new_front = "+++\n" + insert_sources(front, citations) + "\n+++"
    result = new_front + ("\n\n" + new_body if new_body else "") + "\n"
    if not dry_run:
        path.write_text(result, encoding="utf-8")
    return {"kind": "converted", "path": relative, "citations": citations}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="report without writing files")
    options = parser.parse_args()
    publications = load_publications()
    titles = title_map(publications)
    counts: Counter[str] = Counter()
    reasons: dict[str, list[str]] = defaultdict(list)
    unmapped: Counter[str] = Counter()
    converted = 0
    for path in sorted(ENTRIES.rglob("*.md")):
        result = convert(path, titles, options.dry_run)
        kind = result["kind"]
        counts[kind] += 1
        if kind == "converted":
            converted += 1
        elif kind == "mid-body":
            reasons["mid-body"].append(result["path"])
        elif kind == "unparsed":
            for title in result["unmapped"]:
                unmapped[title] += 1
            reasons["unparsed"].append(result["path"])
        elif kind in ("mismatch", "conflict"):
            reasons[kind].append(result["path"])
    total = sum(counts.values())
    print(f"entries: {total}")
    print(f"converted: {converted}")
    print(f"already converted: {counts['already-converted']}")
    print(f"no Sources line: {counts['no-sources']}")
    print(f"left in place (mid-body): {counts['mid-body']}")
    print(f"left in place (unparsed): {counts['unparsed']}")
    print(f"left in place (publication not in source_ids): {counts['mismatch']}")
    print(f"left in place (conflict): {counts['conflict']}")
    if reasons["mid-body"]:
        print("\nmid-body Sources lines:")
        for path in reasons["mid-body"]:
            print(f"  {path}")
    if unmapped:
        print("\nunmapped printed titles:")
        for title, count in unmapped.most_common():
            print(f"  {count}  {title}")
    for kind in ("mismatch", "conflict", "unparsed"):
        if reasons[kind]:
            print(f"\n{kind}:")
            for path in reasons[kind]:
                print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
