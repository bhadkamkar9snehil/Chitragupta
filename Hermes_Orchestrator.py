#!/usr/bin/env python3
"""
Hermes L2 Investigation Orchestrator

Thin, verified Python client for the Hermes L2 SQL runtime deployed to
XStudio_Helpdesk (see Knowledge/00_Hermes_L2_FULL_INSTALL.sql and
Knowledge/deploy-hermes-sql.md).

===============================================================================
CHANGELOG
===============================================================================

Version: 3.0.0
Date: 2026-09-02
Author: LMEL MES / XStudio Support

Changes:
    v1 invented its own SQL directly against tables/columns that don't exist
    on the live server. v2 was a full rewrite into a verified thin wrapper
    around the 20 `Hermes_L2_*` stored procedures, plus a keyword-search
    "investigate()" that acted as the whole triage brain.

    v3 removes that brain. The reasoning belongs to the Hermes Agent bot
    driving this script via its own terminal tool, not a heuristic here --
    see AGENTS.md/CLAUDE.md for why. This script is now ONLY the two
    genuinely fiddly, easy-to-get-wrong primitives: atomically claiming a
    ticket (`--poll`, wraps dbo.Hermes_L2_Claim_Ticket_Usp's sp_getapplock +
    UPDLOCK + OUTPUT-param dance) and writing a response back through the
    audited path (`--publish-response`, wraps
    dbo.Hermes_L2_Publish_Response_Usp). Everything else -- what to
    investigate, which tables/SPs to look at, what SQL to run, what the
    reply should say -- is the calling bot's job, using its own terminal
    tool to run sqlcmd/python directly against the same
    `Hermes_L2_Execute_SQL_Usp` / `Hermes_L2_Find_SQL_Objects_Usp` procedures
    this class also wraps for convenience.

===============================================================================
WHAT THIS GIVES HERMES
===============================================================================

    - A real SQL connection (env-var credentials, TrustServerCertificate,
      matching every other script in this project).
    - Ticket dispatch: recover stale runs, list candidates, atomically claim
      one (dbo.Hermes_L2_Claim_Ticket_Usp uses sp_getapplock + UPDLOCK).
    - Full ticket context (dbo.Complaint_Mst_Tbl row + prior Hermes runs).
    - Live discovery: search stored procedures/views/triggers by name or by
      text in their definition (dbo.Hermes_L2_Find_SQL_Objects_Usp), fetch a
      specific object's full definition
      (dbo.Hermes_L2_Get_SQL_Object_Definition_Usp).
    - Generic SQL execution with a full audit trail: reads, existing SPs, or
      corrective writes, against any database on this server -- not
      SELECT-only (dbo.Hermes_L2_Execute_SQL_Usp). Every call is recorded in
      dbo.Hermes_L2_SQL_Action_Trn_Tbl with before/after evidence.
    - Structured response back to the ticket: resolution, question to the
      user, or L3 escalation, all of which update the ticket's real
      `Status`/`AskStatus` columns through the values discovered live by
      dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp (never hardcoded).

===============================================================================
CREDENTIALS
===============================================================================

Read from the environment, same as every other script in this project:
    MSSQL_MCP_SERVER, MSSQL_MCP_USER, MSSQL_MCP_PASSWORD
Override with --server/--username/--password if needed. Never hardcode a
password here.

===============================================================================
USAGE
===============================================================================

    python Hermes_Orchestrator.py --discover-workflow
        Print the live Status / AskStatus / messages combinations and their
        ticket counts. Run this before picking --eligible-status values.

    python Hermes_Orchestrator.py --poll --eligible-status "Enter"
        Atomically claim one eligible ticket and print its full context
        (including any structured L1 handoff fields) as JSON, then stop.
        Prints {"status": "NO_TICKETS"} or {"status": "NO_CLAIMABLE_TICKET"}
        if there's nothing to claim right now.

    python Hermes_Orchestrator.py --publish-response --run-id <RunID> \\
        --response-type UPDATE --reply-text "..." [--problem-summary "..."] \\
        [--findings "..."] [--root-cause "..."] [--resolution "..."] \\
        [--new-ticket-status "..."] [--new-ask-status "..."] [--mirror-to-support-remarks]
        Write a response for a run claimed by --poll. --response-type is one
        of QUESTION, UPDATE, RESOLUTION, L3_ESCALATION.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import pyodbc
except ImportError:
    pyodbc = None  # HermesL2Client imports it locally too; only needed here for --query error handling

_SCHEMA_ALLOWLIST_PATH = Path(__file__).parent / "Knowledge" / "schema_allowlist.json"
# Matches a plain identifier or db.schema.table / schema.table dotted form --
# deliberately conservative (letters/digits/underscore only) so it never
# mistakes a string literal or a number for a column name.
_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _load_flat_schema(database: Optional[str] = None) -> Dict[str, tuple]:
    """normalized table name (no schema/db prefix, lowercased) -> (db, qualified_name, columns).
    Same shape --query's own post-failure suggestion logic builds inline --
    factored out here so --build-query can validate BEFORE ever running
    anything, not just suggest a fix after a real SQL error comes back.

    A table name that exists in more than one database (confirmed live:
    dbo.Area_Mst_Tbl in both XStudio_Helpdesk and XStudio_Xbatch) would
    otherwise silently resolve to whichever database's entry happened to
    be inserted last. Pass `database` to disambiguate; without it, first
    match wins and is reported honestly (not silently)."""
    if not _SCHEMA_ALLOWLIST_PATH.exists():
        return {}
    allowlist = json.loads(_SCHEMA_ALLOWLIST_PATH.read_text(encoding="utf-8"))
    flat: Dict[str, tuple] = {}
    for db, tables in allowlist.items():
        if database and db.lower() != database.lower():
            continue
        for qname, cols in tables.items():
            key = qname.split(".")[-1].lower()
            if key not in flat:  # first match wins, never silently overwritten by a later db
                flat[key] = (db, qname, cols)
    return flat


def build_query_mechanically(table: str, columns: List[str], where: Optional[str] = None,
                              order_by: Optional[str] = None, top: Optional[int] = None,
                              database: Optional[str] = None) -> Dict[str, Any]:
    """Mechanically construct a SELECT against the REAL schema, validating
    every identifier against Knowledge/schema_allowlist.json before ever
    building a string -- a hallucinated table/column is rejected here,
    with a concrete correction, instead of only being caught after a real
    query fails (or, worse, never actually being run at all and just
    asserted as fact -- confirmed live 2026-09-04, a claim with zero
    matching rows in Hermes_L2_SQL_Action_Trn_Tbl). Read-only by
    construction: only ever emits a SELECT.

    Returns {"ok": True, "database": ..., "sql": ...} on success, or
    {"ok": False, "error": ..., "suggestions": [...]} with the closest
    real names on any unresolved identifier -- never partial/best-guess
    SQL.
    """
    flat = _load_flat_schema(database)
    if not flat:
        return {"ok": False, "error": "schema_allowlist.json not found or empty", "suggestions": []}

    table_key = table.split(".")[-1].strip("[]").lower()
    entry = flat.get(table_key)
    ambiguity_warning = None
    if entry and not database:
        all_dbs_flat = _load_flat_schema(None)
        dbs_with_table = [db for db, tbls in json.loads(_SCHEMA_ALLOWLIST_PATH.read_text(encoding="utf-8")).items()
                          if any(q.split(".")[-1].lower() == table_key for q in tbls)]
        if len(dbs_with_table) > 1:
            ambiguity_warning = (
                f"'{table}' exists in multiple databases {dbs_with_table} -- resolved to "
                f"{entry[0]} (first match) since --database wasn't given. Pass --database "
                f"explicitly if that's the wrong one."
            )
    if not entry:
        suggestions = difflib.get_close_matches(table_key, list(flat.keys()), n=5, cutoff=0.4)
        return {
            "ok": False,
            "error": f"Table/view '{table}' does not exist in the live schema.",
            "suggestions": [flat[s][1] for s in suggestions],
        }
    db, qualified_name, real_columns = entry
    real_columns_lower = {c.lower(): c for c in real_columns}

    def _validate_identifier(name: str) -> Optional[str]:
        """Returns the real, correctly-cased column name, or None if it
        doesn't resolve (caller reports suggestions in that case)."""
        return real_columns_lower.get(name.strip("[]").lower())

    resolved_columns = []
    bad_columns = []
    for c in columns:
        real = _validate_identifier(c)
        if real:
            resolved_columns.append(real)
        else:
            bad_columns.append(c)
    if bad_columns:
        all_suggestions = {}
        for bad in bad_columns:
            all_suggestions[bad] = difflib.get_close_matches(bad, real_columns, n=3, cutoff=0.4)
        return {
            "ok": False,
            "error": f"Column(s) {bad_columns} do not exist on {qualified_name}.",
            "suggestions": all_suggestions,
            "real_columns": real_columns,
        }

    # Best-effort identifier check inside WHERE -- catches a hallucinated
    # filter column even though the free-text clause itself isn't fully
    # parsed. Skips SQL keywords/operators and anything that isn't a bare
    # identifier token (string/number literals, quoted values).
    _SQL_KEYWORDS = {
        "and", "or", "not", "in", "is", "null", "like", "between", "exists",
        "select", "from", "where", "top", "asc", "desc", "order", "by", "as",
        "true", "false",
    }
    where_bad = []
    if where:
        tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", where)
        for tok in tokens:
            if tok.lower() in _SQL_KEYWORDS or tok.upper() in {"N"}:  # N'...' unicode literal prefix
                continue
            if not _validate_identifier(tok):
                # Only flag it if it isn't clearly a value (e.g. a status
                # string) -- heuristic: real schema identifiers are what we
                # actually know, so anything NOT matching a real column
                # here AND not a keyword is worth a warning, not a hard
                # block (free text WHERE clauses legitimately reference
                # values that happen to look like identifiers).
                where_bad.append(tok)

    select_list = ", ".join(f"[{c}]" for c in resolved_columns) if resolved_columns else "*"
    top_clause = f"TOP ({int(top)}) " if top else ""
    # Fully database-qualified (2026-09-05 fix): the connection this SQL
    # actually runs against is opened once at client-construction time and
    # never re-pointed mid-process. Emitting a bare 'dbo.Table' reference
    # meant --execute would silently run against WHATEVER database the
    # connection happened to already be on, not the database this table
    # actually lives in -- a real, previously-undetected bug (only masked
    # in prior testing by using a table that happens to exist, differently,
    # in both databases). Three-part naming makes the query correct
    # regardless of which database the connection is currently pointed at.
    db_qualified_name = f"[{db}].{qualified_name}"
    sql = f"SELECT {top_clause}{select_list} FROM {db_qualified_name}"
    if where:
        sql += f" WHERE {where}"
    if order_by:
        sql += f" ORDER BY {order_by}"

    result = {"ok": True, "database": db, "table": qualified_name, "sql": sql}
    if ambiguity_warning:
        result["ambiguity_warning"] = ambiguity_warning
    if where_bad:
        result["warning"] = (
            f"These WHERE tokens don't match a real column on {qualified_name} -- "
            f"double check they're intended as literal values, not column names: {where_bad}"
        )
    return result

