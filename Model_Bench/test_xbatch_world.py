import json
import tempfile
import unittest
from pathlib import Path

from Model_Bench.xbatch_world import (
    build_evidence_matrix,
    load_world,
    select_recipes,
    validate_recipes,
    world_context,
)


class XBatchWorldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.world = load_world()

    def test_every_manifest_route_has_exactly_one_recipe(self):
        manifest_routes = {route["route"] for route in self.world["manifest"]["routes"]}
        recipe_routes = [recipe["route"] for recipe in self.world["recipes"]]
        self.assertEqual(manifest_routes, set(recipe_routes))
        self.assertEqual(len(recipe_routes), len(set(recipe_routes)))

    def test_recipe_validation_rejects_arbitrary_sql(self):
        bad = [{
            "recipe_id": "bad", "route": "discover", "description": "bad",
            "ticket_signals": [], "identifiers": [],
            "probes": [{"tool": "xstudio_query", "arguments": {"sql": "SELECT * FROM x"}}],
            "required_evidence": [], "interpretation_rules": [],
            "stop_conditions": [], "escalation_conditions": [], "review_checks": [],
        }]
        with self.assertRaisesRegex(ValueError, "arbitrary SQL"):
            validate_recipes(bad, {"discover"})

    def test_sap_ticket_selects_sap_recipe_without_model_inference(self):
        selection = select_recipes({
            "BriefDetails": "Production posting pending in SAP",
            "ProblemCategory": "SAP Integration",
            "ExtractedEntitiesJson": json.dumps({"HeatNo": "H99328"}),
        }, self.world)
        self.assertEqual("sap_posting", selection["primary"]["route"])
        self.assertEqual("99328", selection["identifiers"]["heat"])

    def test_world_context_contains_direct_relationship_neighbours_and_is_bounded(self):
        selection = select_recipes({
            "BriefDetails": "Billet H99328 is missing from yard inventory",
            "ExtractedEntitiesJson": json.dumps({"HeatNo": "H99328"}),
        }, self.world)
        context = world_context(selection, self.world, max_chars=6000)
        self.assertEqual("billet_inventory", context["recipe"]["route"])
        objects = {
            edge["target"]["object"]
            for edge in context["relationships"]
            if edge["source"]["object"] == "Billet_Inventory"
        }
        self.assertIn("XBatch_Material_Grade_Mst_Tbl", objects)
        self.assertLessEqual(len(json.dumps(context, separators=(",", ":"))), 6000)

    def test_unknown_ticket_uses_discover_recipe_without_fabricated_identifier(self):
        selection = select_recipes({"BriefDetails": "unclassified application behaviour"}, self.world)
        self.assertEqual("discover", selection["primary"]["route"])
        self.assertEqual({}, selection["identifiers"])

    def test_evidence_matrix_maps_claim_refs_to_recorded_actions(self):
        recipe = next(item for item in self.world["recipes"] if item["route"] == "heat_execution")
        proposal = {"claims": [{"claim": "EAF row exists", "evidence_refs": ["A1"]}]}
        matrix = build_evidence_matrix(proposal, recipe, [{"ID": "A1", "OperationName": "l2_heat_eaf", "ObjectName": "EAF_PER_HEAT"}])
        self.assertEqual("REFERENCED", matrix["claims"][0]["status"])
        self.assertEqual(["heat_process_state"], matrix["claims"][0]["evidence_categories"])

    def test_evidence_matrix_reads_frozen_proposal_evidence_shape(self):
        recipe = next(item for item in self.world["recipes"] if item["route"] == "heat_execution")
        proposal = {"claims": [{"id": "C1", "claim": "LRF row exists", "status": "VERIFIED",
                                 "evidence": [{"action_id": "A2"}]}]}
        matrix = build_evidence_matrix(
            proposal, recipe,
            [{"ID": "A2", "OperationName": "l2_heat_lrf", "ObjectName": "LRF_Per_Heat"}],
        )
        self.assertEqual("REFERENCED", matrix["claims"][0]["status"])
        self.assertEqual(["heat_process_state"], matrix["claims"][0]["evidence_categories"])


if __name__ == "__main__":
    unittest.main()
