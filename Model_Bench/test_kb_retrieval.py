#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_retrieval as kb  # noqa: E402


MANIFEST = {
    "always_load": ["mental-model.md"],
    "identifier_routing": {
        "HeatNo": ["heat_execution"],
        "HeatID": ["heat_execution"],
        "EquipmentID": ["performance"],
    },
    "routes": [
        {
            "route": "performance",
            "description": "Delay OEE downtime performance issue",
            "keywords": ["delay", "OEE", "downtime", "equipment delay"],
            "load": ["xbatch-investigation-surfaces.md#delay--oee"],
        },
        {
            "route": "heat_execution",
            "description": "Heat EAF LRF CCM execution",
            "keywords": ["heat", "EAF", "LRF", "CCM"],
            "load": ["sohar-sms-event-workflows.md"],
        },
        {
            "route": "discover",
            "description": "Unknown symptom",
            "keywords": [],
            "load": ["sql-write-model.md"],
        },
    ],
}


class RouteTests(unittest.TestCase):
    def test_strong_identifier_beats_vague_language(self):
        routes = kb.route_candidates("HeatNo 1604015 delay value looks wrong", MANIFEST)
        self.assertEqual(routes[0]["route"], "heat_execution")
        self.assertIn("HeatNo identifier", routes[0]["reasons"])

    def test_no_signal_abstains_to_discover(self):
        routes = kb.route_candidates("screen behaves strangely", MANIFEST)
        self.assertEqual(routes, [{"route": "discover", "score": 0.0, "reasons": ["no deterministic route signal"]}])

    def test_route_returns_canonical_knowledge_paths(self):
        routes = [{"route": "performance", "score": 10.0, "reasons": []}]
        docs = kb.knowledge_docs_for_routes(MANIFEST, routes)
        paths = [d["path"] for d in docs]
        self.assertIn("Knowledge/mental-model.md", paths)
        self.assertIn("Knowledge/xbatch-investigation-surfaces.md#delay--oee", paths)

    def test_legacy_string_identifier_mapping_still_parses(self):
        legacy = dict(MANIFEST)
        legacy["identifier_routing"] = {"TransactionID": "api_transaction or sap_posting"}
        legacy["routes"] = MANIFEST["routes"] + [
            {"route": "api_transaction", "description": "API transaction", "keywords": ["API"], "load": []},
            {"route": "sap_posting", "description": "SAP posting", "keywords": ["SAP"], "load": []},
        ]
        routes = kb.route_candidates("TransactionID ABC failed", legacy)
        names = [r["route"] for r in routes[:2]]
        self.assertEqual(set(names), {"api_transaction", "sap_posting"})


