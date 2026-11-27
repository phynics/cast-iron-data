#!/usr/bin/env python3
"""Base classes as printed prose (phynics/cast-iron#540): the compare of the class features of a `kind = "class"` entry against print.

A companion of `feature-prose-540.py` and `feature-prose-540-class-options.py`, which it loads. This first step is a REPORT: it writes no entry and no
file. It reads each base class of a book the way the archetype pass reads an archetype, so that the verdicts and holds can be counted before a
writer is built (the pilot on the seven Advanced Player's Guide classes, phynics/cast-iron#540).

What is read
------------
- The **region** of a class is its feature heads: the lines from the first `####` head to the next `###` heading (the class table, the spells-known
  table, the alternate capstones and the archetypes are outside it and stay as they are). No head, no anchor and no key moves: only the text under a
  head is compared. Each `####` head is read as the bold name of a feature (`headings_as_names` of the class-option script).
- The **window** of print is the section "Class Features" of the class: from that title to the next title that is not the title of a table.
  A class table is set in the middle of the text in print, and a table title does not end the window.
- A feature has its **level** from the class table (`class_table_levels` of the archetype script), which is what a class feature's trades point at.

Usage
-----
    feature-prose-540-classes.py --self-test
    feature-prose-540-classes.py [CORPUS] --compare --book ID [--classes alchemist,cavalier] --books DIR --cache DIR
"""

from __future__ import annotations

import argparse
import dataclasses
import importlib.util
import os
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


co = _load("feature_prose_540_class_options", "feature-prose-540-class-options.py")
fp = co.fp


def feature_region(body: str) -> tuple[int, int] | None:
    """(first line, end line) of the class features of a base-class body: from the first `####` head to the next `###` or higher heading."""
    lines = body.split("\n")
    first = next((i for i, ln in enumerate(lines) if ln.startswith("#### ")), None)
    if first is None:
        return None
    end = next((i for i in range(first, len(lines)) if re.match(r"^#{1,3} ", lines[i])), len(lines))
    return first, end


def window(blocks: list) -> list:
    """The blocks of the section "Class Features" of the class: after that title, up to the next title that is not the title of a table."""
    at = next((i for i, b in enumerate(blocks) if b.kind == "title" and fp.squash(b.plain()) == "classfeatures"), None)
    if at is None:
        return []
    out = []
    for b in blocks[at + 1:]:
        # a sidebar or a table title is set larger (24) than a subsection title (18): the section ends at the next subsection or class title
        if b.kind == "title" and not b.plain().strip().lower().startswith("table") and (b.size == 18 or b.size >= 38):
            break
        out.append(b)
    return out


HEAD_RE = re.compile(r"^#### (.*?)(?: \{#([^}]+)\})?\s*$")
WRITE_FEATURES = False        # the `features` of a class (anchor and level from the class table): off until the app has answered (owner call 5); bodies are written without
# The printed name of a head that the corpus names otherwise and that no plural or tag rule reaches: (class entry, key) -> print's head
PRINT_NAMES: dict[tuple[str, str], str] = {("ref/class/antipaladin", "channel-energy"): "Channel Negative Energy (Su)"}


def stem(name: str) -> str:
    """A head without its tag, in lower case, the last word in the singular ("Weapon and Armor Proficiencies" and "... Proficiency" are one head)."""
    s = fp.ABILITY_TAG.sub("", name).strip().rstrip(":").strip().lower()
    s = re.sub(r"ies$", "y", s)
    return re.sub(r"(?<!s)s$", "", s)


def corpus_heads(lines: list[str], region: tuple[int, int]) -> list[tuple[int, str, str]]:
    """(line, head text, key) of each `####` head of the region."""
    out = []
    for i in range(region[0], region[1]):
        m = HEAD_RE.match(lines[i])
        if m:
            out.append((i, m.group(1), m.group(2) or fp.slugify(fp.ABILITY_TAG.sub("", m.group(1)))))
    return out


