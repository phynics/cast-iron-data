#!/usr/bin/env python3
"""Record the verdicts of the link-only hubs of phynics/cast-iron#461 (S10) in the queue.

    python3 scripts/hub-verdicts-461.py <corpus-dir> --dataset <dir> [--decisions scripts/membership-verdicts-461-s10.tsv]
        [--queue scripts/membership-queue-461.tsv] [--write | --check]

Owner ruling of 2026-11-24, design (a): a link-only hub keeps only its home book. Its topic lists are
back (`scripts/hub-topic-lists-461.py`). For each queue row (hub, book) of the 14 navigation hubs
that has no verdict and is in the `corpus-check` warning, this script derives the verdict from the
corpus and the pinned dataset:

  hub-link <target>         the book is in `source_ids` of an entry that the hub lists (an
                            `entry-link` block, a link in its body, or a dataset subtopic), or of an
                            entry that a listed entry lists as a block or a dataset subtopic (one
                            level deeper: Basics lists Classes, which lists Hybrid Classes in the
                            dataset). The verdict is
                            `remove`; `print_page` is the page of the listed entry's `[[sources]]`
                            row for the book, else `none`. Depth two names the first listed entry.
  hub-no-evidence <record>  no listed entry carries the book. `remove`. `<record>` is the subtopic
                            record whose name also names an unrelated entry of that book (`weather`
                            is a domain and a blessing too), or `none`.

The rows of `--decisions` are the reviewed verdicts of the other S10 rows (cites, removals that a
reading decided, the listed-link rows): `entry`, `book`, `verdict`, `print_page`, `evidence`. A row
there is written as it stands. A decisions row for a pair that the script derives is refused.

`--write` puts `verdict`, `print_page` and `evidence` into the queue, sets `slice` to `done` and
empties `ruling` (the queue script does the same for a decided row). It never changes a row that
has a verdict already, and a second run changes nothing. `--check` writes nothing and exits 1 when
a derived or decided row is missing or differs. The Gamemastery row of the GameMastery Guide is
left out on purpose: its curated node stays until phynics/cast-iron-data#277 (owner ruling of
2026-11-24), so the membership stays. Output has ids and book ids only.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HUBS = {
    "advanced-gm-topics", "advanced-magic-topics", "advanced-player-topics", "basics", "gamemastery",
    "gm-specific-campaigns", "optional-alignment-changes", "optional-combat-changes",
    "optional-magic-changes", "optional-subsystems", "seafaring-and-piracy-rules", "specific-rulesets",
    "traits-and-other-details", "universal-path-abilities",
}
S10_GROUPS = ("hub-cited", "link-only-hub", "faith-excerpt")
# Left out on purpose, with no verdict (see the module docstring): the memberships stay.
SKIP = {
    ("ref/rule/gamemastery", "game-mastery-guide"),  # the curated node of the GameMastery Guide stays (data #277)
}


def load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


lists = load("hub_topic_lists", "hub-topic-lists-461.py")


class Corpus:
    def __init__(self, root: Path, ds):
        self.ents = lists.load_corpus(root)
        self.by_rec = lists.index_records(self.ents)
        self.ds = ds

    def upstream(self, eid: str):
        for pv in self.ents[eid][0]["provenance"]:
            if pv.get("dataset") == lists.DATASET_ID and (self.ds.root / pv["path"]).exists():
                rec = self.ds.file(pv["path"]).get(pv["record"])
                if isinstance(rec, dict):
                    return pv, rec
        return None, {}

    def listed(self, eid: str, body_links: bool = True) -> list[str]:
        """Entries that `eid` lists: its blocks and body links, then its dataset subtopics. With
        `body_links` off only the blocks and the subtopics count (a link in running text is not a
        list: the second level uses it, so that the Foraging page does not list the skill it names)."""
        _fm, body, _p = self.ents[eid]
        out = [t for t, _ in lists.BLOCK.findall(body)]
        if body_links:
            out += lists.LINK.findall(body)
        out = list(dict.fromkeys(out))
        pv, rec = self.upstream(eid)
        for s in rec.get("subtopics", []):
            t, _ = lists.resolve(s, pv["path"], self.by_rec)
            if t and t != eid and t not in out:
                out.append(t)
        return out

    def carries(self, eid: str, book: str) -> bool:
        return eid in self.ents and book in self.ents[eid][0]["source_ids"]

    def page(self, eid: str, book: str) -> str:
        for s in self.ents[eid][0].get("sources", []):
            if s.get("publication") == book and s.get("page"):
                return s["page"]
        return "none"

    def verdict(self, hub: str, book: str) -> tuple[str, str]:
        first = self.listed(hub)
        for t in first:
            if self.carries(t, book):
                return self.page(t, book), f"hub-link {t}"
        for t in first:
            if t in self.ents and any(self.carries(t2, book) for t2 in self.listed(t, body_links=False)):
                return "none", f"hub-link {t}"
        pv, rec = self.upstream(hub)
        for s in rec.get("subtopics", []):
            if any(self.carries(e, book) for e, _p in self.by_rec.get(s, [])):
                return "none", f"hub-no-evidence {s}"
        return "none", "hub-no-evidence none"


def read_tsv(path: Path):
    with open(path, encoding="utf-8", newline="") as f:
        rdr = csv.DictReader(f, delimiter="\t")
        return rdr.fieldnames, list(rdr)


def wanted(corpus: Corpus, queue_rows: list[dict], decisions: Path | None) -> dict[tuple[str, str], tuple[str, str, str]]:
    out = {}
    for r in queue_rows:
        key = (r["entry"], r["book"])
        if r["entry"].removeprefix("ref/rule/") in HUBS and r["entry"].startswith("ref/rule/") \
                and key not in SKIP and r["member"] != "1":
            derived = r["evidence"].split(" ")[0] in ("hub-link", "hub-no-evidence")
            if not (derived or (not r["verdict"] and r["in_warning"] == "yes")):
                continue
            page, ev = corpus.verdict(r["entry"], r["book"])
            out[key] = ("remove", page, ev)
    if decisions:
        _h, rows = read_tsv(decisions)
        for d in rows:
            key = (d["entry"], d["book"])
            if key in out:
                raise SystemExit(f"refused: decisions row {key[0]} in {key[1]} is derived by the script")
            if not d["verdict"] or not d["print_page"] or not d["evidence"]:
                raise SystemExit(f"refused: decisions row {key[0]} in {key[1]} is incomplete")
            out[key] = (d["verdict"], d["print_page"], d["evidence"])
    return out


def write_queue(path: Path, fields: list[str], rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(fields) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in fields) + "\n")


def refresh_warning(root: Path, queue_path: Path) -> int:
    """The three columns that a change of the corpus moves, from the corpus: `in_warning` (`yes`
    exactly when the `corpus-check` warning lists the pair), `body_line` (a body source line names
    the book) and `group` (a function of the entry, the body line and the book's PDF). The queue
    script computes the same values when it has a fresh screen; this needs none. `body_line` and
    `group` change only on the rows of the S10 groups. Verdicts and every other column stay."""
    mq = load("membership_queue", "membership-queue-461.py")
    pubs, entries, _t = mq.load(root)
    warn = mq.warning_pairs(entries)
    fields, rows = read_tsv(queue_path)
    changed = {"in_warning": 0, "body_line": 0, "group": 0}
    for r in rows:
        d = entries[r["entry"]]
        body_line = mq.apply.body_citation("+++\n+++\n" + d["_body"], pubs[r["book"]]["title"])
        now = {"in_warning": "yes" if (r["book"], r["entry"]) in warn else "",
               "body_line": "yes" if body_line else "",
               "group": mq.group_of(d, body_line, r["pdf"] == "yes")}
        for col, v in now.items():
            # `body_line` and `group` are the slice's own: other groups keep what their slices wrote
            if col != "in_warning" and r["group"] not in S10_GROUPS:
                continue
            if r[col] != v:
                r[col] = v
                changed[col] += 1
    write_queue(queue_path, fields, rows)
    print(f"changed {changed}; the warning lists {len(warn)} memberships")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--dataset", type=Path, required=True)
    ap.add_argument("--decisions", type=Path, default=HERE / "membership-verdicts-461-s10.tsv")
    ap.add_argument("--queue", type=Path, default=HERE / "membership-queue-461.tsv")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--refresh-warning", action="store_true",
                      help="set `in_warning`, `body_line` and `group` of every queue row from the corpus (after the apply scripts ran)")
    a = ap.parse_args()
    if a.refresh_warning:
        return refresh_warning(a.corpus, a.queue)

    fields, rows = read_tsv(a.queue)
    corpus = Corpus(a.corpus, lists.Dataset(a.dataset))
    want = wanted(corpus, rows, a.decisions if a.decisions.is_file() else None)
    index = {(r["entry"], r["book"]): r for r in rows}
    missing = sorted(set(want) - set(index))
    if missing:
        raise SystemExit("refused: not in the queue: " + ", ".join(f"{e} in {b}" for e, b in missing[:5]))

    pending = []
    for key, (verdict, page, ev) in sorted(want.items()):
        r = index[key]
        if (r["verdict"], r["print_page"], r["evidence"]) != (verdict, page, ev):
            if r["verdict"] and r["verdict"] != verdict:
                raise SystemExit(f"refused: {key[0]} in {key[1]} has verdict {r['verdict']!r}, not {verdict!r}")
            pending.append(key)
    if a.check or not a.write:
        for e, b in pending[:20]:
            print(f"pending: {e} in {b}")
        print(f"{len(want)} verdicts, {len(pending)} not in the queue")
        return 1 if (pending and a.check) else 0

    for key in pending:
        verdict, page, ev = want[key]
        r = index[key]
        r["verdict"], r["print_page"], r["evidence"], r["slice"], r["ruling"] = verdict, page, ev, "done", ""
    write_queue(a.queue, fields, rows)
    print(f"{len(pending)} verdicts written, {len(want) - len(pending)} already there")
    return 0


if __name__ == "__main__":
    sys.exit(main())
