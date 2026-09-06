#!/usr/bin/env python3
"""Contract tests for the harness-owned GBrain adapter."""
from __future__ import annotations

import unittest
from unittest import mock

import l2_gbrain as mod


class GBrainAdapterTests(unittest.TestCase):
    def test_trust_scopes_are_structurally_separate(self):
        trusted = set(mod.sources_for_scope("trusted"))
        self.assertEqual(trusted, {"l2-knowledge", "l2-facts", "l2-solutions"})
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("sessions")))
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("candidates")))
        self.assertTrue(trusted.isdisjoint(mod.sources_for_scope("approved_cases")))

    def test_search_always_names_explicit_sources(self):
        with mock.patch.object(mod, "run", return_value=(0, '[{"slug":"x"}]', "")) as run:
            result = mod.search("posting stuck", scope="trusted", mode="hybrid", limit=5)
        self.assertTrue(result["ok"])
        args = run.call_args.args[0]
        self.assertEqual(args[0], "search")
        source_arg = args[args.index("--source") + 1]
        self.assertEqual(source_arg, "l2-knowledge,l2-facts,l2-solutions")
        self.assertNotIn("l2-sessions", source_arg)

    def test_deep_is_explicit_and_legacy_vector_maps_to_deep(self):
        for requested in ("deep", "vector"):
            with self.subTest(requested=requested), \
                 mock.patch.object(mod, "run", return_value=(0, '[]', "")) as run:
                result = mod.search("root cause", scope="approved_cases", mode=requested)
            self.assertTrue(result["ok"])
            self.assertEqual(result["effective_mode"], "deep")
            self.assertEqual(run.call_args.args[0][0], "query")

    def test_non_json_output_fails_closed(self):
        with mock.patch.object(mod, "run", return_value=(0, "not json", "")):
            result = mod.search("x")
        self.assertFalse(result["ok"])
        self.assertFalse(result["retry_same_call"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
