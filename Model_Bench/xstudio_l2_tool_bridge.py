#!/usr/bin/env python3
"""Guarded SQL bridge for the xstudio_l2 Hermes plugin.

A JSON request arrives on stdin; a bounded JSON response leaves on stdout.

This file is the only L2 worker-facing place that knows how to import the
pyodbc-backed Hermes_Orchestrator module. Keeping that knowledge here
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

    Deliberately not a module-level import. Its pure guard logic --
    read-only checking, the procedure allowlist, response bounding -- is also
    exercised without a live database dependency. A lazy import keeps those
    testable and turns a missing driver into
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

# Curated, read-only heat surfaces used by the deterministic resolver. The
# worker can ask for one resolver call instead of spending several turns
# guessing whether a ticket's H-prefixed identifier maps to a numeric key.
HEAT_RESOLUTION_SURFACES: tuple[tuple[str, tuple[str, ...], tuple[str, ...]], ...] = (
    ("dbo.XMES_CCM_Billet_Genealogy_Trn_Tbl", ("HeatNo", "StrandNo"), ("HeatNo",)),
    ("dbo.XStudio_List_XMES_CCM_Billet_Genealogy_Trn_Tbl_Vw", ("HeatNo", "StrandNo"), ("HeatNo",)),
    ("dbo.CCM_Per_Heat", ("HeatID", "Strand1BilletCounter", "Strand2BilletCounter",
                           "Strand3BilletCounter", "Strand4BilletCounter",
                           "Strand5BilletCounter", "Strand6BilletCounter"), ("HeatID",)),
    ("dbo.XStudio_List_CCM_Per_Heat_Vw", ("HeatNo", "HeatID", "Strand1BilletCounter",
                                            "Strand2BilletCounter", "Strand3BilletCounter",
                                            "Strand4BilletCounter", "Strand5BilletCounter",
                                            "Strand6BilletCounter"), ("HeatNo", "HeatID")),
)

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
    "transactionid", "billetno", "materialdocument", "workordernumber", "heatno", "batchno",
    "workorderno", "workorder",
    "productionorder", "orderno", "recipeid", "recipeno",
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


def _closest_tables(database: str, table: str, limit: int = 5) -> list[str]:
    """Real allowlisted tables whose names are closest to a guessed one."""
    import difflib
    names = [q.split(".")[-1].strip("[]") for q in (_load_allowlist().get(database) or {})]
    guess = table.split(".")[-1].strip("[]")
    lowered = {n.lower(): n for n in names}
    matches = difflib.get_close_matches(guess.lower(), list(lowered), n=limit, cutoff=0.5)
    return [lowered[m] for m in matches]


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
            return lookup[identifier], scalars[identifier].rstrip(".,;:/-")

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
            return column, match.group(1).rstrip(".,;:/-")
    return None


# Audit/sync plumbing present on every XStudio table; never evidence for a ticket.
_PROBE_EXCLUDED = {
    "id", "name", "parentid", "createdby", "modifiedby", "createdon", "isdeleted", "issystem",
    "assigneduserid", "hostaddress", "dbsyncstatus", "mobilesyncstatus", "source",
}
# Ticket prose names chemistry elements; the columns use symbols.
_TERM_ALIASES = {
    "carbon": "c", "silicon": "si", "manganese": "mn", "sulphur": "s", "sulfur": "s",
    "phosphorus": "p", "chromium": "cr", "nickel": "ni", "copper": "cu", "aluminium": "al",
    "aluminum": "al", "nitrogen": "n2ppm", "vanadium": "v", "niobium": "nb", "boron": "b",
}
_PROBE_COLUMN_LIMIT = 16


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(text).lower())


def _ticket_terms(ticket_text: str) -> set[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_]*", ticket_text or "")
    terms = {_norm(w) for w in words}
    terms |= {_TERM_ALIASES[t] for t in terms if t in _TERM_ALIASES}
    # Adjacent word pairs catch "Power-On time" -> "poweron", "Cut start time" -> "cutstart".
    lowered = [w.lower() for w in words]
    terms |= {_norm(x + y) for x, y in zip(lowered, lowered[1:])}
    return {t for t in terms if t}


def _probe_columns(filter_column: str, real_columns: list[str], requested: list[Any],
                   ticket_text: str = "") -> list[str]:
    """Columns for an identifier probe, chosen by the harness, never by the model."""
    usable = [c for c in real_columns if _norm(c) not in _PROBE_EXCLUDED]
    lookup = {_norm(c): c for c in usable}
    terms = _ticket_terms(ticket_text)
    identifiers = set(_IDENTIFIER_PRIORITY) | {"billetno", "strandno", "sampletype", "grade"}
    ranked = [filter_column]
    ranked += [lookup[_norm(r)] for r in requested if _norm(r) in lookup]
    ranked += [c for c in usable if _norm(c) in terms]                        # named exactly
    ranked += [c for c in usable if len(_norm(c)) >= 5
               and any(_norm(c).startswith(t) for t in terms if len(t) >= 5)]  # "arcing" -> ArcingTime
    ranked += [c for c in usable if any(len(t) >= 10 and t in _norm(c) for t in terms)]
    ranked += [c for c in usable if _norm(c) in identifiers]
    ranked += [c for c in usable if any(w in c.lower() for w in _PROBE_COLUMN_WORDS)]
    columns: list[str] = []
    for column in ranked:
        if column not in columns:
            columns.append(column)
    return columns[:_PROBE_COLUMN_LIMIT]


def _audited_probe_read(client: Any, *, run_id: str, database: str, table: str, sql: str,
                        operation: str, filter_column: str, filter_value: str) -> tuple[list[dict[str, Any]], str | None]:
    """One audited read: the audit SP executes the SELECT once and returns rows + action ID.

    run_readonly_query ran every probe twice (an audit row with no result, then a raw
    read) and dropped the action ID, so probe evidence could never back a VERIFIED claim.
    """
    action_id, rows = client.execute_readonly_sql_with_rows(
        run_id=run_id, database_name=database, sql=sql, schema_name="dbo",
        object_name=table.split(".")[-1], operation_name=operation,
        purpose=f"Ticket probe of {table} by {filter_column}",
        parameters_json={filter_column: filter_value},
    )
    rows = rows[:MAX_LIST_ITEMS]
    if action_id:
        client.update_sql_action_evidence(action_id, after_json=rows)
    return rows, action_id


def _probe_table(req: dict[str, Any], client: Any) -> dict[str, Any]:
    """Probe one allowlisted table by one strong ticket identifier."""
    database = str(_database(req))
    table = str(_require(req, "table")).strip()
    # Harness probes pass the ticket; the worker tool passes only ticket_id.
    ticket = req.get("ticket") or client.get_ticket_context(str(_require(req, "ticket_id")))
    if not isinstance(ticket, dict):
        raise ValueError("ticket must be an object")

    resolved = _allowed_table(database, table)
    if resolved is None:
        # Live 2026-09-24: MES_SAP_Production_Trn_Tbl was refused because the caller named
        # XStudio_Helpdesk. A table that lives in exactly one other allowed database is read there.
        homes = [db for db in sorted(ALLOWED_DATABASES) if db != database and _allowed_table(db, table)]
        if len(homes) == 1:
            database = homes[0]
            resolved = _allowed_table(database, table)
    if resolved is None:
        # Live 2026-09-23: reviewers guessed Heat_Master, CCM_Billet_Genealogy_Trn_Tbl, ... and spent
        # their call budget on misses. Name the real tables closest to the guess.
        return {
            "ok": False,
            "operation": "probe_table",
            "error": f"table/view {table!r} is not present in the schema allowlist",
            "did_you_mean": _closest_tables(database, table),
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
    columns = _probe_columns(filter_column, real_columns, req.get("matched_columns") or [],
                             json.dumps(ticket, default=str))
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

    rows, action_id = _audited_probe_read(
        client, run_id=run_id, database=database, table=qualified, sql=built["sql"],
        operation="l2_probe_table", filter_column=filter_column, filter_value=filter_value,
    )
    return {
        "ok": True,
        "operation": "probe_table",
        "action_id": action_id,
        "database": database,
        "table": qualified,
        "probe_possible": True,
        "identifier": {"column": filter_column, "value": filter_value},
        "columns": columns,
        "sql": built.get("sql"),
        "rows": rows,
    }


def _probe_related_table(req: dict[str, Any], client: Any) -> dict[str, Any]:
    """Probe one allowlisted table by an EXPLICIT column/value -- the
    relationship-hop counterpart to probe_table(). Where probe_table()
    guesses the filter from ticket text, here the filter is already known
    (a real foreign-key value read off a row a prior probe already
    returned), so there is no identifier-detection step and no ticket
    argument at all. Same safety primitives, same bounded row cap, same
    schema-checked columns -- only the source of the filter differs.
    """
    database = str(_database(req))
    table = str(_require(req, "table")).strip()
    filter_column = str(_require(req, "filter_column")).strip()
    filter_value = str(_require(req, "filter_value"))
    run_id = str(_require(req, "run_id"))

    resolved = _allowed_table(database, table)
    if resolved is None:
        return {
            "ok": False,
            "operation": "probe_related_table",
            "error": f"table/view {table!r} is not present in the schema allowlist",
            "retry_same_call": False,
        }
    qualified, real_columns = resolved
    real_filter_column = next(
        (c for c in real_columns if c.lower() == filter_column.lower()), None
    )
    if real_filter_column is None:
        return {
            "ok": False,
            "operation": "probe_related_table",
            "error": f"column {filter_column!r} is not a real column on {qualified}",
            "retry_same_call": False,
        }

    columns = _probe_columns(real_filter_column, real_columns, req.get("matched_columns") or [])
    built = _orchestrator().build_query_mechanically(
        table=qualified,
        columns=columns,
        where=f"[{real_filter_column}] = N'{_escape_sql_string(filter_value)}'",
        order_by=None,
        top=_top(req, 20),
        database=database,
    )
    if not built.get("ok"):
        return {"operation": "probe_related_table", **built, "retry_same_call": False}

    rows, action_id = _audited_probe_read(
        client, run_id=run_id, database=database, table=qualified, sql=built["sql"],
        operation="l2_probe_related_table", filter_column=real_filter_column, filter_value=filter_value,
    )
    return {
        "ok": True,
        "operation": "probe_related_table",
        "action_id": action_id,
        "database": database,
        "table": qualified,
        "identifier": {"column": real_filter_column, "value": filter_value},
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
    audit_operation = procedure
    if req.get("evidence_role") == "reviewer":
        audit_operation = f"review_{procedure}"
    action_id, result = client.execute_readonly_sql_with_rows(
        run_id=run_id, database_name=database, sql=sql,
        schema_name="dbo",
        object_name=procedure,
        operation_name=audit_operation,
        purpose="Typed L2 allowlisted diagnostic procedure",
        parameters_json=parameters,
    )
    result = result[:MAX_LIST_ITEMS]
    if action_id:
        client.update_sql_action_evidence(action_id, after_json=result)
    return {"ok": True, "operation": "read_procedure", "database": database,
            "procedure": procedure, "result": result,
            "evidence_refs": [{"action_id": action_id, "operation": audit_operation}]}


def _heat_id(value: Any) -> int:
    raw = str(value).strip()
    if raw[:1].upper() == "H":
        raw = raw[1:]
    if not raw.isdigit():
        raise ValueError("heat must be a numeric heat identifier, optionally prefixed with H")
    return int(raw)


def _semantic_read(client: Any, *, run_id: str, sql: str, parameters: tuple[Any, ...],
                   operation_name: str, object_name: str, purpose: str) -> tuple[list[dict[str, Any]], dict[str, str]]:
    """Execute a reviewed fixed query and preserve a stable audited reference.

    The model supplies no SQL.  `sql` is a code-owned recipe and its live read
    uses DB-API parameters; audit text contains only normalized numeric input.
    """
    audit_sql = sql.replace("?", str(parameters[0])) if parameters else sql
    # The Helpdesk audit SP executes this fixed SELECT in XStudio_Xbatch and
    # returns both its rows and action ID.  Do not repeat it on the bridge's
    # Helpdesk connection: that was both a duplicate read and the source of
    # false "invalid object" errors against the wrong database.
    action_id, rows = client.execute_readonly_sql_with_rows(
        run_id=run_id, database_name="XStudio_Xbatch", sql=audit_sql,
        schema_name="dbo", object_name=object_name, operation_name=operation_name,
        purpose=purpose, parameters_json={"heat": parameters[0]} if parameters else {},
    )
    if action_id:
        client.update_sql_action_evidence(action_id, after_json=rows[:MAX_LIST_ITEMS])
    return rows[:MAX_LIST_ITEMS], {"action_id": action_id, "operation": operation_name}


def _semantic_text_read(client: Any, *, run_id: str, sql: str, value: str,
                        parameter_name: str, operation_name: str,
                        object_name: str, purpose: str) -> tuple[list[dict[str, Any]], dict[str, str]]:
    """Execute one fixed text-key recipe after strict identifier validation.

    The audit stored procedure accepts SQL text rather than DB-API parameters,
    so this boundary validates the tiny identifier alphabet and quotes it. The
    model can choose an identifier, but cannot influence SQL structure.
    """
    normalized = str(value).strip()
    if not re.fullmatch(r"[A-Za-z0-9_.-]{1,100}", normalized):
        raise ValueError(f"{parameter_name} must be 1-100 letters, digits, dot, dash, or underscore")
    literal = "N'" + _escape_sql_string(normalized) + "'"
    action_id, rows = client.execute_readonly_sql_with_rows(
        run_id=run_id, database_name="XStudio_Xbatch", sql=sql.replace("?", literal),
        schema_name="dbo", object_name=object_name, operation_name=operation_name,
        purpose=purpose, parameters_json={parameter_name: normalized},
    )
    bounded = rows[:MAX_LIST_ITEMS]
    if action_id:
        client.update_sql_action_evidence(action_id, after_json=bounded)
    return bounded, {"action_id": action_id, "operation": operation_name}


def _heat_context(req: dict[str, Any], client: Any) -> dict[str, Any]:
    if _database(req) != "XStudio_Xbatch":
        raise ValueError("heat_context is allowlisted only for database=XStudio_Xbatch")
    run_id = str(_require(req, "run_id"))
    heat = _heat_id(_require(req, "heat"))
    recipes = (
        ("eaf", "EAF_PER_HEAT", "l2_heat_eaf", "Canonical EAF state for heat",
         "SELECT TOP 3 HeatID, Status, StartTime, EndTime, ModifiedOn FROM dbo.EAF_PER_HEAT WHERE HeatID = ? ORDER BY ModifiedOn DESC"),
        ("lrf", "LRF_Per_Heat", "l2_heat_lrf", "Canonical LRF state for heat",
         "SELECT TOP 3 HeatID, Status, StartTime, EndTime, WorkOrder, SAPWorkflowStatus, ModifiedOn FROM dbo.LRF_Per_Heat WHERE HeatID = ? ORDER BY ModifiedOn DESC"),
        ("ccm", "CCM_Per_Heat", "l2_heat_ccm", "Canonical CCM and billet counters for heat",
         "SELECT TOP 3 HeatID, Status, StartTime, EndTime, TotalBilletsCount, TotalPostedBilletCount, Strand1BilletCounter, Strand2BilletCounter, Strand3BilletCounter, Strand4BilletCounter, Strand5BilletCounter, Strand6BilletCounter, ModifiedOn FROM dbo.CCM_Per_Heat WHERE HeatID = ? ORDER BY ModifiedOn DESC"),
        ("work_orders", "XBatch_Work_Order_Mst_Tbl", "l2_heat_work_orders", "Work orders containing heat in the CSV HeatNo allocation",
         "SELECT TOP 10 w.ID, w.WorkOrderNumber, w.HeatNo, w.Status, w.ManufacturingOrderCategory, w.MfgOrderCreationDate, w.ModifiedOn FROM dbo.XBatch_Work_Order_Mst_Tbl w CROSS APPLY STRING_SPLIT(ISNULL(w.HeatNo, ''), ',') h WHERE TRY_CONVERT(int, LTRIM(RTRIM(h.value))) = ? ORDER BY w.ModifiedOn DESC"),
        ("sap_posting", "SAP_Posting_Tbl", "l2_heat_sap_posting", "Outbound SAP posting records for heat",
         "SELECT TOP 10 ID, WorkOrderNo, HeatNo, SAP_Status, SAP_DocumentNo, SAP_Message, IsProcessed, PostingDate, PostingType, MovementType, BatchNo, Quantity, ModifiedOn FROM dbo.SAP_Posting_Tbl WHERE TRY_CONVERT(int, HeatNo) = ? ORDER BY ModifiedOn DESC"),
        ("production", "MES_SAP_Production_Trn_Tbl", "l2_heat_sap_production", "MES production transactions for heat",
         "SELECT TOP 10 ID, HeatNo, ManufacturingOrder, Batch, InspectionLot, MaterialDocument, Saptransactionid, SAPPostingStatus, QuantityInCount, BilletNo, PostingDate, ModifiedOn FROM dbo.MES_SAP_Production_Trn_Tbl WHERE HeatNo = ? ORDER BY ModifiedOn DESC"),
        ("billet_genealogy", "XStudio_List_XMES_CCM_Billet_Genealogy_Trn_Tbl_Vw", "l2_heat_billet_genealogy", "Billet and per-strand sequence evidence for heat",
         "SELECT TOP 25 ID, HeatNo, BilletNo, StrandNo, BilletSequence, StrandSequence, ChargeType, Status, CreatedOn FROM dbo.XStudio_List_XMES_CCM_Billet_Genealogy_Trn_Tbl_Vw WHERE TRY_CONVERT(int, HeatNo) = ? ORDER BY StrandNo, StrandSequence, BilletSequence"),
    )
    entities: dict[str, Any] = {}
    evidence_refs: list[dict[str, str]] = []
    operation_prefix = "review_" if req.get("evidence_role") == "reviewer" else ""
    for key, object_name, operation, purpose, sql in recipes:
        rows, ref = _semantic_read(client, run_id=run_id, sql=sql, parameters=(heat,),
                                   operation_name=operation_prefix + operation, object_name=object_name, purpose=purpose)
        entities[key] = rows
        evidence_refs.append(ref)
    return {"ok": True, "operation": "heat_context", "database": "XStudio_Xbatch",
            "normalized_identifiers": {"heat": str(heat)}, "entities": entities,
            "evidence_refs": evidence_refs,
            "claim_guidance": "Rows establish observed state only. Absence in these surfaces does not prove API or trigger causation."}


def _sap_api_context(req: dict[str, Any], client: Any) -> dict[str, Any]:
    if _database(req) != "XStudio_Xbatch":
        raise ValueError("sap_api_context is allowlisted only for database=XStudio_Xbatch")
    api_type = str(_require(req, "api_type")).strip()
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9 _-]{0,99}", api_type):
        raise ValueError("api_type must be a short API name")
    result = _read_procedure({"database": "XStudio_Xbatch", "run_id": _require(req, "run_id"),
                              "procedure": "XMES_Get_API_Transaction_Summary", "parameters": {"APIType": api_type},
                              "evidence_role": req.get("evidence_role")}, client)
    identifier = str(req.get("identifier") or "").strip()
    if identifier and result.get("ok"):
        rows = list(result.get("result") or [])
        needle = identifier.casefold()
        result["unfiltered_row_count"] = len(rows)
        result["result"] = [
            row for row in rows
            if needle in json.dumps(row, default=str, separators=(",", ":")).casefold()
        ]
    result["operation"] = "sap_api_context"
    result["normalized_identifiers"] = {"api_type": api_type, "identifier": identifier or None}
    result["claim_guidance"] = (
        "Returned rows are live API evidence. An empty identifier match within this bounded summary "
        "does not by itself prove the API was never invoked and never proves why it was absent."
    )
    return result


def _work_order_context(req: dict[str, Any], client: Any) -> dict[str, Any]:
    if _database(req) != "XStudio_Xbatch":
        raise ValueError("work_order_context is allowlisted only for database=XStudio_Xbatch")
    run_id = str(_require(req, "run_id"))
    work_order = str(_require(req, "work_order")).strip()
    campaign = str(req.get("campaign") or "").strip()
    recipes = (
        ("campaign_work_order", "XStudio_XMes_Campaign_Plan_work_order_Vw",
         "l2_work_order_campaign", "Canonical campaign/work-order projection by SAP or MES work-order number",
         "SELECT TOP 10 ID, WorkOrderNumber, MESWorkOrderNumber, CampaignNo, CampaignId, Campaign_Status, Status, Equipment, ItemName, TotalQuantity, CreatedDate FROM dbo.XStudio_XMes_Campaign_Plan_work_order_Vw WHERE WorkOrderNumber = ? OR MESWorkOrderNumber = ? ORDER BY CreatedDate DESC"),
        ("work_order_master", "XBatch_Work_Order_Mst_Tbl",
         "l2_work_order_master", "Work-order master including internal ID, external number, CSV heat allocation and SAP state",
         "SELECT TOP 10 ID, WorkOrderNumber, HeatNo, Status, SalesOrder, ManufacturingOrderCategory, SAPTransactionID, CampaignId, CreatedOn, ModifiedOn FROM dbo.XBatch_Work_Order_Mst_Tbl WHERE WorkOrderNumber = ? ORDER BY COALESCE(ModifiedOn, CreatedOn) DESC"),
    )
    entities: dict[str, Any] = {}
    evidence_refs: list[dict[str, str]] = []
    operation_prefix = "review_" if req.get("evidence_role") == "reviewer" else ""
    for key, object_name, operation, purpose, sql in recipes:
        rows, ref = _semantic_text_read(
            client, run_id=run_id, sql=sql, value=work_order,
            parameter_name="work_order", operation_name=operation_prefix + operation,
            object_name=object_name, purpose=purpose,
        )
        entities[key] = rows
        evidence_refs.append(ref)
    if campaign:
        rows, ref = _semantic_text_read(
            client, run_id=run_id,
            sql="SELECT TOP 10 ID, WorkOrderNumber, MESWorkOrderNumber, CampaignNo, CampaignId, Campaign_Status, Status, Equipment, ItemName, TotalQuantity, CreatedDate FROM dbo.XStudio_XMes_Campaign_Plan_work_order_Vw WHERE CampaignNo = ? ORDER BY CreatedDate DESC",
            value=campaign, parameter_name="campaign", operation_name=operation_prefix + "l2_campaign_work_orders",
            object_name="XStudio_XMes_Campaign_Plan_work_order_Vw",
            purpose="Canonical campaign membership by external campaign number",
        )
        entities["campaign_membership"] = rows
        evidence_refs.append(ref)
    return {
        "ok": True, "operation": "work_order_context", "database": "XStudio_Xbatch",
        "normalized_identifiers": {"work_order": work_order, "campaign": campaign or None},
        "entities": entities, "evidence_refs": evidence_refs,
        "identifier_guidance": (
            "ID is the internal work-order key; WorkOrderNumber/MESWorkOrderNumber are external identifiers. "
            "HeatNo in XBatch_Work_Order_Mst_Tbl is a comma-separated allocation, not a scalar foreign key."
        ),
        "claim_guidance": "No matching row proves only absence from the checked live surfaces; it does not prove deletion, orphaning, or cause.",
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
    "probe_related_table": _probe_related_table,
    "query": _query,
    "get_ticket_context": _get_ticket_context,
    "get_run_actions": _get_run_actions,
    "save_ledger": _save_ledger,
    "heat_context": _heat_context,
    "sap_api_context": _sap_api_context,
    "work_order_context": _work_order_context,
}


def dispatch(req: dict[str, Any]) -> dict[str, Any]:
    operation = str(_require(req, "operation"))
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
    try:  # local call trace (Model_Bench/l2_calltrace.py); L2_CALLTRACE=0 disables
        import l2_calltrace
        l2_calltrace.install()
    except ImportError:
        pass
    raise SystemExit(main())
