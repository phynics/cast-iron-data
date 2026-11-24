#!/usr/bin/env python3
"""Test scripts/hub-topic-lists-461.py on a small synthetic corpus and dataset (no real data).

    python3 scripts/test-hub-topic-lists-461.py

Cases: a hub in the warning (a non-first book without a row), with at most 40 words and no block,
is restored with one block per subtopic in upstream order; a subtopic record that two entries share
resolves to the one from the same upstream file, then to the `json/rules_*` one; two entries from
two other files stay unresolved and go to the review file; a second run changes nothing and
`--check` is 1 before the run and 0 after; a hub with a `[[sources]]` row for every non-first book,
and an entry with real text, are left alone.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "hub-topic-lists-461.py"


def entry(eid, title, books, path, record, body, rows=()):
    r = "".join(f'[[sources]]\npublication = "{b}"\npage = "1"\n' for b in rows)
    return (f'+++\nid = "{eid}"\nkind = "rule"\ntitle = "{title}"\nsource_ids = {json.dumps(books)}\n'
            f'provenance = [\n  {{ dataset = "pathfinder-data-1-e", record = "{record}", path = "{path}" }},\n]\n'
            f'{r}\n[fields]\nkind = "none"\n+++\n{body}\n')


class HubTopicLists(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        t = Path(self.tmp.name)
        self.root, self.ds = t / "corpus", t / "dataset"
        (self.root / "entries" / "rule").mkdir(parents=True)
        (self.ds / "json").mkdir(parents=True)
        files = {
            "hub": entry("ref/rule/hub", "Hub", ["a", "b"], "json/rules_x.json", "hub", "These are topics."),
            "weather": entry("ref/rule/weather", "Weather", ["a"], "json/rules_x.json", "weather", "Rain."),
            "domain": entry("ref/domain/weather", "Weather Domain", ["a"], "json/domains.json", "weather", "Domain."),
            "twin1": entry("ref/rule/twin-one", "Twin", ["a"], "json/rules_y.json", "twin", "One."),
            "twin2": entry("ref/rule/twin-two", "Twin", ["a"], "json/rules_z.json", "twin", "Two."),
            "solo": entry("ref/rule/solo", "Solo", ["a"], "json/rules_x.json", "solo", "Solo."),
            "cited": entry("ref/rule/cited", "Cited", ["a", "b"], "json/rules_x.json", "cited", "Cited hub.", rows=["b"]),
            "long": entry("ref/rule/long", "Long", ["a", "b"], "json/rules_x.json", "long", "word " * 60),
        }
        for name, text in files.items():
            (self.root / "entries" / "rule" / f"{name}.md").write_text(text, encoding="utf-8")
        data = {
            "hub": {"name": "Hub", "subtopics": ["weather", "twin", "solo", "missing", "weather"]},
            "weather": {"name": "Weather"},
            "solo": {"name": "Solo"},
            "cited": {"name": "Cited", "subtopics": ["solo"]},
            "long": {"name": "Long", "subtopics": ["solo"]},
        }
        (self.ds / "json" / "rules_x.json").write_text(json.dumps(data), encoding="utf-8")
        (self.ds / "json" / "domains.json").write_text(json.dumps({"weather": {"name": "Weather"}}), encoding="utf-8")
        (self.ds / "json" / "rules_y.json").write_text(json.dumps({"twin": {"name": "Twin"}}), encoding="utf-8")
        (self.ds / "json" / "rules_z.json").write_text(json.dumps({"twin": {"name": "Twin"}}), encoding="utf-8")
        self.review = t / "review.tsv"

    def tearDown(self):
        self.tmp.cleanup()

    def run_script(self, *args):
        return subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root), "--dataset", str(self.ds), *args],
                              capture_output=True, text=True)

    def hub(self):
        return (self.root / "entries" / "rule" / "hub.md").read_text(encoding="utf-8")

    def test_restore(self):
        self.assertEqual(self.run_script("--check").returncode, 1)
        r = self.run_script("--apply", "--review", str(self.review))
        self.assertEqual(r.returncode, 0, r.stderr)
        targets = [l.split('"')[1] for l in self.hub().split("\n") if l.startswith("target = ")]
        # weather resolves to the entry of the same upstream file (not the domain); the repeated
        # subtopic is written once; the two twins compete and the missing record has no entry
        self.assertEqual(targets, ["ref/rule/weather", "ref/rule/solo"])
        review = self.review.read_text(encoding="utf-8").splitlines()
        self.assertEqual([l.split("\t")[1:3] for l in review[1:]], [["twin", "ambiguous"], ["missing", "no-entry"]])
        # entries that are not hubs of the list are untouched
        self.assertNotIn("entry-link", (self.root / "entries" / "rule" / "cited.md").read_text(encoding="utf-8"))
        self.assertNotIn("entry-link", (self.root / "entries" / "rule" / "long.md").read_text(encoding="utf-8"))

    def test_second_run_changes_nothing(self):
        self.run_script("--apply")
        before = self.hub()
        self.assertEqual(self.run_script("--apply").returncode, 0)
        self.assertEqual(self.hub(), before)
        self.assertEqual(self.run_script("--check").returncode, 0)

    def test_check_finds_a_stray_block(self):
        self.run_script("--apply")
        p = self.root / "entries" / "rule" / "hub.md"
        p.write_text(p.read_text(encoding="utf-8") + '\n::: entry-link\ntarget = "ref/rule/cited"\ntitle = "Cited"\n:::\n', encoding="utf-8")
        r = self.run_script("--check")
        self.assertEqual(r.returncode, 2, r.stdout)
        self.assertIn("mismatch: ref/rule/hub", r.stdout)


if __name__ == "__main__":
    unittest.main()
