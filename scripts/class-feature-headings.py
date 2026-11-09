#!/usr/bin/env python3
"""Turn each class feature label into a heading with a stable explicit anchor.

A class entry writes the class-features section as `###` headings followed by
standalone bold feature names:

    **Fast Movement (Ex)**

    **Gained:** At 1st Level

This script gives every such paragraph a `####` heading one level below the
section heading and an explicit anchor derived from the feature name:

    #### Fast Movement (Ex) {#fast-movement}

The paragraph itself stays where it was, so the only change is bold label to
heading. Later work (cast-iron#252) uses the heading keys for the `replaces`
lists of archetypes and class options.

Run from the corpus root:

    python3 scripts/class-feature-headings.py            # rewrite
    python3 scripts/class-feature-headings.py --verify   # compare to HEAD
    python3 scripts/class-feature-headings.py --check    # report, change nothing

The script is idempotent: a second run finds no bold feature labels to convert.

Scope
-----
The class-features region starts at `### Class Features` and stops at the first
terminal section (`### Ex-…`, `### Alternate Capstones`, `### Archetypes`,
`### Favored Class Bonuses`, `### Grit and Panache`, `### Adding Spells to a
Witch's Familiar`, or `### Speaking Druidic`). It includes the intermediate
`### Spells Known` and `### Spells Prepared` tables because class features
continue below them.

Only standalone bold paragraphs are converted. Bold labels that are an item in
a list are options or table rows, not feature paragraphs, and are reported as
skipped. Archetype and capstone names in later sections are out of scope for
this pass.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ENTRY_DIR = Path("entries/class")

START = re.compile(r"^Class Features")
STOP = re.compile(
    r"^(?:Ex-|Alternate Capstones$|Archetypes$|Archetypes by Feature$|"
    r"Favored Class Bonuses$|Grit and Panache$|"
    r"Adding Spells to a Witch's Familiar$|Speaking Druidic$)"
)

# A whole paragraph of strong text, with no nested markup.
FEATURE = re.compile(r"^\*\*([^*]+)\*\*$")

# The printed ability tag: (Ex), (Su), (Sp), (Ex or Su), (Sp, Su), (Ex or Sp).
ABILITY_TAG = re.compile(
    r"\s*/?\s*\((?:Ex|Su|Sp)(?:\s*(?:,|/|or)\s*(?:Ex|Su|Sp))*\)\s*:?\s*$",
    re.IGNORECASE,
)

HEADING = re.compile(r"^(#{2,6}) (.*?)(?: \{#([A-Za-z0-9_.-]+)\})?$")

# A bold label that is the start of a list item, not a feature paragraph.
LIST_LABEL = re.compile(r"^\s*(?:[-*]|\d+\.) \*\*([^*]+)\*\*")

RESERVED = {"entry-related"}


def slugify(text: str) -> str:
    """Lowercase ASCII alphanumeric words joined by `-`, like the schema crate."""
    out: list[str] = []
    pending = False
    for ch in text:
        if ch.isascii() and ch.isalnum():
            if pending and out:
                out.append("-")
            pending = False
            out.append(ch.lower())
        else:
            pending = True
    return "".join(out)


def feature_anchor(name: str) -> str:
    """Anchor base for one printed feature name, without its ability tag."""
    return slugify(ABILITY_TAG.sub("", name))


def body_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def feature_region(lines: list[str]):
    """Yield (index, line) for the class-features region, plus skipped list labels."""
    inside = False
    features: list[tuple[int, str]] = []
    list_labels: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        heading = HEADING.match(line)
        if heading:
            title = heading.group(2).strip()
            if START.match(title):
                inside = True
            elif STOP.match(title):
                inside = False
            continue
        if not inside:
            continue
        match = FEATURE.match(line)
        if match:
            features.append((index, match.group(1)))
            continue
        list_match = LIST_LABEL.match(line)
        if list_match:
            list_labels.append((index, list_match.group(1)))
    return features, list_labels


def transform(path: Path) -> tuple[list[str], list[tuple[int, str]], list[tuple[int, str]]]:
    """Return the rewritten lines, converted feature names and skipped list labels."""
    lines = body_lines(path)
    features, list_labels = feature_region(lines)

    used = dict.fromkeys(RESERVED, True)
    for line in lines:
        heading = HEADING.match(line)
        if heading and heading.group(3):
            used[heading.group(3)] = True

    changed: list[tuple[int, str]] = []
    by_index: dict[int, str] = {}
    for index, name in features:
        base = feature_anchor(name)
        if not base:
            continue
        anchor = base
        suffix = 2
        while anchor in used:
            anchor = f"{base}-{suffix}"
            suffix += 1
        used[anchor] = True
        by_index[index] = f"#### {name} {{#{anchor}}}"
        changed.append((index, name))

    rewritten = [by_index.get(index, line) for index, line in enumerate(lines)]
    return rewritten, changed, list_labels


def entry_files() -> list[Path]:
    return sorted(ENTRY_DIR.glob("*.md"))


def command_transform(check: bool) -> int:
    total = 0
    skipped_classes: list[str] = []
    skipped_lists: list[tuple[str, int]] = []
    print(f"{'class':28} {'headings':>8}  features")
    for path in entry_files():
        text = path.read_text(encoding="utf-8")
        if 'kind = "class"' not in text:
            continue
        rewritten, changed, list_labels = transform(path)
        total += len(changed)
        if not changed:
            skipped_classes.append(path.stem)
        for _, name in list_labels:
            skipped_lists.append((path.stem, name))
        print(f"{path.stem:28} {len(changed):>8}")
        if changed and not check:
            path.write_text("\n".join(rewritten) + "\n", encoding="utf-8")

    print(f"\ntotal headings added: {total}")
    if skipped_classes:
        print("classes with no feature paragraph: " + ", ".join(skipped_classes))
    if skipped_lists:
        print("bold labels inside lists left unchanged (not feature paragraphs):")
        for stem, name in skipped_lists:
            print(f"  {stem}: {name}")
    return 0


def head_lines(path: Path) -> list[str]:
    """The file at HEAD, or an empty list when the script runs outside a work tree."""
    try:
        text = subprocess.run(
            ["git", "show", f"HEAD:{path.as_posix()}"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    return text.splitlines()


def verify() -> int:
    """Prove every body differs only by bold label to heading (and anchor)."""
    failures = 0
    checked = 0
    for path in entry_files():
        current = body_lines(path)
        original = head_lines(path)
        if not original:
            print(f"{path}: no HEAD copy; skipped", file=sys.stderr)
            continue
        # In the new body, every level-4 heading with an explicit anchor is a
        # converted feature label. Turn it back into the bold paragraph it was.
        reverted: list[str] = []
        converted = 0
        for line in current:
            match = re.match(r"^#### (.*?) \{#[A-Za-z0-9_.-]+\}$", line)
            if match:
                reverted.append(f"**{match.group(1)}**")
                converted += 1
            else:
                reverted.append(line)
        checked += 1
        if reverted != original:
            failures += 1
            first = next(
                (
                    (index + 1, before, after)
                    for index, (before, after) in enumerate(zip(original, reverted))
                    if before != after
                ),
                None,
            )
            if first:
                line, before, after = first
                print(
                    f"{path}:{line}: body changed outside the transformation\n"
                    f"  before: {before!r}\n  after:  {after!r}",
                    file=sys.stderr,
                )
            else:
                print(
                    f"{path}: body length {len(original)} -> {len(reverted)}",
                    file=sys.stderr,
                )
        else:
            print(f"{path.stem}: {converted} labels -> headings; body otherwise identical")
    print(f"\nverified {checked} class bodies; {failures} mismatch(es)")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report without writing")
    parser.add_argument(
        "--verify",
        action="store_true",
        help="compare the working tree to HEAD, reverting only the new headings",
    )
    args = parser.parse_args()
    if args.verify:
        return verify()
    return command_transform(args.check)


if __name__ == "__main__":
    raise SystemExit(main())
