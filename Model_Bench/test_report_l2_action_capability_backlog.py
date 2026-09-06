#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parent / "report_l2_action_capability_backlog.py"
_spec = importlib.util.spec_from_file_location("report_l2_action_capability_backlog_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


class BacklogReportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name)
        self.root = self.vault / "actions" / "candidates"
        self.root.mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def _candidate(self, name: str, tickets: int, observations: int, *, status="needs_executor_design", risk="unclassified"):
        data = {
            "schema_version": 1,
            "kind": "xstudio_action_capability_candidate",
            "candidate_id": name,
            "status": status,
            "distinct_ticket_count": tickets,
            "observation_count": observations,
            "representative_human_action": f"human action {name}",
            "normalized_action": f"normalized {name}",
            "design_requirements": {"risk": risk, "capability_id": None},
            "source_cases": [f"case-{i}" for i in range(observations)],
            "ticket_ids": [f"T{i}" for i in range(tickets)],
            "first_seen_at": "2026-09-01T00:00:00+00:00",
        }
        (self.root / f"{name}.json").write_text(json.dumps(data), encoding="utf-8")

    def test_ranking_prefers_distinct_reviewed_tickets_then_observations(self):
        self._candidate("two-many", 2, 8)
        self._candidate("three-few", 3, 3)
        self._candidate("three-more", 3, 5)
        rows = mod.backlog(self.vault)
        self.assertEqual([r["candidate_id"] for r in rows], ["three-more", "three-few", "two-many"])
        self.assertEqual([r["rank"] for r in rows], [1, 2, 3])

    def test_terminal_candidates_are_hidden_by_default(self):
        self._candidate("active", 2, 2)
        self._candidate("done", 10, 10, status="registry_entry")
        self.assertEqual([r["candidate_id"] for r in mod.backlog(self.vault)], ["active"])
        self.assertEqual(len(mod.backlog(self.vault, include_terminal=True)), 2)

    def test_report_does_not_infer_low_risk_from_repetition(self):
        self._candidate("repeated", 20, 20)
        row = mod.backlog(self.vault)[0]
        self.assertEqual(row["risk"], "unclassified")
        self.assertIn("inspect the real side effect", row["selection_note"])

    def test_non_candidate_json_is_ignored(self):
        (self.root / "other.json").write_text(json.dumps({"kind": "something_else"}), encoding="utf-8")
        self.assertEqual(mod.backlog(self.vault), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
