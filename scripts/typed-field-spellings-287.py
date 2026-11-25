#!/usr/bin/env python3
"""Give the typed fields of phynics/cast-iron-data#287 one spelling per value.

    python3 scripts/typed-field-spellings-287.py [CORPUS]            # rewrite the entries (idempotent)
    python3 scripts/typed-field-spellings-287.py [CORPUS] --check    # fail when an old spelling is left
    python3 scripts/typed-field-spellings-287.py --self-test

Several typed fields held two spellings of one value, which splits a filter or a facet. The rules
(the owner rulings of 2026-11-25 are 1 and 6):

    1 creature_type  `magicalBeast` -> `magical beast`, `monstrousHumanoid` -> `monstrous humanoid`
    2 size           lower case (`Medium` -> `medium`)
    3 alignment      abbreviations written out (`N` -> `neutral`, `CE` -> `chaotic evil`,
                     `CG or CE` -> `chaotic good or chaotic evil`)
    4 hit_die        no trailing period (`d8.` -> `d8`), also in the `**Hit Die:**` line
    5 school         a bracketed list leaves the value (`evocation [fire or cold]` -> `evocation`).
                     The descriptors in the list join `descriptors` (a spell that lets the caster
                     choose one of several lists all of them, in alphabetical order). A note
                     (`see text`, `variable`, `see text for lesser planar binding`) has no field: the
                     `School:` row of the stat block keeps the printed bracket, and `corpus-check`
                     accepts a row that adds a bracket to the school
    6 subschools     lower case, as print sets them in the school line (`conjuration (calling)`)
    7 descriptors    `glamer` is an illusion subschool, so it leaves `descriptors` and joins
                     `subschools` where the entry lacks it

The typed field and the stat block row change together (`Size:`, `Alignment:`, `Subschool:`,
`Descriptors:`), so the drift check stays at zero: a row is rewritten only when it states the value
that the field held before. A `Descriptors:` row whose list becomes empty goes. A value that no rule
maps stays as it is, and the run lists it.

`--check` fails (exit 1, one line per problem) when a typed field still holds an old spelling:
a legacy creature type, a capitalised size or subschool, an abbreviated alignment, a hit die with a
period, a bracket in a school, or `glamer` in `descriptors`. A school that no rule maps
(`UNMAPPED_SCHOOLS`) is not a problem. Python 3.11 or later, no third-party package.
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
import tomllib
from collections import Counter
from pathlib import Path

CREATURE_TYPES = {"magicalBeast": "magical beast", "monstrousHumanoid": "monstrous humanoid"}
ALIGNMENTS = {
    "LG": "lawful good",
    "NG": "neutral good",
    "CG": "chaotic good",
    "LN": "lawful neutral",
    "N": "neutral",
    "CN": "chaotic neutral",
    "LE": "lawful evil",
    "NE": "neutral evil",
    "CE": "chaotic evil",
}
ALIGNMENT_TOKEN = re.compile(r"\b(" + "|".join(sorted(ALIGNMENTS, key=len, reverse=True)) + r")\b")
# Descriptors that a school bracket lists. Anything else in a bracket is a note.
BRACKET_DESCRIPTORS = {
    "acid", "air", "chaotic", "cold", "curse", "earth", "electricity", "evil", "fire", "good",
    "lawful", "mind-affecting", "water",
}
SCHOOLS = {
    "abjuration", "conjuration", "divination", "enchantment", "evocation", "illusion",
    "necromancy", "transmutation", "universal",
}
# A school value that is no school and no bracket (`multiple (see text)`): left as printed.
UNMAPPED_SCHOOLS = {"multiple (see text)"}
SCHOOL_BRACKET = re.compile(r"^([a-z]+) \[(.*)\]$")
SIZES = {"fine", "diminutive", "tiny", "small", "medium", "large", "huge", "gargantuan", "colossal"}

FIELD_LINE = re.compile(r'^([a-z_]+) = (?:"(.*)"|\[(.*)\])$')
STATBLOCK_OPEN = "::: statblock"
STATBLOCK_CLOSE = ":::"


def split_entry(text: str) -> tuple[str, str] | None:
    """The front matter up to and including its closing fence, and the body after it."""
    if not text.startswith("+++\n"):
        return None
    end = text.find("\n+++\n", 4)
    if end < 0:
        return None
    return text[: end + 5], text[end + 5 :]


def fields_of(head: str) -> dict:
    return tomllib.loads(head[4:-5]).get("fields", {})


def parse_array(raw: str) -> list[str]:
    return [item for item in re.findall(r'"([^"]*)"', raw)]


def write_array(values: list[str]) -> str:
    return "[" + ", ".join(f'"{value}"' for value in values) + "]"


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\\", "").strip()).lower().rstrip(".;")


def expand_alignment(value: str) -> str:
    return ALIGNMENT_TOKEN.sub(lambda match: ALIGNMENTS[match.group(1)], value)


def split_bracket(inner: str) -> tuple[list[str], list[str]] | None:
    """`fire or cold` -> (['fire', 'cold'], []); `curse, see text` -> (['curse'], ['see text']).
    None when the list holds a word that is neither a descriptor nor a note."""
    descriptors: list[str] = []
    notes: list[str] = []
    for part in re.split(r",\s*|\s+or\s+", inner):
        part = re.sub(r"^or\s+", "", part.strip())
        if not part:
            continue
        if part in BRACKET_DESCRIPTORS:
            descriptors.append(part)
        elif part == "variable" or part.startswith("see text"):
            notes.append(part)
        else:
            return None
    return descriptors, notes


def plan_entry(text: str) -> tuple[str, Counter, list[str]]:
    """The rewritten entry text, what changed (a count per rule), and the values left unmapped."""
    parts = split_entry(text)
    changes: Counter = Counter()
    unmapped: list[str] = []
    if parts is None:
        return text, changes, unmapped
    head, body = parts
    fields = fields_of(head)
    if not fields:
        return text, changes, unmapped
    kind = fields.get("kind")

    old = {key: fields.get(key) for key in ("size", "alignment", "hit_die")}
    new: dict[str, object] = {}

    if kind == "creature":
        creature_type = fields.get("creature_type")
        if creature_type in CREATURE_TYPES:
            new["creature_type"] = CREATURE_TYPES[creature_type]
            changes["creature_type"] += 1
        size = fields.get("size")
        if isinstance(size, str) and size != size.lower():
            new["size"] = size.lower()
            changes["size"] += 1
        alignment = fields.get("alignment")
        if isinstance(alignment, str) and ALIGNMENT_TOKEN.search(alignment):
            new["alignment"] = expand_alignment(alignment)
            changes["alignment"] += 1
    if kind in ("class", "prestige_class", "npc_class") or "hit_die" in fields:
        hit_die = fields.get("hit_die")
        if isinstance(hit_die, str) and hit_die.endswith("."):
            new["hit_die"] = hit_die.rstrip(".")
            changes["hit_die"] += 1

    old_subschools = list(fields.get("subschools", []))
    old_descriptors = list(fields.get("descriptors", []))
    if kind == "spell":
        school = fields.get("school", "")
        subschools = list(old_subschools)
        descriptors = list(old_descriptors)
        match = SCHOOL_BRACKET.match(school)
        if match:
            split = split_bracket(match.group(2))
            if split is None:
                unmapped.append(f"school = {school!r}")
            else:
                found, _notes = split
                new["school"] = match.group(1)
                changes["school"] += 1
                if found:
                    descriptors = sorted(set(descriptors) | set(found))
                    changes["school_descriptors"] += 1
        elif school not in SCHOOLS and school not in UNMAPPED_SCHOOLS:
            unmapped.append(f"school = {school!r}")
        if any(value != value.lower() for value in subschools):
            subschools = [value.lower() for value in subschools]
            changes["subschools"] += 1
        if "glamer" in descriptors:
            descriptors = [value for value in descriptors if value != "glamer"]
            if "glamer" not in subschools:
                subschools.append("glamer")
                changes["glamer_added_to_subschools"] += 1
            changes["glamer"] += 1
        if subschools != old_subschools:
            new["subschools"] = subschools
        if descriptors != old_descriptors:
            new["descriptors"] = descriptors

    if not new:
        return text, changes, unmapped

    # The front matter: rewrite the lines of `[fields]`, then place a field the entry lacked.
    out: list[str] = []
    in_fields = False
    for line in head.split("\n"):
        if line == "[fields]":
            in_fields = True
        elif in_fields and line.startswith("["):
            in_fields = False
        match = FIELD_LINE.match(line) if in_fields else None
        key = match.group(1) if match else None
        if key not in new:
            out.append(line)
        elif isinstance(new[key], list):
            if new[key]:
                out.append(f"{key} = {write_array(new[key])}")  # type: ignore[arg-type]
        else:
            out.append(f'{key} = "{new[key]}"')

    def place(key: str, after: tuple[str, ...]) -> None:
        if key not in new or key in fields or not new[key]:
            return
        for anchor in after:
            for index, line in enumerate(out):
                if line.startswith(f"{anchor} = "):
                    out.insert(index + 1, f"{key} = {write_array(new[key])}")  # type: ignore[arg-type]
                    return
        raise SystemExit(f"cannot place `{key}`: the entry has no `school` line")

    place("subschools", ("school",))
    place("descriptors", ("subschools", "school"))
    new_head = "\n".join(out)

    # The body: the stat block rows that state the value that the field held.
    body_lines = body.split("\n")
    in_block = False
    result: list[str] = []
    for line in body_lines:
        if line.startswith(STATBLOCK_OPEN):
            in_block = True
        elif in_block and line == STATBLOCK_CLOSE:
            in_block = False
        if in_block:
            row = re.match(r"^([A-Za-z ]+): (.*?)(\\?)$", line)
            if row:
                label, value, tail = row.group(1), row.group(2), row.group(3)
                rewritten = None
                if label == "Size" and "size" in new and norm(value) == norm(old["size"]):
                    rewritten = new["size"]
                elif label == "Alignment" and "alignment" in new and norm(value) == norm(old["alignment"]):
                    rewritten = new["alignment"]
                elif label == "Subschool" and "subschools" in new and old_subschools and (
                    norm(value) == norm(", ".join(old_subschools))
                ):
                    rewritten = ", ".join(new["subschools"])  # type: ignore[arg-type]
                elif label == "Descriptors" and "descriptors" in new and old_descriptors and (
                    norm(value) == norm(", ".join(old_descriptors))
                ):
                    rewritten = ", ".join(new["descriptors"]) if new["descriptors"] else None  # type: ignore[arg-type]
                    if rewritten is None:
                        changes["descriptors_row_removed"] += 1
                        continue
                if rewritten is not None and rewritten != value:
                    line = f"{label}: {rewritten}{tail}"
                    changes[f"row_{label.lower()}"] += 1
        elif "hit_die" in new and norm(line.removeprefix("**Hit Die:**")) == norm(old["hit_die"]) and line.startswith(
            "**Hit Die:**"
        ):
            line = f"**Hit Die:** {new['hit_die']}"
            changes["row_hit_die"] += 1
        result.append(line)
    return new_head + "\n".join(result), changes, unmapped


def entry_files(corpus: Path) -> list[Path]:
    return sorted((corpus / "entries").rglob("*.md"))


def apply(corpus: Path) -> int:
    total: Counter = Counter()
    unmapped: list[str] = []
    written = 0
    for path in entry_files(corpus):
        text = path.read_text(encoding="utf-8")
        new_text, changes, left = plan_entry(text)
        unmapped += [f"{path.relative_to(corpus)}: {value}" for value in left]
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            written += 1
            total.update(changes)
    print(f"{written} entries rewritten")
    for key, count in sorted(total.items()):
        print(f"  {key}: {count}")
    for line in unmapped:
        print(f"unmapped: {line}")
    return 0


def problems_of(corpus: Path) -> list[str]:
    problems: list[str] = []
    for path in entry_files(corpus):
        text = path.read_text(encoding="utf-8")
        parts = split_entry(text)
        if parts is None:
            continue
        fields = fields_of(parts[0])
        name = path.relative_to(corpus)
        creature_type = fields.get("creature_type")
        if creature_type in CREATURE_TYPES:
            problems.append(f"{name}: creature_type {creature_type!r}, write {CREATURE_TYPES[creature_type]!r}")
        size = fields.get("size")
        if isinstance(size, str) and size != size.lower():
            problems.append(f"{name}: size {size!r} is not lower case")
        alignment = fields.get("alignment")
        if isinstance(alignment, str) and ALIGNMENT_TOKEN.search(alignment):
            problems.append(f"{name}: alignment {alignment!r} is abbreviated")
        hit_die = fields.get("hit_die")
        if isinstance(hit_die, str) and hit_die.endswith("."):
            problems.append(f"{name}: hit_die {hit_die!r} ends with a period")
        school = fields.get("school")
        if isinstance(school, str) and ("[" in school or "(" in school) and school not in UNMAPPED_SCHOOLS:
            problems.append(f"{name}: school {school!r} holds a bracket")
        for value in fields.get("subschools", []):
            if value != value.lower():
                problems.append(f"{name}: subschool {value!r} is not lower case")
        for value in fields.get("descriptors", []):
            if value == "glamer":
                problems.append(f"{name}: descriptors holds `glamer`, an illusion subschool")
    return problems


def check(corpus: Path) -> int:
    problems = problems_of(corpus)
    for line in problems:
        print(line)
    if problems:
        print(f"{len(problems)} typed fields still hold an old spelling")
        return 1
    print("typed fields: one spelling per value")
    return 0


def self_test() -> int:
    def entry(fields: str, body: str = "") -> str:
        return f'+++\nid = "ref/x"\n\n[fields]\n{fields}\n+++\n{body}'

    def run(text: str) -> str:
        return plan_entry(text)[0]

    creature = entry(
        'kind = "creature"\ncreature_type = "magicalBeast"\nsize = "Large"\nalignment = "CG or CE"',
        "::: statblock\nAlignment: CG or CE\nSize: Large\nType: Magical Beast\n:::\n",
    )
    expect = entry(
        'kind = "creature"\ncreature_type = "magical beast"\nsize = "large"\nalignment = "chaotic good or chaotic evil"',
        "::: statblock\nAlignment: chaotic good or chaotic evil\nSize: large\nType: Magical Beast\n:::\n",
    )
    assert run(creature) == expect, run(creature)
    assert run(expect) == expect
    klass = entry('kind = "class"\nhit_die = "d8."', "**Hit Die:** d8.\n")
    assert run(klass) == entry('kind = "class"\nhit_die = "d8"', "**Hit Die:** d8\n")
    spell = entry(
        'kind = "spell"\nschool = "evocation [fire or cold]"\nlevels = []',
        "::: statblock\nSchool: evocation \\[fire or cold\\]\n:::\n",
    )
    assert run(spell) == entry(
        'kind = "spell"\nschool = "evocation"\ndescriptors = ["cold", "fire"]\nlevels = []',
        "::: statblock\nSchool: evocation \\[fire or cold\\]\n:::\n",
    ), run(spell)
    note = entry('kind = "spell"\nschool = "conjuration [see text]"\nsubschools = ["Summoning"]', "::: statblock\nSubschool: Summoning\n:::\n")
    assert run(note) == entry(
        'kind = "spell"\nschool = "conjuration"\nsubschools = ["summoning"]', "::: statblock\nSubschool: summoning\n:::\n"
    ), run(note)
    glamer = entry(
        'kind = "spell"\nschool = "illusion"\nsubschools = ["Glamer"]\ndescriptors = ["evil", "glamer"]',
        "::: statblock\nSubschool: Glamer\nDescriptors: evil, glamer\n:::\n",
    )
    assert run(glamer) == entry(
        'kind = "spell"\nschool = "illusion"\nsubschools = ["glamer"]\ndescriptors = ["evil"]',
        "::: statblock\nSubschool: glamer\nDescriptors: evil\n:::\n",
    ), run(glamer)
    only = entry('kind = "spell"\nschool = "illusion"\nsubschools = ["Glamer"]\ndescriptors = ["glamer"]', "::: statblock\nDescriptors: glamer\nRange: x\n:::\n")
    assert run(only) == entry('kind = "spell"\nschool = "illusion"\nsubschools = ["glamer"]', "::: statblock\nRange: x\n:::\n"), run(only)
    odd = entry('kind = "spell"\nschool = "multiple (see text)"')
    assert plan_entry(odd)[0] == odd and not plan_entry(odd)[2]
    unknown = entry('kind = "spell"\nschool = "evocation [bogus]"')
    assert plan_entry(unknown)[0] == unknown and plan_entry(unknown)[2]
    with tempfile.TemporaryDirectory() as tmp:
        corpus = Path(tmp)
        (corpus / "entries").mkdir()
        (corpus / "entries" / "a.md").write_text(creature, encoding="utf-8")
        assert check(corpus) == 1
        apply(corpus)
        assert check(corpus) == 0
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
    corpus = Path(args.corpus)
    return check(corpus) if args.check else apply(corpus)


if __name__ == "__main__":
    sys.exit(main())
