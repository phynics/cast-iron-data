#!/usr/bin/env python3
"""The review queue of the trades migration (phynics/cast-iron#452).

`trade-review-452-baseline.tsv` is the migration's own queue, preserved: one row per trade that
`cast-iron-corpus migrate-trades` could not resolve, plus one row per `**Replaces:**` or `**Alters:**`
line that no trade can hold (`trade` 0; `subsection` names the variant section that prints it).
`trade-review-452.tsv` holds the same rows with a decision for each. This script turns the decisions
of `trade-review-452-decisions.tsv` into the rows and into the entries:

  baseline FILE   write the baseline from a migration queue FILE (one time; computes `subsection`)
  fill            build the queue from the baseline, copy each decision onto the rows it covers (first
                  matching decision wins) and fill the citation of every row
  apply           write the `feature`, `class`, `levels` and `power` of every closed row into its entry
  split           split each composite trade that `trade-splits-452.tsv` lists into its parts: entry, baseline,
                  queue and adjustment logs move together (see Splits below)
  normalize       write step values as grant levels (see Steps below) and log each change
  check           fail unless the queue equals the baseline, every row is closed and cited, and the
                  entries agree with the rows and with the adjustment log
  stats           count the rows per disposition and reason

Run it from the root of the corpus: `python3 -I scripts/trade-review-452.py <command>`. Every command is
idempotent. `apply` and `normalize` rewrite only the trades that they name (queue rows and the adjustment
log); a trade that the migration resolved stays as written unless the log says otherwise.

Dispositions of a row:

  open       not decided yet; `check` fails while any row is open
  resolved   print settles the feature: `feature` (and `class`, `levels`, `power`) go into the trade
  exception  the trade stays unresolved on purpose; `decision` names the documented reason (codebook:
             `trade-review-452.md`)

The decisions file has one decision per line: `scope` (an entry id, `class <ref/class/x>`,
`reason <reason>`, `prefix <id prefix>`, or `kind <kind>`), `printed` (the printed name in lower case, `*`
for any, or `~regex` that must match the whole name), then `disposition`, `code`, `feature`, `class`,
`levels`, `power`, `note`. In a `~regex` decision, `\\1` in `feature`, `levels`, `power` and `note` is a group
of the regex. `levels` may be a comma separated list, `ordinals` (the ordinals of the printed name),
`steps:<feature>` (the step numbers of the printed name) or `grant:<label>` (the level at which the class
table of the base class grants `<label>`); `power` may be `=printed`.

Evidence. The `print` column is a search hit from `trade-review-452-print.py`, not a reading. `evidence` says
what settles a closed row: `print` (the search found the name on the cited page or next to it), `manual` (a
reader checked the book page: `trade-evidence-452.tsv` records the printed page, and `fill` copies it) or
`corpus` (no hit and no reading: the entry's own text and the class table settle it, and `evidence_note`
says why print did not).

Splits. A printed item that names several features at once (`Mutagen, 2nd-level discovery`) is a composite:
a trade holds one feature. `trade-splits-452.tsv` lists, for each composite that print lets us split, its parts
in print order: the printed text of each part, and its `feature`, `class`, `levels` and `power`. The parts,
joined with `, `, must read as the composite (the drift check joins the printed names of the trades with
commas, so a split never changes what the entry prints). `split` replaces the trade by its parts in the entry,
replaces the row in the baseline and the queue by one row for each part (reason `split-part`), and renumbers
the later trades of the entry in the queue, the baseline and the two adjustment logs. This is the one
command that edits the baseline; the rows of the parts are the only rows that it adds. It decides what to do
from the entry alone: a trade that is no longer in the entry is a split that is done, so a second run changes
no byte. A split that the entry holds but a file does not (an interrupted run) is not repaired: `git checkout`
the corpus and run it again. A composite that print shows to be one feature is resolved by an ordinary
decision, and one that a split would make print differently (`and` with no comma between the features) is an
exception with the code `split-blocked`.

Steps. A progression step (`Armor training 2`, `Trap sense +3`, `Judgment 1/day`, `Spirit power (lesser)`)
is identified by the BASE-CLASS GRANT LEVELS in `levels`, read from the class table of the base class;
`power` names a stable component (a bardic performance, a deed, a school power) only when the level alone
is not enough. A step is never a `power`.
"""
import csv
import json
import re
import sys
import tomllib
from collections import Counter
from pathlib import Path

ROOT = Path(".")
QUEUE = ROOT / "scripts/trade-review-452.tsv"
BASELINE = ROOT / "scripts/trade-review-452-baseline.tsv"
DECISIONS = ROOT / "scripts/trade-review-452-decisions.tsv"
ADJUSTMENTS = ROOT / "scripts/trade-adjustments-452.tsv"
MANUAL = ROOT / "scripts/trade-adjustments-manual-452.tsv"
EVIDENCE = ROOT / "scripts/trade-evidence-452.tsv"
SPLITS = ROOT / "scripts/trade-splits-452.tsv"
SPLIT_COLUMNS = ["id", "op", "composite", "part", "feature", "class", "levels", "power", "note"]
BASE_COLUMNS = ["id", "kind", "trade", "op", "printed", "reason", "candidates", "unclaimed_old_anchors", "subsection"]
COLUMNS = BASE_COLUMNS + [
    "disposition", "decision", "feature", "class", "levels", "power", "book", "page", "page_reason", "print",
    "class_hit", "class_book", "class_page", "evidence", "evidence_note",
]
ADJUST_COLUMNS = ["id", "trade", "op", "printed", "before", "after", "rule"]


