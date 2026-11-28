#!/usr/bin/env python3
"""Check written class-option sentences directly against the printed PDF text."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import re
import sys
import tomllib
import unicodedata
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CLASS_OPTIONS = load("class_options_for_sentence_audit", HERE.parent / "feature-prose-540-class-options.py")


# Direct page-region transcriptions for the three heads whose PDF text layer mixes neighboring
# tables into the prose. These are checked against print separately from the writer's corrections.
PRINT_REGION_TEXT = {
    ("occult-adventures", "ref/phrenicamp/mimic-metamagic"): (
        "When the psychic gains this amplification, she chooses two metamagic feats; she need not have these feats to select them. "
        "When she casts a spell, she can spend points from her phrenic pool to apply one of the chosen feats to the linked spell "
        "without increasing the spell's level or casting time. She must spend a number of points equal to double the number of levels "
        "by which the feat normally increases a spell's level (minimum 2 points). If the metamagic feat alters the spell's casting time "
        "in a different way than the standard rules for a spontaneous caster using a metamagic feat (as in the case of Quicken Spell), "
        "it changes the casting time accordingly. The psychic can still apply metamagic feats she knows to the spell while using this "
        "amplification, increasing the casting time and spell level as normal. This amplification can be applied only to a spell that the "
        "chosen metamagic feat could normally affect, and only if the spellcaster can cast spells of a high enough level that she would be "
        "able to apply the metamagic feat in question to the linked spell. For example, an 11th-level psychic could spend 8 points to "
        "quicken a 1st-level spell, but couldn't quicken a 2nd-level spell because she's unable to cast 6th-level spells. This ability "
        "doesn't require her to have any free spell slots in the relevant level, however, so the psychic in the example could quicken a "
        "1st-level spell even if she had cast all her 5th-level spells for the day. A psychic can select this amplification multiple times, "
        "adding two additional options to the list of metamagic feats she can apply using this amplification each time."
    ),
    ("occult-adventures", "ref/phrenicamp/ongoing-defense"): (
        "The psychic can increase the duration of spells that improve her psychic defenses. She can spend 1 point from her phrenic pool "
        "when she casts any intellect fortress, mental barrier, thought shield, or tower of iron will spell to extend the spell's duration "
        "by 1 round."
    ),
    ("occult-adventures", "ref/phrenicamp/undercast-surge"): (
        "When the psychic undercasts a spell (see page 144), she can spend points from her phrenic pool to increase the spell's effective "
        "level, essentially using up a lower-level spell slot to cast a higher-level version of the spell. This costs 2 points per spell "
        "level increased. She can't use this ability to cast a version higher than the version she knows. For instance, a psychic who knows "
        "mind thrust III but not mind thrust IV could cast mind thrust II and spend 2 points to treat it as mind thrust III, but couldn't "
        "spend 4 points to treat it as mind thrust IV. This amplification can be linked only to spells that can be undercast."
    ),
}


def printed_region_text(book: str, entry_id: str, extracted: str) -> str:
    """Return a direct transcription of the printed region when the PDF text layer interleaves tables."""
    return PRINT_REGION_TEXT.get((book, entry_id), extracted)


def printed_head_names(ledger: list[dict], entries: dict, entry_id: str) -> list[str]:
    """Include titles of options outside the rewrite, so their printed heads still bound adjacent text."""
    return ([row["feature"] for row in ledger]
            + [entry.title for entry in entries.values()]
            + CLASS_OPTIONS.fp.ITALIC_HEADS.get(entry_id, []))


def plain(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\\([*])", r"\1", text)
    return " ".join(text.replace("**", "").replace("_", "").split()).casefold()


def sentences(text: str) -> list[str]:
    text = plain(text)
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+(?=[a-z0-9])", text) if part.strip()]


DIGITS = re.compile(r"\d+")
WORD = re.compile(r"[a-z]+(?:['’][a-z]+)?|\d+", re.I)
LIGATURES = str.maketrans({"æ": "ae", "œ": "oe", "ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl"})


def words(text: str) -> list[str]:
    normalized = unicodedata.normalize("NFKD", plain(text)).translate(LIGATURES).replace("’", "'")
    return [word.casefold() for word in WORD.findall(normalized)]


def sentences_match(left: str, right: str) -> bool:
    left, right = plain(left), plain(right)
    if DIGITS.findall(left) != DIGITS.findall(right):
        return False
    if len(CLASS_OPTIONS.NEGATIONS.findall(left)) != len(CLASS_OPTIONS.NEGATIONS.findall(right)):
        return False
    a, b = words(left), words(right)
    if len(a) != len(b):
        return False
    differences = [(x, y) for x, y in zip(a, b) if x != y]
    if not differences:
        return True
    return (len(differences) == 1 and min(map(len, differences[0])) >= 6
            and CLASS_OPTIONS.one_misprint(*differences[0]))


def is_covered(sentence: str, body: str, errata: tuple[str, str] | None = None) -> tuple[bool, bool]:
    candidates = sentences(body)
    if any(sentences_match(sentence, candidate) for candidate in candidates):
        return True, False
    if errata:
        printed, corrected = errata
        printed_plain, corrected_plain = plain(printed), plain(corrected)
        sentence_plain = plain(sentence)
        candidates_plain = [plain(candidate) for candidate in candidates]
        if printed_plain in sentence_plain and any(corrected_plain in candidate for candidate in candidates_plain):
            return True, True
        if corrected_plain in sentence_plain and any(printed_plain in candidate for candidate in candidates_plain):
            return True, True
    return False, False


def tags_match(printed: str, ledger: str, entry: str) -> bool:
    return printed == ledger == entry


def starts_with_printed_intro(body: str, intro: str) -> bool:
    return bool(intro) and plain(body).startswith(plain(intro))


def hash_bound_print(row: dict[str, str], proposals: dict[tuple[str, str], str]) -> str | None:
    text = proposals.get((row["entry"], row["anchor"]))
    if text is None or hashlib.sha256(text.encode()).hexdigest() != row["print_sha256"]:
        return None
    return text


def source_page(front: str, book: str) -> str:
    match = re.search(rf'publication = "{re.escape(book)}"[^\n]*\npage = "([^"]+)"', front)
    return match.group(1) if match else ""


def extract_print(corpus: Path, book: str, books_dir: Path, cache_dir: Path) -> tuple[dict[tuple[str, str], tuple[str, str]], object, object]:
    """Return (entry, anchor) -> print text and head using the book's matching extraction path."""
    options = CLASS_OPTIONS
    fp = options.fp
    fp.configure_book(book)
    title = fp.publication_title(corpus, book)
    pdf = fp.find_pdf(books_dir, title)
    if not pdf:
        raise SystemExit(f"no copy of {title!r} under {books_dir}")
    source = fp.load_book(fp.book_xml(pdf, cache_dir))
    ledger_path = HERE / f"540-{book}.tsv"
    with ledger_path.open(encoding="utf-8", newline="") as f:
        ledger = list(csv.DictReader(f, delimiter="\t"))
    written = [row for row in ledger if row["status"] == "written" and row["shape"] == "single"]
    entries = {entry.id: entry for entry in options.load_class_options(corpus, book)}
    if book == "pathfinder-unchained":
        # The shared splitter cannot isolate this book's run-in heads in raw page
        # text. Its print-derived proposals are hash-bound to the compared spans.
        proposals = options.read_props(options.proposals_file(corpus, book))
        options.SENTENCE_AUDIT_SOURCE = source
        texts = {}
        for row in written:
            text = hash_bound_print(row, proposals)
            if text is None:
                continue
            if "opens with print's sentence about the mark" in row["note"]:
                intro = options.marked_head_intro(book, row["entry"])
                if intro and not text.startswith(intro):
                    text = intro + "\n\n" + text
            entry = entries.get(row["entry"])
            page_match = re.match(r"\d+", row["page"])
            if entry and entry.id.split("/")[1] == "unchevolution" and page_match:
                group = options.group_map(source).of(entry.title, int(page_match.group()))
                if group:
                    text = group[0] + "\n\n" + text
            texts[(row["entry"], row["anchor"])] = (text, row["feature"])
        return texts, entries, options
    printed_names = printed_head_names(ledger, entries, "")
    options.install_split(printed_names)

    intro_specs = options.INTRO_MARK_SPECS.get(book, {})
    for family, (marker, prefer) in intro_specs.items():
        intro = options.IntroMarkMap(source, marker, prefer)
        options.INTRO_MARK_TEXT[(book, family)] = (intro.text, intro.page)

    texts: dict[tuple[str, str], tuple[str, str]] = {}
    for row in written:
        entry = entries.get(row["entry"])
        page_numbers = [int(n) for n in re.findall(r"\d+", row["page"])]
        if entry is None or not page_numbers:
            continue
        page, last_page = page_numbers[0], page_numbers[-1]
        blocks = fp.read_blocks(source, max(1, page + fp.PAGE_OFFSET[0] - 1),
                                min(last_page + 2 + fp.PAGE_OFFSET[0], max(source.pages)))
        section = [fp.Para("title", [(entry.title, True, False)], page, 0, 20)] + blocks
        _, printed = fp.split_print(section, printed_head_names(ledger, entries, entry.id))
        wanted = fp.import_name(entry.id, row["feature"])
        wanted_key = fp.namekey(fp.ABILITY_TAG.sub("", wanted))
        matches = [feature for feature in printed
                   if fp.namekey(fp.ABILITY_TAG.sub("", fp.head_text(feature.head))) == wanted_key]
        if len(matches) != 1:
            continue
        feature = matches[0]
        links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", entry.body)
        vocab = source.vocab | {w.lower() for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", entry.body)}
        text, _, _ = fp.print_md(feature, links, vocab, entry.id)
        text = printed_region_text(book, entry.id, text)
        print_head = fp.head_text(feature.head)
        if book == "ultimate-wilderness":
            text, split_tag = options.strip_ultimate_wilderness_head_fragment(entry.id, text)
            if split_tag:
                print_head = f"{entry.title}† ({split_tag})"
        if entry.id in options.GROUP_LINE_ENTRIES:
            group = options.group_map(source).of(entry.title, page)
            if group:
                text = group[0] + "\n\n" + text
        family = entry.id.split("/")[1]
        if row["note"] and "opens with print's sentence about the mark" in row["note"]:
            intro = options.marked_head_intro(book, entry.id)
            if intro and not text.startswith(intro):
                text = intro + "\n\n" + text
        texts[(entry.id, row["anchor"])] = (text, print_head)
    return texts, entries, options


def self_test() -> int:
    checks = 0

    def eq(actual, expected, label):
        nonlocal checks
        checks += 1
        if actual != expected:
            print(f"FAIL: {label}: {actual!r} != {expected!r}")
            return False
        return True

    good = [
        ("A linked [rule](ref/rule) applies.", ["a linked rule applies."]),
        ("A first sentence. A second sentence!", ["a first sentence.", "a second sentence!"]),
        ("The ﬁrst-level effect deals +2 damage.", "The first-level effect deals +2 damage."),
    ]
    for source, expected in good:
        if isinstance(expected, list):
            if not eq(sentences(source), expected, "sentence split"):
                return 1
        else:
            if not eq(sentences_match(source, expected), True, "ligature equivalence"):
                return 1
    for left, right, label, expected in [
        ("The effect deals +2 damage.", "The effect deals +3 damage.", "changed number", False),
        ("The effect does not apply.", "The effect does apply.", "dropped negation", False),
        ("His ability is useful.", "Her ability is useful.", "pronoun substitution", False),
        ("The familiar can attack.", "The familar can attack.", "one omitted letter", True),
        ("The familiar can attack.", "The familiarS can attack.", "one suffix letter", True),
        ("The creature can attack.", "The creature can attacked.", "two-letter suffix near miss", False),
        ("Neither creature can attack.", "The creature can attack.", "dropped neither", False),
    ]:
        if not eq(sentences_match(left, right), expected, label):
            return 1

    class Entry:
        def __init__(self, title):
            self.title = title

    if not eq(printed_head_names([{"feature": "Free in Body"}], {"x": Entry("Greater Mask Misery")}, "x"),
              ["Free in Body", "Greater Mask Misery"], "printed heads include the title of an out-of-scope no-import option"):
        return 1
    if not eq(printed_region_text("occult-adventures", "ref/phrenicamp/mimic-metamagic", "a deliberately wrong proposal"),
              PRINT_REGION_TEXT[("occult-adventures", "ref/phrenicamp/mimic-metamagic")],
              "the sentence audit uses its own Occult Adventures p. 63 print transcription"):
        return 1
    if not eq("quicken" in words(printed_region_text("occult-adventures", "ref/phrenicamp/mimic-metamagic", "")), True,
              "the direct print transcription includes roman quicken, independent of the writer's override"):
        return 1
    if not eq(tags_match("", "Ex", ""), False, "imported tag absent from print" ):
        return 1
    if not eq(tags_match("Su", "Su", "Su"), True, "printed tag agrees across print, ledger, and entry"):
        return 1
    if not eq(starts_with_printed_intro("Intro.\n\nPower.", "Intro."), True, "entry opens with a claimed printed intro"):
        return 1
    if not eq(starts_with_printed_intro("Power.", "Intro."), False, "missing claimed printed intro is rejected"):
        return 1
    if not eq(CLASS_OPTIONS.leaked_head_fragment("†(Su): Power."), True, "a dagger and ability-tag head fragment is caught at body start"):
        return 1
    if not eq(CLASS_OPTIONS.leaked_head_fragment("Intro.\n\n(Ex): Power.", "Intro."), True, "a tag fragment after the intro is caught"):
        return 1
    if not eq(CLASS_OPTIONS.leaked_head_fragment("Intro.\n\nA complete sentence.", "Intro."), False, "ordinary prose after the intro is accepted"):
        return 1
    if not eq(starts_with_printed_intro("1-Point Evolutions: The following evolutions cost 1 point from the eidolon's evolution pool.\n\nPower.",
                                      "1-Point Evolutions: The following evolutions cost 1 point from the eidolon's evolution pool."),
              True, "evolution opens with its printed group sentence"):
        return 1
    if not eq(starts_with_printed_intro("Power.", "1-Point Evolutions: The following evolutions cost 1 point from the eidolon's evolution pool."),
              False, "evolution missing its printed group sentence is rejected"):
        return 1
    bound_row = {"entry": "ref/test/option", "anchor": "option", "print_sha256": hashlib.sha256(b"Printed text.").hexdigest()}
    if not eq(hash_bound_print(bound_row, {("ref/test/option", "option"): "Printed text."}), "Printed text.",
              "print-derived text is accepted when its ledger hash matches"):
        return 1
    if not eq(hash_bound_print(bound_row, {("ref/test/option", "option"): "Altered text."}), None,
              "edited proposal text is rejected when its ledger hash differs"):
        return 1
    if not eq(is_covered("an entry-only sentence.", "a printed sentence."), (False, False), "entry-only sentence is absent from print"):
        return 1
    if not eq(is_covered("The text has an extra word.", "The text has a word.", ("extra word", "word")),
              (True, True), "a recorded erratum explains a certain print correction"):
        return 1
    print(f"self-test: {checks} checks passed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("corpus", type=Path, nargs="?", default=Path("."))
    ap.add_argument("book", nargs="?", default="")
    ap.add_argument("--books", type=Path, help="directory containing the source PDFs")
    ap.add_argument("--cache", type=Path, help="PDF text cache directory")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not (args.book and args.books and args.cache):
        ap.error("book, --books, and --cache are required")

    rows = list(csv.DictReader((args.corpus / "scripts/class-options" / f"540-{args.book}.tsv").open(encoding="utf-8"), delimiter="\t"))
    entries = {}
    pages = {}
    fronts = {}
    for path in (args.corpus / "entries").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        parts = text.split("+++\n", 2)
        if len(parts) != 3:
            continue
        match = re.search(r'^id = "([^"]+)"$', parts[1], re.M)
        if match:
            entries[match.group(1)] = plain(parts[2])
            pages[match.group(1)] = source_page(parts[1], args.book)
            fronts[match.group(1)] = parts[1]

    printed, entries_raw, options = extract_print(args.corpus, args.book, args.books, args.cache)
    errata_by_entry = {}
    errata_path = args.corpus / "scripts/errata.tsv"
    if errata_path.exists():
        with errata_path.open(encoding="utf-8", newline="") as f:
            for erratum in csv.DictReader(f, delimiter="\t"):
                if erratum["book"] == args.book and erratum["decision"] == "misprint-fix":
                    errata_by_entry[erratum["entry"]] = (erratum["printed_value"], erratum["kept_value"])
    written = [row for row in rows if row["status"] == "written" and row["shape"] == "single"]
    print_found = print_total = entry_found = entry_total = 0
    page_matches = tag_matches = 0
    exceptions = []
    corrections = []
    for row in written:
        key = (row["entry"], row["anchor"])
        source = printed.get(key)
        body = entries.get(row["entry"])
        if source is None or body is None:
            exceptions.append(f"{row['entry']}#{row['anchor']}: no unique printed head or entry body")
            continue
        print_text, print_head = source
        entry_page = pages.get(row["entry"], "")
        if args.book == "pathfinder-unchained" and row["entry"].split("/")[1] == "unchevolution":
            entry_pages = re.findall(r"\d+", entry_page)
            page_ok = bool(row["page"] and entry_pages and entry_pages[-1] == row["page"])
        else:
            page_ok = entry_page == row["page"] and bool(row["page"])
        if page_ok:
            page_matches += 1
        else:
            exceptions.append(f"PAGE {row['entry']}: ledger page {row['page']!r}, entry page {entry_page!r}")

        front = fronts[row["entry"]]
        fields = re.search(r"(?ms)^\[fields\]\n(.*?)(?:\n\[|\Z)", front)
        ability = re.search(r'^ability_type = "([^"]+)"$', fields.group(1), re.M) if fields else None
        printed_tag = options.ability_tag_of_printed_head(print_head)
        entry_tag = ability.group(1) if ability else ""
        if tags_match(printed_tag, row["ability_tag"], entry_tag):
            tag_matches += 1
        else:
            exceptions.append(f"TAG {row['entry']}: print {printed_tag!r}, ledger {row['ability_tag']!r}, entry {entry_tag!r}")

        if "opens with print's sentence about the mark" in row["note"]:
            intro = options.marked_head_intro(args.book, row["entry"])
            if not intro or not starts_with_printed_intro(body, intro):
                exceptions.append(f"INTRO {row['entry']}: ledger claims a key-marked head but the entry lacks its printed intro")
        if options.leaked_head_fragment(body, options.marked_head_intro(args.book, row["entry"])):
            exceptions.append(f"HEAD FRAGMENT {row['entry']}: body starts with a leaked key mark or ability-tag fragment")
        if args.book == "pathfinder-unchained" and row["entry"].split("/")[1] == "unchevolution":
            source_book = getattr(options, "SENTENCE_AUDIT_SOURCE", None)
            page_start = re.match(r"\d+", row["page"])
            group = options.group_map(source_book).of(entries_raw[row["entry"]].title, int(page_start.group())) if source_book and page_start else None
            if not group or not starts_with_printed_intro(body, group[0]):
                exceptions.append(f"GROUP INTRO {row['entry']}: missing printed evolution group sentence")
        source_sentences = sentences(print_text)
        entry_sentences = sentences(body)
        errata = errata_by_entry.get(row["entry"])
        for sentence in source_sentences:
            print_total += 1
            covered, corrected = is_covered(sentence, body, errata)
            if covered:
                print_found += 1
                if corrected:
                    corrections.append(f"ERRATA {row['entry']}: printed wording corrected under ruling 43")
            else:
                exceptions.append(f"PRINT -> ENTRY {row['entry']}#{row['anchor']}: not found: {sentence}")
        for sentence in entry_sentences:
            entry_total += 1
            covered, corrected = is_covered(sentence, print_text, errata)
            if covered:
                entry_found += 1
                if corrected:
                    corrections.append(f"ERRATA {row['entry']}: corrected wording maps to print under ruling 43")
            else:
                exceptions.append(f"ENTRY -> PRINT {row['entry']}#{row['anchor']}: extra: {sentence}")
    print(f"Print -> entry: {print_found} of {print_total} sentences found in {len(written)} written entries")
    print(f"Entry -> print: {entry_found} of {entry_total} sentences found in printed page text")
    print(f"Page metadata: {page_matches} of {len(written)} written entries match the ledger")
    print(f"Printed ability tags: {tag_matches} of {len(written)} match the print head, ledger, and entry field")
    for correction in corrections:
        print(f"CORRECTION: {correction}")
    for exc in exceptions:
        print(f"EXCEPTION: {exc}")
    return 1 if exceptions else 0


if __name__ == "__main__":
    sys.exit(main())
