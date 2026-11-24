#!/usr/bin/env python3
"""Restore the topic lists of the navigation hubs (phynics/cast-iron#461, S10).

    python3 scripts/hub-topic-lists-461.py <corpus-dir> --dataset <dir> [--list | --apply | --check]
        [--review review.tsv]

The import dropped the `subtopics` list of a rules record of the dataset that the corpus pins
(`pathfinder-data-1-e`, the commit of `legal.toml`). Gamemastery, Specific Campaign Types and
twelve other hubs are one dataset sentence now, followed by nothing. Owner ruling of 2026-11-24
(design (a) of the issue): the hub gets its list back as `::: entry-link` blocks, one per
subtopic, in upstream order. The books of the listed entries then carry the credit, and the hub
keeps only its home book.

`<dataset>` is a checkout of that dataset (read only). The script never writes there.

Which entries (`--list` prints them, and `--apply` acts only on these):

  * the entry has a provenance record of the dataset whose record has a `subtopics` list,
  * the entry body has no `::: entry-link` block and at most 40 words (a hub with real text,
    like Races or Militia Terminology, is not a navigation hub),
  * the entry is in the `corpus-check` warning: a book that is not the first one in `source_ids`
    and has no `[[sources]]` row.

How a subtopic record resolves to one corpus entry: the first rule that gives exactly one entry
wins. (1) The entry from the same upstream file with the record name, (2) the entry from a
`json/rules_*.json` file, (3) the only entry with that record name. A rule that gives two or more
entries does not pick one: the subtopic goes to the review file (`--review`, problem `ambiguous`)
and the hub gets no block for it. A subtopic without any entry goes there too (`no-entry`). A record
name that several entries share (`weather` is a domain and a blessing too) is settled by rule 1 or 2
to the rules entry, and the review file lists it as `collision-resolved` with the entry it chose.

The blocks go after the hub's text, in upstream order, with the target's title. A target that the
body links already (an inline link or a block) is skipped, and so is a repeated subtopic. Running
twice changes nothing.

`--check` writes nothing. It exits 1 when a hub still lacks a block, and 2 when a block does not
match what the dataset says: a block that no subtopic resolves to, a subtopic without its block, or
blocks in another order than upstream. Output has ids only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

DATASET_ID = "pathfinder-data-1-e"
MAX_WORDS = 40
FRONT = re.compile(r"\A\+\+\+\n(.*?)\n\+\+\+\n(.*)\Z", re.S)
LINK = re.compile(r"\]\((ref/[^)#\s]+)")
BLOCK = re.compile(r'^::: entry-link\ntarget = "([^"]+)"\ntitle = "([^"]*)"\n:::$', re.M)


def read_entry(path: Path):
    m = FRONT.match(path.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"refused: {path} has no front matter")
    return tomllib.loads(m.group(1)), m.group(2)


def load_corpus(root: Path):
    """All entries that carry a provenance record of the dataset, by id."""
    ents = {}
    for p in sorted((root / "entries").rglob("*.md")):
        head = p.read_text(encoding="utf-8")
        if DATASET_ID not in head[:3000]:
            continue
        fm, body = read_entry(p)
        if any(pv.get("dataset") == DATASET_ID for pv in fm.get("provenance", [])):
            ents[fm["id"]] = (fm, body, p)
    return ents


class Dataset:
    def __init__(self, root: Path):
        self.root = root
        self.cache: dict[str, dict] = {}

    def file(self, rel: str) -> dict:
        if rel not in self.cache:
            self.cache[rel] = json.loads((self.root / rel).read_text(encoding="utf-8"))
        return self.cache[rel]


def in_warning(fm: dict) -> list[str]:
    """Non-first books of the entry that have no `[[sources]]` row."""
    rows = {s.get("publication") for s in fm.get("sources", [])}
    return [b for b in fm["source_ids"][1:] if b not in rows]


def candidates(ents, ds: Dataset):
    out = []
    for eid, (fm, body, path) in sorted(ents.items()):
        if BLOCK.search(body) or len(body.split()) > MAX_WORDS:
            continue
        if not in_warning(fm):
            continue
        for pv in fm["provenance"]:
            if pv.get("dataset") != DATASET_ID or not (ds.root / pv["path"]).exists():
                continue
            rec = ds.file(pv["path"]).get(pv["record"])
            if isinstance(rec, dict) and rec.get("subtopics"):
                out.append((eid, pv["path"], pv["record"], rec["subtopics"]))
                break
    return out


def index_records(ents):
    by_rec = defaultdict(list)
    for eid, (fm, _b, _p) in ents.items():
        for pv in fm["provenance"]:
            if pv.get("dataset") == DATASET_ID:
                by_rec[pv["record"]].append((eid, pv["path"]))
    return by_rec


def resolve(rec: str, upstream_path: str, by_rec) -> tuple[str | None, list[str]]:
    """The one entry id for a subtopic record, or None and the ids that compete."""
    hits = by_rec.get(rec, [])
    for keep in (
        lambda p: p == upstream_path,
        lambda p: p.startswith("json/rules_"),
        lambda p: True,
    ):
        ids = sorted({e for e, p in hits if keep(p)})
        if len(ids) == 1:
            return ids[0], ids
        if len(ids) > 1:
            return None, ids
    return None, []


def review_rows(ents, by_rec, hubs):
    """The subtopics that need a look: `ambiguous` (two or more entries, no rule picks one),
    `no-entry`, and `collision-resolved` (several entries share the record name and rule 1 or 2
    chose the rules entry). `hubs` is a list of (hub id, upstream path, subtopic records)."""
    review = []
    for eid, path, subs in hubs:
        for rec in subs:
            tid, ids = resolve(rec, path, by_rec)
            rivals = sorted({e for e, _p in by_rec.get(rec, [])})
            if tid is None:
                review.append((eid, rec, "ambiguous" if ids else "no-entry", " ".join(ids), ""))
            elif len(rivals) > 1:
                review.append((eid, rec, "collision-resolved", " ".join(rivals), tid))
    return list(dict.fromkeys(review))  # a subtopic that the dataset lists twice is reviewed once


def restored_hubs(ents, ds: Dataset):
    """The hubs that have their blocks: at most 40 words besides them, a record with `subtopics`."""
    out = []
    for eid, (fm, body, _p) in sorted(ents.items()):
        if not BLOCK.search(body) or len(BLOCK.sub("", body).split()) > MAX_WORDS:
            continue
        for pv in fm["provenance"]:
            if pv.get("dataset") == DATASET_ID and (ds.root / pv["path"]).exists():
                rec = ds.file(pv["path"]).get(pv["record"])
                if isinstance(rec, dict) and rec.get("subtopics"):
                    out.append((eid, pv["path"], rec["subtopics"]))
                    break
    return out


def plan(root: Path, ds: Dataset):
    ents = load_corpus(root)
    by_rec = index_records(ents)
    hubs = []
    cands = candidates(ents, ds)
    for eid, path, record, subs in cands:
        fm, body, file = ents[eid]
        linked = set(LINK.findall(body))
        blocks, seen = [], {eid}
        for rec in subs:
            tid, ids = resolve(rec, path, by_rec)
            if tid is None:
                continue
            if tid in seen or tid in linked:
                continue
            seen.add(tid)
            blocks.append((tid, ents[tid][0]["title"], rec))
        hubs.append((eid, file, body, blocks))
    review = review_rows(ents, by_rec, [(eid, path, subs) for eid, path, _r, subs in cands])
    return hubs, review, ents, by_rec, cands


def render(body: str, blocks) -> str:
    text = body.rstrip("\n")
    parts = [text] + [
        f'::: entry-link\ntarget = "{t}"\ntitle = "{title}"\n:::' for t, title, _ in blocks
    ]
    return "\n\n".join(parts) + "\n"


def write_review(path: Path, review) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("hub\tsubtopic\tproblem\tentries_with_this_record\tchosen\n")
        for r in review:
            f.write("\t".join(r) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--dataset", type=Path, required=True)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--list", action="store_true")
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    ap.add_argument("--review", type=Path, help="write the subtopics that did not resolve here (TSV)")
    a = ap.parse_args()

    ds = Dataset(a.dataset)
    hubs, review, ents, by_rec, cands = plan(a.corpus, ds)
    if a.review:
        # the hubs of this run, and the hubs that already have their blocks: the file is the same
        # before and after `--apply`
        rows = review_rows(ents, by_rec, [(e, p, s) for e, p, _r, s in cands] + restored_hubs(ents, ds))
        write_review(a.review, rows)
        review = rows

    if a.list or not (a.apply or a.check):
        for eid, _f, _b, blocks in hubs:
            print(f"{eid}\t{len(blocks)} blocks")
        print(f"{len(hubs)} hubs, {sum(len(b) for *_, b in hubs)} blocks, {len(review)} unresolved subtopics")
        return 0

    # Hubs are chosen before the blocks exist; a second run finds none (a hub with a block is skipped).
    if a.check:
        pending = [h[0] for h in hubs if h[3]]
        for e in pending:
            print(f"pending: {e}")
        # a restored hub no longer lists as a candidate, so check its blocks against the dataset directly
        bad = verify_restored(a.corpus, Dataset(a.dataset))
        for e in bad:
            print(f"mismatch: {e}")
        print(f"{len(pending)} hubs pending, {len(bad)} mismatches")
        return 2 if bad else (1 if pending else 0)

    for eid, file, body, blocks in hubs:
        if not blocks:
            continue
        text = file.read_text(encoding="utf-8")
        m = FRONT.match(text)
        file.write_text("+++\n" + m.group(1) + "\n+++\n" + render(m.group(2), blocks), encoding="utf-8")
        print(f"restored {eid}: {len(blocks)} blocks")
    print(f"{sum(1 for h in hubs if h[3])} hubs, {sum(len(h[3]) for h in hubs)} blocks written, {len(review)} unresolved subtopics")
    return 0


def verify_restored(root: Path, ds: Dataset) -> list[str]:
    """Every hub of the list that has blocks: its blocks are exactly what the dataset resolves to."""
    ents = load_corpus(root)
    by_rec = index_records(ents)
    bad = []
    for eid, (fm, body, _p) in sorted(ents.items()):
        if len(re.sub(r"::: entry-link\n.*?\n:::", "", body, flags=re.S).split()) > MAX_WORDS:
            continue
        have = [t for t, _ in BLOCK.findall(body)]
        if not have:
            continue
        for pv in fm["provenance"]:
            if pv.get("dataset") != DATASET_ID or not (ds.root / pv["path"]).exists():
                continue
            rec = ds.file(pv["path"]).get(pv["record"])
            if not (isinstance(rec, dict) and rec.get("subtopics")):
                continue
            want = []
            for r in rec["subtopics"]:
                tid, _ = resolve(r, pv["path"], by_rec)
                if tid and tid != eid and tid not in want:
                    want.append(tid)
            linked = set(LINK.findall(BLOCK.sub("", body)))
            extra = [t for t in have if t not in want]
            if extra:
                bad.append(f"{eid} has a block for {extra[0]} that no subtopic resolves to")
            missing = [t for t in want if t not in have and t not in linked]
            if missing:
                bad.append(f"{eid} has no block for {missing[0]} ({len(missing)} missing)")
            if [t for t in have if t in want] != [t for t in want if t in have]:
                bad.append(f"{eid} lists its blocks in another order than the dataset")
            break
    return bad


if __name__ == "__main__":
    sys.exit(main())
