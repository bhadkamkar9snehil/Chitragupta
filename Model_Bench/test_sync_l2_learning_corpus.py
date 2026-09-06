#!/usr/bin/env python3
"""Contract tests for canonical learning-corpus refresh boundaries."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODULE = ROOT / "sync_l2_learning_corpus.py"
_spec = importlib.util.spec_from_file_location("sync_l2_learning_corpus_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


class LearningCorpusSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name) / "vault"
        self.vault.mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def test_sync_rebuilds_only_canonical_mirror_and_preserves_runtime_planes(self):
        old_knowledge = self.vault / "knowledge" / "git" / "old.md"
        old_knowledge.parent.mkdir(parents=True)
        old_knowledge.write_text("stale mirror", encoding="utf-8")

        runtime_files = {
            "sessions/x.md": "session",
            "cases/approved/x.md": "case",
            "facts/x.md": "fact",
            "candidates/x.md": "candidate",
            "solutions/approved/x.md": "governed solution",
            "actions/plans/x.json": "{}",
            "actions/candidates/x.json": "{}",
            "eval/x.jsonl": "{}\n",
        }
        for rel, content in runtime_files.items():
            path = self.vault / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        source = Path(self.tmp.name) / "source.md"
        source.write_text("current canonical reference", encoding="utf-8")
        mod._sync(
            self.vault,
            [(source, Path("knowledge/git/current.md"))],
            {"schema_version": 1, "files": []},
        )

        self.assertFalse(old_knowledge.exists())
        self.assertEqual(
            (self.vault / "knowledge/git/current.md").read_text(encoding="utf-8"),
            "current canonical reference",
        )
        for rel, content in runtime_files.items():
            with self.subTest(rel=rel):
                self.assertEqual((self.vault / rel).read_text(encoding="utf-8"), content)

    def test_sync_creates_runtime_directories_without_populating_them(self):
        mod._sync(self.vault, [], {"schema_version": 1, "files": []})
        for rel in mod.RUNTIME_DIRS:
            with self.subTest(rel=rel):
                self.assertTrue((self.vault / rel).is_dir())


if __name__ == "__main__":
    unittest.main(verbosity=2)
