#!/usr/bin/env python3
"""Give the imported skills, traps and afflictions their kinds, and alias their duplicates (issue #167).

The Pf Data folders `skill`, `trap`, `disease`, `drug`, `madness` and `curse` were imported as
`kind = "rule"`, so the Skills, Traps and Afflictions lists held only the carried entries and many
rules existed twice. Two passes fix that. A pass changes no `id` and moves no file.

  kinds       Sets the kind of every entry of the six folders:

                skill                       -> skill   (a stat block replaces the label pairs)
                trap                        -> trap    (tag: the lower-case `Type:` word)
                disease, curse              -> affliction (tag: the lower-case first word of `Type:`)
                drug                        -> affliction (tag `addiction`)
                madness                     -> affliction (tag `insanity`)

              The tag is one of the six words of `AFFLICTION_TYPES` in phynics/cast-iron
              (`crates/corpus/src/check.rs`), which `corpus-check` enforces. Drugs and madnesses
              print `Type: ingested`, `Type lesser madness` and so on, so their tag comes from the
              issue, and from `scripts/affliction-slot-vocabulary-171.tsv`, not from the line.
              Skills: the five `**Label**` / `**Details:** value` pairs become one stat block
              (`Key Ability`, `Trained Only`, `Armor Check Penalty`, `Optional Unchained Skill`,
              `Optional Background Skill`), and every other `**Name**` / `**Details:** text` pair
              (the rank unlocks, the survival items) becomes `**Name:** text`.
              Folders that stay as they are, each with a reason in the review file:
                haunt     stays `rule`. The GameMastery Guide (p. 242) says "Although haunts function
                          like traps" and that "the distinction between a trap and an undead
                          creature blurs" with a haunt: it does not say a haunt is a kind of trap.
                          Set `HAUNT_KIND` to `trap` when the owner decides otherwise.
                template  stays `rule` (issue).
                eq-poison stays `item` (issue).

  duplicates  Finds a carried entry (`ref/carried/...`, kind skill, trap or affliction) that prints
              the same rule as an imported entry: the same title, and the same book, or a book
              that another entry of the same title prints together with it. A carried entry that
              sits in a creature's text (`/monsters/` in the id) and the creature-specific
              afflictions (`ref/affliction/`) are variants, not duplicates, and stay (listed as `variant`).
              The kept entry is the one that holds every printed fact of the other:
                * the imported entry holds every fact of the carried one: keep the imported entry;
                * only the carried entry holds every fact of the imported one: keep the carried one;
                * neither does: keep both and list the pair (`hold`).
              A fact is a paragraph or a stat block row, compared by its words. The abbreviations
              `Dex` and `Dexterity` count as one word. Merged into the kept entry:
                * the `source_ids` and the `[[sources]]` pages of the dropped entry;
                * the italic opening line of a carried skill, and a `Reset: none` row of a carried
                  trap that the imported trap leaves out.
              The dropped entry is deleted, with these changes so that its id keeps resolving
              (phynics/cast-iron AGENTS.md rules 3 and 6):
                * `aliases.toml`: a row `old = <dropped id>`, `target = <kept id>`, `basis = "shared"`,
                  and every row that targeted the dropped id now targets the kept id (a target may
                  not be an old id);
                * `exclusions.toml`: a `[[rejected]]` row, `duplicate of <kept id>`;
                * every body link, `target`, `parent` and book node that named the dropped id names
                  the kept id (a link anchor that the kept entry lacks is dropped and listed). When the
                  kept entry already has a node in the same curated book, the dropped leaf node goes.
              Poisons (`eq-poison` items against carried afflictions) and the item twins of drugs
              are not decided here: an item is bought, an affliction is a rule, and the issue does
              not say which one a pair keeps. They are listed as `hold` with the counts.

`scripts/kind-skills-traps-afflictions-review-167.tsv` lists every kind change, every duplicate pair
(both ids, the kept one, the reason), every merge, and every entry left as it is. `--write` adds its
rows to the file and never removes one, so a rerun after a crash keeps the earlier rows.

Usage, from the corpus root:

    python3 -I scripts/kind-skills-traps-afflictions-167.py             survey: counts, pairs, holds
    python3 -I scripts/kind-skills-traps-afflictions-167.py --write     apply, then write the review file
    python3 -I scripts/kind-skills-traps-afflictions-167.py --write --pass kinds
    python3 -I scripts/kind-skills-traps-afflictions-167.py --check     exit 1 if a pass has work left
    python3 -I scripts/kind-skills-traps-afflictions-167.py --self-test

`--pass` is `kinds`, `duplicates`, or both (the default). After `--write` run
`cargo xtask corpus-fmt <dir>` and `cargo xtask corpus-check <dir>` (phynics/cast-iron), then the content
compile with the `--published` id list, so that a lost id fails.
"""

from __future__ import annotations

import argparse
import bisect
import collections
import csv
import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

