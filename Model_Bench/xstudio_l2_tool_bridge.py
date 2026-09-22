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
        op = req.get("operation")
        op_msg = f" for operation={op}" if op else ""
        raise ValueError(f"database is required{op_msg}")
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
    raw_identifiers = req.get("identifiers") or req.get("columns")
    if not raw_identifiers or not isinstance(raw_identifiers, list) or not any(str(x).strip() for x in raw_identifiers):
        raise ValueError("identifiers is required for operation=validate_identifiers")
    requested_columns = [str(x).strip() for x in raw_identifiers if str(x).strip()]
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


_IDENTIFIER_PRIORITY = [
    "transactionid", "heatno", "batchno", "workorderno", "workorder",
    "productionorder", "orderno", "materialdocument", "recipeid", "recipeno",
    "equipmentid", "equipment", "heatid", "batchid",
]

_PROBE_COLUMN_WORDS = (
    "status", "state", "reason", "error", "message", "date", "time",
    "actual", "set", "value", "code", "type", "name", "result", "document",
)


def _flatten_scalars(value: Any, prefix: str = "") -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            name = f"{prefix}.{key}" if prefix else str(key)
            out.extend(_flatten_scalars(child, name))
    elif isinstance(value, list):
        for i, child in enumerate(value[:20]):
            out.extend(_flatten_scalars(child, f"{prefix}[{i}]"))
    elif value is not None and not isinstance(value, (dict, list)):
        text = str(value).strip()
        if text and len(text) <= 300:
            out.append((prefix.split(".")[-1].split("[")[0], text))
    return out


def _allowed_table(database: str, table: str) -> tuple[str, list[str]] | None:
    tables = _load_allowlist().get(database) or {}
    table_key = table.split(".")[-1].strip("[]").lower()
    for qualified, columns in tables.items():
        if qualified.split(".")[-1].strip("[]").lower() == table_key:
            return qualified, [str(column) for column in columns]
    return None


def _ticket_scalar_map(ticket: dict[str, Any]) -> dict[str, str]:
    scalars: dict[str, str] = {}
    for key, value in _flatten_scalars(ticket):
        normalized = re.sub(r"[^a-z0-9]", "", key.lower())
        if normalized and normalized not in scalars:
            scalars[normalized] = value
    return scalars


def _probe_filter(ticket: dict[str, Any], columns: list[str]) -> tuple[str, str] | None:
    lookup = {column.replace("_", "").lower(): column for column in columns}
    scalars = _ticket_scalar_map(ticket)
    for identifier in _IDENTIFIER_PRIORITY:
        if identifier in lookup and identifier in scalars:
            return lookup[identifier], scalars[identifier]

    raw = json.dumps(ticket, default=str)
    for identifier in _IDENTIFIER_PRIORITY:
        column = lookup.get(identifier)
        if not column:
            continue
        match = re.search(
            rf"(?i)\b{re.escape(identifier)}\b\s*[\"'=: -]+\s*[\"']?([A-Za-z0-9_.:/-]{{2,100}})",
            raw,
        )
        if match:
            return column, match.group(1)
    return None


def _probe_columns(filter_column: str, real_columns: list[str], requested: list[Any]) -> list[str]:
    lookup = {re.sub(r"[^a-z0-9]", "", column.lower()): column for column in real_columns}
    columns = [filter_column]
    for candidate in requested:
        real = lookup.get(re.sub(r"[^a-z0-9]", "", str(candidate).lower()))
        if real and real not in columns:
            columns.append(real)
    for column in real_columns:
        lower = column.lower()
        if any(word in lower for word in _PROBE_COLUMN_WORDS) and column not in columns:
            columns.append(column)
        if len(columns) >= 12:
            break
    return columns[:12]


def _probe_table(req: dict[str, Any], client: Any) -> dict[str, Any]:
    """Probe one allowlisted table by one strong ticket identifier."""
    database = str(_database(req))
    table = str(_require(req, "table")).strip()
    ticket = _require(req, "ticket")
    if not isinstance(ticket, dict):
        raise ValueError("ticket must be an object")

    resolved = _allowed_table(database, table)
    if resolved is None:
        return {
            "ok": False,
            "operation": "probe_table",
            "error": f"table/view {table!r} is not present in the schema allowlist",
            "retry_same_call": False,
        }
    qualified, real_columns = resolved
    selected_filter = _probe_filter(ticket, real_columns)
    if selected_filter is None:
        return {
            "ok": True,
            "operation": "probe_table",
            "database": database,
            "table": qualified,
            "probe_possible": False,
            "reason": "No strong ticket identifier maps to a real column; automatic broad reads are intentionally avoided.",
            "rows": [],
        }

    run_id = str(_require(req, "run_id"))
    filter_column, filter_value = selected_filter
    columns = _probe_columns(filter_column, real_columns, req.get("matched_columns") or [])
    built = _orchestrator().build_query_mechanically(
        table=qualified,
        columns=columns,
        where=f"[{filter_column}] = N'{_escape_sql_string(filter_value)}'",
        order_by=None,
        top=_top(req, 20),
        database=database,
    )
    if not built.get("ok"):
        return {"operation": "probe_table", **built, "retry_same_call": False}

    rows = _orchestrator().run_readonly_query(
        client, built["sql"], database=database, run_id=run_id
    )
    return {
        "ok": True,
        "operation": "probe_table",
        "database": database,
        "table": qualified,
        "probe_possible": True,
        "identifier": {"column": filter_column, "value": filter_value},
        "columns": columns,
        "sql": built.get("sql"),
        "rows": rows,
    }


