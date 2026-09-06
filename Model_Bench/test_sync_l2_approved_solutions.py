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


def row(solution_id="S-1", title="Known issue"):
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
        self.policy.write_text(
            json.dumps({"schema_version": 1, "approved": approved}),
            encoding="utf-8",
        )

    def _approve(self, source):
        self._write_policy([{
            "solution_id": source["ID"],
            "content_sha256": mod.content_sha256(source),
            "approved_by": "operator",
            "approved_at": "2026-09-06T00:00:00+00:00",
            "review_evidence": "Reviewed against independently verified resolved tickets.",
        }])

    def test_empty_policy_performs_no_live_sql_read_and_clears_generated_scope(self):
        approved_dir = self.vault / "solutions" / "approved"
        approved_dir.mkdir(parents=True)
        (approved_dir / "old.md").write_text("old generated export", encoding="utf-8")
        self._write_policy([])
        with mock.patch.object(
            mod, "_query_live_solutions", side_effect=AssertionError("must not query")
        ):
            result = mod.sync_approved_solutions(
                vault=self.vault, policy_path=self.policy, rows=None
            )
        self.assertTrue(result["ok"])
        self.assertEqual(result["removed"], 1)
        self.assertEqual(list(approved_dir.glob("*.md")), [])

    def test_explicit_hash_pinned_approval_exports_stable_trusted_markdown(self):
        source = row()
        digest = mod.content_sha256(source)
        self._approve(source)
        first = mod.sync_approved_solutions(
            vault=self.vault, policy_path=self.policy, rows=[source]
        )
        self.assertTrue(first["ok"])
        self.assertEqual(first["written"], 1)

        path = next((self.vault / "solutions" / "approved").glob("*.md"))
        before = path.read_bytes()
        text = before.decode()
        self.assertIn('trust: "governed_reusable_solution"', text)
        self.assertIn(digest, text)
        self.assertIn("Verify applicability and live state", text)
        self.assertNotIn("UsageCount", text)

        second = mod.sync_approved_solutions(
            vault=self.vault, policy_path=self.policy, rows=[source]
        )
        self.assertTrue(second["ok"])
        self.assertEqual(second["written"], 0)
        self.assertEqual(second["unchanged"], 1)
        self.assertEqual(path.read_bytes(), before)

    def test_semantic_drift_fails_closed_and_removes_stale_trusted_export(self):
        source = row()
        self._approve(source)
        self.assertTrue(mod.sync_approved_solutions(
            vault=self.vault, policy_path=self.policy, rows=[source]
        )["ok"])

        changed = row(title="Changed after review")
        result = mod.sync_approved_solutions(
            vault=self.vault, policy_path=self.policy, rows=[changed]
        )
        self.assertFalse(result["ok"])
        self.assertEqual(result["removed"], 1)
        self.assertIn("content drift", "\n".join(result["errors"]))
        self.assertEqual(
            list((self.vault / "solutions" / "approved").glob("*.md")), []
        )

    def test_generated_scope_has_one_owner_and_removes_unapproved_files(self):
        source = row()
        self._approve(source)
        approved_dir = self.vault / "solutions" / "approved"
        approved_dir.mkdir(parents=True)
        (approved_dir / "hand-authored.md").write_text("wrong directory owner", encoding="utf-8")

        result = mod.sync_approved_solutions(
            vault=self.vault, policy_path=self.policy, rows=[source]
        )
        self.assertTrue(result["ok"])
        self.assertFalse((approved_dir / "hand-authored.md").exists())
        self.assertEqual(len(list(approved_dir.glob("*.md"))), 1)

    def test_dry_run_reports_changes_without_mutating_scope(self):
        source = row()
        self._approve(source)
        approved_dir = self.vault / "solutions" / "approved"
        approved_dir.mkdir(parents=True)
        old = approved_dir / "old.md"
        old.write_text("keep during dry run", encoding="utf-8")

        result = mod.sync_approved_solutions(
            vault=self.vault,
            policy_path=self.policy,
            rows=[source],
            dry_run=True,
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["written"], 1)
        self.assertEqual(result["removed"], 1)
        self.assertTrue(old.exists())
        self.assertEqual(len(list(approved_dir.glob("*.md"))), 1)

    def test_policy_requires_governance_metadata_and_full_hash(self):
        self._write_policy([{"solution_id": "S-1", "content_sha256": "abc"}])
        result = mod.sync_approved_solutions(
            vault=self.vault, policy_path=self.policy, rows=[row()]
        )
        self.assertFalse(result["ok"])
        errors = "\n".join(result["errors"])
        self.assertIn("64 lowercase hex", errors)
        self.assertIn("approved_by", errors)
        self.assertIn("review_evidence", errors)


if __name__ == "__main__":
    unittest.main(verbosity=2)
