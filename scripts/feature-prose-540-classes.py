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
import difflib
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


NUMERIC = re.compile(r"^(?:[+\-\u2013\u2014]?\d+(?:/\d+)?(?:st|nd|rd|th)?|[\u2014\u2013-]|\+\d+)[,.]?$")


def is_table_para(text: str) -> bool:
    """A paragraph that is the cells of a class table: most of its words are numbers, dashes or ordinals, or it is the header row of the table (Fort, Ref and
    Will saves). Print sets the class table in the middle of the text and the reader makes paragraphs of the cells."""
    toks = text.split()
    if len(toks) >= 4 and re.search(r"\bFort\b.*\bRef\b.*\bWill\b", text):
        return True
    return len(toks) >= 5 and sum(bool(NUMERIC.match(x)) for x in toks) / len(toks) >= 0.5


def section_behind(blocks: list, win: list, lacking: set[str]) -> list:
    """The sections that follow the class features in print under a title that is a head of the corpus (`lacking`): the title and its blocks up to the next
    title. The cells of a table in them are left out as in the window."""
    last = blocks.index(win[-1]) if win and win[-1] in blocks else 0
    out: list = []
    on = False
    for b in blocks[last + 1:]:
        if b.kind == "title" and not b.plain().strip().lower().startswith("table"):
            on = fp.squash(b.plain()) in lacking
            if on:
                out.append(b)
            continue
        if on and not (b.kind == "para" and is_table_para(b.plain())):
            out.append(b)
    return out


def prose_after_cells(text: str) -> str:
    """The text of a sentence that shares a paragraph with the cells of a table: after the leading numbers ("6 6 6 6 due to encumbrance. At 5th level, ...") or
    after the last cell of a table ("... 6 6 6 4 \u2014 with the summoner. Effects that cause death ..."), when it holds a sentence (a full stop), else
    nothing (a row of a table with words in its cells)."""
    toks = text.split()
    cands = []
    i = 0
    while i < len(toks) and NUMERIC.match(toks[i]):
        i += 1
    if i > 0:
        cands.append(" ".join(toks[i:]))
    k = max((n for n, x in enumerate(toks) if NUMERIC.match(x)), default=-1)
    if 0 <= k < len(toks) - 1:
        cands.append(" ".join(toks[k + 1:]))
    for prose in cands:
        if len(prose.split()) >= 4 and re.search(r"[a-z]{3}[^.]*\.\s", prose + " ") and not re.search(r"\b(?:Fort|Ref|Will)\b", prose):
            return prose
    return ""


TABLE_RUN = re.compile(r"^\s*(?:spells|extracts|formulae)\s+(?:per\s+day|known)|^\s*base\s+attack|^\s*level\s+(?:bonus|1st)", re.I)


def split_table_runs(b):
    """The paragraphs that stay of a paragraph that holds the header and the cells of a class table after its text ("Witch's Familiar (Ex): At 1st level, ...
    [bold] Spells per Day 0 3 1 -- ..."): the text before the first bold run that is a table header, and a sentence that follows the cells. None when the
    paragraph has no table header run."""
    for n, (txt, bold, _it) in enumerate(b.runs):
        if n > 0 and bold and TABLE_RUN.match(txt):
            keep = [fp.Para("para", list(b.runs[:n]), b.page, b.col, 0)]
            rest = "".join(x[0] for x in b.runs[n:])
            prose = prose_after_cells(rest)
            if prose:
                keep.append(fp.Para("para", [(prose, False, False)], b.page, b.col, 0))
            return keep
    return None


def window(blocks: list, heads: set[str] | frozenset = frozenset()) -> list:
    """The blocks of the section "Class Features" of the class: after that title, up to the next subsection or class title. A class table (its title and its
    cells) and a sidebar title (set larger, 24) do not end it; the cells of the table are not text of a feature."""
    at = next((i for i, b in enumerate(blocks) if b.kind == "title" and fp.squash(b.plain()) == "classfeatures"), None)
    if at is None:
        return []
    out = []
    for b in blocks[at + 1:]:
        if b.kind == "title" and not b.plain().strip().lower().startswith("table") and (b.size == 18 or b.size >= 38) and fp.squash(b.plain()) not in heads:
            break                                          # a subsection title ends the window, unless the corpus has it as a feature head (Patron Spells)
        if b.kind == "title" and b.plain().strip().lower().startswith("table"):
            continue                                       # the title of a class table is not text of a feature
        if b.kind == "para":
            cut = split_table_runs(b)
            if cut is not None:                            # prose, then the header and the cells of a class table in one paragraph
                out += cut
                continue
        if b.kind == "para" and is_table_para(b.plain()):
            prose = prose_after_cells(b.plain())
            if prose:                                      # the cells ran into the text of a sentence that the table broke: the sentence stays
                out.append(fp.Para("para", [(prose, False, False)], b.page, b.col, 0))
            continue
        out.append(b)
    return join_across_tables(out)