def option_title_keys(corpus: Path) -> dict[str, list[tuple[str, str]]]:
    """namekey -> [(entry id, group)] of every class option: an item of an option list in print (a curse, a mystery) that has its own entry is linked.
    Titles repeat across groups ("Tongues" is an oracle curse and a shaman hex), so the group of the list decides (`pick_options`)."""
    out: dict[str, list[tuple[str, str]]] = {}
    for x in co.load_class_options(corpus):
        out.setdefault(fp.namekey(x.title), []).append((x.id, (x.data.get("fields") or {}).get("group", "")))
    return out


def pick_options(items: list[tuple[str, list[tuple[str, str]]]]) -> list[tuple[str, str]]:
    """The links of one option list: (name, entry id), from the group that most of its items belong to."""
    groups = Counter(g for _, cands in items for _, g in cands)
    group = groups.most_common(1)[0][0] if groups else ""
    out = []
    for name, cands in items:
        pick = next((i for i, g in cands if g == group), cands[0][0] if cands else None)
        if pick:
            out.append((name, pick))
    return out


def compare_class(corpus: Path, e, bk, cache: dict, options: dict | None = None) -> dict:
    """The comparison of one base class, as a plan for the writer: one item per `####` head of the class (its key, print's head text, print's text and
    status), the print heads that the corpus has no head for (`extra`), the heads that print does not have (`missing`), and the items of option lists
    (owner call 4: an item that has an entry of its own is a link, the feature keeps print's lead-in)."""
    region = feature_region(e.body)
    if region is None or not e.page.isdigit():
        return {"items": [], "extra": [], "missing": [], "window": 0, "problems": ["no `####` head, or no page"], "region": None}
    lines = e.body.split("\n")
    heads = corpus_heads(lines, region)
    page = int(e.page)
    blocks = fp.read_blocks(bk, page, min(page + 12, max(bk.pages)))
    win = window(blocks)
    title = fp.Para("title", [(e.title, True, False)], page, 0, 20)
    _, pfs = fp.split_print([title] + win, [h for _, h, _ in heads])
    printed = {fp.namekey(fp.head_text(f.head)): fp.head_text(f.head) for f in pfs}
    names = {}                                                    # key -> the name that the pseudo body gives the head
    for _, text, key in heads:
        want = PRINT_NAMES.get((e.id, key))
        if want is None and fp.namekey(text) not in printed:
            want = next((ph for ph in printed.values() if stem(ph) == stem(text)), None)       # "Proficiency" for "Proficiencies"
        names[key] = want or text
    pseudo_lines = []
    for ln in lines[region[0]:region[1]]:
        m = HEAD_RE.match(ln)
        pseudo_lines.append(f"**{names[m.group(2) or fp.slugify(fp.ABILITY_TAG.sub('', m.group(1)))]}**" if m else ln)
    pseudo = "\n".join(pseudo_lines)
    _, feats = fp.parse_import(pseudo, set())
    e2 = dataclasses.replace(e, body=pseudo)
    res = fp.compare_entry(e2, [title] + win, bk)
    by_span = {r["span"]: r for r in res["rows"] if r["span"]}
    items, missing = [], []
    for (line, text, key), f in zip(heads, feats):
        r = by_span.get(f.span_sha())
        if r is None or "head not printed" in r["notes"]:
            missing.append(key)
            items.append({"key": key, "line": line, "head": text, "print": "", "status": "hold", "notes": ["head not printed"]})
        else:
            items.append({"key": key, "line": line, "head": r["head"], "print": r["print"], "status": r["status"], "notes": list(r["notes"])})
    extra, options = [], options or {}                          # the items of an option list are collected, then linked from one group
    last = None
    for r in res["rows"]:
        if r["span"] and r["span"] in {f.span_sha() for f in feats}:
            last = r
            continue
        opt = options.get(fp.namekey(r["head"]))
        if opt and last is not None:                                # an item of an option list that has its own entry: a link under the feature
            it = next((x for x in items if x["head"] == last["head"]), None)
            if it is not None:
                it.setdefault("candidates", []).append((r["head"], opt))
            continue
        if "head printed, not in the import" in " ".join(r["notes"]):
            extra.append(r["head"])
    for it in items:
        if it.get("candidates"):
            it["links"] = pick_options(it.pop("candidates"))
    return {"items": items, "extra": extra, "missing": missing, "window": len(win), "problems": res["problems"], "region": region,
            "levels": fp.class_table_levels(corpus, e.id, cache)}


