#!/usr/bin/env python3
"""Screen book memberships against print (phynics/cast-iron#461, from #457).

Since #434 every book in an entry's `source_ids` makes the entry a member of that book. This
script finds memberships that the book may not print. It reads the corpus and the owner's PDFs
and writes a TSV queue. The queue holds ids, titles, book ids and page numbers. It never holds
PDF text, never prints it, and keeps PDF file names and paths out of every message.

    python3 scripts/membership-screen.py <corpus-dir> --pdf-dir <dir> --out queue.tsv \
        [--text-cache <dir>] [--books id,id] [--jobs 3]

Needs `pdftotext` (poppler) on PATH, Python 3.11+, and no other packages. The text cache is the
only place that holds extracted text. It must be outside the corpus and outside any git
repository (the script refuses otherwise); an entry is extracted again when its PDF changes.
Without --text-cache it uses a temporary directory and removes it at the end. A PDF that fails to
extract is named by publication id only, and the run exits with status 1.

THE QUEUE IS A LIST OF HYPOTHESES, NOT PROOF. A tag says why a membership looks unprinted. It
never authorises a removal: each row needs a print check (the cited page, and any table, sidebar
or renamed section that holds the entry) and a recorded verdict before it is removed. A script
may then apply only the approved rows. See the `verdict` and `print_page` columns.

What is screened
  Every (entry, book) pair where the entry has more than one `source_ids` book and the book has
  an owner PDF (matched to `publications.toml` by title, so no file name appears in any output).
  Linked entries with one book are screened as well, only as family evidence, and are not queued.
    * The entry has a `[[sources]]` row for the book with a page: the title must be printed on
      that page or the page before or after it (printed page numbers; a range covers all of it).
    * Otherwise (no row, or a row without a page): the title must be printed anywhere in the
      book. A page from a body `**Sources:** Book pg N` line is used like a row page.
  "Title" is the entry title without parentheticals such as "(Familiar)", also with a comma
  inversion ("Cure Light Wounds, Mass" -> "Mass Cure Light Wounds"), with an optional plural,
  and with or without a leading "The". The match is on whole words, with punctuation, case and
  hyphenation at line ends ignored. It is a heuristic: a plural in print for a singular title is
  found only for the "-s", "-es" and "-f/-ves" forms, and a parenthetical can be what tells two
  entries apart. The `body` and `loose` passes below are weaker evidence than a title.

Status of each pair
  printed   the title is on the cited page window (row) or on at least `--weak-pages`+1 pages
            of the book (no row)
  body      the title is not on the window (row) or on at most `--weak-pages` pages (no row),
            but six words in a row from each of up to three places in the entry's own prose are
            on the window or anywhere in the book (a prose of 6 to 11 words is one run). Counted
            as printed; not queued. Tables, stat blocks and headings are not part of the prose.
  loose     a row, the exact title is not on the window, but every word of it is (a variant or a
            table row printed in another order). Counted as printed; not queued.
  weak      no row, no body match, and the title is on 1..`--weak-pages` pages of the book: a
            mention at most. About half of these are printed.
  off-page  a row, the title (or the body prose) is not on the window but is elsewhere in the
            book: the page citation is off, which is not an unprinted membership
  absent    nothing of the above
  unaligned the book's page numbers could not be read (fewer than --min-align of its pages
            carry a number that agrees with their neighbours): no verdict of any kind for any of
            its memberships, and no page numbers. Not queued.
  no-text   the PDF has no text layer. Not queued.

Tag of each queued pair
  hub-keep     the entry is a hub (kind rule/ability/misc whose body opens "These topics" or has
               two or more per-section `**Sources:**` lines). The owner keeps hub memberships.
               Never a removal.
  family-leak  an entry linked by `variant`/`addon` (either direction), its `parent`, or one of
               its children prints the title in this book (that entry's own status is printed
               or body)
  inherited    its parent has the same book in `source_ids`, and the entry has no row for it
  uncited      the book is in `source_ids` with no `[[sources]]` row
  review       none of the above
  weak, cite-off   for status weak and off-page. These are not removal candidates.
A pair gets the first tag that fits, in the order above. The TSV also carries `via`
(variant|addon|parent|child), so every tag can be split further.

Columns of the TSV: book, entry, kind, title, member (1 = first book of `source_ids`), n_books,
tag, status, cited (page text of the row or body line), cite (row|body|none), hits (pages of the
book that print the title or body text, no-row checks and off-page rows), found (printed numbers
of the first five of those pages), via (variant|addon|parent|child), family (up to three linked
entries that print there, each with the evidence: title or body), parent_has_book (yes when the
entry's parent lists the book).
  gate  `primary` on a row that is the entry's first book (not hub-keep or cite-off). Removing it
        changes the entry's primary book, so it is never part of a scripted batch. The reviewer
        records the old and the proposed primary, checks that the proposed primary prints the
        entry, keeps at least one supported membership, and decides on its own.
  proposed_primary, proposed_status  on a gated row: the first later book that is not itself a
        removal candidate for the entry, and this script's status for it ("unscreened" without
        a PDF; "(none)" when every other book is a removal candidate)
  verdict, print_page, evidence  empty. The reviewer's decision (`remove`, `keep`, `expands`) and
        the printed page that decides it, and a short code for what the print check found:
        `race-section-read-no-trait` (the book's section for the race was read; it does not print
        the trait), `race-section-read-mention-only` (the same, and the trait is named in passing
        or in a `replaces` line only), `no-race-section-no-trait`. For other kinds:
        `section-read-no-entry` (the chapter that would hold the entry was read and the whole
        book searched for its title and for runs of its text; it is not printed),
        `wrong-credit-invalidated` (the entry's page row names this book, the cited page was
        read, and the book does not print the entry there or elsewhere: the page prints another
        entry, usually a sibling variant. The rejected row is recorded in
        `scripts/membership-citation-audit-461.tsv`), `reference-kept-on-related` (the cited page
        prints a related entry that lists the book, cites an overlapping page and has a
        relations edge to this entry; the audit file names it), `title-printed` (keep: the entry
        is printed on the page), `passing-mention-recorded` (remove: the book only names the entry in
        passing and no related entry carries the page; the audit file records the page and the
        kind of mention, class `mention`), `wrong-credit-invalidated` also covers an entry whose printed counterpart
        differs materially (an affliction with other numbers than the book prints).
        Batch 4 adds: `whole-book-absent` (no `[[sources]]` row and no body line; the whole book was
        searched for the title and for runs of the entry's prose, and neither is printed),
        `whole-book-absent-new-primary-printed` (the same for the entry's first book. The row is
        `gate = primary`, and `proposed_primary`, which becomes first, prints the entry on
        `print_page`: `proposed_status` `printed` when its title is on the cited page, `body` when
        runs of the entry's prose are), `mention-only` (the book names the entry in passing and
        prints nothing of it; the entry has no row for the book, so there is no page to invalidate),
        `expansion-credited-on-related` (remove: the book prints an option for the entry on
        `print_page`, and an entry that links it already credits that page),
        `expansion-credited-via-upa-1` (verdict `expands`: the printed text is in a related entry
        that already cites the page; the overview entry gets an `[[expanded_in]]` credit through
        `scripts/expansion-credits-apply.py`, decisions in `scripts/expansion-credits-461-batch4.tsv`),
        `section-printed` (keep: the book prints a section of the entry's body on `print_page`; a
        keep needs a `[[sources]]` row, and the row is added when the entry holds only a body line).
        A re-run overwrites the queue; scripts/membership-apply.py applies the rows marked `remove`
        and `cite`. Since S0 of #461 the queue is kept by scripts/membership-queue-461.py, which
        adds the columns `group`, `slice`, `waits`, `in_warning`, `pdf`, `body_line`, `exact` and
        `paren`, the verdicts `cite` and `resolved`, and the rows that this screen does not queue
        (see scripts/membership-queue-461.md). `--status-out` writes its input.

Known limits (see the PR for the calibration): no-PDF memberships and books without readable
page numbers are not judged, and neither says anything about absence. A hub-looking entry that
does not match the hub rule above lands in `uncited`/`review` and needs the owner.

Output is deterministic: sorted, no timestamps. Run `python3 scripts/membership-screen.py -h`.
"""
from __future__ import annotations

