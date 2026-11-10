#!/usr/bin/env python3
"""Resolve printed Replaces/Alters names to class-feature heading anchors.

An archetype or class option stores the printed feature names in `replaces` and
`alters`. Cast Iron adds optional `replaces_features` and `alters_features`
lists that hold the heading anchors of the base class entry, so the app can
compare trades without parsing display names. This script fills those lists.

A name is confident when, after stripping case, punctuation, and an ability tag
such as `(Ex)`, `(Su)`, or `(Sp)`, its slug is a heading anchor of the base
class. An archetype's base class is its `archetype` relation target. A class
option's base classes are the `classes` of its group in `option-groups.toml`.
A name that does not resolve is left out and reported; the script never
guesses.

Run from the corpus root:

    python3 scripts/replaces-features.py            # rewrite
    python3 scripts/replaces-features.py --check    # report, change nothing

The script is idempotent: a second run writes the same lists. It edits only
`replaces_features` and `alters_features` lines in archetype and class-option
front matter.
"""

from __future__ import annotations

import argparse
import re
import tomllib
from collections import Counter, defaultdict
from pathlib import Path

ENTRY_DIR = Path("entries")
CLASS_DIRS = (ENTRY_DIR / "class", ENTRY_DIR / "pclass")

# A heading with an explicit anchor. The class-feature pass added one to every
# feature paragraph, so these are the stable keys a trade can name.
HEADING = re.compile(r"^#{2,6} .*? \{#([A-Za-z0-9_.-]+)\}\s*$", re.MULTILINE)

# The printed ability tag: (Ex), (Su), (Sp), (Ex or Su), (Sp, Su), (Ex or Sp).
ABILITY_TAG = re.compile(
    r"\s*/?\s*\((?:Ex|Su|Sp)(?:\s*(?:,|/|or|and)\s*(?:Ex|Su|Sp))*\)\s*:?\s*$",
    re.IGNORECASE,
)

ID_LINE = re.compile(r'^id = "([^"]+)"', re.MULTILINE)
FEATURE_LINE = re.compile(r"^(?:replaces|alters)_features\s*=")


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


def feature_key(name: str) -> str:
    """The heading anchor a printed feature name would have."""
    return slugify(ABILITY_TAG.sub("", name.strip()))


def split_front(text: str) -> tuple[list[str], list[str]]:
    """The opening fence plus TOML lines, and the closing fence plus body."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "+++":
        raise ValueError("file does not start with +++")
    end = next(
        (index for index in range(1, len(lines)) if lines[index].strip() == "+++"),
        None,
    )
    if end is None:
        raise ValueError("front matter is not closed")
    return lines[: end + 1], lines[end:]


def parse_front(text: str) -> tuple[list[str], dict]:
    front, _ = split_front(text)
    try:
        data = tomllib.loads("\n".join(front[1:-1]))
    except tomllib.TOMLDecodeError as error:
        raise ValueError(f"bad front matter: {error}") from error
    return front, data


def entry_id(data: dict) -> str:
    return data.get("id", "")


def class_anchors() -> dict[str, set[str]]:
    """Heading anchors of every class and prestige-class entry, by id."""
    anchors: dict[str, set[str]] = {}
    for directory in CLASS_DIRS:
        for path in sorted(directory.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            if not re.search(r'^kind = "(?:class|prestige_class)"$', text, re.MULTILINE):
                continue
            _, data = parse_front(text)
            anchors[entry_id(data)] = set(HEADING.findall(text))
    return anchors


def option_groups() -> dict[str, list[str]]:
    path = Path("option-groups.toml")
    if not path.is_file():
        return {}
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    return {
        slug: list(group.get("classes", []))
        for slug, group in data.get("groups", {}).items()
    }


def base_classes(data: dict, groups: dict[str, list[str]]) -> list[str]:
    kind = data.get("kind")
    if kind == "archetype":
        return [
            relation["target"]
            for relation in data.get("relations", [])
            if relation.get("kind") == "archetype"
        ]
    if kind == "class_option":
        group = data.get("fields", {}).get("group", "")
        return list(groups.get(group, []))
    return []


def resolved(anchors: set[str], names: list[str]) -> tuple[list[str], list[str]]:
    """Resolve each comma-separated printed name inside a typed list item."""
    keys: list[str] = []
    unresolved: list[str] = []
    for name in names:
        for part in name.split(","):
            part = part.strip()
            if not part:
                continue
            key = feature_key(part)
            if key in anchors:
                keys.append(key)
            else:
                unresolved.append(part)
    return keys, unresolved


def toml_array(values: list[str]) -> str:
    return "[" + ", ".join(f'"{value}"' for value in values) + "]"


def rewrite(
    text: str,
    replaces_features: list[str],
    alters_features: list[str],
) -> str:
    """Replace the two feature lines in canonical position and leave the rest alone."""
    front, rest = split_front(text)
    toml_lines = front[1:-1]
    filtered = [line for line in toml_lines if not FEATURE_LINE.match(line)]

    insert_at = None
    for index, line in enumerate(filtered):
        if line.startswith("alters = "):
            insert_at = index + 1
        elif line.startswith("replaces = ") and insert_at is None:
            insert_at = index + 1
    if insert_at is None:
        return text

    extra: list[str] = []
    if replaces_features:
        extra.append(f"replaces_features = {toml_array(replaces_features)}")
    if alters_features:
        extra.append(f"alters_features = {toml_array(alters_features)}")
    filtered[insert_at:insert_at] = extra

    replaced = [front[0], *filtered, *rest]
    return "\n".join(replaced) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report, change nothing")
    args = parser.parse_args()

    anchors = class_anchors()
    groups = option_groups()
    resolved_names = 0
    entries_with_features = 0
    updated = 0
    unresolved: list[tuple[str, str, str, str]] = []
    unresolved_by_class: Counter[str] = Counter()

    for path in sorted(ENTRY_DIR.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if 'kind = "archetype"' not in text and 'kind = "class_option"' not in text:
            continue
        _, data = parse_front(text)
        if data.get("kind") not in ("archetype", "class_option"):
            continue
        fields = data.get("fields", {})
        replaces = fields.get("replaces", [])
        alters = fields.get("alters", [])
        if not replaces and not alters:
            continue

        classes = base_classes(data, groups)
        class_anchors_set: set[str] = set()
        for class_id in classes:
            class_anchors_set.update(anchors.get(class_id, set()))
        class_label = ", ".join(classes) if classes else "(no base class)"

        replaces_features, replaces_unresolved = resolved(class_anchors_set, replaces)
        alters_features, alters_unresolved = resolved(class_anchors_set, alters)
        resolved_names += len(replaces_features) + len(alters_features)
        if replaces_features or alters_features:
            entries_with_features += 1
        for field, names in (
            ("replaces", replaces_unresolved),
            ("alters", alters_unresolved),
        ):
            for name in names:
                unresolved.append((entry_id(data), class_label, field, name))
                unresolved_by_class[class_label] += 1

        rewritten = rewrite(text, replaces_features, alters_features)
        if rewritten != text:
            updated += 1
            if not args.check:
                path.write_text(rewritten, encoding="utf-8")

    print(f"resolved {resolved_names} names in {entries_with_features} entries")
    print(f"updated {updated} files{' (would change)' if args.check else ''}")
    print(f"unresolved {len(unresolved)} names")
    if unresolved:
        print("\nunresolved by base class:")
        for class_label, count in unresolved_by_class.most_common():
            print(f"  {class_label}: {count}")
        print("\nunresolved names:")
        for entry, class_label, field, name in unresolved:
            print(f"  {entry} [{class_label}] {field}: {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