def join_across_tables(blocks: list) -> list:
    """A sentence that print breaks for a class table (the table stands in the middle of it) continues in the next paragraph, in lower case: the two
    are one paragraph. Only a paragraph that does not end in terminal punctuation, followed by one that starts in lower case, is joined."""
    out: list = []
    for b in blocks:
        if (out and b.kind == "para" and out[-1].kind == "para" and not co.paragraph_complete(out[-1].plain())
                and b.plain().strip()[:1].islower() and fp.head_candidate(b) is None):
            a = out.pop()
            out.append(fp.Para("para", list(a.runs) + [(" ", False, False)] + list(b.runs), a.page, a.col, 0))
        else:
            out.append(b)
    return out


HEAD_RE = re.compile(r"^#### (.*?)(?: \{#([^}]+)\})?\s*$")
WRITE_FEATURES = False        # the `features` of a class (anchor and level from the class table): off until the app has answered (owner call 5); bodies are written without
# The printed name of a head that the corpus names otherwise and that no plural or tag rule reaches: (class entry, key) -> print's head
PRINT_NAMES: dict[tuple[str, str], str] = {}


# Where an unlisted section stands when print sets it away from its feature (the sidebar of the Witch's Familiar is in the next column, after Major Hex):
# (class entry, key) -> (the key of the feature it belongs under, its level: one level below the feature head, ruling 15)
PLACE_UNDER: dict[tuple[str, str], tuple[str, int]] = {
    ("ref/class/witch", "adding-spells-to-a-witch-s-familiar"): ("witch-s-familiar", 5),
    ("ref/class/witch", "spells-gained-at-a-new-level"): ("witch-s-familiar", 5),
    ("ref/class/witch", "familiar-teaching-familiar"): ("witch-s-familiar", 5),
    ("ref/class/witch", "learn-from-a-scroll"): ("witch-s-familiar", 5),
}
# A box that interrupts a feature in print and that the corpus has as a `###` section: (class entry, key of the box) -> the key of the feature that its last
# paragraph ends (the Antipaladin's box "Fall From Grace" stands inside Spells, p. 121)
SIDEBAR_TAILS: dict[tuple[str, str], str] = {("ref/class/antipaladin", "fall-from-grace"): "spells"}
# Sections that print sets behind the class features and that the corpus has inside a feature (the Antipaladin's code of conduct is a row of its
# proficiencies): they become unlisted sections of their own, so the text stays where print has it.
SECTIONS_BEHIND: dict[str, set[str]] = {"ref/class/antipaladin": {"codeofconduct", "associates"}}
TABLE_LEAK = re.compile(r"\b(?:Spells|Extracts) per Day\s+(?:\d|1st|[\u2014\u2013])|(?:(?:[\u2014\u2013]|\d+)\s+){6,}")


# Print's layout puts a class table beside the text, and the text layer of the page runs words of the table's Special column into a sentence. Known cases:
# (class entry, key) -> [(what the layer has, what the sentence says)], each checked against the page.
LAYOUT_FIXES: dict[tuple[str, str], list[tuple[str, str]]] = {
    ("ref/class/summoner", "eidolon"): [("the Twin eidolon summoner's class level", "the summoner's class level")],
    ("ref/class/inquisitor", "slayer"): [("cannot be changed for the remainder of the judgment", "cannot be changed for the remainder of the judgment.")],     # print's sentence has no full stop (errata row of ruling 43)
    ("ref/class/antipaladin", "fiendish-boon"): [("re:Spells per Day 1st 2nd 3rd 4th(?: [\u2014\u2013\\d]+)+ ", "")],             # the cells of Table 2-13 (Advanced Player's Guide, Antipaladin p. 121)
    ("ref/class/inquisitor", "solo-tactics"): [("re:Spells per Day(?: \\d+)+ ", "")],                                              # the cells of Table 2-4 (Inquisitor p. 40)
    ("ref/class/summoner", "life-link"): [("more than 1,000 feet Spells per Day 5 5 5 5 5 5 away", "more than 1,000 feet away")],       # the cells of Table 2-8 (Advanced Player's Guide, Summoner p. 56)   # Table 2-7 lists "Twin eidolon" at 20th level (Advanced Player's Guide, Summoner p. 55)
}


