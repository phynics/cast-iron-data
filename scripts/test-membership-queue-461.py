#!/usr/bin/env python3
"""Test scripts/membership-queue-461.py on a small synthetic corpus (no real data, no book text).

    python3 scripts/test-membership-queue-461.py

Cases: every pair of the `corpus-check` warning and every figurine membership gets a row; the group
and the slice of a row follow the entry (a standard racial trait, a class hub and its mirror, a race
hub, a hub with and without a body source line, a faith excerpt, a figurine, a book without a PDF); an old verdict is
kept as it is; a book that left `source_ids` is `resolved` (with the `expanded_in` page when the
entry credits it); a row whose title is on the cited page is a `keep`, but a figurine whose variant
name is not on the page is not; a second run gives the same file; `--check` accepts the file and
finds a missing row, a stale group and a `keep` without its `[[sources]]` row.
"""
import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
QUEUE = HERE / "membership-queue-461.py"
sys.path.insert(0, str(HERE))

SCREEN_COLS = ["book", "entry", "kind", "title", "member", "n_books", "tag", "status", "cited", "cite",
               "hits", "found", "via", "family", "parent_has_book", "gate", "proposed_primary",
               "proposed_status", "verdict", "print_page", "evidence"]
ALL_COLS = SCREEN_COLS + ["has_row", "exact", "paren", "queued"]
PUBS = "".join(f'[[publication]]\nid = "{b}"\ntitle = "{t}"\n\n' for b, t in
               (("core", "Core Book"), ("book-a", "Alpha Book"), ("book-b", "Beta Book"), ("book-c", "Gamma Book"),
                ("nopdf", "Lost Book")))


def entry(eid: str, kind: str, title: str, ids: list[str], rows: str = "", body: str = "Text.\n", fields: str = "") -> str:
    ids_text = ", ".join(f'"{i}"' for i in ids)
    return (f'+++\nid = "{eid}"\nkind = "{kind}"\ntitle = "{title}"\nsource_ids = [{ids_text}]\n{rows}\n'
            f'[fields]\nkind = "{kind}"\n{fields}+++\n{body}')


ROW_B = '[[sources]]\npublication = "book-b"\npage = "12"\n'
FIG = "Figurine of Wondrous Power"


def corpus_files() -> dict[str, str]:
    return {
        "racial-trait/dwarf/medium.md": entry("ref/racial-trait/dwarf/medium", "racial_trait", "Medium",
                                              ["core", "book-a", "book-b"], fields="alternate = false\n"),
        "racial-trait/elf/odd.md": entry("ref/racial-trait/elf/odd", "racial_trait", "Odd Trait",
                                         ["core", "book-a"], fields="alternate = true\n"),
        "class/rogue.md": entry("ref/class/rogue", "class", "Rogue", ["core", "book-a", "nopdf"]),
        "class/wizard.md": entry("ref/class/wizard", "class", "Wizard", ["core", "book-a"]),
        "rule/class-rogue/capstones.md": entry("ref/rule/class-rogue/capstones", "rule", "Rogue Capstones", ["core", "book-a"]),
        "race/elf.md": entry("ref/race/elf", "race", "Elf", ["core", "book-a"]),
        "rule/hub-line.md": entry("ref/rule/hub-line", "rule", "Hub With Line", ["core", "book-a"],
                                  body="Links.\n\n**Source** Alpha Book pg. 3\\\n"),
        "faith/lamashtu.md": entry("ref/faith/lamashtu", "rule", "Lamashtu", ["core", "book-a"],
                                   body="Links.\n\n**Sources:** Alpha Book pg 3\\\n"),
        "rule/hub-bare.md": entry("ref/rule/hub-bare", "rule", "Hub Bare", ["core", "book-a"], body="Links.\n"),
        "spell/printed.md": entry("ref/spell/printed", "spell", "Printed Spell", ["core", "book-b"], rows=ROW_B),
        "spell/single.md": entry("ref/spell/single", "spell", "Single Spell", ["core", "book-a", "nopdf"]),
        "spell/gone.md": entry("ref/spell/gone", "spell", "Gone Spell", ["core"]),
        "spell/credited.md": entry("ref/spell/credited", "spell", "Credited Spell", ["core"],
                                   rows='[[expanded_in]]\npublication = "book-c"\npage = "44"\n'),
        "item/fig-a.md": entry("ref/item/fig-a", "item", f"{FIG} (Slate Spider)", ["core", "book-a", "book-b"],
                               rows=ROW_B.replace('"12"', '"166"') + '[[sources]]\npublication = "book-a"\npage = "9"\n'),
        "item/fig-b.md": entry("ref/item/fig-b", "item", f"{FIG} (Black Jade Raven)", ["core", "book-a", "book-b"],
                               rows='[[sources]]\npublication = "book-a"\npage = "9"\n' + ROW_B.replace('"12"', '"166"')),
    }


def screen_row(book: str, entry_id: str, **kw) -> dict:
    row = dict.fromkeys(ALL_COLS, "")
    row.update(book=book, entry=entry_id, kind="spell", title="x", member="2", n_books="3", tag="uncited",
               status="printed", cite="none", hits="2", queued="")
    row.update(kw)
    return row


