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
fp.LOOSE_ITEMS["on"] = True      # ruling 60: the loose reading of a prerequisite item (every word, any order, a sentence with "must" or "only available")

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


INVERTED_HEAD = re.compile(r"^(.+?),\s*(Lesser|Greater|Improved|Mass)(\s*\([A-Za-z]{2}\))?\s*:?$")


VARIANT_FIRST = re.compile(r"^(Lesser|Greater|Improved|Mass) ")


def inverted(name: str) -> str:
    m = re.match(r"^(Lesser|Greater|Improved|Mass) (.+?)(\s*\([A-Za-z]{2}\))?$", name)
    return f"{m.group(2)}, {m.group(1)}{m.group(3) or ''}" if m else name


def install_split(names: list[str]) -> None:
    """The print reader takes an italic paragraph start as a head only when the entry expects that name. A page of class options sets
    the powers of other entries beside the entry's own (the evolutions are italic heads in one list), so every name of the book is
    expected, and a power's text ends at the next power of the page."""
    EXTRA_NAMES[:] = list(names) + [inverted(n) for n in names if VARIANT_FIRST.match(n)]      # print sets the variant behind the name, in italics
    if not getattr(fp.split_print, "_class_options", False):
        orig = fp.split_print

        def wrapped(section, expected):
            # a printed section heading ("2-Point Evolutions", "Base Forms") ends the text of the power above it: it stands as a head of its own
            section = section[:1] + [fp.Para("para", [(q.plain().strip(), True, False)], q.page, q.col, 0) if q.kind == "title" else q
                                     for q in section[1:]]
            opening, feats = orig(section, list(expected) + EXTRA_NAMES)
            for f in feats:                      # print sets "Beast Totem, Greater (Su)" for the corpus title "Greater Beast Totem"
                m = INVERTED_HEAD.match(f.head)
                if m:
                    f.head = f"{m.group(2)} {m.group(1)}{m.group(3) or ''}"
            return opening, feats
        wrapped._class_options = True
        fp.split_print = wrapped


def reviewed_spans(corpus: Path) -> dict[tuple[str, str], str]:
    """The 423 hand replacements of #537 as (entry id, span hash) -> print reference: print-reviewed text in row form. A power whose
    current span still hashes to a resolution's `span_sha256` has a reviewed source; its verdict is `reviewed-537`, and the wording is
    print's (a resolution never overrides the print compare)."""
    out: dict[tuple[str, str], str] = {}
    for r in rw.load_resolutions(corpus / rw.RESOLUTIONS_FILE).values():
        out[(r.id, r.span_sha256)] = r.print                                                    # the span as the import had it
        out[(r.id, hashlib.sha256(rw.resolution_power_text(r).encode()).hexdigest())] = r.print   # the span once the resolution is applied (the corpus today)
    return out


REVIEWED: dict[tuple[str, str], str] = {}


def powers_of(e) -> list[tuple[str, str]]:
    """The powers of an entry as (name, span hash): the candidates of `rewrite-class-option-powers.py` (a bold name that stands over
    import rows), in body order, with its hash of the span. A bold name over other rows (Deities, Bonus Spells) is no power."""
    blocks = rw.parse_blocks(e.body.split("\n"))
    return [(re.sub(r":$", "", c.name), rw.span_sha(blocks[c.start:c.end])) for c in rw.candidates(blocks, True)]


HEADING_FAMILIES = {"evolution"}     # ruling 61: an evolution opens with the printed sentence of its group heading ("2-Point Evolutions: The following ...")


def heading_blocks(bk, page: int) -> list:
    """The print from three pages before the cited one to the next: a group of evolutions runs over pages, its heading stands at the start."""
    return fp.read_blocks(bk, max(1, page + fp.PAGE_OFFSET[0] - 3), min(page + 1 + fp.PAGE_OFFSET[0], max(bk.pages)))


def group_heading(e, blocks) -> tuple[str, int] | None:
    """The group heading of a power as one paragraph, "2-Point Evolutions: The following evolutions cost 2 points from the eidolon's
    evolution pool.", and the printed page it stands on: the last title above the head of the entry, and the paragraph under it when that
    starts "The following"."""
    want = fp.namekey(e.title)
    at = next((i for i, p in enumerate(blocks) if p.kind == "para" and (c := fp.head_candidate(p)) and fp.namekey(c[0]) == want), None)
    if at is None:
        return None
    ti = next((i for i in range(at - 1, -1, -1) if blocks[i].kind == "title"), None)
    if ti is None or ti + 1 >= at:
        return None
    para = blocks[ti + 1]
    text, _, _ = fp.print_md(fp.PrintFeature("", [para.runs], para.page, False), [], set())
    text = text.strip()
    if not text.startswith("The following"):
        return None
    return f"{re.sub(chr(10), ' ', blocks[ti].plain()).strip()}: {text}", blocks[ti].page


