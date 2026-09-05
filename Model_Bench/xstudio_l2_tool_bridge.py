#!/usr/bin/env python3
"""Windows-side bridge for the xstudio_l2 Hermes plugin.

A JSON request arrives on stdin; a bounded JSON response leaves on stdout.

This file is the only L2 worker-facing place that knows how to import the
Windows pyodbc-backed Hermes_Orchestrator module. Keeping that knowledge here
is the whole point: the model never composes an interpreter path, a driver
import, a credential, or a connection string, so it cannot repeat the
Ticket_424 failure of trying to build that transport itself.

Safety properties enforced here (not merely documented):
  * `query` is read-only -- write/DDL/EXEC keywords are rejected, and the check
    runs after string literals are blanked so a keyword inside quoted text is
    not a false positive.
  * `read_procedure` cannot execute a model-supplied procedure name; only the
    explicit SAFE_READ_PROCEDURES allowlist, with an exact parameter contract.
  * every response is size/row bounded so one broad read cannot eat the
    worker's context window.
  * credentials are read from the environment and never echoed back.
"""
from __future__ import annotations

import difflib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _orchestrator():
    """Import the guarded orchestrator primitives lazily.

    Deliberately not a module-level import. This file runs under the Windows
    interpreter (the only one with pyodbc), but its pure guard logic --
    read-only checking, the procedure allowlist, response bounding -- is also
    exercised by the WSL-side contract tests, where pyodbc does not exist by
    design. A lazy import keeps those testable and turns a missing driver into
    a clean JSON error instead of an import traceback.
    """
    import Hermes_Orchestrator  # noqa: PLC0415

    return Hermes_Orchestrator


DEFAULT_SERVER = "10.2.6.204"
DEFAULT_USER = "sa"
HELPDESK_DB = "XStudio_Helpdesk"
ALLOWED_DATABASES = {"XStudio_Helpdesk", "XStudio_Xbatch", "XStudio_Configuration_Xbatch"}
SCHEMA_ALLOWLIST = REPO_ROOT / "Knowledge" / "schema_allowlist.json"

# Bounds sized against the worker's 65.6K context: a single tool result must
# never be able to consume a meaningful fraction of it.
MAX_RESPONSE_CHARS = 8000
MAX_LIST_ITEMS = 25
MAX_STRING_CHARS = 6000

# Diagnostic procedures the agent may run, with their exact parameter contract.
# Adding an entry here is a deliberate review decision: it grants EXEC on that
# one procedure and nothing else.
SAFE_READ_PROCEDURES: dict[str, set[str]] = {
    "XMES_Get_API_Transaction_Summary": {"APIType"},
}

_WRITE_OR_EXEC = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE|EXEC|EXECUTE|MERGE|CREATE|GRANT|REVOKE|DENY)\b",
    re.IGNORECASE,
)

# Blanks out '...' literals (including '' escapes) so that a row value such as
# 'no update available' does not read as an UPDATE statement.
_SQL_STRING_LITERAL = re.compile(r"'(?:[^']|'')*'")


def is_read_only_sql(sql: str) -> bool:
    """True when the statement carries no write/DDL/EXEC keyword outside literals."""
    return not _WRITE_OR_EXEC.search(_SQL_STRING_LITERAL.sub("''", sql or ""))


def _require(req: dict[str, Any], key: str) -> Any:
    value = req.get(key)
    if value is None or value == "" or value == []:
        raise ValueError(f"{key} is required for operation={req.get('operation')}")
    return value


def _database(req: dict[str, Any], *, required: bool = True) -> str | None:
    value = req.get("database")
    if value is None and not required:
        return None
    if not value:
        raise ValueError("database is required")
    if value not in ALLOWED_DATABASES:
        raise ValueError(f"database {value!r} is not allowed; choose one of {sorted(ALLOWED_DATABASES)}")
    return str(value)


def _top(req: dict[str, Any], default: int) -> int:
    return max(1, min(int(req.get("top") or default), 100))


