#!/usr/bin/env python3
"""Contract tests for xstudio-l2-learning.

These tests intentionally do not require zvec-grep. Subprocess/search behavior is
stubbed so the trust/scoping and session-recording contract can be validated on
any local checkout.
"""
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
        ctx = FakeContext()
        mod.register(ctx)
        self.assertEqual(set(ctx.tools), {"l2_recall", "l2_lesson"})
        self.assertEqual({x["toolset"] for x in ctx.tools.values()}, {"l2_learning"})
        self.assertIn("post_llm_call", ctx.hooks)
        self.assertNotIn("pre_llm_call", ctx.hooks)
        self.assertNotIn("on_turn_start", ctx.hooks)

    def test_session_recording_is_on_but_untrusted_and_redacted(self):
        mod._write_session_turn(
            user_message="Investigate ticket. password=hunter2",
            assistant_response="Checked evidence. --password secret123",
            session_id="sess-1",
            turn_id="turn-1",
            profile="l2-investigator-primary",
            model="local-model",
            platform="cli",
        )
        files = list((self.vault / "sessions").rglob("*.md"))
        self.assertEqual(len(files), 1)
        text = files[0].read_text(encoding="utf-8")
        self.assertIn('trust: "unverified_episodic"', text)
        self.assertIn("# User", text)
        self.assertIn("# Assistant", text)
        self.assertNotIn("hunter2", text)
        self.assertNotIn("secret123", text)
        self.assertIn("[REDACTED]", text)

    def test_trusted_recall_never_searches_sessions_or_candidates(self):
        calls = []

        def fake_run(args, timeout=mod.QUERY_TIMEOUT_SECONDS):
            calls.append(args)
            return 0, "knowledge/git/foo.md:1-3\nuseful reference", ""

        with mock.patch.object(mod.shutil, "which", return_value="/usr/bin/zg"), \
             mock.patch.object(mod, "_index_ready", return_value=True), \
             mock.patch.object(mod, "_run_zg", side_effect=fake_run):
            result = json.loads(mod._recall({"query": "posting stuck", "scope": "trusted"}))

        self.assertTrue(result["ok"])
        self.assertEqual(result["trust"], "mixed_trusted_reference")
        cmd = calls[0]
        joined = " ".join(cmd)
        self.assertIn("knowledge/**", joined)
        self.assertIn("facts/**", joined)
        self.assertIn("solutions/approved/**", joined)
        self.assertNotIn("sessions/**", joined)
        self.assertNotIn("candidates/**", joined)
        self.assertFalse(result["automatic_prefetch"])
        self.assertTrue(result["live_verification_required"])

    def test_session_recall_is_explicitly_unverified(self):
        with mock.patch.object(mod.shutil, "which", return_value="/usr/bin/zg"), \
             mock.patch.object(mod, "_index_ready", return_value=True), \
             mock.patch.object(mod, "_run_zg", return_value=(0, "sessions/2026/x.md:1-3\nold hypothesis", "")):
            result = json.loads(mod._recall({"query": "same failure before", "scope": "sessions"}))
        self.assertTrue(result["ok"])
        self.assertEqual(result["trust"], "unverified_episodic")
        self.assertIn("mistakes", result["warning"])

    def test_lesson_proposal_is_candidate_not_memory(self):
        result = json.loads(mod._propose_lesson({
            "kind": "failure_pattern",
            "summary": "Repeated wrapper retries after the same transport error waste context.",
            "evidence": "Observed on two independent tickets; reviewer confirmed transport itself was healthy.",
            "route": "hermes_runtime",
            "tags": "retry,budget",
        }, session_id="s1", task_id="t_123456"))
        self.assertTrue(result["ok"])
        self.assertEqual(result["trust"], "unverified_candidate")
        path = Path(result["path"])
        self.assertTrue(path.exists())
        self.assertEqual(path.parent, self.vault / "candidates")
        self.assertIn("intentionally untrusted", path.read_text(encoding="utf-8"))

    def test_lesson_requires_evidence(self):
        result = json.loads(mod._propose_lesson({"summary": "maybe useful"}))
        self.assertFalse(result["ok"])
        self.assertIn("evidence is required", result["error"])

    def test_recall_fails_cleanly_when_index_unavailable(self):
        with mock.patch.object(mod.shutil, "which", return_value=None):
            result = json.loads(mod._recall({"query": "x"}))
        self.assertFalse(result["ok"])
        self.assertFalse(result["retry_same_call"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
