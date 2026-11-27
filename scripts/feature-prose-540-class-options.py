#!/usr/bin/env python3
"""Class options as printed prose (phynics/cast-iron#540, the class-options phase).

A companion of `feature-prose-540.py`, which it loads as a library: the print reader (`read_blocks`, `compare_entry`, `print_md`,
the OCR and layout switches of a book) is the one of the archetype pass, so the two never read print differently. The archetype
rules of #540 (rulings 1 to 58) apply to class options as far as they fit; what is new is the shape of the entry.

Shapes (owner rulings of 2026-11-24 on the data plan)
-----------------------------------------------------
- **single** (1,597 entries): one power whose name repeats the entry title. The converted body is the printed paragraphs, with no
  head that repeats the title and no `features` (ruling Q1).
- **multi** (about 465): several powers, 360 of them under section headings ("### Revelations"). Each power becomes a head one level
  below its section heading (`####`), or `##` with no section, with an explicit `{#anchor}`; the entry gets `features`, in print order,
  with a `level` only when print gives it (the archetype rule, Q4). The blocks that are no power (Deities, Bonus Spells, ...) stay.
- **none** (705 entries): no import row. They are out of the rewrite; `--compare` and `--check` only report them (ruling Q2).

An entry converts all or nothing, and a converted entry has no import row left, which is also what takes it out of the scope of
`rewrite-class-option-powers.py --check` (its resolutions and exceptions are then `retired`).

Files (per book, beside the archetype files, which this script never touches)
-----------------------------------------------------------------------------
`scripts/feature-prose-540-<book>.class-options.tsv`
    One row per power: entry, feature (the name as written), anchor, shape, level_import, level, verdict, status, page, span_sha256, note.
    `verdict`: `agree` (the rule draft equals print), `differ` (print differs from the draft in wording only), `hold` (a number or a
    rule word differs, or the draft cannot express print), `missing-head` (the import has a power that print does not show),
    `nopage`, `nobook`. `status` is what `--write` goes by: `draft`, `print` or `hold` (as in the archetype table).
`scripts/feature-prose-540-<book>.class-options.proposals.toml`
    The printed text of each power, which a TSV cannot hold.

Usage
-----
    feature-prose-540-class-options.py --self-test
    feature-prose-540-class-options.py [CORPUS] --compare --book ID [--families a,b] [--books DIR --cache DIR]
    feature-prose-540-class-options.py [CORPUS] --write --book ID [--families a,b]
    feature-prose-540-class-options.py [CORPUS] --check [--book ID]      no PDF needed; exit 1 unless a rerun changes nothing
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import re
import sys
import tomllib
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


fp = _load("feature_prose_540", "feature-prose-540.py")
rw = _load("rewrite_class_option_powers", "rewrite-class-option-powers.py")

HEADER = ["entry", "feature", "anchor", "shape", "level_import", "level", "verdict", "status", "page", "span_sha256", "note"]
SETTLED = ("draft", "print")


def tsv_file(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / f"feature-prose-540-{book}.class-options.tsv"


def proposals_file(corpus: Path, book: str) -> Path:
    return corpus / "scripts" / f"feature-prose-540-{book}.class-options.proposals.toml"


# ---- the entries ---------------------------------------------------------------------------------

def load_class_options(corpus: Path, book: str | None = None, families: set[str] | None = None) -> list:
    """The class-option entries (the archetype `Entry` type with kind `class_option`), in id order, whose first source is `book`."""
    out = []
    for path in sorted((corpus / "entries").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if 'kind = "class_option"' not in text[:4000]:
            continue
        front, body = fp.split_entry(text)
        data = tomllib.loads(front)
        if (data.get("fields") or {}).get("kind") != "class_option":
            continue
        sources = data.get("sources") or []
        first = sources[0]["publication"] if sources else (data.get("source_ids") or [None])[0]
        if book and first != book:
            continue
        if families and data["id"].split("/")[1] not in families:
            continue
        page = str(sources[0].get("page", "")) if sources else ""
        out.append(fp.Entry(path, data["id"], data["title"], "class_option", front, body, data, first, page, []))
    return out


def shape_of(body: str) -> tuple[str, int]:
    """(shape, powers): `none` when the body holds no import row, `single` for one power, `multi` for several."""
    lines = body.split("\n")
    if not rw.entry_in_scope(lines):
        return "none", 0
    n = len(rw.candidates(rw.parse_blocks(lines), True))
    return ("single" if n == 1 else "multi"), n


def census(entries: list) -> dict:
    """The counts that `--check` and `--compare` report for a set of entries (the 705 are only reported)."""
    shapes = Counter(shape_of(e.body)[0] for e in entries)
    none_by_family = Counter(e.id.split("/")[1] for e in entries if shape_of(e.body)[0] == "none")
    return {"single": shapes["single"], "multi": shapes["multi"], "none": shapes["none"], "none_by_family": none_by_family}


# ---- the comparison ------------------------------------------------------------------------------

def level_of(text: str) -> int | None:
    return fp.lead_level(text.split("\n\n", 1)[0]) if text else None


EXTRA_NAMES: list[str] = []          # the names of every class option of the book: an italic head of a neighbour ends a power's text


def install_split(names: list[str]) -> None:
    """The print reader takes an italic paragraph start as a head only when the entry expects that name. A page of class options sets
    the powers of other entries beside the entry's own (the evolutions are italic heads in one list), so every name of the book is
    expected, and a power's text ends at the next power of the page."""
    EXTRA_NAMES[:] = names
    if not getattr(fp.split_print, "_class_options", False):
        orig = fp.split_print

        def wrapped(section, expected):
            return orig(section, list(expected) + EXTRA_NAMES)
        wrapped._class_options = True
        fp.split_print = wrapped


