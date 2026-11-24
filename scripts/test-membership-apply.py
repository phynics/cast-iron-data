#!/usr/bin/env python3
"""Test scripts/membership-apply.py on small synthetic corpora (no real data, no book text).

    python3 scripts/test-membership-apply.py

Cases: a `[[sources]]` row the audit file releases is dropped with the membership; the same
entry with a body `**Source:**` line as well is refused and left byte for byte unchanged; a
body line alone is refused; a row without an audit row is refused; a released row with a
wrong page is refused. Each refusal must happen before anything is written. A format 3 corpus
(`books/<publication-id>.toml`, curated books only) loses the placement from the curated file;
a derived book has no file, so only `source_ids` and the row change. A placement whose node
has children is refused, before any file is written.

`cite` rows (S0 of #461): the row is added in `source_ids` order with the printed page; running again
changes nothing; `--check` exits 1 while a change is pending and 0 after the run; a row with another
page, a book outside `source_ids`, an `[[expanded_in]]` credit and a bad page are refused before any
write; a body source line stays unless `--convert-body` takes the book's part out of it (and refuses
a line whose page does not overlap); a `keep` row without its `[[sources]]` row is pending.

A row for the entry's first book (`gate = primary`) is applied only when the reviewer cleared it:
`proposed_primary` is the book that becomes first, `proposed_status` is `printed` or `body`, and
the entry cites a page in that book. Every other gated row is refused.
"""
import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
APPLY = HERE / "membership-apply.py"
QUEUE_HEAD = ["book", "entry", "kind", "title", "member", "n_books", "tag", "status", "cited", "cite", "hits",
              "found", "via", "family", "parent_has_book", "gate", "proposed_primary", "proposed_status",
              "verdict", "print_page", "evidence"]
AUDIT_HEAD = ["entry", "book", "class", "cited_page", "print_page", "family", "related_cite", "edge",
              "mention_pages", "mention_kind", "read", "evidence", "invalidated"]
PUBS = '''[[publication]]
id = "book-a"
title = "Alpha Book"

[[publication]]
id = "book-b"
title = "Beta Book"

[[publication]]
id = "book-c"
title = "Gamma Book"
'''


def entry(sources: str, body: str) -> str:
    return ('+++\nid = "ref/spell/test-spell"\nkind = "spell"\ntitle = "Test Spell"\n'
            'source_ids = ["book-a", "book-b", "book-c"]\n' + sources + '\n[fields]\nkind = "spell"\n+++\n' + body)


ROW = '[[sources]]\npublication = "book-b"\npage = "12"\n'