def _load_allowlist() -> dict[str, Any]:
    if not SCHEMA_ALLOWLIST.exists():
        raise RuntimeError(f"schema allowlist not found: {SCHEMA_ALLOWLIST}")
    data = json.loads(SCHEMA_ALLOWLIST.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError("schema allowlist is not a JSON object")
    return data


def _validate_identifiers(req: dict[str, Any]) -> dict[str, Any]:
    database = _database(req)
    table = str(_require(req, "table")).strip()
    requested_columns = [str(x).strip() for x in (req.get("identifiers") or req.get("columns") or []) if str(x).strip()]
    tables = _load_allowlist().get(database) or {}
    if not isinstance(tables, dict):
        raise ValueError(f"database {database!r} is absent from schema allowlist")

    table_key = table.split(".")[-1].strip("[]").lower()
    matches = [(qualified, cols) for qualified, cols in tables.items()
               if qualified.split(".")[-1].strip("[]").lower() == table_key]
    if not matches:
        real_names = list(tables.keys())
        suggestions = difflib.get_close_matches(
            table_key, [n.split(".")[-1].lower() for n in real_names], n=5, cutoff=0.35)
        return {
            "ok": False,
            "operation": "validate_identifiers",
            "database": database,
            "error": f"table/view {table!r} is not present in the schema allowlist",
            "suggestions": [n for n in real_names if n.split(".")[-1].lower() in suggestions][:5],
            "retry_same_call": False,
        }

    qualified, real_columns = matches[0]
    real_lookup = {str(c).lower(): str(c) for c in real_columns}
    missing: dict[str, list[str]] = {}
    resolved: list[str] = []
    for column in requested_columns:
        real = real_lookup.get(column.strip("[]").lower())
        if real:
            resolved.append(real)
        else:
            missing[column] = difflib.get_close_matches(column, list(real_columns), n=5, cutoff=0.35)
    if missing:
        return {
            "ok": False,
            "operation": "validate_identifiers",
            "database": database,
            "table": qualified,
            "error": "one or more columns are not present in the schema allowlist",
            "missing": missing,
            "resolved": resolved,
            "retry_same_call": False,
        }
    return {"ok": True, "operation": "validate_identifiers", "database": database,
            "table": qualified, "columns": resolved}


def _client():
    return _orchestrator().HermesL2Client(
        server=os.environ.get("MSSQL_MCP_SERVER") or DEFAULT_SERVER,
        database=HELPDESK_DB,
        username=os.environ.get("MSSQL_MCP_USER") or DEFAULT_USER,
        password=os.environ.get("MSSQL_MCP_PASSWORD"),
        worker_id="HERMES_L2_TYPED_TOOL",
    )


def _escape_sql_string(value: Any) -> str:
    return str(value).replace("'", "''")


def _read_procedure(req: dict[str, Any], client: Any) -> dict[str, Any]:
    database = _database(req)
    run_id = str(_require(req, "run_id"))
    procedure = str(_require(req, "procedure"))
    parameters = req.get("parameters") or {}
    if not isinstance(parameters, dict):
        raise ValueError("parameters must be an object")

    allowed_params = SAFE_READ_PROCEDURES.get(procedure)
    if allowed_params is None:
        return {
            "ok": False,
            "operation": "read_procedure",
            "error": (f"procedure {procedure!r} is not in the explicit read-only allowlist; "
                      "use find_objects/get_definition/query instead of arbitrary EXEC"),
            "allowed_procedures": sorted(SAFE_READ_PROCEDURES),
            "retry_same_call": False,
        }
    unknown = sorted(set(parameters) - allowed_params)
    missing = sorted(allowed_params - set(parameters))
    if unknown or missing:
        return {
            "ok": False,
            "operation": "read_procedure",
            "procedure": procedure,
            "error": "procedure parameters do not match the reviewed allowlist",
            "required_parameters": sorted(allowed_params),
            "unknown_parameters": unknown,
            "missing_parameters": missing,
            "retry_same_call": False,
        }

    assignments = ", ".join(f"@{name} = N'{_escape_sql_string(parameters[name])}'" for name in sorted(allowed_params))
    sql = f"EXEC [dbo].[{procedure}] {assignments};"
    raw = client.execute_sql(
        run_id=run_id,
        database_name=database,
        action_type="READ",
        sql=sql,
        schema_name="dbo",
        object_name=procedure,
        operation_name=procedure,
        purpose="Typed L2 allowlisted diagnostic procedure",
        parameters_json=parameters,
        use_transaction=False,
    )
    try:
        result: Any = json.loads(raw) if isinstance(raw, str) else raw
    except json.JSONDecodeError:
        result = raw
    return {"ok": True, "operation": "read_procedure", "database": database,
            "procedure": procedure, "result": result}


def dispatch(req: dict[str, Any]) -> dict[str, Any]:
    operation = str(_require(req, "operation"))

    # Operations that need no live connection are handled before opening one.
    if operation == "validate_identifiers":
        return _validate_identifiers(req)
    if operation == "suggest_tables":
        database = _database(req)
        result = _orchestrator().suggest_tables_mechanically(
            str(_require(req, "search")), top=_top(req, 8), database=database)
        return {"operation": operation, **result}

    client: Any = None
    try:
        client = _client()

        if operation == "select":
            database = _database(req)
            built = _orchestrator().build_query_mechanically(
                table=str(_require(req, "table")),
                columns=[str(x) for x in _require(req, "columns")],
                where=req.get("where"), order_by=req.get("order_by"),
                top=_top(req, 20), database=database,
            )
            if not built.get("ok"):
                return {"operation": operation, **built, "retry_same_call": False}
            rows = _orchestrator().run_readonly_query(
                client, built["sql"], database=database, run_id=req.get("run_id"))
            return {"ok": True, "operation": operation, "database": database,
                    "table": built.get("table"), "sql": built.get("sql"),
                    "warning": built.get("warning") or built.get("ambiguity_warning"), "rows": rows}

        if operation == "query":
            database = _database(req)
            sql = str(_require(req, "sql")).strip()
            if not is_read_only_sql(sql):
                return {"ok": False, "operation": operation,
                        "error": ("query is read-only and cannot contain write/DDL/EXEC keywords; "
                                  "use read_procedure only for explicitly allowlisted diagnostics"),
                        "retry_same_call": False}
            rows = _orchestrator().run_readonly_query(
                client, sql, database=database, run_id=req.get("run_id"))
            return {"ok": True, "operation": operation, "database": database, "rows": rows}

        if operation == "find_objects":
            database = _database(req)
            rows = client.find_sql_objects(database_name=database,
                search_text=str(_require(req, "search")), object_type=req.get("object_type"), top_n=_top(req, 20))
            return {"ok": True, "operation": operation, "database": database, "objects": rows}

        if operation == "get_definition":
            database = _database(req)
            result = client.get_sql_object_definition(database_name=database,
                schema_name=str(req.get("schema") or "dbo"), object_name=str(_require(req, "object_name")))
            return {"ok": True, "operation": operation, "database": database, "definition": result}

        if operation == "get_ticket_context":
            return {"ok": True, "operation": operation,
                    "ticket": client.get_ticket_context(str(_require(req, "ticket_id")))}

        if operation == "get_run_actions":
            return {"ok": True, "operation": operation,
                    "actions": client.get_run_actions(str(_require(req, "run_id")))}

        if operation == "save_ledger":
            run_id = str(_require(req, "run_id"))
            ledger = _require(req, "ledger")
            if not isinstance(ledger, dict):
                raise ValueError("ledger must be an object")
            client.save_investigation_ledger(run_id, ledger)
            return {"ok": True, "operation": operation, "run_id": run_id, "saved": True}

        if operation == "read_procedure":
            return _read_procedure(req, client)

        raise ValueError(f"unsupported operation: {operation}")
    finally:
        if client is not None:
            try:
                client.close()
            except Exception:
                pass


def _compact(value: Any, depth: int = 0) -> Any:
    if depth > 6:
        return "<nested value omitted>"
    if isinstance(value, str):
        if len(value) <= MAX_STRING_CHARS:
            return value
        return value[:MAX_STRING_CHARS] + f"... [truncated {len(value) - MAX_STRING_CHARS} chars]"
    if isinstance(value, list):
        items = [_compact(v, depth + 1) for v in value[:MAX_LIST_ITEMS]]
        if len(value) > MAX_LIST_ITEMS:
            items.append({"_truncated_items": len(value) - MAX_LIST_ITEMS})
        return items
    if isinstance(value, dict):
        return {str(k): _compact(v, depth + 1) for k, v in value.items()}
    return value


def _bounded_response(result: dict[str, Any]) -> dict[str, Any]:
    compact = _compact(result)
    rendered = json.dumps(compact, default=str, separators=(",", ":"))
    if len(rendered) <= MAX_RESPONSE_CHARS:
        return compact
    return {
        "ok": bool(result.get("ok")),
        "operation": result.get("operation"),
        "truncated": True,
        "message": ("Tool output exceeded the L2 context budget. Refine the query/filter or "
                    "select fewer columns rather than repeating the same broad call."),
        "preview": rendered[:MAX_RESPONSE_CHARS - 500],
    }


def main() -> int:
    operation = None
    try:
        req = json.loads(sys.stdin.read() or "{}")
        if not isinstance(req, dict):
            raise ValueError("request must be a JSON object")
        operation = req.get("operation")
        result = _bounded_response(dispatch(req))
    except Exception as exc:
        result = {"ok": False, "operation": operation,
                  "error": f"{type(exc).__name__}: {exc}", "retry_same_call": False}
    print(json.dumps(result, default=str, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