def compare_one(e, book, bk) -> list[dict]:
    """The rows of one entry: one per power, from the shared print comparison of the archetype pass."""
    shape, n = shape_of(e.body)
    base = {"entry": e.id, "shape": shape, "page": e.page, "span": "", "note": ""}
    powers = powers_of(e)
    _, feats = fp.parse_import(e.body, set())
    by_name: dict[str, list] = {}
    for f in feats:
        by_name.setdefault(re.sub(r":$", "", f.name), []).append(f)
    if not e.page.isdigit():
        return [dict(base, feature=n_, anchor=fp.anchor_of(n_), verdict="nopage", status="hold", level_import="", level="",
                     note="no page is cited", span_sha256=sha) for n_, sha in powers]
    page = int(e.page)
    last = page + (3 if shape == "multi" else 1)
    blocks = fp.read_blocks(bk, max(1, page + fp.PAGE_OFFSET[0] - 1), min(last + fp.PAGE_OFFSET[0], max(bk.pages)))
    section = [fp.Para("title", [(e.title, True, False)], page, 0, 20)] + blocks
    res = fp.compare_entry(e, section, bk)
    by_span = {r["span"]: r for r in res["rows"] if r["span"]}
    rows, seen = [], Counter()
    for name, sha in powers:
        seen[name] += 1
        f = by_name.get(name, [None] * seen[name])[seen[name] - 1] if name in by_name else None
        r = by_span.get(f.span_sha()) if f is not None else None
        if r is None:
            rows.append(dict(base, feature=name, anchor=fp.anchor_of(name), verdict="missing-head", status="hold", level_import="",
                             level="", note="head not printed on the cited page and the next ones", span_sha256=sha, print=""))
            continue
        verdict = {"draft": "agree", "print": "differ", "hold": "hold"}[r["status"]]
        if (e.id, sha) in REVIEWED:
            verdict = "reviewed-537" if verdict != "hold" else "hold"          # a hold stays a hold: the resolution is a source, not an answer
        note_r = f"resolution of #537: {REVIEWED[(e.id, sha)]}" if (e.id, sha) in REVIEWED else ""
        notes = "; ".join([n_ for n_ in r["notes"] if n_] + ([note_r] if note_r else []))[:300]
        status, printed = r["status"], r["print"]
        if shape == "single" and e.id.split("/")[1] in HEADING_FAMILIES:
            gh = group_heading(e, heading_blocks(bk, page))
            if gh is None:
                notes = "; ".join([n_ for n_ in [notes, "no group heading found above the head"] if n_])[:300]
                status = "hold"
            elif gh[1] > page:
                notes = "; ".join([n_ for n_ in [notes, f"the group heading is on p. {gh[1]}, after the cited p. {page}"] if n_])[:300]
                status = "hold"
            else:
                printed = gh[0] + "\n\n" + printed
                if gh[1] < page:
                    base = dict(base, page=f"{gh[1]}-{page}")           # the sentence is on the page before: the entry cites both (ruling 61)
        rows.append(dict(base, feature=name, anchor=r["anchor"], verdict=verdict, status=status,
                         level_import=r["level_import"] if r["level_import"] is not None else "",
                         level=level_of(r["print"]) or "", note=notes, span_sha256=sha, print=printed))
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
        names.append(x.title)                      # a converted option has no import row left, but its italic head still ends the text above it
        if shape_of(x.body)[0] != "none":
            for f in fp.parse_import(x.body, set())[1]:
                names += [f.name, fp.tail_name(f.name)]
    install_split(names)
    REVIEWED.update(reviewed_spans(corpus))
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
    reach = sum(1 for r in rows if "resolution of #537" in r.get("note", ""))
    lines = [f"resolutions of #537 that reach these powers: {reach}",
             f"entries: {cen['single']} single-power, {cen['multi']} multi-power, {cen['none']} without import rows (out of the rewrite)",
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


def with_page(text: str, page: str) -> str:
    """The first `[[sources]]` page row of the entry file set to `page`."""
    return re.sub(r'(\[\[sources\]\]\n(?:[^\n]*\n)*?page = )"[^"]*"', lambda m: m.group(1) + f'"{page}"', text, count=1)


def run_headings(args) -> int:
    """Ruling 61 for the entries that are converted already: each evolution entry opens with the printed sentence of its group heading
    (it is idempotent: an entry that has the sentence is left). An entry whose heading is on another page than the cited one is reported."""
    corpus = Path(args.corpus).resolve()
    book = args.book
    title = fp.publication_title(corpus, book)
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    done = skipped = 0
    for e in load_class_options(corpus, book):
        if e.id.split("/")[1] not in HEADING_FAMILIES or shape_of(e.body)[0] != "none" or not e.page.isdigit():
            continue
        page = int(e.page)
        gh = group_heading(e, heading_blocks(bk, page))
        if gh is None or gh[1] > page:
            print(f"  {e.id}: " + ("no group heading found above the head" if gh is None else f"the group heading is on p. {gh[1]}, after the cited p. {page}"))
            skipped += 1
            continue
        if gh[0] in e.body:
            continue
        body = "\n" + gh[0] + "\n\n" + e.body.lstrip("\n")
        text = e.path.read_text(encoding="utf-8").replace(e.body, body, 1)
        if gh[1] < page:
            text = with_page(text, f"{gh[1]}-{page}")           # the sentence is on the page before: the entry cites both (ruling 61)
        e.path.write_text(text, encoding="utf-8")
        done += 1
    print(f"group headings: {done} entries changed, {skipped} not changed")
    return 0


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
        if mine[0]["page"] and mine[0]["page"] != e.page:
            front = with_page(front, mine[0]["page"])
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
            if have != {sha for _, sha in powers_of(e)}:
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

    eq(inverted("Greater Beast Totem (Su)"), "Beast Totem, Greater (Su)", "print sets the variant behind the name")
    eq(inverted("Beast Totem"), "Beast Totem", "a name without a variant stays")
    eq(INVERTED_HEAD.match("Beast Totem, Greater (Su)").groups(), ("Beast Totem", "Greater", " (Su)"), "the inverted head is read")
    P = fp.Para
    E = type("E", (), {"title": "Wing Buffet"})()
    blk = [P("title", [("1-Point Evolutions", True, False)], 60, 0, 18),
           P("para", [("The following evolutions cost 1 point from the eidolon\u2019s evolution pool.", False, False)], 60, 0),
           P("para", [("Bite (Ex)", True, False), (": An eidolon bites.", False, False)], 60, 0),
           P("para", [("Wing Buffet (Ex)", True, False), (": An eidolon buffets.", False, False)], 61, 1),
           P("title", [("2-Point Evolutions", True, False)], 61, 1, 18),
           P("para", [("The following evolutions cost 2 points from the eidolon\u2019s evolution pool.", False, False)], 61, 1)]
    gh = group_heading(E, blk)
    eq(gh and gh[0], "1-Point Evolutions: The following evolutions cost 1 point from the eidolon's evolution pool.", "ruling 61: the heading above the head and its sentence")
    eq(gh and gh[1], 60, "ruling 61: the page of the heading")
    eq(group_heading(type("E", (), {"title": "Nothing"})(), blk), None, "ruling 61: a head that is not printed has no heading")
    eq(group_heading(type("E", (), {"title": "Bite"})(), blk[2:]), None, "ruling 61: no title above the head, no heading")
    eq(with_page('[[sources]]\npublication = "x"\npage = "62"\n\n[fields]\n', "61-62"), '[[sources]]\npublication = "x"\npage = "61-62"\n\n[fields]\n', "ruling 61: the page row becomes a range")
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
    rows = [{"entry": "ref/x/a", "verdict": "agree", "status": "draft", "note": ""}, {"entry": "ref/x/b", "verdict": "hold", "status": "hold", "note": "resolution of #537: Book p. 1"}]
    out = report(rows, {"single": 2, "multi": 0, "none": 1, "none_by_family": Counter({"talent": 1})})
    eq("entries with a hold: 1 of 2" in out and "reach these powers: 1" in out and "talent 1" in out, True, "the report counts holds, resolutions and the options without import rows")
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
    ap.add_argument("--headings", action="store_true", help="ruling 61: put the printed group heading in the converted evolution entries")
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
    if args.headings:
        return run_headings(args)
    if args.write:
        return run_write(args)
    if args.check:
        return run_check(args)
    ap.error("one of --self-test, --compare, --write, --check")


if __name__ == "__main__":
    sys.exit(main())
