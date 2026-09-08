#!/usr/bin/env python3
from __future__ import annotations

import sys
import json
import unittest
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_retrieval as kb  # noqa: E402


MANIFEST = {
    "gbrain": {
        "source_id": "xstudio-knowledge", "allowed_slug_prefixes": ["knowledge/", "deploy/skills/xstudio/"],
        "excluded_slug_prefixes": ["agent_comms/", "knowledge/eval/"], "excluded_slugs": ["knowledge/atlas/old"],
        "candidate_limit": 12, "return_limit": 3, "snippet_chars": 600, "timeout_seconds": 20,
        "min_retrieval_score": 0.70, "min_embedding_coverage_pct": 100.0,
    },
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


class GBrainManifestTests(unittest.TestCase):
    def test_production_manifest_has_bounded_source_scoped_gbrain_contract(self):
        cfg = kb.load_manifest()["gbrain"]
        self.assertEqual((cfg["source_id"], cfg["candidate_limit"], cfg["return_limit"]),
                         ("xstudio-knowledge", 12, 3))
        self.assertEqual((cfg["snippet_chars"], cfg["min_retrieval_score"], cfg["min_embedding_coverage_pct"]),
                         (600, 0.70, 100.0))

    def test_gbrain_contract_never_allows_non_authority_surfaces(self):
        cfg = kb.load_manifest()["gbrain"]
        self.assertIn("knowledge/", cfg["allowed_slug_prefixes"])
        self.assertTrue({"agent_comms/", "plans/", "attachments/", ".env"} <= set(cfg["excluded_slug_prefixes"]))


class _Result:
    def __init__(self, stdout="", stderr="", returncode=0):
        self.stdout, self.stderr, self.returncode = stdout, stderr, returncode


class GBrainAdapterTests(unittest.TestCase):
    def setUp(self):
        self.cfg = MANIFEST["gbrain"]

    def test_status_requires_exact_source_full_coverage_and_drained_jobs(self):
        payload = {"sources": [{"source_id": "xstudio-knowledge", "total_pages": 142,
                    "total_chunks": 601, "embedded_chunks": 601, "embed_coverage_pct": 100,
                    "failed_jobs_24h": 0, "queue_depth": 0}]}
        status = kb.get_gbrain_status(self.cfg, runner=lambda *a, **k: _Result(json.dumps(payload)))
        self.assertEqual(status["status"], "READY")

    def test_gbrain_runner_adds_bun_to_non_login_path(self):
        seen = {}
        def runner(cmd, **kwargs):
            seen.update(kwargs); return _Result('{"sources":[]}')
        kb.get_gbrain_status(self.cfg, runner=runner)
        self.assertTrue(seen["env"]["PATH"].startswith("/home/snehil/.bun/bin:"))

    def test_status_reports_incomplete_embeddings(self):
        payload = {"sources": [{"source_id": "xstudio-knowledge", "total_pages": 142,
                    "total_chunks": 601, "embedded_chunks": 227, "embed_coverage_pct": 37.8,
                    "failed_jobs_24h": 0, "queue_depth": 0}]}
        status = kb.get_gbrain_status(self.cfg, runner=lambda *a, **k: _Result(json.dumps(payload)))
        self.assertEqual(status["status"], "DEGRADED")

    def test_search_is_scoped_bounded_and_filters_weak_or_forbidden_hits(self):
        rows = [
            {"slug":"agent_comms/old","source_id":"xstudio-knowledge","score":.99},
            {"slug":"knowledge/xbatch-investigation-surfaces","source_id":"xstudio-knowledge",
             "title":"Xbatch", "chunk_text":"SAP posting", "score":.91, "keyword_hit":True},
            {"slug":"knowledge/weak","source_id":"xstudio-knowledge","score":.42},
        ]
        calls = []
        def runner(cmd, **kwargs):
            calls.append(cmd); return _Result(json.dumps(rows))
        result = kb.retrieve_gbrain("SAP posting pending", self.cfg, runner=runner)
        request = json.loads(calls[0][3])
        self.assertEqual(request["source_id"], "xstudio-knowledge")
        self.assertEqual([h["slug"] for h in result["hits"]], ["knowledge/xbatch-investigation-surfaces"])

    def test_search_failure_and_weak_neighbour_abstain(self):
        failed = kb.retrieve_gbrain("SAP", self.cfg, runner=lambda *a, **k: _Result(stderr="closed", returncode=1))
        weak = kb.retrieve_gbrain("leave policy", self.cfg, runner=lambda *a, **k: _Result(json.dumps([
            {"slug":"knowledge/weak","source_id":"xstudio-knowledge","score":.95, "evidence":"weak_semantic"}])) )
        self.assertEqual((failed["status"], failed["hits"], weak["abstained"]), ("UNAVAILABLE", [], True))

    def test_weak_semantic_label_is_accepted_only_with_two_literal_ticket_terms(self):
        rows = [{"slug":"knowledge/work-order", "source_id":"xstudio-knowledge", "score":.90,
                 "title":"Work order execution", "chunk_text":"campaign status", "evidence":"weak_semantic"}]
        result = kb.retrieve_gbrain("work order missing", self.cfg,
                                    runner=lambda *a, **k: _Result(json.dumps(rows)))
        self.assertFalse(result["abstained"])


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


class CombinedRetrievalTests(unittest.TestCase):
    def test_retrieve_keeps_routes_solutions_and_gbrain_separate(self):
        gbrain = {"status":"READY", "hits":[{"kb_id":"gbrain:x:y"}], "abstained":False}
        with patch.object(kb, "fetch_articles", return_value=[]), patch.object(kb, "retrieve_gbrain", return_value=gbrain):
            result = kb.retrieve(None, "heat issue", MANIFEST)
        self.assertEqual(result["gbrain"], gbrain)
        self.assertEqual(result["solutions"], [])
        self.assertIn("route_candidates", result)

    def test_gbrain_failure_preserves_routes_and_explicit_unavailability(self):
        unavailable = {"status":"UNAVAILABLE", "hits":[], "abstained":True, "abstention_reason":"timeout"}
        with patch.object(kb, "fetch_articles", return_value=[]), patch.object(kb, "retrieve_gbrain", return_value=unavailable):
            result = kb.retrieve(None, "HeatNo H123", MANIFEST)
        self.assertEqual(result["route_candidates"][0]["route"], "heat_execution")
        self.assertEqual(result["gbrain"]["status"], "UNAVAILABLE")


if __name__ == "__main__":
    unittest.main()
