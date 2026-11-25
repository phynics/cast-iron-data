#!/usr/bin/env python3
"""Leaf packets and leaf records of the multi-model structure for phynics/cast-iron#540.

A batch lead sends each hold of `feature-prose-540.py --compare` (a feature row with status `hold`) to one
producer leaf, then the producer's record to a verifier leaf of the other model family, then, when the two
disagree, to a tie-break leaf. A leaf edits no file, runs no git and judges only its one hold: it gets a packet (text
only, no path) and returns one fixed-format record.

    feature-prose-540-leaves.py packets  --book ID --books DIR --cache DIR --out DIR
        write one packet per hold row of the review table of the book: DIR/<packet>.md, DIR/index.json
    feature-prose-540-leaves.py verifier --book ID --index DIR --packet NAME --role verifier|tiebreak
        the packet of a verifier or tie-break leaf: the producer packet plus the record(s) to check
    feature-prose-540-leaves.py parse    --book ID --packet NAME --role producer|verifier|tiebreak --model M [--call N]
                                         [--seconds S] [--tokens N] FILE
        read the one fenced JSON record in FILE, validate it, and append it with its provenance to
        `scripts/feature-prose-540-<book>.records.jsonl`; exit 1 and write nothing when it does not validate
        (the leaf is run again; a record is never mended by hand)
    feature-prose-540-leaves.py status   --book ID
        per hold: producer, verifier, agreement, what is left to do
    feature-prose-540-leaves.py apply    --book ID
        write the accepted records as rows of `<book>.decisions.tsv` and `<book>.edits.toml`, and the queue file
        `scripts/feature-prose-540-<book>.queue.tsv`
    feature-prose-540-leaves.py scrub    --book ID
        take a third-party web address out of the records (public text names the book and the page only)
    feature-prose-540-leaves.py --self-test

The record (one fenced JSON object): entry, feature (the anchor), verdict (print | edit | hold), text (the proposed
printed text of the feature, Markdown, without the head), trades ({op, name, by} each), level (1..20 or null), rulings
(numbers), confidence (0..1), notes. A verifier or tie-break record also has `agrees` (bool) and `disagreements`.
`print` means: take the script's print text as it is; `edit` means: this text instead (an empty text drops a corpus-only
head); `hold` means: the leaf cannot decide (an owner question).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

VERDICTS = ("print", "edit", "hold")
ROLES = ("producer", "verifier", "tiebreak")
RECORD_KEYS = ["entry", "feature", "verdict", "text", "trades", "level", "rulings", "confidence", "notes"]
VERIFIER_KEYS = RECORD_KEYS + ["agrees", "disagreements"]

# The owner rulings of phynics/cast-iron#540 that a hold can turn on, quoted (numbers as on the issue).
RULINGS = {
    3: "Print against the corpus in a number or rule word: take print's wording; a changed number or rule word is held for an errata check before it lands.",
    8: "The comparator expands printed \"every N levels\" rules (\"+1 for every three levels after 3rd\") before comparing; where the values are equal, print's wording is taken; the rest get a hand review. Where print corrects a corpus value, print wins.",
    9: "Misprints are fixed only when the meaning is certain (\"A 3rd level\" -> \"At 3rd level\"), and each fix is recorded in the note.",
    10: "Print's asterisks without their key are dropped; corpus paragraphs that print does not have are dropped.",
    11: "When a feature replaces a base-class feature gained at 1st level and print gives no level, `level = 1` (ruling 35: even if it also replaces later features).",
    14: "The hold is decided against print: print's wording unless the number is a likely misprint.",
    15: "Option-list items printed as a list under a feature (creature types, forms, bloodlines, domains, mysteries, totems) stay plain subheadings under their feature: not `features`, no Level head.",
    16: "Printed cross-references stay (\"(see the Stealth skill)\", \"(see below)\").",
    17: "Stored trades with no printed support are dropped.",
    18: "A table is written as a Markdown table, each cell as printed.",
    22: "Level back-references (\"... bonus spells at these levels\"): rename the stored trade to the printed words; the levels live in the Level head.",
    26: "Bare book citations are dropped where the corpus links the named rule instead (\"augury (Pathfinder RPG Core Rulebook 245)\"); so are superscripts and daggers that mark another book (UM, APG, UC, ARG). \"see\" cross-references stay.",
    28: "A stored trade stays when the prose of a feature states it; its `by` names that feature.",
    33: "Scaffold headings (Class Skills, Skills, Alignment, Bonus Feats, Prerequisites, Weapon and Armor Proficiency, ...) are never `features`.",
    34: "Talent lists, ki-power lists and courses (\"can select from the following ...\") are unlisted subheadings under the parent feature.",
    36: "A trade stated in a feature's prose (\"A faith hunter does not gain the justice or destruction judgments\") is kept with `by` that feature.",
    41: "A box holding rules that the archetype uses stays in the entry as an unlisted section; a pure lore box is left out.",
}
FORM = """A feature is a headed section of the printed prose, as the book prints it: the printed paragraphs and the printed
"This replaces/alters ..." sentence, with no invented rows, labels or subheads. Italics are written _like this_ and links as
[text](ref/kind/slug), as the corpus has them in the current text. Print wins over the corpus in wording and numbers unless the
printed number is a likely misprint."""

PACKET_HEAD = """You are a leaf of a batch of the data work of phynics/cast-iron#540 (Pathfinder First Edition rules: archetype
features rewritten as the book prints them). Judge only this one hold. Edit no files, run no git commands, run no tools: everything
you need is in this packet. Return exactly one record as ONE fenced ```json block, nothing else."""

OUTPUT_FORMAT = """## The record to return

One fenced JSON object, exactly these keys: {"entry": "<id above>", "feature": "<anchor above>", "verdict": "print|edit|hold",
"text": "<proposed printed text of this feature, Markdown, paragraphs separated by a blank line, without the head>",
"trades": [{"op": "replaces|alters", "name": "<as the printed sentence says it>", "by": ["<anchor of the feature that prints it>"]}],
"level": <1..20 or null>, "rulings": [<numbers>], "confidence": <0..1>, "notes": "<one or two sentences>"}

* print: take the script's print text as it is (set `text` to \"\"). edit: print's text needs a change (an extraction error,
  a table, a missing italic, a misplaced paragraph, raw HTML), or the head is the corpus's own and print has none: write the corrected text
  (an empty `text` drops a head that print does not have, ruling 10). hold: you cannot decide; say why and quote the printed words.
* trades: the trades THIS feature's printed text states ("This replaces ... / This alters ..."), as the sentence says them.
* level: as print proves it (the first sentence's "At Nth level" lead, or ruling 11), else null."""

TIEBREAK_NOTE = """## You are the tie-break

A producer and a verifier of two model families disagree about this hold. Their two records are below. Decide from the printed text
and the rulings, not by counting: return your OWN complete record, plus `"agrees"` (true when it equals the producer's record) and
`"disagreements"` (where you differ from the producer, with the printed words)."""

VERIFIER_NOTE = """## You are a verifier

Another model produced the record below for this same hold. Check it against the printed page text and the rulings, not against
your own first guess. Return your OWN complete record in the same format (what you would propose), plus two more keys:
`"agrees"` (true only when you would write the same text, trades and level; wording that differs only in white space is the same)
and `"disagreements"` (a list of short strings: each place where you differ, with the printed words; empty when you agree)."""


def load_main():
    spec = importlib.util.spec_from_file_location("fp540", HERE / "feature-prose-540.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["fp540"] = mod
    spec.loader.exec_module(mod)
    return mod


def norm(text: str) -> str:
    t = unicodedata.normalize("NFC", text or "")
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("–", "-").replace("−", "-").replace("—", "-").replace(" ", " ")
    return re.sub(r"\s+", " ", t).strip()


def tsv_rows(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").split("\n")
    head = lines[0].split("\t")
    return [dict(zip(head, ln.split("\t"))) for ln in lines[1:] if ln]


def packet_name(entry: str, anchor: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", f"{entry.removeprefix('ref/')}--{anchor}".lower()).strip("-")


def records_path(book: str) -> Path:
    return HERE / f"feature-prose-540-{book}.records.jsonl"


def queue_path(book: str) -> Path:
    return HERE / f"feature-prose-540-{book}.queue.tsv"


BASE_RULINGS = (3, 8, 9, 14, 26)


def rulings_for(note: str, print_text: str, draft: str) -> list[int]:
    """The rulings that a hold can turn on: a base set, plus those that its note and texts point to."""
    out = set(BASE_RULINGS)
    if re.search(r"level 1|\blevel\b.*trade", note, re.I) or not re.match(r"\s*(?:At|Starting at|Beginning at) \d", print_text):
        out.add(11)
    if re.search(r"replaces|alters", print_text, re.I):
        out |= {17, 28}
    if "|" in print_text or "table" in print_text.lower():
        out.add(18)
    if re.search(r"following|choose|select", print_text, re.I):
        out |= {15}
    if "head not printed" in note or "not in the import" in note:
        out |= {10, 33}
    return sorted(out)


# ---- validation -------------------------------------------------------------------------------------

def extract_json(text: str) -> dict:
    blocks = re.findall(r"```(?:json)?\s*\n(.*?)\n\s*```", text, re.S)
    if len(blocks) != 1:
        raise ValueError(f"expected exactly one fenced JSON block, found {len(blocks)}")
    try:
        obj = json.loads(blocks[0])
    except json.JSONDecodeError as ex:
        raise ValueError(f"the JSON does not parse: {ex}")
    if not isinstance(obj, dict):
        raise ValueError("the record is not a JSON object")
    return obj


def validate(rec: dict, role: str, entry: str, anchor: str) -> list[str]:
    errs: list[str] = []
    keys = VERIFIER_KEYS if role != "producer" else RECORD_KEYS
    if set(rec) != set(keys):
        extra, missing = sorted(set(rec) - set(keys)), sorted(set(keys) - set(rec))
        errs.append(f"keys differ: missing {missing}, extra {extra}")
        return errs
    if rec["entry"] != entry:
        errs.append(f"entry is {rec['entry']!r}, the packet is {entry!r}")
    if rec["feature"] != anchor:
        errs.append(f"feature is {rec['feature']!r}, the packet is {anchor!r}")
    if rec["verdict"] not in VERDICTS:
        errs.append(f"verdict {rec['verdict']!r} is not one of {VERDICTS}")
    if not isinstance(rec["text"], str):
        errs.append("text is not a string")
    if not isinstance(rec["trades"], list):
        errs.append("trades is not a list")
    else:
        for t in rec["trades"]:
            if not (isinstance(t, dict) and set(t) == {"op", "name", "by"} and t["op"] in ("replaces", "alters")
                    and isinstance(t["name"], str) and t["name"].strip()
                    and (t["by"] is None or (isinstance(t["by"], list) and all(isinstance(x, str) for x in t["by"])))):
                errs.append(f"a trade is not {{op, name, by}}: {t!r}")
    lv = rec["level"]
    if not (lv is None or (isinstance(lv, int) and not isinstance(lv, bool) and 1 <= lv <= 20)):
        errs.append("level is not null or an integer 1..20")
    if not (isinstance(rec["rulings"], list) and all(isinstance(x, int) and not isinstance(x, bool) for x in rec["rulings"])):
        errs.append("rulings is not a list of numbers")
    c = rec["confidence"]
    if not (isinstance(c, (int, float)) and not isinstance(c, bool) and 0 <= c <= 1):
        errs.append("confidence is not a number 0..1")
    if not (isinstance(rec["notes"], str) and rec["notes"].strip()):
        errs.append("notes is empty")
    if rec["verdict"] == "edit" and not rec["text"].strip() and not rec["notes"].strip():
        errs.append("an edit with no text needs a note that says it drops the head")
    if role != "producer":
        if not isinstance(rec["agrees"], bool):
            errs.append("agrees is not a bool")
        if not (isinstance(rec["disagreements"], list) and all(isinstance(x, str) for x in rec["disagreements"])):
            errs.append("disagreements is not a list of strings")
        elif rec["agrees"] is True and rec["disagreements"]:
            errs.append("agrees is true and disagreements is not empty")
        elif rec["agrees"] is False and not rec["disagreements"]:
            errs.append("agrees is false and disagreements is empty")
    return errs


TRADE_SENTENCE = re.compile(r"(?:^|(?<=\n)|(?<=[.!?] ))This (?:ability |class feature |performance )?(?:replaces|alters|changes)\b[^\n]*?\.(?=\s|$)")


def settle(rec: dict, index_row: dict) -> dict:
    """Typography and the shorthand of the format: curly quotes become the corpus's straight quotes; a `print` verdict
    with an empty text means the script's print text; an `edit` whose text is the print text is a `print`."""
    rec = dict(rec)
    rec["text"] = rec["text"].replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    if rec["verdict"] == "print" and not rec["text"].strip():
        rec["text"] = index_row["print"]
    if rec["verdict"] == "edit" and rec["text"].strip() and norm(rec["text"]) == norm(index_row["print"]):
        rec["verdict"] = "print"
        rec["text"] = index_row["print"]
    return rec


def check_against_packet(rec: dict, index_row: dict) -> list[str]:
    """The record must match the packet's print text when it says `print`."""
    errs = []
    if rec["verdict"] == "print" and norm(rec["text"]) != norm(index_row["print"]):
        errs.append("verdict print, but the text is not the script's print text")
    if rec["verdict"] == "edit" and rec["text"].strip():
        # an edit keeps the printed trade sentence of the feature ("This replaces ...", "This alters ...")
        for m in TRADE_SENTENCE.finditer(index_row["print"]):
            if norm(m.group(0)).lower() not in norm(rec["text"]).lower():
                errs.append(f"the edit text lacks the printed trade sentence: {m.group(0).strip()!r}")
    return errs


def same_proposal(a: dict, b: dict) -> bool:
    """Whether two records propose the same thing: verdict class, text (white space and quotes folded), level, trades."""
    if a["verdict"] != b["verdict"]:
        return False
    if a["verdict"] == "hold":
        return True
    ta = sorted((t["op"], norm(t["name"]).lower()) for t in a["trades"])
    tb = sorted((t["op"], norm(t["name"]).lower()) for t in b["trades"])
    return norm(a["text"]) == norm(b["text"]) and a["level"] == b["level"] and ta == tb


# ---- packets ----------------------------------------------------------------------------------------

def build_rows(args):
    fp = load_main()
    corpus = ROOT
    fp.configure_book(args.book)
    title = fp.publication_title(corpus, args.book)
    pdf = fp.find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    entries = {e.id: e for e in fp.load_entries(corpus, args.book)}
    return fp, bk, pdf, title, entries


def raw_page(pdf: Path, n: int, cache: dict) -> str:
    if n not in cache:
        out = subprocess.run(["pdftotext", "-raw", "-f", str(n), "-l", str(n), str(pdf), "-"], capture_output=True, text=True,
                             check=True).stdout
        cache[n] = out.rstrip()
    return cache[n]


HEAD_COLON = re.compile(r"\n(?:[A-Z][^\n:]{2,70}? \((?:Ex|Su|Sp)[^)\n]*\)|[A-Z][A-Za-z' -]{3,40}):")


def printed_window(raw: str, head: str, whole: bool) -> str:
    """The part of the page text around the head: from a little before it to the next printed head (at most 5,000 characters).
    A hold whose head print lacks gets the whole text."""
    name = re.sub(r"\s*\((?:Ex|Su|Sp)[^)]*\)\s*$", "", head).strip()
    at = raw.find(name)
    if whole or at < 0:
        return raw
    start = max(0, raw.rfind("\n", 0, max(0, at - 250)))
    nxt = HEAD_COLON.search(raw, at + len(name) + 40)
    end = min(len(raw), nxt.start() + 60 if nxt else len(raw), at + 3500)
    trade = re.search(r"This (?:replaces|alters|changes)\b[^\n]*(?:\n[^\n]*?)*?\.\s*\n", raw[at:end + 1])
    if trade:
        # the printed trade sentence closes the feature: keep it, and 300 characters more (a sentence that follows it)
        end = min(end, at + trade.end() + 80)
        nl = raw.find("\n", end)
        end = nl if nl >= 0 else end
    return ("..." if start else "") + raw[start:end].strip() + ("..." if end < len(raw) else "")


def cmd_packets(args) -> int:
    fp, bk, pdf, title, entries = build_rows(args)
    rows = tsv_rows(fp.tsv_path(ROOT, args.book))
    holds = [r for r in rows if r["status"] == "hold"]
    decisions = fp.read_decisions(ROOT, args.book)
    edits = fp.read_edits(ROOT, args.book)
    adds = fp.read_adds(ROOT, args.book)
    stops = {fp.squash(x.title) for x in entries.values()} | fp.CLASS_TITLES | fp.UNTYPED_ARCHETYPE_TITLES
    inv = {v: k for k, v in bk.printed.items()}
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    cache: dict = {}
    index = []
    by_entry: dict[str, list[dict]] = {}
    for r in holds:
        by_entry.setdefault(r["entry"], []).append(r)
    for eid, hrows in by_entry.items():
        e = entries[eid]
        page = int(e.page) if e.page.isdigit() else None
        blocks = fp.read_blocks(bk, max(1, page + 1 - 3), min(page + 1 + 4, max(bk.pages)))
        section = fp.find_section(blocks, e.title, stops)
        res = fp.compare_entry(e, section, bk)
        res["decisions"], res["edits"], res["adds"] = decisions, edits, adds
        fin = fp.finalize(e, res)
        opening_imp, feats = fp.parse_import(e.body, set())
        by_name = {fp.anchor_of(fp.head_text(f.name)): f for f in feats}
        trades = fp.trades_of(e)
        printed = [(r["anchor"], r["head"], r["level"], r["listed"]) for r in fin["rows"]]
        for hr in hrows:
            row = next((x for x in fin["rows"] if x["anchor"] == hr["anchor"]), None)
            if row is None:
                continue
            f = by_name.get(hr["anchor"])
            current = "\n\n".join(fp.logical(b) for b in f.raw[1:]) if f else "(no such feature in the import)"
            pg = int(row["page"]) if str(row["page"]).isdigit() else page
            pages = [pg] + ([pg + 1] if pg + 1 in inv else [])
            joined = "\n\n".join(f"[printed page {p}]\n{raw_page(pdf, inv[p], cache)}" for p in pages if p in inv)
            raw = printed_window(joined, row["head"], not row["print"])
            trade_lines = "\n".join(
                f"- {'replaces' if 'replaces' in t else 'alters'}: {t.get('replaces') or t.get('alters')}" for t in trades) or "(none)"
            ruling_lines = "\n".join(f"{n}. {RULINGS[n]}" for n in rulings_for("; ".join(row["notes"]), row["print"], row["draft"]))
            structure = "; ".join(f"{h} [`{a}`{', level ' + str(lv) if lv else ''}{'' if li else ', unlisted'}]" for a, h, lv, li in printed)
            name = packet_name(eid, hr["anchor"])
            text = f"""{PACKET_HEAD}

# Hold: {title} p. {row['page'] or e.page}: {row['head']}

* entry id: `{eid}` (archetype "{e.title}" of {', '.join(c.split('/')[-1] for c in e.classes)})
* feature anchor: `{hr['anchor']}`
* why the script held it: {'; '.join(row['notes']) or hr['note']}

## Form and rulings

{FORM}

Rulings that can apply (owner rulings of phynics/cast-iron#540, numbered as on the issue; ones that cannot apply are left out):

{ruling_lines}

## Stored trades of the entry

{trade_lines}

## Heads of the entry in print order

{structure}

## Current corpus text of this feature (the import form: bold rows, labels, invented upgrade rows)

{current}

## Draft by the script (rule draft built from the import rows)

{row['draft'] or '(none: the import has no such feature)'}

## Print text by the script (extracted from the book's text layer; links and italics carried over from the corpus)

{row['print'] or '(none: print has no such head)'}

## Printed text around the head (the book's text layer, reading order; a mark such as APG or UM glued to a word is a cross-reference to another book)

{raw}

{OUTPUT_FORMAT}
"""
            (out / f"{name}.md").write_text(text, encoding="utf-8")
            index.append({"packet": name, "entry": eid, "feature": hr["anchor"], "head": row["head"], "page": row["page"] or e.page,
                          "print": row["print"], "draft": row["draft"], "note": "; ".join(row["notes"]) or hr["note"],
                          "chars": len(text)})
    (out / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(index)} packets in {len(by_entry)} entries; largest {max((i['chars'] for i in index), default=0)} characters")
    return 0


def cmd_verifier(args) -> int:
    """The packet of a verifier (`--role verifier`) or tie-break leaf (`--role tiebreak`): the producer packet without the two
    import-derived sections (the current corpus text and the rule draft are not evidence about print), plus the record(s)
    to check. A `print` record shows an empty text (the print text)."""
    packet = (Path(args.index) / f"{args.packet}.md").read_text(encoding="utf-8")
    res = resolve(args.book).get(args.packet) or {}
    shown = []
    for role in ("producer", "verifier"):
        r = res.get(role)
        if r and (role == "producer" or args.role == "tiebreak"):
            rec = dict(r["record"])
            if rec["verdict"] == "print":
                rec["text"] = ""
            shown.append((role, r["model"], rec))
    if not shown:
        raise SystemExit("no producer record for this packet")
    for sec in ("## Current corpus text of this feature", "## Draft by the script"):
        packet = re.sub(rf"{re.escape(sec)}.*?(?=\n## )", "", packet, flags=re.S)
    marker = "## The record to return"
    head, tail = packet.split(marker, 1)
    note = VERIFIER_NOTE if args.role == "verifier" else TIEBREAK_NOTE
    body = "".join(f"### Record of the {role} leaf\n\n```json\n{json.dumps(rec, ensure_ascii=False, indent=1)}\n```\n\n" for role, _m, rec in shown)
    sys.stdout.write(head.rstrip() + "\n\n" + note + "\n\n" + body + marker + tail.rstrip()
                     + "\n* A record that checks another: add `\"agrees\"` (bool) and `\"disagreements\"` (list of strings) to your record. A text of \"\" with verdict print means the script's print text.\n")
    return 0


