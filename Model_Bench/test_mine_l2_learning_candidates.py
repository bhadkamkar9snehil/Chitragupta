#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parent / "mine_l2_learning_candidates.py"
_spec = importlib.util.spec_from_file_location("mine_l2_learning_candidates_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


def case_text(*, case_id: str, trust: str, outcome: str, ticket_id: str, run_id: str,
              root_cause: str = "", detail: str = "") -> str:
    return (
        "---\n"
        f'case_id: "{case_id}"\n'
        f'trust: "{trust}"\n'
        f'outcome: "{outcome}"\n'
        f'ticket_id: "{ticket_id}"\n'
        f'run_id: "{run_id}"\n'
        "---\n\n"
        + (f"## Root cause\n\n{root_cause}\n\n" if root_cause else "")
        + f"## Outcome evidence\n\n{detail}\n"
    )


class CandidateMiningTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name)
        for bucket in ("approved", "rejected", "reopened"):
            (self.vault / "cases" / bucket).mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def test_rejection_and_reopen_become_unverified_candidates(self):
        (self.vault / "cases/rejected/r.md").write_text(case_text(
            case_id="r1", trust="reviewed_negative_example", outcome="reviewer_rejected",
            ticket_id="T1", run_id="R1", detail="Live row contradicted the proposal."), encoding="utf-8")
        (self.vault / "cases/reopened/o.md").write_text(case_text(
            case_id="o1", trust="reopen_signal", outcome="resolution_reopened_or_regressed",
            ticket_id="T2", run_id="R2", detail="Ticket left Closed after publication."), encoding="utf-8")
        counts = mod.mine_candidates(self.vault)
        self.assertEqual(counts["rejection_candidates"], 1)
        self.assertEqual(counts["reopen_candidates"], 1)
        files = list((self.vault / "candidates").glob("*.md"))
        self.assertEqual(len(files), 2)
        for path in files:
            text = path.read_text(encoding="utf-8")
            self.assertIn('trust: "unverified_candidate"', text)
            self.assertIn("Automatically mined", text)

    def test_repeated_approved_root_cause_requires_two_distinct_tickets(self):
        root = "SAP posting remained pending because the API transaction never reached a terminal success state."
        for i, ticket in enumerate(("T1001", "T2002"), 1):
            (self.vault / f"cases/approved/a{i}.md").write_text(case_text(
                case_id=f"a{i}", trust="reviewed_published_historical_case",
                outcome="reviewer_approved_and_published", ticket_id=ticket, run_id=f"R{i}",
                root_cause=root, detail="Publisher postconditions succeeded."), encoding="utf-8")
        counts = mod.mine_candidates(self.vault)
        self.assertEqual(counts["repeated_root_cause_candidates"], 1)
        text = next((self.vault / "candidates").glob("auto-repeated_root_cause-*.md")).read_text(encoding="utf-8")
        self.assertIn("multiple_reviewed_published_cases", text)

    def test_same_ticket_twice_does_not_create_repeated_root_cause_candidate(self):
        root = "The same durable root cause text long enough for deterministic grouping."
        for i in (1, 2):
            (self.vault / f"cases/approved/a{i}.md").write_text(case_text(
                case_id=f"a{i}", trust="reviewed_published_historical_case",
                outcome="reviewer_approved_and_published", ticket_id="T1", run_id=f"R{i}",
                root_cause=root, detail="ok"), encoding="utf-8")
        counts = mod.mine_candidates(self.vault)
        self.assertEqual(counts["repeated_root_cause_candidates"], 0)

    def test_mining_is_idempotent(self):
        (self.vault / "cases/rejected/r.md").write_text(case_text(
            case_id="r1", trust="reviewed_negative_example", outcome="reviewer_rejected",
            ticket_id="T1", run_id="R1", detail="Wrong table assumption."), encoding="utf-8")
        first = mod.mine_candidates(self.vault)
        second = mod.mine_candidates(self.vault)
        self.assertEqual(first["rejection_candidates"], 1)
        self.assertEqual(second["rejection_candidates"], 0)
        self.assertGreaterEqual(second["skipped"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