def compare_one(e, book, bk) -> list[dict]:
    """The rows of one entry: one per import power, from the shared print comparison of the archetype pass."""
    shape, n = shape_of(e.body)
    base = {"entry": e.id, "shape": shape, "page": e.page, "span": "", "note": ""}
    _, feats = fp.parse_import(e.body, set())
    if not e.page.isdigit():
        return [dict(base, feature=f.name, anchor=fp.anchor_of(f.name), verdict="nopage", status="hold", level_import="", level="",
                     note="no page is cited", span_sha256=f.span_sha()) for f in feats]
    page = int(e.page)
    last = page + (3 if shape == "multi" else 1)
    blocks = fp.read_blocks(bk, max(1, page + fp.PAGE_OFFSET[0] - 1), min(last + fp.PAGE_OFFSET[0], max(bk.pages)))
    section = [fp.Para("title", [(e.title, True, False)], page, 0, 20)] + blocks
    res = fp.compare_entry(e, section, bk)
    by_span = {r["span"]: r for r in res["rows"] if r["span"]}
    rows = []
    for f in feats:
        r = by_span.get(f.span_sha())
        if r is None:
            rows.append(dict(base, feature=f.name, anchor=fp.anchor_of(f.name), verdict="missing-head", status="hold", level_import="",
                             level="", note="head not printed on the cited page and the next ones", span_sha256=f.span_sha(), print=""))
            continue
        verdict = {"draft": "agree", "print": "differ", "hold": "hold"}[r["status"]]
        notes = "; ".join(n for n in r["notes"] if n)[:300]
        rows.append(dict(base, feature=f.name, anchor=r["anchor"], verdict=verdict, status=r["status"],
                         level_import=r["level_import"] if r["level_import"] is not None else "",
                         level=level_of(r["print"]) or "", note=notes, span_sha256=f.span_sha(), print=r["print"]))
    return rows


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    title = fp.publication_title(corpus, book)
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    families = set(args.families.split(",")) if args.families else None
    everything = load_class_options(corpus, book)
    names: list[str] = []
    for x in everything:
        if shape_of(x.body)[0] != "none":
            for f in fp.parse_import(x.body, set())[1]:
                names += [f.name, fp.tail_name(f.name)]
    install_split(names)
    entries = [x for x in everything if not families or x.id.split("/")[1] in families]
    cen = census(entries)
    rows, props = [], {}
    for e in entries:
        if shape_of(e.body)[0] == "none":
            continue
        for r in compare_one(e, book, bk):
            if r.get("print"):
                props.setdefault(e.id, {"id": e.id, "feature": []})["feature"].append({"anchor": r["anchor"], "print": r["print"]})
            rows.append(r)
    write_tsv(tsv_file(corpus, book), rows)
    write_props(proposals_file(corpus, book), props)
    print(report(rows, cen))
    return 0


def report(rows: list[dict], cen: dict) -> str:
    verdicts = Counter(r["verdict"] for r in rows)
    per_entry: dict[str, list[dict]] = {}
    for r in rows:
        per_entry.setdefault(r["entry"], []).append(r)
    held = sum(1 for rs in per_entry.values() if any(r["status"] == "hold" for r in rs))
    lines = [f"entries: {cen['single']} single-power, {cen['multi']} multi-power, {cen['none']} without import rows (out of the rewrite)",
             f"powers: {len(rows)}; verdicts: " + ", ".join(f"{k} {v}" for k, v in sorted(verdicts.items())),
             f"entries with a hold: {held} of {len(per_entry)}"]
    if cen["none"]:
        lines.append("without import rows by family: " + ", ".join(f"{k} {v}" for k, v in sorted(cen["none_by_family"].items(), key=lambda kv: -kv[1])))
    return "\n".join(lines)