def feature_text(it: dict) -> str:
    """The text under a head: print's paragraphs; the items of an option list that have entries of their own are links after the lead-in."""
    text = it["print"].strip()
    if it.get("links"):
        text += "\n\n" + "\n".join(f"- [{name}]({eid})" for name, eid in it["links"])
    return text


def settled(plan: dict) -> bool:
    return bool(plan["items"]) and not plan["extra"] and not plan["missing"] and all(i["status"] in ("print", "draft") for i in plan["items"])


def converted_body(body: str, plan: dict) -> str:
    """The class body with the text under each head replaced by print's, the head as print has it with the key written out, the class table and every
    other line as they were (rule 3 of AGENTS.md: no key moves)."""
    lines = body.split("\n")
    a, b = plan["region"]
    out = []
    for it in plan["items"]:
        out += [f"#### {it['head']} {{#{it['key']}}}", "", feature_text(it), ""]
    return "\n".join(lines[:a] + out + lines[b:]) if out else body


def run_compare(args) -> int:
    corpus = Path(args.corpus).resolve()
    book = args.book
    fp.configure_book(book)
    pdf = fp.find_pdf(Path(args.books), fp.publication_title(corpus, book))
    if not pdf:
        raise SystemExit(f"no copy of the book {book} under {args.books}")
    bk = fp.load_book(fp.book_xml(pdf, Path(args.cache)))
    co.install_split([x.title for x in co.load_class_options(corpus)])
    options = option_title_keys(corpus)
    wanted = set(args.classes.split(",")) if args.classes else None
    total, cache, written = Counter(), {}, 0
    for e in co.load_entries(corpus, "class", book):
        if not e.id.startswith("ref/class/") or (wanted and e.id.rsplit("/", 1)[1] not in wanted):
            continue
        plan = compare_class(corpus, e, bk, cache, options)
        c = Counter(x["status"] for x in plan["items"])
        total.update(c)
        links = sum(len(x.get("links", [])) for x in plan["items"])
        print(f"{e.id}: window {plan['window']} blocks; " + ", ".join(f"{k} {v}" for k, v in sorted(c.items()))
              + f"; heads not printed {len(plan['missing'])}; print heads not in the corpus {len(plan['extra'])}" + (f"; option links {links}" if links else ""))
        for x in plan["items"]:
            if x["status"] == "hold":
                print(f"    hold {x['head'][:34]}: {(x['notes'] or [''])[0][:100]}")
        if plan["extra"]:
            print("    print heads not in the corpus: " + ", ".join(plan["extra"][:8]))
        if args.write and settled(plan):
            co.write_atomic(e.path, "+++\n" + e.front.strip("\n") + "\n+++\n" + converted_body(e.body, plan))
            written += 1
            print("    written")
    print("total: " + ", ".join(f"{k} {v}" for k, v in sorted(total.items())) + (f"; {written} classes written" if args.write else ""))
    if args.write and written and args.checker:
        import subprocess
        subprocess.run([args.checker, "fmt", str(corpus)], check=True)
    return 0


