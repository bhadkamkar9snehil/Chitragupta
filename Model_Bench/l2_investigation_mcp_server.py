#!/usr/bin/env python3
"""Conductor L2 investigation MCP surface.

The normal table-read path is deliberately split by responsibility:

  Chitragupta / Conductor
      chooses what evidence it needs and owns ticket/run audit state
             |
             v
  XS Builder `compile-read-query`
      live-discovers the requested table and validates every projected,
      filter and ordering column; compiles a bounded SELECT from structured
      intent (no raw WHERE / ORDER BY supplied by the model)
             |
             v
  Chitragupta Hermes_L2_Execute_SQL_Usp
      executes that SELECT ONCE and records it against the active RunID

The investigation boundary is intentionally only XStudio_Helpdesk and
XStudio_Xbatch. XS Builder itself remains generic; this MCP does not.

`execute_sql` remains as a read-only escape hatch for JOINs/aggregates that the
single-table structured compiler cannot express. It is not the default path.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from Hermes_Orchestrator import (  # noqa: E402
    HermesL2Client,
    suggest_tables_mechanically,
)
from xsbuilder_query_bridge import (  # noqa: E402
    ALLOWED_DATABASES,
    compile_read_query,
)
from mcp.server.fastmcp import FastMCP  # noqa: E402

SERVER = os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
USERNAME = os.environ.get("MSSQL_MCP_USER", "sa")
PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")
HELPDESK_DATABASE = "XStudio_Helpdesk"
XBATCH_DATABASE = "XStudio_Xbatch"

mcp = FastMCP("l2-investigation")
_client: Optional[HermesL2Client] = None

_WRITE_KEYWORDS = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE|EXEC|EXECUTE|MERGE|CREATE|GRANT|REVOKE|DENY)\b",
    re.IGNORECASE,
)


def _get_client() -> HermesL2Client:
    global _client
    if _client is None:
        _client = HermesL2Client(
            server=SERVER,
            database=HELPDESK_DATABASE,
            username=USERNAME,
            password=PASSWORD,
        )
    return _client


def _allowed_database(database: str) -> str:
    for allowed in ALLOWED_DATABASES:
        if (database or "").lower() == allowed.lower():
            return allowed
    raise ValueError(
        f"Database '{database}' is outside this investigator's boundary. "
        f"Allowed: {', '.join(sorted(ALLOWED_DATABASES))}."
    )


def _rows(cursor) -> list[dict[str, Any]]:
    if not cursor.description:
        return []
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def _execute_read_once(
    sql: str,
    *,
    database: str,
    run_id: Optional[str],
    schema_name: Optional[str] = None,
    object_name: Optional[str] = None,
    operation_name: str = "mcp_read",
    purpose: str = "Investigation read",
    parameters_json: Optional[Any] = None,
) -> list[dict[str, Any]]:
    """Execute one read exactly once.

    With a RunID, the SELECT runs *inside* Hermes_L2_Execute_SQL_Usp so the
    same execution is also the durable SQL-action audit record. This avoids
    the old run_readonly_query behavior where an audited SELECT was first run
    by the logging SP and then run a second time directly merely to obtain rows.
    """
    canonical_database = _allowed_database(database)
    query_without_literals = re.sub(r"'(?:[^']|'')*'", "''", sql)
    if _WRITE_KEYWORDS.search(query_without_literals):
        raise ValueError("Investigation query must be read-only SELECT/CTE SQL.")

    client = _get_client()
    cur = client.conn.cursor()

    if not run_id:
        cur.execute(sql)
        return _rows(cur)

    cur.execute(
        """
        DECLARE @ActionIDOut varchar(36);
        EXEC dbo.Hermes_L2_Execute_SQL_Usp
            @RunID = ?, @DatabaseName = ?, @ActionType = 'READ',
            @SchemaName = ?, @ObjectName = ?, @OperationName = ?,
            @Purpose = ?, @Sql = ?, @ParametersJson = ?, @BeforeJson = NULL,
            @UseTransaction = 0, @HermesUserID = NULL,
            @ActionID = @ActionIDOut OUTPUT;
        SELECT @ActionIDOut AS ActionID;
        """,
        (
            run_id,
            canonical_database,
            schema_name,
            object_name,
            operation_name,
            purpose,
            sql,
            json.dumps(parameters_json) if parameters_json is not None else None,
        ),
    )

    # The first result set is the SELECT emitted by @Sql. The procedure's
    # HermesActionStatus and the wrapper's ActionID result sets follow it.
    result_rows: Optional[list[dict[str, Any]]] = None
    while True:
        if cur.description and result_rows is None:
            result_rows = _rows(cur)
        elif cur.description:
            cur.fetchall()  # drain audit/status result sets
        if not cur.nextset():
            break
    client.conn.commit()
    return result_rows or []


@mcp.tool()
def suggest_tables(text: str, top: int = 8) -> dict:
    """Rank likely tables/views, restricted to Helpdesk + Xbatch.

    This is retrieval/routing only. A candidate is not trusted as real query
    input until `query_table` asks XS Builder to live-discover its contract.
    """
    top = max(1, min(int(top), 20))
    candidates: list[dict[str, Any]] = []
    for database in (HELPDESK_DATABASE, XBATCH_DATABASE):
        result = suggest_tables_mechanically(text, top=top, database=database)
        candidates.extend(result.get("candidates") or [])
    candidates.sort(key=lambda item: item.get("score", 0), reverse=True)
    return {"ok": True, "candidates": candidates[:top]}


@mcp.tool()
def query_table(
    database: str,
    table: str,
    columns: list[str],
    filters: Optional[list[dict[str, Any]]] = None,
    order_by: Optional[list[dict[str, Any]]] = None,
    top: int = 100,
    run_id: Optional[str] = None,
    schema: str = "dbo",
) -> dict:
    """DEFAULT data-reading tool.

    Provide structured intent, never SQL text:
      filters: [{"column":"Status","operator":"eq","value":"Pending"}]
      order_by: [{"column":"CreatedOn","direction":"DESC"}]

    XS Builder live-discovers the exact table/columns and compiles the SELECT.
    Unknown columns, unsupported operators, raw WHERE SQL, and raw ORDER BY SQL
    therefore cannot reach execution. Pass this ticket's run_id so the read is
    recorded in Hermes_L2_SQL_Action_Trn_Tbl.
    """
    canonical_database = _allowed_database(database)
    request_evidence = {
        "database": canonical_database,
        "schema": schema,
        "table": table,
        "columns": columns,
        "filters": filters or [],
        "order_by": order_by or [],
        "top": top,
    }
    compiled = compile_read_query(
        database=canonical_database,
        schema=schema,
        table=table,
        columns=columns,
        filters=filters,
        order_by=order_by,
        top=top,
    )
    rows = _execute_read_once(
        compiled["sql"],
        database=canonical_database,
        run_id=run_id,
        schema_name=schema,
        object_name=table,
        operation_name="xsbuilder_query_table",
        purpose="XS Builder live-validated structured investigation read",
        parameters_json=request_evidence,
    )
    return {
        "ok": True,
        "database": compiled["database"],
        "schema": compiled["schema"],
        "table": compiled["table"],
        "columns": compiled["columns"],
        "sql": compiled["sql"],
        "rows": rows,
    }


@mcp.tool()
def find_sql_objects(search_term: str, database: str = XBATCH_DATABASE) -> Any:
    """Search procedures/views/triggers/tables in one of the two allowed DBs."""
    canonical_database = _allowed_database(database)
    return _get_client().find_sql_objects(canonical_database, search_term)


@mcp.tool()
def get_sql_object_definition(
    object_name: str,
    database: str = XBATCH_DATABASE,
    schema: str = "dbo",
) -> Any:
    """Inspect one real SQL object's live metadata/definition in an allowed DB."""
    canonical_database = _allowed_database(database)
    return _get_client().get_sql_object_definition(canonical_database, schema, object_name)