def write_tsv(path: Path, rows: list[dict]) -> None:
    lines = ["\t".join(HEADER)]
    for r in rows:
        lines.append("\t".join(str(r.get(k, "")).replace("\t", " ").replace("\n", " ") for k in HEADER))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_tsv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").split("\n")
    assert lines[0].split("\t") == HEADER, f"{path}: header is not {HEADER}"
    return [dict(zip(HEADER, ln.split("\t"))) for ln in lines[1:] if ln]


def write_props(path: Path, props: dict) -> None:
    out = ["# The printed text of the powers of the class options that are not converted yet. Generated: never edit by hand.", ""]
    for e in props.values():
        for f in e["feature"]:
            out += ["[[entry]]", f"id = {fp.toml_str(e['id'])}", f"anchor = {fp.toml_str(f['anchor'])}", f"print = {fp.toml_str(f['print'])}", ""]
    path.write_text("\n".join(out), encoding="utf-8")


def read_props(path: Path) -> dict[tuple[str, str], str]:
    if not path.exists():
        return {}
    return {(x["id"], x["anchor"]): x["print"] for x in tomllib.loads(path.read_text(encoding="utf-8")).get("entry", [])}


# ---- writing -------------------------------------------------------------------------------------

def convert_body(e, texts: dict[str, str], levels: dict[str, int | None], anchors: dict[str, str]) -> tuple[str, list[tuple[str, int | None]]]:
    """The converted body and the `features` of a multi-power entry. `texts` maps the span hash of each power to its printed
    text, `levels` to its level, `anchors` to its anchor."""
    lines = e.body.split("\n")
    blocks = rw.parse_blocks(lines)
    cands = rw.candidates(blocks, True)
    if len(cands) == 1 and not any(b.kind == "boundary" and b.text.startswith("#") for b in blocks):
        c = cands[0]
        text = texts[rw.span_sha(blocks[c.start:c.end])]
        keep_before = [b.text for b in blocks[:c.start]]
        keep_after = [b.text for b in blocks[c.end:]]
        return "\n" + "\n\n".join(keep_before + [text] + keep_after).strip("\n") + "\n", []
    out, features, i = [], [], 0
    by_start = {c.start: c for c in cands}
    heading = 1
    while i < len(blocks):
        b = blocks[i]
        if b.kind == "boundary" and b.text.startswith("#"):
            heading = len(b.text) - len(b.text.lstrip("#"))
        c = by_start.get(i)
        if c:
            sha = rw.span_sha(blocks[c.start:c.end])
            name = re.sub(r"[:]$", "", c.name)
            level = levels.get(sha)
            anchor = anchors[sha]
            out.append("#" * (heading + 1 if heading > 1 else 2) + f" {name} {{#{anchor}}}")
            out.append(texts[sha])
            features.append((anchor, level))
            i = c.end
            continue
        out.append(b.text)
        i += 1
    return "\n" + "\n\n".join(out).strip("\n") + "\n", features


def features_front(front: str, features: list[tuple[str, int | None]]) -> str:
    items = "".join("  { anchor = \"%s\"%s },\n" % (a, f", level = {l}" if l else "") for a, l in features)
    return re.sub(r"(^group = \"[^\"]*\"\n)", lambda m: m.group(1) + "features = [\n" + items + "]\n", front, count=1, flags=re.M)


