#!/usr/bin/env python3
"""Local stdio MCP server exposing this project's mechanical, audited
investigation primitives as tools -- built for Conductor's `investigate`
agent step (Phase 1 of the Conductor migration, see
Plans/Conductor_Migration_Plan_05092026.md), replacing the raw `terminal`
tool the old Hermes-Kanban investigator used to run sqlcmd/python
one-liners directly.

Why a wrapper instead of exposing sqlcmd/a raw SQL executor as a tool:
every one of these tools calls straight into Hermes_Orchestrator.py's
already-verified, already-audited functions (build_query_mechanically,
suggest_tables_mechanically, HermesL2Client.find_sql_objects, etc.) --
schema-validated, write-guarded, and recorded to Hermes_L2_SQL_Action_
Trn_Tbl exactly like every other investigation path in this project.
Nothing here re-implements or bypasses that; it's a thin MCP-protocol
skin so an LLM agent step can call the SAME primitives iteratively.

Tools exposed:
    suggest_tables(text, top=8)          -- schema-narrowing, no LLM
    build_query(table, columns, where=None, order_by=None, top=None,
                execute=False)            -- mechanical, schema-validated SELECT
    find_sql_objects(search_term, database=None)
    get_sql_object_definition(object_name, database=None)
    search_solutions(query, top=5)
    execute_sql(sql, database)            -- audited, NOT write-guarded (the
                                              underlying Hermes_L2_Execute_SQL_Usp
                                              records every action; use build_query
                                              for anything build_query can express,
                                              reach for this only when it can't)

Run standalone to smoke-test: python l2_investigation_mcp_server.py --self-test
Run for real (stdio, what Conductor launches):
    python l2_investigation_mcp_server.py
Credentials: same MSSQL_MCP_SERVER/MSSQL_MCP_USER/MSSQL_MCP_PASSWORD env
vars as every other script in this project.
"""
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))
from Hermes_Orchestrator import (  # noqa: E402
    HermesL2Client, build_query_mechanically, run_readonly_query, suggest_tables_mechanically,
)

from mcp.server.fastmcp import FastMCP  # noqa: E402

SERVER = os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
USERNAME = os.environ.get("MSSQL_MCP_USER", "sa")
PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")
DATABASE = "XStudio_Helpdesk"

mcp = FastMCP("l2-investigation")

_client: Optional[HermesL2Client] = None


def _get_client() -> HermesL2Client:
    """Lazy, single shared connection for the life of this server process
    (one per Conductor agent-step invocation, per stdio server lifecycle)."""
    global _client
    if _client is None:
        _client = HermesL2Client(server=SERVER, database=DATABASE, username=USERNAME, password=PASSWORD)
    return _client


@mcp.tool()
def suggest_tables(text: str, top: int = 8) -> dict:
    """Narrow the real schema down to tables/views actually relevant to
    free-text (a ticket's description/summary), via keyword overlap
    against real table/column names plus a curated domain index -- no
    LLM, no guessing. Call this FIRST, before build_query, unless you
    already know the exact table name from a prior step."""
    return suggest_tables_mechanically(text, top=top)


@mcp.tool()
def build_query(table: str, columns: list, where: Optional[str] = None,
                 order_by: Optional[str] = None, top: Optional[int] = None,
                 database: Optional[str] = None, execute: bool = False,
                 run_id: Optional[str] = None) -> dict:
    """Mechanically build (and optionally run) a SELECT against TABLE,
    validating every column name against the real live schema first. A
    hallucinated table/column name is rejected here with the closest real
    name, never silently built into SQL. Prefer this over hand-writing a
    query whenever you're not 100% certain of a column name. Pass run_id
    (this investigation's run_id) to get the read recorded to the audit
    trail; omit it for a quick lookup that doesn't need auditing."""
    result = build_query_mechanically(table=table, columns=columns, where=where,
                                       order_by=order_by, top=top, database=database)
    if not result.get("ok") or not execute:
        return result
    result["rows"] = run_readonly_query(_get_client(), result["sql"], database=result["database"], run_id=run_id)
    return result


@mcp.tool()
def find_sql_objects(search_term: str, database: Optional[str] = None) -> Any:
    """Search stored procedures/views/triggers by name or by text in their
    own definition. Use this to check whether an official stored procedure
    already covers an operation before ever considering a direct write, and
    to verify a 'this doesn't exist' claim before accepting it."""
    return _get_client().find_sql_objects(search_term, database=database)


@mcp.tool()
def get_sql_object_definition(object_name: str, database: Optional[str] = None) -> Any:
    """Fetch a specific stored procedure/view/trigger's full live definition
    text -- read the real logic before trusting what a name implies."""
    return _get_client().get_sql_object_definition(object_name, database=database)


@mcp.tool()
def search_solutions(route: str, top: int = 5) -> Any:
    """List existing Hermes_Solution_Article_Mst_Tbl entries for this exact
    Route (e.g. 'heat_execution', 'sap_posting') -- ordered by usage count.
    Exact-match on Route, not free-text search; check --get-ticket-context/
    the ticket's own ProblemCategory for the right route value. Call this
    BEFORE investigating from scratch -- a known fix may already exist."""
    cur = _get_client().conn.cursor()
    cur.execute(
        "SELECT TOP (?) ID, Title, ProblemSummary, RootCause, ResolutionSteps, UsageCount "
        "FROM dbo.Hermes_Solution_Article_Mst_Tbl "
        "WHERE Route = ? AND IsActive = 1 AND IsDeleted = 0 ORDER BY UsageCount DESC",
        (top, route),
    )
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


@mcp.tool()
def execute_sql(sql: str, database: str = DATABASE, run_id: Optional[str] = None) -> Any:
    """Run a read-only SELECT (write keywords are refused) against any
    database on this server, three-part-name it yourself if it isn't the
    default (e.g. SELECT ... FROM [XStudio_Xbatch].dbo.Table). NOT
    schema-validated like build_query -- only reach for this when
    build_query genuinely can't express what you need (a JOIN, an
    aggregate). Never invent a table/column name here; use
    suggest_tables/find_sql_objects first. Pass run_id to get the read
    recorded to the audit trail."""
    return run_readonly_query(_get_client(), sql, database=database, run_id=run_id)


def _self_test() -> None:
    print(json.dumps(suggest_tables("SAP posting failed for heat batch", top=3), indent=2))


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        _self_test()
    else:
        mcp.run(transport="stdio")