# A ticket Description/reply field can carry an inline base64 image
# (<img src="data:image/png;base64,...">) pasted by a user in the source
# helpdesk UI. A real 2026-09-03 incident: one such blob was ~93,000
# characters -- dumped verbatim into an LLM agent's context by --poll, it
# alone blew past the compression budget before the agent did anything.
# Strip these before any ticket context leaves this script.
# Base64 data embedded in a JSON string can contain backslash-escaped
# sequences (\n, \", \\) breaking a plain [A-Za-z0-9+/=] run partway
# through -- allow either a base64 char or a 2-char escape, so the match
# doesn't stop early and leave the tail of the image un-stripped.
_BASE64_IMAGE_RE = re.compile(r'data:image/[a-zA-Z0-9.+-]+;base64,(?:[A-Za-z0-9+/=]|\\.){200,}')


def _strip_embedded_images(value: Any) -> Any:
    """Recursively replace inline base64 image data with a short placeholder."""
    if isinstance(value, str):
        def _replace(m: "re.Match[str]") -> str:
            return f"[embedded image removed, {len(m.group(0))} chars]"
        return _BASE64_IMAGE_RE.sub(_replace, value)
    if isinstance(value, dict):
        return {k: _strip_embedded_images(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_strip_embedded_images(v) for v in value]
    return value

try:
    import pyodbc
except ImportError:
    print("ERROR: pyodbc is required. Install with: pip install pyodbc", file=sys.stderr)
    sys.exit(1)

DEFAULT_DRIVER = "ODBC Driver 17 for SQL Server"
DEFAULT_DATABASE = "XStudio_Helpdesk"


def _rows_as_dicts(cursor) -> List[Dict[str, Any]]:
    if not cursor.description:
        return []
    cols = [c[0] for c in cursor.description]
    return [dict(zip(cols, row)) for row in cursor.fetchall()]


def _last_result_row(cursor) -> Optional[Dict[str, Any]]:
    """
    Several Hermes procs emit their own final SELECT before control returns to
    a wrapper batch that appends `SELECT @Out AS X;` -- that makes the OUTPUT
    value land in the *last* result set, not the first. Walk every result set
    and keep the last non-empty one.
    """
    row: Optional[Dict[str, Any]] = None
    rows = _rows_as_dicts(cursor)
    if rows:
        row = rows[-1]
    while cursor.nextset():
        rows = _rows_as_dicts(cursor)
        if rows:
            row = rows[-1]
    return row


class HermesL2Client:
    """
    Thin wrapper around the Hermes_L2_* stored procedures in XStudio_Helpdesk.
    Every method here maps to exactly one deployed procedure; none of them
    guess at table/column names.
    """

    def __init__(self, server: str, database: str = DEFAULT_DATABASE,
                 username: Optional[str] = None, password: Optional[str] = None,
                 driver: str = DEFAULT_DRIVER, worker_id: str = "HERMES_WORKER",
                 hermes_user_id: Optional[str] = None):
        self.worker_id = worker_id
        self.hermes_user_id = hermes_user_id
        self.conn = self._connect(server, database, username, password, driver)

    @staticmethod
    def _connect(server: str, database: str, username: Optional[str],
                 password: Optional[str], driver: str) -> "pyodbc.Connection":
        if username and password:
            cs = (
                f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};"
                f"UID={username};PWD={password};TrustServerCertificate=yes;"
            )
        else:
            cs = (
                f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};"
                f"Trusted_Connection=yes;TrustServerCertificate=yes;"
            )
        return pyodbc.connect(cs, timeout=15)

    def close(self) -> None:
        self.conn.close()

    # -- Discovery -----------------------------------------------------

    def discover_helpdesk_workflow(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp
        Multiple result sets: live Status/AskStatus/messages combinations
        with counts, priority master, complaint-type master, and any
        SPs/triggers touching Complaint_Mst_Tbl. Always run this before
        assuming a status name/value is still current -- it is a live query,
        not a stored assumption.
        """
        cur = self.conn.cursor()
        cur.execute("EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;")
        result_sets = []
        while True:
            result_sets.append(_rows_as_dicts(cur))
            if not cur.nextset():
                break
        return {
            "status_combinations": result_sets[0] if len(result_sets) > 0 else [],
            "priority_master": result_sets[1] if len(result_sets) > 1 else [],
            "complaint_type_master": result_sets[2] if len(result_sets) > 2 else [],
            "related_sql_objects": result_sets[3] if len(result_sets) > 3 else [],
        }

    def find_sql_objects(self, database_name: str, search_text: str,
                          object_type: Optional[str] = None, top_n: int = 50) -> List[Dict]:
        """EXEC dbo.Hermes_L2_Find_SQL_Objects_Usp -- search procs/views/triggers by name or definition text."""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Find_SQL_Objects_Usp "
            "@DatabaseName = ?, @SearchText = ?, @ObjectType = ?, @TopN = ?;",
            (database_name, search_text, object_type, top_n),
        )
        return _rows_as_dicts(cur)

    def get_sql_object_definition(self, database_name: str, schema_name: str,
                                   object_name: str) -> Optional[Dict]:
        """EXEC dbo.Hermes_L2_Get_SQL_Object_Definition_Usp -- full sys.sql_modules text for one object."""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Get_SQL_Object_Definition_Usp "
            "@DatabaseName = ?, @SchemaName = ?, @ObjectName = ?;",
            (database_name, schema_name, object_name),
        )
        rows = _rows_as_dicts(cur)
        return rows[0] if rows else None

    def get_reference_documents(self, search_text: str, area: Optional[str] = None,
                                 top_n: int = 10) -> List[Dict]:
        """EXEC dbo.Hermes_L2_Get_Reference_Documents_Usp"""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Get_Reference_Documents_Usp "
            "@SearchText = ?, @Area = ?, @TopN = ?;",
            (search_text, area, top_n),
        )
        return _rows_as_dicts(cur)

    # -- Ticket dispatch -------------------------------------------------

    def _find_stale_run_candidates(self, stale_minutes: int) -> List[str]:
        """Read-only mirror of Hermes_L2_Recover_Stale_Runs_Usp's own WHERE
        clause, used only to decide which run_ids to check against Kanban
        before actually recovering anything -- see recover_stale_runs."""
        cur = self.conn.cursor()
        cur.execute(
            "SELECT ID FROM dbo.Hermes_L2_Response_Trn_Tbl "
            "WHERE IsActive = 1 AND IsDeleted = 0 "
            "AND ISNULL(HeartbeatOn, ClaimedOn) < DATEADD(MINUTE, -?, GETDATE());",
            (stale_minutes,),
        )
        return [str(r[0]) for r in cur.fetchall()]

    def recover_stale_runs(self, stale_minutes: int = 60) -> int:
        """EXEC dbo.Hermes_L2_Recover_Stale_Runs_Usp -- run first in every cycle.

        Kanban-aware as of 2026-09-04: this SP is pure T-SQL with no
        visibility into Kanban, so a run whose kanban task is still
        legitimately queued (ready/blocked/running -- just backed up
        behind other work, not abandoned) used to get yanked purely on
        wall-clock elapsed time. Confirmed live: one ticket accumulated 22
        consecutive forced-FAILED-and-reclaimed cycles this way while its
        kanban task was never actually abandoned, just waiting behind a
        max_in_progress:1 dispatcher and, separately, a board that wasn't
        being dispatched at all. Before recovering anything, find the
        stale-looking candidates, ask Kanban which of them still have a
        genuinely non-terminal task tracking them, and exclude those from
        the SP's sweep -- they get left alone regardless of how long
        they've been claimed. A run with NO live kanban task at all (the
        case this SP genuinely exists for: the kanban card itself was
        never created, or Kanban has fully forgotten about it) is still
        recovered exactly as before."""
        candidates = self._find_stale_run_candidates(stale_minutes)
        exclude_run_ids = None
        if candidates:
            live_run_ids = _find_live_kanban_run_ids()
            if live_run_ids is not None:
                protected = [c for c in candidates if c in live_run_ids]
                if protected:
                    exclude_run_ids = ",".join(protected)
            # live_run_ids is None only on a Kanban-check failure -- fail
            # open to the prior blind-timeout behavior for this sweep
            # rather than silently never recovering anything.

        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Recover_Stale_Runs_Usp "
            "@StaleMinutes = ?, @HermesUserID = ?, @ExcludeRunIDs = ?;",
            (stale_minutes, self.hermes_user_id, exclude_run_ids),
        )
        row = cur.fetchone()
        self.conn.commit()
        return row.RecoveredRunCount if row else 0

    def get_candidate_tickets(self, eligible_status_csv: str, batch_size: int = 20) -> List[Dict]:
        """EXEC dbo.Hermes_L2_Get_Candidate_Tickets_Usp"""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Get_Candidate_Tickets_Usp @EligibleStatusCsv = ?, @BatchSize = ?;",
            (eligible_status_csv, batch_size),
        )
        return _rows_as_dicts(cur)

    def claim_ticket(self, ticket_id: str, eligible_status_csv: str,
                      host_address: Optional[str] = None) -> Optional[str]:
        """
        EXEC dbo.Hermes_L2_Claim_Ticket_Usp -- atomic claim (sp_getapplock + UPDLOCK).
        Returns the new RunID, or None if another worker already holds this ticket
        or it's no longer in an eligible status.
        """
        cur = self.conn.cursor()
        cur.execute(
            """
            DECLARE @RunIDOut varchar(36);
            EXEC dbo.Hermes_L2_Claim_Ticket_Usp
                @TicketID = ?,
                @EligibleStatusCsv = ?,
                @WorkerID = ?,
                @HermesUserID = ?,
                @HostAddress = ?,
                @RunID = @RunIDOut OUTPUT;
            SELECT @RunIDOut AS RunID;
            """,
            (ticket_id, eligible_status_csv, self.worker_id, self.hermes_user_id, host_address),
        )
        row = _last_result_row(cur)
        self.conn.commit()
        return row["RunID"] if row else None

    def get_ticket_context(self, ticket_id: str, history_rows: int = 10) -> Dict:
        """EXEC dbo.Hermes_L2_Get_Ticket_Context_Usp -- ticket row + prior Hermes runs."""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Get_Ticket_Context_Usp @TicketID = ?, @HistoryRows = ?;",
            (ticket_id, history_rows),
        )
        result_sets = []
        while True:
            result_sets.append(_rows_as_dicts(cur))
            if not cur.nextset():
                break
        return {
            "ticket": result_sets[0][0] if result_sets and result_sets[0] else None,
            "prior_runs": result_sets[1] if len(result_sets) > 1 else [],
        }

    def get_run(self, run_id: str) -> Optional[Dict]:
        """EXEC dbo.Hermes_L2_Get_Run_Usp"""
        cur = self.conn.cursor()
        cur.execute("EXEC dbo.Hermes_L2_Get_Run_Usp @RunID = ?;", (run_id,))
        rows = _rows_as_dicts(cur)
        return rows[0] if rows else None

    def get_run_actions(self, run_id: str) -> List[Dict]:
        """EXEC dbo.Hermes_L2_Get_Run_Actions_Usp -- SQL action audit trail for one run."""
        cur = self.conn.cursor()
        cur.execute("EXEC dbo.Hermes_L2_Get_Run_Actions_Usp @RunID = ?;", (run_id,))
        return _rows_as_dicts(cur)

    # -- Investigation runtime -------------------------------------------

    def start_investigation(self, run_id: str, route: str) -> None:
        """EXEC dbo.Hermes_L2_Start_Investigation_Usp"""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Start_Investigation_Usp @RunID = ?, @Route = ?, @HermesUserID = ?;",
            (run_id, route, self.hermes_user_id),
        )
        self.conn.commit()

    def heartbeat(self, run_id: str) -> None:
        """EXEC dbo.Hermes_L2_Heartbeat_Usp -- call periodically during long investigations."""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Heartbeat_Usp @RunID = ?, @HermesUserID = ?;",
            (run_id, self.hermes_user_id),
        )
        self.conn.commit()

    def save_investigation_state(self, run_id: str, route: Optional[str] = None,
                                  problem_summary: Optional[str] = None,
                                  findings: Optional[str] = None,
                                  root_cause: Optional[str] = None,
                                  resolution: Optional[str] = None,
                                  investigation_json: Optional[Any] = None,
                                  next_eligible_on: Optional[datetime] = None) -> None:
        """EXEC dbo.Hermes_L2_Save_Investigation_State_Usp -- checkpoint mid-investigation."""
        cur = self.conn.cursor()
        inv_json = json.dumps(investigation_json) if investigation_json is not None else None
        cur.execute(
            """
            EXEC dbo.Hermes_L2_Save_Investigation_State_Usp
                @RunID = ?, @Route = ?, @ProblemSummary = ?, @Findings = ?,
                @RootCause = ?, @Resolution = ?, @InvestigationJson = ?,
                @NextEligibleOn = ?, @HermesUserID = ?;
            """,
            (run_id, route, problem_summary, findings, root_cause, resolution,
             inv_json, next_eligible_on, self.hermes_user_id),
        )
        self.conn.commit()

    def execute_sql(self, run_id: str, database_name: str, action_type: str, sql: str,
                     schema_name: Optional[str] = None, object_name: Optional[str] = None,
                     operation_name: Optional[str] = None, purpose: Optional[str] = None,
                     parameters_json: Optional[Any] = None, before_json: Optional[Any] = None,
                     use_transaction: bool = False) -> str:
        """
        EXEC dbo.Hermes_L2_Execute_SQL_Usp -- the generic read/write capability.

        @action_type is a free-text label recorded for audit (e.g. 'READ',
        'EXEC_SP', 'UPDATE', 'INSERT', 'DDL'); it does not gate what @sql may
        do. This procedure is intentionally not SELECT-only -- see
        Knowledge/sql-write-model.md. Permissions on the SQL login used here
        are the real capability boundary.

        Returns the ActionID (audit row in Hermes_L2_SQL_Action_Trn_Tbl).
        Call update_sql_action_evidence() afterwards with the after-state.
        """
        params_json = json.dumps(parameters_json) if parameters_json is not None else None
        before_json_s = json.dumps(before_json) if before_json is not None else None
        cur = self.conn.cursor()
        cur.execute(
            """
            DECLARE @ActionIDOut varchar(36);
            EXEC dbo.Hermes_L2_Execute_SQL_Usp
                @RunID = ?, @DatabaseName = ?, @ActionType = ?, @SchemaName = ?,
                @ObjectName = ?, @OperationName = ?, @Purpose = ?, @Sql = ?,
                @ParametersJson = ?, @BeforeJson = ?, @UseTransaction = ?,
                @HermesUserID = ?, @ActionID = @ActionIDOut OUTPUT;
            SELECT @ActionIDOut AS ActionID;
            """,
            (run_id, database_name, action_type, schema_name, object_name,
             operation_name, purpose, sql, params_json, before_json_s,
             use_transaction, self.hermes_user_id),
        )
        row = _last_result_row(cur)
        self.conn.commit()
        return row["ActionID"] if row else None

    def update_sql_action_evidence(self, action_id: str, before_json: Optional[Any] = None,
                                    after_json: Optional[Any] = None) -> None:
        """EXEC dbo.Hermes_L2_Update_SQL_Action_Evidence_Usp"""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Update_SQL_Action_Evidence_Usp "
            "@ActionID = ?, @BeforeJson = ?, @AfterJson = ?, @HermesUserID = ?;",
            (action_id,
             json.dumps(before_json) if before_json is not None else None,
             json.dumps(after_json) if after_json is not None else None,
             self.hermes_user_id),
        )
        self.conn.commit()

    # -- Response / workflow ----------------------------------------------

    def publish_response(self, run_id: str, response_type: str, reply_text: str,
                          problem_summary: Optional[str] = None, findings: Optional[str] = None,
                          root_cause: Optional[str] = None, resolution: Optional[str] = None,
                          investigation_json: Optional[Any] = None,
                          new_ticket_status: Optional[str] = None,
                          new_ask_status: Optional[str] = None,
                          next_eligible_on: Optional[datetime] = None,
                          mirror_reply_to_support_remarks: bool = False,
                          mirror_question_to_ask_remarks: bool = False) -> None:
        """EXEC dbo.Hermes_L2_Publish_Response_Usp -- generic structured reply; prefer
        resolve_ticket() / ask_question() / escalate_l3() for the three normal outcomes."""
        cur = self.conn.cursor()
        inv_json = json.dumps(investigation_json) if investigation_json is not None else None
        cur.execute(
            """
            EXEC dbo.Hermes_L2_Publish_Response_Usp
                @RunID = ?, @ResponseType = ?, @ReplyText = ?, @ProblemSummary = ?,
                @Findings = ?, @RootCause = ?, @Resolution = ?, @InvestigationJson = ?,
                @NewTicketStatus = ?, @NewAskStatus = ?, @NextEligibleOn = ?,
                @MirrorReplyToSupportRemarks = ?, @MirrorQuestionToAskRemarks = ?,
                @HermesUserID = ?;
            """,
            (run_id, response_type, reply_text, problem_summary, findings, root_cause,
             resolution, inv_json, new_ticket_status, new_ask_status, next_eligible_on,
             mirror_reply_to_support_remarks, mirror_question_to_ask_remarks,
             self.hermes_user_id),
        )
        self.conn.commit()

    def ask_question(self, run_id: str, question: str, new_ticket_status: str,
                      new_ask_status: str, mirror_to_ask_remarks: bool = True) -> None:
        """EXEC dbo.Hermes_L2_Ask_Question_Usp -- Hermes needs more info from the user."""
        cur = self.conn.cursor()
        cur.execute(
            """
            EXEC dbo.Hermes_L2_Ask_Question_Usp
                @RunID = ?, @Question = ?, @NewTicketStatus = ?, @NewAskStatus = ?,
                @MirrorQuestionToAskRemarks = ?, @HermesUserID = ?;
            """,
            (run_id, question, new_ticket_status, new_ask_status,
             mirror_to_ask_remarks, self.hermes_user_id),
        )
        self.conn.commit()

    def resolve_ticket(self, run_id: str, reply_text: str, resolution: str,
                        resolved_ticket_status: str, problem_summary: Optional[str] = None,
                        findings: Optional[str] = None, root_cause: Optional[str] = None,
                        investigation_json: Optional[Any] = None,
                        mirror_to_support_remarks: bool = True) -> None:
        """EXEC dbo.Hermes_L2_Resolve_Ticket_Usp"""
        cur = self.conn.cursor()
        inv_json = json.dumps(investigation_json) if investigation_json is not None else None
        cur.execute(
            """
            EXEC dbo.Hermes_L2_Resolve_Ticket_Usp
                @RunID = ?, @ReplyText = ?, @Resolution = ?, @ResolvedTicketStatus = ?,
                @ProblemSummary = ?, @Findings = ?, @RootCause = ?, @InvestigationJson = ?,
                @MirrorToSupportRemarks = ?, @HermesUserID = ?;
            """,
            (run_id, reply_text, resolution, resolved_ticket_status, problem_summary,
             findings, root_cause, inv_json, mirror_to_support_remarks, self.hermes_user_id),
        )
        self.conn.commit()

    def escalate_l3(self, run_id: str, reply_text: str, l3_ticket_status: str,
                     problem_summary: Optional[str] = None, findings: Optional[str] = None,
                     root_cause: Optional[str] = None, investigation_json: Optional[Any] = None,
                     mirror_to_support_remarks: bool = True) -> None:
        """EXEC dbo.Hermes_L2_Escalate_L3_Usp"""
        cur = self.conn.cursor()
        inv_json = json.dumps(investigation_json) if investigation_json is not None else None
        cur.execute(
            """
            EXEC dbo.Hermes_L2_Escalate_L3_Usp
                @RunID = ?, @ReplyText = ?, @L3TicketStatus = ?, @ProblemSummary = ?,
                @Findings = ?, @RootCause = ?, @InvestigationJson = ?,
                @MirrorToSupportRemarks = ?, @HermesUserID = ?;
            """,
            (run_id, reply_text, l3_ticket_status, problem_summary, findings, root_cause,
             inv_json, mirror_to_support_remarks, self.hermes_user_id),
        )
        self.conn.commit()

    def fail_run(self, run_id: str, error_message: str, retry_after_minutes: int = 5) -> None:
        """EXEC dbo.Hermes_L2_Fail_Run_Usp"""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Fail_Run_Usp @RunID = ?, @ErrorMessage = ?, "
            "@RetryAfterMinutes = ?, @HermesUserID = ?;",
            (run_id, error_message, retry_after_minutes, self.hermes_user_id),
        )
        self.conn.commit()

    def log_blocked_escalation(self, run_id: str, ticket_id: str, block_reason: str,
                                findings: Optional[str] = None) -> None:
        """EXEC dbo.Hermes_L2_Log_Blocked_Escalation_Usp -- visibility-only human-queue
        insert, does not touch Complaint_Mst_Tbl or require an active run."""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_L2_Log_Blocked_Escalation_Usp @RunID = ?, @TicketID = ?, "
            "@BlockReason = ?, @Findings = ?, @HermesUserID = ?;",
            (run_id, ticket_id, block_reason, findings, self.hermes_user_id),
        )
        self.conn.commit()

    def log_activity(self, ticket_id: str, activity_type: str, note_text: Optional[str] = None,
                      actor_type: str = "Bot", actor_name: Optional[str] = None,
                      old_value: Optional[str] = None, new_value: Optional[str] = None,
                      is_customer_visible: bool = False, run_id: Optional[str] = None) -> None:
        """EXEC dbo.Hermes_Log_Ticket_Activity_Usp"""
        cur = self.conn.cursor()
        cur.execute(
            """
            EXEC dbo.Hermes_Log_Ticket_Activity_Usp
                @TicketID = ?, @ActivityType = ?, @ActorType = ?, @ActorName = ?,
                @NoteText = ?, @OldValue = ?, @NewValue = ?, @IsCustomerVisible = ?,
                @RunID = ?, @HermesUserID = ?;
            """,
            (ticket_id, activity_type, actor_type, actor_name, note_text, old_value,
             new_value, is_customer_visible, run_id, self.hermes_user_id),
        )
        self.conn.commit()

    def create_solution(self, title: str, resolution_steps: str, problem_summary: Optional[str] = None,
                         root_cause: Optional[str] = None, route: Optional[str] = None,
                         tags: Optional[str] = None) -> str:
        """EXEC dbo.Hermes_Create_Solution_Article_Usp -- returns new SolutionID"""
        cur = self.conn.cursor()
        cur.execute(
            """
            DECLARE @NewSolutionID varchar(36);
            EXEC dbo.Hermes_Create_Solution_Article_Usp
                @Title = ?, @ResolutionSteps = ?, @ProblemSummary = ?, @RootCause = ?,
                @Route = ?, @Tags = ?, @HermesUserID = ?, @NewSolutionID = @NewSolutionID OUTPUT;
            SELECT @NewSolutionID;
            """,
            (title, resolution_steps, problem_summary, root_cause, route, tags, self.hermes_user_id),
        )
        row = cur.fetchone()
        self.conn.commit()
        return row[0] if row else None

    def link_solution(self, ticket_id: str, solution_id: str, run_id: Optional[str] = None,
                       was_helpful: Optional[bool] = None) -> None:
        """EXEC dbo.Hermes_Link_Solution_To_Ticket_Usp"""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_Link_Solution_To_Ticket_Usp @TicketID = ?, @SolutionID = ?, "
            "@RunID = ?, @WasHelpful = ?, @HermesUserID = ?;",
            (ticket_id, solution_id, run_id, was_helpful, self.hermes_user_id),
        )
        self.conn.commit()

    def get_ticket_activity(self, ticket_id: str) -> List[Dict]:
        """EXEC dbo.Hermes_Get_Ticket_Activity_Usp -- full work-log timeline for one ticket."""
        cur = self.conn.cursor()
        cur.execute("EXEC dbo.Hermes_Get_Ticket_Activity_Usp @TicketID = ?;", (ticket_id,))
        return _rows_as_dicts(cur)

    def create_problem(self, title: str, root_cause_summary: Optional[str] = None,
                        root_cause_category_id: Optional[str] = None) -> str:
        """EXEC dbo.Hermes_Create_Problem_Usp -- returns new ProblemID"""
        cur = self.conn.cursor()
        cur.execute(
            """
            DECLARE @NewProblemID varchar(36);
            EXEC dbo.Hermes_Create_Problem_Usp
                @Title = ?, @RootCauseSummary = ?, @RootCauseCategoryID = ?,
                @HermesUserID = ?, @NewProblemID = @NewProblemID OUTPUT;
            SELECT @NewProblemID;
            """,
            (title, root_cause_summary, root_cause_category_id, self.hermes_user_id),
        )
        row = cur.fetchone()
        self.conn.commit()
        return row[0] if row else None

    def link_problem(self, problem_id: str, ticket_id: str) -> None:
        """EXEC dbo.Hermes_Link_Ticket_To_Problem_Usp"""
        cur = self.conn.cursor()
        cur.execute(
            "EXEC dbo.Hermes_Link_Ticket_To_Problem_Usp @ProblemID = ?, @TicketID = ?, @HermesUserID = ?;",
            (problem_id, ticket_id, self.hermes_user_id),
        )
        self.conn.commit()

    def list_root_cause_categories(self) -> List[Dict]:
        """Read dbo.Hermes_Root_Cause_Category_Mst_Tbl -- the controlled taxonomy."""
        cur = self.conn.cursor()
        cur.execute(
            "SELECT ID, CategoryName, Description FROM dbo.Hermes_Root_Cause_Category_Mst_Tbl "
            "WHERE IsActive = 1 AND IsDeleted = 0 ORDER BY CategoryName;"
        )
        return _rows_as_dicts(cur)


# Statuses that mean "Kanban still owns this task, leave it alone" -- see
# _find_live_kanban_run_ids and recover_stale_runs. Deliberately excludes
# 'done' and 'archived': a task that reached a terminal state without ever
# publishing is exactly the case that SHOULD still be recovered (same
# correction applied to Model_Bench/enforce_publish_safety_net.py's
# find_live_kanban_run_ids the same day, for the same confirmed bug).
_NON_TERMINAL_KANBAN_STATUSES = {"ready", "blocked", "triage", "running", "review", "scheduled"}


def _find_live_kanban_run_ids() -> Optional[set]:
    """run_ids that still have a genuinely non-terminal kanban task
    tracking them, across every board -- checked before
    Hermes_L2_Recover_Stale_Runs_Usp would otherwise force-fail a claim on
    wall-clock time alone. This script always runs as the Windows Python
    interpreter (invoked via WSL interop by its cron wrappers, or directly
    from PowerShell) and never has `hermes` on its own PATH, so the call
    is always wrapped through `wsl -d Ubuntu`, matching every other script
    in this project that needs to reach the kanban CLI from here.

    Returns None on any failure (hermes/wsl unavailable, bad JSON) so the
    caller can fail OPEN to the prior blind-timeout behavior for that
    sweep rather than silently never recovering anything.
    """
    live_run_ids: set = set()
    for board_args in (["kanban", "list", "--json"], ["kanban", "--board", "l2-review", "list", "--json"]):
        try:
            result = subprocess.run(
                ["wsl", "-d", "Ubuntu", "--", "bash", "-lc", "hermes " + " ".join(board_args)],
                capture_output=True, text=True, timeout=30,
            )
            if result.returncode != 0:
                return None
            tasks = json.loads(result.stdout)
        except Exception:
            return None

        for t in tasks:
            if t.get("status") not in _NON_TERMINAL_KANBAN_STATUSES:
                continue
            body = t.get("body") or ""
            for line in body.splitlines():
                line = line.strip()
                if line.startswith("run_id:"):
                    live_run_ids.add(line.split(":", 1)[1].strip())
                    break
    return live_run_ids


_LAST_CLAIM_STATE_PATH = Path(__file__).parent / ".hermes_l2_last_claim.json"

# Local, DB-untouched draft staging for the proposer/verifier gate -- see
# --draft-response/--approve-draft/--reject-draft. Deliberately NOT a DB
# table/column: the write-discipline requires a real stored procedure for
# any live-DB status transition, and the whole point of a draft is that it
# doesn't need one -- the ticket's ProcessStatus stays whatever --poll left
# it as (CLAIMED/INVESTIGATING) until a verifier actually approves.
_DRAFTS_DIR = Path(__file__).parent / "Model_Bench" / "drafts"
_REJECTED_DRAFTS_DIR = _DRAFTS_DIR / "rejected"
_COMBO_AUDIT_PATH = Path(__file__).parent / "Model_Bench" / "combo_audit.jsonl"


def _log_combo_audit(entry: Dict[str, Any]) -> None:
    _COMBO_AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with _COMBO_AUDIT_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, default=str) + "\n")

# Keywords that make a query anything other than a pure read. Checked
# case-insensitively as whole words so this doesn't false-positive on e.g.
# a column literally named "Updated". Not a substitute for the
# approvals.deny sqlcmd/cursor.execute rules -- this is the read-side
# counterpart: the investigation agent has terminal access and needs SOME
# way to run ad-hoc SELECTs (sys.procedures lookups, schema checks per
# xstudio-sql-write-discipline), and without a sanctioned path for that it
# was falling back to "sqlcmd" (not on PATH in the cron gateway's minimal
# systemd environment) and silently skipping verification entirely -- a
# real 2026-09-03 incident. This gives it one.
_WRITE_KEYWORDS = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|TRUNCATE|EXEC|EXECUTE|MERGE|CREATE|GRANT|REVOKE|DENY)\b",
    re.IGNORECASE,
)


def poll_and_claim(client: HermesL2Client, eligible_status_csv: str, bot_label: Optional[str] = None) -> Dict[str, Any]:
    """
    Deterministic, safe half of a cycle: recover stale runs, find candidates,
    atomically claim ONE, load its full context (including any structured L1
    fields), and stop -- no investigation, no write beyond the claim itself.

    This is what `--poll` runs. It exists so an LLM agent (a Hermes bot) can
    be handed a real, already-claimed ticket with real context, and do its
    OWN reasoning and tool calls for the investigation, instead of getting
    only this script's shallow keyword-search triage. When the agent is
    done, it should call `--publish-response` with its findings so the write
    goes through the audited Hermes_L2_Publish_Response_Usp path rather than
    a raw UPDATE.
    """
    result: Dict[str, Any] = {"status": "STARTED"}
    result["stale_runs_recovered"] = client.recover_stale_runs()

    candidates = client.get_candidate_tickets(eligible_status_csv, batch_size=20)
    if not candidates:
        result["status"] = "NO_TICKETS"
        return result

    # "L2 should only see tickets it can actually solve or escalate through
    # investigation" (explicit 2026-09-03 instruction). Confirmed live that
    # ~43% of the open queue is typed "Request for Customization" -- a
    # feature/UI change request, not a bug or data question. No amount of
    # SQL investigation resolves those; they need a product/engineering
    # decision, not this pipeline. Filtered client-side (ComplaintTypeName
    # already comes back from Hermes_L2_Get_Candidate_Tickets_Usp) rather
    # than editing that official SP.
    _NOT_L2_INVESTIGABLE_TYPES = {"Request for Customization", "Request For Customization Rights"}
    candidates = [c for c in candidates if c.get("ComplaintTypeName") not in _NOT_L2_INVESTIGABLE_TYPES]
    if not candidates:
        result["status"] = "NO_CLAIMABLE_TICKET"
        return result

    for candidate in candidates:
        run_id = client.claim_ticket(candidate["TicketID"], eligible_status_csv)
        if run_id:
            context = client.get_ticket_context(candidate["TicketID"])
            client.start_investigation(run_id, route="AGENT_INVESTIGATION")
            result["status"] = "CLAIMED"
            result["run_id"] = run_id
            result["ticket_id"] = candidate["TicketID"]
            result["ticket"] = _strip_embedded_images(context["ticket"])
            result["prior_runs"] = _strip_embedded_images(context["prior_runs"])
            # Persist the real IDs to disk so --publish-response can verify
            # (or default to) them instead of trusting a GUID the agent
            # transcribed by hand from this JSON. A real 2026-09-03 incident:
            # a 9B local model misstated both the ticket ID and the heat
            # number in its very first response, before any tool call --
            # not a context-loss bug, a small-model verbatim-recall failure.
            # Don't make the model responsible for exact-value fidelity when
            # code can pass it through mechanically instead.
            _LAST_CLAIM_STATE_PATH.write_text(json.dumps({
                "run_id": run_id,
                "ticket_id": candidate["TicketID"],
                "claimed_at": datetime.now(timezone.utc).isoformat(),
                # Which bot (profile/model combo) claimed this -- needed to
                # score/compare combos honestly once more than one profile
                # is polling the same live queue concurrently. Not a DB
                # column deliberately (no schema change for something this
                # local); model_scorecard.py reads it straight from here.
                "bot_label": bot_label,
            }), encoding="utf-8")
            return result

    result["status"] = "NO_CLAIMABLE_TICKET"
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Hermes L2 Investigation Orchestrator")
    parser.add_argument("--server", default=os.environ.get("MSSQL_MCP_SERVER"))
    parser.add_argument("--database", default=None,
                         help=f"Defaults to {DEFAULT_DATABASE} for ticket/Hermes-runtime "
                              "operations. --query has NO default -- pass it explicitly "
                              "(XStudio_Helpdesk for Complaint_Mst_Tbl/Hermes tables, "
                              "XStudio_Xbatch for production/quality/heat/SAP data). "
                              "Confirmed live 2026-09-04: omitting it silently queried "
                              "XStudio_Helpdesk for an Xbatch investigation, producing "
                              "'Invalid object name' on real, existing views for 20+ "
                              "minutes straight before escalating a solvable ticket.")
    parser.add_argument("--username", default=os.environ.get("MSSQL_MCP_USER"))
    parser.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    parser.add_argument("--driver", default=DEFAULT_DRIVER)
    parser.add_argument("--worker-id", default="HERMES_WORKER_001")
    parser.add_argument("--hermes-user-id", default=None,
                         help="Real XStudio user ID for the Hermes service identity, if one exists")
    parser.add_argument("--eligible-status", default=None,
                         help="Comma-separated Status values to treat as claimable "
                              "(e.g. 'Enter'). Run --discover-workflow first to find current values.")
    parser.add_argument("--discover-workflow", action="store_true",
                         help="Print live Status/AskStatus combinations and exit -- run this "
                              "before choosing --eligible-status.")
    parser.add_argument("--poll", action="store_true",
                         help="Claim one eligible ticket and print its full context as JSON, "
                              "then stop (no investigation/write). For an LLM agent driving "
                              "this script via its own terminal tool -- see poll_and_claim().")
    parser.add_argument("--bot-label", default=None,
                         help="Free-text identity of the bot/profile claiming this ticket "
                              "(e.g. 'l2-nemo' or 'nemotron-3-nano-4b'). Recorded in the local "
                              "claim/draft state so model_scorecard.py can attribute a run to "
                              "the right model when multiple bots poll the same queue.")
    parser.add_argument("--publish-response", action="store_true",
                         help="Write a response for an already-claimed run (--run-id). "
                              "Requires --response-type and --reply-text.")
    parser.add_argument("--draft-response", action="store_true",
                         help="Like --publish-response, but writes to a LOCAL draft file "
                              "instead of the live database -- the ticket's real ProcessStatus "
                              "is untouched. Use this instead of --publish-response when a "
                              "verifier gate is in front of this run; a separate --approve-draft "
                              "call does the real publish after review. Same required args as "
                              "--publish-response.")
    parser.add_argument("--approve-draft", default=None, metavar="RUN_ID",
                         help="Read the local draft for RUN_ID and actually publish it via the "
                              "real Hermes_L2_Publish_Response_Usp path, then remove the draft. "
                              "For a verifier to call after review, not the investigating agent.")
    parser.add_argument("--reject-draft", default=None, metavar="RUN_ID",
                         help="Discard the local draft for RUN_ID without publishing it -- the "
                              "ticket stays claimed/unpublished for a nudge/retry. Requires "
                              "--rejection-reason.")
    parser.add_argument("--rejection-reason", default=None,
                         help="Required with --reject-draft. Recorded for audit and reused as "
                              "the retry nudge's specific objection.")
    parser.add_argument("--verifier-label", default=None,
                         help="Free-text identity of the verifier bot calling --approve-draft/"
                              "--reject-draft (e.g. 'l2-nemo'). Recorded alongside the draft's "
                              "own investigator_bot_label in Model_Bench/combo_audit.jsonl so a "
                              "specific investigator+verifier COMBO can be scored, not just a "
                              "single model.")
    parser.add_argument("--run-id", default=None,
                         help="Omit to use the run_id from the most recent --poll claim "
                              "automatically (recommended -- do not hand-type a GUID). If "
                              "given explicitly, it must match that same recorded claim "
                              "unless --force-run-id is also passed.")
    parser.add_argument("--force-run-id", action="store_true",
                         help="Allow --run-id to differ from the last recorded --poll claim. "
                              "For trusted deterministic callers only (e.g. a stale-claim "
                              "sweep publishing for a DIFFERENT run than whatever this "
                              "machine's own last claim was) -- never pass this from an "
                              "agent turn just to silence the mismatch error.")
    parser.add_argument("--response-type", default=None,
                         choices=["QUESTION", "UPDATE", "RESOLUTION", "L3_ESCALATION", "NEEDS_HUMAN_ACTION"])
    parser.add_argument("--fail-run", action="store_true",
                         help="Mark --run-id FAILED with --error-message (EXEC "
                              "Hermes_L2_Fail_Run_Usp) so it becomes eligible for a plain retry "
                              "after --retry-after-minutes. Does NOT touch the L3 human queue -- "
                              "for pipeline-tracking failures (Kanban lost the run), not genuine "
                              "investigation outcomes. Use --response-type L3_ESCALATION/"
                              "NEEDS_HUMAN_ACTION via --publish-response for those instead.")
    parser.add_argument("--error-message", default=None, help="Required with --fail-run.")
    parser.add_argument("--retry-after-minutes", type=int, default=5,
                         help="With --fail-run: how soon the ticket becomes re-pollable.")
    parser.add_argument("--escalate-blocked", action="store_true",
                         help="EXEC Hermes_L2_Log_Blocked_Escalation_Usp -- pure visibility "
                              "insert into the human L3 queue, does not touch "
                              "Hermes_L2_Response_Trn_Tbl or Complaint_Mst_Tbl. Requires "
                              "--run-id, --ticket-id, --block-reason.")
    parser.add_argument("--block-reason", default=None, help="Required with --escalate-blocked.")
    parser.add_argument("--build-query", default=None, metavar="TABLE",
                         help="Mechanically construct a SELECT against TABLE, validating every "
                              "column against Knowledge/schema_allowlist.json BEFORE building any "
                              "SQL -- a hallucinated table/column is rejected here, with the "
                              "closest real name, instead of only being caught after a query fails "
                              "or (worse) never being run at all. Requires --columns. Prints the "
                              "SQL by default; add --execute to actually run it (read-only, "
                              "audited the same as --query).")
    parser.add_argument("--columns", default=None,
                         help="Comma-separated column list for --build-query.")
    parser.add_argument("--where", default=None,
                         help="With --build-query: raw WHERE clause text (identifiers checked "
                              "best-effort against the real schema, values are not).")
    parser.add_argument("--top", type=int, default=None, help="With --build-query: TOP N rows.")
    parser.add_argument("--order-by", default=None, help="With --build-query: ORDER BY clause.")
    parser.add_argument("--execute", action="store_true",
                         help="With --build-query: actually run the constructed SQL (read-only, "
                              "audited) instead of just printing it.")
    parser.add_argument("--reply-text", default=None)
    parser.add_argument("--problem-summary", default=None)
    parser.add_argument("--findings", default=None)
    parser.add_argument("--root-cause", default=None)
    parser.add_argument("--resolution", default=None)
    parser.add_argument("--new-ticket-status", default=None,
                         help="Real live Status value to move the ticket to, or omit to leave unchanged.")
    parser.add_argument("--new-ask-status", default=None)
    parser.add_argument("--mirror-to-support-remarks", action="store_true",
                         help="Also write --reply-text into Complaint_Mst_Tbl.SupportExecutiveRemarks.")
    parser.add_argument("--mirror-to-ask-remarks", action="store_true",
                         help="Also write --reply-text into Complaint_Mst_Tbl.AskRemarks (only takes "
                              "effect when --response-type QUESTION).")
    parser.add_argument("--query", default=None,
                         help="Run a read-only SELECT (or sys.* metadata query) against --database "
                              "and print results as JSON. Refused if it contains any write keyword "
                              "(INSERT/UPDATE/DELETE/DROP/ALTER/EXEC/...). For investigation reads "
                              "-- table/column/procedure lookups per xstudio-sql-write-discipline -- "
                              "not a general SQL console.")
    parser.add_argument("--log-activity", action="store_true",
                         help="Append one row to Hermes_Ticket_Activity_Trn_Tbl -- the ticket's "
                              "real work-log timeline. Requires --ticket-id and --activity-type; "
                              "--note-text strongly recommended.")
    parser.add_argument("--ticket-id", default=None,
                         help="Real Complaint_Mst_Tbl.ID -- required with --log-activity/"
                              "--link-solution. Copy it from your task body (the same ticket_id "
                              "used everywhere else), don't guess or retype from memory.")
    parser.add_argument("--activity-type", default=None,
                         choices=["Note", "StatusChange", "Escalation", "Resolution", "Reopen", "SolutionLinked", "ProblemLinked"],
                         help="Required with --log-activity.")
    parser.add_argument("--note-text", default=None, help="Free text for --log-activity.")
    parser.add_argument("--actor-type", default="Bot", choices=["Bot", "Human", "System"])
    parser.add_argument("--search-solutions", default=None, metavar="ROUTE",
                         help="Print active Hermes_Solution_Article_Mst_Tbl rows for this Route "
                              "(e.g. 'heat_execution'), ordered by UsageCount desc -- check this "
                              "BEFORE investigating from scratch. A known fix may already exist.")
    parser.add_argument("--create-solution", action="store_true",
                         help="Create a new knowledge-base entry after a genuine RESOLUTION. "
                              "Requires --solution-title and --resolution-steps; "
                              "--problem-summary/--root-cause/--route/--tags optional. "
                              "Prints the new SolutionID.")
    parser.add_argument("--solution-title", default=None)
    parser.add_argument("--resolution-steps", default=None)
    parser.add_argument("--route", default=None)
    parser.add_argument("--tags", default=None)
    parser.add_argument("--link-solution", default=None, metavar="SOLUTION_ID",
                         help="Link --ticket-id to this existing SolutionID (from --search-solutions "
                              "or --create-solution) -- increments its UsageCount and auto-logs a "
                              "SolutionLinked activity. Requires --ticket-id.")
    parser.add_argument("--get-activity", action="store_true",
                         help="Print the full work-log timeline (Hermes_Ticket_Activity_Trn_Tbl) "
                              "for --ticket-id, as JSON. Use this to see what prior investigation "
                              "attempts (and the reviewer) actually did -- not just the ticket's "
                              "final remarks.")
    parser.add_argument("--list-root-cause-categories", action="store_true",
                         help="Print the controlled root-cause taxonomy (Hermes_Root_Cause_Category_Mst_Tbl) as JSON.")
    parser.add_argument("--create-problem", action="store_true",
                         help="Create a Problem record (a recurring root cause behind N tickets). "
                              "Requires --solution-title (reused as the Problem title) and "
                              "prints the new ProblemID. --root-cause optional.")
    parser.add_argument("--link-problem", default=None, metavar="PROBLEM_ID",
                         help="Link --ticket-id to this existing ProblemID.")
    parser.add_argument("--find-sql-objects", default=None, metavar="SEARCH_TEXT",
                         help="EXEC Hermes_L2_Find_SQL_Objects_Usp -- search procs/views/tables/"
                              "triggers by name or definition text in --target-database (NOT "
                              "--database, which is the connection -- this SP only exists in "
                              "XStudio_Helpdesk and searches cross-database via its own param). "
                              "Prefer this over guessing an object name.")
    parser.add_argument("--object-type", default=None,
                         help="Optional filter for --find-sql-objects (e.g. TABLE/VIEW/PROCEDURE).")
    parser.add_argument("--target-database", default="XStudio_Xbatch",
                         help="The database --find-sql-objects/--get-sql-object-definition should "
                              "search -- separate from --database (the connection, which stays "
                              "XStudio_Helpdesk since that's where these SPs are installed).")
    parser.add_argument("--get-sql-object-definition", default=None, metavar="OBJECT_NAME",
                         help="EXEC Hermes_L2_Get_SQL_Object_Definition_Usp -- full real definition "
                              "text for one table/view/SP/trigger in --target-database. Use this "
                              "instead of guessing what a view actually does.")
    parser.add_argument("--schema-name", default="dbo", help="Schema for --get-sql-object-definition.")
    parser.add_argument("--get-reference-documents", default=None, metavar="SEARCH_TEXT",
                         help="EXEC Hermes_L2_Get_Reference_Documents_Usp -- search existing "
                              "systemreferencedocuments. Optional --area filter.")
    parser.add_argument("--area", default=None, help="Optional filter for --get-reference-documents.")
    parser.add_argument("--get-run-actions", default=None, metavar="RUN_ID",
                         help="EXEC Hermes_L2_Get_Run_Actions_Usp -- the full SQL action audit "
                              "trail for one run (yours or a prior one on the same ticket).")
    parser.add_argument("--get-ticket-context", default=None, metavar="TICKET_ID",
                         help="EXEC Hermes_L2_Get_Ticket_Context_Usp -- re-fetch the LIVE "
                              "Complaint_Mst_Tbl row (+ prior Hermes runs) for this ticket_id. "
                              "Use this whenever your task body's embedded entity data might be "
                              "stale (e.g. corrected after you were assigned) -- don't keep "
                              "querying against values that were already fixed upstream.")
    args = parser.parse_args()
    # --build-query needs to know whether --database was actually typed by
    # the caller, to decide whether an ambiguous table name (one that
    # exists in more than one database) deserves a warning. Captured here,
    # before the unconditional default-fill below overwrites args.database
    # for every other code path -- confirmed live this exact bug: the
    # ambiguity warning could never fire because args.database was never
    # actually None by the time --build-query's own handler ran.
    _database_explicitly_given = args.database

    if not args.server:
        parser.error("--server is required (or set MSSQL_MCP_SERVER)")

    if args.query is not None and args.database is None:
        parser.error(
            "--query requires an explicit --database -- there is no default. "
            "Use XStudio_Helpdesk for Complaint_Mst_Tbl/Hermes runtime tables, "
            "XStudio_Xbatch for production/quality/heat/billet/SAP data. "
            "Confirmed live 2026-09-04: omitting this silently queried the wrong "
            "database and produced false 'Invalid object name' errors on real, "
            "existing tables."
        )
    if args.database is None:
        args.database = DEFAULT_DATABASE

    client = HermesL2Client(
        server=args.server, database=args.database, username=args.username,
        password=args.password, driver=args.driver, worker_id=args.worker_id,
        hermes_user_id=args.hermes_user_id,
    )

    try:
        if args.discover_workflow:
            workflow = client.discover_helpdesk_workflow()
            print("Live Status / AskStatus / messages combinations (dbo.Complaint_Mst_Tbl):")
            for row in workflow["status_combinations"]:
                print(f"  {row}")
            return

        if args.poll:
            if not args.eligible_status:
                parser.error("--eligible-status is required with --poll")
            result = poll_and_claim(client, args.eligible_status, bot_label=args.bot_label)
            print(json.dumps(result, indent=2, default=str))
            return

        if args.log_activity:
            if not args.ticket_id or not args.activity_type:
                parser.error("--log-activity requires --ticket-id and --activity-type")
            client.log_activity(
                ticket_id=args.ticket_id, activity_type=args.activity_type,
                note_text=args.note_text, actor_type=args.actor_type, run_id=args.run_id,
            )
            print(f"Logged {args.activity_type} activity for ticket {args.ticket_id}.")
            return

        if args.search_solutions:
            cur = client.conn.cursor()
            cur.execute(
                "SELECT TOP 5 ID, Title, ProblemSummary, RootCause, ResolutionSteps, UsageCount "
                "FROM dbo.Hermes_Solution_Article_Mst_Tbl "
                "WHERE Route = ? AND IsActive = 1 AND IsDeleted = 0 "
                "ORDER BY UsageCount DESC",
                (args.search_solutions,),
            )
            cols = [d[0] for d in cur.description]
            rows = [dict(zip(cols, row)) for row in cur.fetchall()]
            print(json.dumps(rows, indent=2, default=str))
            return

        if args.create_solution:
            if not args.solution_title or not args.resolution_steps:
                parser.error("--create-solution requires --solution-title and --resolution-steps")
            new_id = client.create_solution(
                title=args.solution_title, resolution_steps=args.resolution_steps,
                problem_summary=args.problem_summary, root_cause=args.root_cause,
                route=args.route, tags=args.tags,
            )
            print(f"Created solution {new_id}")
            return

        if args.link_solution:
            if not args.ticket_id:
                parser.error("--link-solution requires --ticket-id")
            client.link_solution(ticket_id=args.ticket_id, solution_id=args.link_solution, run_id=args.run_id)
            print(f"Linked ticket {args.ticket_id} to solution {args.link_solution}.")
            return

        if args.get_activity:
            if not args.ticket_id:
                parser.error("--get-activity requires --ticket-id")
            print(json.dumps(client.get_ticket_activity(args.ticket_id), indent=2, default=str))
            return

        if args.list_root_cause_categories:
            print(json.dumps(client.list_root_cause_categories(), indent=2, default=str))
            return

        if args.create_problem:
            if not args.solution_title:
                parser.error("--create-problem requires --solution-title (used as the Problem title)")
            new_id = client.create_problem(
                title=args.solution_title, root_cause_summary=args.root_cause,
            )
            print(f"Created problem {new_id}")
            return

        if args.link_problem:
            if not args.ticket_id:
                parser.error("--link-problem requires --ticket-id")
            client.link_problem(problem_id=args.link_problem, ticket_id=args.ticket_id)
            print(f"Linked ticket {args.ticket_id} to problem {args.link_problem}.")
            return

        if args.find_sql_objects:
            print(json.dumps(
                client.find_sql_objects(args.target_database, args.find_sql_objects, object_type=args.object_type),
                indent=2, default=str,
            ))
            return

        if args.get_sql_object_definition:
            result = client.get_sql_object_definition(args.target_database, args.schema_name, args.get_sql_object_definition)
            print(json.dumps(result, indent=2, default=str) if result else "null")
            return

        if args.get_reference_documents:
            print(json.dumps(
                client.get_reference_documents(args.get_reference_documents, area=args.area),
                indent=2, default=str,
            ))
            return

        if args.get_run_actions:
            print(json.dumps(client.get_run_actions(args.get_run_actions), indent=2, default=str))
            return

        if args.get_ticket_context:
            print(json.dumps(client.get_ticket_context(args.get_ticket_context), indent=2, default=str))
            return

        if args.build_query:
            if not args.columns:
                parser.error("--build-query requires --columns")
            result = build_query_mechanically(
                table=args.build_query,
                columns=[c.strip() for c in args.columns.split(",") if c.strip()],
                where=args.where, order_by=args.order_by, top=args.top,
                database=_database_explicitly_given,
            )
            if not result["ok"]:
                print(json.dumps(result, indent=2))
                sys.exit(1)
            if not args.execute:
                print(json.dumps(result, indent=2))
                return
            # Fall through into the exact same audited --query path below --
            # no separate execution code to maintain, and it gets the same
            # write-keyword refusal, the same audit trail, and the same
            # post-failure fuzzy-suggestion safety net for free (structurally
            # unreachable here since every identifier was already validated,
            # but a real, still-useful backstop against anything this
            # validator itself missed).
            args.query = result["sql"]
            args.database = args.database or result["database"]
            print(f"Executing mechanically-built query: {result['sql']}", file=sys.stderr)

        if args.query:
            # Strip single-quoted string literals before checking for write
            # keywords -- otherwise a legitimate read like
            # "...WHERE p.name LIKE '%Insert%'" (searching for procedure
            # NAMES) gets refused because "Insert" appears inside a string
            # literal, not as an actual SQL command. A real 2026-09-03
            # false-positive, found while investigating this exact
            # official-SP-first workflow.
            query_without_literals = re.sub(r"'(?:[^']|'')*'", "''", args.query)
            if _WRITE_KEYWORDS.search(query_without_literals):
                parser.error(
                    "--query must be read-only (SELECT / sys.* metadata lookups only). "
                    "This query contains a write keyword and was refused. Writes go through "
                    "--publish-response, never a direct query."
                )
            # Audit every --query call the same way execute_sql() already does for
            # Hermes_L2_Execute_SQL_Usp -- added 2026-09-04 after confirming live that
            # Hermes_L2_SQL_Action_Trn_Tbl had gone dark since 2026-09-02, the exact day
            # --query was introduced as the skill's primary read path. The reviewer reads
            # this table to verify an investigator's claims were actually backed by a
            # query; --query running real investigation reads with zero audit trail was
            # silently making every one of those investigations look unverified, which is
            # exactly the rejection reason confirmed live on real review tasks. Best-effort:
            # if --run-id isn't supplied (e.g. an ad-hoc lookup with no active run), skip
            # logging rather than erroring -- audit richness should never block a read.
            action_id = None
            if args.run_id:
                try:
                    action_id = client.execute_sql(
                        run_id=args.run_id, database_name=args.database or "", action_type="READ",
                        sql=args.query, operation_name="--query", purpose="Investigation read via --query",
                    )
                except Exception:
                    pass  # audit logging must never block the actual read
            cur = client.conn.cursor()
            try:
                cur.execute(args.query)
            except pyodbc.Error as e:
                # Turn "Invalid column/object name 'X'" into an immediate,
                # actionable correction using the same ground truth
                # validate_identifiers.py uses -- so a naming miss is fixed
                # in this same tool call, not left for the agent to
                # separately remember to check afterward (or, per a real
                # 2026-09-03 incident, not check at all and escalate a
                # ticket that a one-word column-name fix would have solved).
                msg = str(e)
                col_m = re.search(r"Invalid column name '([^']+)'", msg)
                obj_m = re.search(r"Invalid object name '([^']+)'", msg)
                allowlist_path = Path(__file__).parent / "Knowledge" / "schema_allowlist.json"
                if (col_m or obj_m) and allowlist_path.exists():
                    allowlist = json.loads(allowlist_path.read_text(encoding="utf-8"))
                    flat = {}  # normalized table name -> (db, qname, columns)
                    for db, tables in allowlist.items():
                        for qname, cols in tables.items():
                            flat[qname.split(".")[-1].lower()] = (db, qname, cols)

                    if obj_m:
                        # Wrong table/object name -- suggest against every real table.
                        bad_name = obj_m.group(1)
                        table_names = list(flat.keys())
                        suggestions = difflib.get_close_matches(bad_name.lower(), table_names, n=3, cutoff=0.5)
                        suggestion_text = [flat[s][1] for s in suggestions]
                    else:
                        # Wrong column name -- restrict candidates to the table(s) this
                        # query actually references, not the whole schema (a same/similar
                        # column name existing in some unrelated table produced a wrong,
                        # confident-looking suggestion the first time this was tried).
                        bad_name = col_m.group(1)
                        referenced = re.findall(
                            r"(?:FROM|JOIN)\s+(?:\[?\w+\]?\.)?\[?(\w+)\]?", args.query, re.IGNORECASE
                        )
                        candidate_cols = []
                        for t in referenced:
                            entry = flat.get(t.lower())
                            if entry:
                                candidate_cols.extend(entry[2])
                        if not candidate_cols:
                            # Table itself wasn't resolvable from the query text -- fall
                            # back to a schema-wide search rather than giving no help.
                            for db, tables in allowlist.items():
                                for cols in tables.values():
                                    candidate_cols.extend(cols)
                        suggestion_text = difflib.get_close_matches(bad_name, candidate_cols, n=3, cutoff=0.5)

                    if suggestion_text:
                        raise RuntimeError(
                            f"{msg} -- '{bad_name}' is not real. Closest real names in the "
                            f"live schema (scoped to this query's own table where possible): "
                            f"{suggestion_text}. Retry the query with one of these, do not guess "
                            f"again or escalate without trying the correction."
                        ) from None
                raise
            if cur.description is None:
                result_payload = {"rows_affected": cur.rowcount}
            else:
                cols = [d[0] for d in cur.description]
                rows = [dict(zip(cols, row)) for row in cur.fetchall()]
                result_payload = _strip_embedded_images(rows)
            if action_id:
                try:
                    client.update_sql_action_evidence(
                        action_id, after_json={"row_count": len(result_payload) if isinstance(result_payload, list) else None,
                                                "sample": result_payload[:5] if isinstance(result_payload, list) else result_payload},
                    )
                except Exception:
                    pass  # audit logging must never block the actual read
            print(json.dumps(result_payload, indent=2, default=str))
            return

        if args.escalate_blocked:
            if not (args.run_id and args.ticket_id and args.block_reason):
                parser.error("--escalate-blocked requires --run-id, --ticket-id, and --block-reason")
            client.log_blocked_escalation(
                run_id=args.run_id, ticket_id=args.ticket_id,
                block_reason=args.block_reason, findings=args.findings,
            )
            print(json.dumps({"status": "ESCALATED", "run_id": args.run_id}, indent=2))
            return

        if args.fail_run:
            if not (args.run_id and args.error_message):
                parser.error("--fail-run requires --run-id and --error-message")
            client.fail_run(
                run_id=args.run_id,
                error_message=args.error_message,
                retry_after_minutes=args.retry_after_minutes,
            )
            print(json.dumps({"status": "FAILED", "run_id": args.run_id}, indent=2))
            return

        if args.publish_response:
            if not (args.response_type and args.reply_text):
                parser.error("--publish-response requires --response-type and --reply-text")

            last_claim = None
            if _LAST_CLAIM_STATE_PATH.exists():
                last_claim = json.loads(_LAST_CLAIM_STATE_PATH.read_text(encoding="utf-8"))

            run_id = args.run_id
            if run_id is None:
                if last_claim is None:
                    parser.error(
                        "--run-id was omitted and no prior --poll claim was found on disk "
                        f"({_LAST_CLAIM_STATE_PATH}). Run --poll first, or pass --run-id explicitly."
                    )
                run_id = last_claim["run_id"]
                print(f"Using run_id from most recent --poll claim: {run_id}", file=sys.stderr)
            elif last_claim is not None and run_id != last_claim["run_id"] and not args.force_run_id:
                parser.error(
                    f"--run-id {run_id!r} does not match the most recently claimed run "
                    f"{last_claim['run_id']!r} (ticket {last_claim.get('ticket_id')!r}, "
                    f"claimed {last_claim.get('claimed_at')!r}). This usually means the wrong "
                    f"ID was typed/recalled from memory -- omit --run-id to use the recorded "
                    f"claim automatically, or verify this is genuinely a different, already-"
                    f"claimed run before overriding."
                )

            client.publish_response(
                run_id=run_id,
                response_type=args.response_type,
                reply_text=args.reply_text,
                problem_summary=args.problem_summary,
                findings=args.findings,
                root_cause=args.root_cause,
                resolution=args.resolution,
                new_ticket_status=args.new_ticket_status,
                new_ask_status=args.new_ask_status,
                mirror_reply_to_support_remarks=args.mirror_to_support_remarks,
                mirror_question_to_ask_remarks=args.mirror_to_ask_remarks,
            )
            if last_claim is not None and last_claim["run_id"] == run_id:
                _LAST_CLAIM_STATE_PATH.unlink(missing_ok=True)
            print(json.dumps({"status": "PUBLISHED", "run_id": run_id}, indent=2))
            return

        if args.draft_response:
            if not (args.response_type and args.reply_text):
                parser.error("--draft-response requires --response-type and --reply-text")

            last_claim = None
            if _LAST_CLAIM_STATE_PATH.exists():
                last_claim = json.loads(_LAST_CLAIM_STATE_PATH.read_text(encoding="utf-8"))

            run_id = args.run_id
            if run_id is None:
                if last_claim is None:
                    parser.error(
                        "--run-id was omitted and no prior --poll claim was found on disk "
                        f"({_LAST_CLAIM_STATE_PATH}). Run --poll first, or pass --run-id explicitly."
                    )
                run_id = last_claim["run_id"]
                print(f"Using run_id from most recent --poll claim: {run_id}", file=sys.stderr)
            elif last_claim is not None and run_id != last_claim["run_id"] and not args.force_run_id:
                parser.error(
                    f"--run-id {run_id!r} does not match the most recently claimed run "
                    f"{last_claim['run_id']!r}. Omit --run-id to use the recorded claim "
                    f"automatically, or pass --force-run-id if this is genuinely intentional."
                )

            _DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
            draft = {
                "run_id": run_id,
                "ticket_id": (last_claim or {}).get("ticket_id"),
                "investigator_bot_label": (last_claim or {}).get("bot_label"),
                "response_type": args.response_type,
                "reply_text": args.reply_text,
                "problem_summary": args.problem_summary,
                "findings": args.findings,
                "root_cause": args.root_cause,
                "resolution": args.resolution,
                "new_ticket_status": args.new_ticket_status,
                "new_ask_status": args.new_ask_status,
                "mirror_to_support_remarks": args.mirror_to_support_remarks,
                "drafted_at": datetime.now(timezone.utc).isoformat(),
            }
            (_DRAFTS_DIR / f"{run_id}.json").write_text(json.dumps(draft, indent=2), encoding="utf-8")
            if last_claim is not None and last_claim["run_id"] == run_id:
                _LAST_CLAIM_STATE_PATH.unlink(missing_ok=True)
            print(json.dumps({"status": "DRAFTED", "run_id": run_id,
                               "note": "Not yet published -- awaiting verifier approval."}, indent=2))
            return

        if args.approve_draft:
            run_id = args.approve_draft
            draft_path = _DRAFTS_DIR / f"{run_id}.json"
            if not draft_path.exists():
                parser.error(f"No draft found for run_id {run_id!r} at {draft_path}")
            draft = json.loads(draft_path.read_text(encoding="utf-8"))
            client.publish_response(
                run_id=run_id,
                response_type=draft["response_type"],
                reply_text=draft["reply_text"],
                problem_summary=draft.get("problem_summary"),
                findings=draft.get("findings"),
                root_cause=draft.get("root_cause"),
                resolution=draft.get("resolution"),
                new_ticket_status=draft.get("new_ticket_status"),
                new_ask_status=draft.get("new_ask_status"),
                mirror_reply_to_support_remarks=bool(draft.get("mirror_to_support_remarks")),
            )
            draft_path.unlink()
            _log_combo_audit({
                "run_id": run_id,
                "ticket_id": draft.get("ticket_id"),
                "outcome": "APPROVED",
                "investigator_bot_label": draft.get("investigator_bot_label"),
                "verifier_bot_label": args.verifier_label,
                "response_type": draft.get("response_type"),
                "logged_at": datetime.now(timezone.utc).isoformat(),
            })
            print(json.dumps({"status": "PUBLISHED_FROM_DRAFT", "run_id": run_id}, indent=2))
            return

        if args.reject_draft:
            if not args.rejection_reason:
                parser.error("--reject-draft requires --rejection-reason")
            run_id = args.reject_draft
            draft_path = _DRAFTS_DIR / f"{run_id}.json"
            if not draft_path.exists():
                parser.error(f"No draft found for run_id {run_id!r} at {draft_path}")
            draft = json.loads(draft_path.read_text(encoding="utf-8"))
            draft["rejected_at"] = datetime.now(timezone.utc).isoformat()
            draft["rejection_reason"] = args.rejection_reason
            _REJECTED_DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
            (_REJECTED_DRAFTS_DIR / f"{run_id}_{int(datetime.now(timezone.utc).timestamp())}.json").write_text(
                json.dumps(draft, indent=2), encoding="utf-8"
            )
            draft_path.unlink()
            _log_combo_audit({
                "run_id": run_id,
                "ticket_id": draft.get("ticket_id"),
                "outcome": "REJECTED",
                "investigator_bot_label": draft.get("investigator_bot_label"),
                "verifier_bot_label": args.verifier_label,
                "response_type": draft.get("response_type"),
                "rejection_reason": args.rejection_reason,
                "logged_at": datetime.now(timezone.utc).isoformat(),
            })
            print(json.dumps({"status": "REJECTED", "run_id": run_id,
                               "reason": args.rejection_reason}, indent=2))
            return

        parser.error("Pass one of --discover-workflow, --poll, --publish-response, "
                      "--draft-response, --approve-draft, or --reject-draft.")
    finally:
        client.close()


if __name__ == "__main__":
    main()
