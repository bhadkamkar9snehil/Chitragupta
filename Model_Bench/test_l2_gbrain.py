#!/usr/bin/env python3
"""Focused contracts for the temporary dispatch-time GBrain adapter."""
from __future__ import annotations

import os
import unittest
from pathlib import Path
from unittest import mock

import l2_gbrain as mod


class GBrainAdapterTests(unittest.TestCase):
    def test_uses_shared_xstudio_source_names(self):
        self.assertEqual(set(mod.SOURCE_IDS), {
            "xstudio-knowledge", "xstudio-reference", "xstudio-solutions",
            "xstudio-approved-cases", "xstudio-rejected-cases", "xstudio-reopened-cases",
        })

    def test_trusted_scope_excludes_historical_cases(self):
        self.assertEqual(
            set(mod.sources_for_scope("trusted")),
            {"xstudio-knowledge", "xstudio-reference", "xstudio-solutions"},
        )
        self.assertTrue(
            set(mod.sources_for_scope("trusted")).isdisjoint(mod.sources_for_scope("cases"))
        )

    def test_search_names_sources_explicitly(self):
        with mock.patch.object(mod, "run", return_value=(0, '[{"slug":"x"}]', "")) as run:
            result = mod.search("posting stuck", scope="trusted", limit=5)
        self.assertTrue(result["ok"])
        args = run.call_args.args[0]
        self.assertEqual(args[0], "search")
        self.assertEqual(
            args[args.index("--source") + 1],
            "xstudio-knowledge,xstudio-reference,xstudio-solutions",
        )

    def test_unknown_scope_fails_before_process_call(self):
        with mock.patch.object(mod, "run") as run:
            result = mod.search("x", scope="sessions")
        self.assertFalse(result["ok"])
        run.assert_not_called()

    def test_run_uses_shared_xstudio_brain_home(self):
        completed = mock.Mock(returncode=0, stdout="[]", stderr="")
        with mock.patch("subprocess.run", return_value=completed) as subprocess_run, \
             mock.patch.dict(os.environ, {"XSTUDIO_GBRAIN_HOME": "/tmp/xstudio-brain"}, clear=False):
            mod.run(["sources", "list", "--json"])
        self.assertEqual(
            subprocess_run.call_args.kwargs["env"]["GBRAIN_HOME"],
            "/tmp/xstudio-brain",
        )

    def test_default_home_is_xstudio_gbrain(self):
        with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(Path, "home", return_value=Path("/home/test")):
            self.assertEqual(mod.gbrain_home(), Path("/home/test/.hermes/xstudio-gbrain"))

    def test_non_json_output_fails_closed(self):
        with mock.patch.object(mod, "run", return_value=(0, "not json", "")):
            result = mod.search("x")
        self.assertFalse(result["ok"])
        self.assertFalse(result["retry_same_call"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
