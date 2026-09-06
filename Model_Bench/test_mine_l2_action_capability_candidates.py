#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parent / "mine_l2_action_capability_candidates.py"
_spec = importlib.util.spec_from_file_location("mine_l2_action_capability_candidates_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


def approved_case(*, case_id: str, ticket_id: str, run_id: str, response_type: str,
                  action: str) -> str:
    return (
        "---\n"
        f'case_id: "{case_id}"\n'
        f'ticket_id: "{ticket_id}"\n'
        f'run_id: "{run_id}"\n'
        f'response_type: "{response_type}"\n'
        "---\n\n"
        "## Resolution / proposed action\n\n" + action + "\n\n"
        "## Outcome evidence\n\nReviewer approved and publisher postconditions succeeded.\n"
    )


class CapabilityCandidateMiningTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name)
        (self.vault / "cases/approved").mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def _add(self, action: str, ticket: str, index: int):
        (self.vault / f"cases/approved/{index}.md").write_text(approved_case(
            case_id=f"c{index}", ticket_id=ticket, run_id=f"R{index}",
            response_type="NEEDS_HUMAN_ACTION", action=action,
        ), encoding="utf-8")

    def test_two_distinct_human_action_tickets_create_backlog_candidate(self):
        action = "Retry the SAP posting through the supported posting retry path after confirming the transaction remains pending."
        self._add(action, "T1", 1); self._add(action, "T2", 2)
        counts = mod.mine_capability_candidates(self.vault)
        self.assertEqual(counts["created"], 1)
        candidate = json.loads(next((self.vault / "actions/candidates").glob("*.json")).read_text(encoding="utf-8"))
        self.assertEqual(candidate["trust"], "unverified_capability_candidate")
        self.assertEqual(candidate["status"], "needs_executor_design")
        self.assertEqual(candidate["distinct_ticket_count"], 2)
        self.assertIsNone(candidate["design_requirements"]["execution"])
        self.assertIsNone(candidate["design_requirements"]["parameter_schema"])

    def test_single_ticket_does_not_create_candidate(self):
        (self.vault / "cases/approved/1.md").write_text(approved_case(
            case_id="c1", ticket_id="T1", run_id="R1", response_type="NEEDS_HUMAN_ACTION",
            action="Perform the supported corrective action after validating the live target state.",
        ), encoding="utf-8")
        counts = mod.mine_capability_candidates(self.vault)
        self.assertEqual(counts["eligible_groups"], 0)
        self.assertFalse((self.vault / "actions/candidates").exists())

    def test_resolution_cases_are_not_capability_backlog(self):
        action = "No human action is required because the issue is already resolved."
        for i, ticket in enumerate(("T1", "T2"), 1):
            (self.vault / f"cases/approved/{i}.md").write_text(approved_case(
                case_id=f"c{i}", ticket_id=ticket, run_id=f"R{i}", response_type="RESOLUTION", action=action,
            ), encoding="utf-8")
        counts = mod.mine_capability_candidates(self.vault)
        self.assertEqual(counts["created"], 0)

    def test_third_observation_updates_same_candidate_instead_of_duplicate(self):
        action = "Reset the supported integration state through the official operator procedure after verifying all preconditions."
        self._add(action, "T1", 1); self._add(action, "T2", 2)
        first = mod.mine_capability_candidates(self.vault)
        self.assertEqual(first["created"], 1)
        self._add(action, "T3", 3)
        second = mod.mine_capability_candidates(self.vault)
        self.assertEqual(second["updated"], 1)
        files = list((self.vault / "actions/candidates").glob("*.json"))
        self.assertEqual(len(files), 1)
        self.assertEqual(json.loads(files[0].read_text(encoding="utf-8"))["distinct_ticket_count"], 3)

    def test_repeated_learning_cycle_does_not_erase_curator_owned_design_state(self):
        action = "Retry the supported integration transaction after verifying the failed live state and duplicate guards."
        self._add(action, "T1", 1); self._add(action, "T2", 2)
        mod.mine_capability_candidates(self.vault)
        path = next((self.vault / "actions/candidates").glob("*.json"))
        governed = json.loads(path.read_text(encoding="utf-8"))
        governed["status"] = "contract_drafted"
        governed["design_requirements"] = {
            "capability_id": "xbatch.integration.retry",
            "risk": "low",
            "parameter_schema": {"type": "object"},
            "preconditions": ["failed live state"],
            "execution": {"type": "stored_procedure", "target": "dbo.RealRetryUsp"},
            "idempotency": {"key": "transaction_id"},
            "verification": ["terminal success"],
            "rollback": {"not_required": True, "justification": "idempotent retry"},
            "required_evidence": [{"id": "failed_tx"}],
            "approval_policy": {"requires_human_approval": True},
        }
        governed["draft_contract"] = {"id": "xbatch.integration.retry", "mode": "shadow"}
        governed["governance_history"] = [{"event": "contract_drafted", "reviewed_by": "operator"}]
        path.write_text(json.dumps(governed, indent=2), encoding="utf-8")

        # New evidence arrives after governance work has already started.
        self._add(action, "T3", 3)
        result = mod.mine_capability_candidates(self.vault)
        self.assertEqual(result["updated"], 1)
        after = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(after["distinct_ticket_count"], 3)
        self.assertEqual(after["status"], "contract_drafted")
        self.assertEqual(after["design_requirements"], governed["design_requirements"])
        self.assertEqual(after["draft_contract"], governed["draft_contract"])
        self.assertEqual(after["governance_history"], governed["governance_history"])

    def test_unchanged_rerun_leaves_candidate_byte_stable(self):
        action = "Perform the supported retry only after verifying the current failure and duplicate-prevention state."
        self._add(action, "T1", 1); self._add(action, "T2", 2)
        mod.mine_capability_candidates(self.vault)
        path = next((self.vault / "actions/candidates").glob("*.json"))
        before = path.read_bytes()
        result = mod.mine_capability_candidates(self.vault)
        self.assertEqual(result["unchanged"], 1)
        self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
