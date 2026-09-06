#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parent / "build_l2_historical_retrieval_eval.py"
_spec = importlib.util.spec_from_file_location("build_l2_historical_retrieval_eval_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


def session_text(run_id: str, ticket_id: str, user: str) -> str:
    return (
        "---\n"
        f'run_id: "{run_id}"\n'
        f'ticket_id: "{ticket_id}"\n'
        'trust: "unverified_episodic"\n'
        "---\n\n"
        "# User\n\n" + user + "\n\n# Assistant\n\nWorking.\n"
    )


def case_text(case_id: str, run_id: str, ticket_id: str, outcome: str) -> str:
    return (
        "---\n"
        f'case_id: "{case_id}"\n'
        f'run_id: "{run_id}"\n'
        f'ticket_id: "{ticket_id}"\n'
        f'outcome: "{outcome}"\n'
        "---\n\n# Historical case\n"
    )


class HistoricalEvalBuilderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name)
        (self.vault / "sessions/2026-09-06/l2-investigator/s1").mkdir(parents=True)
        for bucket in ("approved", "rejected", "reopened"):
            (self.vault / "cases" / bucket).mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def test_builds_case_from_earliest_correlated_session(self):
        sdir = self.vault / "sessions/2026-09-06/l2-investigator/s1"
        (sdir / "001.md").write_text(session_text(
            "RUN-1", "TICKET-1", "SAP posting is stuck and no material document has been generated for the work order."
        ), encoding="utf-8")
        (sdir / "002.md").write_text(session_text(
            "RUN-1", "TICKET-1", "Later follow-up text should not become the replay query."
        ), encoding="utf-8")
        expected = self.vault / "cases/approved/ticket-1-case-a.md"
        expected.write_text(case_text("case-a", "RUN-1", "TICKET-1", "reviewer_approved_and_published"), encoding="utf-8")

        cases = mod.build_cases(self.vault)
        self.assertEqual(len(cases), 1)
        case = cases[0]
        self.assertEqual(case["scope"], "approved_cases")
        self.assertEqual(case["expected_any"], [expected.name])
        self.assertIn("SAP posting is stuck", case["query"])
        self.assertNotIn("Later follow-up", case["query"])
        self.assertEqual(case["metadata"]["run_id"], "RUN-1")

    def test_ignores_outcome_without_correlated_session(self):
        (self.vault / "cases/rejected/r.md").write_text(
            case_text("r1", "RUN-MISSING", "T2", "reviewer_rejected"), encoding="utf-8"
        )
        self.assertEqual(mod.build_cases(self.vault), [])

    def test_uses_bucket_specific_scope(self):
        sdir = self.vault / "sessions/2026-09-06/l2-investigator/s1"
        for i, bucket in enumerate(("approved", "rejected", "reopened"), 1):
            run = f"R{i}"
            (sdir / f"{i}.md").write_text(session_text(
                run, f"T{i}", f"Ticket symptom number {i} has enough context to form a retrieval replay query."
            ), encoding="utf-8")
            (self.vault / f"cases/{bucket}/{i}.md").write_text(
                case_text(f"c{i}", run, f"T{i}", bucket), encoding="utf-8"
            )
        scopes = {case["scope"] for case in mod.build_cases(self.vault)}
        self.assertEqual(scopes, {"approved_cases", "rejected_cases", "reopened_cases"})

    def test_write_cases_is_jsonl(self):
        cases = [{"id": "x", "query": "a useful historical support query", "scope": "approved_cases", "expected_any": ["x.md"]}]
        path = mod.write_cases(self.vault, Path("eval/cases.jsonl"), cases)
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(rows, cases)


if __name__ == "__main__":
    unittest.main(verbosity=2)
