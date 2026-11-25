#!/usr/bin/env python3
"""Validate the shared errata review file `scripts/errata.tsv` (phynics/cast-iron-data#309).

    python3 scripts/errata.py [CORPUS] --check     # CORPUS defaults to the repository root
    python3 scripts/errata.py --self-test

`scripts/errata.md` documents the columns, classes and decisions, and how a compare script reads the
file. This script reads only the corpus and the TSV (Python 3.11 or later, no third-party package,
no PDF). `--check` fails (exit 1, one line per problem) when:

- the header is not the one in `COLUMNS`, or a row has another number of fields;
- a required field is empty, or `class` or `decision` is not in its list, or the pair is not allowed;
- two rows share `(entry, field)`, or the rows are not sorted by `(entry, field)`;
- `book` is not a publication id of `publications.toml`;
- `printed_sha256` is not the SHA-256 of the normalized `printed_value` (so a row that was edited
  without its hash is stale);
- the entry does not exist, or its text (front matter and body) lacks the value that the decision
  says it holds: `printed_value` for `print`, `kept_value` for `keep` and `misprint-fix`.

Text is compared after `norm_text`: Markdown links reduced to their text, `*` and `_` removed, curly
quotes and long dashes folded to ASCII, white space collapsed, case folded.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import tempfile
import unicodedata
from pathlib import Path

COLUMNS = [
    "entry", "field", "book", "page", "printing", "printed_value", "kept_value",
    "class", "evidence", "decision", "printed_sha256", "note",
]
REQUIRED = [c for c in COLUMNS if c not in ("kept_value", "note")]
CLASSES = ("import-error", "paraphrase", "misprint", "errata", "unknown")
DECISIONS = ("print", "keep", "misprint-fix")
# Which classes a decision allows, and whether `kept_value` is filled.
ALLOWED = {
    "print": ({"import-error", "paraphrase", "unknown"}, False),
    "keep": ({"errata"}, True),
    "misprint-fix": ({"misprint"}, True),
}
TSV = Path("scripts") / "errata.tsv"


def norm_text(s: str) -> str:
    """The form in which a value and an entry are compared."""
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"\\([\\`*_{}\[\]()#+.!-])", r"\1", s)  # Markdown backslash escapes
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = s.replace("*", "").replace("_", "")
    s = s.translate(str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"',
                                   "–": "-", "—": "-", "−": "-"}))
    return " ".join(s.split()).casefold()


def sha(s: str) -> str:
    """The `printed_sha256` of a printed value: NFC, white space collapsed, UTF-8."""
    return hashlib.sha256(" ".join(unicodedata.normalize("NFC", s).split()).encode("utf-8")).hexdigest()


def read_rows(path: Path) -> tuple[list[str], list[tuple[int, list[str]]]]:
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    header = lines[0].split("\t") if lines else []
    return header, [(i + 2, ln.split("\t")) for i, ln in enumerate(lines[1:])]


def entry_files(corpus: Path) -> dict[str, Path]:
    """Entry id -> file, read from the `id = "..."` line of each front matter."""
    out: dict[str, Path] = {}
    for p in (corpus / "entries").rglob("*.md"):
        with p.open(encoding="utf-8") as f:
            for _ in range(4):
                m = re.match(r'id = "([^"]+)"', f.readline())
                if m:
                    out[m.group(1)] = p
                    break
    return out


def publication_ids(corpus: Path) -> set[str]:
    return set(re.findall(r'^id = "([^"]+)"', (corpus / "publications.toml").read_text(encoding="utf-8"), re.M))


def check(corpus: Path, tsv: Path | None = None) -> list[str]:
    tsv = tsv or corpus / TSV
    if not tsv.is_file():
        return [f"{tsv}: missing"]
    header, rows = read_rows(tsv)
    if header != COLUMNS:
        want = "\t".join(COLUMNS)
        return [f"{tsv.name}:1: the header must be: {want}"]
    pubs, files = publication_ids(corpus), entry_files(corpus)
    cache: dict[str, str] = {}
    bad: list[str] = []
    seen: set[tuple[str, str]] = set()
    prev: tuple[str, str] | None = None
    for n, f in rows:
        where = f"{tsv.name}:{n}"
        if len(f) != len(COLUMNS):
            bad.append(f"{where}: {len(f)} fields, expected {len(COLUMNS)}")
            continue
        r = dict(zip(COLUMNS, f))
        label = f"{where} {r['entry']} {r['field']}"
        for c in REQUIRED:
            if not r[c].strip():
                bad.append(f"{label}: `{c}` is empty")
        for c in COLUMNS:
            if r[c] != r[c].strip():
                bad.append(f"{label}: `{c}` has leading or trailing white space")
        if r["class"] and r["class"] not in CLASSES:
            bad.append(f"{label}: class `{r['class']}` is not one of {', '.join(CLASSES)}")
        if r["decision"] and r["decision"] not in DECISIONS:
            bad.append(f"{label}: decision `{r['decision']}` is not one of {', '.join(DECISIONS)}")
        elif r["decision"]:
            classes, has_kept = ALLOWED[r["decision"]]
            if r["class"] in CLASSES and r["class"] not in classes:
                bad.append(f"{label}: decision `{r['decision']}` needs class {' or '.join(sorted(classes))}")
            if has_kept and not r["kept_value"]:
                bad.append(f"{label}: decision `{r['decision']}` needs a `kept_value`")
            if not has_kept and r["kept_value"]:
                bad.append(f"{label}: decision `{r['decision']}` leaves `kept_value` empty (the corpus holds the printed value)")
            if r["decision"] == "keep" and not r["evidence"].startswith("Paizo errata for "):
                bad.append(f"{label}: a `keep` row cites a Paizo errata document (`evidence` starts with \"Paizo errata for \")")
        key = (r["entry"], r["field"])
        if key in seen:
            bad.append(f"{label}: duplicate (entry, field)")
        elif prev and key < prev:
            bad.append(f"{label}: rows must be sorted by (entry, field)")
        seen.add(key)
        prev = key
        if r["book"] and r["book"] not in pubs:
            bad.append(f"{label}: book `{r['book']}` is not in publications.toml")
        if r["printed_value"] and r["printed_sha256"] != sha(r["printed_value"]):
            bad.append(f"{label}: printed_sha256 is stale (the printed value changed, or the hash is wrong)")
        path = files.get(r["entry"])
        if path is None:
            bad.append(f"{label}: no entry with this id")
            continue
        text = cache.get(r["entry"])
        if text is None:
            text = cache[r["entry"]] = norm_text(path.read_text(encoding="utf-8"))
        want = r["printed_value"] if r["decision"] == "print" else r["kept_value"]
        if want and norm_text(want) not in text:
            which = "printed_value" if r["decision"] == "print" else "kept_value"
            bad.append(f"{label}: the entry text does not contain the {which}")
    return bad


def self_test() -> int:
    fails = 0

    def eq(got, want, what):
        nonlocal fails
        if got != want:
            fails += 1
            print(f"FAIL {what}: got {got!r}, want {want!r}")

    eq(norm_text("A [bull rush](ref/rule/bull-rush) of\n  _the_ **bard’s** – x"), "a bull rush of the bard's - x", "norm_text")
    eq(norm_text(r"Disarming Threat\*, an asterisk \[\*\] key"), norm_text("Disarming Threat*, an asterisk [*] key"), "norm_text drops Markdown escapes")
    eq(sha("a  b\n c") == sha("a b c"), True, "sha ignores white space runs")
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "entries").mkdir()
        (root / "scripts").mkdir()
        (root / "publications.toml").write_text('[[publications]]\nid = "book-a"\n', encoding="utf-8")
        (root / "entries" / "one.md").write_text('+++\nid = "ref/x/one"\n+++\n\nIt deals 1d8\npoints of **damage**.\n', encoding="utf-8")
        value = "it deals 1d8 points of damage."

        def row(**kw):
            r = {"entry": "ref/x/one", "field": "f", "book": "book-a", "page": "1", "printing": "Second printing",
                 "printed_value": value, "kept_value": "", "class": "unknown", "evidence": "none", "decision": "print",
                 "printed_sha256": sha(value), "note": ""}
            r.update(kw)
            return "\t".join(r[c] for c in COLUMNS)

        def run(*rows):
            (root / TSV).write_text("\t".join(COLUMNS) + "\n" + "".join(x + "\n" for x in rows), encoding="utf-8")
            return check(root)

        eq(run(row()), [], "a valid print row")
        eq(len(run(row(entry="ref/x/two"))), 1, "an unknown entry")
        eq(len(run(row(printed_value="it deals 1d6 points of damage.", printed_sha256=sha("it deals 1d6 points of damage.")))), 1, "the entry lacks the printed value")
        eq(len(run(row(printed_sha256="0" * 64))), 1, "a stale hash")
        eq(len(run(row(book="book-b"))), 1, "an unknown book")
        eq(len(run(row(**{"class": "errata"}))), 1, "errata needs keep")
        eq(len(run(row(kept_value="x"))), 1, "print leaves kept_value empty")
        eq(len(run(row(decision="keep", **{"class": "errata"}, kept_value=value))), 1, "keep cites an errata document")
        eq(run(row(decision="keep", **{"class": "errata"}, kept_value=value, evidence="Paizo errata for Book A")), [], "a valid keep row")
        eq(len(run(row(field="b"), row(field="a"))), 1, "unsorted rows")
        eq(len(run(row(), row())), 1, "a duplicate row")
        eq(len(run(row().rsplit("\t", 1)[0])), 1, "a short row")
    print("self-test: ok" if not fails else f"self-test: {fails} failure(s)")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("corpus", nargs="?", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--check", action="store_true", help="validate scripts/errata.tsv against the corpus")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.check:
        ap.error("give --check or --self-test")
    bad = check(Path(args.corpus).resolve())
    for line in bad:
        print(line)
    if bad:
        print(f"errata: {len(bad)} problem(s)")
        return 1
    rows = len(read_rows(Path(args.corpus).resolve() / TSV)[1])
    print(f"errata: {rows} row(s) ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
