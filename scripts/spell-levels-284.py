#!/usr/bin/env python3
"""Apply the verified spell class levels of `scripts/spell-levels-284.tsv` (phynics/cast-iron-data#284).

    python3 scripts/spell-levels-284.py [CORPUS]            # write the rows (idempotent)
    python3 scripts/spell-levels-284.py [CORPUS] --check    # fail when an entry and the table disagree
    python3 scripts/spell-levels-284.py --self-test

The community spell sheet gave 251 class levels (172 spells) that the corpus lacked. The sheet has
errors of its own, so each row was compared with print. The corpus holds a class level only where
print states it, or where a printed rule derives it (owner rulings of 2026-11-25). The review table
`scripts/spell-levels-284.tsv` has one row per sheet row, and one row for each derived level and each
removal that the same pass found. Columns:

    entry         the entry id (`ref/spell/...`)
    spell         the title the sheet uses
    class         the class, lower case (`unchained summoner`; the corpus writes `Unchained Summoner`)
    sheet_level   the level the sheet gave; empty for a row that is not a sheet row
    printed_level the level the corpus holds after the row; empty for `reject` and `remove-unprinted`
    book          the publication id of the printed source (`publications.toml`)
    page          the printed page (the number in the footer, not the PDF page)
    decision      `add`: the level is printed, or derived by a printed rule, and the script writes it;
                  `present`: the same, and the entry already had it when the table was made;
                  `reject`: print does not give the class that level, and no rule derives it
                  (`book` and `page` are the place that was read);
                  `remove-unprinted`: the entry holds a level that no printing states and no rule
                  derives, and the script removes the class (`book` and `page` are the printing)
    basis         the evidence. A derived level names its rule and the printed level it starts from:
                  the oracle casts from the cleric list, the skald from the bard list, the hunter
                  list is the druid list to 6th level and the ranger list (the lower level wins)

The script writes a row in two places that must agree (`corpus-check` fails on a difference): the
`levels` table of `[fields]`, and the `Level:` row of the stat block. A new class goes into the table
before the first class that sorts after it, so an alphabetical table stays alphabetical. The `Level:`
row is then written the way the corpus writes it: levels ascending, the classes of one level in table
order, one level per line joined by a backslash. A row whose class already has the same level is left
alone; an `add` row whose class has another level stops the run. The script reads and checks every
entry before it writes one, so a conflict leaves the corpus as it was.

The script reads only the corpus and the TSV (Python 3.11 or later, no third-party package, no PDF).
`--check` fails (exit 1, one line per problem) when the header or a row is malformed, when a `book` is
not in `publications.toml`, when an `add` or `present` row is not in its entry, when a
`remove-unprinted` class is still in its entry, or when a `reject` row's sheet level is in its entry.
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from pathlib import Path

COLUMNS = ["entry", "spell", "class", "sheet_level", "printed_level", "book", "page", "decision", "basis"]
DECISIONS = ("add", "present", "reject", "remove-unprinted")
TSV = Path("scripts") / "spell-levels-284.tsv"
LEVELS_RE = re.compile(r"^levels = \[\n(.*?)\n\]\n", re.S | re.M)
ROW_RE = re.compile(r'^  \{ class = "([^"]+)", level = (\d+) \},?$')
STAT_RE = re.compile(r"^Level: (.*?)\n(?=[A-Z][A-Za-z ]*:|:::)", re.S | re.M)

Pairs = list[tuple[str, int]]


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
        decision = row["decision"]
        if decision not in DECISIONS:
            problems.append(f"{where}: decision {decision!r} is not one of {DECISIONS}")
        if not row["class"] or row["class"] != row["class"].strip().lower():
            problems.append(f"{where}: class must be lower case")
        if row["sheet_level"] and not re.fullmatch(r"[1-9]", row["sheet_level"]):
            problems.append(f"{where}: sheet_level must be empty or 1 to 9")
        if decision == "reject" and not row["sheet_level"]:
            problems.append(f"{where}: a rejected row is a sheet row and needs its sheet_level")
        if decision in ("reject", "remove-unprinted"):
            if row["printed_level"]:
                problems.append(f"{where}: a {decision} row has no printed_level")
        elif not re.fullmatch(r"[1-9]", row["printed_level"]):
            problems.append(f"{where}: printed_level must be 1 to 9")
        if row["book"] not in publications:
            problems.append(f"{where}: book {row['book']!r} is not in publications.toml")
        if not row["page"].strip() or not row["basis"].strip():
            problems.append(f"{where}: page and basis are required")
        if "the the" in row["basis"]:
            problems.append(f"{where}: 'the the' in the basis")
    return problems


def parse_levels(text: str) -> tuple[Pairs, re.Match] | None:
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


def render_stat(pairs: Pairs) -> str:
    by_level: dict[int, list[str]] = {}
    for name, level in sorted(pairs, key=lambda p: p[1]):  # stable: table order within a level
        by_level.setdefault(level, []).append(name)
    return "\\\n".join(f"{level}: {', '.join(names)}" for level, names in by_level.items())


def render_table(pairs: Pairs) -> str:
    return "levels = [\n" + "\n".join(f'  {{ class = "{n}", level = {l} }},' for n, l in pairs) + "\n]\n"


def insert(pairs: Pairs, name: str, level: int) -> Pairs:
    for index, (other, _) in enumerate(pairs):
        if other.lower() > name.lower():
            return pairs[:index] + [(name, level)] + pairs[index:]
    return pairs + [(name, level)]


def edit_entry(path: Path, adds: Pairs, removes: list[str]) -> tuple[list[str], str | None]:
    """The text of one entry after the rows, and the problems. Writes nothing."""
    text = path.read_text(encoding="utf-8")
    parsed = parse_levels(text)
    if parsed is None:
        if re.search(r"^levels = ", text, re.M):
            return [f"{path}: no `levels` table in the expected form"], None
        if removes or not re.search(r"^casting_time = ", text, re.M) or re.search(r"^Level:", text, re.M):
            return [f"{path}: no `levels` table, and no place to start one"], None
        pairs: Pairs = []
        for name, level in adds:
            pairs = insert(pairs, name, level)
        text = re.sub(r"^casting_time = ", lambda m: render_table(pairs) + m.group(0), text, count=1, flags=re.M)
        text = re.sub(r"^Casting time:", lambda m: f"Level: {render_stat(pairs)}\n" + m.group(0), text,
                      count=1, flags=re.M)
        return [], text
    pairs, match = parsed
    stat = STAT_RE.search(text)
    if stat is not None and stat.group(1) != render_stat(pairs):
        return [f"{path}: the `Level:` row does not match the table before the change"], None
    problems = []
    for name in removes:
        pairs = [p for p in pairs if p[0] != name]
    for name, level in adds:
        have = dict(pairs)
        if name in have:
            if have[name] != level:
                problems.append(f"{path}: {name} is level {have[name]}, the table says {level}")
            continue
        pairs = insert(pairs, name, level)
    if problems:
        return problems, None
    text = text[: match.start()] + render_table(pairs) + text[match.end():]
    stat = STAT_RE.search(text)
    if stat is not None:
        text = text[: stat.start(1)] + render_stat(pairs) + text[stat.end(1):]
    return [], text


def publications_of(corpus: Path) -> set[str]:
    return set(re.findall(r'^id = "([^"]+)"', (corpus / "publications.toml").read_text(encoding="utf-8"), re.M))


def entry_path(corpus: Path, entry: str) -> Path:
    return corpus / "entries" / "spell" / (entry.rsplit("/", 1)[1] + ".md")


def run(corpus: Path, check: bool) -> int:
    rows, problems = read_rows(corpus / TSV)
    problems += validate(rows, publications_of(corpus))
    adds: dict[str, Pairs] = {}
    removes: dict[str, list[str]] = {}
    rejects: dict[str, list[tuple[str, int]]] = {}
    counts = {d: 0 for d in DECISIONS}
    for row in rows:
        if row["decision"] in counts:
            counts[row["decision"]] += 1
        name = class_label(row["class"])
        if row["decision"] in ("add", "present") and row["printed_level"]:
            adds.setdefault(row["entry"], []).append((name, int(row["printed_level"])))
        elif row["decision"] == "remove-unprinted":
            removes.setdefault(row["entry"], []).append(name)
        elif row["decision"] == "reject" and row["sheet_level"]:
            rejects.setdefault(row["entry"], []).append((name, int(row["sheet_level"])))
    entries = sorted(set(adds) | set(removes))
    new_text: dict[Path, str] = {}
    for entry in entries:
        path = entry_path(corpus, entry)
        if not path.exists():
            problems.append(f"{entry}: no entry file {path}")
            continue
        found, text = edit_entry(path, adds.get(entry, []), removes.get(entry, []))
        problems += found
        if text is not None and text != path.read_text(encoding="utf-8"):
            if check:
                problems.append(f"{entry}: differs from the table (run the script without --check)")
            else:
                new_text[path] = text
    for entry, wanted in sorted(rejects.items()):
        path = entry_path(corpus, entry)
        parsed = parse_levels(path.read_text(encoding="utf-8")) if path.exists() else None
        have = dict(parsed[0]) if parsed else {}
        for name, level in wanted:
            if have.get(name) == level:
                problems.append(f"{entry}: {name} {level} was rejected, but the entry holds it")
    if not problems:
        for path, text in new_text.items():  # every entry is clean: now write
            path.write_text(text, encoding="utf-8")
    for problem in problems:
        print(problem)
    if not problems:
        print(f"{len(rows)} rows ({counts['add']} add, {counts['present']} present, {counts['reject']} reject, "
              f"{counts['remove-unprinted']} remove-unprinted) in {len(entries)} entries: ok"
              + ("" if check else f", {len(new_text)} written"))
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
    bare = entry.replace('levels = [\n  { class = "Bard", level = 2 },\n  { class = "Wizard", level = 3 },\n]\n', "")
    bare = bare.replace("Level: 2: Bard\\\n3: Wizard\n", "")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "x.md"
        path.write_text(entry, encoding="utf-8")
        problems, text = edit_entry(path, [("Psychic", 3), ("Bard", 2)], ["Wizard"])
        assert problems == [] and text is not None
        assert '{ class = "Psychic", level = 3 },' in text and "Wizard" not in text, text
        assert "Level: 2: Bard\\\n3: Psychic\n" in text, text
        path.write_text(text, encoding="utf-8")
        assert edit_entry(path, [("Psychic", 3)], ["Wizard"]) == ([], text)  # idempotent
        assert edit_entry(path, [("Bard", 3)], [])[0] != []  # a different level stops the run
        path.write_text(bare, encoding="utf-8")
        problems, text = edit_entry(path, [("Witch", 8)], [])
        assert problems == [] and text is not None and "Level: 8: Witch\nCasting time" in text, text
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
