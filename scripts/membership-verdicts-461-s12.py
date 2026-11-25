#!/usr/bin/env python3
"""Record the reviewed S12 verdicts of phynics/cast-iron#461 in the queue and the helper files.

    python3 scripts/membership-verdicts-461-s12.py <corpus-dir>
        [--verdicts scripts/membership-verdicts-461-s12.tsv] [--credits scripts/expansion-credits-461-s12.tsv]
        [--check]

S12 is the slice of the books that were not among the owner's PDFs when the queue was made: the
Player's Guides and Adventure Path volumes (the owner added them on 2026-11-25). The verdict file
has one row per (book, entry), read in the book:

  * `verdict` is `cite` (the book prints the entry; `print_page` is the printed page, `membership-apply.py`
    writes the `[[sources]]` row), `keep` (the entry has its row already), `remove` (the book does not
    print the entry), or `expands` (the book is out of `source_ids` already and prints favored class options
    or the like that no entry holds: the script adds a `credit` action of class `expands-no-via` with the
    page `print_page` to `scripts/expansion-credits-461-s12.tsv`; S9 ruling 1 of 2026-11-24). A row that is decided already takes a new verdict only when `replaces` names the old one
    (the 92 figurine memberships: `keep` with evidence `unverified-no-pdf` becomes `remove`). Evidence
    `unverified-no-pdf` stays on a row whose book is still not among the PDFs (a blog post).
  * a pair that has no queue row yet (the book had a `[[sources]]` row, so the warning never listed it) gets
    one, built from the corpus.
  * `proposed_primary` and `proposed_status` clear the gate of a removal of the entry's first book (the new
    first book is `proposed_primary`; `print_page` is the page that it prints).

For each row the script

  * writes `verdict`, `print_page`, `evidence` and slice `done` into the queue
    (`scripts/membership-queue-461.tsv`),
  * for `remove` with a `[[sources]]` row: adds the audit row that releases the row
    (`scripts/membership-citation-audit-461.tsv`; class `wrong-credit`, or `mention`), and
  * for `keep` whose `[[sources]]` page differs from `print_page`: adds a `page` action to
    `scripts/expansion-credits-461-s12.tsv` (`scripts/expansion-credits-apply.py` applies it).

Every queue row of a book that the verdict file reads in print (any row but evidence `unverified-no-pdf`)
gets `pdf = yes` and the group that follows from it. Apply the corpus changes afterwards with
`membership-apply.py` (removals and cites). Running again changes nothing. `--check` writes nothing and exits
1 when a row is not recorded yet. Output has ids and book ids only; the verdict file holds book titles and
printed pages, never book text, file names or paths.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIT_COLS = ["entry", "book", "class", "cited_page", "print_page", "family", "related_cite", "edge",
              "mention_pages", "mention_kind", "read", "evidence", "invalidated"]
CREDIT_COLS = ["entry", "book", "action", "class", "cited_page", "print_page", "family", "related_cite",
               "edge", "mention_pages", "mention_kind", "read", "evidence", "invalidated", "via", "primary_to"]
WRONG = ("the book prints neither this entry nor a related entry on the cited page; "
         "the page row is a sibling's or the generic section's page copied over.")
MENTION = ("the book prints neither this entry nor a related entry; it only mentions it. "
           "Owner decision 2026-11-17: a mention is not a printing, so the membership goes")
UNVERIFIED = "unverified-no-pdf"


def load_module(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def read_tsv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path: Path, cols: list[str], rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def header(root: Path, entry: str) -> dict:
    text = (root / "entries" / (entry.split("/", 1)[1] + ".md")).read_text(encoding="utf-8")
    return tomllib.loads(text.split("+++\n")[1])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", type=Path)
    ap.add_argument("--verdicts", type=Path, default=HERE / "membership-verdicts-461-s12.tsv")
    ap.add_argument("--queue", type=Path, default=HERE / "membership-queue-461.tsv")
    ap.add_argument("--audit", type=Path, default=HERE / "membership-citation-audit-461.tsv")
    ap.add_argument("--credits", type=Path, default=HERE / "expansion-credits-461-s12.tsv")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    mq = load_module("membership_queue", "membership-queue-461.py")
    pubs, entries, title_to_pub = mq.load(a.corpus)
    titles = {b: p["title"] for b, p in pubs.items()}
    verdicts = read_tsv(a.verdicts)
    queue = read_tsv(a.queue)
    qcols = list(queue[0].keys())
    qix = {(r["book"], r["entry"]): r for r in queue}
    audit = read_tsv(a.audit)
    aix = {(r["entry"], r["book"]) for r in audit}
    credits = read_tsv(a.credits) if a.credits.exists() else []
    cix = {(r["entry"], r["book"]) for r in credits}
    mq.PARENT_BOOKS.clear()
    mq.PARENT_BOOKS.update({e: set(d["source_ids"]) for e, d in entries.items()})
    in_print = {v["book"] for v in verdicts if v["evidence"] != UNVERIFIED}
    pending = 0
    for v in verdicts:
        key = (v["book"], v["entry"])
        if v["verdict"] not in ("keep", "cite", "remove", "expands"):
            raise SystemExit(f"refused: {v['entry']} in {v['book']}: unknown verdict {v['verdict']!r}")
        q = qix.get(key)
        d = header(a.corpus, v["entry"])
        if v["book"] not in d["source_ids"] and not (q and (q["verdict"] == v["verdict"] == "remove" or v["verdict"] == "expands")):
            raise SystemExit(f"refused: {v['book']} is not in the source_ids of {v['entry']}")
        row = next((s for s in d.get("sources", []) if s["publication"] == v["book"]), None)
        if q is None:  # the book has a `[[sources]]` row, so the warning never listed the pair
            q = {c: "" for c in qcols}
            q.update(mq.corpus_row(entries[v["entry"]], v["book"], title_to_pub))
            q.update(book=v["book"], entry=v["entry"], status="absent", cite="row" if row else "none",
                     hits="0", pdf="yes", slice="S12")
            q["ruling"] = ""
            qix[key] = q
            queue.append(q)
            pending += 1
        if q["verdict"] and q["verdict"] != v["verdict"] and q["verdict"] != v.get("replaces"):
            raise SystemExit(f"refused: {v['entry']} in {v['book']} has the verdict {q['verdict']} already")
        if not q["verdict"] or q["print_page"] != v["print_page"] or q["evidence"] != v["evidence"] or q["verdict"] != v["verdict"] \
                or (v.get("proposed_primary") and (q["proposed_primary"] != v["proposed_primary"] or q["gate"] != "primary")):
            pending += 1
            q.update(verdict=v["verdict"], print_page=v["print_page"], evidence=v["evidence"], slice="done")
            if v["verdict"] == "remove" and v.get("proposed_primary"):
                q["proposed_primary"] = v["proposed_primary"]
                q["proposed_status"] = v.get("proposed_status") or "printed"
                q["gate"] = "primary"
            elif v["verdict"] not in ("remove", "expands"):
                q["gate"] = q["proposed_primary"] = q["proposed_status"] = ""  # nothing to clear: the book stays
        if q["in_warning"] == "yes" and d["source_ids"][0] == v["book"]:
            q["member"] = "1"
            q["in_warning"] = ""
        if v["verdict"] == "remove" and row is not None and (v["entry"], v["book"]) not in aix:
            pending += 1
            cls = v.get("class") or "wrong-credit"
            cited = row.get("page", "")
            audit.append({"entry": v["entry"], "book": v["book"], "class": cls, "cited_page": cited,
                          "print_page": "none", "family": "", "related_cite": "", "edge": "",
                          "mention_pages": v.get("mention_pages", ""), "mention_kind": v.get("mention_kind", ""),
                          "read": v["read"], "evidence": v.get("audit_evidence") or (MENTION if cls == "mention" else WRONG),
                          "invalidated": f"{titles[v['book']]} p. {cited}" if cited else titles[v["book"]]})
        if v["verdict"] == "expands" and (v["entry"], v["book"]) not in cix \
                and not any(x["publication"] == v["book"] for x in d.get("expanded_in", [])):
            pending += 1
            credits.append({"entry": v["entry"], "book": v["book"], "action": "credit", "class": "expands-no-via",
                            "cited_page": v["print_page"], "print_page": v["print_page"], "read": v["read"],
                            "evidence": "the favored class options sit in a section of the book that no entry holds; the entry only gains an expanded_in credit without via"})
        if v["verdict"] == "keep" and row is not None and row.get("page") and row["page"] != v["print_page"] \
                and (v["entry"], v["book"]) not in cix:
            pending += 1
            credits.append({"entry": v["entry"], "book": v["book"], "action": "page", "cited_page": row["page"],
                            "print_page": v["print_page"], "read": v["read"], "evidence": "page corrected"})
    # The books read in print: every queue row of the book is `pdf = yes`, and its group follows.
    for r in queue:
        if r["book"] in in_print:
            d = entries[r["entry"]]
            body_line = mq.apply.body_citation("+++\n+++\n" + d["_body"], pubs[r["book"]]["title"])
            group = mq.group_of(d, body_line, True)
            if r["pdf"] != "yes" or r["group"] != group:
                pending += 1
                r["pdf"], r["group"] = "yes", group
                r["body_line"] = "yes" if body_line else ""
    if a.check:
        print(f"pending: {pending}")
        return 1 if pending else 0
    order = {t: i for i, t in enumerate(mq.screen.TAG_ORDER)}
    queue.sort(key=lambda r: (r["book"], order[r["tag"]], r["entry"]))
    write_tsv(a.queue, qcols, queue)
    write_tsv(a.audit, AUDIT_COLS, audit)
    if credits or a.credits.exists():
        write_tsv(a.credits, CREDIT_COLS, credits)
    print(f"recorded: {pending}; verdict rows: {len(verdicts)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