class ApplyTest(unittest.TestCase):
    def run_apply(self, text: str, audit_page: str | None = "12", audit_class: str = "wrong-credit",
                  books: dict[str, str] | None = None, tag: str = "family-leak",
                  evidence: str = "wrong-credit-invalidated"):
        """`books` maps a path under the corpus to a book file; the default is the format 1 `books.toml`."""
        tmp = Path(tempfile.mkdtemp())
        (tmp / "entries/spell").mkdir(parents=True)
        (tmp / "publications.toml").write_text(PUBS, encoding="utf-8")
        for name, content in (books or {"books.toml": '[[books]]\nsource = "book-a"\n'}).items():
            (tmp / name).parent.mkdir(exist_ok=True)
            (tmp / name).write_text(content, encoding="utf-8")
        path = tmp / "entries/spell/test-spell.md"
        path.write_text(text, encoding="utf-8")
        queue = tmp / "queue.tsv"
        row = dict.fromkeys(QUEUE_HEAD, "")
        row.update(book="book-b", entry="ref/spell/test-spell", kind="spell", title="Test Spell", tag=tag,
                   verdict="remove", print_page="3", evidence=evidence)
        with open(queue, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=QUEUE_HEAD, delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerow(row)
        audit = tmp / "audit.tsv"
        with open(audit, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=AUDIT_HEAD, delimiter="\t", lineterminator="\n")
            w.writeheader()
            if audit_page is not None:
                a = dict.fromkeys(AUDIT_HEAD, "")
                a.update(entry="ref/spell/test-spell", book="book-b", cited_page=audit_page, print_page="none",
                         read="read p. 12", evidence="not printed", invalidated="Beta Book p. 12")
                a["class"] = audit_class
                w.writerow(a)
        r = subprocess.run([sys.executable, str(APPLY), str(tmp), "--queue", str(queue), "--audit", str(audit)],
                           capture_output=True, text=True)
        self.corpus = tmp
        return r, path

    def test_row_released_by_audit_is_dropped(self):
        r, path = self.run_apply(entry(ROW, "Text.\n"))
        self.assertEqual(r.returncode, 0, r.stderr)
        out = path.read_text()
        self.assertIn('source_ids = ["book-a", "book-c"]', out)
        self.assertNotIn("[[sources]]", out)

    def test_hub_keep_row_is_refused_unless_it_carries_the_hub_design_evidence(self):
        """Design (a) of the link-only hubs (owner ruling of 2026-11-24): `hub-keep` yields only to
        `hub-link`, `listed-link` and `hub-no-evidence`; any other evidence on a hub row is refused."""
        text = entry("", "Text.\n")
        r, path = self.run_apply(text, audit_page=None, tag="hub-keep", evidence="wrong-credit-invalidated")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(path.read_text(), text)
        for evidence in ("hub-link ref/spell/other", "listed-link ref/spell/other", "hub-no-evidence weather"):
            r, path = self.run_apply(text, audit_page=None, tag="hub-keep", evidence=evidence)
            self.assertEqual(r.returncode, 0, (evidence, r.stderr))
            self.assertIn('source_ids = ["book-a", "book-c"]', path.read_text())

    def test_format_3_curated_book_loses_its_placement(self):
        book = ('[[books]]\nsource = "book-b"\n\n[[books.chapters]]\ntitle = "Spells"\n\n'
                '[[books.chapters.children]]\ntitle = "Test Spell"\nentry = "ref/spell/test-spell"\n')
        r, path = self.run_apply(entry(ROW, "Text.\n"), books={"books/book-b.toml": book})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("books/: placements dropped 1", r.stdout)
        self.assertNotIn("ref/spell/test-spell", (self.corpus / "books/book-b.toml").read_text())
        self.assertIn('source_ids = ["book-a", "book-c"]', path.read_text())

    def test_format_3_derived_book_has_no_file_and_nothing_to_drop(self):
        r, path = self.run_apply(entry(ROW, "Text.\n"), books={"books/book-a.toml": '[[books]]\nsource = "book-a"\n'})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("books/: placements dropped 0", r.stdout)
        self.assertIn('source_ids = ["book-a", "book-c"]', path.read_text())

    def test_format_3_placement_with_a_nested_child_is_refused_before_any_write(self):
        book = ('[[books]]\nsource = "book-b"\n\n[[books.chapters]]\ntitle = "Spells"\n\n'
                '[[books.chapters.children]]\ntitle = "Alpha"\nentry = "ref/spell/alpha"\n\n'
                '[[books.chapters.children]]\ntitle = "Test Spell"\nentry = "ref/spell/test-spell"\n\n'
                '[[books.chapters.children.children]]\ntitle = "Child"\nentry = "ref/spell/child"\n')
        text = entry(ROW, "Text.\n")
        r, path = self.run_apply(text, books={"books/book-b.toml": book})
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("has children", r.stderr)
        self.assertEqual((self.corpus / "books/book-b.toml").read_text(), book)
        self.assertEqual(path.read_text(), text)

    def test_body_line_beside_a_released_row_is_refused(self):
        text = entry(ROW, "Text.\n\n**Source:** Beta Book pg. 12\n")
        r, path = self.run_apply(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("body source line", r.stderr)
        self.assertEqual(path.read_text(), text)

    def test_plural_body_line_beside_a_row_is_refused(self):
        text = entry(ROW, "Text.\n\n**Sources:** Beta Book pg. 12, Alpha Book pg. 3\n")
        r, path = self.run_apply(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(path.read_text(), text)

    def test_body_line_alone_is_refused(self):
        text = entry("", "Text.\n\n**source:** Beta Book/12\n")
        r, path = self.run_apply(text, audit_page=None)
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(path.read_text(), text)

    def test_body_line_for_another_book_does_not_block(self):
        r, path = self.run_apply(entry(ROW, "Text.\n\n**Source:** Alpha Book pg. 3\n"))
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_row_without_audit_is_refused(self):
        text = entry(ROW, "Text.\n")
        r, path = self.run_apply(text, audit_page=None)
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(path.read_text(), text)

    def test_audit_with_other_page_is_refused(self):
        text = entry(ROW, "Text.\n")
        r, path = self.run_apply(text, audit_page="13")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(path.read_text(), text)

    def run_first(self, text: str, gate: str = "primary", proposed: str = "book-b", status: str = "printed",
                  print_page: str = "12", extra: list[dict] | None = None, rerun: bool = False):
        """Remove book-a, the entry's first book, with a gated queue row."""
        tmp = Path(tempfile.mkdtemp())
        (tmp / "entries/spell").mkdir(parents=True)
        (tmp / "publications.toml").write_text(PUBS, encoding="utf-8")
        (tmp / "books.toml").write_text('[[books]]\nsource = "book-a"\n', encoding="utf-8")
        path = tmp / "entries/spell/test-spell.md"
        path.write_text(text, encoding="utf-8")
        queue = tmp / "queue.tsv"
        row = dict.fromkeys(QUEUE_HEAD, "")
        row.update(book="book-a", entry="ref/spell/test-spell", kind="spell", title="Test Spell", tag="family-leak",
                   gate=gate, proposed_primary=proposed, proposed_status=status, verdict="remove", print_page=print_page,
                   evidence="whole-book-absent-new-primary-printed")
        with open(queue, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=QUEUE_HEAD, delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerow(row)
            for more in extra or []:
                other = dict.fromkeys(QUEUE_HEAD, "")
                other.update(entry="ref/spell/test-spell", kind="spell", title="Test Spell", tag="uncited",
                             verdict="remove", print_page="none", evidence="whole-book-absent")
                other.update(more)
                w.writerow(other)
        args = [sys.executable, str(APPLY), str(tmp), "--queue", str(queue), "--audit", str(tmp / "none.tsv")]
        r = subprocess.run(args, capture_output=True, text=True)
        if rerun:
            first = path.read_text()
            again = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(again.returncode, 0, again.stderr)
            self.assertIn("already out 1", again.stdout)
            self.assertEqual(path.read_text(), first)
        return r, path

    def test_cleared_first_book_is_removed_and_the_proposed_book_becomes_first(self):
        r, path = self.run_first(entry(ROW, "Text.\n"))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('source_ids = ["book-b", "book-c"]', path.read_text())

    def test_first_book_with_the_wrong_proposed_primary_is_refused(self):
        text = entry(ROW, "Text.\n")
        r, path = self.run_first(text, proposed="book-c")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(path.read_text(), text)

    def test_first_book_whose_new_primary_has_no_page_is_refused(self):
        text = entry("", "Text.\n")
        r, path = self.run_first(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("no page citation", r.stderr)
        self.assertEqual(path.read_text(), text)

    def test_first_book_row_that_is_not_cleared_is_refused(self):
        for gate, status in (("primary", "unscreened"), ("primary", "(none)"), ("other", "printed")):
            text = entry(ROW, "Text.\n")
            r, path = self.run_first(text, gate=gate, status=status)
            self.assertNotEqual(r.returncode, 0, (gate, status))
            self.assertEqual(path.read_text(), text)

    def test_first_book_without_a_gate_is_refused(self):
        text = entry(ROW, "Text.\n")
        r, path = self.run_first(text, gate="", proposed="")
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(path.read_text(), text)

    def test_queue_that_also_removes_the_proposed_new_first_book_is_refused(self):
        text = entry(ROW, "Text.\n")
        r, path = self.run_first(text, extra=[dict(book="book-b")])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("also removes", r.stderr)
        self.assertEqual(path.read_text(), text)

    def test_new_first_book_cited_at_another_page_than_the_reviewed_one_is_refused(self):
        text = entry(ROW, "Text.\n")
        r, path = self.run_first(text, print_page="13")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("reviewed print_page", r.stderr)
        self.assertEqual(path.read_text(), text)

    def test_a_successful_first_book_removal_can_run_again(self):
        r, path = self.run_first(entry(ROW, "Text.\n"), rerun=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('source_ids = ["book-b", "book-c"]', path.read_text())


class CiteTest(unittest.TestCase):
    def run_cite(self, text: str, verdict: str = "cite", print_page: str = "12", book: str = "book-b",
                 flags: list[str] | None = None, tmp: Path | None = None):
        """One queue row on `ref/spell/test-spell`; returns (result, entry path, argv, corpus)."""
        if tmp is None:
            tmp = Path(tempfile.mkdtemp())
            (tmp / "entries/spell").mkdir(parents=True)
            (tmp / "publications.toml").write_text(PUBS, encoding="utf-8")
            (tmp / "books.toml").write_text('[[books]]\nsource = "book-a"\n', encoding="utf-8")
            (tmp / "entries/spell/test-spell.md").write_text(text, encoding="utf-8")
            queue = tmp / "queue.tsv"
            row = dict.fromkeys(QUEUE_HEAD, "")
            row.update(book=book, entry="ref/spell/test-spell", kind="spell", title="Test Spell", tag="uncited",
                       verdict=verdict, print_page=print_page, evidence="section-printed")
            with open(queue, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=QUEUE_HEAD, delimiter="\t", lineterminator="\n")
                w.writeheader()
                w.writerow(row)
        argv = [sys.executable, str(APPLY), str(tmp), "--queue", str(tmp / "queue.tsv"),
                "--audit", str(tmp / "none.tsv")] + (flags or [])
        r = subprocess.run(argv, capture_output=True, text=True)
        return r, tmp / "entries/spell/test-spell.md", argv, tmp

    def test_row_is_added_and_a_second_run_changes_nothing(self):
        text = entry("", "Text.\n")
        r, path, argv, tmp = self.run_cite(text, flags=["--check"])
        self.assertEqual(r.returncode, 1, r.stdout)  # pending before the run
        self.assertIn("pending changes: 1", r.stdout)
        self.assertEqual(path.read_text(), text)  # --check writes nothing
        r, path, argv, tmp = self.run_cite(text, tmp=tmp)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("added 1", r.stdout)
        out = path.read_text()
        self.assertIn('[[sources]]\npublication = "book-b"\npage = "12"\n\n[fields]', out)
        again = subprocess.run(argv, capture_output=True, text=True)
        self.assertIn("added 0, already there 1", again.stdout)
        self.assertEqual(path.read_text(), out)
        done = subprocess.run(argv + ["--check"], capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stdout)
        self.assertIn("pending changes: 0", done.stdout)

    def test_row_goes_where_source_ids_order_puts_it(self):
        a = '[[sources]]\npublication = "book-a"\npage = "3"\n'
        c = '[[sources]]\npublication = "book-c"\npage = "5"\n'
        r, path, *_ = self.run_cite(entry(a + c, "Text.\n"))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn(a + '[[sources]]\npublication = "book-b"\npage = "12"\n' + c, path.read_text())
        r, path, *_ = self.run_cite(entry(c, "Text.\n"))
        self.assertIn('[[sources]]\npublication = "book-b"\npage = "12"\n' + c, path.read_text())

    def test_row_without_a_page_gets_the_page(self):
        r, path, *_ = self.run_cite(entry('[[sources]]\npublication = "book-b"\n', "Text.\n"))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('publication = "book-b"\npage = "12"', path.read_text())

    def test_row_with_another_page_is_refused(self):
        text = entry('[[sources]]\npublication = "book-b"\npage = "13"\n', "Text.\n")
        r, path, *_ = self.run_cite(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("cites book-b at p. 13", r.stderr)
        self.assertEqual(path.read_text(), text)

    def test_book_outside_source_ids_and_expanded_in_credit_are_refused(self):
        text = entry("", "Text.\n").replace('"book-a", "book-b", "book-c"', '"book-a", "book-c"')
        r, path, *_ = self.run_cite(text)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("is not in source_ids", r.stderr)
        credit = text.replace("\n[fields]", '[[expanded_in]]\npublication = "book-b"\npage = "12"\n\n[fields]', 1)
        r, path, *_ = self.run_cite(credit)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("expanded_in", r.stderr)
        self.assertEqual(path.read_text(), credit)

    def test_page_that_is_not_a_page_is_refused(self):
        for page in ("", "none", "12a", "p. 12"):
            text = entry("", "Text.\n")
            r, path, *_ = self.run_cite(text, print_page=page)
            self.assertNotEqual(r.returncode, 0, page)
            self.assertEqual(path.read_text(), text)

    def test_inside_cover_is_a_page(self):
        """Some books print an entry on the inside cover, which has no number (corpus convention)."""
        r, path, *_ = self.run_cite(entry("", "Text.\n"), print_page="inside cover")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('publication = "book-b"\npage = "inside cover"\n', path.read_text())

    def test_body_line_stays_unless_convert_body_is_given(self):
        text = entry("", "Text.\n\n**Source** Beta Book pg. 12\\\nMore text.\n")
        r, path, *_ = self.run_cite(text)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("**Source** Beta Book pg. 12\\", path.read_text())
        r, path, *_ = self.run_cite(text, flags=["--convert-body"])
        self.assertEqual(r.returncode, 0, r.stderr)
        out = path.read_text()
        self.assertNotIn("Beta Book", out.split("+++", 2)[2])
        self.assertIn("Text.\n\nMore text.\n", out)

    def test_convert_body_keeps_the_other_books_of_the_line(self):
        text = entry("", "Text.\n\n**Sources:** Alpha Book pg 3, Beta Book pg 12-13\n")
        r, path, *_ = self.run_cite(text, flags=["--convert-body"])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("**Sources:** Alpha Book pg 3\n", path.read_text())

    def test_convert_body_reads_the_series_prefix_of_the_old_citations(self):
        """`Pathfinder RPG Beta Book` and `PRPG Beta Book` are the book; `Beta Book 5` is another one."""
        text = entry("", "Text.\n\n**Sources:** Pathfinder RPG Beta Book pg 12\\\nA.\n\n**Sources:** PRPG Beta Book pg 12\nB.\n\n"
                         "**Sources:** Beta Book 5 pg 12\\\nC.\n")
        r, path, *_ = self.run_cite(text, flags=["--convert-body"])
        self.assertEqual(r.returncode, 0, r.stderr)
        body = path.read_text().split("+++", 2)[2]
        self.assertNotIn("Pathfinder RPG Beta Book", body)
        self.assertNotIn("PRPG Beta Book", body)
        self.assertIn("**Sources:** Beta Book 5 pg 12\\\nC.", body)

    def test_convert_body_with_another_page_is_refused_before_any_write(self):
        text = entry("", "Text.\n\n**Source** Beta Book pg. 40\\\n")
        r, path, *_ = self.run_cite(text, flags=["--convert-body"])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("reconcile it by hand", r.stderr)
        self.assertEqual(path.read_text(), text)

    def test_a_keep_row_without_its_row_is_pending_and_with_it_is_not(self):
        r, path, *_ = self.run_cite(entry("", "Text.\n"), verdict="keep", flags=["--check"])
        self.assertEqual(r.returncode, 1)
        self.assertIn("verdict keep and no [[sources]] row: 1", r.stdout)
        r, path, *_ = self.run_cite(entry('[[sources]]\npublication = "book-b"\npage = "12"\n', "T.\n"),
                                    verdict="keep", flags=["--check"])
        self.assertEqual(r.returncode, 0, r.stdout)

    def run_mixed(self, cite_text: str):
        """A removal (book-c from `one`) and a cite (book-b on `two`) in one queue."""
        tmp = Path(tempfile.mkdtemp())
        (tmp / "entries/spell").mkdir(parents=True)
        (tmp / "publications.toml").write_text(PUBS, encoding="utf-8")
        (tmp / "books.toml").write_text('[[books]]\nsource = "book-a"\n', encoding="utf-8")
        one = tmp / "entries/spell/one.md"
        two = tmp / "entries/spell/two.md"
        one.write_text(entry("", "Text.\n").replace("test-spell", "one"), encoding="utf-8")
        two.write_text(cite_text.replace("test-spell", "two"), encoding="utf-8")
        queue = tmp / "queue.tsv"
        with open(queue, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=QUEUE_HEAD, delimiter="\t", lineterminator="\n")
            w.writeheader()
            for eid, book, verdict, page, ev in (("ref/spell/one", "book-c", "remove", "3", "whole-book-absent"),
                                                 ("ref/spell/two", "book-b", "cite", "12", "section-printed")):
                row = dict.fromkeys(QUEUE_HEAD, "")
                row.update(book=book, entry=eid, kind="spell", title="Test Spell", tag="uncited", verdict=verdict,
                           print_page=page, evidence=ev)
                w.writerow(row)
        argv = [sys.executable, str(APPLY), str(tmp), "--queue", str(queue), "--audit", str(tmp / "none.tsv")]
        return subprocess.run(argv, capture_output=True, text=True), one, two

    def test_a_refused_cite_after_a_removal_leaves_every_file_unchanged(self):
        before_one = entry("", "Text.\n").replace("test-spell", "one")
        bad_two = entry('[[sources]]\npublication = "book-b"\npage = "13"\n', "Text.\n")  # another page: refused
        r, one, two = self.run_mixed(bad_two)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("cites book-b at p. 13", r.stderr)
        self.assertEqual(one.read_text(), before_one)  # the removal was not written
        self.assertEqual(two.read_text(), bad_two.replace("test-spell", "two"))

    def test_the_same_mix_applies_when_every_row_is_valid(self):
        r, one, two = self.run_mixed(entry("", "Text.\n"))
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('source_ids = ["book-a", "book-b"]', one.read_text())
        self.assertIn('publication = "book-b"\npage = "12"', two.read_text())


if __name__ == "__main__":
    unittest.main()
