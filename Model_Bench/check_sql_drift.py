#!/usr/bin/env python3
"""Read-only: fail if a live Hermes procedure/function/view differs from its numbered source.

Why: on 2026-09-21 an older build of 50_response_and_workflow.sql was applied live.
Hermes_Log_Agent_Trace_Usp lost @TraceEventID/@EventOnIst, every trace drain failed
on its first insert, and no worker tool call reached SQL for 27 hours. Comments and
whitespace are ignored; any other difference is drift. Redeploy the named source with
Model_Bench/deploy_sql_file.py.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import pyodbc

from deploy_sql_file import batches

KNOWLEDGE = Path(__file__).resolve().parent.parent / "Knowledge"
# Install order (AGENTS.md §14); a later file's definition wins, as in the bundle.
SOURCES = (
    "10_helpdesk_discovery.sql", "20_ticket_dispatch.sql", "25_ticket_dispatch_hardening.sql",
    "30_context_and_live_discovery.sql", "40_investigation_runtime.sql",
    "50_response_and_workflow.sql", "55_update_retry_hardening.sql", "60_metrics_and_reporting.sql",
    "65_xbatch_diagnostics.sql",
)
_HEADER = re.compile(r"CREATE\s+(?:OR\s+ALTER\s+)?(?:PROCEDURE|PROC|FUNCTION|VIEW)\s+(?:dbo\.)?\[?(\w+)\]?", re.I)


def normalized_body(sql: str) -> str:
    """Definition text after the object name, without comments or whitespace differences."""
    sql = re.sub(r"/\*.*?\*/", " ", sql, flags=re.S)
    sql = re.sub(r"--[^\n]*", " ", sql)
    match = _HEADER.search(sql)
    return re.sub(r"\s+", " ", sql[match.end():] if match else sql).strip().lower()


def source_objects() -> dict[str, tuple[str, str]]:
    objects: dict[str, tuple[str, str]] = {}
    for name in SOURCES:
        for batch in batches((KNOWLEDGE / name).read_text(encoding="utf-8-sig")):
            match = _HEADER.search(re.sub(r"/\*.*?\*/|--[^\n]*", " ", batch, flags=re.S))
            if match:
                objects[match.group(1)] = (name, batch)
    return objects


def drifted(cursor, objects: dict[str, tuple[str, str]]) -> list[str]:
    problems = []
    for obj, (source, body) in sorted(objects.items()):
        cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID(?))", f"dbo.{obj}")
        live = cursor.fetchone()[0]
        if live is None:
            problems.append(f"{obj}: missing live (source {source})")
        elif normalized_body(live) != normalized_body(body):
            problems.append(f"{obj}: live differs from {source}")
    return problems


def main() -> int:
    cs = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.environ.get('MSSQL_MCP_SERVER', '10.2.6.204')};DATABASE=XStudio_Helpdesk;"
        f"UID={os.environ.get('MSSQL_MCP_USER', 'sa')};PWD={os.environ['MSSQL_MCP_PASSWORD']};"
        "TrustServerCertificate=yes;Connection Timeout=60"
    )
    objects = source_objects()
    problems = drifted(pyodbc.connect(cs).cursor(), objects)
    for problem in problems:
        print(f"DRIFT: {problem}")
    print(f"{len(objects)} source objects checked; {len(problems)} drifted")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