FRONT = re.compile(r"\A\+\+\+\n(.*?)\n\+\+\+\n", re.S)
REVIEW = "scripts/kind-skills-traps-afflictions-review-167.tsv"
COLUMNS = ("entry_id", "action", "kind_before", "kind_after", "tag", "other_id", "citation", "reason")
PASSES = ("kinds", "duplicates")

# Folder -> (new kind, how the tag is found). `None` as the tag source: no tag.
FOLDERS: dict[str, tuple[str, str | None]] = {
    "skill": ("skill", None),
    "trap": ("trap", "type-word"),
    "disease": ("affliction", "type-word"),
    "curse": ("affliction", "type-word"),
    "drug": ("affliction", "addiction"),
    "madness": ("affliction", "insanity"),
}
# The six words of AFFLICTION_TYPES in phynics/cast-iron `crates/corpus/src/check.rs`.
AFFLICTION_TYPES = ("addiction", "curse", "disease", "infestation", "insanity", "poison")
# The owner may decide that haunts are traps. Until then they stay `rule` (see the docstring).
HAUNT_KIND = None
HAUNT_REASON = (
    "stays `rule`: GameMastery Guide p. 242 says haunts function like traps and that the distinction "
    "between a trap and an undead creature blurs; it does not say a haunt is a kind of trap"
)
# What the kept entry is, per kind of the imported folder.
PAIR_KIND = {
    "skill": "skill",
    "trap": "trap",
    "disease": "affliction",
    "curse": "affliction",
    "drug": "affliction",
    "madness": "affliction",
}
# Folders whose pairs wait for an owner decision (an item is bought, an affliction is a rule).
HOLD_FOLDERS = {"eq-poison": "affliction"}
ABBREVIATIONS = {
    "str": "strength",
    "dex": "dexterity",
    "con": "constitution",
    "int": "intelligence",
    "wis": "wisdom",
    "cha": "charisma",
}
LABEL_WORDS = frozenset(
    "type cr challenge rating perception dc disable device trigger reset effect save onset frequency "
    "cure contracted key ability trained only armor check penalty details".split()
)
SKILL_PAIRS = (
    ("Associated Skill", "Key Ability"),
    ("Trained Only", "Trained Only"),
    ("Armor Check Penalty", "Armor Check Penalty"),
    ("Optional Unchained Skill", "Optional Unchained Skill"),
    ("Optional Background Skill", "Optional Background Skill"),
)
SKILL_BLOCK = re.compile(
    "".join(
        rf"\*\*{re.escape(label)}\*\*\n\n\*\*Details:\*\* (?P<v{n}>[^\n]+)(?:\n\n|\Z)"
        for n, (label, _) in enumerate(SKILL_PAIRS)
    )
)
# The carried skill stat block says `Trained Only: Yes` and `Armor Check Penalty: Yes` for every skill
# (Acrobatics and Bluff are not trained only), so its rows are no facts: the imported label pairs
# replace them.
SKILL_ROWS_SUPERSEDED = frozenset({"Key Ability", "Trained Only", "Armor Check Penalty"})
DETAIL_PAIR = re.compile(r"^\*\*([^*\n]+)\*\*\n\n\*\*Details:\*\* ", re.M)
ID_CHARS = r"[A-Za-z0-9/_-]"


@dataclass
class Entry:
    path: Path
    text: str
    id: str
    kind: str
    title: str
    source_ids: list[str]
    tags: list[str]
    sources: list[dict]
    body: str

    @property
    def folder(self) -> str:
        parts = self.id.split("/")
        return parts[1] if len(parts) > 2 else ""


@dataclass
class Plan:
    """What a run would change: one list per kind of change, and the review rows."""

    kind_changes: list[tuple[Entry, str, str | None, str]] = field(default_factory=list)
    keeps: list[tuple[Entry, str, str]] = field(default_factory=list)
    pairs: list["Pair"] = field(default_factory=list)
    holds: list[tuple[str, str, str, str]] = field(default_factory=list)
    rows: list[dict] = field(default_factory=list)


@dataclass
class Pair:
    kept: Entry
    dropped: Entry
    reason: str
    intro: str | None = None
    none_rows: list[str] = field(default_factory=list)
    new_sources: list[tuple[str, str | None]] = field(default_factory=list)


# ---------------------------------------------------------------- reading


def parse_entry(path: Path, text: str) -> Entry:
    match = FRONT.match(text)
    assert match is not None, f"{path}: no front matter"
    meta = tomllib.loads(match.group(1))
    return Entry(
        path=path,
        text=text,
        id=meta["id"],
        kind=meta["kind"],
        title=meta["title"],
        source_ids=list(meta.get("source_ids", [])),
        tags=list(meta.get("tags", [])),
        sources=list(meta.get("sources", [])),
        body=text[match.end() :].lstrip("\n"),
    )


