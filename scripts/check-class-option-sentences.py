#!/usr/bin/env python3
"""Check written class-option sentences against the reviewed print proposals in both directions."""
from __future__ import annotations

import argparse
import re
import tomllib
from pathlib import Path


NEGATIONS = re.compile(r"\b(?:not|no|never|cannot)\b|n't", re.I)
DIGITS = re.compile(r"\d+")
SENTENCES = re.compile(r"(?<=[.!?])[\"’”)]*\s+|\n+\s*\n+")


def plain(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^\s*#{1,6}\s+.*$", "", text, flags=re.M)
    text = re.sub(r"[*_`~]", "", text)
    text = re.sub(r"\\([\\`*_{}\[\]()#+.!-])", r"\1", text)
    return " ".join(text.split())


def sentences(text: str) -> list[str]:
    return [x.strip() for x in SENTENCES.split(plain(text)) if len(re.findall(r"[A-Za-z]", x)) >= 8]


def edit_distance(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def near_match(a: str, b: str) -> bool:
    da, db = DIGITS.findall(a), DIGITS.findall(b)
    na, nb = len(NEGATIONS.findall(a)), len(NEGATIONS.findall(b))
    if da != db or na != nb:
        return False
    letters_a = "".join(re.findall(r"[a-z]", a.casefold()))
    letters_b = "".join(re.findall(r"[a-z]", b.casefold()))
    return edit_distance(letters_a, letters_b) <= 2


def match_count(source: list[str], target: list[str]) -> int:
    remaining = list(target)
    found = 0
    for sentence in source:
        exact = next((i for i, candidate in enumerate(remaining) if plain(sentence).casefold() == plain(candidate).casefold()), None)
        candidate = exact if exact is not None else next((i for i, item in enumerate(remaining) if near_match(sentence, item)), None)
        if candidate is not None:
            remaining.pop(candidate)
            found += 1
    return found


def self_test() -> int:
    checks = [
        (near_match("The target is affected.", "The target is aff ected."), True),
        (near_match("At 2nd level, the power lasts.", "At 3rd level, the power lasts."), False),
        (near_match("The target is not immune.", "The target is immune."), False),
        (match_count(["A sentence.", "A sentence."], ["A sentence."]), 1),
    ]
    for actual, expected in checks:
        if actual != expected:
            raise AssertionError(f"sentence-check self-test: got {actual!r}, expected {expected!r}")
    print(f"self-test: {len(checks)} checks passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", nargs="?", default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument("--book", default="advanced-class-guide")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    corpus = Path(args.corpus)
    directory = corpus / "scripts" / "class-options"
    ledger = list(__import__("csv").DictReader((directory / f"540-{args.book}.tsv").open(), delimiter="\t"))
    proposals = tomllib.loads((directory / f"540-{args.book}.proposals.toml").read_text(encoding="utf-8"))
    printed = {(r["id"], r["anchor"]): r["print"] for r in proposals.get("entry", [])}
    paths = {}
    for path in (corpus / "entries").rglob("*.md"):
        head = path.read_text(encoding="utf-8").split("+++", 2)[1]
        found = re.search(r'^id = "([^"]+)"', head, re.M)
        if found:
            paths[found.group(1)] = path
    p_sentences: list[str] = []
    e_sentences: list[str] = []
    missing = []
    for row in ledger:
        if row["status"] != "written":
            continue
        key = (row["entry"], row["anchor"])
        entry_path = paths.get(row["entry"])
        if not entry_path or key not in printed:
            missing.append(row["entry"])
            continue
        body = entry_path.read_text(encoding="utf-8").split("+++", 2)[2]
        p_sentences.extend(sentences(printed[key]))
        e_sentences.extend(sentences(body))
    p_to_e = match_count(p_sentences, e_sentences)
    e_to_p = match_count(e_sentences, p_sentences)
    print(f"print → entry: {p_to_e} of {len(p_sentences)} sentences")
    print(f"entry → print: {e_to_p} of {len(e_sentences)} sentences")
    if missing:
        print("missing proposal or entry: " + ", ".join(sorted(set(missing))))
        return 1
    return 0 if p_to_e == len(p_sentences) and e_to_p == len(e_sentences) else 1


if __name__ == "__main__":
    raise SystemExit(main())
