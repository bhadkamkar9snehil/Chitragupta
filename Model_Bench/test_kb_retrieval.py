#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import kb_retrieval as kb


MANIFEST = {
    "always_load": ["mental-model.md"],
    "identifier_routing": {
        "HeatNo": ["heat_execution"],
        "EquipmentID": ["performance"],
    },
    "routes": [
        {
            "route": "performance",
            "description": "Delay OEE downtime performance issue",
            "keywords": ["delay", "OEE", "downtime", "equipment delay"],
            "load": ["surfaces.md#delay--oee"],
            "live_sql_leads": ["Delay_Trn_Tbl"],
        },
        {
            "route": "heat_execution",
            "description": "Heat EAF LRF CCM execution",
            "keywords": ["heat", "EAF", "LRF", "CCM"],
            "load": ["heat.md"],
            "live_sql_leads": ["EAF_PER_HEAT"],
        },
        {
            "route": "discover",
            "description": "Unknown symptom",
            "keywords": [],
            "load": ["discover.md"],
            "live_sql_leads": ["sys.tables"],
        },
    ],
}


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.root = self.base / "repo"
        self.knowledge = self.root / "Knowledge"
        self.vault = self.base / "vault"
        self.knowledge.mkdir(parents=True)
        (self.vault / "facts").mkdir(parents=True)
        (self.vault / "solutions" / "approved").mkdir(parents=True)
        (self.knowledge / "mental-model.md").write_text("# Mental model\n\nAlways verify current state.", encoding="utf-8")
        (self.knowledge / "surfaces.md").write_text(
            "# Other\n\nIgnore this section.\n\n## Delay / OEE\n\nEquipment delay mapping and downtime analysis.\n\n## Next\n\nNot part of delay section.\n",
            encoding="utf-8",
        )
        (self.knowledge / "heat.md").write_text("# Heat execution\n\nHeatNo EAF LRF state.", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def _write_md(self, path: Path, trust: str, body: str, **meta):
        fields = {"trust": trust, **meta}
        fm = "\n".join(f"{key}: {value!r}" for key, value in fields.items())
        path.write_text(f"---\n{fm}\n---\n\n{body}\n", encoding="utf-8")

    def test_strong_identifier_beats_vague_language(self):
        routes = kb.route_candidates("HeatNo 1604015 delay value looks wrong", MANIFEST)
        self.assertEqual(routes[0]["route"], "heat_execution")
        self.assertIn("HeatNo identifier", routes[0]["reasons"])

    def test_no_signal_abstains_to_discover(self):
        routes = kb.route_candidates("screen behaves strangely", MANIFEST)
        self.assertEqual(routes, [{"route": "discover", "score": 0.0, "reasons": ["no deterministic route signal"]}])

    def test_anchor_extracts_only_requested_canonical_section(self):
        value = kb.read_canonical_reference("Knowledge/surfaces.md#delay--oee", root=self.root)
        self.assertTrue(value["ok"])
        self.assertIn("Equipment delay mapping", value["content"])
        self.assertNotIn("Ignore this section", value["content"])
        self.assertNotIn("Not part of delay section", value["content"])
        self.assertEqual(value["trust_class"], "canonical_reference")

    def test_only_reviewed_facts_are_eligible(self):
        self._write_md(self.vault / "facts" / "reviewed.md", "reviewed_operational", "Equipment delay mapping missing from analysis")
        self._write_md(self.vault / "facts" / "candidate.md", "unverified_candidate", "Equipment delay mapping candidate guess")
        results = kb.promoted_facts("equipment delay mapping", vault=self.vault)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["source_ref"], "facts/reviewed.md")
        self.assertEqual(results[0]["trust_class"], "reviewed_operational")

    def test_active_looking_but_unapproved_solution_is_not_trusted(self):
        path = self.vault / "solutions" / "approved" / "s1.md"
        self._write_md(
            path,
            "active_solution_article",
            "# Equipment delay solution\n\nCorrect equipment delay mapping and verify analysis.",
            solution_id="S-1",
            content_sha256="a" * 64,
        )
        self.assertEqual(kb.governed_solutions("equipment delay mapping", vault=self.vault), [])

        self._write_md(
            path,
            "governed_reusable_solution",
            "# Equipment delay solution\n\nCorrect equipment delay mapping and verify analysis.",
            solution_id="S-1",
            content_sha256="a" * 64,
            approved_by="operator",
        )
        results = kb.governed_solutions("equipment delay mapping", vault=self.vault)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["trust_class"], "governed_reusable_solution")
        self.assertEqual(results[0]["solution_id"], "S-1")
        self.assertEqual(results[0]["governance_content_sha256"], "a" * 64)

    def test_retrieve_uses_governed_sources_and_never_live_solution_sql(self):
        self._write_md(self.vault / "facts" / "f.md", "reviewed_operational", "Equipment delay mapping missing")
        self._write_md(
            self.vault / "solutions" / "approved" / "s.md",
            "governed_reusable_solution",
            "# Fix mapping\n\nEquipment delay mapping correction",
            solution_id="S-2",
            content_sha256="b" * 64,
        )
        with mock.patch.object(kb, "gbrain_trusted_search", return_value={
            "ok": True,
            "backend": "gbrain",
            "source_ids": ["l2-knowledge", "l2-facts", "l2-solutions"],
            "results": [],
        }):
            result = kb.retrieve(
                "EquipmentID E-1 equipment delay mapping",
                MANIFEST,
                vault=self.vault,
                root=self.root,
            )
        self.assertTrue(result["promoted_facts"])
        self.assertTrue(result["governed_solutions"])
        self.assertFalse(result["retrieval_policy"]["live_solution_sql_read_allowed"])
        self.assertTrue(result["retrieval_policy"]["governed_solution_export_required"])

    def test_legacy_retrieve_signature_ignores_connection_object(self):
        with mock.patch.object(kb, "gbrain_trusted_search", return_value={
            "ok": True, "backend": "gbrain",
            "source_ids": ["l2-knowledge", "l2-facts", "l2-solutions"], "results": [],
        }):
            result = kb.retrieve(
                object(),
                "EquipmentID E-1 equipment delay",
                MANIFEST,
                vault=self.vault,
                root=self.root,
            )
        self.assertEqual(result["route_candidates"][0]["route"], "performance")
        self.assertFalse(result["retrieval_policy"]["live_solution_sql_read_allowed"])

    def test_gbrain_search_is_explicit_trusted_scope_and_automatic_safe(self):
        fake_search = mock.Mock(return_value={
            "ok": True,
            "source_ids": ["l2-knowledge", "l2-facts", "l2-solutions"],
            "results": [],
        })
        fake_module = mock.Mock()
        fake_module.available.return_value = True
        fake_module.search = fake_search
        with mock.patch.dict("sys.modules", {"l2_gbrain": fake_module}):
            result = kb.gbrain_trusted_search("equipment delay", limit=4)
        self.assertTrue(result["ok"])
        fake_search.assert_called_once_with(
            "equipment delay", scope="trusted", mode="hybrid", limit=4, automatic=True
        )

    def test_source_contains_no_raw_solution_table_or_pyodbc_dependency(self):
        source = Path(kb.__file__).read_text(encoding="utf-8")
        self.assertNotIn("Hermes_Solution_Article_Mst_Tbl", source)
        self.assertNotIn("pyodbc", source)

    def test_live_sql_leads_are_route_guidance_not_solution_articles(self):
        routes = [{"route": "performance", "score": 10.0, "reasons": []}]
        leads = kb.live_sql_leads_for_routes(MANIFEST, routes)
        self.assertEqual(leads, [{"object": "Delay_Trn_Tbl", "route": "performance", "verification_required": True}])


if __name__ == "__main__":
    unittest.main(verbosity=2)