def read_tsv(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE))


def write_tsv(path, columns, rows):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, columns, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar="\\"
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def write_queue(rows):
    write_tsv(QUEUE, COLUMNS, rows)


def entry_path(entry_id):
    return ROOT / "entries" / (entry_id.removeprefix("ref/") + ".md")


def split_entry(text):
    head, front, body = text.split("+++\n", 2)
    return front, body


_publications = None


def publications():
    global _publications
    if _publications is None:
        data = tomllib.loads((ROOT / "publications.toml").read_text(encoding="utf-8"))
        _publications = {row["id"]: row.get("title", row["id"]) for row in data["publication"]}
    return _publications


def publication_title(publication):
    return publications().get(publication, publication)


def title_key(title):
    return re.sub(r"[^a-z0-9]+", "", title.lower().replace("’", "").replace("'", ""))


def publication_by_title(title):
    key = title_key(title)
    for pid, t in publications().items():
        if title_key(t) == key:
            return pid
    return None


def entry_info(entry_id):
    front, _ = split_entry(entry_path(entry_id).read_text(encoding="utf-8"))
    data = tomllib.loads(front)
    relations = [r["target"] for r in data.get("relations", []) if r["kind"] == "archetype"]
    return data, relations


def toml_string(literal):
    return tomllib.loads("x = " + literal)["x"]


# --- variant sections -------------------------------------------------------------------------

MARKUP = re.compile(r"\[([^\]]*)\]\([^)]*\)|[*_`\\]")


def plain(text):
    return " ".join(MARKUP.sub(lambda m: m.group(1) or "", text).split())


def sources_of(text):
    """`Advanced Player's Guide pg 88, Divine Anthology pg 24` as [(title, page)]."""
    found = re.findall(r"(?:^|,\s*)(.+?)\s+pg\s+(\d+)", plain(text))
    if found:
        return found
    # A source line without a page (`**Sources:** Haunted Heroes Handbook`) names the book only.
    return [(t.strip(), "") for t in plain(text).split(", ") if t.strip()]


def variant_occurrences(entry_id):
    """The `**Replaces:**` and `**Alters:**` items that sit below the normal part of an entry, in body
    order, each with the subsection that owns it. The normal part ends at the first `###` heading that
    the entry's `**Sources:**` line follows (the rule of the drift check); the owner of a later line is
    the nearest such heading before it."""
    _, body = split_entry(entry_path(entry_id).read_text(encoding="utf-8"))
    lines = body.split("\n")

    def next_line(i):
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        return lines[j] if j < len(lines) else ""

    out = []
    owner = None
    for i, line in enumerate(lines):
        if line.startswith("### ") and next_line(i).startswith("**Sources:**"):
            j = i + 1
            while not lines[j].startswith("**Sources:**"):
                j += 1
            owner = (plain(line[4:]), sources_of(lines[j][len("**Sources:**"):]))
            continue
        m = re.match(r"\*\*(Replaces|Alters):\*\*\s*(.*)$", line)
        if m and owner:
            text = m.group(2)
            k = i + 1
            while k < len(lines) and lines[k].strip() and not lines[k].startswith("**"):
                text += " " + lines[k]
                k += 1
            for item in text.split(","):
                item = plain(item).rstrip(".;").strip()
                if item:
                    out.append({"op": m.group(1).lower(), "printed": item, "subsection": owner[0], "sources": owner[1]})
    return out


def variant_for(row, cache={}):
    """The occurrence that a variant-only row stands for (rows and occurrences pair up in order)."""
    key = row["id"]
    if key not in cache:
        cache[key] = {"occ": variant_occurrences(key), "used": set()}
    entry = cache[key]
    for i, occ in enumerate(entry["occ"]):
        if i in entry["used"] or occ["op"] != row["op"] or occ["printed"].lower() != plain(row["printed"]).lower():
            continue
        if row.get("subsection") and occ["subsection"] != row["subsection"]:
            continue
        entry["used"].add(i)
        return occ
    return None


# --- decisions ---------------------------------------------------------------------------------

def match_printed(pattern, printed):
    """The match object (or True) when the pattern covers the printed name, else None."""
    printed = " ".join(printed.lower().split())
    if pattern == "*":
        return True
    if pattern.startswith("~"):
        return re.fullmatch(pattern[1:], printed, re.I)
    return True if " ".join(pattern.lower().split()) == printed else None


ORDINAL = re.compile(r"\b(\d{1,2})(?:st|nd|rd|th)\b|\bfirst\b", re.I)


def ordinals(printed):
    """The levels that the ordinals of a printed name state (`2nd-, 8th-, and 16th-level` is 2, 8, 16)."""
    found = {1 if m.group(0).lower() == "first" else int(m.group(1)) for m in ORDINAL.finditer(printed)}
    if not found or any(not 1 <= n <= 20 for n in found):
        raise SystemExit(f"no usable ordinal level in {printed!r}")
    return ",".join(str(n) for n in sorted(found))


_anchors = {}


def class_anchors(class_id):
    """The heading anchors of a class entry: the features a trade may name."""
    if class_id not in _anchors:
        text = entry_path(class_id).read_text(encoding="utf-8")
        _anchors[class_id] = set(re.findall(r"^#{3,6} .*? \{#([^}]+)\}$", text, re.M))
    return _anchors[class_id]


