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

    def _row(self, source_id: str, *, federated: bool = False, path: Path | None = None):
        return {
            "id": source_id,
            "config": {
                "federated": federated,
                "local_path": str(path or (self.vault / mod.SOURCE_DIRS[source_id])),
            },
        }

    def test_check_rejects_missing_federated_or_unbound_sources(self):
        rows = [self._row("l2-knowledge", federated=True)]
        rows.extend(
            self._row(source_id)
            for source_id in mod.SOURCE_DIRS
            if source_id not in {"l2-knowledge", "l2-sessions", "l2-candidates"}
        )
        rows.append({"id": "l2-candidates", "config": {"federated": False}})
        with mock.patch.object(mod, "_sources_list", return_value=rows):
            errors = mod._check_sources(self.vault)
        self.assertIn("GBrain source must be non-federated: l2-knowledge", errors)
        self.assertIn("missing GBrain source: l2-sessions", errors)
        self.assertIn("GBrain source path is not reported for l2-candidates", errors)

    def test_check_rejects_wrong_source_path(self):
        rows = [self._row(source_id) for source_id in mod.SOURCE_DIRS]
        rows[0] = self._row("l2-knowledge", path=self.vault / "wrong")
        with mock.patch.object(mod, "_sources_list", return_value=rows):
            errors = mod._check_sources(self.vault)
        self.assertTrue(any("path mismatch for l2-knowledge" in error for error in errors))

    def test_complete_non_federated_topology_passes(self):
        rows = [self._row(source_id) for source_id in mod.SOURCE_DIRS]
        with mock.patch.object(mod, "_sources_list", return_value=rows):
            self.assertEqual(mod._check_sources(self.vault), [])

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

    def test_dry_run_has_no_git_or_gbrain_side_effects(self):
        with mock.patch.object(mod, "available") as available, \
             mock.patch.object(mod, "_checkpoint") as checkpoint, \
             mock.patch.object(mod, "run") as run:
            result = mod.sync_gbrain(self.vault, dry_run=True)
        self.assertTrue(result["ok"])
        self.assertTrue(result["dry_run"])
        available.assert_not_called()
        checkpoint.assert_not_called()
        run.assert_not_called()

    def test_isolated_brain_is_initialized_when_missing(self):
        calls = []
        def fake_run(args, **kwargs):
            calls.append(args)
            if args[:2] == ["doctor", "--json"]:
                return 1, "", "missing"
            return 0, "", ""
        with mock.patch.object(mod, "run", side_effect=fake_run):
            initialized = mod._ensure_brain()
        self.assertTrue(initialized)
        self.assertIn(["init", "--pglite"], calls)

    def test_lockfile_lives_outside_vault(self):
        lock = self.vault.parent / f".{self.vault.name}.gbrain-sync.lock"
        with mod._sync_lock(self.vault) as acquired:
            self.assertTrue(acquired)
            self.assertTrue(lock.exists())
            self.assertFalse((self.vault / ".gbrain-sync.lock").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
