#!/usr/bin/env python3
"""Regenerate Knowledge/schema_allowlist.json from the live databases (read-only).

The allowlist backs identifier validation in the typed xstudio_l2 tools and the
orchestrator's "did you mean" column suggestions. It needs only real object and
column names, so it reads INFORMATION_SCHEMA directly for every table and view.

This replaces two writers that drifted: a parser of the 2026-09-05 markdown schema
exports (tables only) and add_views_to_allowlist.py (views patched in). By
2026-09-23 the file was missing every Jev*/LocalModel* column and whole tables such
as Hermes_Agent_Trace_Trn_Tbl. Rerun after any schema deployment.

Usage:
    python Model_Bench/build_schema_allowlist.py
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import pyodbc

OUT_PATH = Path(__file__).resolve().parent.parent / "Knowledge" / "schema_allowlist.json"
DATABASES = ("XStudio_Helpdesk", "XStudio_Xbatch")
COLUMNS_SQL = """
SELECT c.TABLE_SCHEMA, c.TABLE_NAME, c.COLUMN_NAME, t.TABLE_TYPE
FROM INFORMATION_SCHEMA.COLUMNS c
JOIN INFORMATION_SCHEMA.TABLES t
  ON t.TABLE_SCHEMA = c.TABLE_SCHEMA AND t.TABLE_NAME = c.TABLE_NAME
WHERE t.TABLE_TYPE IN ('BASE TABLE', 'VIEW')
ORDER BY c.TABLE_SCHEMA, c.TABLE_NAME, c.ORDINAL_POSITION
"""


def live_objects(database: str) -> dict[str, list[str]]:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.environ.get('MSSQL_MCP_SERVER', '10.2.6.204')};DATABASE={database};"
        f"UID={os.environ.get('MSSQL_MCP_USER', 'sa')};PWD={os.environ['MSSQL_MCP_PASSWORD']};"
        "TrustServerCertificate=yes;Connection Timeout=60"
    )
    try:
        cur = conn.cursor()
        objects: dict[str, list[str]] = {}
        views: set[str] = set()
        for schema, table, column, table_type in cur.execute(COLUMNS_SQL).fetchall():
            objects.setdefault(f"{schema}.{table}", []).append(column)
            if table_type == "VIEW":
                views.add(f"{schema}.{table}")
        for name in sorted(views):
            if not _view_executes(cur, name):
                del objects[name]
        return objects
    finally:
        conn.close()


def _view_executes(cur, name: str) -> bool:
    """Exclude vendor views that no longer bind (10 live on 2026-09-23): Qwen spent
    19 tool calls on them. A repaired view reappears on the next regeneration."""
    schema, _, view = name.partition(".")
    try:
        cur.execute(f"SELECT TOP 0 * FROM [{schema}].[{view}]")
        while cur.nextset():
            pass
        return True
    except pyodbc.Error:
        print(f"  excluded non-executable view {name}")
        return False


def main() -> None:
    allowlist = {database: live_objects(database) for database in DATABASES}
    OUT_PATH.write_text(json.dumps(allowlist, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for database, objects in allowlist.items():
        print(f"{database}: {len(objects)} tables/views")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