def decision_for(row, decisions, info):
    data, relations = info
    for d in decisions:
        scope = d["scope"]
        if scope.startswith("class "):
            if scope[6:] not in relations:
                continue
        elif scope.startswith("reason "):
            if scope[7:] != row["reason"]:
                continue
        elif scope.startswith("prefix "):
            if not row["id"].startswith(scope[7:]):
                continue
        elif scope.startswith("kind "):
            if scope[5:] != row["kind"]:
                continue
        elif scope != row["id"]:
            continue
        m = match_printed(d["printed"], row["printed"])
        if m and d["disposition"] == "resolved" and relations and d["feature"]:
            # A decision names a feature that every base class of the entry must hold; a generic
            # decision that one class cannot take leaves the row for a later, more specific one.
            if not all(d["feature"] in class_anchors(c) for c in relations):
                continue
        if m:
            if m is True:
                return d
            return {
                k: (m.expand(v) if k in ("feature", "levels", "power", "note") and "\\" in v else v)
                for k, v in d.items()
            }
    return None


# --- grant levels --------------------------------------------------------------------------------

_tables = {}


def class_table(class_id):
    """{label: [levels]} from the class feature table of a class entry: `|3rd|...|Armor training 1|`."""
    if class_id not in _tables:
        table = {}
        text = entry_path(class_id).read_text(encoding="utf-8")
        for line in text.split("\n"):
            m = re.match(r"\|(\d+)(?:st|nd|rd|th)\|(.*)\|$", line)
            if not m:
                continue
            cells = m.group(2).split("|")
            special = next((c for c in cells if re.search(r"[A-Za-z]{3}", c) and not re.fullmatch(r"[+\-/\d ]+", c)), "")
            for token in plain(special).split(", "):
                table.setdefault(token.strip().lower(), []).append(int(m.group(1)))
        _tables[class_id] = table
    return _tables[class_id]


def grant_levels(class_id, label):
    levels = class_table(class_id).get(plain(label).lower())
    if not levels:
        raise SystemExit(f"{class_id}: no class table row grants {label!r}")
    return ",".join(str(n) for n in sorted(set(levels)))


# `steps:<feature>`: the step numbers of a printed name -> the label that the class table uses.
STEP_LABELS = {
    "armor-training": "armor training {n}",
    "weapon-training": "weapon training {n}",
    "gun-training": "gun training {n}",
    "outside-contact": "outside contact {n}",
    "trap-sense": "trap sense +{n}",
    "poison-resistance": "poison resistance +{n}",
}


def step_levels(feature, class_id, printed):
    text = re.sub(
        r"(\d+)\s*(?:-|through)\s*(\d+)",
        lambda m: ", ".join(str(n) for n in range(int(m.group(1)), int(m.group(2)) + 1)),
        printed.lower(),
    )
    text = re.sub(r"^\D*?(?=[+\d])", "", text, count=1)
    levels = set()
    for n in sorted({int(x) for x in re.findall(r"\d+", text)}):
        levels.update(int(x) for x in grant_levels(class_id, STEP_LABELS[feature].format(n=n)).split(","))
    return ",".join(str(n) for n in sorted(levels))


# Step values that the migration wrote as `power`: (class, feature) -> label of the power in the class table.
STEP_POWERS = {
    ("alchemist", "poison-resistance"): lambda p: f"poison resistance {p}" if re.fullmatch(r"\+\d", p) else None,
    ("investigator", "poison-resistance"): lambda p: f"poison resistance {p}" if re.fullmatch(r"\+\d", p) else None,
    ("barbarian", "trap-sense"): lambda p: f"trap sense {p}" if re.fullmatch(r"\+\d", p) else None,
    ("rogue", "trap-sense"): lambda p: f"trap sense {p}" if re.fullmatch(r"\+\d", p) else None,
    ("fighter", "armor-training"): lambda p: f"armor training {p}" if p.isdigit() else None,
    ("fighter", "weapon-training"): lambda p: f"weapon training {p}" if p.isdigit() else None,
    ("fighter", "bravery"): lambda p: f"bravery +{p}" if p.isdigit() else None,
    ("gunslinger", "gun-training"): lambda p: f"gun training {p}" if p.isdigit() else None,
    ("gunslinger", "nimble"): lambda p: f"nimble {p}" if re.fullmatch(r"\+\d", p) else None,
    ("inquisitor", "judgment"): lambda p: f"judgment {p}" if re.fullmatch(r"\d/day", p) else None,
    ("mesmerist", "touch-treatment"): lambda p: (
        "touch treatment (greater)" if p == "major" else f"touch treatment ({p})"
        if p in ("minor", "moderate", "greater", "break enchantment") else None
    ),
    ("warpriest", "blessings"): lambda p: "blessings (major)" if p == "major" else None,
}


# --- claims ------------------------------------------------------------------------------------

def claim_of(trade):
    """What a trade claims: (op, feature, class, power, levels) with levels None for every level."""
    op = "replaces" if "replaces" in trade else "alters"
    levels = frozenset(trade["levels"]) if trade.get("levels") else None
    return op, trade["feature"], trade.get("class"), trade.get("power"), levels


def overlap(a, b):
    """The one-claim rule of corpus-check: the same key, feature, class and power at a shared level."""
    if a[:4] != b[:4]:
        return False
    return a[4] is None or b[4] is None or bool(a[4] & b[4])


