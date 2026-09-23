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
        fake_orch.run_readonly_query.return_value = [{"ID": "1", "GradeName": "S355", "Spec": "..."}]
        with patch.object(bridge, "_load_allowlist", return_value=self._allowlist()), \
             patch.object(bridge, "_orchestrator", return_value=fake_orch):
            result = bridge._probe_related_table(
                {"database": "XStudio_Xbatch", "table": "dbo.Grade_Master", "filter_column": "GradeName",
                 "filter_value": "S355", "run_id": "r"},
                client=MagicMock(),
            )
        self.assertTrue(result["ok"])
        self.assertEqual(result["operation"], "probe_related_table")
        self.assertEqual(result["identifier"], {"column": "GradeName", "value": "S355"})
        self.assertEqual(len(result["rows"]), 1)
        where_arg = fake_orch.build_query_mechanically.call_args.kwargs["where"]
        self.assertIn("[GradeName]", where_arg)
        self.assertIn("N'S355'", where_arg)

    def test_registered_as_a_connected_operation(self):
        self.assertIn("probe_related_table", bridge._CONNECTED_OPERATIONS)


class DatabaseRoutingTests(unittest.TestCase):
    """Live 2026-09-23: Xbatch tables queried against XStudio_Helpdesk failed and burned budget."""

    ALLOWLIST = {
        "XStudio_Helpdesk": {"dbo.Complaint_Mst_Tbl": ["ID"]},
        "XStudio_Xbatch": {"dbo.EAF_PER_HEAT": ["HeatID"], "dbo.LRF_Per_Heat": ["HeatID"]},
        "XStudio_Configuration_Xbatch": {},
    }

    def _route(self, req):
        with patch.object(bridge, "_load_allowlist", return_value=self.ALLOWLIST):
            return bridge._route_database(req)

    def test_select_on_other_database_table_is_rerouted(self):
        routed = self._route({"operation": "select", "database": "XStudio_Helpdesk", "table": "dbo.EAF_PER_HEAT"})
        self.assertEqual(routed["database"], "XStudio_Xbatch")
        self.assertEqual(routed["database_rerouted_from"], "XStudio_Helpdesk")

    def test_query_joins_are_routed_only_when_every_table_lives_there(self):
        routed = self._route({"operation": "query", "database": "XStudio_Helpdesk",
                              "sql": "SELECT * FROM dbo.EAF_PER_HEAT e JOIN [dbo].[LRF_Per_Heat] l ON l.HeatID=e.HeatID"})
        self.assertEqual(routed["database"], "XStudio_Xbatch")
        mixed = {"operation": "query", "database": "XStudio_Helpdesk",
                 "sql": "SELECT * FROM EAF_PER_HEAT JOIN Complaint_Mst_Tbl ON 1=1"}
        self.assertEqual(self._route(mixed), mixed)

    def test_correct_or_unknown_database_is_left_alone(self):
        ok = {"operation": "select", "database": "XStudio_Xbatch", "table": "EAF_PER_HEAT"}
        self.assertEqual(self._route(ok), ok)
        unknown = {"operation": "select", "database": "XStudio_Helpdesk", "table": "NoSuchTable"}
        self.assertEqual(self._route(unknown), unknown)


class ColumnResolutionTests(unittest.TestCase):
    ALLOW = {"XStudio_Xbatch": {"dbo.LRF_Per_Heat": ["ID", "HeatID", "ArcingTime"]}}

    def _resolve(self, columns):
        with patch.object(bridge, "_load_allowlist", return_value=self.ALLOW):
            return bridge._resolve_columns("XStudio_Xbatch", "LRF_Per_Heat", columns)

    def test_star_or_nothing_selects_real_columns(self):
        self.assertEqual(self._resolve(["*"])[0], ["ID", "HeatID", "ArcingTime"])
        self.assertEqual(self._resolve([])[0], ["ID", "HeatID", "ArcingTime"])

    def test_guessed_columns_are_dropped_not_substituted_and_reported(self):
        cols, note = self._resolve(["heatid", "SuperHeat", "ArcingTime"])
        self.assertEqual(cols, ["HeatID", "ArcingTime"])
        self.assertEqual(note["columns_ignored"], ["SuperHeat"])
        self.assertIn("ArcingTime", note["real_columns"])

    def test_all_guesses_wrong_falls_back_to_real_columns(self):
        cols, note = self._resolve(["HeatNo"])
        self.assertEqual(cols, ["ID", "HeatID", "ArcingTime"])
        self.assertEqual(note["columns_ignored"], ["HeatNo"])

class KnownSourceHintTests(unittest.TestCase):
    def test_guessed_ticket_and_run_tables_point_to_real_sources(self):
        self.assertIn("Complaint_Mst_Tbl", bridge._known_source_hint("dbo.Tickets")["hint"])
        self.assertIn("xstudio_get_run_actions", bridge._known_source_hint("RunActivityLog")["hint"])
        self.assertEqual(bridge._known_source_hint("dbo.LRF_Per_Heat"), {})


if __name__ == "__main__":
    unittest.main()
