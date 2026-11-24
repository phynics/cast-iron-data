#!/usr/bin/env python3
"""Test the `expanded_in` action of scripts/expansion-credits-apply.py on a small synthetic corpus.

    python3 scripts/test-expansion-credits-apply.py

Cases (phynics/cast-iron#461, S9): class `expands` needs a `via` entry; class `expands-no-via`
writes a credit with `publication` and `page` and no `via` key, and refuses a `via`; both take the
book out of `source_ids` and drop its placement; applying twice changes nothing; an unknown class
is refused before anything is written.
"""
import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
APPLY = HERE / "expansion-credits-apply.py"
HEAD = ["entry", "book", "action", "class", "cited_page", "print_page", "family", "related_cite", "edge",
        "mention_pages", "mention_kind", "read", "evidence", "invalidated", "via", "primary_to"]
PUBS = ''.join(f'[[publication]]\nid = "{i}"\ntitle = "{t}"\n\n' for i, t in
               (("book-a", "Alpha Book"), ("book-b", "Beta Book"), ("book-c", "Gamma Book")))
ENTRY = ('+++\nid = "ref/race/test-race"\nkind = "race"\ntitle = "Test Race"\n'
         'source_ids = ["book-a", "book-b", "book-c"]\n[[sources]]\npublication = "book-a"\npage = "5"\n\n'
         '[fields]\nkind = "none"\n+++\nText.\n')
BOOK_B = ('[[books]]\nsource = "book-b"\n\n[[books.chapters]]\ntitle = "Races"\n\n'
          '[[books.chapters.children]]\ntitle = "Test Race"\nentry = "ref/race/test-race"\n')


class ExpandedInTest(unittest.TestCase):
    def run_apply(self, klass: str, via: str):
        tmp = Path(tempfile.mkdtemp())
        (tmp / "entries/race").mkdir(parents=True)
        (tmp / "books").mkdir()
        (tmp / "publications.toml").write_text(PUBS, encoding="utf-8")
        (tmp / "books/book-b.toml").write_text(BOOK_B, encoding="utf-8")
        path = tmp / "entries/race/test-race.md"
        path.write_text(ENTRY, encoding="utf-8")
        row = dict.fromkeys(HEAD, "")
        row.update(entry="ref/race/test-race", book="book-b", action="expanded_in", cited_page="31", print_page="31",
                   read="read p. 31", evidence="only a favored class line", via=via)
        row["class"] = klass
        dec = tmp / "decisions.tsv"
        with open(dec, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=HEAD, delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerow(row)
        self.corpus, self.path, self.dec = tmp, path, dec
        return subprocess.run([sys.executable, str(APPLY), str(tmp), "--decisions", str(dec)],
                              capture_output=True, text=True)

    def test_no_via_credit_has_no_via_key(self):
        r = self.run_apply("expands-no-via", "")
        self.assertEqual(r.returncode, 0, r.stderr)
        out = self.path.read_text()
        self.assertIn('source_ids = ["book-a", "book-c"]', out)
        self.assertIn('[[expanded_in]]\npublication = "book-b"\npage = "31"\n', out)
        self.assertNotIn("via", out)
        self.assertNotIn("ref/race/test-race", (self.corpus / "books/book-b.toml").read_text())
        again = subprocess.run([sys.executable, str(APPLY), str(self.corpus), "--decisions", str(self.dec)],
                               capture_output=True, text=True)
        self.assertEqual(again.returncode, 0, again.stderr)
        self.assertEqual(self.path.read_text(), out)
        self.assertIn("expanded_in already: 1", again.stdout)

    def test_via_credit_writes_via(self):
        r = self.run_apply("expands", "ref/class/test-class")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('via = "ref/class/test-class"', self.path.read_text())

    def test_class_expands_still_needs_via(self):
        before = ENTRY
        r = self.run_apply("expands", "")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("via", r.stderr)
        self.assertEqual(self.path.read_text(), before)

    def test_no_via_class_refuses_a_via(self):
        r = self.run_apply("expands-no-via", "ref/class/test-class")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("expands-no-via", r.stderr)
        self.assertEqual(self.path.read_text(), ENTRY)

    def test_unknown_class_is_refused(self):
        r = self.run_apply("expands-anyway", "")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(self.path.read_text(), ENTRY)


if __name__ == "__main__":
    unittest.main()