def row_key(row, counter):
    key = (row["id"], row["trade"], row["op"], row["printed"], row.get("subsection", ""))
    counter[key] += 1
    return key + (counter[key],)


def citation(row, data):
    """book, page and page_reason of a row: the owning subsection for a variant row, else the entry."""
    if row["reason"] == "variant-only":
        occ = variant_for(row)
        if occ is None:
            return "", "", "the line was not found in the entry's variant sections"
        if not occ["sources"]:
            return "", "", "the owning subsection names no source"
        titles = [t for t, _ in occ["sources"]]
        pages = [p for _, p in occ["sources"] if p]
        why = "" if pages else "the owning subsection's source line names the book without a page"
        return "; ".join(titles), "; ".join(pages), why
    sources = data.get("sources") or []
    if sources:
        s = sources[0]
        page = str(s.get("page", ""))
        return publication_title(s["publication"]), page, "" if page else "the entry's source gives no page"
    ids = data.get("source_ids") or []
    return (publication_title(ids[0]) if ids else ""), "", "the entry cites no page"


def cmd_baseline(args):
    rows = read_tsv(args[0])
    out = []
    counter = Counter()
    for row in rows:
        row = {k: row.get(k, "") for k in BASE_COLUMNS}
        row["subsection"] = ""
        if row["reason"] == "variant-only":
            occ = variant_for(row)
            if occ is None:
                raise SystemExit(f"{row['id']}: no variant line for {row['printed']!r}")
            row["subsection"] = occ["subsection"]
        out.append(row)
    write_tsv(BASELINE, BASE_COLUMNS, out)
    print(f"baseline: {len(out)} rows")


def cmd_fill(args):
    baseline = read_tsv(BASELINE)
    existing = {}
    if QUEUE.exists():
        counter = Counter()
        for r in read_tsv(QUEUE):
            existing[row_key(r, counter)] = r
    decisions = read_tsv(DECISIONS)
    cache = {}
    rows = []
    counter = Counter()
    for b in baseline:
        key = row_key(b, counter)
        row = {c: "" for c in COLUMNS}
        row.update(existing.get(key, {}))
        row.update({c: b.get(c, "") for c in BASE_COLUMNS})
        if not row["disposition"]:
            row["disposition"] = "open"
        rows.append(row)
    changed = 0
    for row in rows:
        info = cache.setdefault(row["id"], entry_info(row["id"]))
        data, relations = info
        book, page, why = citation(row, data)
        if row["reason"] != "variant-only" and row["print"] in ("page", "words") and row["book"]:
            book, page, why = row["book"], row["page"], ""
        row["_cite"] = (book, page, why)
        if row["reason"] == "split-part":
            part = split_part(row)
            if part is None:
                raise SystemExit(f"{row['id']}: no splits-file row for the part {row['printed']!r}")
            d = {"disposition": "resolved", "code": "split-part", "feature": part["feature"], "class": part["class"],
                 "levels": part["levels"], "power": part["power"], "note": part["note"]}
        else:
            d = decision_for(row, decisions, info)
        if d is None:
            continue
        levels = d["levels"]
        class_id = relations[0] if relations else ""
        if levels == "ordinals":
            levels = ordinals(row["printed"])
        elif levels.startswith("steps:"):
            levels = step_levels(levels[6:], class_id, row["printed"])
        elif levels.startswith("grant:"):
            levels = grant_levels(class_id, levels[6:])
        power = row["printed"] if d["power"] == "=printed" else d["power"]
        row["_new"] = dict(
            disposition=d["disposition"], decision=d["code"] + (": " + d["note"] if d["note"] else ""),
            feature=d["feature"], **{"class": d["class"]}, levels=levels, power=power,
        )
    # One trade of a key claims a feature at a level and power; a later trade that would claim the same
    # stays unresolved (the rule that migrate-trades follows too).
    by_entry = {}
    for row in rows:
        by_entry.setdefault(row["id"], []).append(row)
    adjusted = adjusted_trades()
    for entry_id, entry_rows in by_entry.items():
        queued = {int(r["trade"]) for r in entry_rows if r["trade"] != "0"}
        trades = [dict(t) for t in cache[entry_id][0].get("fields", {}).get("trades", [])]
        for i, t in enumerate(trades, 1):
            after = adjusted.get((entry_id, i))
            if after is not None:
                t.update(after)
        claimed = [(i, claim_of(t)) for i, t in enumerate(trades, 1) if "feature" in t and i not in queued]
        for row in sorted(entry_rows, key=lambda r: int(r["trade"])):
            new = row.get("_new")
            if not new or new["disposition"] != "resolved":
                continue
            claim = (
                row["op"], new["feature"], new["class"] or None, new["power"] or None,
                frozenset(int(x) for x in new["levels"].split(",")) if new["levels"] else None,
            )
            clash = next((i for i, c in claimed if overlap(claim, c)), None)
            if clash is not None:
                new.update(
                    disposition="exception", feature="", levels="", power="", **{"class": ""},
                    decision=f"overlaps-earlier-claim: trade {clash} of the same key already names feature {claim[1]} at a shared level and power, and the one-claim rule lets one trade name it (the decision for this item was: {new['decision']})",
                )
            else:
                claimed.append((int(row["trade"]), claim))
    manual = {}
    if EVIDENCE.exists():
        for e in read_tsv(EVIDENCE):
            manual[(e["id"], e["printed"].lower(), e.get("subsection", ""))] = e
    for row in rows:
        new = row.pop("_new", None)
        book, page, why = row.pop("_cite")
        e = manual.get((row["id"], row["printed"].lower(), row["subsection"])) or manual.get(
            (row["id"], row["printed"].lower(), "")
        )
        if e:
            book, page, why = e["book"], e["page"], ""
            row["evidence"], row["evidence_note"] = "manual", e["note"]
        elif row["print"] in ("page", "words"):
            row["evidence"], row["evidence_note"] = "print", ""
        elif row["print"]:
            row["evidence"] = "corpus"
            row["evidence_note"] = (
                "no copy of the book; settled from the entry's own line and the class table"
                if row["print"] == "nobook" else
                "the book is available, but the search found no hit and nobody read the page; settled from the entry's own line and the class table"
            )
        if new:
            new = dict(new, book=book, page=page, page_reason=why)
            if any(row.get(k, "") != v for k, v in new.items()):
                row.update(new)
                changed += 1
    write_queue(rows)
    print(f"fill: {changed} rows changed, {sum(1 for r in rows if r['disposition'] == 'open')} open")


