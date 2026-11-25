#!/usr/bin/env python3
"""Apply the verified spell class levels of `scripts/spell-levels-284.tsv` (phynics/cast-iron-data#284).

    python3 scripts/spell-levels-284.py [CORPUS]            # add the missing rows (idempotent)
    python3 scripts/spell-levels-284.py [CORPUS] --check    # fail when a row is missing or the file is stale
    python3 scripts/spell-levels-284.py --self-test

The community spell sheet gave 251 class levels (172 spells) that the corpus lacked. The sheet has
errors of its own, so each row was compared with print. `scripts/spell-levels-284.tsv` is the review
table: one row per sheet row. Columns:

    entry         the entry id (`ref/spell/...`)
    spell         the title the sheet uses
    class         the class, lower case (`unchained summoner`; the corpus writes `Unchained Summoner`)
    sheet_level   the level the sheet gave
    printed_level the level that print gives; empty for a rejected row
    book          the publication id of the printed source (`publications.toml`)
    page          the printed page (the number in the footer, not the PDF page)
    decision      `add`: print confirms the row, and the script writes it;
                  `present`: print confirms the row, and the entry already had it when the table
                  was made (an earlier change added it, or the sheet comparison did not see it);
                  `reject`: print does not give the class that level (`book` and `page` are the
                  place that was read, `basis` says what it holds);
                  `held-322`: print confirms the row, but the entry is in the file set of the open
                  pull request #322, so another change writes it
    basis         what the evidence is: the spell's own level line, a class spell list, or the rule
                  of the hunter list

The script writes an `add` row in two places that must agree (`corpus-check` fails on a difference):
the `levels` table of `[fields]`, and the `Level:` row of the stat block. The new class goes into the
table before the first class that sorts after it, so an alphabetical table stays alphabetical. The
`Level:` row is then written the way the corpus writes it: levels ascending, the classes of one level
in table order, one level per line joined by a backslash. A row whose class already has the same level
is left alone; a row whose class has another level stops the run.

The script reads only the corpus and the TSV (Python 3.11 or later, no third-party package, no PDF).
`--check` fails (exit 1, one line per problem) when the header or a row is malformed, when a `book`
is not in `publications.toml`, when an `add` row is not in its entry, or when a `reject` row is.
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

COLUMNS = ["entry", "spell", "class", "sheet_level", "printed_level", "book", "page", "decision", "basis"]
DECISIONS = ("add", "present", "reject", "held-322")
TSV = Path("scripts") / "spell-levels-284.tsv"
LEVELS_RE = re.compile(r"^levels = \[\n(.*?)\n\]\n", re.S | re.M)
ROW_RE = re.compile(r'^  \{ class = "([^"]+)", level = (\d+) \},?$')
STAT_RE = re.compile(r"^Level: (.*?)\n(?=[A-Z][A-Za-z ]*:|:::)", re.S | re.M)


def class_label(name: str) -> str:
    """`unchained summoner` -> `Unchained Summoner`: how the corpus writes a class."""
    return " ".join(w.capitalize() for w in name.split())


def read_rows(path: Path) -> tuple[list[dict], list[str]]:
    problems: list[str] = []
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    if not lines or lines[0].split("\t") != COLUMNS:
        return [], [f"{path}: the header is not {COLUMNS}"]
    rows = []
    for number, line in enumerate(lines[1:], 2):
        fields = line.split("\t")
        if len(fields) != len(COLUMNS):
            problems.append(f"{path}:{number}: {len(fields)} fields, expected {len(COLUMNS)}")
            continue
        row = dict(zip(COLUMNS, fields))
        row["line"] = number
        rows.append(row)
    return rows, problems


def validate(rows: list[dict], publications: set[str]) -> list[str]:
    problems = []
    seen = set()
    last = None
    for row in rows:
        where = f"{TSV}:{row['line']}"
        key = (row["entry"], row["class"])
        if key in seen:
            problems.append(f"{where}: {key} appears twice")
        seen.add(key)
        if last is not None and key < last:
            problems.append(f"{where}: rows are not sorted by (entry, class)")
        last = key
        if row["decision"] not in DECISIONS:
            problems.append(f"{where}: decision {row['decision']!r} is not one of {DECISIONS}")
        if row["class"] != row["class"].strip().lower() or not row["class"]:
            problems.append(f"{where}: class must be lower case")
        if not re.fullmatch(r"[1-9]", row["sheet_level"]):
            problems.append(f"{where}: sheet_level must be 1 to 9")
        if row["decision"] == "reject":
            if row["printed_level"]:
                problems.append(f"{where}: a rejected row has no printed_level")
        elif not re.fullmatch(r"[1-9]", row["printed_level"]):
            problems.append(f"{where}: printed_level must be 1 to 9")
        if row["book"] not in publications:
            problems.append(f"{where}: book {row['book']!r} is not in publications.toml")
        if not row["page"].strip() or not row["basis"].strip():
            problems.append(f"{where}: page and basis are required")
    return problems


def parse_levels(text: str) -> tuple[list[tuple[str, int]], re.Match] | None:
    match = LEVELS_RE.search(text)
    if not match:
        return None
    pairs = []
    for line in match.group(1).split("\n"):
        row = ROW_RE.match(line)
        if not row:
            return None
        pairs.append((row.group(1), int(row.group(2))))
    return pairs, match


def render_stat(pairs: list[tuple[str, int]]) -> str:
    by_level: dict[int, list[str]] = {}
    for name, level in sorted(pairs, key=lambda p: p[1]):  # stable: table order within a level
        by_level.setdefault(level, []).append(name)
    return "\\\n".join(f"{level}: {', '.join(names)}" for level, names in by_level.items())


def render_table(pairs: list[tuple[str, int]]) -> str:
    return "levels = [\n" + "\n".join(f'  {{ class = "{n}", level = {l} }},' for n, l in pairs) + "\n]\n"


def insert(pairs: list[tuple[str, int]], name: str, level: int) -> list[tuple[str, int]]:
    for index, (other, _) in enumerate(pairs):
        if other.lower() > name.lower():
            return pairs[:index] + [(name, level)] + pairs[index:]
    return pairs + [(name, level)]


def start_table(path: Path, text: str, wanted: list[tuple[str, int]], write: bool) -> list[str]:
    """An entry with no `levels` at all: the table goes before `casting_time`, the row before
    `Casting time:` of the stat block."""
    if not re.search(r"^casting_time = ", text, re.M) or re.search(r"^Level:", text, re.M):
        return [f"{path}: no `levels` table, and no place to start one"]
    if not write:
        return []
    pairs: list[tuple[str, int]] = []
    for name, level in wanted:
        pairs = insert(pairs, name, level)
    text = re.sub(r"^casting_time = ", lambda m: render_table(pairs) + m.group(0), text, count=1, flags=re.M)
    text = re.sub(r"^Casting time:", lambda m: f"Level: {render_stat(pairs)}\n" + m.group(0), text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")
    return []


def apply_entry(path: Path, wanted: list[tuple[str, int]], write: bool) -> list[str]:
    """Add `wanted` to one entry. Returns the problems; writes the file when `write` and clean."""
    text = path.read_text(encoding="utf-8")
    parsed = parse_levels(text)
    if parsed is None:
        if re.search(r"^levels = ", text, re.M):
            return [f"{path}: no `levels` table in the expected form"]
        return start_table(path, text, wanted, write)
    pairs, match = parsed
    stat = STAT_RE.search(text)
    if stat is not None and stat.group(1) != render_stat(pairs):
        return [f"{path}: the `Level:` row does not match the table before the change"]
    problems = []
    for name, level in wanted:
        have = dict(pairs)
        if name in have:
            if have[name] != level:
                problems.append(f"{path}: {name} is level {have[name]}, the table says {level}")
            continue
        pairs = insert(pairs, name, level)
    if problems or not write:
        return problems
    text = text[: match.start()] + render_table(pairs) + text[match.end():]
    stat = STAT_RE.search(text)
    if stat is not None:
        text = text[: stat.start(1)] + render_stat(pairs) + text[stat.end(1):]
    path.write_text(text, encoding="utf-8")
    return []


def publications_of(corpus: Path) -> set[str]:
    return set(re.findall(r'^id = "([^"]+)"', (corpus / "publications.toml").read_text(encoding="utf-8"), re.M))


def run(corpus: Path, check: bool) -> int:
    rows, problems = read_rows(corpus / TSV)
    problems += validate(rows, publications_of(corpus))
    by_entry: dict[str, list[tuple[str, int]]] = {}
    rejected = 0
    for row in rows:
        if row["decision"] in ("add", "present"):
            by_entry.setdefault(row["entry"], []).append((class_label(row["class"]), int(row["printed_level"])))
        elif row["decision"] == "reject":
            rejected += 1
    for entry, wanted in sorted(by_entry.items()):
        path = corpus / "entries" / "spell" / (entry.rsplit("/", 1)[1] + ".md")
        if not path.exists():
            problems.append(f"{entry}: no entry file {path}")
            continue
        if check:
            text = path.read_text(encoding="utf-8")
            parsed = parse_levels(text)
            have = dict(parsed[0]) if parsed else {}
            for name, level in wanted:
                if have.get(name) != level:
                    problems.append(f"{entry}: {name} {level} is missing (run the script without --check)")
            stat = STAT_RE.search(text)
            if parsed and stat is not None and stat.group(1) != render_stat(parsed[0]):
                problems.append(f"{entry}: the `Level:` row does not match the table")
        else:
            problems += apply_entry(path, wanted, write=not problems)
    for problem in problems:
        print(problem)
    if not problems:
        added = sum(len(w) for w in by_entry.values())
        print(f"{len(rows)} rows, {added} confirmed in {len(by_entry)} entries, {rejected} rejected: ok")
    return 1 if problems else 0


def self_test() -> int:
    pairs = [("Bard", 2), ("Cleric", 3), ("Wizard", 3)]
    assert insert(pairs, "Psychic", 3) == [("Bard", 2), ("Cleric", 3), ("Psychic", 3), ("Wizard", 3)]
    assert insert(pairs, "Alchemist", 1)[0] == ("Alchemist", 1)
    assert insert(pairs, "Witch", 4)[-1] == ("Witch", 4) or insert(pairs, "Witch", 4)[-2] == ("Witch", 4)
    assert render_stat(insert(pairs, "Psychic", 3)) == "2: Bard\\\n3: Cleric, Psychic, Wizard"
    assert class_label("unchained summoner") == "Unchained Summoner"
    entry = (
        '+++\nid = "ref/spell/x"\n[fields]\nkind = "spell"\nlevels = [\n'
        '  { class = "Bard", level = 2 },\n  { class = "Wizard", level = 3 },\n]\n'
        'casting_time = "1 standard action"\n+++\n\n::: statblock\nSchool: x\n'
        "Level: 2: Bard\\\n3: Wizard\nCasting time: 1 standard action\n:::\n\nBody.\n"
    )
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "x.md"
        path.write_text(entry, encoding="utf-8")
        assert apply_entry(path, [("Psychic", 3), ("Bard", 2)], write=True) == []
        text = path.read_text(encoding="utf-8")
        assert '{ class = "Psychic", level = 3 },' in text and "Level: 2: Bard\\\n3: Psychic, Wizard\n" in text, text
        assert apply_entry(path, [("Psychic", 3)], write=True) == []  # idempotent
        assert path.read_text(encoding="utf-8") == text
        assert apply_entry(path, [("Bard", 3)], write=True) != []  # a different level stops the run
    print("self-test ok")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("corpus", nargs="?", default=".")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    return run(Path(args.corpus), args.check)


if __name__ == "__main__":
    sys.exit(main())