def _read_procedure(req: dict[str, Any], client: Any) -> dict[str, Any]:
    database = _database(req)
    run_id = str(_require(req, "run_id"))
    procedure = str(_require(req, "procedure"))
    parameters = _require(req, "parameters")
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


def _select(req: dict[str, Any], client: Any) -> dict[str, Any]:
    database = str(_database(req))
    table = str(_require(req, "table"))
    columns = [str(x) for x in _require(req, "columns")]
    run_id = str(_require(req, "run_id"))
    built = _orchestrator().build_query_mechanically(
        table=table,
        columns=columns,
        where=req.get("where"),
        order_by=req.get("order_by"),
        top=_top(req, 20),
        database=database,
    )
    if not built.get("ok"):
        return {"operation": "select", **built, "retry_same_call": False}
    rows = _orchestrator().run_readonly_query(
        client, built["sql"], database=database, run_id=run_id
    )
    return {
        "ok": True,
        "operation": "select",
        "database": database,
        "table": built.get("table"),
        "sql": built.get("sql"),
        "warning": built.get("warning") or built.get("ambiguity_warning"),
        "rows": rows,
    }


def _query(req: dict[str, Any], client: Any) -> dict[str, Any]:
    database = str(_database(req))
    sql = str(_require(req, "sql")).strip()
    run_id = str(_require(req, "run_id"))
    if not is_read_only_sql(sql):
        return {
            "ok": False,
            "operation": "query",
            "error": (
                "query is read-only and cannot contain write/DDL/EXEC keywords; "
                "use read_procedure only for explicitly allowlisted diagnostics"
            ),
            "retry_same_call": False,
        }
    rows = _orchestrator().run_readonly_query(
        client, sql, database=database, run_id=run_id
    )
    return {"ok": True, "operation": "query", "database": database, "rows": rows}


def _find_objects(req: dict[str, Any], client: Any) -> dict[str, Any]:
    database = str(_database(req))
    rows = client.find_sql_objects(
        database_name=database,
        search_text=str(_require(req, "search")),
        object_type=req.get("object_type"),
        top_n=_top(req, 20),
    )
    return {"ok": True, "operation": "find_objects", "database": database, "objects": rows}


def _get_definition(req: dict[str, Any], client: Any) -> dict[str, Any]:
    database = str(_database(req))
    result = client.get_sql_object_definition(
        database_name=database,
        schema_name=str(req.get("schema") or "dbo"),
        object_name=str(_require(req, "object_name")),
    )
    return {"ok": True, "operation": "get_definition", "database": database, "definition": result}


def _get_ticket_context(req: dict[str, Any], client: Any) -> dict[str, Any]:
    return {
        "ok": True,
        "operation": "get_ticket_context",
        "ticket": client.get_ticket_context(str(_require(req, "ticket_id"))),
    }


def _get_run_actions(req: dict[str, Any], client: Any) -> dict[str, Any]:
    return {
        "ok": True,
        "operation": "get_run_actions",
        "actions": client.get_run_actions(str(_require(req, "run_id"))),
    }


def _save_ledger(req: dict[str, Any], client: Any) -> dict[str, Any]:
    run_id = str(_require(req, "run_id"))
    ledger = _require(req, "ledger")
    if not isinstance(ledger, dict):
        raise ValueError("ledger must be an object")
    client.save_investigation_ledger(run_id, ledger)
    return {"ok": True, "operation": "save_ledger", "run_id": run_id, "saved": True}


_CONNECTED_OPERATIONS = {
    "probe_table": _probe_table,
    "select": _select,
    "query": _query,
    "find_objects": _find_objects,
    "get_definition": _get_definition,
    "get_ticket_context": _get_ticket_context,
    "get_run_actions": _get_run_actions,
    "save_ledger": _save_ledger,
    "read_procedure": _read_procedure,
}


def dispatch(req: dict[str, Any]) -> dict[str, Any]:
    operation = str(_require(req, "operation"))
    if operation == "validate_identifiers":
        return _validate_identifiers(req)
    if operation == "suggest_tables":
        database = str(_database(req))
        result = _orchestrator().suggest_tables_mechanically(
            str(_require(req, "search")), top=_top(req, 8), database=database
        )
        return {"operation": operation, **result}

    handler = _CONNECTED_OPERATIONS.get(operation)
    if handler is None:
        raise ValueError(f"unsupported operation: {operation}")

    client = _client()
    try:
        return handler(req, client)
    finally:
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
