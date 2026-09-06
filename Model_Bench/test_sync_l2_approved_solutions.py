#!/usr/bin/env python3
"""Contract tests for governed SQL Solution export into trusted retrieval scope."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent
MODULE = ROOT / "sync_l2_approved_solutions.py"
_spec = importlib.util.spec_from_file_location("sync_l2_approved_solutions_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


def row(solution_id="S-1", title="Known issue", usage_count=3):
    return {
        "ID": solution_id,
        "Title": title,
        "ProblemSummary": "Posting remains pending after upstream success.",
        "RootCause": "Retry state was not advanced.",
        "ResolutionSteps": "Use the reviewed supported retry path and verify terminal state.",
        "RootCauseCategoryID": "RC-1",
        "Route": "sap_api",
        "RelatedViewsJson": '["dbo.SAP_Posting_Tbl"]',
        "Tags": "sap,retry",
        "UsageCount": usage_count,
    }


class GovernedSolutionExportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.vault = self.root / "vault"
        self.policy = self.root / "policy.json"

    def tearDown(self):
        self.tmp.cleanup()

    def _write_policy(self, approved):
        self.policy.write_text(json.dumps({"schema_version": 1, "approved": approved}), encoding="utf-8")

    def _approve(self, source):
        self._write_policy([{
            "solution_id": source["ID"], "content_sha256": mod.content_sha256(source),
            "approved_by": "operator", "approved_at": "2026-09-06T00:00:00+00:00",
            "review_evidence": "Reviewed against independently verified resolved tickets.",
        }])

    def test_empty_policy_performs_no_live_sql_read(self):
        self._write_policy([])
        with mock.patch.object(mod, "_query_live_solutions", side_effect=AssertionError("must not query")):
            result = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=None)
        self.assertTrue(result["ok"])
        self.assertEqual(result["approved_count"], 0)
        self.assertEqual(list((self.vault / "solutions" / "approved").glob("*.md")) if (self.vault / "solutions" / "approved").exists() else [], [])

    def test_explicit_hash_pinned_approval_exports_trusted_markdown(self):
        source = row(); digest = mod.content_sha256(source); self._approve(source)
        result = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[source])
        self.assertTrue(result["ok"]); self.assertEqual(result["exported"], 1)
        files = list((self.vault / "solutions" / "approved").glob("*.md"))
        self.assertEqual(len(files), 1)
        text = files[0].read_text(encoding="utf-8")
        self.assertIn('trust: "governed_reusable_solution"', text)
        self.assertIn(digest, text)
        self.assertIn("Verify applicability and live state", text)

    def test_identical_second_sync_is_byte_stable_and_skipped(self):
        source = row(); self._approve(source)
        first = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[source])
        self.assertEqual(first["exported"], 1)
        path = next((self.vault / "solutions" / "approved").glob("*.md"))
        before = path.read_bytes()
        second = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[source])
        self.assertTrue(second["ok"]); self.assertEqual(second["exported"], 0); self.assertEqual(second["skipped"], 1)
        self.assertEqual(path.read_bytes(), before)

    def test_usage_count_change_does_not_invalidate_semantic_approval(self):
        source = row(usage_count=3); self._approve(source)
        digest = mod.content_sha256(source)
        changed_counter = row(usage_count=99)
        self.assertEqual(mod.content_sha256(changed_counter), digest)
        first = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[source])
        self.assertTrue(first["ok"])
        second = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[changed_counter])
        self.assertTrue(second["ok"]); self.assertEqual(second["exported"], 0); self.assertEqual(second["skipped"], 1)
        text = next((self.vault / "solutions" / "approved").glob("*.md")).read_text(encoding="utf-8")
        self.assertIn("UsageCount at this sync: 99", text)

    def test_live_semantic_content_drift_fails_closed(self):
        source = row(); self._approve(source)
        changed = row(title="Changed after review")
        result = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[changed])
        self.assertFalse(result["ok"])
        self.assertIn("content drift", "\n".join(result["errors"]))
        self.assertFalse((self.vault / "solutions" / "approved" / "s-1.md").exists())

    def test_semantic_drift_archives_previous_trusted_export(self):
        source = row(); self._approve(source)
        self.assertTrue(mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[source])["ok"])
        changed = row(title="Changed after review")
        drift = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[changed])
        self.assertFalse(drift["ok"]); self.assertEqual(drift["archived"], 1)
        self.assertEqual(list((self.vault / "solutions" / "approved").glob("*.md")), [])
        self.assertEqual(len(list((self.vault / "archive" / "solutions").glob("*.md"))), 1)

    def test_removing_approval_archives_only_managed_export(self):
        source = row(); self._approve(source)
        first = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[source])
        self.assertTrue(first["ok"])
        hand = self.vault / "solutions" / "approved" / "hand-authored.md"
        hand.write_text("do not sweep", encoding="utf-8")
        self._write_policy([])
        second = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[])
        self.assertTrue(second["ok"]); self.assertEqual(second["archived"], 1)
        self.assertTrue(hand.exists())
        self.assertEqual(len(list((self.vault / "archive" / "solutions").glob("*.md"))), 1)

    def test_policy_requires_governance_metadata_and_full_hash(self):
        self._write_policy([{"solution_id": "S-1", "content_sha256": "abc"}])
        result = mod.sync_approved_solutions(vault=self.vault, policy_path=self.policy, rows=[row()])
        self.assertFalse(result["ok"])
        errors = "\n".join(result["errors"])
        self.assertIn("64 lowercase hex", errors)
        self.assertIn("approved_by", errors)
        self.assertIn("review_evidence", errors)


if __name__ == "__main__":
    unittest.main(verbosity=2)
