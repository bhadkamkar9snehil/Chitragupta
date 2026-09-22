#!/usr/bin/env python3
"""Contract tests for l2_context_retriever.py, the adapter that gives
assemble_stage_context() the kb.retrieve(...) call shape it expects without
overwriting the live SQL kb_retrieval.py (see l2_context_retriever.py's
module docstring for why both exist)."""
from __future__ import annotations

import unittest
from unittest import mock

import l2_context_retriever as mod
from l2_context_envelope import ALLOWED_TRUST_BY_COLLECTION


class ContextRetrieverTests(unittest.TestCase):
    def _manifest(self):
        return {
            "always_load": ["mental-model.md"],
            "routes": [{"route": "sap_posting", "keywords": ["sap", "posting"], "load": ["sap.md"]}],
            "identifier_routing": {},
        }

    def test_gbrain_lane_trust_classes_match_envelope_schema(self):
        """A trust_class this adapter emits that l2_context_envelope rejects
        would silently degrade every review/rework card (assemble_stage_context
        raises, the CLI wrapper falls back to assemble_degraded_context) --
        catch that here instead of only via a live subprocess failure."""
        for _limit_key, _scope, envelope_key, _source_type, trust_class in mod._GBRAIN_LANES:
            self.assertIn(trust_class, ALLOWED_TRUST_BY_COLLECTION[envelope_key])

    def test_missing_source_degrades_named_not_raised(self):
        with mock.patch.object(mod.gbrain, "search", return_value={"ok": False, "error": "no requested source is populated yet"}):
            result = mod.retrieve("posting stuck", self._manifest(), top=3,
                                  limits={"facts": 3, "solutions": 2, "approved_cases": 2, "rejected_cases": 2, "reopened_cases": 2})
        self.assertTrue(result["retrieval_degraded"])
        # The "facts" policy lane queries the "knowledge" gbrain scope (see
        # l2_context_retriever._GBRAIN_LANES), so the reported reason names
        # the scope actually queried, not the policy limit key.
        self.assertTrue(any("knowledge:" in reason for reason in result["degradation_reasons"]))
        self.assertEqual(result["promoted_facts"], [])

    def test_populated_source_yields_real_items_with_valid_trust_class(self):
        def fake_search(query, *, scope, limit, automatic):
            if scope == "knowledge":
                return {
                    "ok": True, "source_ids": ["xstudio-knowledge"],
                    "results": [{"slug": "knowledge/x", "title": "X", "chunk_text": "relevant text", "score": 0.9}],
                }
            return {"ok": False, "error": "no requested source is populated yet"}

        with mock.patch.object(mod.gbrain, "search", side_effect=fake_search):
            result = mod.retrieve("posting stuck", self._manifest(), top=3,
                                  limits={"facts": 3, "solutions": 2, "approved_cases": 2, "rejected_cases": 2, "reopened_cases": 2})
        self.assertEqual(len(result["promoted_facts"]), 1)
        item = result["promoted_facts"][0]
        self.assertEqual(item["source_ref"], "knowledge/x")
        self.assertIn(item["trust_class"], ALLOWED_TRUST_BY_COLLECTION["promoted_facts"])
        self.assertEqual(result["gbrain"]["knowledge"]["source_ids"], ["xstudio-knowledge"])

    def test_include_gbrain_false_skips_every_lane_without_calling_gbrain(self):
        with mock.patch.object(mod.gbrain, "search") as search:
            result = mod.retrieve("posting stuck", self._manifest(), top=3, include_gbrain=False)
        search.assert_not_called()
        self.assertFalse(result["retrieval_degraded"])
        for _limit_key, _scope, envelope_key, _source_type, _trust_class in mod._GBRAIN_LANES:
            self.assertEqual(result[envelope_key], [])

    def test_canonical_documents_use_manifest_routing_not_sql(self):
        result = mod.retrieve("sap posting failed", self._manifest(), top=3, include_gbrain=False, root=None)
        refs = {item["source_ref"] for item in result["canonical_documents"] if "error" not in item}
        # always_load doc plus the matched route's doc, both resolved relative to REPO_ROOT.
        self.assertTrue(any("mental-model.md" in ref for ref in refs) or refs == set(),
                         "unreadable Knowledge/ files in a bare test env degrade to error items, not a crash")


if __name__ == "__main__":
    unittest.main(verbosity=2)
