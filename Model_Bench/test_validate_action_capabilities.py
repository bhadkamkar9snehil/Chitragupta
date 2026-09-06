#!/usr/bin/env python3
"""Contract tests for corrective-action capability policy validation."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parent / "validate_action_capabilities.py"
_spec = importlib.util.spec_from_file_location("validate_action_capabilities_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


BASE = {
    "schema_version": 1,
    "global_mode": "shadow",
    "capability_contract": {
        "required_fields": ["id", "description", "risk", "mode", "parameter_schema", "preconditions", "execution", "idempotency", "verification", "rollback", "required_evidence", "approval_policy"],
        "allowed_modes": ["observe", "recommend", "shadow", "supervised", "autonomous"],
        "allowed_risk": ["low", "medium", "high", "critical"],
    },
    "capabilities": [],
}


def shadow_capability():
    return {
        "id": "xbatch.test.shadow",
        "description": "Synthetic shadow capability.",
        "risk": "low",
        "mode": "shadow",
        "parameter_schema": {"type": "object", "properties": {"batch_no": {"type": "string", "minLength": 1}}, "required": ["batch_no"], "additionalProperties": False},
        "preconditions": ["live target row exists"],
        "execution": {"type": "none", "target": ""},
        "idempotency": {},
        "verification": ["re-read live target row"],
        "rollback": {},
        "required_evidence": [{"id": "live_target", "description": "Current target row."}],
        "approval_policy": {"requires_human_approval": True},
    }


class RegistryValidationTests(unittest.TestCase):
    def validate(self, data):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return mod.validate(path)

    def test_empty_observe_registry_is_valid(self):
        data = copy.deepcopy(BASE); data["global_mode"] = "observe"
        self.assertEqual(self.validate(data), [])

    def test_shadow_capability_may_have_no_execution_target(self):
        data = copy.deepcopy(BASE); data["capabilities"] = [shadow_capability()]
        self.assertEqual(self.validate(data), [])

    def test_supervised_requires_real_executor_and_human_approval(self):
        cap = shadow_capability(); cap["mode"] = "supervised"; cap["execution"] = {"type": "stored_procedure", "target": "dbo.SafeProcedure"}; cap["idempotency"] = {"key": "batch_no"}; cap["approval_policy"] = {"requires_human_approval": False}
        data = copy.deepcopy(BASE); data["global_mode"] = "supervised"; data["capabilities"] = [cap]
        errors = self.validate(data)
        self.assertTrue(any("requires_human_approval=true" in e for e in errors))

    def test_autonomous_rejects_critical_and_requires_promotion_and_rollback(self):
        cap = shadow_capability(); cap["mode"] = "autonomous"; cap["risk"] = "critical"; cap["execution"] = {"type": "api", "target": "internal-safe-endpoint"}; cap["idempotency"] = {"key": "batch_no"}; cap["approval_policy"] = {"allows_autonomous": True}; cap["rollback"] = {}
        data = copy.deepcopy(BASE); data["global_mode"] = "autonomous"; data["capabilities"] = [cap]
        errors = "\n".join(self.validate(data))
        self.assertIn("critical-risk capability cannot be autonomous", errors)
        self.assertIn("requires rollback/compensation", errors)
        self.assertIn("requires non-empty promotion_evidence", errors)

    def test_parameter_schema_rejects_open_ended_extra_properties(self):
        cap = shadow_capability(); cap["parameter_schema"]["additionalProperties"] = True
        data = copy.deepcopy(BASE); data["capabilities"] = [cap]
        self.assertTrue(any("additionalProperties must be false" in e for e in self.validate(data)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
