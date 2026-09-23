#!/usr/bin/env python3
"""Contract tests for probe_related_table() -- the relationship-hop
counterpart to probe_table(). Same safety primitives (schema-checked
columns, mechanically-built SQL, escaped values), but the filter is
supplied explicitly instead of guessed from ticket text.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import xstudio_l2_tool_bridge as bridge


class ProbeRelatedTableTests(unittest.TestCase):
    def _allowlist(self):
        return {
            "XStudio_Xbatch": {
                "dbo.Grade_Master": ["ID", "GradeName", "Spec"],
            }
        }

    def test_rejects_a_table_not_in_the_schema_allowlist(self):
        with patch.object(bridge, "_load_allowlist", return_value=self._allowlist()):
            result = bridge._probe_related_table(
                {"database": "XStudio_Xbatch", "table": "dbo.NotReal", "filter_column": "ID",
                 "filter_value": "1", "run_id": "r"},
                client=MagicMock(),
            )
        self.assertFalse(result["ok"])
        self.assertIn("not present in the schema allowlist", result["error"])

    def test_rejects_a_column_not_real_on_the_table(self):
        with patch.object(bridge, "_load_allowlist", return_value=self._allowlist()):
            result = bridge._probe_related_table(
                {"database": "XStudio_Xbatch", "table": "dbo.Grade_Master", "filter_column": "GuessedColumn",
                 "filter_value": "1", "run_id": "r"},
                client=MagicMock(),
            )
        self.assertFalse(result["ok"])
        self.assertIn("is not a real column on", result["error"])

    def test_valid_hop_builds_a_mechanically_safe_query_and_returns_rows(self):
        fake_orch = MagicMock()
        fake_orch.build_query_mechanically.return_value = {"ok": True, "sql": "SELECT ... WHERE [GradeName] = N'S355'"}
        client = MagicMock()
        # One audited execution returns the action ID with the rows.
        client.execute_readonly_sql_with_rows.return_value = ("ACT-1", [{"ID": "1", "GradeName": "S355"}])
        with patch.object(bridge, "_load_allowlist", return_value=self._allowlist()), \
             patch.object(bridge, "_orchestrator", return_value=fake_orch):
            result = bridge._probe_related_table(
                {"database": "XStudio_Xbatch", "table": "dbo.Grade_Master", "filter_column": "GradeName",
                 "filter_value": "S355", "run_id": "r"},
                client=client,
            )
        self.assertEqual(result["action_id"], "ACT-1")
        client.update_sql_action_evidence.assert_called_once()
        self.assertTrue(result["ok"])
        self.assertEqual(result["operation"], "probe_related_table")
        self.assertEqual(result["identifier"], {"column": "GradeName", "value": "S355"})
        self.assertEqual(len(result["rows"]), 1)
        where_arg = fake_orch.build_query_mechanically.call_args.kwargs["where"]
        self.assertIn("[GradeName]", where_arg)
        self.assertIn("N'S355'", where_arg)

    def test_registered_as_a_connected_operation(self):
        self.assertIn("probe_related_table", bridge._CONNECTED_OPERATIONS)


class ClosestTableTests(unittest.TestCase):
    ALLOWLIST = {"XStudio_Xbatch": {"dbo.XMES_CCM_Billet_Genealogy_Trn_Tbl": ["HeatNo"],
                                    "dbo.EAF_PER_HEAT": ["HeatID"], "dbo.LRF_Per_Heat": ["HeatID"]}}

    def test_unknown_table_names_the_closest_real_ones(self):
        # Live 2026-09-23 reviewer guesses.
        with patch.object(bridge, "_load_allowlist", return_value=self.ALLOWLIST):
            result = bridge._probe_table({"database": "XStudio_Xbatch", "table": "CCM_Billet_Genealogy_Trn_Tbl",
                                          "ticket": {"HeatNo": "1"}, "run_id": "r"}, MagicMock())
        self.assertFalse(result["ok"])
        self.assertEqual(result["did_you_mean"][0], "XMES_CCM_Billet_Genealogy_Trn_Tbl")


if __name__ == "__main__":
    unittest.main()
