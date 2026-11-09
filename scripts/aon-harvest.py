#!/usr/bin/env python3
"""Harvest Archives of Nethys (AoN) page links for the corpus.

This is a curation-time script. It is never run by the app, by the CI check, or at build
time. It makes a small number of requests to AoN's PF1e bulk listings, caches the raw
responses outside the repository, and writes an optional `aon` field only for entries and
publications whose kind and normalized title match exactly one AoN page.

Pages used
==========

The PF1e site publishes one list page per record kind. The harvest requests these pages,
one request each, and reads the record links from them:

    Feats.aspx             all feats          -> FeatDisplay.aspx?ItemName=...
    Spells.aspx            all spells         -> SpellDisplay.aspx?ItemName=...
    Monsters.aspx          all monsters       -> MonsterDisplay.aspx?ItemName=...
    Equipment.aspx         all equipment      -> EquipmentDisplay.aspx?ItemName=...
    MagicItems.aspx        all magic items    -> MagicItemDisplay.aspx?ItemName=...
    Classes.aspx           all classes        -> ClassDisplay.aspx?ItemName=...
    PrestigeClasses.aspx   all prestige       -> PrestigeClassDisplay.aspx?ItemName=...
    Archetypes.aspx        all archetypes     -> ArchetypeDisplay.aspx?ItemName=...
    Races.aspx             all races          -> RaceDisplay.aspx?ItemName=...
    Traits.aspx            all traits         -> TraitDisplay.aspx?ItemName=...
    Skills.aspx            all skills         -> SkillDisplay.aspx?ItemName=...
    Sources.aspx           all publications   -> SourceDisplay.aspx?FixedSource=...

AoN exposes no documented bulk JSON export. These list pages are its own full listings;
the script does not build a URL from a title and probe it with one request per entry. If a
listing is missing (404), the kind is reported as unmatched rather than guessed. A 403 or
429 stops the run: the script does not retry behind a different user agent, rotate
addresses, or otherwise evade a block.

Matching
========

The key is the entry kind plus the normalized title (Unicode NFKC, case-folded, whitespace
collapsed). A title that has exactly one AoN link gets that link. A title with several
links is ambiguous and gets no link; this covers mythic versions, Greater/Lesser/Mass
variants, Elephant revisions, and monsters that share a name. A title that includes a
distinct qualifier, such as `Power Attack (Mythic)`, matches when AoN lists it under that
distinct title. Publications match on their title in the AoN source list, with a small
reviewed alias table for the names AoN prints differently.

Every miss is reported. The coverage report goes to `/tmp` by default and is never
committed. Existing `aon` values are not removed unless `--prune` is passed, so a reviewed
link cannot disappear because a list page was temporarily unavailable.

Usage
=====

    python3 scripts/aon-harvest.py                 # fetch, match, write, report
    python3 scripts/aon-harvest.py --offline       # use the cache only
    python3 scripts/aon-harvest.py --dry-run       # match and report, write nothing
    python3 scripts/aon-harvest.py --prune         # remove entries with no exact match

Then format and check the corpus with the Cast Iron tool that reads the `aon` field:

    cargo xtask corpus-fmt <dir>
    cargo xtask corpus-check <dir>

The raw responses are cached under `$AON_CACHE` (default `/tmp/cast-iron-aon-cache`). The
script refuses a cache inside the repository.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import time
import tomllib
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "entries"
PUBLICATIONS = ROOT / "publications.toml"

BASE_URL = "https://aonprd.com/"
USER_AGENT = "cast-iron-data/1.0 (+https://github.com/phynics/cast-iron-data)"
REQUEST_DELAY_SECONDS = 2.0
REQUEST_TIMEOUT_SECONDS = 60
MAX_5XX_STREAK = 2

DEFAULT_CACHE = Path("/tmp/cast-iron-aon-cache")
DEFAULT_REPORT = Path("/tmp/cast-iron-aon-coverage.md")

# The index pages. They are one request each; the category pages below are discovered from
# the links on them, never built from an entry title.
INITIAL_PAGES: tuple[tuple[str, str], ...] = (
    ("feat", "Feats.aspx"),
    ("spell", "Spells.aspx?Class=All"),
    ("creature", "Monsters.aspx?Letter=All"),
    ("item", "Equipment.aspx"),
    ("item", "MagicItems.aspx"),
    ("class", "Classes.aspx"),
    ("prestige_class", "PrestigeClasses.aspx"),
    ("archetype", "Archetypes.aspx"),
    ("trait", "Traits.aspx"),
    ("race", "Races.aspx"),
    ("skill", "Skills.aspx"),
    ("publication", "Sources.aspx"),
)

# AoN prints some publication titles differently from `publications.toml`. These are the
# reviewed spellings from the book-order research; an unmatched title is reported, never
# guessed.
PUBLICATION_ALIASES: dict[str, str] = {
    "prpg core rulebook": "core-rulebook",
    "pathfinder rpg bestiary": "bestiary",
    "pathfinder rpg bestiary 2": "bestiary-2",
    "pathfinder rpg bestiary 3": "bestiary-3",
    "pathfinder rpg bestiary 4": "bestiary-4",
    "pathfinder rpg bestiary 5": "bestiary-5",
    "pathfinder rpg bestiary 6": "bestiary-6",
    "gamemastery guide": "game-mastery-guide",
}

# The page stem names the record type, so a cross-link on a list page cannot put a class
# under `feat`. One stem may serve more than one corpus kind.
PAGE_KINDS: dict[str, tuple[str, ...]] = {
    "FeatDisplay": ("feat",),
    "SpellDisplay": ("spell",),
    "MonsterDisplay": ("creature",),
    "CreatureDisplay": ("creature",),
    "EquipmentDisplay": ("item",),
    "EquipmentWeaponsDisplay": ("item",),
    "EquipmentArmorDisplay": ("item",),
    "EquipmentMiscDisplay": ("item",),
    "MagicItemDisplay": ("item",),
    "MagicItemsDisplay": ("item",),
    "MagicWeaponsDisplay": ("item",),
    "MagicArmorDisplay": ("item",),
    "MagicArtifactsDisplay": ("item",),
    "MagicCursedDisplay": ("item",),
    "MagicIntelligentDisplay": ("item",),
    "MagicPotionsDisplay": ("item",),
    "MagicRingsDisplay": ("item",),
    "MagicRodsDisplay": ("item",),
    "MagicStavesDisplay": ("item",),
    "MagicWondrousDisplay": ("item",),
    "MagicOtherDisplay": ("item",),
    "ClassDisplay": ("class",),
    "PrestigeClassDisplay": ("prestige_class",),
    "PrestigeClassesDisplay": ("prestige_class",),
    "ArchetypeDisplay": ("archetype",),
    "TraitDisplay": ("trait", "racial_trait"),
    "RaceDisplay": ("race",),
    "RacesDisplay": ("race",),
    "SkillDisplay": ("skill",),
    "RuleDisplay": ("rule",),
    "SourceDisplay": ("publication",),
    # Class-option pages are not separate list requests; they appear as cross-links on
    # the class and feat listings.
    "BloodlineDisplay": ("class_option",),
    "DomainDisplay": ("class_option",),
    "MysteryDisplay": ("class_option",),
    "PatronDisplay": ("class_option",),
    "ArcaneSchoolDisplay": ("class_option",),
    "FamiliarDisplay": ("class_option",),
    "AnimalCompanionDisplay": ("class_option",),
    "SpiritDisplay": ("class_option",),
    "ShamanSpiritDisplay": ("class_option",),
    "HexDisplay": ("class_option",),
    "RagePowerDisplay": ("class_option",),
    "TalentDisplay": ("class_option",),
    "DiscoveryDisplay": ("class_option",),
    "ExploitDisplay": ("class_option",),
    "DeedDisplay": ("class_option",),
    "StylestrikeDisplay": ("class_option",),
    "KineticistTalentsDisplay": ("class_option",),
    "OccultRitualDisplay": ("class_option",),
    "BlessingDisplay": ("class_option",),
    "InquisitionDisplay": ("class_option",),
    "OathDisplay": ("class_option",),
    "CurseDisplay": ("class_option",),
    "EmotionalFocusDisplay": ("class_option",),
    "ImplementDisplay": ("class_option",),
    "OrderDisplay": ("class_option",),
    "PerformanceDisplay": ("class_option",),
    "PhrenicAmplificationDisplay": ("class_option",),
    "MesmeristTrickDisplay": ("class_option",),
    "StareDisplay": ("class_option",),
    "VigilanteTalentDisplay": ("class_option",),
    "SlayerTalentDisplay": ("class_option",),
    "NinjaTrickDisplay": ("class_option",),
    "SwashbucklerDeedDisplay": ("class_option",),
    "AspectDisplay": ("class_option",),
    "EvolutionDisplay": ("class_option",),
    "MercyDisplay": ("class_option",),
    "MasterpieceDisplay": ("class_option",),
}

ENTRY_QUERY_RE = re.compile(
    r"^([A-Za-z0-9]+Display\.aspx)\?(ItemName|FixedName|FinalName)=([^&]+)$"
)
SOURCE_QUERY_RE = re.compile(r"^SourceDisplay\.aspx\?FixedSource=([^&]+)$")
FRONT_MATTER_RE = re.compile(r"\A\+\+\+\n(.*?)\n\+\+\+\n", re.DOTALL)


class HarvestError(Exception):
    pass


class BlockedError(HarvestError):
    """The site refused automated access; the run stops without trying to evade it."""


@dataclass
class Anchor:
    href: str
    text: str


class LinkParser(HTMLParser):
    """Collects anchor hrefs and their visible text."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.anchors: list[Anchor] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attrs_map = dict(attrs)
        href = attrs_map.get("href")
        if href is None:
            return
        self._href = href
        self._text = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or self._href is None:
            return
        text = " ".join("".join(self._text).split())
        if text:
            self.anchors.append(Anchor(self._href, text))
        self._href = None
        self._text = []


