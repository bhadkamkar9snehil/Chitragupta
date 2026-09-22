#!/usr/bin/env python3
"""Contract tests for xstudio-l2-learning without requiring a live GBrain."""
from __future__ import annotations

import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PLUGIN = Path(__file__).resolve().parent / "xstudio_l2_learning_plugin" / "__init__.py"
_spec = importlib.util.spec_from_file_location("xstudio_l2_learning_plugin_tested", PLUGIN)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


class FakeContext:
    def __init__(self):
        self.tools = {}
        self.hooks = {}
    def register_tool(self, *, name, toolset, schema, handler, description=""):
        self.tools[name] = {"toolset": toolset, "schema": schema, "handler": handler, "description": description}
    def register_hook(self, name, callback):
        self.hooks[name] = callback


class LearningPluginTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name) / "vault"
        self.env = mock.patch.dict(os.environ, {"CHITRAGUPTA_L2_LEARNING_VAULT": str(self.vault)}, clear=False)
        self.env.start()
    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def test_registers_explicit_tools_and_session_recorder_without_prefetch(self):
        ctx = FakeContext(); mod.register(ctx)
        self.assertEqual(set(ctx.tools), {"l2_recall", "l2_lesson"})
        self.assertEqual({x["toolset"] for x in ctx.tools.values()}, {"l2_learning"})
        self.assertIn("post_llm_call", ctx.hooks)
        self.assertNotIn("pre_llm_call", ctx.hooks)
        self.assertNotIn("on_turn_start", ctx.hooks)

    def test_session_recording_is_on_but_untrusted_and_redacted(self):
        mod._write_session_turn(user_message="Investigate ticket. password=hunter2",
                                assistant_response="Checked evidence. --password secret123",
                                session_id="sess-1", turn_id="turn-1", profile="l2-investigator-primary",
                                model="local-model", platform="cli")
        files = list((self.vault / "sessions").rglob("*.md"))
        self.assertEqual(len(files), 1)
        text = files[0].read_text(encoding="utf-8")
        self.assertIn('trust: "unverified_episodic"', text)
        self.assertNotIn("hunter2", text); self.assertNotIn("secret123", text)
        self.assertIn("[REDACTED]", text)

    def test_trusted_recall_uses_only_trusted_gbrain_sources(self):
        fake = {
            "ok": True,
            "source_ids": ["l2-knowledge", "l2-facts", "l2-solutions"],
            "requested_mode": "hybrid",
            "effective_mode": "hybrid",
            "results": [{"slug": "knowledge/foo", "chunk": "useful reference"}],
        }
        with mock.patch.object(mod, "_gbrain_available", return_value=True), \
             mock.patch.object(mod, "_gbrain_search", return_value=fake) as search:
            result = json.loads(mod._recall({"query": "posting stuck", "scope": "trusted"}))
        self.assertTrue(result["ok"])
        self.assertEqual(result["backend"], "gbrain")
        self.assertEqual(set(result["source_ids"]), {"l2-knowledge", "l2-facts", "l2-solutions"})
        self.assertNotIn("l2-sessions", result["source_ids"])
        self.assertFalse(result["automatic_prefetch"])
        self.assertTrue(result["live_verification_required"])
        search.assert_called_once_with("posting stuck", scope="trusted", mode="hybrid", limit=5)

    def test_case_scopes_preserve_outcome_semantics(self):
        cases = {
            "cases": "historical_outcome_evidence",
            "approved_cases": "reviewed_published_historical_case",
            "rejected_cases": "reviewed_negative_example",
            "reopened_cases": "observed_resolution_regression",
        }
        for scope, trust in cases.items():
            fake = {"ok": True, "source_ids": list(mod.SCOPE_SOURCES[scope]),
                    "requested_mode": "hybrid", "effective_mode": "hybrid", "results": []}
            with mock.patch.object(mod, "_gbrain_available", return_value=True), \
                 mock.patch.object(mod, "_gbrain_search", return_value=fake):
                result = json.loads(mod._recall({"query": "same issue", "scope": scope}))
            self.assertTrue(result["ok"], scope)
            self.assertEqual(result["trust"], trust, scope)
            self.assertTrue(result["live_verification_required"], scope)

    def test_session_recall_is_explicitly_unverified(self):
        fake = {"ok": True, "source_ids": ["l2-sessions"], "requested_mode": "hybrid",
                "effective_mode": "hybrid", "results": [{"chunk": "old hypothesis"}]}
        with mock.patch.object(mod, "_gbrain_available", return_value=True), \
             mock.patch.object(mod, "_gbrain_search", return_value=fake):
            result = json.loads(mod._recall({"query": "same failure before", "scope": "sessions"}))
        self.assertEqual(result["trust"], "unverified_episodic")
        self.assertIn("mistakes", result["warning"])

    def test_lesson_proposal_is_candidate_not_memory(self):
        result = json.loads(mod._propose_lesson({
            "kind": "failure_pattern",
            "summary": "Repeated wrapper retries after the same transport error waste context.",
            "evidence": "Observed on two independent tickets; reviewer confirmed transport itself was healthy.",
            "route": "hermes_runtime", "tags": "retry,budget",
        }, session_id="s1", task_id="t_123456"))
        self.assertTrue(result["ok"]); self.assertEqual(result["trust"], "unverified_candidate")
        path = Path(result["path"]); self.assertTrue(path.exists()); self.assertEqual(path.parent, self.vault / "candidates")
        self.assertIn("intentionally untrusted", path.read_text(encoding="utf-8"))

    def test_lesson_requires_evidence(self):
        result = json.loads(mod._propose_lesson({"summary": "maybe useful"}))
        self.assertFalse(result["ok"]); self.assertIn("evidence is required", result["error"])

    def test_layout_includes_outcome_action_backlog_and_replay_planes(self):
        vault = mod._ensure_layout()
        for rel in ("cases/approved", "cases/rejected", "cases/reopened", "actions/plans", "actions/candidates", "eval"):
            self.assertTrue((vault / rel).is_dir(), rel)

    def test_recall_fails_cleanly_when_gbrain_unavailable(self):
        with mock.patch.object(mod, "_gbrain_available", return_value=False):
            result = json.loads(mod._recall({"query": "x"}))
        self.assertFalse(result["ok"]); self.assertFalse(result["retry_same_call"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