def encode_keys(keys):
    """`feature=x | levels=3,7 | power=+2`: the feature keys of a trade, for the adjustment log."""
    return " | ".join(
        f"{k}={','.join(str(n) for n in keys[k]) if k == 'levels' else keys[k]}"
        for k in ("feature", "class", "levels", "power") if keys.get(k)
    )


def decode_keys(text):
    keys = dict(part.split("=", 1) for part in text.split(" | ") if part)
    if "levels" in keys:
        keys["levels"] = [int(n) for n in keys["levels"].split(",")]
    return keys


def adjusted_trades():
    """{(id, trade): {feature keys}} that the adjustment log says an entry holds."""
    out = {}
    if ADJUSTMENTS.exists():
        for r in read_tsv(ADJUSTMENTS):
            out[(r["id"], int(r["trade"]))] = decode_keys(r["after"])
    return out


TRADE_RE = re.compile(r"^  \{ (replaces|alters) = (\"(?:[^\"\\]|\\.)*\")(.*) \},?$")


def trade_lines(front):
    lines = front.split("\n")
    start = next(i for i, l in enumerate(lines) if l == "trades = [")
    end = next(i for i in range(start + 1, len(lines)) if lines[i] == "]")
    return lines, start + 1, end


def render(line, keys):
    """The trade line with its feature keys replaced by `keys` (feature, class, levels, power)."""
    m = TRADE_RE.match(line)
    op, printed = m.group(1), m.group(2)
    parts = [f"{op} = {printed}"]
    if keys.get("feature"):
        parts.append(f'feature = "{keys["feature"]}"')
        if keys.get("class"):
            parts.append(f'class = "{keys["class"]}"')
        if keys.get("levels"):
            parts.append("levels = [" + ", ".join(str(n) for n in keys["levels"]) + "]")
        if keys.get("power"):
            parts.append('power = "' + keys["power"].replace("\\", "\\\\").replace('"', '\\"') + '"')
    return "  { " + ", ".join(parts) + " },"


def keys_of_row(row):
    if row["disposition"] != "resolved":
        return {}
    return {
        "feature": row["feature"], "class": row["class"], "power": row["power"],
        "levels": [int(x) for x in row["levels"].split(",")] if row["levels"] else [],
    }


def rewrite_entry(entry_id, edits):
    """edits: {trade index: (op, printed, keys)}; each must match the parsed line. Returns True if written."""
    path = entry_path(entry_id)
    text = path.read_text(encoding="utf-8")
    head, front, body = text.split("+++\n", 2)
    lines, first, end = trade_lines(front)
    touched = False
    for index, (op, printed, keys) in edits.items():
        line = lines[first + index - 1]
        m = TRADE_RE.match(line)
        if not m or m.group(1) != op or toml_string(m.group(2)) != printed:
            raise SystemExit(f"{entry_id}: trade {index} is not `{op} = {printed!r}`: {line!r}")
        want = render(line, keys)
        if line != want:
            lines[first + index - 1] = want
            touched = True
    if touched:
        path.write_text(head + "+++\n" + "\n".join(lines) + "+++\n" + body, encoding="utf-8")
    return touched


def cmd_apply(args):
    by_entry = {}
    for r in read_tsv(QUEUE):
        if r["disposition"] in ("resolved", "exception") and r["trade"] != "0":
            by_entry.setdefault(r["id"], {})[int(r["trade"])] = (r["op"], r["printed"], keys_of_row(r))
    written = sum(rewrite_entry(entry_id, edits) for entry_id, edits in by_entry.items())
    print(f"apply: {written} entries written")


def split_groups():
    """{(id, op, composite): [part rows in print order]} from the splits file."""
    groups = {}
    if SPLITS.exists():
        for r in read_tsv(SPLITS):
            groups.setdefault((r["id"], r["op"], r["composite"]), []).append(r)
    for (entry_id, op, composite), parts in groups.items():
        if len(parts) < 2 or ", ".join(p["part"] for p in parts) != composite:
            raise SystemExit(f"{entry_id}: the parts of {composite!r} do not join with ', ' to the composite")
    return groups


def split_part(row):
    """The splits-file row that a `split-part` queue row stands for, or None."""
    for (entry_id, op, _), parts in split_groups().items():
        if entry_id == row["id"] and op == row["op"]:
            for part in parts:
                if part["part"] == row["printed"]:
                    return part
    return None