@dataclass
class Listing:
    kind: str
    page: str
    path: Path
    status: str = "not fetched"
    anchors: list[Anchor] = field(default_factory=list)


@dataclass
class Coverage:
    matched: int = 0
    ambiguous: int = 0
    unmatched: int = 0
    examples: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))

    def add(self, status: str, title: str) -> None:
        if status == "matched":
            self.matched += 1
        elif status == "ambiguous":
            self.ambiguous += 1
        else:
            self.unmatched += 1
        if status != "matched" and len(self.examples[status]) < 15:
            self.examples[status].append(title)


def normalize_title(value: str) -> str:
    """The match key: NFKC, case-folded, curly quotes unified, whitespace collapsed."""
    value = unicodedata.normalize("NFKC", html.unescape(value))
    value = value.replace("\u2018", "'").replace("\u2019", "'")
    value = value.replace("\u201c", '"').replace("\u201d", '"')
    value = value.casefold()
    return " ".join(value.split())


def relative_link(href: str) -> str | None:
    """An AoN path with no scheme or host, or None for an unrelated/external link."""
    href = html.unescape(href.strip())
    if href.startswith(BASE_URL):
        href = href[len(BASE_URL) :]
    elif href.startswith("https://www.aonprd.com/"):
        href = href[len("https://www.aonprd.com/") :]
    elif "://" in href or href.startswith("//"):
        return None
    return href.removeprefix("/")