def stem(name: str) -> str:
    """A head without its tag, in lower case, the last word in the singular ("Weapon and Armor Proficiencies" and "... Proficiency" are one head)."""
    s = " ".join(fp.ABILITY_TAG.sub("", name).strip().rstrip(":").strip().lower().split())        # print sets some heads with double spaces
    s = re.sub(r"ies$", "y", s)
    return re.sub(r"(?<!s)s$", "", s)


def references(corpus: Path, class_id: str, key: str) -> list[str]:
    """The entries that point at a head of a base class: a trade of an archetype of the class (`feature = "<key>"`, in `entries/arc-<class>/`) or a link to
    `<class id>#<key>` anywhere. A head that print does not set may be dropped only when nothing points at its key."""
    cls = class_id.rsplit("/", 1)[1]
    out = []
    for p in sorted((corpus / "entries").rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        if f"{class_id}#{key})" in text or (p.parent.name == f"arc-{cls}" and f'feature = "{key}"' in text):
            out.append(p.stem)
    return out


def overlap(a: str, b: str) -> int:
    wa = set(re.findall(r"[a-z']{4,}", a.lower()))
    return len(wa & set(re.findall(r"[a-z']{4,}", b.lower())))


def split_between(paras: list[str], first_corpus: str, second_corpus: str) -> int:
    """Where a printed feature ends and the next feature of the corpus (that print sets inside it, as text) begins: the paragraph index that gives the best
    overlap of words, the first part with the corpus text of the first feature and the rest with the second (at least one paragraph each)."""
    best, at = -1, len(paras)
    for k in range(1, len(paras)):
        s = sum(overlap(x, first_corpus) for x in paras[:k]) + sum(overlap(x, second_corpus) for x in paras[k:])
        if s > best:
            best, at = s, k
    return at


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


def class_decisions(corpus: Path, book: str) -> dict[tuple[str, str], tuple[str, str]]:
    """The decisions of the book's class options file for classes: (class id, key) -> (decision, note); `print` settles a hold as print has it (the corpus
    wording is the import's paraphrase, or print has text that the corpus lacks), `hold` keeps it for an errata check."""
    return co.read_decisions(co.decisions_file(corpus, book))


def compare_class(corpus: Path, e, bk, cache: dict, options: dict | None = None, decisions: dict | None = None) -> dict:
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
    # a corpus head that print sets as the title of a section behind the class features ("Patron Spells" over the patrons of the Witch, p. 70): that
    # section is read as the text of the head
    lacking = {fp.squash(fp.ABILITY_TAG.sub("", h)) for _, h, _ in heads if fp.namekey(h) not in printed and not any(stem(ph) == stem(h) for ph in printed.values())}
    win = win + section_behind(blocks, win, lacking | SECTIONS_BEHIND.get(e.id, set()))
    _, pfs = fp.split_print([title] + win, [h for _, h, _ in heads])
    printed = {fp.namekey(fp.head_text(f.head)): fp.head_text(f.head) for f in pfs}
    names = {}                                                    # key -> the name that the pseudo body gives the head
    for _, text, key in heads:
        want = PRINT_NAMES.get((e.id, key))
        if want is None and fp.namekey(text) not in printed:
            want = next((ph for ph in printed.values() if stem(ph) == stem(text)), None)       # "Proficiency" for "Proficiencies"
        names[key] = (want or text).rstrip(":").strip()            # "Order (Ex):" is a name without its colon (a name that ends in one is no feature name)
    pseudo_lines = []
    for ln in lines[region[0]:region[1]]:
        m = HEAD_RE.match(ln)
        pseudo_lines.append(f"**{names[m.group(2) or fp.slugify(fp.ABILITY_TAG.sub('', m.group(1)))]}**" if m else ln)
    pseudo = "\n".join(pseudo_lines)
    probe = {fp.namekey(h) for h in (fp.head_of_para(p_) for p_ in win) if h}                  # as the print comparison reads the import: a row that print sets as a head is split off
    _, feats_all = fp.parse_import(pseudo, probe)
    feats = [f for f in feats_all if not f.pseudo]
    if len(feats) != len(heads):
        return {"items": [], "extra": [], "missing": [], "window": len(win), "problems": [f"{len(heads)} heads but {len(feats)} features read from them"], "region": region}
    e2 = dataclasses.replace(e, body=pseudo)
    res = fp.compare_entry(e2, [title] + win, bk)
    by_span = {r["span"]: r for r in res["rows"] if r["span"]}
    items, missing = [], []
    all_spans = {f.span_sha() for f in feats_all}
    for (line, text, key), f in zip(heads, feats):
        r = by_span.get(f.span_sha())
        if r is None or "head not printed" in r["notes"]:
            missing.append(key)
            items.append({"key": key, "line": line, "head": text, "print": "", "status": "hold", "notes": ["head not printed"]})
        else:
            status, notes = r["status"], list(r["notes"])
            dec = (decisions or {}).get((e.id, key))
            if dec and dec[0] == "print" and status == "hold":
                status = "print"
                notes.append(f"decision: {dec[1]}")
            head, text = r["head"], r["print"]
            tag = re.match(r"^\(((?:Ex|Su|Sp)(?:(?:, or |, and |, | or | and )(?:Ex|Su|Sp))*)\):\s*", text)
            if tag:                                       # the tag of the head ("Summon Monster I" "(Sp):") stands in the first run: it belongs to the head
                head = f"{head} ({tag.group(1)})" if not re.search(r"\((?:Ex|Su|Sp)[^)]*\)\s*$", head) else head
                text = text[tag.end():]
            for old, new in LAYOUT_FIXES.get((e.id, key), []):
                fix = (lambda s, o=old, n=new: re.sub(o[3:], n, s)) if old.startswith("re:") else (lambda s, o=old, n=new: s.replace(o, n))
                if fix(" ".join(text.split())) != " ".join(text.split()):
                    text = "\n\n".join(fix(" ".join(x.split())) for x in text.split("\n\n"))
                    notes.append(f"layout: words or cells of a class table are in the sentence ({old[:50]!r})")
            leak = TABLE_LEAK.search(" ".join(text.split()))
            if leak:                                      # cells of a class table in the sentence: a layout fix (`LAYOUT_FIXES`) must name them
                status = "hold"
                notes.append(f"cells of a class table are in the text: ...{' '.join(text.split())[max(0, leak.start() - 40):leak.end() + 30]}...")
            cut = co.incomplete_paragraph(text)
            if cut:                                       # the completeness guard: the window ended, or a table stands in the sentence
                status = "hold"
                notes.append(f"print text may be cut at a page or column break: ...{cut}")
            items.append({"key": key, "line": line, "head": head, "print": text, "status": status, "notes": notes})
    ends = [h[0] for h in heads[1:]] + [region[1]]
    for (ln, _txt, _key), end, it in zip(heads, ends, items):
        it["corpus"] = "\n".join(lines[ln + 1:end])
    for n, it in enumerate(items):
        if "head not printed" not in it["notes"]:
            continue
        refs = references(corpus, e.id, it["key"])
        prev = next((x for x in reversed(items[:n]) if "head not printed" not in x["notes"]), None)
        if not refs:
            it["drop"] = True                                     # nothing points at the key: print sets the text inside another feature, written once, there
            it["status"] = "print"
            it["notes"] = [f"dropped: no trade or link points at `{it['key']}`; print sets its text inside the feature above it"]
        elif prev is not None and prev["print"]:
            paras = prev["print"].split("\n\n")
            if len(paras) > 1:
                k = split_between(paras, prev["corpus"], it["corpus"])
                prev["print"], it["print"] = "\n\n".join(paras[:k]), "\n\n".join(paras[k:])
                it["status"] = "hold"
                it["notes"] = [f"print sets this head's text inside `{prev['key']}` (split by the corpus text); referenced by {refs[:3]}"]
                it["split_from"] = prev["key"]
                dec = (decisions or {}).get((e.id, it["key"]))
                if dec and dec[0] == "print":
                    it["status"] = "print"
                    it["notes"].append(f"decision: {dec[1]}")
    extra, options = [], options or {}                          # the items of an option list are collected, then linked from one group
    last = None
    taken = set(re.findall(r"\{#([^}]+)\}", e.body)) | {fp.slugify(fp.ABILITY_TAG.sub("", t_)) for _, t_, _ in heads}
    title_heads = {fp.squash(b.plain()) for b in win if b.kind == "title"}
    new_items: list[tuple[str | None, dict]] = []                # (key of the item before it in print, the unlisted section)
    for r in res["rows"]:
        if r["span"] and r["span"] in all_spans:
            if fp.squash(r["head"]) in SECTIONS_BEHIND.get(e.id, set()) and r["print"].strip():
                # a row of the corpus (its code of conduct, under the proficiencies) that print sets as a paragraph of its own behind the last feature
                head = r["head"].rstrip(":").strip()
                key = fp.slugify(head)
                status, notes = r["status"], list(r["notes"]) + ["printed behind the class features, a row of the proficiencies in the corpus: an unlisted section"]
                if key in taken:
                    status = "hold"
                    notes.append(f"the new key `{key}` is a key of the class already")
                taken.add(key)
                new_items.append((items[-1]["key"], {"key": key, "line": -1, "head": head, "print": r["print"], "status": status, "notes": notes,
                                                      "level": 4, "unlisted": True}))
            last = r
            continue
        opt = options.get(fp.namekey(r["head"]))
        if opt and last is not None:                                # an item of an option list that has its own entry: a link under the feature
            it = next((x for x in items if x["head"] == last["head"]), None)
            if it is not None:
                it.setdefault("candidates", []).append((r["head"].rstrip("*").strip(), opt))      # the star after a name is print's book marker (ruling 26): the link replaces it
            continue
        if "head printed, not in the import" in " ".join(r["notes"]) and not is_table_para(r["head"]):
            # a printed head that the corpus lacks: an unlisted section, one level below the feature (a sub-head, ruling 15) or a rules box at the level
            # of the features (a sidebar title, ruling 41), with a new explicit key that no key of the class has
            head = r["head"]
            key = fp.slugify(fp.ABILITY_TAG.sub("", head))
            status, notes = r["status"], list(r["notes"])
            if key in taken:
                status = "hold"
                notes.append(f"the new key `{key}` is a key of the class already")
            taken.add(key)
            cut = co.incomplete_paragraph(r["print"])
            if cut:
                status = "hold"
                notes.append(f"print text may be cut at a page or column break: ...{cut}")
            prev = next((x for x in items if last is not None and x["head"] == last["head"]), None)
            new_items.append((prev["key"] if prev else None, {"key": key, "line": -1, "head": head, "print": r["print"], "status": status, "notes": notes,
                                                          "level": 4 if fp.squash(head) in title_heads else 5, "unlisted": True}))
            last = r
    for it in items:
        if it.get("candidates"):
            it["links"] = pick_options(it.pop("candidates"))
        if re.search(r"[a-z][A-Z]", it["head"]) and fp.namekey(it["head"]) in {fp.namekey(t_) for _, t_, _ in heads}:
            it["head"] = next(t_ for _, t_, _ in heads if fp.namekey(t_) == fp.namekey(it["head"]))      # small capitals in the text layer ("Patron sPells")
    for after, sec in list(new_items):
        tail_to = SIDEBAR_TAILS.get((e.id, sec["key"]))
        if tail_to:
            # a sidebar that the corpus has as a section of its own after the class features (`### Fall from Grace`): not a second copy. The paragraph after
            # the box in the text layer is the end of the feature that the box interrupts; it goes back there. The rest of the box must be the section's text.
            sect = re.search(r"^### " + re.escape(sec["head"]) + r"\s*\n(.*?)(?=^### |\Z)", e.body, re.M | re.S | re.I)
            want = fp.squash(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", sect.group(1))) if sect else ""
            sents = re.split(r"(?<=[.!?])\s+", sec["print"].strip())
            host = next((x for x in items if x["key"] == tail_to), None)
            scored = [(difflib.SequenceMatcher(None, fp.squash(" ".join(sents[:k])), want).ratio(), k) for k in range(1, len(sents))]
            ratio, cut = max(scored, default=(0.0, 0))             # the end of the box that fits the section's text best
            if ratio < 0.97 or host is None:
                sec["status"] = "hold"
                sec["notes"].append(f"the box does not match the section `### {sec['head']}` of the corpus (ratio {ratio:.3f})")
                continue
            tail = " ".join(sents[cut:])
            host["print"] = host["print"].rstrip() + "\n\n" + tail
            host["notes"].append(f"print sets the last sentences of this feature after the box `{sec['head']}`")
            new_items.remove((after, sec))
            continue
        placed = PLACE_UNDER.get((e.id, sec["key"]))
        if placed:
            after, sec["level"] = placed
        at = next((n for n, x in enumerate(items) if x["key"] == after), len(items) - 1)
        while at + 1 < len(items) and items[at + 1].get("unlisted"):
            at += 1                                              # after the sections that already follow the feature, in print order
        items.insert(at + 1, sec)
    missing = [i["key"] for i in items if "head not printed" in i["notes"] and not i.get("drop") and not i.get("split_from")]      # a head that no rule resolved
    return {"items": items, "extra": extra, "missing": missing, "window": len(win), "problems": res["problems"], "region": region,
            "levels": fp.class_table_levels(corpus, e.id, cache)}


def feature_text(it: dict) -> str:
    """The text under a head: print's paragraphs; the items of an option list that have entries of their own are links after the lead-in."""
    text = it["print"].strip()
    if it.get("links"):
        text += "\n\n" + "\n".join(f"- [{name}]({eid})" for name, eid in it["links"])
    return text


def class_features(plan: dict) -> list[tuple[str, int | None]]:
    """The `features` of a class: (key, level) for each head, the level from the Special column of the class table (`class_table_levels`). Built for the
    switch `WRITE_FEATURES`, which is off: where the app wants the key in the front matter of a class is not answered yet (owner call 5), so the
    bodies are written without it and the front is not touched."""
    lv = plan.get("levels", {})
    return [(it["key"], lv.get(fp.first_level_key(it["head"]))) for it in plan["items"]]


def settled(plan: dict) -> bool:
    return bool(plan["items"]) and not plan["extra"] and not plan["missing"] and all(i["status"] in ("print", "draft") for i in plan["items"] if not i.get("drop"))


def converted_body(body: str, plan: dict) -> str:
    """The class body with the text under each head replaced by print's, the head as print has it with the key written out, the class table and every
    other line as they were (rule 3 of AGENTS.md: no key moves)."""
    lines = body.split("\n")
    a, b = plan["region"]
    out = []
    for it in plan["items"]:
        if it.get("drop"):
            continue
        out += ["#" * it.get("level", 4) + f" {it['head']} {{#{it['key']}}}", "", feature_text(it), ""]
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
        plan = compare_class(corpus, e, bk, cache, options, class_decisions(corpus, book))
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
            if WRITE_FEATURES:
                raise SystemExit("the `features` of a class are not written yet: the app has not said where the key stands in a class (owner call 5)")
            body2 = converted_body(e.body, plan)
            gone = co.heading_keys(e.body) - co.heading_keys(body2)
            allowed = {"sec-" + it["key"] for it in plan["items"] if it.get("drop")} | {it["key"] for it in plan["items"] if it.get("drop")}
            if gone - allowed:
                raise SystemExit(f"{e.id}: the heading keys {sorted(gone - allowed)} would move (only a dropped head without a reference may go)")
            co.write_atomic(e.path, "+++\n" + e.front.strip("\n") + "\n+++\n" + body2)
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
    eq((stem("Weapon and Armor Proficiencies"), stem("Weapon  and  Armor  Proficiency")), ("weapon and armor proficiency",) * 2, "a head in the plural and in the singular, with double spaces, is one head")
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
    eq(pick_options([("Concussive bomb", [("ref/discovery/concussive-bomb", "alchemist-discovery")])]), [("Concussive bomb", "ref/discovery/concussive-bomb")], "an option name has no star in its link text")
    eq(pick_options([("Clouded Vision", [("ref/oraclecurse/clouded-vision", "oracle-curse")]), ("Tongues", [("ref/shamanhex/tongues", "shaman-hex"), ("ref/oraclecurse/tongues", "oracle-curse")]),
                     ("Lame", [("ref/oraclecurse/lame", "oracle-curse")])]),
       [("Clouded Vision", "ref/oraclecurse/clouded-vision"), ("Tongues", "ref/oraclecurse/tongues"), ("Lame", "ref/oraclecurse/lame")], "owner call 4: a title that two groups share is linked from the group of the list")
    eq(LAYOUT_FIXES[("ref/class/summoner", "eidolon")][0][1], "the summoner's class level", "a known layout fix names the words of the table that the layer ran into a sentence")
    eq(WRITE_FEATURES, False, "owner call 5: the `features` switch is off")
    eq(class_features({"items": [{"key": "mystery", "head": "Mystery"}, {"key": "bomb", "head": "Bomb (Su)"}], "levels": {fp.first_level_key("Mystery"): 1}}),
       [("mystery", 1), ("bomb", None)], "the levels of the features come from the class table, a feature that is not in it has none")
    eq(re.match(r"^\(((?:Ex|Su|Sp)[^)]*)\):\s*", "(Sp): Starting at 1st level, a summoner").group(1), "Sp", "the tag that print leaves in the first run is found")
    eq((settled(plan), settled(dict(plan, extra=["X"])), settled(dict(plan, missing=["mystery"]))), (True, False, False), "a class is written all or nothing")
    P = fp.Para
    blocks = [P("title", [("Oracle", True, False)], 42, 1, 38), P("title", [("Class Features", True, False)], 42, 1, 18),
              P("para", [("Spells: A.", False, False)], 42, 1), P("title", [("Table 2–5: Oracle", True, False)], 44, 0, 24), P("para", [("1st +0", False, False)], 44, 0),
              P("para", [("Orisons: B.", False, False)], 45, 0), P("title", [("Alternate Capstones", True, False)], 46, 0, 18), P("para", [("Late.", False, False)], 46, 0)]
    eq([b.plain() for b in window(blocks)], ["Spells: A.", "1st +0", "Orisons: B."], "the window runs over a table (its title is no text) and ends at the next title")
    side = blocks[:3] + [P("title", [("Fall From Grace", True, False)], 46, 0, 24), P("para", [("Sidebar.", False, False)], 46, 0), P("title", [("Ex-Antipaladins", True, False)], 46, 0, 18)]
    eq([b.plain() for b in window(side)], ["Spells: A.", "Fall From Grace", "Sidebar."], "a sidebar title (larger) does not end the window, the next subsection does")
    eq(window([blocks[0]]), [], "a page without the Class Features title has no window")
    eq((prose_after_cells("6 6 6 6 6 6 due to encumbrance. At 5th level, you are immune to fatigue."), prose_after_cells("1st +0 +0 +0 +2 Mystery, oracle's curse, orisons 3 \u2014 \u2014")),
       ("due to encumbrance. At 5th level, you are immune to fatigue.", ""), "a sentence that the cells ran into stays, a table row with words in its cells does not")
    cutp = [P("para", [("A damage remains", False, False)], 44, 0), P("para", [("with the summoner. Effects", False, False)], 45, 0), P("para", [("Next: B.", True, False)], 45, 0)]
    eq([b.plain() for b in join_across_tables(cutp)], ["A damage remains with the summoner. Effects", "Next: B."], "a sentence that a table broke is joined, a new paragraph is not")
    mixed = P("para", [("Witch's Familiar (Ex)", True, False), (": At 1st level, a witch forms a bond.", False, False), ("    Spells per Day 0", True, False), (" 3 1 \u2014 \u2014 \u2014 \u2014 \u2014 \u2014 \u2014", False, False)], 67, 0)
    eq([x.plain() for x in split_table_runs(mixed)], ["Witch's Familiar (Ex): At 1st level, a witch forms a bond."], "a paragraph with prose and then a table keeps its prose")
    eq(split_table_runs(P("para", [("Plain: text.", False, False)], 1, 0)), None, "a paragraph without a table header run is left")
    eq((is_table_para("6 6 6 6 6 6 6 6 6"), is_table_para("1st +0 +0 +0 +2 Mystery, oracle's curse, orisons 3 \u2014 \u2014 \u2014"), is_table_para("Base Attack Fort Ref Will Level Bonus Save Save Save Special"),
        is_table_para("An oracle casts divine spells drawn from the cleric spell lists.")), (True, True, True, False), "the cells of a class table are no text of a feature")
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
