#!/usr/bin/env python3
"""Contract tests for GBrain trust-source synchronization."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import sync_l2_gbrain as mod


class GBrainSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name) / "vault"
        for rel in mod.SOURCE_DIRS.values():
            (self.vault / rel).mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        self.tmp.cleanup()

    def test_check_rejects_missing_or_federated_sources(self):
        rows = [{"id": "l2-knowledge", "config": {"federated": True}}]
        rows.extend(
            {"id": source_id, "config": {"federated": False}}
            for source_id in mod.SOURCE_DIRS
            if source_id not in {"l2-knowledge", "l2-sessions"}
        )
        with mock.patch.object(mod, "_sources_list", return_value=rows):
            errors = mod._check_sources(self.vault)
        self.assertIn("GBrain source must be non-federated: l2-knowledge", errors)
        self.assertIn("missing GBrain source: l2-sessions", errors)

    def test_registration_uses_non_federated_explicit_paths(self):
        calls = []
        def fake_run(args, **kwargs):
            calls.append(args)
            return 0, "{}", ""
        with mock.patch.object(mod, "run", side_effect=fake_run):
            created = mod._register_missing(self.vault, {})
        self.assertEqual(set(created), set(mod.SOURCE_DIRS))
        self.assertEqual(len(calls), len(mod.SOURCE_DIRS))
        for args in calls:
            self.assertEqual(args[:2], ["sources", "add"])
            self.assertIn("--no-federated", args)
            self.assertIn("--force", args)
            self.assertIn("--path", args)

    def test_sync_names_every_source_individually(self):
        calls = []
        def fake_run(args, **kwargs):
            calls.append(args)
            return 0, "", ""
        with mock.patch.object(mod, "run", side_effect=fake_run):
            synced = mod._sync_sources()
        self.assertEqual(synced, list(mod.SOURCE_DIRS))
        self.assertEqual(calls, [["sync", "--source", source] for source in mod.SOURCE_DIRS])


if __name__ == "__main__":
    unittest.main(verbosity=2)
