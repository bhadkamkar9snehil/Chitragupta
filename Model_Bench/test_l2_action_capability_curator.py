#!/usr/bin/env python3
"""Contract tests for governed capability-candidate promotion."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODULE = ROOT / "l2_action_capability_curator.py"
_spec = importlib.util.spec_from_file_location("l2_action_capability_curator_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


BASE_REGISTRY = {
    "schema_version": 1,
    "global_mode": "observe",
    "capability_contract": {
        "required_fields": ["id", "description", "risk", "mode", "parameter_schema", "preconditions", "execution", "idempotency", "verification", "rollback", "required_evidence", "approval_policy"],
        "allowed_modes": ["observe", "recommend", "shadow", "supervised", "autonomous"],
        "allowed_risk": ["low", "medium", "high", "critical"],
    },
    "capabilities": [],
}


def candidate():
    return {
        "schema_version": 1,
        "kind": "xstudio_action_capability_candidate",
        "candidate_id": "abc123",
        "trust": "unverified_capability_candidate",
        "status": "needs_executor_design",
        "distinct_ticket_count": 2,
        "representative_human_action": "Retry the failed posting through the supported service path.",
    }


def contract():
    return {
        "id": "xbatch.sap.retry_posting",
        "description": "Retry one failed SAP posting through the supported deterministic path.",
        "risk": "low",
        "mode": "shadow",
        "parameter_schema": {
            "type": "object",
            "properties": {"transaction_id": {"type": "string", "minLength": 1, "maxLength": 100}},
            "required": ["transaction_id"],
            "additionalProperties": False,
        },
        "preconditions": ["live transaction is failed and retryable"],
        "execution": {"type": "stored_procedure", "target": "dbo.XMES_SAP_Retry_Posting_Usp"},
        "idempotency": {"key": "transaction_id", "rule": "do not submit while a successful posting exists"},
        "verification": ["re-read transaction and require successful terminal state"],
        "rollback": {"strategy": "none", "not_required": True, "justification": "retry is idempotent and verification-gated"},
        "required_evidence": [{"id": "failed_transaction", "description": "Current failed transaction row."}],
        "approval_policy": {"requires_human_approval": True},
    }


class CapabilityCuratorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.vault = self.root / "vault"
        self.candidates = self.vault / "actions" / "candidates"
        self.candidates.mkdir(parents=True)
        self.candidate_path = self.candidates / "abc123.json"
        self.candidate_path.write_text(json.dumps(candidate()), encoding="utf-8")
        self.registry = self.root / "registry.json"
        self.registry.write_text(json.dumps(BASE_REGISTRY), encoding="utf-8")
        self.contract = self.root / "contract.json"
        self.contract.write_text(json.dumps(contract()), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_invalid_transition_is_rejected(self):
        data = json.loads(self.candidate_path.read_text())
        with self.assertRaisesRegex(ValueError, "invalid capability-candidate transition"):
            mod._transition(data, "shadow_ready", reviewed_by="operator", evidence="no design yet")

    def test_contract_must_be_registry_valid(self):
        mod.start_research(self.candidate_path, reviewed_by="operator", evidence="research opened")
        broken = contract(); broken["parameter_schema"]["additionalProperties"] = True
        self.contract.write_text(json.dumps(broken), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "failed registry validation"):
            mod.apply_contract(self.candidate_path, self.contract, self.registry,
                               reviewed_by="operator", evidence="design review")

    def test_shadow_ready_requires_concrete_executor_contract(self):
        mod.start_research(self.candidate_path, reviewed_by="operator", evidence="research opened")
        weak = contract(); weak["execution"] = {"type": "none", "target": ""}
        self.contract.write_text(json.dumps(weak), encoding="utf-8")
        mod.apply_contract(self.candidate_path, self.contract, self.registry,
                           reviewed_by="operator", evidence="drafted planning-only contract")
        with self.assertRaisesRegex(ValueError, "not shadow-ready"):
            mod.mark_shadow_ready(self.candidate_path, self.registry,
                                  reviewed_by="operator", evidence="executor not verified")

    def test_promotion_adds_shadow_capability_without_raising_global_mode(self):
        mod.start_research(self.candidate_path, reviewed_by="operator", evidence="supported SP identified")
        mod.apply_contract(self.candidate_path, self.contract, self.registry,
                           reviewed_by="operator", evidence="contract reviewed")
        mod.mark_shadow_ready(self.candidate_path, self.registry,
                              reviewed_by="operator", evidence="preconditions and verification confirmed")
        result = mod.promote_to_registry(self.candidate_path, self.registry,
                                         reviewed_by="operator", evidence="approved for registry inclusion")
        registry = json.loads(self.registry.read_text())
        self.assertEqual(registry["global_mode"], "observe")
        self.assertEqual(len(registry["capabilities"]), 1)
        self.assertEqual(registry["capabilities"][0]["mode"], "shadow")
        self.assertEqual(result["status"], "registry_entry")
        self.assertFalse(result["registry_entry"]["execution_authorized"])

    def test_existing_different_registry_contract_is_not_overwritten(self):
        existing = copy.deepcopy(BASE_REGISTRY)
        other = contract(); other["description"] = "Different reviewed contract"
        existing["capabilities"] = [other]
        self.registry.write_text(json.dumps(existing), encoding="utf-8")
        mod.start_research(self.candidate_path, reviewed_by="operator", evidence="research")
        mod.apply_contract(self.candidate_path, self.contract, self.registry,
                           reviewed_by="operator", evidence="draft")
        mod.mark_shadow_ready(self.candidate_path, self.registry,
                              reviewed_by="operator", evidence="ready")
        with self.assertRaisesRegex(ValueError, "different capability"):
            mod.promote_to_registry(self.candidate_path, self.registry,
                                    reviewed_by="operator", evidence="promote")


if __name__ == "__main__":
    unittest.main(verbosity=2)
