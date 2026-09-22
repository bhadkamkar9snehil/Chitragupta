#!/usr/bin/env python3
"""Contract tests for the harness-owned GBrain adapter."""
from __future__ import annotations

import os
import unittest
from pathlib import Path
from unittest import mock

import l2_gbrain as mod


class GBrainAdapterTests(unittest.TestCase):
    def test_source_topology_contains_all_explicit_trust_lanes(self):
        self.assertEqual(set(mod.SOURCE_DIRS), {
            "l2-knowledge", "l2-facts", "l2-solutions",
            "l2-approved-cases", "l2-rejected-cases", "l2-reopened-cases",
            "l2-sessions", "l2-candidates",
        })

    def test_trust_scopes_are_structurally_separate(self):
        trusted = set(mod.sources_for_scope("trusted"))
        self.assertEqual(trusted, {"l2-knowledge", "l2-facts", "l2-solutions"})
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("sessions")))
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("candidates")))
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("approved_cases")))

    def test_search_always_names_explicit_sources(self):
        with mock.patch.object(mod, "run", return_value=(0, '[{"slug":"x"}]', "")) as run:
            result = mod.search("posting stuck", scope="trusted", mode="hybrid", limit=5, automatic=True)
        self.assertTrue(result["ok"])
        args = run.call_args.args[0]
        self.assertEqual(args[0], "search")
        source_arg = args[args.index("--source") + 1]
        self.assertEqual(source_arg, "l2-knowledge,l2-facts,l2-solutions")
        self.assertNotIn("l2-sessions", source_arg)
        self.assertTrue(result["deterministic_retrieval"])
        self.assertTrue(result["automatic"])

    def test_legacy_modes_never_invoke_gbrain_query(self):
        for requested in ("deep", "vector", "fts", "hybrid"):
            with self.subTest(requested=requested), \
                 mock.patch.object(mod, "run", return_value=(0, '[]', "")) as run:
                result = mod.search("root cause", scope="approved_cases", mode=requested, automatic=True)
            self.assertTrue(result["ok"])
            self.assertEqual(result["effective_mode"], "hybrid")
            self.assertEqual(run.call_args.args[0][0], "search")
            self.assertNotIn("query", run.call_args.args[0])

    def test_automatic_retrieval_forbids_raw_or_mixed_scopes(self):
        for scope in ("all", "sessions", "candidates"):
            with self.subTest(scope=scope), mock.patch.object(mod, "run") as run:
                result = mod.search("x", scope=scope, automatic=True)
            self.assertFalse(result["ok"])
            self.assertIn("forbidden for automatic", result["error"])
            run.assert_not_called()

    def test_explicit_supplemental_recall_can_address_untrusted_lane(self):
        with mock.patch.object(mod, "run", return_value=(0, '[]', "")) as run:
            result = mod.search("counterexample", scope="sessions", automatic=False)
        self.assertTrue(result["ok"])
        self.assertEqual(result["source_ids"], ["l2-sessions"])
        self.assertEqual(run.call_args.args[0][0], "search")

    def test_unknown_mode_fails_before_process_call(self):
        with mock.patch.object(mod, "run") as run:
            result = mod.search("x", mode="think")
        self.assertFalse(result["ok"])
        run.assert_not_called()

    def test_run_forces_isolated_gbrain_home(self):
        completed = mock.Mock(returncode=0, stdout="[]", stderr="")
        with mock.patch("subprocess.run", return_value=completed) as subprocess_run, \
             mock.patch.dict(os.environ, {"CHITRAGUPTA_GBRAIN_HOME": "/tmp/chitragupta-brain"}, clear=False):
            mod.run(["sources", "list", "--json"])
        env = subprocess_run.call_args.kwargs["env"]
        self.assertEqual(env["GBRAIN_HOME"], "/tmp/chitragupta-brain")

    def test_default_gbrain_home_is_not_generic_user_brain(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            home = mod.gbrain_home()
        self.assertEqual(home, Path.home() / ".hermes" / "l2-gbrain")

    def test_non_json_output_fails_closed(self):
        with mock.patch.object(mod, "run", return_value=(0, "not json", "")):
            result = mod.search("x")
        self.assertFalse(result["ok"])
        self.assertFalse(result["retry_same_call"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