def part_keys(part):
    return {
        "feature": part["feature"], "class": part["class"], "power": part["power"],
        "levels": [int(x) for x in part["levels"].split(",")] if part["levels"] else [],
    }


def trade_line(op, printed, keys):
    return render("  { %s = %s }," % (op, json.dumps(printed, ensure_ascii=False)), keys)


def split_trades_of_entry(entry_id, groups):
    """Replace the composite trades of one entry by their parts. `groups` is [(op, composite, parts)].
    Returns [(position, composite, parts)] for the splits that this call made, in the order made (a position
    counts the trades of the entry as they stand after the earlier splits); writes nothing."""
    path = entry_path(entry_id)
    head, front, body = path.read_text(encoding="utf-8").split("+++\n", 2)
    lines, first, end = trade_lines(front)
    done = []
    for op, composite, parts in groups:
        found = None
        for j in range(first, end):
            m = TRADE_RE.match(lines[j])
            if m and m.group(1) == op and toml_string(m.group(2)) == composite:
                found = j
                break
        if found is None:
            continue
        new = [trade_line(op, part["part"], part_keys(part)) for part in parts]
        lines[found:found + 1] = new
        end += len(new) - 1
        done.append((found - first + 1, composite, parts))
    return done, (path, head, lines, body)


def cmd_split(args):
    groups = split_groups()
    by_entry = {}
    for (entry_id, op, composite), parts in groups.items():
        by_entry.setdefault(entry_id, []).append((op, composite, parts))
    have_queue = QUEUE.exists()  # `fill` builds the queue from the baseline when there is none
    baseline, queue = read_tsv(BASELINE), read_tsv(QUEUE) if have_queue else []
    logs = {path: read_tsv(path) for path in (ADJUSTMENTS, MANUAL) if path.exists()}
    entries = split_count = 0
    for entry_id in sorted(by_entry):
        done, (path, head, lines, body) = split_trades_of_entry(entry_id, by_entry[entry_id])
        if not done:
            continue
        for position, composite, parts in done:
            k = len(parts)
            for name, rows in (("baseline", baseline), ("queue", queue)):
                if name == "queue" and not have_queue:
                    continue
                at = [i for i, r in enumerate(rows) if r["id"] == entry_id and r["op"] == parts[0]["op"]
                      and r["printed"] == composite and int(r["trade"]) == position]
                if len(at) != 1:
                    raise SystemExit(f"{entry_id}: the {name} has no row for trade {position} ({composite!r})")
                parent = rows[at[0]]
                for r in rows:
                    if r["id"] == entry_id and int(r["trade"]) > position:
                        r["trade"] = str(int(r["trade"]) + k - 1)
                new_rows = []
                for n, part in enumerate(parts):
                    row = dict(parent, trade=str(position + n), printed=part["part"], reason="split-part",
                               candidates="", unclaimed_old_anchors="")
                    if name == "queue":
                        for column in ("disposition", "decision", "feature", "class", "levels", "power",
                                       "evidence", "evidence_note", "class_hit", "class_book", "class_page"):
                            row[column] = ""
                        row["disposition"] = "open"
                    new_rows.append(row)
                rows[at[0]:at[0] + 1] = new_rows
            for path_of_log, rows in logs.items():
                for r in rows:
                    if r["id"] == entry_id and int(r["trade"]) == position:
                        raise SystemExit(f"{entry_id} trade {position}: the composite has an adjustment-log row")
                    if r["id"] == entry_id and int(r["trade"]) > position:
                        r["trade"] = str(int(r["trade"]) + k - 1)
            split_count += 1
        path.write_text(head + "+++\n" + "\n".join(lines) + "+++\n" + body, encoding="utf-8")
        entries += 1
    if entries:
        write_tsv(BASELINE, BASE_COLUMNS, baseline)
        if have_queue:
            write_queue(queue)
        for path_of_log, rows in logs.items():
            write_tsv(path_of_log, ADJUST_COLUMNS if path_of_log == ADJUSTMENTS else list(rows[0]), rows)
    print(f"split: {split_count} trades split in {entries} entries")