import argparse
import bisect
import collections
import concurrent.futures
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unicodedata
from pathlib import Path

TAG_ORDER = ["hub-keep", "family-leak", "inherited", "uncited", "review", "weak", "cite-off"]
REMOVAL_TAGS = ("family-leak", "inherited", "uncited", "review")
HUB_KINDS = ("rule", "ability", "misc")

# Publication id -> other spellings of the title that the owner's PDF uses.
ALT_TITLES = {
    "pathfinder-campaign-setting": ["Pathfinder Chronicles Campaign Setting"],
    "blood-of-the-beast": ["Blood of Beasts"],
    "faiths-of-balance": ["Faiths of the Balance"],
    "construct-handbook": ["Constructs Handbook"],
    "osirion-land-of-the-pharaohs": ["Osirion, Land of Pharaohs"],
    "osirion-legacy-of-the-pharaohs": ["Osirion, Legacy of Pharaohs"],
    "demons-revisited": ["Demons Revisted"],
    "rivers-into-darkness": ["River into Darkness"],
}


# ---------------------------------------------------------------------------------- text helpers


def fold(s: str) -> str:
    """Lowercase ASCII with every run of non-alphanumerics (apostrophes dropped) as one space."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = s.replace("&", " and ")
    s = re.sub(r"['`]", "", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def squash(s: str) -> str:
    return fold(s).replace(" ", "")


def pdf_stem_title(stem: str) -> str:
    """The book title in a PDF file name: no product code, edition note or module code."""
    s = re.sub(r"^[A-Z]{2,4}\d[\w.-]*\s+", "", stem)  # a leading product code
    s = re.sub(r"^Pathfinder\s*\[[^\]]*\]\s*", "", s)
    s = re.sub(r"\s*\([^)]*\)", "", s)
    s = re.sub(r"^[A-Z]{1,2}\d(?:\.\d)?\s*-\s*", "", s)
    s = re.sub(r"\s+LV\s*\d+$", "", s)
    return s.strip()


def title_key(s: str) -> str:
    k = fold(s)
    k = re.sub(r"\bvolume\b|\bvol\b", "vol", k)
    k = re.sub(r"^the ", "", k)
    return k.replace(" ", "")


STOP = {"of", "the", "and", "a", "an", "to", "in", "for", "or", "on", "at", "with"}


def loose_words(title: str) -> set[str] | None:
    """The words of a title for the all-words test, or None when that test would be too weak.

    It needs two words of three letters or more, and the title must not end in a numeral, since
    "Summon Monster II" would then pass wherever "Summon Monster III" is printed."""
    base = re.sub(r"\s*\([^)]*\)", "", title).strip() or title
    toks = fold(base).split()
    if not toks or re.fullmatch(r"\d+|[ivxlc]+", toks[-1]):
        return None
    words = {t[:-1] if t.endswith("s") else t for t in toks if t not in STOP and len(t) >= 3}
    return words if len(words) >= 2 else None


def body_chunks(body: str) -> list[re.Pattern]:
    """Three runs of six words from the entry's own prose: start, a third in, two thirds in.

    A run of words printed in a book is stronger evidence than a title, because many entries
    (racial traits, stat blocks, variants) have a title the book never prints as such. Stat
    blocks, tables and headings are left out; links and emphasis are reduced to their words."""
    keep = []
    in_block = False
    for line in body.splitlines():
        if line.startswith(":::"):
            in_block = not in_block if "statblock" in line or in_block else in_block
            continue
        if in_block or line.startswith(("|", "#", "<", "---")):
            continue
        keep.append(line)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", " ".join(keep))
    toks = fold(text).split()[:400]
    if len(toks) < 6:
        return []
    if len(toks) < 12:  # short prose: one run of all its words, up to ten
        return [re.compile(r"(?<![a-z0-9])" + r"\ ".join(map(re.escape, toks[:10])) + r"(?![a-z0-9])")]
    n = 6
    starts = sorted({0, len(toks) // 3, 2 * len(toks) // 3})
    starts = [p for p in starts if p + n <= len(toks)]
    return [re.compile(r"(?<![a-z0-9])" + r"\ ".join(map(re.escape, toks[p:p + n])) + r"(?![a-z0-9])")
            for p in starts]


def title_patterns(title: str) -> list[str]:
    """Regex source for each way the title can be printed. Text is folded to single spaces."""
    base = re.sub(r"\s*\([^)]*\)", "", title).strip() or title
    forms = {base}
    if "," in base:
        head, tail = base.split(",", 1)
        forms.add(f"{tail.strip()} {head.strip()}")
    for f in list(forms):
        if f.lower().startswith("the "):
            forms.add(f[4:])
    out = []
    for f in sorted(forms):
        toks = fold(f).split()
        if not toks:
            continue
        last = re.escape(toks[-1]) + r"(?:s|es)?"
        if toks[-1].endswith("f") or toks[-1].endswith("fe"):  # elf -> elves
            last = "(?:" + last + "|" + re.escape(toks[-1].rstrip("e")[:-1]) + "ves)"
        body = r"\ ".join([re.escape(t) for t in toks[:-1]] + [last])
        out.append(r"(?<![a-z0-9])" + body + r"(?![a-z0-9])")
    return out


def paren_pattern(title: str) -> re.Pattern | None:
    """The parenthetical of a title ("Figurine of Wondrous Power (Slate Spider)" -> "Slate Spider")
    as a pattern, or None. A parenthetical of fewer than five letters, or one of GENERIC_PARENS
    ("Familiar", "Mass", "Lesser"), tells no two entries apart, so it gives None."""
    m = re.search(r"\(([^)]*)\)", title)
    if not m:
        return None
    inner = fold(m.group(1))
    if len(inner.replace(" ", "")) < 5 or inner in GENERIC_PARENS:
        return None
    pats = title_patterns(m.group(1))
    return re.compile("|".join(pats)) if pats else None


GENERIC_PARENS = {"familiar", "creature", "spell", "feat", "trait", "item", "class", "mythic", "variant",
                  "lesser", "greater", "mass", "communal", "alchemical", "magic item", "optional rule"}


# ------------------------------------------------------------------------------------- the book


class Book:
    """The text of one PDF, one folded string per page, with printed page numbers."""

    def __init__(self, raw_pages: list[str]):
        self.n = len(raw_pages)
        self.text = []
        for raw in raw_pages:
            dehyph = re.sub(r"(?<=[A-Za-z])-\s*\n\s*(?=[a-z])", "", raw)
            self.text.append(fold(dehyph) + " @@ " + fold(raw))
        self.words = [{w[:-1] if w.endswith("s") else w for w in t.split()} for t in self.text]
        self.printed, self.align = self._printed_numbers(raw_pages)
        self.by_printed: dict[int, list[int]] = collections.defaultdict(list)
        for i, n in enumerate(self.printed):
            self.by_printed[n].append(i)
        self.whole = "\n".join(self.text)
        self.starts = []
        pos = 0
        for t in self.text:
            self.starts.append(pos)
            pos += len(t) + 1

    @staticmethod
    def _printed_numbers(raw_pages: list[str]) -> tuple[list[int], float]:
        """Printed page number of each PDF page, from the page numbers at its head and foot.

        Each page votes for (pdf index - number) offsets. The offset of a page is the commonest
        vote among the pages around it, so an inserted plate or a missing number does not
        shift the rest of the book. The second value is the share of pages whose own vote
        agrees with that offset: a low share means the numbers could not be read."""
        votes: list[list[int]] = []
        for i, raw in enumerate(raw_pages):
            lines = [l.strip() for l in raw.splitlines() if l.strip()]
            cand = []
            for l in lines[:3] + lines[-3:]:
                m = re.fullmatch(r"(\d{1,3})", l)
                if m:
                    cand.append((int(m.group(1)), 2))
                    continue
                m = re.fullmatch(r"(\d{1,3})\s+\S.*|.*\S\s+(\d{1,3})", l)
                if m and len(l) < 80:
                    cand.append((int(m.group(1) or m.group(2)), 1))
            v = []
            for n, w in cand:
                off = (i + 1) - n
                if -6 <= off <= 80:
                    v += [off] * w
            votes.append(v)
        overall = collections.Counter(o for v in votes for o in v)
        default = overall.most_common(1)[0][0] if overall else 0
        out = []
        agree = 0
        for i in range(len(raw_pages)):
            window = collections.Counter()
            for j in range(max(0, i - 7), min(len(raw_pages), i + 8)):
                window.update(votes[j])
            off = window.most_common(1)[0][0] if window else default
            agree += off in votes[i]
            out.append((i + 1) - off)
        return out, agree / max(1, len(raw_pages))

    def window_pages(self, a: int, z: int) -> list[int]:
        idx = []
        for n in range(a - 1, z + 2):
            idx += self.by_printed.get(n, [])
        return sorted(set(idx))

    def window(self, a: int, z: int) -> str:
        """The text of the pages whose printed number is in a-1 .. z+1."""
        return " ## ".join(self.text[i] for i in self.window_pages(a, z))

    def exact(self, a: int, z: int) -> str:
        """The text of the pages whose printed number is in a .. z (no page before or after)."""
        idx = sorted({i for n in range(a, z + 1) for i in self.by_printed.get(n, [])})
        return " ## ".join(self.text[i] for i in idx)

    def window_has_words(self, a: int, z: int, words: set[str]) -> bool:
        have = set().union(*(self.words[i] for i in self.window_pages(a, z))) if self.by_printed else set()
        return words <= have

    def pages_with(self, rx: re.Pattern, cap: int = 40) -> list[int]:
        """Printed numbers of the pages the pattern is on (first `cap` hits)."""
        found = []
        for m in rx.finditer(self.whole):
            i = bisect.bisect_right(self.starts, m.start()) - 1
            if not found or found[-1] != i:
                found.append(i)
            if len(found) >= cap:
                break
        return found


# ------------------------------------------------------------------------------------- loaders


def load_corpus(root: Path):
    pubs = {p["id"]: p for p in tomllib.loads((root / "publications.toml").read_text())["publication"]}
    entries = {}
    for f in sorted((root / "entries").rglob("*.md")):
        s = f.read_text()
        if not s.startswith("+++"):
            continue
        _, fm, body = s.split("+++", 2)
        d = tomllib.loads(fm)
        d["_body"] = body
        entries[d["id"]] = d
    return pubs, entries


def body_pages(body: str, title_to_pub: dict[str, str]) -> dict[str, str]:
    """`**Sources:** Book pg N, Book pg N` lines in a body: publication id -> page text."""
    out = {}
    for m in re.finditer(r"^\*\*Sources?:\*\*\s*(.+)$", body, re.M):
        for part in re.split(r",\s*(?=[A-Z])", m.group(1).rstrip("\\ ")):
            mm = re.fullmatch(r"(.+?)\s+pg\s+(\d+(?:-\d+)?)", part.strip())
            if mm and title_key(mm.group(1)) in title_to_pub:
                out.setdefault(title_to_pub[title_key(mm.group(1))], mm.group(2))
    return out


def is_hub(d: dict) -> bool:
    """A container entry that collects sections from several books ("Rare Races", "Advanced GM
    Topics"): its body opens "These topics ...", or it has two or more per-section `**Sources:**`
    lines. No book prints it under its own title, and the owner keeps its memberships."""
    if d["kind"] not in HUB_KINDS:
        return False
    body = d["_body"].strip()
    return bool(re.match(r"These topics\b", body)) or len(re.findall(r"^\*\*Sources?:\*\*", body, re.M)) >= 2


def parse_pages(page: str) -> list[tuple[int, int]]:
    spans = []
    for part in re.split(r"\s*,\s*", page or ""):
        m = re.fullmatch(r"(\d+)(?:\s*[-–]\s*(\d+))?", part.strip())
        if not m:
            continue
        a = int(m.group(1))
        z = int(m.group(2)) if m.group(2) else a
        if z < a:  # "142-3"
            z = int(str(a)[: len(str(a)) - len(m.group(2))] + m.group(2))
        spans.append((a, z))
    return spans


def match_pdfs(pdf_dir: Path, pubs: dict, wanted: set[str]) -> dict[str, Path]:
    """Publication id -> PDF, by title only. The first file wins when two share a title."""
    keys: dict[str, list[str]] = collections.defaultdict(list)
    for pid in sorted(wanted):
        for t in [pubs[pid]["title"], *ALT_TITLES.get(pid, [])]:
            keys[title_key(t)].append(pid)
    out: dict[str, Path] = {}
    for f in sorted(pdf_dir.rglob("*.pdf")):
        for pid in keys.get(title_key(pdf_stem_title(f.stem)), []):
            out.setdefault(pid, f)
    return out


def extract(pdf: Path, dest: Path, tool: str) -> str | None:
    """Extract one PDF into the cache. Returns None, or an error text with no path in it.

    The cache entry is valid only while the PDF has the size and modification time that its
    `.src` stamp records, so a replaced PDF is extracted again."""
    try:
        st = pdf.stat()
        stamp = f"{st.st_size}:{st.st_mtime_ns}"
        src = dest.with_suffix(".src")
        if dest.exists() and src.exists() and src.read_text() == stamp:
            return None
        tmp = dest.with_suffix(".part")
        subprocess.run([tool, "-enc", "UTF-8", str(pdf), str(tmp)], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=900)
        tmp.replace(dest)
        src.write_text(stamp)
    except subprocess.CalledProcessError as e:
        return f"pdftotext exit status {e.returncode}"
    except subprocess.TimeoutExpired:
        return "pdftotext timed out"
    except OSError as e:
        return f"{type(e).__name__}"  # the message can name a file
    return None


# --------------------------------------------------------------------------------------- screen


def screen(args) -> int:
    root = Path(args.corpus).resolve()
    pubs, entries = load_corpus(root)
    title_to_pub = {}
    for pid, p in pubs.items():
        title_to_pub.setdefault(title_key(p["title"]), pid)
        for t in ALT_TITLES.get(pid, []):
            title_to_pub.setdefault(title_key(t), pid)

    multi = {e: d for e, d in entries.items() if len(d.get("source_ids", [])) > 1}
    members = collections.defaultdict(list)  # book -> [entry ids]
    for e, d in sorted(multi.items()):
        for b in d["source_ids"]:
            members[b].append(e)
    links = build_links(entries)
    # Linked entries with a single book are screened too, as family evidence only (never queued).
    screen_set = {b: list(v) for b, v in members.items()}
    for e in sorted(multi):
        for kind in links.get(e, {}):
            for o in sorted(links[e][kind]):
                for b in multi[e]["source_ids"]:
                    if b in entries[o].get("source_ids", []) and o not in screen_set[b]:
                        screen_set[b].append(o)
    wanted = {b for b in members if b in pubs}
    if args.books:
        wanted &= set(args.books.split(","))
    if not Path(args.pdf_dir).is_dir():
        sys.exit("--pdf-dir is not a directory")
    pdfs = match_pdfs(Path(args.pdf_dir), pubs, wanted)

    cache_owned = args.text_cache is None
    cache = Path(args.text_cache) if args.text_cache else Path(tempfile.mkdtemp(prefix="membership-"))
    cache = cache.resolve()
    if root == cache or root in cache.parents or any((p / ".git").exists() for p in [cache, *cache.parents]):
        sys.exit("--text-cache must be outside the corpus and outside any git repository")
    cache.mkdir(parents=True, exist_ok=True)
    try:
        with concurrent.futures.ThreadPoolExecutor(args.jobs) as ex:
            results = list(ex.map(lambda b: (b, extract(pdfs[b], cache / f"{b}.txt", args.pdftotext)), sorted(pdfs)))
        failed = {b: err for b, err in results if err}
        for b, err in sorted(failed.items()):
            print(f"extraction failed: {b}: {err}", file=sys.stderr)
            pdfs.pop(b)
        rc = run(args, root, pubs, entries, multi, members, screen_set, links, pdfs, cache, title_to_pub)
        return 1 if failed else rc
    finally:
        if cache_owned:
            shutil.rmtree(cache, ignore_errors=True)


def build_links(entries) -> dict[str, dict[str, set[str]]]:
    """Relations in both directions (variant, addon) and parent / children."""
    links: dict[str, dict[str, set[str]]] = collections.defaultdict(lambda: collections.defaultdict(set))
    for e, d in entries.items():
        for r in d.get("relations", []):
            if r["kind"] in ("variant", "addon") and r["target"] in entries:
                links[e][r["kind"]].add(r["target"])
                links[r["target"]][r["kind"]].add(e)
        p = d.get("parent")
        if p and p in entries:
            links[e]["parent"].add(p)
            links[p]["child"].add(e)
    return links


def run(args, root, pubs, entries, multi, members, screen_set, links, pdfs, cache, title_to_pub) -> int:
    status: dict[tuple[str, str], dict] = {}
    quality = {}
    for book in sorted(pdfs):
        try:
            raw = (cache / f"{book}.txt").read_text(encoding="utf-8", errors="replace").split("\f")
        except OSError as e:
            print(f"cannot read the cached text of {book}: {type(e).__name__}", file=sys.stderr)
            continue
        if raw and not raw[-1].strip():
            raw.pop()
        if sum(len(p.strip()) for p in raw) < 2000:
            for e in screen_set[book]:
                status[(e, book)] = {"status": "no-text"}
            quality[book] = (len(members[book]), 0, 0, "no-text", 0.0)
            continue
        bk = Book(raw)
        rows = hit = 0
        res = {}
        for e in screen_set[book]:
            d = entries[e]
            rx = re.compile("|".join(title_patterns(d["title"]))) if title_patterns(d["title"]) else None
            row = next((s for s in d.get("sources", []) if s["publication"] == book), None)
            page = (row or {}).get("page") or ""
            cite = "row" if page else "none"
            if not page:
                bp = body_pages(d["_body"], title_to_pub).get(book)
                if bp:
                    page, cite = bp, "body"
            spans = parse_pages(page)
            chunks = body_chunks(d["_body"])
            r = {"has_row": row is not None, "cited": page, "cite": cite, "hits": 0, "found": [],
                 "exact": "", "paren": ""}
            if spans and rx is not None:  # the title on the cited pages themselves, no page before or after
                r["exact"] = "yes" if any(rx.search(bk.exact(a, z)) for a, z in spans) else "no"
            prx = paren_pattern(d["title"])
            if prx is not None:  # the parenthetical (a variant name) says what the title alone cannot
                if spans and any(prx.search(bk.exact(a, z)) for a, z in spans):
                    r["paren"] = "page"
                else:
                    r["paren"] = "book" if bk.pages_with(prx, 1) else "none"
            if rx is None:
                r["status"] = "absent"
            elif spans:
                rows += 1
                lw = loose_words(d["title"])
                if any(rx.search(bk.window(a, z)) for a, z in spans):
                    r["status"] = "printed"
                    hit += 1
                elif any(c.search(bk.window(a, z)) for c in chunks for a, z in spans):
                    r["status"] = "body"
                elif lw and any(bk.window_has_words(a, z, lw) for a, z in spans):
                    r["status"] = "loose"
                else:
                    pg = bk.pages_with(rx) or sorted({i for c in chunks for i in bk.pages_with(c, 5)})
                    r["hits"] = len(pg)
                    r["found"] = [bk.printed[i] for i in pg[:5]]
                    r["status"] = "off-page" if pg else "absent"
            else:
                pg = bk.pages_with(rx)
                body_pg = []
                if len(pg) <= args.weak_pages:
                    body_pg = sorted({i for c in chunks for i in bk.pages_with(c, 5)})
                if body_pg:  # the book prints the entry's own text: supported, not weak
                    pg, r["status"] = body_pg, "body"
                else:
                    r["status"] = "absent" if not pg else ("weak" if len(pg) <= args.weak_pages else "printed")
                r["hits"] = len(pg)
                r["found"] = [bk.printed[i] for i in pg[:5]]
            res[e] = r
        rate = hit / rows if rows else 1.0
        aligned = bk.align >= args.min_align
        quality[book] = (len(members[book]), rows, rate, "ok" if aligned else "unaligned", bk.align)
        for e, r in res.items():
            if not aligned:  # no readable page numbers: no verdict of any kind, and no page numbers
                r = {"status": "unaligned", "has_row": r["has_row"], "cited": r["cited"], "cite": r["cite"],
                     "hits": 0, "found": [], "exact": "", "paren": ""}
            status[(e, book)] = r

    def prints_there(e: str, book: str) -> bool:
        s = status.get((e, book))
        return bool(s) and s["status"] in ("printed", "body")  # not loose, not weak: too permissive

    allrows = []  # one row per screened membership, whatever its status
    for (e, book), r in sorted(status.items()):
        st = r["status"]
        if e not in multi:
            continue
        d = entries[e]
        lk = links.get(e, {})
        via = []
        fam = []
        for kind in ("variant", "addon", "parent", "child"):
            for o in sorted(lk.get(kind, ())):
                if book in entries[o].get("source_ids", []) and prints_there(o, book):
                    via.append(kind)
                    fam.append(f"{o}({'title' if status[(o, book)]['status'] == 'printed' else 'body'})")
        parent = d.get("parent")
        parent_has = bool(parent and parent in entries and book in entries[parent].get("source_ids", []))
        if is_hub(d):
            tag = "hub-keep"
        elif st == "weak":
            tag = "weak"
        elif st == "off-page":
            tag = "cite-off"
        elif fam:
            tag = "family-leak"
        elif parent_has and not r["has_row"]:
            tag = "inherited"
        elif not r["has_row"]:
            tag = "uncited"
        else:
            tag = "review"
        allrows.append({
            "book": book, "entry": e, "kind": d["kind"], "title": d["title"].replace("\t", " "),
            "member": d["source_ids"].index(book) + 1, "n_books": len(d["source_ids"]),
            "tag": tag, "status": st, "cited": r["cited"], "cite": r["cite"], "hits": r["hits"],
            "found": ",".join(map(str, r["found"])),
            "via": ",".join(dict.fromkeys(via)), "family": ",".join(fam[:3]),
            "parent_has_book": "yes" if parent_has else "",
            "gate": "", "proposed_primary": "", "proposed_status": "", "verdict": "", "print_page": "", "evidence": "",
            "has_row": "yes" if r["has_row"] else "", "exact": r.get("exact", ""), "paren": r.get("paren", ""),
        })
    queue = [q for q in allrows if q["status"] not in ("printed", "body", "loose", "unaligned", "no-text")]
    # First-book rows change the entry's primary book when removed: gate them, and name the book
    # that would become primary (the first later book that is not itself a removal candidate).
    removal_books = collections.defaultdict(set)
    for q in queue:
        if q["tag"] in REMOVAL_TAGS:
            removal_books[q["entry"]].add(q["book"])
    for q in queue:
        if q["member"] == 1 and q["tag"] not in ("hub-keep", "cite-off"):
            q["gate"] = "primary"
            rest = [b for b in entries[q["entry"]]["source_ids"][1:] if b not in removal_books[q["entry"]]]
            q["proposed_primary"] = rest[0] if rest else "(none)"
            if rest:
                q["proposed_status"] = status.get((q["entry"], rest[0]), {}).get("status", "unscreened")
    queue.sort(key=lambda q: (q["book"], TAG_ORDER.index(q["tag"]), q["entry"]))
    queued = {(q["book"], q["entry"]) for q in queue}

    cols = ["book", "entry", "kind", "title", "member", "n_books", "tag", "status", "cited", "cite",
            "hits", "found", "via", "family", "parent_has_book", "gate", "proposed_primary",
            "proposed_status", "verdict", "print_page", "evidence"]
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(cols) + "\n")
        for q in queue:
            f.write("\t".join(str(q[c]) for c in cols) + "\n")

    if args.status_out:  # every screened membership, for scripts/membership-queue-461.py
        ext = cols + ["has_row", "exact", "paren", "queued"]
        with open(args.status_out, "w", encoding="utf-8", newline="\n") as f:
            f.write("\t".join(ext) + "\n")
            for q in sorted(allrows, key=lambda q: (q["book"], q["entry"])):
                q["queued"] = "yes" if (q["book"], q["entry"]) in queued else ""
                f.write("\t".join(str(q.get(c, "")) for c in ext) + "\n")

    report(queue, status, quality, multi, pdfs, members)
    return 0


def report(queue, status, quality, multi, pdfs, members) -> None:
    total_pairs = sum(len(v) for v in members.values())
    screened = sum(1 for v in status.values() if v["status"] not in ("no-text",))
    print(f"multi-book entries: {len(multi)}; memberships: {total_pairs}; "
          f"books with a PDF: {len(pdfs)}; memberships screened: {screened}")
    c = collections.Counter(v["status"] for v in status.values())
    print("status:", dict(sorted(c.items())))
    print("tag:", dict(sorted(collections.Counter(q["tag"] for q in queue).items(),
                              key=lambda kv: TAG_ORDER.index(kv[0]))), "rows:", len(queue))
    bad = sorted(b for b, q in quality.items() if q[3] != "ok")
    print("books without a verdict:", len(bad), bad[:60])
    gated = [q for q in queue if q["gate"]]
    print("first-book rows gated:", len(gated), dict(collections.Counter(q["tag"] for q in gated)),
          "| proposed primary status:", dict(collections.Counter(q["proposed_status"] or q["proposed_primary"] for q in gated)))
    rates = [q[2] for q in quality.values() if q[1] >= 5 and q[3] == "ok"]
    if rates:
        rates.sort()
        print(f"row-window hit rate over {len(rates)} books: median {rates[len(rates)//2]:.2f}, "
              f"min {rates[0]:.2f}, max {rates[-1]:.2f}")
    per = collections.defaultdict(collections.Counter)
    for q in queue:
        per[q["book"]][q["tag"]] += 1
    top = sorted(per, key=lambda b: -sum(per[b][t] for t in REMOVAL_TAGS))[:20]
    print("top books (removal candidates):")
    for b in top:
        n = sum(per[b][t] for t in REMOVAL_TAGS)
        print(f"  {b}\t{n}\t{dict(per[b])}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("corpus", help="corpus directory (a checkout of cast-iron-data)")
    ap.add_argument("--pdf-dir", required=True, help="directory that holds the owner PDFs (searched recursively)")
    ap.add_argument("--out", default="membership-queue.tsv")
    ap.add_argument("--status-out", help="also write every screened membership (printed ones too) with the "
                    "columns `has_row`, `exact` (title on the cited pages themselves), `paren` (the "
                    "parenthetical of the title on the cited page, elsewhere in the book, or nowhere) "
                    "and `queued`; scripts/membership-queue-461.py reads it")
    ap.add_argument("--text-cache", help="directory for extracted text (outside any repository)")
    ap.add_argument("--books", help="comma-separated publication ids; default is every book with a PDF")
    ap.add_argument("--pdftotext", default="pdftotext")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--weak-pages", type=int, default=1,
                    help="a title on this many pages or fewer, with no row, is a weak mention")
    ap.add_argument("--min-align", type=float, default=0.3,
                    help="least share of a book's pages with a readable page number before its verdicts count")
    try:
        return screen(ap.parse_args())
    except (OSError, subprocess.SubprocessError) as e:
        # The message of these errors can name a PDF or a path; keep it out of the output.
        sys.exit(f"error: {type(e).__name__} (message withheld)")


if __name__ == "__main__":
    sys.exit(main())