def self_test() -> int:
    ok, bad = 0, []

    def eq(a, b, what):
        nonlocal ok
        if a == b:
            ok += 1
        else:
            bad.append(f"{what}: {a!r} != {b!r}")

    body = "Intro.\n\n### Class Features and Spells Per Day\n\n|Level|\n| --- |\n|1st|\n\n#### Spells {#spells}\n\n**Ability:** A.\n\n#### Mystery {#mystery}\n\nB.\n\n### Alternate Capstones\n\nC.\n"
    r = feature_region(body)
    eq(body.split("\n")[r[0]:r[1]][0], "#### Spells {#spells}", "the region starts at the first head")
    eq("### Alternate Capstones" in "\n".join(body.split("\n")[r[0]:r[1]]), False, "the region ends at the next ### heading")
    eq(feature_region("No heads here.\n"), None, "a class with no head has no region")
    eq((stem("Weapon and Armor Proficiencies"), stem("Weapon and Armor Proficiency")), ("weapon and armor proficiency",) * 2, "a head in the plural and in the singular is one head")
    eq(stem("Oracle's Curse (Ex)"), "oracle's curse", "a tag is not part of the stem")
    cl = "Intro.\n\n### Class Features\n\n|L|\n\n#### Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}\n\n**Weapons:** Simple.\n\n#### Mystery {#mystery}\n\nOld.\n\n### Alternate Capstones\n\nC.\n"
    reg = feature_region(cl)
    eq([(h, k) for _, h, k in corpus_heads(cl.split("\n"), reg)], [("Weapon and Armor Proficiencies", "weapon-and-armor-proficiencies"), ("Mystery", "mystery")], "the heads of the region with their keys")
    plan = {"region": reg, "items": [{"key": "weapon-and-armor-proficiencies", "head": "Weapon and Armor Proficiency", "print": "Oracles are proficient with simple weapons.", "status": "print"},
                                     {"key": "mystery", "head": "Mystery", "print": "Each oracle draws.", "status": "print", "links": [("Clouded Vision", "ref/oraclecurse/clouded-vision")]}],
            "extra": [], "missing": []}
    nb = converted_body(cl, plan)
    eq(("#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}" in nb, "**Weapons:**" in nb, "- [Clouded Vision](ref/oraclecurse/clouded-vision)" in nb, "### Alternate Capstones" in nb),
       (True, False, True, True), "owner calls 1, 2 and 4: print's head with the old key, no invented row, an option item as a link, the rest of the class as it was")
    eq("\n\n### Alternate Capstones" in nb, True, "a blank line stands before the next heading")
    eq(co.heading_keys(cl) <= co.heading_keys(nb), True, "no heading key of the class moves")
    eq(pick_options([("Clouded Vision", [("ref/oraclecurse/clouded-vision", "oracle-curse")]), ("Tongues", [("ref/shamanhex/tongues", "shaman-hex"), ("ref/oraclecurse/tongues", "oracle-curse")]),
                     ("Lame", [("ref/oraclecurse/lame", "oracle-curse")])]),
       [("Clouded Vision", "ref/oraclecurse/clouded-vision"), ("Tongues", "ref/oraclecurse/tongues"), ("Lame", "ref/oraclecurse/lame")], "owner call 4: a title that two groups share is linked from the group of the list")
    eq((settled(plan), settled(dict(plan, extra=["X"])), settled(dict(plan, missing=["mystery"]))), (True, False, False), "a class is written all or nothing")
    P = fp.Para
    blocks = [P("title", [("Oracle", True, False)], 42, 1, 38), P("title", [("Class Features", True, False)], 42, 1, 18),
              P("para", [("Spells: A.", False, False)], 42, 1), P("title", [("Table 2–5: Oracle", True, False)], 44, 0, 24), P("para", [("1st +0", False, False)], 44, 0),
              P("para", [("Orisons: B.", False, False)], 45, 0), P("title", [("Alternate Capstones", True, False)], 46, 0, 18), P("para", [("Late.", False, False)], 46, 0)]
    eq([b.plain() for b in window(blocks)], ["Spells: A.", "Table 2–5: Oracle", "1st +0", "Orisons: B."], "the window runs over a table and ends at the next title")
    side = blocks[:3] + [P("title", [("Fall From Grace", True, False)], 46, 0, 24), P("para", [("Sidebar.", False, False)], 46, 0), P("title", [("Ex-Antipaladins", True, False)], 46, 0, 18)]
    eq([b.plain() for b in window(side)], ["Spells: A.", "Fall From Grace", "Sidebar."], "a sidebar title (larger) does not end the window, the next subsection does")
    eq(window([blocks[0]]), [], "a page without the Class Features title has no window")
    for line in bad:
        print("FAIL", line)
    print(f"self-test: {ok} checks passed" if not bad else f"self-test: {len(bad)} failures")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(HERE.parent))
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--compare", action="store_true")
    ap.add_argument("--book")
    ap.add_argument("--classes")
    ap.add_argument("--books")
    ap.add_argument("--cache")
    ap.add_argument("--write", action="store_true", help="write the classes whose items are all settled (the others are reported)")
    ap.add_argument("--checker", help="the cast-iron-corpus binary: `fmt` runs after a write")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.compare:
        return run_compare(args)
    ap.error("one of --self-test, --compare")


if __name__ == "__main__":
    sys.exit(main())
