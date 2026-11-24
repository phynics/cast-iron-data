#!/usr/bin/env python3
"""Find the spells that exist in both word orders (#296) and compare each pair.

A carried PSRD spell titled `Restoration, Greater` and a Pf Data spell titled
`Greater Restoration` are one spell. This script lists the pairs, compares
their fields and words, and keeps the review table
`scripts/word-order-spells-296.tsv`.

Run it from the corpus root:

    python3 scripts/word-order-spells-296.py --check   # the table is complete and true
    python3 scripts/word-order-spells-296.py --write   # regenerate the table
    python3 scripts/word-order-spells-296.py --show ID # print one pair side by side

Table columns:
  carried        the carried id (the inverted title, `Restoration, Greater`)
  survivor       the Pf Data id (`Greater Restoration`)
  books          printings of the survivor, `publication page`
  status         decision, kept by hand across `--write` runs:
                   alias   carried entry is retired by an alias to the survivor (pending)
                   merged  that was done: the carried file is gone and its alias row exists
                   hold    differs in a printed number or rule word; owner question
  differences    computed: what the carried entry has that the survivor does not, and the reverse
  print_check    kept by hand: what the printed book says and what was done

`--check` fails when a pair has no row or no decision, when a row names a pair
that no longer exists and is not `merged`, when a `merged` row has a carried
file, no alias row or no survivor, and when an `alias` row is not a pair.
A modifier title is `X, <Modifier>` for the modifiers in MODS; its twin is the
non-carried spell whose normalised title is `<Modifier> X`.
"""
import collections
import difflib
import os
import re
import sys
import tomllib

MODS = "Greater|Lesser|Mass|Communal|Improved|Masterful|Superior|Advanced|Major|Minor|Grand|True"
TSV = "scripts/word-order-spells-296.tsv"
HEADER = ["carried", "survivor", "books", "status", "differences", "print_check"]
STATUSES = ("alias", "merged", "hold")
FIELDS = ["school", "subschools", "descriptors", "casting_time", "components", "range",
          "effects", "duration", "saving_throw", "spell_resistance"]


def load():
    ents = {}
    for root, _, fs in os.walk("entries"):
        for f in fs:
            if f.endswith(".md"):
                p = os.path.join(root, f)
                fm, body = open(p, encoding="utf8").read()[4:].split("\n+++\n", 1)
                d = tomllib.loads(fm)
                ents[d["id"]] = (p, d, body)
    return ents


def norm(t):
    return re.sub(r"\W+", " ", t.lower()).strip()


def pairs(ents):
    by = collections.defaultdict(list)
    for i, (_, d, _) in ents.items():
        if d["kind"] == "spell" and not i.startswith("ref/carried/"):
            by[norm(d["title"])].append(i)
    out = []
    for i, (_, d, _) in sorted(ents.items()):
        if d["kind"] != "spell" or not i.startswith("ref/carried/"):
            continue
        m = re.match(r"(.*), (" + MODS + r")$", d["title"])
        if m:
            tw = by.get(norm(m.group(2) + " " + m.group(1)), [])
            if len(tw) == 1:
                out.append((i, tw[0]))
    return out


def books(d):
    rows = d.get("sources") or []
    if rows:
        return ", ".join(f'{r["publication"]} {r.get("page", "?")}' for r in rows)
    return ", ".join(d.get("source_ids", []))


def paragraphs(body):
    """(summary line or None, text) of an entry body: no statblock, headings, markup or links."""
    body = re.sub(r"::: statblock.*?\n:::\n", "", body, flags=re.S)
    paras = [p for p in body.strip().split("\n\n") if not p.startswith("#")]
    summary = None
    if paras and re.fullmatch(r"_[^_]*_", paras[0].strip().replace("\n", " ")):
        summary, paras = paras[0].strip("_ \n"), paras[1:]
    t = "\n\n".join(paras)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[_*>\\]", "", t)
    return summary, re.sub(r"\s+", " ", t).strip()


def levels(d):
    return {(x["class"], x["level"]) for x in d["fields"].get("levels", [])}


def fieldval(d, k):
    v = d["fields"].get(k)
    if k == "effects" and v:
        return [(x["label"].lower().rstrip("s"), norm(x["value"])) for x in v]
    if isinstance(v, list):
        return sorted(norm(x) for x in v)
    return norm(v) if isinstance(v, str) else v