def canonical_path(page: str, key: str, raw_value: str) -> str:
    """The corpus form: one query key and a fully percent-encoded value."""
    value = urllib.parse.unquote_plus(html.unescape(raw_value))
    return f"{page}?{key}={urllib.parse.quote(value, safe='')}"


def classify_anchor(anchor: Anchor) -> tuple[str, str, str] | None:
    """(page, query_value, canonical relative href) when the anchor is a record page."""
    href = relative_link(anchor.href)
    if href is None:
        return None
    entry = ENTRY_QUERY_RE.match(href)
    if entry:
        page, key, raw = entry.group(1), entry.group(2), entry.group(3)
        value = urllib.parse.unquote_plus(html.unescape(raw))
        return page, value, canonical_path(page, key, raw)
    source = SOURCE_QUERY_RE.match(href)
    if source:
        raw = source.group(1)
        value = urllib.parse.unquote_plus(html.unescape(raw))
        return (
            "SourceDisplay.aspx",
            value,
            canonical_path("SourceDisplay.aspx", "FixedSource", raw),
        )
    return None


def page_kinds(page: str) -> tuple[str, ...]:
    stem = page.removesuffix(".aspx")
    return PAGE_KINDS.get(stem, ())


def cache_dir() -> Path:
    path = Path(os.environ.get("AON_CACHE", DEFAULT_CACHE)).resolve()
    if path == ROOT or ROOT in path.parents:
        raise HarvestError(
            f"the cache directory {path} is inside the repository; set AON_CACHE to a "
            "path outside it"
        )
    return path


