#!/usr/bin/env python3
"""Focused contracts for the isolated GBrain adapter."""
from __future__ import annotations

import os
import unittest
from pathlib import Path
from unittest import mock

import l2_gbrain as mod


class GBrainAdapterTests(unittest.TestCase):
    def test_only_real_model_facing_source_lanes_exist(self):
        self.assertEqual(set(mod.SOURCE_IDS), {
            "l2-knowledge", "l2-facts", "l2-solutions",
            "l2-approved-cases", "l2-rejected-cases", "l2-reopened-cases",
        })
        self.assertNotIn("sessions", mod.SCOPE_SOURCES)
        self.assertNotIn("candidates", mod.SCOPE_SOURCES)
        self.assertNotIn("all", mod.SCOPE_SOURCES)

    def test_trusted_scope_excludes_historical_cases(self):
        self.assertEqual(
            set(mod.sources_for_scope("trusted")),
            {"l2-knowledge", "l2-facts", "l2-solutions"},
        )
        self.assertTrue(
            set(mod.sources_for_scope("trusted")).isdisjoint(mod.sources_for_scope("cases"))
        )

    def test_search_is_always_explicit_retrieval_only(self):
        with mock.patch.object(mod, "run", return_value=(0, '[{"slug":"x"}]', "")) as run:
            result = mod.search("posting stuck", scope="trusted", limit=5)
        self.assertTrue(result["ok"])
        args = run.call_args.args[0]
        self.assertEqual(args[0], "search")
        self.assertNotIn("query", args)
        self.assertEqual(
            args[args.index("--source") + 1],
            "l2-knowledge,l2-facts,l2-solutions",
        )

    def test_unknown_scope_fails_before_process_call(self):
        with mock.patch.object(mod, "run") as run:
            result = mod.search("x", scope="sessions")
        self.assertFalse(result["ok"])
        run.assert_not_called()

    def test_run_forces_isolated_gbrain_home(self):
        completed = mock.Mock(returncode=0, stdout="[]", stderr="")
        with mock.patch("subprocess.run", return_value=completed) as subprocess_run, \
             mock.patch.dict(os.environ, {"CHITRAGUPTA_GBRAIN_HOME": "/tmp/chitragupta-brain"}, clear=False):
            mod.run(["sources", "list", "--json"])
        self.assertEqual(
            subprocess_run.call_args.kwargs["env"]["GBRAIN_HOME"],
            "/tmp/chitragupta-brain",
        )

    def test_knowledge_path_can_be_bound_explicitly(self):
        with mock.patch.dict(os.environ, {"CHITRAGUPTA_KNOWLEDGE_PATH": "/tmp/repo/Knowledge"}, clear=False):
            self.assertEqual(mod.knowledge_path(), Path("/tmp/repo/Knowledge"))

    def test_non_json_output_fails_closed(self):
        with mock.patch.object(mod, "run", return_value=(0, "not json", "")):
            result = mod.search("x")
        self.assertFalse(result["ok"])
        self.assertFalse(result["retry_same_call"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