def cmd_normalize(args):
    """Rewrite the step values that the migration wrote as `power` into grant levels, and log them."""
    queued = {(r["id"], int(r["trade"])) for r in read_tsv(QUEUE) if r["trade"] != "0"}
    log = {}
    if ADJUSTMENTS.exists():
        log = {(r["id"], int(r["trade"])): r for r in read_tsv(ADJUSTMENTS)}
    edits_by_entry = {}
    # The log is authoritative: an entry that was reset (a merge) gets the logged trades again.
    for (entry_id, index), r in log.items():
        edits_by_entry.setdefault(entry_id, {})[index] = (r["op"], r["printed"], decode_keys(r["after"]))
    for path in sorted((ROOT / "entries").glob("arc-*/*.md")):
        text = path.read_text(encoding="utf-8")
        if "\ntrades = [" not in text:
            continue
        data = tomllib.loads(split_entry(text)[0])
        relations = [r["target"] for r in data.get("relations", []) if r["kind"] == "archetype"]
        if len(relations) != 1:
            continue
        slug = relations[0].removeprefix("ref/class/")
        for i, t in enumerate(data["fields"]["trades"], 1):
            if "power" not in t or (data["id"], i) in queued or (data["id"], i) in log:
                continue
            label_of = STEP_POWERS.get((slug, t.get("feature")))
            label = label_of(t["power"]) if label_of else None
            if label is None:
                continue
            levels = [int(x) for x in grant_levels(relations[0], label).split(",")]
            op = "replaces" if "replaces" in t else "alters"
            before = {k: t[k] for k in ("feature", "class", "levels", "power") if k in t}
            if "levels" in before:
                continue  # a trade that already has levels and a power is judged by hand
            after = {k: v for k, v in before.items() if k != "power"}
            after["levels"] = levels
            rule = f"step value {t['power']!r} of {slug} {t['feature']} is a progression step: grant levels from the class table ({label})"
            if (slug, t["feature"], t["power"]) == ("mesmerist", "touch-treatment", "major"):
                rule += "; the Vox prints 'major' for its 10th-level Subsonic Strike (Ultimate Intrigue p. 39: 'At 10th level ... replaces touch treatment (major)'), the tier that the class table calls greater"
            # The grant levels may meet another trade of the entry: the whole feature, or the same
            # step twice. Then the named component stays (the one-claim rule needs the two apart).
            proposed = (op, after["feature"], after.get("class"), None, frozenset(levels))
            clash = next(
                (j for j, u in enumerate(data["fields"]["trades"], 1)
                 if j != i and "feature" in u and overlap(proposed, claim_of(u))), None)
            if clash is not None:
                after = dict(before)
                rule = f"kept: grant levels {levels} of {t['power']!r} would overlap trade {clash} of the same key; the named component stays"
            if after != before:
                edits_by_entry.setdefault(data["id"], {})[i] = (op, t[op], after)
            log[(data["id"], i)] = {
                "id": data["id"], "trade": str(i), "op": op, "printed": t[op],
                "before": encode_keys(before), "after": encode_keys(after), "rule": rule,
            }
    # A whole Poison resistance trade next to an explicit immunity trade of the same key is the three
    # resistance steps; the immunity trade names its own grant level.
    for path in sorted((ROOT / "entries").glob("arc-*/*.md")):
        text = path.read_text(encoding="utf-8")
        if "\ntrades = [" not in text:
            continue
        data = tomllib.loads(split_entry(text)[0])
        relations = [r["target"] for r in data.get("relations", []) if r["kind"] == "archetype"]
        if len(relations) != 1 or relations[0] not in ("ref/class/alchemist", "ref/class/investigator"):
            continue
        trades = data["fields"]["trades"]
        for i, t in enumerate(trades, 1):
            op = "replaces" if "replaces" in t else "alters"
            if (data["id"], i) in queued or (data["id"], i) in log or t.get("feature") != "poison-resistance":
                continue
            if t.get("levels") or t.get("power") or t[op].lower() != "poison resistance":
                continue
            if not any(j != i and op in u and re.fullmatch(r"(poison )?immunity( to poison)?", u[op].lower()) for j, u in enumerate(trades, 1)):
                continue
            levels = [int(x) for x in grant_levels(relations[0], "poison resistance +2").split(",")]
            levels += [int(x) for x in grant_levels(relations[0], "poison resistance +4").split(",")]
            levels += [int(x) for x in grant_levels(relations[0], "poison resistance +6").split(",")]
            before = {"feature": "poison-resistance"}
            after = {"feature": "poison-resistance", "levels": sorted(levels)}
            edits_by_entry.setdefault(data["id"], {})[i] = (op, t[op], after)
            log[(data["id"], i)] = {
                "id": data["id"], "trade": str(i), "op": op, "printed": t[op],
                "before": encode_keys(before), "after": encode_keys(after),
                "rule": "the entry also lists poison immunity: the resistance trade is the steps +2, +4 and +6 (class table), and immunity has its own grant level",
            }
    # Adjustments that a reader made by hand, each with its reason.
    if MANUAL.exists():
        for m in read_tsv(MANUAL):
            key = (m["id"], int(m["trade"]))
            front, _ = split_entry(entry_path(m["id"]).read_text(encoding="utf-8"))
            t = tomllib.loads(front)["fields"]["trades"][key[1] - 1]
            if t.get(m["op"]) != m["printed"]:
                raise SystemExit(f"{m['id']} trade {key[1]} is not {m['printed']!r}")
            after = decode_keys(m["after"])
            before_keys = decode_keys(log[key]["before"]) if key in log else {k: t[k] for k in ("feature", "class", "levels", "power") if k in t}
            edits_by_entry.setdefault(m["id"], {})[key[1]] = (m["op"], m["printed"], after)
            log[key] = {
                "id": m["id"], "trade": m["trade"], "op": m["op"], "printed": m["printed"],
                "before": encode_keys(before_keys), "after": encode_keys(after), "rule": "manual: " + m["rule"],
            }
    written = sum(rewrite_entry(entry_id, edits) for entry_id, edits in edits_by_entry.items())
    rows = [log[k] for k in sorted(log)]
    write_tsv(ADJUSTMENTS, ADJUST_COLUMNS, rows)
    print(f"normalize: {len(edits_by_entry)} entries, {len(rows)} adjustments logged, {written} written")