# Public text names the book and the page only: a third-party site that a leaf quotes from a corrupt corpus text is not named.
REDACT = [(re.compile(r"(?i)\b(?:https?://)?(?:www\.)?d20pfsrd(?:\.com)?\S*"), "a third-party web address"),
          (re.compile(r"(?i)archives of nethys|aonprd\S*"), "a rules web site")]


def redact(obj):
    if isinstance(obj, str):
        for rx, to in REDACT:
            obj = rx.sub(to, obj)
        return obj
    if isinstance(obj, list):
        return [redact(x) for x in obj]
    if isinstance(obj, dict):
        return {k: redact(v) for k, v in obj.items()}
    return obj


def cmd_scrub(args) -> int:
    p = records_path(args.book)
    rows = [json.loads(ln) for ln in p.read_text(encoding="utf-8").split("\n") if ln]
    p.write_text("".join(json.dumps(redact(r), ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
    print(f"{len(rows)} records scrubbed")
    return 0


# ---- records ----------------------------------------------------------------------------------------

def read_records(book: str) -> list[dict]:
    p = records_path(book)
    return [json.loads(ln) for ln in p.read_text(encoding="utf-8").split("\n") if ln] if p.exists() else []


def cmd_parse(args) -> int:
    index_dir = Path(args.index) if args.index else None
    if not index_dir:
        raise SystemExit("--index DIR (the packets directory) is needed")
    index = {i["packet"]: i for i in json.loads((index_dir / "index.json").read_text(encoding="utf-8"))}
    ix = index[args.packet]
    text = Path(args.file).read_text(encoding="utf-8")
    try:
        rec = extract_json(text)
    except ValueError as ex:
        print(f"REJECTED {args.packet} ({args.role}, {args.model}): {ex}", file=sys.stderr)
        return 1
    errs = validate(rec, args.role, ix["entry"], ix["feature"]) if set(rec) >= set(RECORD_KEYS) else [
        f"keys differ: missing {sorted(set(RECORD_KEYS) - set(rec))}"]
    if not errs:
        rec = settle(rec, ix)
        errs = check_against_packet(rec, ix)
    if errs:
        print(f"REJECTED {args.packet} ({args.role}, {args.model}): " + "; ".join(errs), file=sys.stderr)
        return 1
    row = {"packet": args.packet, "role": args.role, "model": args.model, "call": args.call, "seconds": args.seconds,
           "tokens": args.tokens, "record": redact(rec)}
    with records_path(args.book).open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    print(f"ok {args.packet} ({args.role}, {args.model}): {rec['verdict']}"
          + (f", agrees={rec['agrees']}" if "agrees" in rec else ""))
    return 0


def resolve(book: str) -> dict[str, dict]:
    """Per packet: the producer, the verifier, the tie-break, whether they agree, and the accepted record."""
    by: dict[str, dict] = {}
    for r in read_records(book):
        d = by.setdefault(r["packet"], {})
        d[r["role"]] = r        # the last record of a role wins (a re-run replaces a rejected one)
    out = {}
    for packet, d in by.items():
        p, v, t = d.get("producer"), d.get("verifier"), d.get("tiebreak")
        agreed = None
        accepted = None
        if p and v:
            # the comparison decides (typography folded): a leaf's own `agrees` flag is read as a measurement, not as the verdict
            agreed = same_proposal(p["record"], v["record"])
            if agreed:
                accepted = p["record"]
        if p and v and not agreed and t:
            # the tie-break decides between the two proposals: it agrees with the one it matches
            if same_proposal(t["record"], p["record"]):
                accepted = p["record"]
            elif same_proposal(t["record"], v["record"]):
                accepted = v["record"]
            else:
                accepted = t["record"]
        out[packet] = {"producer": p, "verifier": v, "tiebreak": t, "agreed": agreed, "accepted": accepted}
    return out


def cmd_status(args) -> int:
    res = resolve(args.book)
    flags = [(k, d["verifier"]["record"]["agrees"], d["agreed"]) for k, d in res.items() if d["verifier"] and d["agreed"] is not None]
    print(f"verifier flag differs from the comparison: {sum(1 for _k, a, b in flags if a != b)} of {len(flags)}")
    for packet, d in sorted(res.items()):
        todo = "accepted" if d["accepted"] else ("tie-break needed" if d["agreed"] is False and not d["tiebreak"] else (
            "verifier needed" if d["producer"] and not d["verifier"] else "open"))
        print(f"{packet}\tproducer={d['producer']['model'] if d['producer'] else '-'}\tverifier={d['verifier']['model'] if d['verifier'] else '-'}"
              f"\tagreed={d['agreed']}\t{todo}")
    return 0


# ---- apply ------------------------------------------------------------------------------------------

def cmd_apply(args) -> int:
    fp = load_main()
    res = resolve(args.book)
    index = {i["packet"]: i for i in json.loads((Path(args.index) / "index.json").read_text(encoding="utf-8"))}
    dpath = fp.decisions_path(ROOT, args.book)
    epath = ROOT / "scripts" / f"feature-prose-540-{args.book}.edits.toml"
    dec = fp.read_decisions(ROOT, args.book)
    edits_toml = epath.read_text(encoding="utf-8") if epath.exists() else ""
    queue = []
    for packet, ix in sorted(index.items()):
        d = res.get(packet)
        acc = d["accepted"] if d else None
        pm = d["producer"]["model"] if d and d["producer"] else ""
        vm = d["verifier"]["model"] if d and d["verifier"] else ""
        tm = d["tiebreak"]["model"] if d and d["tiebreak"] else ""
        status, verdict = "open", ""
        key = (ix["entry"], ix["feature"])
        if acc:
            verdict = acc["verdict"]
            rl = ", ".join(str(n) for n in acc["rulings"]) or "-"
            note = (f"hand review of the hold by leaf records (ruling{'s' if len(acc['rulings']) != 1 else ''} {rl}"
                    f"{'; tie-break' if tm else ''}): {acc['notes'].strip()[:420]}")
            note = re.sub(r"\s+", " ", note).replace("\t", " ")
            if acc["verdict"] == "print":
                # a structure decision of the lead (`unlist`, `sub-of:ANCHOR`) already takes print's wording: it stays
                if key not in dec or dec[key][0] == "print":
                    dec[key] = ("print", note)
                status = "decided"
            elif acc["verdict"] == "edit" and not acc["text"].strip():
                dec[key] = ("drop", note)
                status = "decided"
            elif acc["verdict"] == "edit":
                if f'entry = "{key[0]}"\nanchor = "{key[1]}"' not in edits_toml:
                    edits_toml += (("\n" if edits_toml and not edits_toml.endswith("\n\n") else "") +
                                   f'[[edit]]\nentry = "{key[0]}"\nanchor = "{key[1]}"\nnote = {fp.toml_str(note)}\n'
                                   f"text = '''\n{acc['text'].strip()}\n'''\n\n")
                status = "decided"
            else:
                status = "owner-question"
        queue.append({"entry": ix["entry"], "feature": ix["feature"], "status": status, "producer_model": pm,
                      "verifier_model": vm, "tiebreak_model": tm, "page": ix["page"], "verdict": verdict,
                      "agreed": "" if not d or d["agreed"] is None else ("yes" if d["agreed"] else "no")})
    if dec:
        lines = ["\t".join(fp.DECISION_HEADER)] + ["\t".join([k[0], k[1], v[0], v[1]]) for k, v in sorted(dec.items())]
        dpath.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if edits_toml:
        epath.write_text(edits_toml.rstrip("\n") + "\n", encoding="utf-8")
    # the features that the script settled (no hold): no leaf, the script's status as the verdict
    held = {(ix["entry"], ix["feature"]) for ix in index.values()}
    for r in tsv_rows(fp.tsv_path(ROOT, args.book)):
        if r["status"] != "hold" and (r["entry"], r["anchor"]) not in held and r["anchor"]:
            queue.append({"entry": r["entry"], "feature": r["anchor"], "status": "script", "producer_model": "", "verifier_model": "",
                          "tiebreak_model": "", "page": r["page"], "verdict": r["status"], "agreed": ""})
    queue.sort(key=lambda q: (q["entry"], q["status"] == "script", q["feature"]))
    cols = ["entry", "feature", "status", "producer_model", "verifier_model", "tiebreak_model", "page", "verdict", "agreed"]
    for q in queue:
        q["page"] = str(q["page"])
    queue_path(args.book).write_text("\n".join(["\t".join(cols)] + ["\t".join(q[c] for c in cols) for q in queue]) + "\n",
                                     encoding="utf-8")
    print(f"{len(queue)} queue rows: " + ", ".join(f"{s} {sum(1 for q in queue if q['status'] == s)}"
                                                  for s in sorted({q['status'] for q in queue})))
    return 0


# ---- self-test --------------------------------------------------------------------------------------

def self_test() -> int:
    ok = 0

    def check(cond: bool, what: str) -> None:
        nonlocal ok
        if not cond:
            raise SystemExit(f"self-test failed: {what}")
        ok += 1

    good = {"entry": "ref/x/y", "feature": "z", "verdict": "print", "text": "At 1st level, a y gains a bonus.", "trades": [
        {"op": "replaces", "name": "Bravery", "by": ["z"]}], "level": 1, "rulings": [3], "confidence": 0.9, "notes": "ok"}
    check(extract_json("noise\n```json\n" + json.dumps(good) + "\n```\n")["feature"] == "z", "extract one block")
    for bad in ("no block", "```json\n{}\n```\n```json\n{}\n```", "```json\n{not json}\n```", "```json\n[1]\n```"):
        try:
            extract_json(bad)
            check(False, "extract must reject " + bad[:20])
        except ValueError:
            check(True, "rejects")
    check(validate(good, "producer", "ref/x/y", "z") == [], "a good record validates")
    check(validate({**good, "verdict": "maybe"}, "producer", "ref/x/y", "z") != [], "bad verdict")
    check(validate({**good, "level": 21}, "producer", "ref/x/y", "z") != [], "bad level")
    check(validate({**good, "level": None}, "producer", "ref/x/y", "z") == [], "null level")
    check(validate({**good, "trades": [{"op": "removes", "name": "a", "by": []}]}, "producer", "ref/x/y", "z") != [], "bad trade op")
    check(validate({**good, "confidence": 2}, "producer", "ref/x/y", "z") != [], "bad confidence")
    check(validate(good, "producer", "ref/x/y", "other") != [], "wrong anchor")
    extra = {k: v for k, v in good.items() if k != "notes"}
    check(validate(extra, "producer", "ref/x/y", "z") != [], "missing key")
    ver = {**good, "agrees": True, "disagreements": []}
    check(validate(ver, "verifier", "ref/x/y", "z") == [], "a verifier record")
    check(validate({**ver, "agrees": False}, "verifier", "ref/x/y", "z") != [], "agrees false needs disagreements")
    check(validate(good, "verifier", "ref/x/y", "z") != [], "a verifier record needs agrees")
    check(check_against_packet(good, {"print": "At 1st level,  a y gains a bonus."}) == [], "print text equal modulo white space")
    check(check_against_packet(good, {"print": "At 2nd level, a y gains a bonus."}) != [], "print text differs")
    ed = {**good, "verdict": "edit", "text": "A y gains a bonus."}
    check(check_against_packet(ed, {"print": "A y gains a bonus.\n\nThis alters the warpriest's blessings."}) != [], "an edit must keep the trade sentence")
    check(check_against_packet({**ed, "text": "A y gains a bonus.\n\nThis alters the warpriest's blessings."},
                               {"print": "A y gains a bonus.\n\nThis alters the warpriest's blessings."}) == [], "an edit with the trade sentence")
    other = {**good, "text": "At 1st level, a y gains a ’bonus."}
    check(same_proposal(good, {**good, "text": " At 1st level, a y gains a bonus. "}), "same modulo space")
    check(not same_proposal(good, other), "a different text")
    check(not same_proposal(good, {**good, "level": None}), "a different level")
    check(not same_proposal(good, {**good, "trades": []}), "different trades")
    check(packet_name("ref/arc-fighter/aerial-assaulter", "take-the-high-ground") == "arc-fighter-aerial-assaulter-take-the-high-ground",
          "packet name")
    ix = {"print": "At 1st level, a y can't fly."}
    sp = settle({**good, "verdict": "print", "text": ""}, ix)
    check(sp["text"] == ix["print"] and sp["verdict"] == "print", "an empty print text is the print text")
    se = settle({**good, "verdict": "edit", "text": "At 1st level, a y can\u2019t fly."}, ix)
    check(se["verdict"] == "print", "an edit equal to print after quote folding is a print")
    se2 = settle({**good, "verdict": "edit", "text": "At 2nd level, a y can\u2019t fly."}, ix)
    check(se2["verdict"] == "edit" and "'" in se2["text"], "a real edit stays, quotes folded")
    check("d20pfsrd" not in redact("a stray d20pfsrd anchor around hinyasi"), "redact names no third-party site")
    print(f"leaves self-test: {ok} checks passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", nargs="?", choices=["packets", "verifier", "parse", "status", "apply", "scrub"])
    ap.add_argument("file", nargs="?")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--book")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    ap.add_argument("--out")
    ap.add_argument("--index")
    ap.add_argument("--packet")
    ap.add_argument("--role", choices=ROLES)
    ap.add_argument("--model", default="")
    ap.add_argument("--call", type=int, default=1)
    ap.add_argument("--seconds", type=float, default=0)
    ap.add_argument("--tokens", type=int, default=0)
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.cmd == "packets":
        return cmd_packets(args)
    if args.cmd == "verifier":
        return cmd_verifier(args)
    if args.cmd == "parse":
        return cmd_parse(args)
    if args.cmd == "status":
        return cmd_status(args)
    if args.cmd == "apply":
        return cmd_apply(args)
    if args.cmd == "scrub":
        return cmd_scrub(args)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
