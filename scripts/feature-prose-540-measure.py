#!/usr/bin/env python3
"""What each hold rule of `feature-prose-540.py` does to the converted books (phynics/cast-iron#540).

A converted entry has no import rows, so the comparison of the script cannot run on it. This tool takes, for every entry of every book that
has a review table, the last version of the file from the git history that is still in import form, runs the comparison of the script on
it with no decision and no edit (so that the holds are the script's own), and counts the feature rows and entry problems that are holds.
It does that (with `--decided`, with the decisions and edits of the review files) with all rules off (the script before the rules), with each rule alone, and with all rules on, and prints for each rule how
many holds it removes and how many it adds against the rules-off run.

    feature-prose-540-measure.py [CORPUS] --books DIR --cache DIR [--rules none,hyphens,...,all] [--book ID[,ID]] [--out FILE]

Needs the owner's copies of the books (`--books`, searched like `--compare` does), `pdftohtml` (poppler), and the full git history of the
corpus. It writes nothing to the corpus.
"""

from __future__ import annotations

import argparse
import collections
import importlib.util
import json
import subprocess
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_script():
    spec = importlib.util.spec_from_file_location("fp540", HERE / "feature-prose-540.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["fp540"] = mod
    spec.loader.exec_module(mod)
    return mod


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=False).stdout


def import_text(root: Path, path: Path) -> str | None:
    """The newest version of the file in the history whose front matter has no `features` list."""
    rel = str(path.relative_to(root))
    for sha in git(root, "log", "--format=%H", "--", rel).split():
        text = git(root, "show", f"{sha}:{rel}")
        if "features = [" not in text.split("\n+++\n", 1)[0]:
            return text
    return None


def holds_of(fp, root: Path, book: str, books_dir: Path, cache: Path, decided: bool = False) -> dict[str, str]:
    fp.configure_book(book)
    pdf = fp.find_pdf(books_dir, fp.publication_title(root, book))
    if not pdf:
        raise SystemExit(f"no copy of {book!r} under {books_dir}")
    bk = fp.load_book(fp.book_xml(pdf, cache))
    entries = []
    for e in fp.load_entries(root, book):
        text = import_text(root, e.path)
        if text is None:
            continue
        front, body = fp.split_entry(text)
        entries.append(fp.Entry(e.path, e.id, e.title, "archetype", front, body, tomllib.loads(front), e.book, e.page, e.classes))
    stops = {fp.squash(x.title) for x in entries} | fp.CLASS_TITLES | fp.UNTYPED_ARCHETYPE_TITLES
    out: dict[str, str] = {}
    for e in entries:
        if not e.page.isdigit():
            continue
        page = int(e.page)
        blocks = fp.read_blocks(bk, max(1, page + 1 - 3), min(page + 1 + 4, max(bk.pages)))
        section = fp.find_section(blocks, e.title, stops)
        if section is None:
            out[f"{e.id}|"] = "title not found"
            continue
        res = fp.compare_entry(e, section, bk)
        if decided:
            res["decisions"], res["edits"], res["adds"] = fp.read_decisions(root, book), fp.read_edits(root, book), fp.read_adds(root, book)
        else:
            res["decisions"], res["edits"], res["adds"] = {}, {}, {}
        fin = fp.finalize(e, res)
        for row in fin["rows"]:
            if row["status"] == "hold":
                out[f"{e.id}|{row['anchor']}"] = "; ".join(row["notes"])
        for problem in fin["problems"]:
            out[f"{e.id}|!{problem[:40]}"] = problem
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", nargs="?", default=str(HERE.parent))
    ap.add_argument("--books", required=True)
    ap.add_argument("--cache", required=True)
    ap.add_argument("--rules", default="none,hyphens,prereq,usage,values,dropped,all")
    ap.add_argument("--book", default="")
    ap.add_argument("--out", default="")
    ap.add_argument("--decided", action="store_true", help="apply the decisions, edits and additions of each book's review files: the holds that are left are those that a rule makes new")
    args = ap.parse_args()
    root = Path(args.corpus).resolve()
    fp = load_script()
    books = args.book.split(",") if args.book else sorted(
        p.name[len("feature-prose-540-"):-4] for p in (root / "scripts").glob("feature-prose-540-*.tsv")
        if not p.name.endswith((".decisions.tsv", ".queue.tsv", ".sentences.tsv", ".class-options.tsv")))
    runs: dict[str, dict[str, str]] = {}
    for spec in args.rules.split(","):
        on = set(fp.RULES) if spec == "all" else (set() if spec == "none" else set(spec.split("+")))
        for k in fp.RULES:
            fp.RULES[k] = k in on
        runs[spec] = {}
        for b in books:
            for key, why in holds_of(fp, root, b, Path(args.books), Path(args.cache), args.decided).items():
                runs[spec][f"{b}|{key}"] = why
        print(f"{spec}: {len(runs[spec])} holds", file=sys.stderr)
    base = set(runs.get("none", {}))
    print(f"{'rules':<10} {'holds':>6} {'removed':>8} {'added':>6}")
    for spec, found in runs.items():
        now = set(found)
        print(f"{spec:<10} {len(now):>6} {len(base - now):>8} {len(now - base):>6}")
    if "all" in runs:
        per = collections.defaultdict(lambda: [0, 0, 0])
        now = set(runs["all"])
        for k in base | now:
            b = k.split("|")[0]
            per[b][0] += k in base
            per[b][1] += k in base and k not in now
            per[b][2] += k in now and k not in base
        print(f"\n{'book':<26} {'holds':>6} {'removed':>8} {'added':>6}   (all rules against none)")
        for b, (h, r, a) in sorted(per.items()):
            print(f"{b:<26} {h:>6} {r:>8} {a:>6}")
    if args.out:
        Path(args.out).write_text(json.dumps(runs, indent=1, sort_keys=True), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
