#!/usr/bin/env python3
"""Check written class-option sentences against the reviewed print proposals in both directions."""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
import tomllib
from pathlib import Path


RULES_PATH = Path(__file__).with_name("feature-prose-540-class-options.py")
RULES_SPEC = importlib.util.spec_from_file_location("class_option_sentence_rules", RULES_PATH)
if RULES_SPEC is None or RULES_SPEC.loader is None:
    raise RuntimeError(f"cannot load shared class-option sentence rules: {RULES_PATH}")
RULES = importlib.util.module_from_spec(RULES_SPEC)
sys.modules[RULES_SPEC.name] = RULES
RULES_SPEC.loader.exec_module(RULES)

DIGITS = re.compile(r"\d+")
WORDS = re.compile(r"[a-z]+(?:['’][a-z]+)?|\d+", re.I)
SENTENCES = re.compile(r"(?<=[.!?])[\"’”)]*\s+|\n+\s*\n+")


def plain(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^\s*#{1,6}\s+.*$", "", text, flags=re.M)
    text = re.sub(r"[*_`~]", "", text)
    text = re.sub(r"\\([\\`*_{}\[\]()#+.!-])", r"\1", text)
    return " ".join(text.split())


def sentences(text: str) -> list[str]:
    return [x.strip() for x in SENTENCES.split(plain(text)) if len(re.findall(r"[A-Za-z]", x)) >= 8]


def near_match(a: str, b: str) -> bool:
    if DIGITS.findall(a) != DIGITS.findall(b) or len(RULES.NEGATIONS.findall(a)) != len(RULES.NEGATIONS.findall(b)):
        return False
    words_a = WORDS.findall(a.casefold())
    words_b = WORDS.findall(b.casefold())
    if len(words_a) != len(words_b):
        return False
    changed = [(x, y) for x, y in zip(words_a, words_b) if x != y]
    return (len(changed) == 1 and min(len(changed[0][0]), len(changed[0][1])) >= 6
            and RULES.one_misprint(*changed[0]))


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
        (near_match("The target is affected.", "The target is affectd."), True),
        (near_match("The target is affected.", "The target is aff ected."), False),
        (near_match("The effect may work.", "The effect can work."), False),
        (near_match("At 2nd level, the power lasts.", "At 3rd level, the power lasts."), False),
        (near_match("The target is not immune.", "The target is immune."), False),
        (near_match("The target isn’t immune.", "The target is immune."), False),
        (near_match("The creature will increase its speed.", "The creature will decrease its speed."), False),
        (near_match("The target is either visible or audible.", "The target is neither visible or audible."), False),
        (near_match("The target is able to see the bard.", "The target is unable to see the bard."), False),
        (near_match("The effect lasts longer than one round.", "The effect lasts longer then one round."), False),
        (near_match("The swift action begins the effect.", "The shift action begins the effect."), False),
        (near_match("The creature can move freely.", "The creature can more freely."), False),
        (near_match("The creature gains a free action.", "The creature gains a fire action."), False),
        (near_match("The target is neither visible nor audible.", "The target is visible nor audible."), False),
        (near_match("The target is visible nor audible.", "The target is visible audible."), False),
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