class JevFusionTests(unittest.TestCase):
    def test_single_identifier_route_skips_jev(self):
        def should_not_run(*args, **kwargs):
            raise AssertionError("Jev must not run for one unambiguous identifier route")

        routes, routing = kb.resolve_route_candidates(
            "HeatNo 1604015 delay value looks wrong",
            MANIFEST,
            jev_decider=should_not_run,
        )
        self.assertEqual(routes[0]["route"], "heat_execution")
        self.assertEqual(routing["mode"], "deterministic")
        self.assertEqual(routing["identifier_routes"], ["heat_execution"])
        self.assertIn("authoritative", routing["jev"]["reason"])

    def test_ambiguous_identifier_constrains_jev_choice(self):
        manifest = dict(MANIFEST)
        manifest["identifier_routing"] = {
            **MANIFEST["identifier_routing"],
            "TransactionID": ["api_transaction", "sap_posting"],
        }
        manifest["routes"] = MANIFEST["routes"] + [
            {
                "route": "api_transaction",
                "description": "API transaction failure",
                "keywords": ["API", "transaction ID"],
                "load": [],
            },
            {
                "route": "sap_posting",
                "description": "SAP posting failure",
                "keywords": ["SAP", "posting"],
                "load": [],
            },
        ]
        seen = {}

        def decider(query, supplied_manifest, *, allowed_routes=None):
            seen["allowed_routes"] = list(allowed_routes or [])
            return {
                "enabled": True,
                "accepted": True,
                "choice": "sap_posting",
                "confidence": 0.91,
                "probabilities": {"api_transaction": 0.09, "sap_posting": 0.91},
                "model": "jev-test",
            }

        routes, routing = kb.resolve_route_candidates(
            "TransactionID 123 failed before posting",
            manifest,
            jev_decider=decider,
        )
        self.assertEqual(set(seen["allowed_routes"]), {"api_transaction", "sap_posting"})
        self.assertEqual(routes[0]["route"], "sap_posting")
        self.assertEqual(routing["mode"], "jev")
        self.assertEqual(routing["selected_route"], "sap_posting")

    def test_semantic_choice_can_promote_canonical_route_without_identifier(self):
        def decider(query, supplied_manifest, *, allowed_routes=None):
            self.assertIsNone(allowed_routes)
            return {
                "enabled": True,
                "accepted": True,
                "choice": "performance",
                "confidence": 0.86,
                "probabilities": {"performance": 0.86, "discover": 0.14},
                "model": "jev-test",
            }

        routes, routing = kb.resolve_route_candidates(
            "screen behaves strangely",
            MANIFEST,
            jev_decider=decider,
        )
        self.assertEqual(routes[0]["route"], "performance")
        self.assertEqual(routes[0]["semantic_source"], "typesafe_jev")
        self.assertEqual(routing["mode"], "jev")

    def test_low_confidence_jev_preserves_deterministic_order(self):
        deterministic = kb.route_candidates("delay equipment missing", MANIFEST)

        def decider(query, supplied_manifest, *, allowed_routes=None):
            return {
                "enabled": True,
                "accepted": False,
                "choice": "heat_execution",
                "confidence": 0.51,
                "probabilities": {"performance": 0.49, "heat_execution": 0.51},
                "model": "jev-test",
                "reason": "Jev confidence below configured threshold",
            }

        routes, routing = kb.resolve_route_candidates(
            "delay equipment missing",
            MANIFEST,
            jev_decider=decider,
        )
        self.assertEqual(routes, deterministic)
        self.assertEqual(routing["mode"], "deterministic")
        self.assertFalse(routing["jev"]["accepted"])


class ArticleRankingTests(unittest.TestCase):
    def setUp(self):
        self.routes = [{"route": "performance", "score": 10.0, "reasons": ["keywords: delay"]}]

    def test_route_only_article_is_not_retrieved(self):
        articles = [
            {
                "ID": "A",
                "Title": "OEE dashboard colour configuration",
                "ProblemSummary": "Visual styling request",
                "RootCause": "Theme configuration",
                "ResolutionSteps": "Change the dashboard theme",
                "Route": "performance",
                "Tags": "dashboard",
                "UsageCount": 100,
                "CreatedOn": None,
                "ModifiedOn": None,
            }
        ]
        ranked = kb.rank_articles(articles, "delay equipment missing", self.routes)
        self.assertEqual(ranked, [])

    def test_one_generic_word_is_not_enough(self):
        articles = [
            {
                "ID": "B",
                "Title": "Delay issue",
                "ProblemSummary": "General note",
                "RootCause": "Unknown",
                "ResolutionSteps": "Review configuration",
                "Route": "performance",
                "Tags": "",
                "UsageCount": 50,
                "CreatedOn": None,
                "ModifiedOn": None,
            }
        ]
        ranked = kb.rank_articles(articles, "delay equipment missing", self.routes)
        self.assertEqual(ranked, [])

    def test_specific_multi_term_match_returns_provenance(self):
        articles = [
            {
                "ID": "C",
                "Title": "Equipment delay missing from analysis",
                "ProblemSummary": "Equipment delay row is present but equipment mapping is missing",
                "RootCause": "Equipment mapping data entry gap",
                "ResolutionSteps": "Correct the equipment mapping and verify the delay analysis row",
                "Route": "performance",
                "Tags": "delay,equipment,mapping",
                "UsageCount": 4,
                "CreatedOn": None,
                "ModifiedOn": None,
            }
        ]
        ranked = kb.rank_articles(articles, "delay equipment missing", self.routes)
        self.assertEqual(len(ranked), 1)
        self.assertEqual(ranked[0]["kb_id"], "solution:C")
        self.assertEqual(ranked[0]["source_ref"], "Hermes_Solution_Article_Mst_Tbl:C")
        self.assertTrue(ranked[0]["verification_required"])
        self.assertGreaterEqual(len(ranked[0]["matched_terms"]), 2)


if __name__ == "__main__":
    unittest.main()