def load_entries(root: Path) -> dict[str, Entry]:
    entries: dict[str, Entry] = {}
    for path in sorted((root / "entries").rglob("*.md")):
        entry = parse_entry(path, path.read_text(encoding="utf-8"))
        entries[entry.id] = entry
    return entries


def load_titles(root: Path) -> dict[str, str]:
    data = tomllib.loads((root / "publications.toml").read_text(encoding="utf-8"))
    return {row["id"]: row["title"] for row in data.get("publication", [])}


def norm(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def citation(entry: Entry, titles: dict[str, str]) -> str:
    """`Core Rulebook p. 87`: the first citation of the entry that has a page."""
    for row in entry.sources:
        if row.get("page"):
            return f"{titles.get(row['publication'], row['publication'])} p. {row['page']}"
    return titles.get(entry.source_ids[0], entry.source_ids[0]) if entry.source_ids else ""


# ---------------------------------------------------------------- facts and coverage


def tokens(text: str) -> list[str]:
    text = text.lower().replace("’", "'").replace("–", "-").replace("—", "-")
    text = re.sub(r"\^\d+\^", " ", text)
    return [ABBREVIATIONS.get(word, word) for word in re.findall(r"[a-z0-9]+", text)]


def table_cells(match: re.Match) -> str:
    rows = re.split(r"\],\s*\[", match.group(0))
    return "\n\n".join(" ".join(re.findall(r'text = "((?:[^"\\]|\\.)*)"', row)) for row in rows)


def facts(body: str) -> list[str]:
    """The paragraphs and stat block rows of a body, without links, anchors, headings or labels."""
    text = re.sub(r"\]\(ref/[^)]*\)", "]", body)
    text = re.sub(r"\]\(#[^)]*\)", "]", text)
    text = re.sub(r"\{#[^}]*\}", "", text)
    text = re.sub(r"::: table\n.*?\n:::", table_cells, text, flags=re.S)
    out: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block or block.startswith("#"):
            continue
        if block.startswith("::: statblock"):
            for row in block.splitlines()[1:]:
                if row.strip() == ":::" or row.startswith("title ="):
                    continue
                if row.partition(":")[0] in SKILL_ROWS_SUPERSEDED:
                    continue
                out.append(row.partition(":")[2] or row)
            continue
        if block == ":::":
            continue
        block = re.sub(r"^\*\*[^*\n]+:\*\*\s*", "", block)
        out.append(block)
    return [fact for fact in out if tokens(fact)]


def uncovered(source: Entry, target: Entry) -> list[str]:
    """The facts of `source` that `target` does not hold: over 15 percent of a fact's words missing."""
    # `none` is a row value that `missing_none_rows` copies over, so it is no fact that can be lost.
    have = set(tokens(target.body)) | LABEL_WORDS | {"none"}
    out = []
    for fact in facts(source.body):
        words = [word for word in tokens(fact) if word not in LABEL_WORDS]
        if not words:
            continue
        missing = [word for word in words if word not in have]
        if missing and len(missing) / len(words) > 0.15:
            out.append(fact.replace("\n", " ")[:90])
    return out


# ---------------------------------------------------------------- kinds


def type_word(body: str) -> str | None:
    """The lower-case first word of the `Type` line (`**Type:** Disease (Injury)`, `**Type** ...`)."""
    match = re.search(r"^\*\*Type:?\*\*:?\s*([A-Za-z]+)", body, re.M)
    return match.group(1).lower() if match else None


def tag_for(folder: str, body: str) -> tuple[str | None, str]:
    """`(tag, basis)`; the tag is `None` when none can be found."""
    kind, source = FOLDERS[folder]
    if source is None:
        return None, ""
    if source == "type-word":
        word = type_word(body)
        if word is None:
            return None, "no `Type` line"
        if kind == "affliction" and word not in AFFLICTION_TYPES:
            return None, f"`Type` word {word!r} is outside the six affliction types"
        return word, "first word of the printed `Type` line"
    return source, "the issue gives this tag for the folder; the vocabulary file holds its print citation"


def convert_skill_body(body: str) -> tuple[str, bool]:
    """The five label pairs as one stat block, then every `**Name**` / `**Details:** text` pair as
    `**Name:** text`. `False` when the five pairs are not there."""
    match = SKILL_BLOCK.match(body.lstrip("\n"))
    if match is None:
        return body, False
    rows = [f"{name}: {match.group(f'v{n}').strip()}" for n, (_, name) in enumerate(SKILL_PAIRS)]
    rest = body.lstrip("\n")[match.end() :]
    rest = DETAIL_PAIR.sub(lambda m: f"**{m.group(1)}:** ", rest)
    block = "::: statblock\n" + "\n".join(rows) + "\n:::\n\n"
    return block + rest, "**Details:**" not in rest


def split_text(text: str) -> tuple[str, str]:
    match = FRONT.match(text)
    assert match is not None
    return text[: match.end()], text[match.end() :]


def set_kind(head: str, kind: str) -> str:
    return re.sub(r'(?m)^kind = "[a-z_]+"$', f'kind = "{kind}"', head, count=1)


def add_tag(head: str, tag: str) -> str:
    match = re.search(r"(?m)^tags = \[(.*?)\]$", head)
    if match:
        current = [part.strip().strip('"') for part in match.group(1).split(",") if part.strip()]
        if tag in current:
            return head
        return head[: match.start()] + "tags = [" + ", ".join(f'"{t}"' for t in current + [tag]) + "]" + head[match.end() :]
    for anchor in ("provenance = [", "[[sources]]", "[fields]"):
        index = head.find("\n" + anchor)
        if index >= 0:
            return head[: index + 1] + f'tags = ["{tag}"]\n' + head[index + 1 :]
    raise AssertionError("no place for tags")


def set_source_ids(head: str, ids: list[str]) -> str:
    line = "source_ids = [" + ", ".join(f'"{i}"' for i in ids) + "]"
    return re.sub(r"(?ms)^source_ids = \[.*?\]$", line, head, count=1)


def add_source_rows(head: str, rows: list[tuple[str, str | None]]) -> str:
    text = ""
    for publication, page in rows:
        text += f'[[sources]]\npublication = "{publication}"\n'
        if page:
            text += f'page = "{page}"\n'
    index = head.index("\n\n[fields]") + 1
    return head[:index] + text + head[index:]


def plan_kinds(entries: dict[str, Entry], titles: dict[str, str], plan: Plan) -> None:
    for entry in entries.values():
        folder = entry.folder
        if entry.id.startswith("ref/carried/") or folder not in set(FOLDERS) | {"haunt"}:
            continue
        if folder == "haunt":
            if HAUNT_KIND is None:
                plan.keeps.append((entry, "keep-rule", HAUNT_REASON))
            else:
                if entry.kind != HAUNT_KIND:
                    plan.kind_changes.append((entry, HAUNT_KIND, None, "haunt"))
            continue
        kind, _ = FOLDERS[folder]
        tag, basis = tag_for(folder, entry.body)
        needs_tag = FOLDERS[folder][1] is not None
        if needs_tag and tag is None:
            plan.keeps.append((entry, "keep-rule", f"cannot tag: {basis}"))
            continue
        done = entry.kind == kind and (not needs_tag or tag in entry.tags)
        if folder == "skill":
            done = done and "**Details:**" not in entry.body
        if done:
            continue
        plan.kind_changes.append((entry, kind, tag, basis))


# ---------------------------------------------------------------- duplicates


def candidates(entries: dict[str, Entry]) -> dict[str, list[Entry]]:
    out: dict[str, list[Entry]] = collections.defaultdict(list)
    for entry in entries.values():
        out[norm(entry.title)].append(entry)
    return out


def evidence_page(others: list[Entry], publication: str) -> str | None:
    for other in others:
        for row in other.sources:
            if row["publication"] == publication and row.get("page"):
                return row["page"]
    return None


def plan_duplicates(entries: dict[str, Entry], titles: dict[str, str], plan: Plan) -> None:
    by_title = candidates(entries)
    for entry in sorted(entries.values(), key=lambda e: e.id):
        folder = entry.folder
        if entry.id.startswith("ref/carried/") or folder not in PAIR_KIND | HOLD_FOLDERS:
            continue
        want = (PAIR_KIND | HOLD_FOLDERS)[folder]
        same = [e for e in by_title[norm(entry.title)] if e.id != entry.id]
        for other in sorted(same, key=lambda e: e.id):
            carried = (
                other.id.startswith("ref/carried/")
                and "/monsters/" not in other.id
                and other.kind == want
            )
            twin = folder == "drug" and other.kind == "item" and set(other.source_ids) & set(entry.source_ids)
            if folder in HOLD_FOLDERS and carried and set(other.source_ids) & set(entry.source_ids):
                plan.holds.append(
                    (entry.id, other.id, "poison", "owner decision: the item is bought, the affliction is a rule; the issue does not name the kept one")
                )
                continue
            if twin:
                plan.holds.append((entry.id, other.id, "item-twin", "an item is bought: the pair keeps both until the owner decides"))
                continue
            variant = (
                folder in PAIR_KIND
                and other.kind == want
                and (
                    ("/monsters/" in other.id and other.id.startswith("ref/carried/"))
                    or other.id.startswith("ref/affliction/")
                )
            )
            if variant:
                plan.holds.append(
                    (
                        entry.id,
                        other.id,
                        "variant",
                        "printed in the text of a creature: it stays with that creature's page and is no duplicate of the rules entry",
                    )
                )
                continue
            if folder not in PAIR_KIND or not carried:
                continue
            shared = set(other.source_ids) & set(entry.source_ids)
            others = [e for e in same if e.id != other.id and e.kind != entry.kind]
            if not shared:
                union = set(other.source_ids) | set(entry.source_ids)
                if not any(union <= set(e.source_ids) for e in same + [entry] if e.id not in (entry.id, other.id)):
                    plan.holds.append((entry.id, other.id, "hold", "different book, and no entry prints both books"))
                    continue
            forward = uncovered(other, simulate(entry))
            if not forward or only_mergeable(other, forward, folder):
                keep, drop, why = entry, other, "the imported entry holds every fact of the carried entry"
            else:
                backward = uncovered(entry, other)
                if not backward:
                    keep, drop, why = other, entry, "only the carried entry holds every fact of the imported entry"
                else:
                    plan.holds.append(
                        (
                            entry.id,
                            other.id,
                            "hold",
                            f"each holds text the other lacks: {len(forward)} fact(s) only in the carried entry (for example {forward[0]!r}), {len(backward)} only in the imported one",
                        )
                    )
                    continue
            pair = Pair(kept=keep, dropped=drop, reason=why)
            if folder == "skill" and keep is entry:
                pair.intro = intro_line(drop)
            pair.none_rows = missing_none_rows(drop, keep)
            kept_ids = set(keep.source_ids)
            for publication in drop.source_ids:
                if publication not in kept_ids:
                    pair.new_sources.append((publication, evidence_page(others, publication)))
            for row in drop.sources:
                if row["publication"] in kept_ids and not any(
                    r["publication"] == row["publication"] for r in keep.sources
                ) and row.get("page"):
                    pair.new_sources.append((row["publication"], row["page"]))
            plan.pairs.append(pair)


def simulate(entry: Entry) -> Entry:
    """The imported entry as the kinds pass leaves it, so that the facts compare like with like."""
    if entry.folder == "skill":
        body, _ = convert_skill_body(entry.body)
        return Entry(**{**entry.__dict__, "body": body})
    return entry


def intro_line(carried: Entry) -> str | None:
    """The italic opening line of a carried skill (`_You know how to tell a lie._`)."""
    for block in re.split(r"\n\s*\n", carried.body):
        block = block.strip()
        if block.startswith("::: statblock") or block == ":::":
            continue
        return block if block.startswith("_") and block.endswith("_") and "\n\n" not in block else None
    return None


def only_mergeable(carried: Entry, lost: list[str], folder: str) -> bool:
    """Whether every fact the imported entry lacks is one that the merge copies over."""
    if folder == "skill":
        intro = intro_line(carried)
        rest = [fact for fact in lost if not (intro and fact == intro.replace("\n", " ")[:90])]
        return not rest
    return False


def missing_none_rows(dropped: Entry, kept: Entry) -> list[str]:
    """Labels of `Label: none` stat block rows of `dropped` that `kept` has no line for."""
    out = []
    for row in re.findall(r"(?m)^([A-Za-z ]+): none$", dropped.body):
        if not re.search(rf"(?m)^\*\*{re.escape(row)}[^*]*\*\*", kept.body) and not re.search(
            rf"(?m)^{re.escape(row)}:", kept.body
        ):
            out.append(row)
    return out


# ---------------------------------------------------------------- applying


def apply_kinds(plan: Plan, entries: dict[str, Entry]) -> None:
    for entry, kind, tag, _basis in plan.kind_changes:
        head, rest = split_text(entry.text)
        head = set_kind(head, kind)
        if tag:
            head = add_tag(head, tag)
        if entry.folder == "skill":
            body = rest.lstrip("\n")
            lead = rest[: len(rest) - len(body)]
            body, ok = convert_skill_body(body)
            if not ok:
                raise SystemExit(f"{entry.id}: the skill labels are not in the expected form")
            rest = lead + body
        entry.text = head + rest


def rewrite_references(root: Path, plan: Plan, entries: dict[str, Entry]) -> list[tuple[str, str, str]]:
    """Point every reference to a dropped id at the kept id. Returns `(file, dropped id, anchor)` rows
    for the link anchors that the kept entry lacks and that were dropped."""
    mapping = {pair.dropped.id: pair.kept for pair in plan.pairs}
    if not mapping:
        return []
    pattern = re.compile(
        "(?<!" + ID_CHARS + ")("
        + "|".join(re.escape(i) for i in sorted(mapping, key=len, reverse=True))
        + ")(?!" + ID_CHARS + r")(#[A-Za-z0-9_-]+)?"
    )
    dropped_anchors: list[tuple[str, str, str]] = []
    skip = {"aliases.toml", "exclusions.toml", "history.toml"}
    files = sorted(
        p
        for p in list((root / "entries").rglob("*.md"))
        + [root / name for name in ("option-groups.toml", "power-exceptions.toml", "legal.toml")]
        if p.is_file() and p.name not in skip
    )
    gone = {pair.dropped.path for pair in plan.pairs}
    for path in files:
        if path in gone:
            continue
        entry = entries.get(path_id(path)) if "entries" in path.parts else None
        text = entry.text if entry is not None else path.read_text(encoding="utf-8")
        if "ref/" not in text:
            continue

        def swap(match: re.Match) -> str:
            kept = mapping[match.group(1)]
            anchor = match.group(2) or ""
            if anchor and not re.search(rf"\{{{re.escape(anchor)}\}}", kept.body):
                dropped_anchors.append((str(path), match.group(1), anchor))
                anchor = ""
            return kept.id + anchor

        new = pattern.sub(swap, text)
        if new != text:
            if entry is not None:
                entry.text = new
            else:
                path.write_text(new, encoding="utf-8")
    return dropped_anchors


def path_id(path: Path) -> str:
    parts = path.parts
    return "ref/" + "/".join(parts[parts.index("entries") + 1 :])[: -len(".md")]


def retarget_books(root: Path, plan: Plan) -> list[tuple[str, str]]:
    """Moves the book node of a dropped entry to the kept entry, or removes the dropped leaf node when
    the kept entry already has a node in the same book. Returns `(book, dropped id)` for removed nodes."""
    removed: list[tuple[str, str]] = []
    for book in sorted((root / "books").glob("*.toml")):
        text = book.read_text(encoding="utf-8")
        blocks = re.split(r"(?m)^(?=\[\[books\.chapters)", text)
        changed = False
        for pair in plan.pairs:
            dropped, kept = pair.dropped.id, pair.kept.id
            if f'entry = "{dropped}"' not in text:
                continue
            kept_here = f'entry = "{kept}"' in "".join(blocks)
            for index, block in enumerate(blocks):
                if f'entry = "{dropped}"\n' not in block + "\n":
                    continue
                if not kept_here:
                    blocks[index] = block.replace(f'entry = "{dropped}"', f'entry = "{kept}"')
                else:
                    header = block.splitlines()[0]
                    nxt = blocks[index + 1].splitlines()[0] if index + 1 < len(blocks) else ""
                    child = header[:-2] + ".children]]"
                    if nxt.startswith(child):
                        raise SystemExit(f"{book.name}: the node of {dropped} has children and {kept} is placed")
                    blocks[index] = ""
                    removed.append((book.stem, dropped))
                changed = True
            text = "".join(blocks)
            blocks = re.split(r"(?m)^(?=\[\[books\.chapters)", text)
        if changed:
            book.write_text(text, encoding="utf-8")
    return removed


def apply_pair_merges(plan: Plan) -> None:
    for pair in plan.pairs:
        kept, dropped = pair.kept, pair.dropped
        head, rest = split_text(kept.text)
        union = list(kept.source_ids) + [s for s in dropped.source_ids if s not in kept.source_ids]
        if union != kept.source_ids:
            head = set_source_ids(head, union)
        if pair.new_sources:
            head = add_source_rows(head, pair.new_sources)
        body = rest
        if pair.intro:
            body = re.sub(r"(?s)(\A\s*::: statblock\n.*?\n:::\n\n)", lambda m: m.group(1) + pair.intro + "\n\n", body, count=1)
        for label in pair.none_rows:
            body = body.rstrip("\n") + f"\n\n**{label}:** none\n"
        kept.text = head + body


def alias_file(root: Path, plan: Plan) -> None:
    path = root / "aliases.toml"
    text = path.read_text(encoding="utf-8")
    for pair in plan.pairs:
        text = text.replace(f'target = "{pair.dropped.id}"\n', f'target = "{pair.kept.id}"\n')
    head, _, rows = text.partition("\n[[entries]]\n")
    blocks = ("[[entries]]\n" + rows).split("\n\n")
    blocks = [b for b in blocks if b.strip()]
    olds = [re.search(r'old = "([^"]+)"', b).group(1) for b in blocks]
    for pair in sorted(plan.pairs, key=lambda p: p.dropped.id):
        old = pair.dropped.id
        if old in olds:
            index = olds.index(old)
            assert f'target = "{pair.kept.id}"' in blocks[index], f"{old} already aliased elsewhere"
            continue
        if pair.kept.id in olds:
            raise SystemExit(f"{pair.kept.id} is an old id in aliases.toml: a target may not be one")
        index = bisect.bisect_left(olds, old)
        olds.insert(index, old)
        blocks.insert(index, f'[[entries]]\nold = "{old}"\ntarget = "{pair.kept.id}"\nbasis = "shared"')
    path.write_text(head + "\n" + "\n\n".join(blocks).rstrip("\n") + "\n", encoding="utf-8")


def exclusions_file(root: Path, plan: Plan) -> None:
    path = root / "exclusions.toml"
    text = path.read_text(encoding="utf-8")
    new = ""
    for pair in plan.pairs:
        if f'path = "{pair.dropped.id}"' in text:
            continue
        new += f'[[rejected]]\npath = "{pair.dropped.id}"\nreason = "duplicate of {pair.kept.id}"\n\n'
    if not new:
        return
    index = text.index("[[resolved]]")
    path.write_text(text[:index] + new + text[index:], encoding="utf-8")


# ---------------------------------------------------------------- review file


def review_rows(plan: Plan, titles: dict[str, str]) -> list[dict]:
    rows: list[dict] = []
    for entry, kind, tag, basis in plan.kind_changes:
        rows.append(
            dict(
                entry_id=entry.id,
                action="kind",
                kind_before=entry.kind,
                kind_after=kind,
                tag=tag or "",
                other_id="",
                citation=citation(entry, titles),
                reason=basis or "folder " + entry.folder,
            )
        )
    for entry, action, reason in plan.keeps:
        rows.append(
            dict(entry_id=entry.id, action=action, kind_before=entry.kind, kind_after=entry.kind, tag="", other_id="", citation=citation(entry, titles), reason=reason)
        )
    for pair in plan.pairs:
        rows.append(
            dict(
                entry_id=pair.dropped.id,
                action="alias",
                kind_before=pair.dropped.kind,
                kind_after="",
                tag="",
                other_id=pair.kept.id,
                citation=citation(pair.kept, titles),
                reason=f"kept {pair.kept.id}: {pair.reason}",
            )
        )
        notes = []
        if pair.intro:
            notes.append("the italic opening line of the carried skill")
        notes += [f"a `{label}: none` row" for label in pair.none_rows]
        notes += [f"{p} source" + (f" page {pg}" if pg else "") for p, pg in pair.new_sources]
        if notes:
            rows.append(
                dict(entry_id=pair.kept.id, action="merge", kind_before=pair.kept.kind, kind_after="", tag="", other_id=pair.dropped.id, citation="", reason="merged from the dropped entry: " + "; ".join(notes))
            )
    for first, second, action, reason in plan.holds:
        rows.append(
            dict(entry_id=first, action=action, kind_before="", kind_after="", tag="", other_id=second, citation="", reason=reason)
        )
    return rows


def write_review(root: Path, rows: list[dict]) -> None:
    path = root / REVIEW
    old: list[dict] = []
    if path.exists():
        with path.open(encoding="utf-8", newline="") as handle:
            old = list(csv.DictReader(handle, delimiter="\t"))
    merged = {(r["entry_id"], r["action"], r["other_id"]): r for r in old}
    for row in rows:
        merged[(row["entry_id"], row["action"], row["other_id"])] = row
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for key in sorted(merged):
            writer.writerow(merged[key])


# ---------------------------------------------------------------- driver


def make_plan(root: Path, selected: tuple[str, ...]) -> tuple[Plan, dict[str, Entry], dict[str, str]]:
    entries = load_entries(root)
    titles = load_titles(root)
    plan = Plan()
    if "kinds" in selected:
        plan_kinds(entries, titles, plan)
    if "duplicates" in selected:
        plan_duplicates(entries, titles, plan)
    return plan, entries, titles


def survey(plan: Plan, entries: dict[str, Entry], selected: tuple[str, ...]) -> None:
    counts = collections.Counter(e.kind for e in entries.values())
    after = collections.Counter(counts)
    for entry, kind, _tag, _basis in plan.kind_changes:
        if entry.kind != kind:
            after[entry.kind] -= 1
            after[kind] += 1
    for pair in plan.pairs:
        after[pair.dropped.kind] -= 1
    print("kind          before   after")
    for kind in ("skill", "trap", "affliction", "rule", "item"):
        print(f"{kind:<12} {counts[kind]:>7} {after[kind]:>7}")
    folders = collections.Counter((e.folder, kind) for e, kind, _t, _b in plan.kind_changes)
    print("\nkind changes by folder:")
    for (folder, kind), n in sorted(folders.items()):
        print(f"  {folder:<10} -> {kind:<10} {n}")
    print(f"\nentries left as they are: {len(plan.keeps)}")
    for folder, n in sorted(collections.Counter(e.folder for e, _a, _r in plan.keeps).items()):
        print(f"  {folder:<10} {n}")
    print(f"\nduplicate pairs to alias: {len(plan.pairs)}")
    for key, n in sorted(collections.Counter((p.dropped.folder or "carried", "kept imported" if p.kept is not p.dropped and not p.kept.id.startswith("ref/carried/") else "kept carried") for p in plan.pairs).items()):
        print(f"  {key[0]:<14} {key[1]:<14} {n}")
    print(f"\nheld pairs (both entries stay): {len(plan.holds)}")
    for action, n in sorted(collections.Counter(a for _f, _s, a, _r in plan.holds).items()):
        print(f"  {action:<10} {n}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--pass", dest="passes", default=",".join(PASSES))
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    selected = tuple(p for p in args.passes.split(",") if p)
    unknown = set(selected) - set(PASSES)
    if unknown:
        parser.error(f"unknown pass: {', '.join(sorted(unknown))}")
    root = Path(args.root)
    plan, entries, titles = make_plan(root, selected)
    pending = len(plan.kind_changes) + len(plan.pairs)
    if args.check:
        survey(plan, entries, selected)
        print(f"\npending: {pending}")
        return 1 if pending else 0
    if not args.write:
        survey(plan, entries, selected)
        for pair in plan.pairs:
            print(f"  alias {pair.dropped.id} -> {pair.kept.id}  ({pair.reason})")
        for first, second, action, reason in plan.holds:
            print(f"  {action:<9} {first} | {second}: {reason}")
        return 0
    write_review(root, review_rows(plan, titles))
    apply_kinds(plan, entries)
    for entry in entries.values():
        if entry.text != entry.path.read_text(encoding="utf-8"):
            entry.path.write_text(entry.text, encoding="utf-8")
    if plan.pairs:
        # Order: the new ids first, so a crash leaves every old id resolving; the files go last.
        alias_file(root, plan)
        exclusions_file(root, plan)
        # Reload, because the kinds pass wrote entries; then merge, retarget and delete.
        entries = load_entries(root)
        plan, entries, titles = make_plan(root, ("duplicates",))
        anchors = rewrite_references(root, plan, entries)
        apply_pair_merges(plan)
        for entry in entries.values():
            if entry.text != entry.path.read_text(encoding="utf-8"):
                entry.path.write_text(entry.text, encoding="utf-8")
        removed = retarget_books(root, plan)
        extra = [
            dict(entry_id=path, action="link-anchor-dropped", kind_before="", kind_after="", tag="", other_id=dropped, citation="", reason=f"the kept entry has no heading {anchor}")
            for path, dropped, anchor in anchors
        ] + [
            dict(entry_id=dropped, action="book-node-removed", kind_before="", kind_after="", tag="", other_id=book, citation="", reason="the kept entry already has a node in this book")
            for book, dropped in removed
        ]
        if extra:
            write_review(root, extra)
        for pair in plan.pairs:
            pair.dropped.path.unlink()
    print(f"wrote {len(plan.kind_changes)} kind changes and {len(plan.pairs)} aliases; run corpus-fmt next")
    return 0


def self_test() -> int:
    failures = 0

    def expect(name: str, got, want) -> None:
        nonlocal failures
        if got != want:
            failures += 1
            print(f"FAIL {name}: {got!r} != {want!r}")

    pairs = (
        "**Associated Skill**\n\n**Details:** Dexterity\n\n**Trained Only**\n\n**Details:** No\n\n"
        "**Armor Check Penalty**\n\n**Details:** Yes\n\n**Optional Unchained Skill**\n\n**Details:** No\n\n"
        "**Optional Background Skill**\n\n**Details:** No\n\n### Action\n\nNone.\n\n**5 Ranks**\n\n**Details:** You move.\n"
    )
    body, ok = convert_skill_body(pairs)
    expect("skill ok", ok, True)
    expect(
        "skill block",
        body.split("\n\n")[0],
        "::: statblock\nKey Ability: Dexterity\nTrained Only: No\nArmor Check Penalty: Yes\n"
        "Optional Unchained Skill: No\nOptional Background Skill: No\n:::",
    )
    expect("skill pair", "**5 Ranks:** You move." in body and "Details" not in body, True)
    expect("type word", type_word("**Type:** Disease (Injury)\n"), "disease")
    expect("type word madness", type_word("**Type** greater madness; **Save DC** 22\\\n"), "greater")
    expect("tag drug", tag_for("drug", "**Type:** ingested")[0], "addiction")
    expect("tag madness", tag_for("madness", "**Type** lesser madness")[0], "insanity")
    expect("tag curse", tag_for("curse", "**Type:** Curse (Regional curse)")[0], "curse")
    expect("tag trap", tag_for("trap", "**Type:** Mechanical")[0], "mechanical")
    expect("tag outside", tag_for("disease", "**Type:** Poison")[0], "poison")
    head = '+++\nid = "ref/x/y"\nkind = "rule"\ntitle = "Y"\nsource_ids = ["a"]\nprovenance = [\n]\n[fields]\nkind = "none"\n+++\n'
    expect("set kind", set_kind(head, "trap").split("\n")[2], 'kind = "trap"')
    expect("fields kind kept", 'kind = "none"' in set_kind(head, "trap"), True)
    expect("add tag", 'tags = ["magic"]\nprovenance' in add_tag(head, "magic"), True)
    expect("tag idempotent", add_tag(add_tag(head, "magic"), "magic"), add_tag(head, "magic"))
    expect("tokens", tokens("Dex 12^1^ – Str"), ["dexterity", "12", "strength"])
    carried = Entry(Path("c"), "", "ref/carried/c", "trap", "T", ["a"], [], [], "::: statblock\nType: magic\nReset: none\n:::\n")
    imported = Entry(Path("p"), "", "ref/trap/t", "rule", "T", ["a"], [], [], "**Type:** Magic\n\n**Effect:** x\n")
    expect("none rows", missing_none_rows(carried, imported), ["Reset"])
    expect("covered", uncovered(carried, imported), [])
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
