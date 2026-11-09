#!/usr/bin/env python3
"""Audit the corpus for third-party text outside its own entries.

Run from the corpus root:

    python3 scripts/third-party-audit.py

A publication with ``third_party = true`` is not published by Paizo. Its text
must stay in entries that cite only that publication, in an add-on or revision
entry, so turning the book off removes it completely. This script reports:

(a) a third-party id in ``source_ids`` whose entry body does not cite it, and a
    body Source line that cites a third-party publication whose id is missing
    from ``source_ids``;
(b) a long paragraph in a non-third-party entry that exactly or nearly matches
    a paragraph in a third-party-only entry;
(c) a body link or relation from an entry with no third-party source to an
    entry whose sources are all third-party;
(d) a third-party-only entry placed in another publication's book tree;
(e) an entry whose ``source_ids`` mix third-party and Paizo publications.

The report is Markdown. It changes no files.
"""

from __future__ import annotations

import re
import sys
import tomllib
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(".")
ENTRY_DIR = ROOT / "entries"
PUBLICATIONS = ROOT / "publications.toml"
BOOKS = ROOT / "books.toml"

FRONT = re.compile(r"\A\+\+\+\n(.*?)\n\+\+\+\n(.*)\Z", re.DOTALL)
SOURCE_LINE = re.compile(r"^\*\*Sources:\*\*\s*(.*?)\\?\s*$", re.MULTILINE)
LINK = re.compile(r"\]\((ref/[^)\s#]+)(?:#[^)]+)?\)")
HEADING = re.compile(r"^#{1,6}\s+")

# A paragraph must be this long before a near-match is interesting. Short stat
# lines and labels recur across books without being copied text.
MIN_PARAGRAPH_CHARS = 160
MIN_PARAGRAPH_WORDS = 20
SHINGLE_WORDS = 8
NEAR_RATIO = 0.90
NEAR_LENGTH_RATIO = 0.80
MAX_POSTING = 25