def run_write(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    families = set(args.families.split(",")) if args.families else None
    rows = read_tsv(tsv_file(corpus, book))
    props = read_props(proposals_file(corpus, book))
    by_entry: dict[str, list[dict]] = {}
    for r in rows:
        by_entry.setdefault(r["entry"], []).append(r)
    converted = 0
    for e in load_class_options(corpus, book, families):
        mine = by_entry.get(e.id)
        if not mine or any(r["status"] not in SETTLED for r in mine):
            continue
        blocks = rw.parse_blocks(e.body.split("\n"))
        texts, levels, anchors = {}, {}, {}
        for r in mine:
            texts[r["span_sha256"]] = props[(e.id, r["anchor"])]
            levels[r["span_sha256"]] = int(r["level"]) if r["level"] else None
            anchors[r["span_sha256"]] = r["anchor"]
        body, features = convert_body(e, texts, levels, anchors)
        front = features_front(e.front, features) if features else e.front
        e.path.write_text("+++\n" + front.strip("\n") + "\n+++\n" + body, encoding="utf-8")
        converted += 1
    print(f"converted {converted} entries")
    return 0


# ---- the check -----------------------------------------------------------------------------------

def run_check(args) -> int:
    corpus = Path(args.corpus).resolve()
    books = [args.book] if args.book else sorted({p.name[len("feature-prose-540-"):-len(".class-options.tsv")]
                                                   for p in (corpus / "scripts").glob("feature-prose-540-*.class-options.tsv")})
    errors: list[str] = []
    for book in books:
        rows = read_tsv(tsv_file(corpus, book))
        entries = {e.id: e for e in load_class_options(corpus, book)}
        by_entry: dict[str, list[dict]] = {}
        for r in rows:
            by_entry.setdefault(r["entry"], []).append(r)
        cen = census(list(entries.values()))
        pending = 0
        for eid, e in entries.items():
            shape, _ = shape_of(e.body)
            mine = by_entry.get(eid)
            if shape == "none":
                if mine and any(r["status"] not in SETTLED for r in mine):
                    errors.append(f"{eid}: no import row is left, but the table has an unsettled row")
                continue
            if not mine:
                pending += 1                  # a part of the book that no batch has compared yet: reported, not an error
                continue
            have = {r["span_sha256"] for r in mine}
            _, feats = fp.parse_import(e.body, set())
            if have != {f.span_sha() for f in feats}:
                errors.append(f"{eid}: the table is stale (the spans of the import rows changed)")
        print(f"{book}: {len(entries)} class options: {cen['single']} single-power and {cen['multi']} multi-power not converted, "
              f"{cen['none']} without import rows (reported, not rewritten); {pending} with import rows not compared yet")
    for line in errors:
        print("error:", line)
    return 1 if errors else 0


# ---- self-test -----------------------------------------------------------------------------------

def self_test() -> int:
    ok, bad = 0, []

    def eq(a, b, what):
        nonlocal ok
        if a == b:
            ok += 1
        else:
            bad.append(f"{what}: {a!r} != {b!r}")

    single = "\n**Animal Fury (Ex)**\n\n**Ability:** A bite attack.\n\n**Special:** A grapple.\n"
    multi = ("\n**Deities**\n\n**Details:** Gorum.\n\n### Revelations\n\nAn oracle can choose from the following.\n\n"
             "**Battlecry (Ex)**\n\n**Standard:** A cry.\n\n**Usage:** 1 time/day\n\n**At 10th level,** more.\n\n"
             "**Clarity (Ex)**\n\n**Immediate:** A reroll.\n")
    none = "\nA kinetic talent prints a stat line.\n\nBurn: 1\n"
    eq(shape_of(single), ("single", 1), "a single-power option")
    eq(shape_of(multi), ("multi", 2), "a multi-power option under a section")
    eq(shape_of(none), ("none", 0), "an option without import rows")
    eq(shape_of("\n## Battlecry (Ex) {#battlecry}\n\nAt 1st level, a cry.\n")[0], "none", "a converted entry has no import row")

    def sha(body, i):
        blocks = rw.parse_blocks(body.split("\n"))
        c = rw.candidates(blocks, True)[i]
        return rw.span_sha(blocks[c.start:c.end])

    class E:                              # the fields `convert_body` reads
        body = single
    body, feats = convert_body(E, {sha(single, 0): "At 1st level, a bite."}, {}, {})
    eq(body.strip(), "At 1st level, a bite.", "a single-power body is the printed paragraphs, no head, no features")
    eq(feats, [], "a single-power option gets no `features`")
    E.body = multi
    texts = {sha(multi, 0): "A cry that all allies hear.", sha(multi, 1): "At 7th level, a reroll."}
    levels = {sha(multi, 0): None, sha(multi, 1): 7}
    anchors = {sha(multi, 0): "battlecry", sha(multi, 1): "clarity"}
    body, feats = convert_body(E, texts, levels, anchors)
    eq("#### Battlecry (Ex) {#battlecry}" in body and "#### Clarity (Ex) {#clarity}" in body, True, "heads are one level below the section heading")
    eq(feats, [("battlecry", None), ("clarity", 7)], "the features of a multi-power option, with a level only when print gives it")
    eq("**Deities**" in body and "### Revelations" in body, True, "the blocks that are no power stay")
    eq(rw.entry_in_scope(body.split("\n")), False, "a converted body has no import row")
    front = 'id = "ref/mystery/battle"\n[fields]\nkind = "class_option"\ngroup = "oracle-mystery"\n'
    eq(features_front(front, feats).split("\n")[4:8], ["features = [", '  { anchor = "battlecry" },', '  { anchor = "clarity", level = 7 },', "]"],
       "`features` follow `group`")
    eq(level_of("At 7th level, a reroll."), 7, "the level of a printed lead")
    eq(level_of("Once per day, a reroll."), None, "no printed lead, no level")
    for line in bad:
        print("FAIL", line)
    print(f"self-test: {ok} checks passed" if not bad else f"self-test: {len(bad)} failures")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(HERE.parent))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--book")
    ap.add_argument("--families")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.compare:
        return run_compare(args)
    if args.write:
        return run_write(args)
    if args.check:
        return run_check(args)
    ap.error("one of --self-test, --compare, --write, --check")


if __name__ == "__main__":
    sys.exit(main())
