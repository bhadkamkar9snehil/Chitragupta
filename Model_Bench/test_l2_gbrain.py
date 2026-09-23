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
        self.assertEqual(trusted, {mod.XSTUDIO_KNOWLEDGE_SOURCE, "l2-knowledge", "l2-facts", "l2-solutions"})
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("sessions")))
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("candidates")))
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("approved_cases")))

    def test_search_always_names_explicit_sources(self):
        # The installed gbrain CLI scopes one `search` call to exactly one
        # --source-id (no combined multi-source syntax), so a scope with N
        # sources makes N calls and merges. Every call must still name its
        # source explicitly -- never an unscoped/federated read.
        with mock.patch.object(mod, "run", return_value=(0, '[{"slug":"x","score":0.5}]', "")) as run:
            result = mod.search("posting stuck", scope="trusted", mode="hybrid", limit=5, automatic=True)
        self.assertTrue(result["ok"])
        called_source_ids = []
        for call in run.call_args_list:
            args = call.args[0]
            self.assertEqual(args[0], "search")
            called_source_ids.append(args[args.index("--source-id") + 1])
        self.assertEqual(set(called_source_ids), {"xstudio-knowledge", "l2-knowledge", "l2-facts", "l2-solutions"})
        self.assertNotIn("l2-sessions", called_source_ids)
        self.assertTrue(result["deterministic_retrieval"])
        self.assertTrue(result["automatic"])

    def test_search_skips_lanes_gbrain_reports_as_unknown_source(self):
        """Only xstudio-knowledge is registered today; l2-facts/l2-solutions
        are the future learning-cycle lanes. A missing lane must be skipped,
        not treated as a hard failure, as long as something in scope answers."""
        def fake_run(args, **kwargs):
            source_id = args[args.index("--source-id") + 1]
            if source_id == "xstudio-knowledge":
                return (0, '[{"slug":"knowledge/x","score":0.9}]', "")
            return (1, "", f"Error [unknown_source]: source {source_id!r} does not exist (removed or archived)")

        with mock.patch.object(mod, "run", side_effect=fake_run):
            result = mod.search("LRF_Per_Heat columns", scope="trusted", automatic=True)
        self.assertTrue(result["ok"])
        self.assertEqual(result["source_ids"], ["xstudio-knowledge"])
        self.assertEqual(set(result["missing_source_ids"]), {"l2-knowledge", "l2-facts", "l2-solutions"})
        self.assertEqual(len(result["results"]), 1)

    def test_search_fails_when_every_lane_in_scope_is_missing(self):
        with mock.patch.object(mod, "run", return_value=(1, "", "Error [unknown_source]: does not exist")):
            result = mod.search("x", scope="facts", automatic=False)
        self.assertFalse(result["ok"])
        self.assertIn("no requested source is populated yet", result["error"])

    def test_explicit_recall_into_an_empty_lane_answers_from_knowledge(self):
        """Live 2026-09-23: scope=facts/cases/solutions errored (not populated yet) and the worker
        spent a turn retrying scope=knowledge. The explicit call now falls back in one step."""
        def fake_run(args, **kwargs):
            if args[args.index("--source-id") + 1] == "xstudio-knowledge":
                return (0, '[{"slug":"knowledge/lrf","score":0.8}]', "")
            return (1, "", "Error [unknown_source]: does not exist")

        with mock.patch.object(mod, "run", side_effect=fake_run):
            result = mod.search("arcing time", scope="facts", automatic=False)
            automatic = mod.search("arcing time", scope="facts", automatic=True)
        self.assertTrue(result["ok"])
        self.assertEqual(result["fallback_scope"], "knowledge")
        self.assertEqual(result["requested_scope"], "facts")
        self.assertFalse(automatic["ok"])  # harness retrieval keeps the named-missing contract

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
        self.assertEqual(home, Path.home() / ".hermes" / "xstudio-gbrain")

    def test_binary_falls_back_to_bun_install_dir_when_not_on_path(self):
        """A systemd --user gateway's PATH is a snapshot from profile-install
        time and typically lacks bun's install dir. gbrain (a bun-installed
        CLI) must still resolve without a per-machine service-unit edit."""
        with mock.patch.object(mod.shutil, "which", return_value=None), \
             mock.patch.object(Path, "exists", return_value=True), \
             mock.patch("os.access", return_value=True):
            self.assertEqual(mod.binary(), str(Path.home() / ".bun" / "bin" / "gbrain"))

    def test_run_injects_bun_bin_into_subprocess_path(self):
        completed = mock.Mock(returncode=0, stdout="[]", stderr="")
        with mock.patch("subprocess.run", return_value=completed) as subprocess_run, \
             mock.patch.dict(os.environ, {"PATH": "/usr/bin"}, clear=True):
            mod.run(["sources", "list", "--json"])
        env_path = subprocess_run.call_args.kwargs["env"]["PATH"]
        self.assertIn(str(Path.home() / ".bun" / "bin"), env_path.split(os.pathsep))

    def test_non_json_output_fails_closed(self):
        with mock.patch.object(mod, "run", return_value=(0, "not json", "")):
            result = mod.search("x")
        self.assertFalse(result["ok"])
        self.assertFalse(result["retry_same_call"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
