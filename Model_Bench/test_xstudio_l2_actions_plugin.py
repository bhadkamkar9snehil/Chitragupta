#!/usr/bin/env python3
"""Contract tests for the non-executing xstudio-l2-actions planning plugin."""
from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PLUGIN = Path(__file__).resolve().parent / "xstudio_l2_actions_plugin" / "__init__.py"


class FakeContext:
    def __init__(self):
        self.tools = {}
        self.hooks = {}

    def register_tool(self, *, name, toolset, schema, handler, description=""):
        self.tools[name] = {"toolset": toolset, "schema": schema, "handler": handler, "description": description}

    def register_hook(self, name, callback):
        self.hooks[name] = callback


class ActionPluginTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.vault = root / "vault"
        self.registry = root / "xstudio_action_capabilities.json"
        self.registry.write_text(json.dumps({
            "schema_version": 1,
            "global_mode": "shadow",
            "capability_contract": {
                "required_fields": [
                    "id", "description", "risk", "mode", "parameter_schema",
                    "preconditions", "execution", "idempotency", "verification",
                    "rollback", "required_evidence", "approval_policy"
                ],
                "allowed_modes": ["observe", "recommend", "shadow", "supervised", "autonomous"],
                "allowed_risk": ["low", "medium", "high", "critical"]
            },
            "capabilities": [{
                "id": "xbatch.test.shadow_action",
                "description": "Synthetic shadow-only action used by contract tests.",
                "risk": "low",
                "mode": "shadow",
                "parameter_schema": {
                    "type": "object",
                    "properties": {
                        "batch_no": {"type": "string", "minLength": 1},
                        "retry_count": {"type": "integer", "minimum": 1, "maximum": 3}
                    },
                    "required": ["batch_no"],
                    "additionalProperties": False
                },
                "preconditions": ["live row proves the target condition"],
                "execution": {"type": "none", "target": ""},
                "idempotency": {},
                "verification": ["re-read the live row"],
                "rollback": {},
                "required_evidence": [{
                    "id": "live_target_row",
                    "description": "Current live SQL row proving the target state."
                }],
                "approval_policy": {"requires_human_approval": True}
            }]
        }, indent=2), encoding="utf-8")

        self.env = mock.patch.dict(os.environ, {
            "CHITRAGUPTA_L2_LEARNING_VAULT": str(self.vault),
            "CHITRAGUPTA_XSTUDIO_ACTION_REGISTRY": str(self.registry),
        }, clear=False)
        self.env.start()

        spec = importlib.util.spec_from_file_location("xstudio_l2_actions_plugin_tested", PLUGIN)
        self.mod = importlib.util.module_from_spec(spec)
        assert spec.loader
        spec.loader.exec_module(self.mod)

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def _good_plan(self):
        return {
            "operation": "plan",
            "capability_id": "xbatch.test.shadow_action",
            "parameters": {"batch_no": "B99503", "retry_count": 1},
            "evidence": [{
                "id": "live_target_row",
                "source": "xstudio_l2",
                "reference": "XStudio_Xbatch.dbo.SomeView batch=B99503",
                "claim": "Current row is in the exact state required by the capability."
            }],
            "rationale": "Root cause is established and the registered shadow action matches.",
            "run_id": "run-1",
            "ticket_id": "ticket-1",
        }

    def test_registers_one_non_executing_tool_and_no_hooks(self):
        ctx = FakeContext()
        self.mod.register(ctx)
        self.assertEqual(set(ctx.tools), {"l2_action"})
        self.assertEqual(ctx.tools["l2_action"]["toolset"], "l2_actions")
        enums = ctx.tools["l2_action"]["schema"]["parameters"]["properties"]["operation"]["enum"]
        self.assertNotIn("execute", enums)
        self.assertEqual(ctx.hooks, {})

    def test_list_and_describe_expose_effective_mode_without_execution(self):
        listed = json.loads(self.mod._handler({"operation": "list"}))
        self.assertTrue(listed["ok"])
        self.assertFalse(listed["execution_tool_available"])
        self.assertEqual(listed["capabilities"][0]["effective_mode"], "shadow")
        described = json.loads(self.mod._handler({"operation": "describe", "capability_id": "xbatch.test.shadow_action"}))
        self.assertTrue(described["ok"])
        self.assertEqual(described["capability"]["risk"], "low")
        self.assertFalse(described["execution_tool_available"])

    def test_plan_requires_declared_evidence_and_rejects_extra_parameters(self):
        missing = self._good_plan()
        missing["evidence"] = []
        result = json.loads(self.mod._handler(missing))
        self.assertFalse(result["ok"])
        self.assertIn("required evidence not supplied", " ".join(result["validation_errors"]))
        self.assertFalse(result["execution_authorized"])
        extra = self._good_plan()
        extra["parameters"]["surprise"] = "not allowed"
        result = json.loads(self.mod._handler(extra))
        self.assertFalse(result["ok"])
        self.assertIn("unexpected properties", " ".join(result["validation_errors"]))

    def test_plan_is_durable_deterministic_and_still_non_executing(self):
        request = self._good_plan()
        first = json.loads(self.mod._handler(request, session_id="s1", profile="l2-investigator-primary"))
        self.assertTrue(first["ok"])
        self.assertEqual(first["status"], "created")
        self.assertFalse(first["execution_authorized"])
        plan = first["plan"]
        self.assertEqual(len(plan["plan_id"]), 32)
        self.assertEqual(plan["trust"], "validated_shadow_plan")
        self.assertEqual(plan["context"]["run_id"], "run-1")
        self.assertFalse(plan["execution_authorized"])
        self.assertTrue(Path(first["path"]).exists())
        second = json.loads(self.mod._handler(request, session_id="s2"))
        self.assertTrue(second["ok"])
        self.assertEqual(second["status"], "existing")
        self.assertEqual(second["plan"]["plan_id"], plan["plan_id"])
        self.assertEqual(len(list((self.vault / "actions" / "plans").glob("*.json"))), 1)

    def test_validate_plan_detects_capability_drift(self):
        first = json.loads(self.mod._handler(self._good_plan()))
        plan_id = first["plan"]["plan_id"]
        valid = json.loads(self.mod._handler({"operation": "validate_plan", "plan_id": plan_id}))
        self.assertTrue(valid["ok"])
        self.assertFalse(valid["execution_authorized"])
        data = json.loads(self.registry.read_text(encoding="utf-8"))
        data["capabilities"][0]["description"] = "changed safety contract"
        self.registry.write_text(json.dumps(data), encoding="utf-8")
        stale = json.loads(self.mod._handler({"operation": "validate_plan", "plan_id": plan_id}))
        self.assertFalse(stale["ok"])
        self.assertIn("capability changed", " ".join(stale["validation_errors"]))

    def test_global_observe_is_hard_planning_gate(self):
        data = json.loads(self.registry.read_text(encoding="utf-8"))
        data["global_mode"] = "observe"
        self.registry.write_text(json.dumps(data), encoding="utf-8")
        result = json.loads(self.mod._handler(self._good_plan()))
        self.assertFalse(result["ok"])
        self.assertIn("not active", result["error"])
        self.assertFalse(result["execution_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
