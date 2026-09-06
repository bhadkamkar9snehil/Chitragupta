#!/usr/bin/env python3
"""Contract tests for the cross-cutting L2 identity guard."""
from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PLUGIN = Path(__file__).resolve().parent / "xstudio_l2_identity_plugin" / "__init__.py"
_spec = importlib.util.spec_from_file_location("xstudio_l2_identity_plugin_tested", PLUGIN)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


class IdentityGuardTests(unittest.TestCase):
    def setUp(self):
        with mod._lock:
            mod._context_cache.clear()

    @staticmethod
    def _show_payload(run_id="RUN-1", ticket_id="TICKET-1"):
        return json.dumps({
            "task": {
                "id": "t_abcdef12",
                "body": (
                    f"run_id: {run_id}\n"
                    f"ticket_id: {ticket_id}\n"
                    "ticket_no: HD-123\n"
                    "pipeline_stage: investigation\n"
                    "review_cycle: 0\n"
                ),
            }
        })

    def _mock_context(self, run_id="RUN-1", ticket_id="TICKET-1"):
        return mock.patch.object(
            mod.subprocess,
            "run",
            return_value=mock.Mock(returncode=0, stdout=self._show_payload(run_id, ticket_id), stderr=""),
        )

    def test_xstudio_query_identity_is_injected_by_harness(self):
        with self._mock_context():
            result = mod._pre_tool_call(
                "xstudio_l2",
                {"operation": "query", "database": "XStudio_Xbatch", "sql": "SELECT 1"},
                task_id="worker-session t_abcdef12",
            )
        self.assertEqual(result["action"], "modify")
        self.assertEqual(result["args"], {"run_id": "RUN-1"})

    def test_ticket_context_identity_is_injected_by_harness(self):
        with self._mock_context():
            result = mod._pre_tool_call(
                "xstudio_l2",
                {"operation": "get_ticket_context"},
                task_id="t_abcdef12",
            )
        self.assertEqual(result, {"action": "modify", "args": {"ticket_id": "TICKET-1"}})

    def test_conflicting_model_run_id_is_blocked(self):
        with self._mock_context():
            result = mod._pre_tool_call(
                "xstudio_l2",
                {"operation": "save_ledger", "run_id": "OTHER", "ledger": {"x": 1}},
                task_id="t_abcdef12",
            )
        self.assertEqual(result["action"], "block")
        self.assertIn("harness-owned", result["message"])
        self.assertIn("model supplied run_id='OTHER'", result["message"])
        self.assertIn("current Kanban task is bound to 'RUN-1'", result["message"])

    def test_matching_model_identity_is_replaced_with_bound_value(self):
        with self._mock_context():
            result = mod._pre_tool_call(
                "xstudio_l2",
                {"operation": "get_run_actions", "run_id": "RUN-1"},
                task_id="t_abcdef12",
            )
        self.assertEqual(result, {"action": "modify", "args": {"run_id": "RUN-1"}})

    def test_pure_schema_discovery_does_not_require_ticket_identity(self):
        result = mod._pre_tool_call(
            "xstudio_l2",
            {"operation": "find_objects", "database": "XStudio_Xbatch", "search": "SAP"},
            task_id="not-a-kanban-id",
        )
        self.assertIsNone(result)

    def test_action_plan_is_bound_to_both_run_and_ticket(self):
        with self._mock_context():
            result = mod._pre_tool_call(
                "l2_action",
                {"operation": "plan", "capability_id": "xbatch.test.shadow", "parameters": {}, "evidence": []},
                task_id="t_abcdef12",
            )
        self.assertEqual(result["action"], "modify")
        self.assertEqual(result["args"], {"run_id": "RUN-1", "ticket_id": "TICKET-1"})

    def test_action_plans_lookup_cannot_cross_ticket(self):
        with self._mock_context():
            result = mod._pre_tool_call(
                "l2_action",
                {"operation": "plans", "run_id": "RUN-1", "ticket_id": "OTHER"},
                task_id="t_abcdef12",
            )
        self.assertEqual(result["action"], "block")
        self.assertIn("model supplied ticket_id='OTHER'", result["message"])

    def test_validate_plan_blocks_cross_run_plan(self):
        with tempfile.TemporaryDirectory() as tmp, self._mock_context(), mock.patch.dict(
            os.environ, {"CHITRAGUPTA_L2_LEARNING_VAULT": tmp}, clear=False
        ):
            plan_id = "a" * 32
            plan_dir = Path(tmp) / "actions" / "plans"
            plan_dir.mkdir(parents=True)
            (plan_dir / f"{plan_id}.json").write_text(json.dumps({
                "plan_id": plan_id,
                "context": {"run_id": "OTHER", "ticket_id": "TICKET-1"},
            }), encoding="utf-8")
            result = mod._pre_tool_call(
                "l2_action", {"operation": "validate_plan", "plan_id": plan_id}, task_id="t_abcdef12"
            )
        self.assertEqual(result["action"], "block")
        self.assertIn("different L2 run", result["message"])

    def test_identity_sensitive_call_fails_closed_when_task_cannot_be_resolved(self):
        with mock.patch.object(mod.subprocess, "run", return_value=mock.Mock(returncode=1, stdout="", stderr="no task")):
            result = mod._pre_tool_call(
                "xstudio_l2", {"operation": "query", "database": "XStudio_Xbatch", "sql": "SELECT 1"},
                task_id="t_deadbeef",
            )
        self.assertEqual(result["action"], "block")
        self.assertIn("could not be resolved", result["message"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