def cache_name(page: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", page)


def fetch(
    kind: str, page: str, cache: Path, offline: bool, state: dict[str, int]
) -> Listing:
    """Fetch one listing through the cache. A 403/429 or a 5xx streak stops the run."""
    listing = Listing(kind=kind, page=page, path=cache / cache_name(page))
    if listing.path.is_file():
        listing.status = "cached"
        listing.anchors = read_anchors(listing.path)
        return listing
    if offline:
        listing.status = "missing (offline)"
        return listing

    time.sleep(REQUEST_DELAY_SECONDS)
    state["requests"] += 1
    request = urllib.request.Request(
        BASE_URL + urllib.parse.quote(page, safe="?&=/()%"),
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            body = response.read()
            status = response.status
    except urllib.error.HTTPError as error:
        if error.code in (403, 429):
            raise BlockedError(
                f"AoN returned HTTP {error.code} for {page}. Automated access is blocked or "
                "rate-limited from this host; the harvest stops here and does not try to evade "
                "the block."
            ) from error
        if 500 <= error.code < 600:
            state["5xx_streak"] += 1
            if state["5xx_streak"] >= MAX_5XX_STREAK:
                raise BlockedError(
                    f"AoN returned {state['5xx_streak']} consecutive 5xx responses; the "
                    f"harvest stops at {page}."
                ) from error
        else:
            state["5xx_streak"] = 0
        listing.status = f"HTTP {error.code}"
        return listing
    except urllib.error.URLError as error:
        raise HarvestError(f"cannot reach {BASE_URL + page}: {error.reason}") from error

    if status != 200:
        if 500 <= status < 600:
            state["5xx_streak"] += 1
            if state["5xx_streak"] >= MAX_5XX_STREAK:
                raise BlockedError(
                    f"AoN returned {state['5xx_streak']} consecutive 5xx responses; the "
                    f"harvest stops at {page}."
                )
        else:
            state["5xx_streak"] = 0
        listing.status = f"HTTP {status}"
        return listing
    state["5xx_streak"] = 0
    cache.mkdir(parents=True, exist_ok=True)
    listing.path.write_bytes(body)
    listing.status = "fetched"
    listing.anchors = read_anchors(listing.path)
    return listing


def read_anchors(path: Path) -> list[Anchor]:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    parser.close()
    return parser.anchors


def discovered_pages(
    listings: list[Listing], class_names: set[str]
) -> list[tuple[str, str]]:
    """The bulk category pages linked from the index pages, in a stable order."""
    by_page = {listing.page: listing for listing in listings}
    pages: list[tuple[str, str]] = []

    def hrefs(page: str) -> list[str]:
        listing = by_page.get(page)
        if listing is None:
            return []
        values = []
        for anchor in listing.anchors:
            href = relative_link(anchor.href)
            if href is not None:
                values.append(href)
        return values

    for href in hrefs("Equipment.aspx"):
        if re.fullmatch(r"Equipment(?:Weapons|Armor|Misc)\.aspx", href):
            pages.append(("item", href))
    for href in hrefs("MagicItems.aspx"):
        if re.fullmatch(r"Magic[A-Za-z]+\.aspx", href) and href != "MagicItems.aspx":
            pages.append(("item", href))
    for href in hrefs("Traits.aspx"):
        if re.fullmatch(r"Traits\.aspx\?Type=.+", href):
            pages.append(("trait", href))
    for href in hrefs("Races.aspx"):
        if re.fullmatch(r"Races\.aspx\?Category=.+", href):
            pages.append(("race", href))
    for href in hrefs("Sources.aspx"):
        if re.fullmatch(r"Sources\.aspx\?ProductLine=.+", href):
            pages.append(("publication", href))
    # Archetypes are listed per class. Fetch only classes that have archetype entries in
    # this corpus, matched by the class title rather than by the corpus id.
    for name in sorted(class_names):
        pages.append(("archetype", f"Archetypes.aspx?Class={name}"))

    seen = set()
    unique = []
    for kind, page in pages:
        key = (kind, page)
        if key in seen:
            continue
        seen.add(key)
        unique.append(key)
    return unique


def sorted_tokens(value: str) -> tuple[str, ...]:
    return tuple(sorted(re.findall(r"[a-z0-9]+", normalize_title(value))))


def corpus_class_info() -> tuple[dict[str, str], set[str]]:
    """Class id -> title, and the class ids that at least one archetype names."""
    classes: dict[str, str] = {}
    targets: set[str] = set()
    for path in sorted(ENTRIES.rglob("*.md")):
        front = read_front_matter(path)
        kind = str(front.get("kind", ""))
        if kind == "class":
            classes[str(front.get("id", ""))] = str(front.get("title", ""))
        elif kind == "archetype":
            for relation in front.get("relations", []):
                if relation.get("kind") == "archetype":
                    targets.add(str(relation.get("target", "")))
    return classes, targets


def aon_class_names(listing: Listing) -> list[str]:
    """The class names AoN's archetype index links, decoded."""
    names = []
    for anchor in listing.anchors:
        href = relative_link(anchor.href)
        if href is None or not href.startswith("ClassDisplay.aspx?ItemName="):
            continue
        names.append(urllib.parse.unquote_plus(href.split("=", 1)[1]))
    return names


def build_entry_index(
    listings: Iterable[Listing],
) -> tuple[dict[tuple[str, str], list[str]], dict[str, int]]:
    """kind plus normalized title -> the distinct AoN paths the listings show."""
    index: dict[tuple[str, str], list[str]] = defaultdict(list)
    seen: dict[str, int] = defaultdict(int)
    for listing in listings:
        for anchor in listing.anchors:
            classified = classify_anchor(anchor)
            if classified is None:
                continue
            page, value, href = classified
            kinds = page_kinds(page)
            if not kinds:
                continue
            # Archetype pages prefix the class name to the value; their anchor text is the
            # bare archetype title. Other pages use the query value or the anchor text,
            # depending on the table layout, so accept both spellings.
            titles = (
                {normalize_title(anchor.text)}
                if page == "ArchetypeDisplay.aspx"
                else {normalize_title(anchor.text), normalize_title(value)}
            )
            for kind in kinds:
                for title in titles:
                    key = (kind, title)
                    if href not in index[key]:
                        index[key].append(href)
                seen[kind] += 1
    return index, seen


def build_source_index(listings: Iterable[Listing]) -> dict[str, list[str]]:
    """Normalized AoN source title -> distinct SourceDisplay paths."""
    index: dict[str, list[str]] = defaultdict(list)
    for listing in listings:
        for anchor in listing.anchors:
            classified = classify_anchor(anchor)
            if classified is None or classified[0] != "SourceDisplay.aspx":
                continue
            href = classified[2]
            for key in {
                normalize_title(classified[1]),
                normalize_title(anchor.text),
            }:
                if href not in index[key]:
                    index[key].append(href)
    return index


def read_front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if match is None:
        raise HarvestError(f"{path}: no closed `+++` front matter")
    return tomllib.loads(match.group(1))


def toml_string(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def set_entry_aon(path: Path, value: str | None, prune: bool) -> str:
    """Set, keep, or prune the `aon` key on one entry. Returns the action taken."""
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if match is None:
        raise HarvestError(f"{path}: no closed `+++` front matter")
    front = match.group(1)
    lines = front.split("\n")
    aon_line = next(
        (index for index, line in enumerate(lines) if line.startswith("aon = ")), None
    )
    if value is None:
        if aon_line is None or not prune:
            return "kept" if aon_line is not None else "unmatched"
        del lines[aon_line]
        action = "pruned"
    else:
        row = f"aon = {toml_string(value)}"
        if aon_line is not None:
            if lines[aon_line] == row:
                return "unchanged"
            lines[aon_line] = row
            action = "updated"
        else:
            title_line = next(
                (index for index, line in enumerate(lines) if line.startswith("title = ")),
                None,
            )
            if title_line is None:
                raise HarvestError(f"{path}: front matter has no `title`")
            lines.insert(title_line + 1, row)
            action = "added"
    new_front = "\n".join(lines)
    path.write_text(
        "+++\n" + new_front + "\n+++\n" + text[match.end() :], encoding="utf-8"
    )
    return action


def set_publication_aon(path: Path, publication_id: str, value: str | None, prune: bool) -> str:
    """Set or prune `aon` at the end of one `[[publication]]` row."""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    start = None
    for index, line in enumerate(lines):
        if line.strip() == f'id = "{publication_id}"':
            start = index
            break
    if start is None:
        raise HarvestError(f"{path}: no publication row for {publication_id!r}")
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].strip() == "" or lines[index].startswith("[["):
            end = index
            break
    row_index = next(
        (
            index
            for index in range(start, end)
            if lines[index].startswith("aon = ")
        ),
        None,
    )
    if value is None:
        if row_index is None or not prune:
            return "kept" if row_index is not None else "unmatched"
        del lines[row_index]
        action = "pruned"
    else:
        row = f"aon = {toml_string(value)}"
        if row_index is not None:
            if lines[row_index] == row:
                return "unchanged"
            lines[row_index] = row
            action = "updated"
        else:
            insert_at = end
            while insert_at > start and lines[insert_at - 1].strip() == "":
                insert_at -= 1
            lines.insert(insert_at, row)
            action = "added"
    path.write_text("\n".join(lines), encoding="utf-8")
    return action


def pick(values: list[str]) -> tuple[str, str]:
    if len(values) == 1:
        return "matched", values[0]
    if len(values) > 1:
        return "ambiguous", ""
    return "unmatched", ""


def unique_publication_titles() -> dict[str, str]:
    """Normalized `publications.toml` title -> publication id."""
    with PUBLICATIONS.open("rb") as handle:
        data = tomllib.load(handle)
    return {
        normalize_title(row["title"]): row["id"] for row in data.get("publication", [])
    }


def count_entries_by_kind() -> dict[str, int]:
    counts: Counter = Counter()
    for path in sorted(ENTRIES.rglob("*.md")):
        counts[str(read_front_matter(path).get("kind", ""))] += 1
    return dict(counts)


def write_blocked_report(path: Path, message: str) -> None:
    """Record a blocked run. No page was matched, so no link was written."""
    counts = count_entries_by_kind()
    lines = [
        "# AoN link harvest",
        "",
        f"**Blocked:** {message}",
        "",
        "No page was fetched, so no entry or publication was matched, and no `aon` field "
        "was written. Every entry is unharvested, not unmatched.",
        "",
        "| Kind | Entries (unharvested) |",
        "|---|---:|",
    ]
    for kind, count in sorted(counts.items()):
        lines.append(f"| {kind or '(no kind)'} | {count} |")
    lines.append(f"| **total** | **{sum(counts.values())}** |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(
    path: Path,
    entry_coverage: dict[str, Coverage],
    publication_coverage: Coverage,
    listings: list[Listing],
    actions: Counter,
    unmatched_publications: list[str],
) -> None:
    lines = [
        "# AoN link harvest",
        "",
        "Curated from the AoN PF1e bulk listings. `matched` means the kind and normalized "
        "title found exactly one page; `ambiguous` means several pages; `unmatched` means none.",
        "",
        "| Kind | Matched | Ambiguous | Unmatched | Total |",
        "|---|---:|---:|---:|---:|",
    ]
    for kind, coverage in sorted(entry_coverage.items()):
        total = coverage.matched + coverage.ambiguous + coverage.unmatched
        lines.append(
            f"| {kind} | {coverage.matched} | {coverage.ambiguous} | "
            f"{coverage.unmatched} | {total} |"
        )
    total = publication_coverage.matched + publication_coverage.ambiguous + publication_coverage.unmatched
    lines.append(
        f"| publication | {publication_coverage.matched} | "
        f"{publication_coverage.ambiguous} | {publication_coverage.unmatched} | {total} |"
    )
    lines.extend(["", "## Listings", "", "| Page | Status | Anchors | Cache |", "|---|---|---:|---|"])
    for listing in listings:
        lines.append(
            f"| {listing.page} | {listing.status} | {len(listing.anchors)} | `{listing.path}` |"
        )
    lines.extend(["", "## Write actions", ""])
    if actions:
        for action, count in sorted(actions.items()):
            lines.append(f"- {action}: {count}")
    else:
        lines.append("- none (dry run, or no matches)")
    if unmatched_publications:
        lines.extend(["", "## Unmatched publications", ""])
        lines.extend(f"- {title}" for title in unmatched_publications[:50])
    for kind, coverage in sorted(entry_coverage.items()):
        if not coverage.examples:
            continue
        lines.extend(["", f"## {kind}: ambiguous", ""])
        lines.extend(f"- {title}" for title in coverage.examples.get("ambiguous", []))
        lines.extend(["", f"## {kind}: unmatched (first 15)", ""])
        lines.extend(f"- {title}" for title in coverage.examples.get("unmatched", []))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--offline", action="store_true", help="read the cache only")
    parser.add_argument("--dry-run", action="store_true", help="write no corpus file")
    parser.add_argument(
        "--prune",
        action="store_true",
        help="remove an existing `aon` when no exact match exists",
    )
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args(argv)

    cache = cache_dir()
    state = {"requests": 0, "5xx_streak": 0}
    listings: list[Listing] = []
    try:
        for kind, page in INITIAL_PAGES:
            listings.append(fetch(kind, page, cache, args.offline, state))
        classes, targets = corpus_class_info()
        wanted = {sorted_tokens(classes[target]) for target in targets if target in classes}
        archetype_index = next(
            listing for listing in listings if listing.page == "Archetypes.aspx"
        )
        names = [
            name
            for name in aon_class_names(archetype_index)
            if sorted_tokens(name) in wanted
        ]
        for kind, page in discovered_pages(listings, set(names)):
            listings.append(fetch(kind, page, cache, args.offline, state))
    except BlockedError as error:
        write_blocked_report(args.report, str(error))
        print(f"error: {error}", file=sys.stderr)
        print(f"report: {args.report}", file=sys.stderr)
        return 2

    entry_index, anchor_counts = build_entry_index(listings)
    source_index = build_source_index(listings)
    publications_by_title = unique_publication_titles()

    entry_coverage: dict[str, Coverage] = defaultdict(Coverage)
    actions: Counter = Counter()
    if not args.dry_run:
        for path in sorted(ENTRIES.rglob("*.md")):
            front = read_front_matter(path)
            kind = str(front.get("kind", ""))
            title = str(front.get("title", ""))
            coverage = entry_coverage[kind]
            if not title:
                coverage.add("unmatched", f"{path}: no title")
                continue
            values = entry_index.get((kind, normalize_title(title)), [])
            status, href = pick(values)
            coverage.add(status, title)
            actions[set_entry_aon(path, href or None, args.prune)] += 1
    else:
        for path in sorted(ENTRIES.rglob("*.md")):
            front = read_front_matter(path)
            kind = str(front.get("kind", ""))
            title = str(front.get("title", ""))
            coverage = entry_coverage[kind]
            if not title:
                coverage.add("unmatched", f"{path}: no title")
                continue
            status, _href = pick(entry_index.get((kind, normalize_title(title)), []))
            coverage.add(status, title)
            actions["unchanged"] += 1

    source_by_publication: dict[str, list[str]] = defaultdict(list)
    for source_title, values in source_index.items():
        publication_id = publications_by_title.get(source_title)
        if publication_id is None:
            publication_id = PUBLICATION_ALIASES.get(source_title)
        if publication_id is None:
            continue
        for href in values:
            if href not in source_by_publication[publication_id]:
                source_by_publication[publication_id].append(href)

    publication_coverage = Coverage()
    unmatched_publications: list[str] = []
    with PUBLICATIONS.open("rb") as handle:
        publication_rows = tomllib.load(handle).get("publication", [])
    for row in publication_rows:
        title = row["title"]
        publication_id = row["id"]
        values = source_by_publication.get(publication_id, [])
        status, href = pick(values)
        publication_coverage.add(status, title)
        if status != "matched":
            unmatched_publications.append(title)
        if not args.dry_run:
            actions[
                set_publication_aon(PUBLICATIONS, publication_id, href or None, args.prune)
            ] += 1

    write_report(
        args.report,
        entry_coverage,
        publication_coverage,
        listings,
        actions,
        unmatched_publications,
    )
    print(f"report: {args.report}")
    for listing in listings:
        print(f"  {listing.page}: {listing.status}, {len(listing.anchors)} anchors")
    for kind, coverage in sorted(entry_coverage.items()):
        print(
            f"  {kind}: matched {coverage.matched}, ambiguous {coverage.ambiguous}, "
            f"unmatched {coverage.unmatched}"
        )
    print(
        f"  publication: matched {publication_coverage.matched}, "
        f"ambiguous {publication_coverage.ambiguous}, "
        f"unmatched {publication_coverage.unmatched}"
    )
    print("  anchors: " + ", ".join(f"{page} {count}" for page, count in sorted(anchor_counts.items())))
    print(f"  requests: {state['requests']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
