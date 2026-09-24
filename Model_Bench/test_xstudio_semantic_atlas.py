import json
import tempfile
import unittest
from pathlib import Path

from Model_Bench.build_xstudio_semantic_atlas import build, load_relationships
from Model_Bench.export_xbatch_relationships import trust_server_certificate_value


class SemanticAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.atlas = build()

    def test_contains_every_exported_schema_and_procedure(self):
        helpdesk = self.atlas["databases"]["XStudio_Helpdesk"]
        xbatch = self.atlas["databases"]["XStudio_Xbatch"]
        self.assertEqual(254, len(helpdesk["objects"]))
        self.assertEqual(12, len(helpdesk["procedures"]))
        self.assertEqual(563, len(xbatch["objects"]))
        self.assertEqual(388, len(xbatch["procedures"]))

    def test_work_order_identifier_semantics_are_present(self):
        columns = self.atlas["databases"]["XStudio_Xbatch"]["objects"]["XBatch_Work_Order_Mst_Tbl"]["columns"]
        names = {column["name"] for column in columns}
        self.assertTrue({"ID", "WorkOrderNumber", "HeatNo", "CampaignId"} <= names)

    def test_api_summary_is_reviewed_but_mutating_posting_procedure_is_not(self):
        procedures = self.atlas["databases"]["XStudio_Xbatch"]["procedures"]
        self.assertEqual("READ_ONLY_REVIEWED", procedures["XMES_Get_API_Transaction_Summary"]["safety"])
        self.assertEqual("MUTATING", procedures["SAP_Posting_Data_ByHeat_Usp"]["safety"])
        self.assertIn("INSERT", procedures["SAP_Posting_Data_ByHeat_Usp"]["observed_write_tokens"])

    def test_api_summary_records_cross_database_dependency(self):
        refs = self.atlas["databases"]["XStudio_Xbatch"]["procedures"]["XMES_Get_API_Transaction_Summary"]["referenced_objects"]
        self.assertTrue(any("XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl" == ref for ref in refs))

    def test_contains_all_active_configuration_relationships_after_duplicate_collapse(self):
        relationships = self.atlas["relationships"]
        self.assertEqual(530, len(relationships))
        self.assertEqual(534, sum(edge["provenance"]["source_row_count"] for edge in relationships))
        billet_grade = next(
            edge for edge in relationships
            if edge["source"]["object"] == "Billet_Inventory"
            and edge["source"]["attribute"] == "GradeID"
        )
        self.assertEqual("XStudio_XBatch", billet_grade["target"]["database"])
        self.assertEqual("XBatch_Material_Grade_Mst_Tbl", billet_grade["target"]["object"])
        self.assertEqual("ID", billet_grade["target"]["attribute"])
        self.assertEqual({"source": "Many", "target": "One"}, billet_grade["cardinality"])
        self.assertEqual("xstudio_configuration_relationship", billet_grade["provenance"]["kind"])

    def test_relationship_ids_are_stable_and_duplicate_rows_collapse(self):
        row = {
            "source_database": "XStudio_XBatch", "source_object": "Child",
            "source_attribute": "ParentID", "target_database": "XStudio_XBatch",
            "target_object": "Parent", "target_attribute": "ID",
            "source_cardinality": "Many", "target_cardinality": "One",
            "relation_name": "ParentID-Parent", "source_row_id": "row-1",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "relationships.json"
            path.write_text(json.dumps({"relationships": [row, {**row, "source_row_id": "row-2"}]}), encoding="utf-8")
            loaded = load_relationships(path)
        self.assertEqual(1, len(loaded))
        self.assertEqual(2, loaded[0]["provenance"]["source_row_count"])
        self.assertEqual("rel_211e1a88b22af1f6", loaded[0]["id"])

    def test_relationship_loader_rejects_missing_endpoints(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "relationships.json"
            path.write_text(json.dumps({"relationships": [{"source_object": "Child"}]}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing required fields"):
                load_relationships(path)

    def test_exporter_normalizes_boolean_trust_server_certificate(self):
        self.assertEqual("yes", trust_server_certificate_value("true"))
        self.assertEqual("yes", trust_server_certificate_value("1"))
        self.assertEqual("no", trust_server_certificate_value("false"))

    def test_atlas_contains_route_domains_and_validated_recipes(self):
        self.assertEqual(10, len(self.atlas["domains"]))
        self.assertEqual(10, len(self.atlas["recipes"]))
        self.assertEqual("xbatch.sap-posting.v1", self.atlas["domains"]["sap_posting"]["recipe_id"])


if __name__ == "__main__":
    unittest.main()
