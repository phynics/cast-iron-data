#!/usr/bin/env python3
"""Prove the sources-field migration preserved every removed Sources line.

For each entry that now carries `[[sources]]`, the script reads the original file from a git
ref (default `origin/main`), extracts the leading Sources paragraph, parses it with the same
reviewed title map, and requires the stored rows to equal that parse. It also renders the rows
back to text and compares it with the removed line, normalized for whitespace and punctuation.
Printed titles that differ from the catalogue title (an alias, such as `PRPG Core Rulebook`)
are reported separately.

Run from the corpus root:

    python3 scripts/sources-field-proof.py [--base origin/main]
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "sources-field.py"

spec = importlib.util.spec_from_file_location("sources_field", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def render(citations, publications) -> str:
    parts = []
    for citation in citations:
        title = publications.get(citation.publication, citation.publication)
        if citation.page:
            parts.append(f"{title} p. {citation.page}")
        else:
            parts.append(title)
    return "; ".join(parts)


def text_key(value: str) -> str:
    value = value.lower()
    value = re.sub(r"\b(?:pg|p|page)\.?\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def original_text(relative: str, base: str) -> str | None:
    try:
        return subprocess.run(
            ["git", "show", f"{base}:{relative}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except subprocess.CalledProcessError:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="origin/main", help="git ref holding the pre-migration files")
    options = parser.parse_args()
    publications = module.load_publications()
    titles = module.title_map(publications)
    checked = exact = aliased = 0
    failures: list[str] = []
    for path in sorted(module.ENTRIES.rglob("*.md")):
        relative = path.relative_to(ROOT).as_posix()
        current = path.read_text(encoding="utf-8")
        try:
            front, _ = module.split_front(current)
        except ValueError:
            continue
        stored_rows = module.front_sources(front)
        if not stored_rows:
            continue
        stored = [
            module.Citation(row["publication"], row.get("page")) for row in stored_rows
        ]
        base_text = original_text(relative, options.base)
        if base_text is None:
            failures.append(f"{relative}: not present in {options.base}")
            continue
        try:
            base_front, base_body = module.split_front(base_text)
        except ValueError:
            failures.append(f"{relative}: original has no front matter")
            continue
        blocks = module.split_blocks(base_body)
        index = module.sources_index(blocks)
        if index is None or not all(
            module.is_header_block(block) for block in blocks[:index]
        ):
            failures.append(f"{relative}: original has no leading Sources block")
            continue
        raw, _ = module.sources_text(blocks[index])
        raw = re.sub(r"^\*\*Sources?:\*\*\s*", "", raw)
        parsed, unmapped = module.parse_citations(raw, titles)
        checked += 1
        if unmapped:
            failures.append(f"{relative}: original has unmapped titles {unmapped}")
            continue
        if parsed != stored:
            failures.append(
                f"{relative}: stored {stored!r} does not match the removed line {parsed!r}"
            )
            continue
        if text_key(raw) == text_key(render(stored, publications)):
            exact += 1
        else:
            aliased += 1
    print(f"checked: {checked}")
    print(f"reproduced exactly after normalization: {exact}")
    print(f"reproduced through a reviewed title alias: {aliased}")
    if failures:
        print(f"failures: {len(failures)}")
        for failure in failures:
            print(f"  {failure}")
        return 1
    print("proof: every converted entry reproduces its removed Sources line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
