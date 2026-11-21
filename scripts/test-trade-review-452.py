#!/usr/bin/env python3
"""Test the `split` command of scripts/trade-review-452.py on a small synthetic corpus (no real data).

    python3 scripts/test-trade-review-452.py

Cases: `split`, `fill`, `apply` and `check` turn a composite trade into its parts, renumber the later trades
of the entry in the baseline and the queue, and leave the queue consistent; a second run of every command
changes no byte; parts that do not join with `, ` to the composite are refused before anything is written.
"""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "trade-review-452.py"
ENTRY = "ref/arc-wiz/adept"
COMPOSITE = "Scribe scroll, 5th- and 10th-level bonus feats"
FILES = {
    "publications.toml": '[[publication]]\nid = "book-a"\ntitle = "Book A"\n',
    "entries/class/wiz.md": (
        '+++\nid = "ref/class/wiz"\nkind = "class"\n+++\n\n'
        "#### Scribe Scroll {#scribe-scroll}\n\n#### Bonus Feats {#bonus-feats}\n"
    ),
    "entries/arc-wiz/adept.md": (
        f'+++\nid = "{ENTRY}"\nkind = "archetype"\nsource_ids = ["book-a"]\n'
        'relations = [\n  { kind = "archetype", target = "ref/class/wiz" },\n]\n'
        '[[sources]]\npublication = "book-a"\npage = "8"\n\n[fields]\nkind = "archetype"\ntrades = [\n'
        f'  {{ replaces = "{COMPOSITE}" }},\n  {{ alters = "Arcane bond", feature = "arcane-bond" }},\n'
        '  { replaces = "Poison use" },\n]\n+++\n\nBody.\n'
    ),
    "scripts/trade-review-452-baseline.tsv": (
        "id\tkind\ttrade\top\tprinted\treason\tcandidates\tunclaimed_old_anchors\tsubsection\n"
        f"{ENTRY}\tarchetype\t1\treplaces\t{COMPOSITE}\tno-heading\t\t\t\n"
        f"{ENTRY}\tarchetype\t3\treplaces\tPoison use\tno-heading\t\t\t\n"
    ),
    "scripts/trade-review-452-decisions.tsv": (
        "scope\tprinted\tdisposition\tcode\tfeature\tclass\tlevels\tpower\tnote\n"
        f"{ENTRY}\tpoison use\texception\tno-class-heading\t\t\t\t\tthe class has no such feature\n"
    ),
    "scripts/trade-evidence-452.tsv": (
        "id\tprinted\tsubsection\tbook\tpage\tnote\n"
        f"{ENTRY}\tScribe scroll\t\tBook A\t8\tprint: parts\n"
        f"{ENTRY}\t5th- and 10th-level bonus feats\t\tBook A\t8\tprint: parts\n"
        f"{ENTRY}\tPoison use\t\tBook A\t8\tprint: line\n"
    ),
}
SPLITS_HEAD = "id\top\tcomposite\tpart\tfeature\tclass\tlevels\tpower\tnote\n"
GOOD = (
    f"{ENTRY}\treplaces\t{COMPOSITE}\tScribe scroll\tscribe-scroll\t\t\t\tpart 1\n"
    f"{ENTRY}\treplaces\t{COMPOSITE}\t5th- and 10th-level bonus feats\tbonus-feats\t\t5,10\t\tpart 2\n"
)
BAD = GOOD.replace("Scribe scroll\tscribe-scroll", "Scribe scrolls\tscribe-scroll")


def run(root, *command):
    return subprocess.run(
        [sys.executable, "-I", str(root / "scripts/trade-review-452.py"), *command],
        cwd=root, capture_output=True, text=True,
    )


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


class SplitTest(unittest.TestCase):
    def corpus(self, splits):
        root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, root, True)
        for name, text in FILES.items():
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            (root / name).write_text(text, encoding="utf-8")
        shutil.copy(TOOL, root / "scripts/trade-review-452.py")
        (root / "scripts/trade-splits-452.tsv").write_text(SPLITS_HEAD + splits, encoding="utf-8")
        return root

    def test_split_renumbers_and_is_idempotent(self):
        root = self.corpus(GOOD)
        for command in ("split", "fill", "apply", "check"):
            done = run(root, command)
            self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        entry = (root / "entries/arc-wiz/adept.md").read_text(encoding="utf-8")
        self.assertIn('{ replaces = "Scribe scroll", feature = "scribe-scroll" },\n'
                      '  { replaces = "5th- and 10th-level bonus feats", feature = "bonus-feats", levels = [5, 10] },\n'
                      '  { alters = "Arcane bond", feature = "arcane-bond" },\n  { replaces = "Poison use" },', entry)
        baseline = (root / "scripts/trade-review-452-baseline.tsv").read_text(encoding="utf-8").splitlines()
        self.assertEqual([line.split("\t")[2:5] for line in baseline[1:]],
                         [["1", "replaces", "Scribe scroll"], ["2", "replaces", "5th- and 10th-level bonus feats"],
                          ["4", "replaces", "Poison use"]])
        queue = (root / "scripts/trade-review-452.tsv").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(queue), 4)
        self.assertEqual([line.split("\t")[9] for line in queue[1:]], ["resolved", "resolved", "exception"])
        before = snapshot(root)
        for command in ("split", "fill", "apply", "check"):
            self.assertEqual(run(root, command).returncode, 0)
        self.assertEqual(snapshot(root), before)

    def test_a_composite_that_returns_fails_the_check(self):
        root = self.corpus(GOOD)
        for command in ("split", "fill", "apply"):
            self.assertEqual(run(root, command).returncode, 0)
        path = root / "entries/arc-wiz/adept.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace('  { replaces = "Scribe scroll", feature = "scribe-scroll" },\n', f'  {{ replaces = "{COMPOSITE}" }},\n  {{ replaces = "Scribe scroll", feature = "scribe-scroll" }},\n'), encoding="utf-8")
        done = run(root, "check")
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("still a trade", done.stdout)

    def test_parts_that_do_not_join_are_refused_before_anything_is_written(self):
        root = self.corpus(BAD)
        before = snapshot(root)
        done = run(root, "split")
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("do not join", done.stderr)
        self.assertEqual(snapshot(root), before)


if __name__ == "__main__":
    unittest.main()