@mcp.tool()
def search_solutions(route: str, top: int = 5) -> Any:
    """Read approved/active Helpdesk solution articles for an exact route."""
    top = max(1, min(int(top), 20))
    cur = _get_client().conn.cursor()
    cur.execute(
        "SELECT TOP (?) ID, Title, ProblemSummary, RootCause, ResolutionSteps, UsageCount "
        "FROM dbo.Hermes_Solution_Article_Mst_Tbl "
        "WHERE Route = ? AND IsActive = 1 AND IsDeleted = 0 ORDER BY UsageCount DESC",
        (top, route),
    )
    return _rows(cur)


@mcp.tool()
def execute_sql(sql: str, database: str = XBATCH_DATABASE, run_id: Optional[str] = None) -> Any:
    """READ-ONLY escape hatch for JOINs/aggregates `query_table` cannot express.

    Only XStudio_Helpdesk and XStudio_Xbatch are accepted. Use query_table for
    ordinary reads because it validates every identifier against live schema.
    Before using this escape hatch, discover the actual objects/columns; never
    invent identifiers.
    """
    canonical_database = _allowed_database(database)
    return _execute_read_once(
        sql,
        database=canonical_database,
        run_id=run_id,
        operation_name="mcp_execute_sql_fallback",
        purpose="Read-only investigation JOIN/aggregate not expressible by query_table",
    )


def _self_test() -> None:
    # Does not require XS Builder; confirms the retrieval side is limited to
    # the intended two-database catalogue.
    print(json.dumps(suggest_tables("SAP posting failed for heat batch", top=3), indent=2))


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        _self_test()
    else:
        mcp.run(transport="stdio")