def normalize(text: str) -> str:
    """Case-fold text, drop Markdown markup, and collapse whitespace."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`\\]", "", text)
    text = text.replace("&", "and")
    text = re.sub(r"[^0-9A-Za-z]+", " ", text)
    return " ".join(text.casefold().split())


def publication_aliases(publication: dict) -> list[str]:
    """Normalized body-Source spellings for one publication."""
    title = publication["title"]
    aliases = {normalize(title)}
    # Source lines often drop a subtitle: "The Elephant in the Room" for the
    # full title. A parenthetical edition marker may also be absent.
    aliases.add(normalize(title.split(":", 1)[0]))
    aliases.add(normalize(re.sub(r"\s*\([^)]*\)\s*$", "", title)))
    return sorted(alias for alias in aliases if alias)


def read_entries() -> dict[str, dict]:
    entries: dict[str, dict] = {}
    for path in sorted(ENTRY_DIR.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = FRONT.match(text)
        if match is None:
            print(f"warning: no front matter in {path}", file=sys.stderr)
            continue
        front, body = match.groups()
        data = tomllib.loads(front)
        entry_id = data.get("id")
        if not entry_id:
            print(f"warning: no id in {path}", file=sys.stderr)
            continue
        entries[entry_id] = {
            "path": path,
            "id": entry_id,
            "front": data,
            "body": body,
            "body_line": text.count("\n", 0, match.start(2)) + 1,
            "source_ids": list(data.get("source_ids", [])),
            "relations": list(data.get("relations", [])),
        }
    return entries


def source_lines(body: str) -> list[tuple[int, str]]:
    return [
        (body.count("\n", 0, match.start()) + 1, match.group(1))
        for match in SOURCE_LINE.finditer(body)
    ]


def body_paragraphs(body: str) -> list[tuple[int, str]]:
    """Paragraphs with the 1-based line where each starts."""
    paragraphs: list[tuple[int, str]] = []
    current: list[str] = []
    start = 1
    line = 1
    for raw in body.splitlines():
        stripped = raw.strip()
        if not stripped:
            if current:
                paragraphs.append((start, " ".join(current)))
                current = []
            line += 1
            continue
        if not current:
            start = line
        current.append(raw)
        line += 1
    if current:
        paragraphs.append((start, " ".join(current)))
    return paragraphs


def readable_paragraph(text: str) -> bool:
    if len(text) < MIN_PARAGRAPH_CHARS:
        return False
    if text.lstrip().startswith(("#", "**Sources:**", "|", ":::")):
        return False
    return len(normalize(text).split()) >= MIN_PARAGRAPH_WORDS


def trim(text: str, width: int = 220) -> str:
    text = " ".join(text.split())
    if len(text) <= width:
        return text
    return text[: width - 1].rstrip() + "…"


def markdown_cell(text: str) -> str:
    return text.replace("|", "\\|")


def main() -> int:
    if not PUBLICATIONS.is_file() or not ENTRY_DIR.is_dir():
        print("error: run from the corpus root", file=sys.stderr)
        return 2

    publications = tomllib.loads(PUBLICATIONS.read_text(encoding="utf-8")).get(
        "publication", []
    )
    by_id = {publication["id"]: publication for publication in publications}
    third_party = {
        publication["id"]
        for publication in publications
        if publication.get("third_party")
    }
    aliases = {
        publication["id"]: publication_aliases(publication)
        for publication in publications
        if publication["id"] in third_party
    }
    entries = read_entries()

    def is_third_party_source(source: str) -> bool:
        return source in third_party

    def third_party_only(entry: dict) -> bool:
        sources = entry["source_ids"]
        return bool(sources) and all(is_third_party_source(source) for source in sources)

    def non_third_party(entry: dict) -> bool:
        return not any(is_third_party_source(source) for source in entry["source_ids"])

    def mixed(entry: dict) -> bool:
        sources = entry["source_ids"]
        return any(is_third_party_source(source) for source in sources) and any(
            not is_third_party_source(source) for source in sources
        )

    def named_in_sources(source_line: str, publication_id: str) -> bool:
        normalized = normalize(source_line)
        return any(alias in normalized for alias in aliases[publication_id])

    def file_line(entry: dict, body_line: int) -> int:
        return entry["body_line"] + body_line - 1

    # (a) source_ids against body Source lines.
    stale: list[tuple[dict, str, list[int]]] = []
    uncited: list[tuple[dict, str, list[int]]] = []
    for entry in entries.values():
        lines = source_lines(entry["body"])
        for publication_id in sorted(third_party):
            listed = publication_id in entry["source_ids"]
            printed = [line for line, text in lines if named_in_sources(text, publication_id)]
            if listed and not printed:
                stale.append(
                    (entry, publication_id, [file_line(entry, line) for line, _ in lines])
                )
            if printed and not listed:
                uncited.append(
                    (entry, publication_id, [file_line(entry, line) for line in printed])
                )

    # (b) uncited third-party text in non-third-party bodies.
    third_party_paragraphs: list[tuple[str, int, str, str]] = []
    index: dict[tuple[str, ...], list[int]] = defaultdict(list)
    for entry in entries.values():
        if not third_party_only(entry):
            continue
        for line, raw in body_paragraphs(entry["body"]):
            if not readable_paragraph(raw):
                continue
            normalized = normalize(raw)
            position = len(third_party_paragraphs)
            third_party_paragraphs.append(
                (entry["id"], file_line(entry, line), raw, normalized)
            )
            words = normalized.split()
            if len(words) >= SHINGLE_WORDS:
                for start in range(len(words) - SHINGLE_WORDS + 1):
                    shingle = tuple(words[start : start + SHINGLE_WORDS])
                    if len(index[shingle]) < MAX_POSTING:
                        index[shingle].append(position)

    exact: list[tuple[dict, int, str, int, str]] = []
    near: list[tuple[dict, int, str, int, str, float]] = []
    third_party_by_key: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    for entry_id, line, raw, normalized in third_party_paragraphs:
        third_party_by_key[normalized].append((entry_id, line, raw))

    for entry in entries.values():
        if not non_third_party(entry):
            continue
        for line, raw in body_paragraphs(entry["body"]):
            if not readable_paragraph(raw):
                continue
            normalized = normalize(raw)
            duplicates = third_party_by_key.get(normalized)
            if duplicates:
                other_id, other_line, _ = duplicates[0]
                exact.append(
                    (entry, file_line(entry, line), raw, other_line, other_id)
                )
                continue
            words = normalized.split()
            if len(words) < SHINGLE_WORDS:
                continue
            counts: Counter[int] = Counter()
            for start in range(len(words) - SHINGLE_WORDS + 1):
                shingle = tuple(words[start : start + SHINGLE_WORDS])
                for position in index.get(shingle, []):
                    counts[position] += 1
            if not counts:
                continue
            best_position, _ = counts.most_common(1)[0]
            other_id, other_line, other_raw, other_normalized = third_party_paragraphs[
                best_position
            ]
            length_ratio = min(len(normalized), len(other_normalized)) / max(
                len(normalized), len(other_normalized)
            )
            if length_ratio < NEAR_LENGTH_RATIO:
                continue
            ratio = SequenceMatcher(None, normalized, other_normalized).ratio()
            if ratio >= NEAR_RATIO:
                near.append(
                    (entry, file_line(entry, line), raw, other_line, other_id, ratio)
                )

    # (c) links and relations from a non-third-party entry to a third-party-only entry.
    bad_links: list[tuple[dict, str, str, int]] = []
    bad_relations: list[tuple[dict, str, str, str, int]] = []
    for entry in entries.values():
        if not non_third_party(entry):
            continue
        for match in LINK.finditer(entry["body"]):
            target_id = match.group(1)
            target = entries.get(target_id)
            if target is not None and third_party_only(target):
                line = entry["body"].count("\n", 0, match.start()) + 1
                bad_links.append(
                    (entry, target_id, match.group(0), file_line(entry, line))
                )
        for relation in entry["relations"]:
            target_id = relation.get("target", "")
            target = entries.get(target_id)
            if target is not None and third_party_only(target):
                line = entry["front"].count("\n", 0, entry["front"].find(f'"{target_id}"')) + 2
                bad_relations.append(
                    (entry, relation.get("kind", "?"), target_id, relation.get("label", ""), line)
                )

    # (d) third-party-only entries placed in another publication's book tree.
    books_text = BOOKS.read_text(encoding="utf-8")
    books = tomllib.loads(books_text).get("books", [])
    placements: list[tuple[str, str, int, str]] = []
    for book in books:
        book_source = book.get("source", "")

        def walk(nodes: list[dict]) -> None:
            for node in nodes:
                entry_id = node.get("entry")
                if entry_id and entry_id in entries and third_party_only(entries[entry_id]):
                    entry = entries[entry_id]
                    if book_source not in entry["source_ids"]:
                        offset = books_text.find(f'entry = "{entry_id}"')
                        line = books_text.count("\n", 0, offset) + 1
                        placements.append((book_source, entry_id, line, node.get("title", "")))
                walk(node.get("children", []))

        walk(book.get("chapters", []))

    # (e) mixed third-party and Paizo source_ids.
    mixed_entries = [entry for entry in entries.values() if mixed(entry)]

    def has_third_party_edge(entry: dict) -> bool:
        return any(
            relation.get("kind") in ("addon", "revision") for relation in entry["relations"]
        )

    print("# Third-party contamination audit\n")
    print(
        f"Corpus: {len(entries)} entries, {len(publications)} publications, "
        f"{len(books)} books. Third-party publications: {len(third_party)}.\n"
    )
    print("| Publication | Entries with this source | Third-party-only entries |")
    print("|---|---:|---:|")
    for publication_id in sorted(third_party):
        with_source = sum(publication_id in entry["source_ids"] for entry in entries.values())
        only = sum(
            entry["source_ids"] == [publication_id] for entry in entries.values()
        )
        title = by_id[publication_id]["title"]
        print(f"| `{publication_id}` ({markdown_cell(title)}) | {with_source} | {only} |")

    print("\n## (a) `source_ids` against body Source lines\n")
    print(f"- A third-party id in `source_ids` with no body Source line citing it: **{len(stale)}**")
    if stale:
        print("\n| Entry | Publication | Source lines |")
        print("|---|---|---|")
        for entry, publication_id, lines in stale:
            line_list = ", ".join(str(line) for line in lines) or "none"
            print(
                f"| `{entry['id']}` | `{publication_id}` | {line_list} |"
            )
    print(
        f"\n- A body Source line citing a third-party publication whose id is not in "
        f"`source_ids`: **{len(uncited)}**"
    )
    if uncited:
        print("\n| Entry | Publication | Source line |")
        print("|---|---|---:|")
        for entry, publication_id, lines in uncited:
            print(
                f"| `{entry['id']}` | `{publication_id}` | "
                f"{', '.join(str(line) for line in lines)} |"
            )

    print("\n## (b) Uncited third-party text in non-third-party bodies\n")
    print(
        f"Compared long paragraphs (at least {MIN_PARAGRAPH_CHARS} characters and "
        f"{MIN_PARAGRAPH_WORDS} words) against {len(third_party_paragraphs)} paragraphs "
        f"from third-party-only entries. A near match has normalized-length ratio at "
        f"least {NEAR_LENGTH_RATIO:.0%} and similarity at least {NEAR_RATIO:.0%}."
    )
    print(f"\n- Exact matches: **{len(exact)}**")
    if exact:
        print("\n| Entry | Line | Third-party entry | Third-party line | Text |")
        print("|---|---:|---|---:|---|")
        for entry, line, raw, other_line, other_id in exact:
            print(
                f"| `{entry['id']}` | {line} | `{other_id}` | {other_line} | "
                f"{markdown_cell(trim(raw))} |"
            )
    print(f"\n- Near matches: **{len(near)}**")
    if near:
        print("\n| Entry | Line | Third-party entry | Third-party line | Similarity | Text |")
        print("|---|---:|---|---:|---:|---|")
        for entry, line, raw, other_line, other_id, ratio in near:
            print(
                f"| `{entry['id']}` | {line} | `{other_id}` | {other_line} | "
                f"{ratio:.0%} | {markdown_cell(trim(raw))} |"
            )

    print("\n## (c) Links and relations from non-third-party entries\n")
    print(f"- Body links to third-party-only entries: **{len(bad_links)}**")
    if bad_links:
        print("\n| Entry | Line | Target | Link |")
        print("|---|---:|---|---|")
        for entry, target_id, link, line in bad_links:
            print(f"| `{entry['id']}` | {line} | `{target_id}` | `{link}` |")
    print(f"\n- Relations to third-party-only entries: **{len(bad_relations)}**")
    if bad_relations:
        print("\n| Entry | Line | Kind | Target | Label |")
        print("|---|---:|---|---|---|")
        for entry, kind, target_id, label, line in bad_relations:
            print(
                f"| `{entry['id']}` | {line} | `{kind}` | `{target_id}` | "
                f"`{label or ''}` |"
            )

    print("\n## (d) Third-party-only entries in other book trees\n")
    print(f"- Placements outside their own publication's book: **{len(placements)}**")
    if placements:
        print("\n| Book source | Entry | books.toml line | Node title |")
        print("|---|---|---:|---|")
        for book_source, entry_id, line, title in placements:
            print(
                f"| `{book_source}` | `{entry_id}` | {line} | {markdown_cell(title)} |"
            )

    print("\n## (e) Entries mixing third-party and Paizo `source_ids`\n")
    print(f"- Mixed entries: **{len(mixed_entries)}**")
    if mixed_entries:
        print("\n| Entry | Sources | Holds an add-on/revision edge |")
        print("|---|---|---|")
        for entry in sorted(mixed_entries, key=lambda item: item["id"]):
            sources = ", ".join(f"`{source}`" for source in entry["source_ids"])
            edge = "yes" if has_third_party_edge(entry) else "no"
            print(f"| `{entry['id']}` | {sources} | {edge} |")

    print("\n## Summary\n")
    total = (
        len(stale)
        + len(uncited)
        + len(exact)
        + len(near)
        + len(bad_links)
        + len(bad_relations)
        + len(placements)
        + len(mixed_entries)
    )
    print(f"Total findings: **{total}**.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
