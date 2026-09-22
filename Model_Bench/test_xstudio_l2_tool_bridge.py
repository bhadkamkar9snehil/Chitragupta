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


if __name__ == "__main__":
    unittest.main()
