#!/usr/bin/env python3
"""Contract tests for outcome-conditioned L2 case materialization."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

MODULE = Path(__file__).resolve().parent / "sync_l2_outcomes.py"
_spec = importlib.util.spec_from_file_location("sync_l2_outcomes_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


def reviewer_task(task_id: str, *, status: str, response_type: str = "RESOLUTION") -> dict:
    proposal = {
        "run_id": "run-1", "ticket_id": "ticket-1", "response_type": response_type,
        "problem_summary": "SAP posting failed for batch B99503.",
        "findings": "Live error row confirmed current failure state.",
        "root_cause": "Synthetic test root cause.",
        "resolution": "Synthetic proposed remediation.",
        "reply_text": "Synthetic reviewed reply.",
    }
    return {
        "id": task_id, "status": status, "assignee": "l2-reviewer-primary",
        "body": (
            "run_id: run-1\n"
            "ticket_id: ticket-1\n"
            "ticket_no: Ticket_424\n"
            "review_cycle: 0\n"
            "investigation_task_id: t_investigator\n"
            "pipeline_stage: review\n"
            "proposal_json: " + json.dumps(proposal, separators=(",", ":")) + "\n"
        ),
    }


def published_row(ticket_status: str = "Closed") -> dict:
    return {
        "ID": "run-1", "TicketID": "ticket-1", "ProcessStatus": "COMPLETED",
        "ResponseType": "RESOLUTION", "ReplyText": "Synthetic reviewed reply.",
        "TicketStatus": ticket_status, "AskStatus": None,
        "SupportExecutiveRemarks": "Synthetic reviewed reply.",
    }


class OutcomeSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name) / "vault"

    def tearDown(self):
        self.tmp.cleanup()

    def test_rejected_review_becomes_counterexample_once(self):
        task = reviewer_task("t_review_reject", status="blocked")
        with mock.patch.object(mod, "reviewer_block_reason", return_value="Reviewer found missing live proof."):
            first = mod.sync_outcomes(vault=self.vault, tasks=[task], args=object())
            second = mod.sync_outcomes(vault=self.vault, tasks=[task], args=object())
        self.assertEqual(first["rejected_recorded"], 1)
        self.assertEqual(second["rejected_recorded"], 0)
        files = list((self.vault / "cases" / "rejected").glob("*.md"))
        self.assertEqual(len(files), 1)
        text = files[0].read_text(encoding="utf-8")
        self.assertIn('trust: "reviewed_negative_example"', text)
        self.assertIn("Reviewer found missing live proof.", text)
        self.assertIn("not proof that every individual statement", text)

    def test_approved_case_requires_publisher_postconditions(self):
        task = reviewer_task("t_review_done", status="done")
        with mock.patch.object(mod, "_query_published_state", return_value=[]):
            result = mod.sync_outcomes(vault=self.vault, tasks=[task], args=object())
        self.assertEqual(result["approved_recorded"], 0)
        self.assertEqual(list((self.vault / "cases" / "approved").glob("*.md")), [])

    def test_approved_published_case_is_recorded_once(self):
        task = reviewer_task("t_review_done", status="done")
        with mock.patch.object(mod, "_query_published_state", return_value=[published_row()]):
            first = mod.sync_outcomes(vault=self.vault, tasks=[task], args=object())
            second = mod.sync_outcomes(vault=self.vault, tasks=[task], args=object())
        self.assertEqual(first["approved_recorded"], 1)
        self.assertEqual(second["approved_recorded"], 0)
        files = list((self.vault / "cases" / "approved").glob("*.md"))
        self.assertEqual(len(files), 1)
        text = files[0].read_text(encoding="utf-8")
        self.assertIn('trust: "reviewed_published_historical_case"', text)
        self.assertIn("deterministic publisher", text)
        self.assertIn('"TicketStatus": "Closed"', text)

    def test_resolution_terminal_status_drift_creates_reopen_signal(self):
        task = reviewer_task("t_review_done", status="done")
        with mock.patch.object(mod, "_query_published_state", return_value=[published_row("Closed")]):
            first = mod.sync_outcomes(vault=self.vault, tasks=[task], args=object())
        self.assertEqual(first["approved_recorded"], 1)
        manifest_path = self.vault / mod.MANIFEST_NAME
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["review_tasks"]["t_review_done"]["last_checked_at"] = (
            datetime.now(timezone.utc) - timedelta(hours=mod.REOPEN_RECHECK_HOURS + 2)
        ).isoformat()
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        with mock.patch.object(mod, "_query_published_state", side_effect=[[published_row("Enter")], [published_row("Enter")]]):
            second = mod.sync_outcomes(vault=self.vault, tasks=[task], args=object())
        self.assertEqual(second["approved_recorded"], 0)
        self.assertEqual(second["reopened_recorded"], 1)
        files = list((self.vault / "cases" / "reopened").glob("*.md"))
        self.assertEqual(len(files), 1)
        text = files[0].read_text(encoding="utf-8")
        self.assertIn('trust: "observed_resolution_regression"', text)
        self.assertIn("'Closed' -> 'Enter'", text)

    def test_dry_run_does_not_write_manifest_or_cases(self):
        task = reviewer_task("t_review_done", status="done")
        with mock.patch.object(mod, "_query_published_state", return_value=[published_row()]):
            result = mod.sync_outcomes(vault=self.vault, tasks=[task], args=object(), dry_run=True)
        self.assertEqual(result["approved_recorded"], 1)
        self.assertFalse((self.vault / mod.MANIFEST_NAME).exists())
        self.assertEqual(list((self.vault / "cases" / "approved").glob("*.md")), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
