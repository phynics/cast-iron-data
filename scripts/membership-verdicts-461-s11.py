#!/usr/bin/env python3
"""Record the reviewed S11 verdicts of phynics/cast-iron#461 in the queue and the helper files.

    python3 scripts/membership-verdicts-461-s11.py <corpus-dir>
        [--verdicts scripts/membership-verdicts-461-s11.tsv] [--check]

The verdict file has one row per (book, entry): `verdict` is `keep` (the book prints the entry;
the row's page is `print_page`), `page` (an entry outside the queue: only the page changes), `cite` (the same, and the entry has no page yet; a row with `replaces` set to the verdict a decided row has now takes the new verdict: owner ruling of 2026-11-24 on the Adventurer's Armory outfits), or `remove`
(the book does not print the entry). The script, for each row

  * writes `verdict`, `print_page`, `evidence` and slice `done` into the queue
    (`scripts/membership-queue-461.tsv`; a row that is decided already is left as it is),
  * for `remove` with a `[[sources]]` row: adds the audit row that releases the row
    (`scripts/membership-citation-audit-461.tsv`; class `wrong-credit`, or `mention`), and
  * for `keep` (or `page`, a row outside the queue) whose `[[sources]]` page differs from `print_page`: adds a `page` action to
    `scripts/expansion-credits-461-s11.tsv`, which `scripts/expansion-credits-apply.py` applies.

Apply the corpus changes afterwards with `expansion-credits-apply.py` (pages) and
`membership-apply.py` (removals, cites). Running again changes nothing. `--check` writes
nothing and exits 1 when a row is not recorded yet. Output has ids and book ids only; the
verdict file holds book titles and printed pages, never book text, file names or paths.
"""
from __future__ import annotations

import argparse
import csv
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent
QUEUE_COLS = None
AUDIT_COLS = ["entry", "book", "class", "cited_page", "print_page", "family", "related_cite", "edge",
              "mention_pages", "mention_kind", "read", "evidence", "invalidated"]
CREDIT_COLS = ["entry", "book", "action", "class", "cited_page", "print_page", "family", "related_cite",
               "edge", "mention_pages", "mention_kind", "read", "evidence", "invalidated", "via", "primary_to"]
WRONG = ("the book prints neither this entry nor a related entry on the cited page; "
         "the page row is a sibling's or the generic section's page copied over.")


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
    ap.add_argument("--verdicts", type=Path, default=HERE / "membership-verdicts-461-s11.tsv")
    ap.add_argument("--queue", type=Path, default=HERE / "membership-queue-461.tsv")
    ap.add_argument("--audit", type=Path, default=HERE / "membership-citation-audit-461.tsv")
    ap.add_argument("--credits", type=Path, default=HERE / "expansion-credits-461-s11.tsv")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    titles = {p["id"]: p["title"] for p in tomllib.loads((a.corpus / "publications.toml").read_text(encoding="utf-8"))["publication"]}
    verdicts = read_tsv(a.verdicts)
    queue = read_tsv(a.queue)
    qcols = list(queue[0].keys())
    qix = {(r["book"], r["entry"]): r for r in queue}
    audit = read_tsv(a.audit)
    aix = {(r["entry"], r["book"]) for r in audit}
    credits = read_tsv(a.credits) if a.credits.exists() else []
    cix = {(r["entry"], r["book"]) for r in credits}
    pending = 0
    for v in verdicts:
        key = (v["book"], v["entry"])
        q = qix.get(key)
        if v["verdict"] == "page":  # a row outside the queue: only its page changes
            row = next((s for s in header(a.corpus, v["entry"]).get("sources", []) if s["publication"] == v["book"]), None)
            if row is None:
                raise SystemExit(f"refused: {v['entry']} has no [[sources]] row for {v['book']}")
            if row.get("page") != v["print_page"] and key[::-1] not in cix:
                pending += 1
                credits.append({"entry": v["entry"], "book": v["book"], "action": "page", "cited_page": row.get("page", ""),
                                "print_page": v["print_page"], "read": v["read"], "evidence": "page corrected"})
            continue
        if q is None:
            raise SystemExit(f"refused: {v['entry']} in {v['book']} is not in the queue")
        if v["verdict"] not in ("keep", "cite", "remove", "page"):
            raise SystemExit(f"refused: {v['entry']} in {v['book']}: unknown verdict {v['verdict']!r}")
        d = header(a.corpus, v["entry"])
        row = next((s for s in d.get("sources", []) if s["publication"] == v["book"]), None)
        if q["verdict"] and q["verdict"] != v["verdict"] and q["verdict"] != v.get("replaces"):
            raise SystemExit(f"refused: {v['entry']} in {v['book']} has the verdict {q['verdict']} already")
        if not q["verdict"] or q["print_page"] != v["print_page"] or q["evidence"] != v["evidence"] \
                or (v.get("group") and q["group"] != v["group"]) or (v.get("proposed_primary") and (q["proposed_primary"] != v["proposed_primary"] or q["gate"] != "primary")):
            pending += 1
            q.update(verdict=v["verdict"], print_page=v["print_page"], evidence=v["evidence"], slice="done")
            if v.get("group"):
                q["group"] = v["group"]  # the entry's group changed with the edit that made the removal possible
            if v.get("proposed_status"):
                q["proposed_status"] = v["proposed_status"]
            if v.get("proposed_primary"):
                q["proposed_primary"] = v["proposed_primary"]
                q["gate"] = "primary"
        if q["in_warning"] == "yes" and d["source_ids"][0] == v["book"]:
            q["member"] = "1"
            q["in_warning"] = ""  # a book that became the first book (a removal of S11) leaves the warning
        if v["verdict"] == "remove" and row is not None and (v["entry"], v["book"]) not in aix:
            pending += 1
            cls = v.get("class") or "wrong-credit"
            cited = row.get("page", "")
            audit.append({"entry": v["entry"], "book": v["book"], "class": cls, "cited_page": cited,
                          "print_page": "none", "family": "", "related_cite": "", "edge": "",
                          "mention_pages": v.get("mention_pages", ""), "mention_kind": v.get("mention_kind", ""),
                          "read": v["read"], "evidence": v.get("audit_evidence") or WRONG,
                          "invalidated": f"{titles[v['book']]} p. {cited}" if cited else titles[v["book"]]})
        if v["verdict"] == "keep" and row is not None and row.get("page") and row["page"] != v["print_page"] \
                and (v["entry"], v["book"]) not in cix:
            pending += 1
            credits.append({"entry": v["entry"], "book": v["book"], "action": "page", "cited_page": row["page"],
                            "print_page": v["print_page"], "read": v["read"], "evidence": "page corrected"})
    if a.check:
        print(f"pending: {pending}")
        return 1 if pending else 0
    write_tsv(a.queue, qcols, queue)
    write_tsv(a.audit, AUDIT_COLS, audit)
    write_tsv(a.credits, CREDIT_COLS, credits)
    print(f"recorded: {pending}; verdict rows: {len(verdicts)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
