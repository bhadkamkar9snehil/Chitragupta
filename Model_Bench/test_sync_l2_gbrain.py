#!/usr/bin/env python3
"""Contracts for direct repository-reference and dynamic-vault GBrain synchronization."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import sync_l2_gbrain as mod


class GBrainSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.vault = root / "vault"
        self.repo = root / "repo"
        self.knowledge = self.repo / "Knowledge"
        self.reference = self.repo / "Reference Documents"
        self.knowledge.mkdir(parents=True)
        self.reference.mkdir(parents=True)
        for rel in mod.VAULT_SOURCE_DIRS.values():
            (self.vault / rel).mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        self.tmp.cleanup()

    def _path(self, source_id: str) -> Path:
        if source_id == "l2-knowledge":
            return self.knowledge
        if source_id == "l2-reference":
            return self.reference
        return self.vault / mod.VAULT_SOURCE_DIRS[source_id]

    def _row(self, source_id: str, *, federated: bool = False, path: Path | None = None):
        return {
            "id": source_id,
            "config": {
                "federated": federated,
                "local_path": str(path or self._path(source_id)),
            },
        }

    def test_static_reference_sources_are_not_vault_mirrors(self):
        paths = mod._expected_paths(self.vault, self.knowledge, self.reference)
        self.assertEqual(paths["l2-knowledge"], self.knowledge)
        self.assertEqual(paths["l2-reference"], self.reference)
        self.assertNotEqual(paths["l2-knowledge"], self.vault / "knowledge")
        self.assertNotEqual(paths["l2-reference"], self.vault / "reference")

    def test_complete_non_federated_topology_passes(self):
        rows = [self._row(source_id) for source_id in mod.SOURCE_IDS]
        with mock.patch.object(mod, "_sources_list", return_value=rows):
            self.assertEqual(mod._check_sources(self.vault, self.knowledge, self.reference), [])

    def test_check_rejects_federation_or_wrong_path(self):
        rows = [self._row(source_id) for source_id in mod.SOURCE_IDS]
        rows[0] = self._row("l2-knowledge", federated=True, path=self.vault / "wrong")
        with mock.patch.object(mod, "_sources_list", return_value=rows):
            errors = mod._check_sources(self.vault, self.knowledge, self.reference)
        self.assertTrue(any("non-federated: l2-knowledge" in e for e in errors))
        self.assertTrue(any("path mismatch for l2-knowledge" in e for e in errors))

    def test_registration_binds_repository_sources_directly(self):
        calls = []

        def fake_run(args, **kwargs):
            calls.append(args)
            return 0, "{}", ""

        with mock.patch.object(mod, "run", side_effect=fake_run):
            created = mod._register_missing(self.vault, {}, self.knowledge, self.reference)
        self.assertEqual(set(created), set(mod.SOURCE_IDS))
        for source_id, expected in (
            ("l2-knowledge", self.knowledge),
            ("l2-reference", self.reference),
        ):
            call = next(call for call in calls if call[2] == source_id)
            self.assertEqual(call[call.index("--path") + 1], str(expected))
            self.assertNotIn("--force", call)
        for call in calls:
            self.assertIn("--no-federated", call)

    def test_sync_names_each_source(self):
        calls = []

        def fake_run(args, **kwargs):
            calls.append(args)
            return 0, "", ""

        with mock.patch.object(mod, "run", side_effect=fake_run):
            synced = mod._sync_sources()
        self.assertEqual(synced, list(mod.SOURCE_IDS))
        self.assertEqual(calls, [["sync", "--source", source] for source in mod.SOURCE_IDS])

    def test_dry_run_has_no_git_or_gbrain_side_effects(self):
        with mock.patch.object(mod, "available") as available, \
             mock.patch.object(mod, "_checkpoint") as checkpoint, \
             mock.patch.object(mod, "run") as run:
            result = mod.sync_gbrain(
                self.vault,
                knowledge=self.knowledge,
                reference=self.reference,
                dry_run=True,
            )
        self.assertTrue(result["ok"])
        self.assertEqual(result["reference"], str(self.reference))
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
            self.assertTrue(mod._ensure_brain())
        self.assertIn(["init", "--pglite"], calls)

    def test_lockfile_lives_outside_vault(self):
        lock = self.vault.parent / f".{self.vault.name}.gbrain-sync.lock"
        with mod._sync_lock(self.vault) as acquired:
            self.assertTrue(acquired)
            self.assertTrue(lock.exists())
            self.assertFalse((self.vault / ".gbrain-sync.lock").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
