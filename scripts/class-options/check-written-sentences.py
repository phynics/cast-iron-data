#!/usr/bin/env python3
"""Check that written class-option bodies and their print proposals contain the same sentences."""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from pathlib import Path


def plain(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\\([*])", r"\1", text)
    text = text.replace("**", "").replace("_", "")
    return " ".join(text.split()).casefold()


def sentences(text: str) -> list[str]:
    text = plain(text)
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+(?=[a-z0-9])", text) if part.strip()]


def is_covered(sentence: str, body: str) -> bool:
    return sentence in body


def source_page(front: str, book: str) -> str:
    match = re.search(rf'publication = "{re.escape(book)}"[^\n]*\npage = "([^"]+)"', front)
    return match.group(1) if match else ""


def self_test() -> int:
    checks = [
        ("A linked [rule](ref/rule) applies.", ["a linked rule applies."]),
        ("A first sentence. A second sentence!", ["a first sentence.", "a second sentence!"]),
        ("An unlinked sentence.", ["an unlinked sentence."]),
    ]
    for source, want in checks:
        got = sentences(source)
        if got != want:
            print(f"FAIL: {source!r}: {got!r} != {want!r}")
            return 1
    if is_covered("an absent sentence.", "a nearby sentence."):
        print("FAIL: a near miss counted as covered")
        return 1
    if is_covered("an entry-only sentence.", "the print proposal"):
        print("FAIL: an entry-only sentence counted as present in print")
        return 1
    print(f"self-test: {len(checks) + 2} checks passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("corpus", type=Path, nargs="?", default=Path("."))
    ap.add_argument("book", nargs="?", default="")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    base = args.corpus / "scripts/class-options"
    rows = (base / f"540-{args.book}.tsv").read_text(encoding="utf-8").splitlines()
    header = rows[0].split("\t")
    ledger = [dict(zip(header, row.split("\t"))) for row in rows[1:] if row.strip()]
    proposals = tomllib.loads((base / f"540-{args.book}.proposals.toml").read_text(encoding="utf-8"))
    written = [r for r in ledger if r["status"] == "written" and r["shape"] == "single"]
    entries = {}
    pages = {}
    for path in (args.corpus / "entries").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        body = text.split("+++\n", 2)
        if len(body) == 3:
            match = re.search(r'^id = "([^"]+)"$', body[1], re.M)
            if match:
                entries[match.group(1)] = plain(body[2])
                pages[match.group(1)] = source_page(body[1], args.book)
    print_found = print_total = entry_found = entry_total = 0
    page_matches = 0
    exceptions = []
    for row in written:
        try:
            body = entries[row["entry"]]
            text = next(f["print"] for f in proposals["entry"]
                        if f["id"] == row["entry"] and f["anchor"] == row["anchor"])
        except (StopIteration, KeyError):
            exceptions.append(f"{row['entry']}#{row['anchor']}: missing entry or proposal")
            continue
        if row.get("page") and pages.get(row["entry"]) == row["page"]:
            page_matches += 1
        else:
            exceptions.append(f"PAGE {row['entry']}: ledger page {row.get('page')!r}, entry page {pages.get(row['entry'])!r}")
        printed_sentences = sentences(text)
        entry_sentences = sentences(body)
        for sentence in printed_sentences:
            print_total += 1
            if is_covered(sentence, body):
                print_found += 1
            else:
                exceptions.append(f"PRINT -> ENTRY {row['entry']}#{row['anchor']}: not found: {sentence}")
        for sentence in entry_sentences:
            entry_total += 1
            if is_covered(sentence, plain(text)):
                entry_found += 1
            else:
                exceptions.append(f"ENTRY -> PRINT {row['entry']}#{row['anchor']}: extra: {sentence}")
    print(f"Print -> entry: {print_found} of {print_total} sentences found in {len(written)} written entries")
    print(f"Entry -> print: {entry_found} of {entry_total} sentences found in print proposals")
    print(f"Page metadata: {page_matches} of {len(written)} written entries match the ledger")
    for exc in exceptions:
        print(f"EXCEPTION: {exc}")
    return 1 if exceptions else 0


if __name__ == "__main__":
    sys.exit(main())
