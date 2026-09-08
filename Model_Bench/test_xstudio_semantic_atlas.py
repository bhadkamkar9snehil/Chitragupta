import unittest

from Model_Bench.build_xstudio_semantic_atlas import build


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


if __name__ == "__main__":
    unittest.main()