def compare(ents, cid, sid):
    _, cd, cb = ents[cid]
    _, sd, sb = ents[sid]
    out = []
    csum, ctext = paragraphs(cb)
    _, stext = paragraphs(sb)
    if csum:
        out.append("carried has the spell-list line, which the spell page does not print")
    lc, ls = levels(cd), levels(sd)
    sclasses = {c for c, _ in ls}
    only = sorted((c, l) for c, l in lc if c not in sclasses)
    if only:
        out.append("levels only in carried: " + ", ".join(f"{c} {l}" for c, l in only))
    for c in sorted({c for c, _ in lc} & sclasses):
        a, b = sorted(l for x, l in lc if x == c), sorted(l for x, l in ls if x == c)
        if set(a) != set(b):
            out.append(f"level of {c}: carried {a} / survivor {b}")
    if ls - lc:
        out.append(f"survivor lists {len(ls - lc)} class levels the carried entry lacks")
    lacking = []
    for k in FIELDS:
        a, b = fieldval(cd, k), fieldval(sd, k)
        if a == b:
            continue
        if a is None:
            lacking.append(k)
        elif b is None or a != b:
            out.append(f"{k}: carried {cd['fields'].get(k)!r} / survivor {sd['fields'].get(k)!r}")
    if lacking:
        out.append("carried has no " + ", ".join(lacking))
    if re.sub(r"\W+", "", ctext.lower()) != re.sub(r"\W+", "", stext.lower()):
        wc, ws = re.findall(r"\w+", ctext.lower()), re.findall(r"\w+", stext.lower())
        ds = [f"[{' '.join(wc[a1:a2])}] / [{' '.join(ws[b1:b2])}]"
              for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, wc, ws, autojunk=False).get_opcodes()
              if op != "equal"]
        out.append("words carried / survivor: " + " | ".join(ds))
    return "; ".join(out) or "none"


def read_tsv():
    if not os.path.exists(TSV):
        return {}
    r = {}
    for line in open(TSV, encoding="utf8").read().splitlines()[1:]:
        c = (line.split("\t") + [""] * 6)[:6]
        r[c[0]] = c
    return r


def alias_rows():
    t = tomllib.loads(open("aliases.toml", encoding="utf8").read())
    return {e["old"]: e["target"] for e in t["entries"]}


def show(ents, cid):
    sid = dict(pairs(ents))[cid]
    for i in (cid, sid):
        _, d, b = ents[i]
        print("=" * 12, i, "|", books(d))
        print({k: d["fields"].get(k) for k in FIELDS}, sorted(levels(d)))
        print(paragraphs(b))
    print("DIFF:", compare(ents, cid, sid))


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    ents = load()
    if mode == "--show":
        return show(ents, sys.argv[2])
    old = read_tsv()
    found = pairs(ents)
    cur = {c: [c, s, books(ents[s][1]), "", compare(ents, c, s), ""] for c, s in found}
    if mode == "--write":
        for c, row in cur.items():
            if c in old:
                row[3], row[5] = old[c][3], old[c][5]
        for c, row in old.items():
            if c not in cur and row[3] == "merged":
                cur[c] = row
        with open(TSV, "w", encoding="utf8") as f:
            f.write("\t".join(HEADER) + "\n")
            for c in sorted(cur):
                f.write("\t".join(cur[c]) + "\n")
        print(f"{len(cur)} rows written")
        return
    bad = []
    aliases = alias_rows()
    for c, row in cur.items():
        if c not in old:
            bad.append(f"no row for pair: {c}")
        elif old[c][3] not in ("alias", "hold"):
            bad.append(f"pair without decision (alias/hold): {c}")
    for c, row in old.items():
        if row[3] not in STATUSES:
            bad.append(f"bad status {row[3]!r}: {c}")
        elif row[3] == "merged":
            if c in ents:
                bad.append(f"merged but the carried entry exists: {c}")
            if aliases.get(c) != row[1]:
                bad.append(f"merged but no alias row to the survivor: {c}")
            if row[1] not in ents:
                bad.append(f"merged but the survivor is missing: {row[1]}")
        elif c not in cur:
            bad.append(f"row names no pair: {c}")
    n = collections.Counter(r[3] for r in old.values())
    print(f"{len(old)} rows: " + ", ".join(f"{n[s]} {s}" for s in STATUSES) + f"; {len(found)} live pairs")
    print("\n".join(bad))
    sys.exit(1 if bad else 0)


main()