def write_tsv(path: Path, cols: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def read_tsv(path: Path) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "publications.toml").write_text(PUBS, encoding="utf-8")
        for rel, text in corpus_files().items():
            p = self.tmp / "entries" / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8")
        old = [dict.fromkeys(SCREEN_COLS, "") | dict(
            book="book-a", entry="ref/racial-trait/elf/odd", kind="racial_trait", title="Odd Trait", member="2",
            n_books="2", tag="family-leak", status="absent", verdict="remove", print_page="9",
            evidence="race-section-read-no-trait"),
            dict.fromkeys(SCREEN_COLS, "") | dict(
                book="book-c", entry="ref/spell/gone", kind="spell", title="Gone Spell", member="2", n_books="2",
                tag="uncited", status="weak"),
            dict.fromkeys(SCREEN_COLS, "") | dict(
                book="book-c", entry="ref/spell/credited", kind="spell", title="Credited Spell", member="2",
                n_books="2", tag="uncited", status="weak"),
            dict.fromkeys(SCREEN_COLS, "") | dict(
                book="book-b", entry="ref/spell/printed", kind="spell", title="Printed Spell", member="2",
                n_books="2", tag="uncited", status="weak")]
        self.queue = self.tmp / "queue.tsv"
        write_tsv(self.queue, SCREEN_COLS, old)
        fresh = [
            screen_row("book-b", "ref/spell/printed", cited="12", cite="row", has_row="yes", exact="yes"),
            screen_row("book-b", "ref/item/fig-a", kind="item", title=f"{FIG} (Slate Spider)", cited="166",
                       cite="row", has_row="yes", exact="yes", paren="none"),
            screen_row("book-b", "ref/item/fig-b", kind="item", title=f"{FIG} (Black Jade Raven)", cited="166",
                       cite="row", has_row="yes", exact="yes", paren="page"),
            screen_row("book-a", "ref/racial-trait/dwarf/medium", kind="racial_trait", title="Medium"),
            screen_row("book-a", "ref/class/rogue", kind="class", title="Rogue"),
            screen_row("book-a", "ref/class/wizard", kind="class", title="Wizard"),
            screen_row("book-a", "ref/rule/class-rogue/capstones", kind="rule", title="Rogue Capstones"),
            screen_row("book-a", "ref/race/elf", kind="race", title="Elf"),
            screen_row("book-a", "ref/rule/hub-line", kind="rule", title="Hub With Line", tag="hub-keep"),
            screen_row("book-a", "ref/rule/hub-bare", kind="rule", title="Hub Bare", tag="hub-keep"),
            screen_row("book-a", "ref/faith/lamashtu", kind="rule", title="Lamashtu"),
            screen_row("book-a", "ref/spell/single", kind="spell", title="Single Spell", status="absent", queued="yes"),
            screen_row("book-a", "ref/item/fig-a", kind="item", title=f"{FIG} (Slate Spider)", cited="9", cite="row",
                       has_row="yes", exact="yes", paren="page"),
        ]
        self.screen_all = self.tmp / "screen-all.tsv"
        write_tsv(self.screen_all, ALL_COLS, fresh)

    def run_queue(self, *args):
        return subprocess.run([sys.executable, str(QUEUE), str(self.tmp), "--queue", str(self.queue), *args],
                              capture_output=True, text=True)

    def build(self):
        r = self.run_queue("--screen-all", str(self.screen_all))
        self.assertEqual(r.returncode, 0, r.stderr + r.stdout)
        return {(x["book"], x["entry"]): x for x in read_tsv(self.queue)}

    def test_pairs_groups_and_slices(self):
        rows = self.build()
        # warning pairs: 2 dwarf/medium, hubs, class, race, single, and so on; every one has a row
        for key in [("book-a", "ref/racial-trait/dwarf/medium"), ("book-b", "ref/racial-trait/dwarf/medium"),
                    ("book-a", "ref/class/rogue"), ("nopdf", "ref/class/rogue"), ("nopdf", "ref/spell/single"),
                    ("book-a", "ref/rule/hub-line"), ("book-a", "ref/race/elf")]:
            self.assertIn(key, rows)
            self.assertEqual(rows[key]["in_warning"], "yes", key)
        want = {
            ("book-a", "ref/racial-trait/dwarf/medium"): ("standard-racial-trait", "S1"),
            ("book-a", "ref/class/rogue"): ("class-hub", "S7"),
            ("book-a", "ref/class/wizard"): ("class-hub", "S7"),
            ("book-a", "ref/rule/class-rogue/capstones"): ("class-hub", "S8"),
            ("book-a", "ref/race/elf"): ("race-hub", "S9"),
            ("book-a", "ref/rule/hub-line"): ("hub-cited", "S10"),
            ("book-a", "ref/rule/hub-bare"): ("link-only-hub", "S10"),
            ("book-a", "ref/spell/single"): ("single-entry", "S5"),
            ("nopdf", "ref/spell/single"): ("no-pdf", "S12"),
            ("nopdf", "ref/class/rogue"): ("class-hub", "S7"),
        }
        for key, (group, slc) in want.items():
            self.assertEqual((rows[key]["group"], rows[key]["slice"]), (group, slc), key)
        self.assertEqual(rows[("book-a", "ref/rule/hub-bare")]["ruling"], "hub-design-a")
        self.assertEqual(rows[("book-a", "ref/rule/hub-bare")]["slice"], "S10")
        self.assertEqual(rows[("book-a", "ref/rule/hub-line")]["ruling"], "")
        self.assertEqual(rows[("book-a", "ref/faith/lamashtu")]["group"], "faith-excerpt")
        self.assertEqual(rows[("book-a", "ref/faith/lamashtu")]["ruling"], "faith-link")
        self.assertEqual(rows[("book-a", "ref/rule/hub-line")]["body_line"], "yes")
        self.assertEqual(rows[("nopdf", "ref/spell/single")]["pdf"], "no")
        self.assertEqual(rows[("nopdf", "ref/spell/single")]["status"], "no-pdf")

    def test_the_alternate_trait_is_not_a_standard_one(self):
        rows = self.build()
        self.assertEqual(rows[("book-a", "ref/racial-trait/elf/odd")]["verdict"], "remove")  # old verdict, kept
        self.assertEqual(rows[("book-a", "ref/racial-trait/elf/odd")]["group"], "single-entry")

    def test_figurine_memberships_are_listed_although_their_rows_hide_them(self):
        rows = self.build()
        for e in ("ref/item/fig-a", "ref/item/fig-b"):
            for b in ("book-a", "book-b"):
                self.assertEqual(rows[(b, e)]["group"], "figurine", (b, e))
                self.assertEqual(rows[(b, e)]["in_warning"], "", (b, e))
        self.assertEqual(rows[("book-b", "ref/item/fig-a")]["slice"], "S4a")  # no verdict yet: its slice

    def test_old_verdicts_stay_and_resolved_rows_are_marked(self):
        rows = self.build()
        old = rows[("book-a", "ref/racial-trait/elf/odd")]
        self.assertEqual((old["verdict"], old["print_page"], old["evidence"], old["slice"]),
                         ("remove", "9", "race-section-read-no-trait", "done"))
        gone = rows[("book-c", "ref/spell/gone")]
        self.assertEqual((gone["verdict"], gone["evidence"], gone["slice"]), ("resolved", "out-of-source-ids", "S0"))
        credited = rows[("book-c", "ref/spell/credited")]
        self.assertEqual((credited["verdict"], credited["evidence"], credited["print_page"]), ("resolved", "expanded-in-row", "44"))

    def test_title_on_the_cited_page_is_a_keep_but_a_variant_name_off_the_page_is_not(self):
        rows = self.build()
        kept = rows[("book-b", "ref/spell/printed")]
        self.assertEqual((kept["verdict"], kept["print_page"], kept["evidence"], kept["slice"]),
                         ("keep", "12", "title-on-cited-page", "S0"))
        # the variant name is not on the cited page: no verdict (the page is read in S4)
        self.assertEqual(rows[("book-b", "ref/item/fig-a")]["paren"], "none")
        self.assertEqual(rows[("book-b", "ref/item/fig-a")]["verdict"], "")
        # the variant name is on the cited page: the title is, so it is a keep
        for key in (("book-b", "ref/item/fig-b"), ("book-a", "ref/item/fig-a")):
            self.assertEqual((rows[key]["verdict"], rows[key]["evidence"]), ("keep", "title-on-cited-page"), key)

    def test_a_second_run_gives_the_same_file(self):
        self.build()
        first = self.queue.read_text()
        self.build()
        self.assertEqual(self.queue.read_text(), first)

    def test_check_accepts_the_file_and_finds_what_is_stale(self):
        self.build()
        r = self.run_queue("--check")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        # a missing row
        rows = read_tsv(self.queue)
        cols = list(rows[0])
        dropped = [x for x in rows if (x["book"], x["entry"]) != ("book-a", "ref/class/rogue")]
        write_tsv(self.queue, cols, dropped)
        r = self.run_queue("--check")
        self.assertEqual(r.returncode, 1)
        self.assertIn("no row for ref/class/rogue in book-a", r.stdout)
        # a stale group
        stale = [dict(x, group="single-entry") if x["entry"] == "ref/race/elf" else x for x in rows]
        write_tsv(self.queue, cols, stale)
        r = self.run_queue("--check")
        self.assertEqual(r.returncode, 1)
        self.assertIn("group single-entry is not race-hub", r.stdout)
        # a keep whose [[sources]] row is gone
        (self.tmp / "entries/spell/printed.md").write_text(
            entry("ref/spell/printed", "spell", "Printed Spell", ["core", "book-b"]), encoding="utf-8")
        write_tsv(self.queue, cols, rows)
        r = self.run_queue("--check")
        self.assertEqual(r.returncode, 1)
        self.assertIn("verdict keep, but the entry has no [[sources]] row", r.stdout)


if __name__ == "__main__":
    unittest.main()