def cmd_check(args):
    rows = read_tsv(QUEUE)
    base = read_tsv(BASELINE)
    problems = []
    # The queue is the migration's queue: every baseline occurrence, with multiplicity, and nothing else.
    cb, cq = Counter(), Counter()
    base_keys = [row_key(b, cb) for b in base]
    queue_keys = [row_key(r, cq) for r in rows]
    for key in sorted(set(base_keys) - set(queue_keys)):
        problems.append(f"baseline row is missing from the queue: {key}")
    for key in sorted(set(queue_keys) - set(base_keys)):
        problems.append(f"queue row is not in the baseline: {key}")
    if len(rows) != len(base):
        problems.append(f"the queue has {len(rows)} rows, the baseline {len(base)}")
    for row in rows:
        where = f"{row['id']} trade {row['trade']} ({row['printed']})"
        if row["disposition"] == "open" and "--allow-open" in args:
            continue
        if row["disposition"] not in ("resolved", "exception"):
            problems.append(f"{where}: disposition is {row['disposition']!r}")
            continue
        if not row["decision"] or not row["book"]:
            problems.append(f"{where}: decision or book is empty")
        if row["evidence"] not in ("print", "manual", "corpus") or (row["evidence"] != "print" and not row["evidence_note"]):
            problems.append(f"{where}: evidence is {row['evidence']!r} without a note")
        if row["evidence"] == "manual" and not row["page"]:
            problems.append(f"{where}: manual evidence without a page")
        if not row["page"] and not row["page_reason"]:
            problems.append(f"{where}: no page and no reason for its absence")
        if row["disposition"] == "resolved" and not row["feature"]:
            problems.append(f"{where}: resolved without a feature")
        if row["disposition"] == "exception" and row["feature"]:
            problems.append(f"{where}: exception with a feature")
    queued = {(r["id"], int(r["trade"])) for r in rows if r["trade"] != "0"}
    cache = {}
    for entry_id in {r["id"] for r in rows}:
        front, _ = split_entry(entry_path(entry_id).read_text(encoding="utf-8"))
        cache[entry_id] = tomllib.loads(front).get("fields", {}).get("trades", [])
    for row in rows:
        if row["trade"] == "0" or row["disposition"] == "open":
            continue
        trades = cache[row["id"]]
        i = int(row["trade"]) - 1
        where = f"{row['id']} trade {row['trade']} ({row['printed']})"
        if i >= len(trades) or trades[i].get(row["op"]) != row["printed"]:
            problems.append(f"{where}: the entry has no such trade")
            continue
        t = trades[i]
        if row["disposition"] == "resolved":
            want = (row["feature"], row["class"] or None, [int(x) for x in row["levels"].split(",")] if row["levels"] else None, row["power"] or None)
            have = (t.get("feature"), t.get("class"), t.get("levels"), t.get("power"))
            if want != have:
                problems.append(f"{where}: the entry holds {have}, the row says {want}")
        elif "feature" in t:
            problems.append(f"{where}: exception, but the entry resolves it to {t['feature']}")
    # Every split is made: the composite is gone and its parts stand next to each other, in print order.
    for (entry_id, op, composite), parts in split_groups().items():
        trades = cache.get(entry_id)
        if trades is None:
            front, _ = split_entry(entry_path(entry_id).read_text(encoding="utf-8"))
            trades = tomllib.loads(front).get("fields", {}).get("trades", [])
        names = [(t.get("replaces") is not None and "replaces" or "alters", t.get("replaces", t.get("alters"))) for t in trades]
        if (op, composite) in names:
            problems.append(f"{entry_id}: the composite {composite!r} is still a trade (run `split`)")
            continue
        want = [(op, part["part"]) for part in parts]
        if not any(names[i:i + len(want)] == want for i in range(len(names))):
            problems.append(f"{entry_id}: the parts of {composite!r} are not next to each other in the entry")
    # The adjustment log agrees with the entries.
    if ADJUSTMENTS.exists():
        for r in read_tsv(ADJUSTMENTS):
            front, _ = split_entry(entry_path(r["id"]).read_text(encoding="utf-8"))
            trades = tomllib.loads(front)["fields"]["trades"]
            t = trades[int(r["trade"]) - 1]
            have = {k: t[k] for k in ("feature", "class", "levels", "power") if k in t}
            if t.get(r["op"]) != r["printed"] or have != decode_keys(r["after"]):
                problems.append(f"{r['id']} trade {r['trade']}: the entry does not match the adjustment log")
    # Every unresolved trade of the corpus is in the queue.
    missing = 0
    for path in sorted((ROOT / "entries").glob("*/*.md")):
        text = path.read_text(encoding="utf-8")
        if "\ntrades = [" not in text:
            continue
        front, _ = split_entry(text)
        data = tomllib.loads(front)
        for i, t in enumerate(data["fields"]["trades"], 1):
            if "feature" not in t and (data["id"], i) not in queued:
                missing += 1
                problems.append(f"{data['id']} trade {i}: unresolved and not in the queue")
    for p in problems[:50]:
        print("check:", p)
    print(f"check: {len(rows)} rows, {len(problems)} problems, {missing} unresolved trades outside the queue")
    sys.exit(1 if problems else 0)


def cmd_stats(args):
    rows = read_tsv(QUEUE)
    counts = Counter((r["kind"], r["reason"], r["disposition"]) for r in rows)
    for key, n in sorted(counts.items()):
        print(n, *key)
    print(len(rows), "rows;", sum(1 for r in rows if r["disposition"] == "open"), "open")


def main():
    commands = {
        "baseline": cmd_baseline, "fill": cmd_fill, "apply": cmd_apply, "split": cmd_split, "normalize": cmd_normalize,
        "check": cmd_check, "stats": cmd_stats,
    }
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        raise SystemExit(__doc__)
    commands[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
