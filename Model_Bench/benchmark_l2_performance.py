#!/usr/bin/env python3
"""L2 Helpdesk performance and live-health report: the one diagnostic for "what is happening".

Everything comes from SQL (runs, trace, frozen work packages), so it answers the same
questions from Windows or WSL without ad hoc scripts:
1. Outcomes: published / failed / active, response types, canned "INCOMPLETE" replies
2. Compute & timing per completed run (tokens, tool calls, claim-to-publish)
3. Tool health: calls and failures per tool, top failure causes
4. Small-model waste: blocked script writes, spill-file reads, completions after submit
5. Worker card sizes by purpose (spill risk above ~39K chars for a 65K-token model)
6. Lifecycle invariants from AGENTS.md (each must be 0)

    python Model_Bench/benchmark_l2_performance.py --since "2026-09-23 13:05"
    python Model_Bench/benchmark_l2_performance.py --hours 6 --json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from typing import Any

import pyodbc

DEFAULT_SERVER = os.environ.get("MSSQL_MCP_SERVER") or "10.2.6.204"
DEFAULT_DATABASE = "XStudio_Helpdesk"
DEFAULT_USER = os.environ.get("MSSQL_MCP_USER") or "sa"
# Hermes spills a tool result above 15% of the model window (65,792 tokens * 4 chars).
SPILL_THRESHOLD_CHARS = int(65_792 * 4 * 0.15)
# Trace results are stored as JSON-encoded strings, so keys appear both plain and escaped.
FAILED_RESULT = ("(ResultJson LIKE '%\"ok\": false%' OR ResultJson LIKE '%\\\"ok\\\": false%' "
                 "OR ResultJson LIKE '%\"error\"%' OR ResultJson LIKE '%\\\"error\\\"%' OR Status = 'error')")

INVARIANTS = {
    "RESOLUTION published but ticket not Closed":
        """SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl r JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
           WHERE r.IsDeleted = 0 AND c.IsDeleted = 0 AND r.ProcessStatus = 'COMPLETED'
             AND r.ResponseType = 'RESOLUTION' AND c.Status <> 'Closed'""",
    "RESOLUTION without IsResolved=1":
        """SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE IsDeleted = 0
           AND ProcessStatus = 'COMPLETED' AND ResponseType = 'RESOLUTION' AND ISNULL(IsResolved, 0) = 0""",
    "L3/NEEDS_HUMAN_ACTION published without L3 queue row":
        """SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl r WHERE r.IsDeleted = 0 AND r.ProcessStatus = 'COMPLETED'
           AND r.ResponseType IN ('L3_ESCALATION', 'NEEDS_HUMAN_ACTION')
           AND NOT EXISTS (SELECT 1 FROM dbo.Hermes_L3_Escalation_Trn_Tbl e WHERE e.RunID = r.ID AND e.IsDeleted = 0)""",
    "More than one RUNNING local-model task":
        """SELECT CASE WHEN COUNT(*) > 1 THEN COUNT(*) ELSE 0 END FROM dbo.Hermes_L2_Response_Trn_Tbl
           WHERE IsActive = 1 AND LocalModelState = 'RUNNING'""",
    "Active run in a terminal ProcessStatus":
        """SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl
           WHERE IsActive = 1 AND IsDeleted = 0 AND ProcessStatus IN ('COMPLETED', 'FAILED')""",
    "Active run whose ticket is missing/deleted":
        """SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl r LEFT JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
           WHERE r.IsActive = 1 AND r.IsDeleted = 0 AND (c.ID IS NULL OR c.IsDeleted = 1)""",
    "More than one active run per ticket":
        """SELECT COUNT(*) FROM (SELECT TicketID FROM dbo.Hermes_L2_Response_Trn_Tbl
           WHERE IsActive = 1 AND IsDeleted = 0 GROUP BY TicketID HAVING COUNT(*) > 1) x""",
    "Published run with empty ReplyText":
        """SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE IsDeleted = 0
           AND ProcessStatus IN ('COMPLETED', 'WAITING_USER') AND NULLIF(LTRIM(RTRIM(ReplyText)), '') IS NULL""",
    "Published UPDATE with NULL NextEligibleOn":
        """SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE IsDeleted = 0
           AND ProcessStatus = 'COMPLETED' AND ResponseType = 'UPDATE' AND NextEligibleOn IS NULL""",
    "Closed ticket with an active Hermes run":
        """SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl r JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
           WHERE r.IsActive = 1 AND r.IsDeleted = 0 AND c.Status = 'Closed'""",
}


def get_db_connection(server: str, database: str, user: str, password: str | None):
    password = password or os.environ.get("MSSQL_MCP_PASSWORD")
    if not password:
        raise RuntimeError("No SQL password supplied. Pass --password or set MSSQL_MCP_PASSWORD.")
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={user};PWD={password};TrustServerCertificate=yes;Connection Timeout=60;"
    )


def _rows(cur, sql: str, *params) -> list[dict[str, Any]]:
    cur.execute(sql, *params)
    cols = [c[0] for c in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def collect_runs(cur, since: datetime) -> list[dict[str, Any]]:
    return _rows(cur, """
        SELECT r.ID AS RunID, c.TicketNo, r.ProcessStatus, r.ResponseType, r.IsActive,
               r.LocalModelPurpose, r.LocalModelState, r.CreatedOn,
               DATEDIFF(SECOND, r.ClaimedOn, r.CompletedOn) AS DurationSeconds,
               CASE WHEN r.ReplyText LIKE 'Evidence status: INCOMPLETE%' THEN 1 ELSE 0 END AS CannedIncomplete
        FROM dbo.Hermes_L2_Response_Trn_Tbl r JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
        WHERE r.IsDeleted = 0 AND (r.CreatedOn >= ? OR r.ModifiedOn >= ? OR r.IsActive = 1)
        ORDER BY r.ModifiedOn DESC""", since, since)


def outcome_summary(runs: list[dict[str, Any]]) -> dict[str, Any]:
    types: dict[str, int] = {}
    for r in runs:
        if r["ProcessStatus"] in ("COMPLETED", "WAITING_USER"):
            key = r["ResponseType"] or "UNKNOWN"
            types[key] = types.get(key, 0) + 1
    durations = [r["DurationSeconds"] for r in runs if r["ProcessStatus"] == "COMPLETED" and r["DurationSeconds"]]
    return {
        "runs": len(runs),
        "published": sum(types.values()),
        "failed": sum(1 for r in runs if r["ProcessStatus"] == "FAILED"),
        "active": sum(1 for r in runs if r["IsActive"]),
        "response_types": types,
        "canned_incomplete_replies": sum(r["CannedIncomplete"] for r in runs),
        "avg_claim_to_publish_min": round(sum(durations) / len(durations) / 60, 1) if durations else None,
    }


def _normalise_error(text: str) -> str:
    text = re.sub(r"[0-9A-F]{8}-[0-9A-F-]{27}", "<id>", text or "", flags=re.I)
    text = re.sub(r"t_[0-9a-f]{8}", "<task>", text)
    text = re.sub(r"/[\w./-]*spillover/[\w.-]+", "<spill-file>", text)
    return re.sub(r"\s+", " ", text)[:150]


def tool_health(cur, since: datetime) -> dict[str, Any]:
    per_tool = _rows(cur, f"""
        SELECT ToolName, COUNT(*) AS Calls, SUM(CASE WHEN {FAILED_RESULT} THEN 1 ELSE 0 END) AS Failed
        FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE EventType = 'post_tool_call' AND EventOn >= ?
        GROUP BY ToolName ORDER BY Calls DESC""", since)
    causes: dict[str, int] = {}
    for row in _rows(cur, f"""SELECT ToolName, LEFT(ResultJson, 400) AS R FROM dbo.Hermes_Agent_Trace_Trn_Tbl
                             WHERE EventType = 'post_tool_call' AND EventOn >= ? AND {FAILED_RESULT}""", since):
        key = f"{row['ToolName']}: {_normalise_error(str(row['R']).replace(chr(92), ''))}"
        causes[key] = causes.get(key, 0) + 1
    top = sorted(causes.items(), key=lambda kv: -kv[1])[:12]
    return {"per_tool": per_tool, "top_failure_causes": [{"cause": k, "count": v} for k, v in top]}


def waste_signals(cur, since: datetime) -> dict[str, int]:
    return _rows(cur, """
        SELECT
          SUM(CASE WHEN ToolName IN ('write_file', 'patch') AND ResultJson LIKE '%Scripts cannot run%' THEN 1 ELSE 0 END)
              AS BlockedScriptWrites,
          SUM(CASE WHEN ToolName = 'read_file' AND ArgsJson LIKE '%spillover%' THEN 1 ELSE 0 END) AS SpillFileReads,
          SUM(CASE WHEN ToolName = 'kanban_complete' AND ResultJson LIKE '%Already done%' THEN 1 ELSE 0 END)
              AS CompletionsAfterSubmit,
          SUM(CASE WHEN ToolName = 'xstudio_submit_proposal' AND ResultJson LIKE '%Reviewers judge the frozen%' THEN 1 ELSE 0 END)
              AS ReviewerSubmitAttempts,
          COUNT(DISTINCT SessionID) AS Sessions
        FROM dbo.Hermes_Agent_Trace_Trn_Tbl
        WHERE EventOn >= ? AND EventType IN ('pre_tool_call', 'post_tool_call')""", since)[0]


def card_sizes(cur, since: datetime) -> list[dict[str, Any]]:
    """Frozen work-package size per purpose; the card body is the bulk of it."""
    return _rows(cur, f"""
        SELECT LocalModelPurpose AS Purpose, COUNT(*) AS Cards,
               AVG(LEN(PendingLocalModelJson)) AS AvgChars, MAX(LEN(PendingLocalModelJson)) AS MaxChars,
               SUM(CASE WHEN LEN(PendingLocalModelJson) > {SPILL_THRESHOLD_CHARS} THEN 1 ELSE 0 END) AS OverSpill
        FROM dbo.Hermes_L2_Response_Trn_Tbl
        WHERE PendingLocalModelJson IS NOT NULL AND LocalModelQueuedOn >= ?
        GROUP BY LocalModelPurpose""", since)


def largest_card_sections(cur, since: datetime) -> dict[str, Any]:
    """Section sizes of the largest recent worker card, to see what to trim.

    kanban_show adds ~40% (JSON escaping, runs, events) on top of the body, so a body
    above ~25K chars still spills for a 65K-token model.
    """
    row = cur.execute("""SELECT TOP 1 LocalModelPurpose, PendingLocalModelJson FROM dbo.Hermes_L2_Response_Trn_Tbl
                         WHERE PendingLocalModelJson IS NOT NULL AND LocalModelQueuedOn >= ?
                         ORDER BY LEN(PendingLocalModelJson) DESC""", since).fetchone()
    if not row:
        return {}
    body = str(json.loads(row[1]).get("body") or "")
    # Blank-line separated blocks, labelled by their first line (pretty JSON context
    # and prose instructions both break this way).
    blocks = [b for b in re.split(r"\n\s*\n", body) if b.strip()]
    ranked = sorted(blocks, key=len, reverse=True)[:8]
    compiler = {k: m.group(1) for k in ("budget_chars", "compiled_chunk_chars", "rendered_chars_estimate",
                                          "target_total_chars", "budget_overflow_for_pinned_context")
                for m in [re.search(rf'"{k}"\s*:\s*(\w+)', body)] if m}
    return {"purpose": row[0], "body_chars": len(body), "context_compiler": compiler,
            "sections": [{"section": b.strip().splitlines()[0][:70], "chars": len(b)} for b in ranked]}


def failure_reasons(cur, since: datetime) -> list[dict[str, Any]]:
    """Why runs ended FAILED in the window (first line of ErrorMessage, grouped)."""
    return _rows(cur, """
        SELECT LEFT(ISNULL(ErrorMessage, '(none)'), 90) AS Reason, COUNT(*) AS Runs
        FROM dbo.Hermes_L2_Response_Trn_Tbl
        WHERE IsDeleted = 0 AND ProcessStatus = 'FAILED' AND ModifiedOn >= ?
        GROUP BY LEFT(ISNULL(ErrorMessage, '(none)'), 90) ORDER BY Runs DESC""", since)


def invariants(cur) -> dict[str, int]:
    return {label: cur.execute(sql).fetchone()[0] for label, sql in INVARIANTS.items()}


def build_report(cur, since: datetime) -> dict[str, Any]:
    runs = collect_runs(cur, since)
    return {
        "window_since": since.isoformat(sep=" ", timespec="minutes"),
        "outcomes": outcome_summary(runs),
        "runs": [{k: v for k, v in r.items() if k != "CannedIncomplete"} for r in runs],
        "tool_health": tool_health(cur, since),
        "waste": waste_signals(cur, since),
        "failure_reasons": failure_reasons(cur, since),
        "card_sizes": card_sizes(cur, since),
        "largest_card": largest_card_sections(cur, since),
        "spill_threshold_chars": SPILL_THRESHOLD_CHARS,
        "invariants": invariants(cur),
    }


def print_markdown(report: dict[str, Any], limit: int) -> None:
    o = report["outcomes"]
    print(f"# Chitragupta L2 health since {report['window_since']} (server-local IST)\n")
    print(f"## Outcomes\n- runs {o['runs']} | published {o['published']} | failed {o['failed']} | active {o['active']}")
    print(f"- response types: {o['response_types']}")
    print(f"- canned 'Evidence status: INCOMPLETE' replies: {o['canned_incomplete_replies']}")
    print(f"- avg claim-to-publish: {o['avg_claim_to_publish_min']} min\n")
    print("## Runs")
    for r in report["runs"][:limit]:
        print(f"- {r['TicketNo']}: {r['ProcessStatus']} {r['ResponseType'] or ''} "
              f"[{r['LocalModelPurpose'] or '-'}/{r['LocalModelState'] or '-'}]")
    if report["failure_reasons"]:
        print("\nFailed-run reasons:")
        for f in report["failure_reasons"]:
            print(f"- {f['Runs']:>3}  {f['Reason']}")
    print("\n## Tool health")
    for t in report["tool_health"]["per_tool"]:
        print(f"- {t['ToolName']}: {t['Calls']} calls, {t['Failed']} failed")
    print("\nTop failure causes:")
    for c in report["tool_health"]["top_failure_causes"]:
        print(f"- {c['count']:>3}  {c['cause']}")
    print(f"\n## Small-model waste\n- {report['waste']}")
    print(f"\n## Worker card sizes (spill above {report['spill_threshold_chars']:,} chars)")
    for c in report["card_sizes"]:
        print(f"- {c['Purpose']}: {c['Cards']} cards, avg {c['AvgChars']:,}, max {c['MaxChars']:,}, over spill {c['OverSpill']}")
    card = report["largest_card"]
    if card:
        print(f"\nLargest {card['purpose']} card body {card['body_chars']:,} chars (spills above ~25K):")
        if card.get("context_compiler"):
            print(f"- context compiler: {card['context_compiler']}")
        for sec in card["sections"]:
            print(f"- {sec['chars']:>7,}  {sec['section']}")
    print("\n## Lifecycle invariants (must be 0)")
    for label, value in report["invariants"].items():
        print(f"- {'OK ' if value == 0 else 'BAD'} {value:>3}  {label}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--server", default=DEFAULT_SERVER)
    parser.add_argument("--database", default=DEFAULT_DATABASE)
    parser.add_argument("--user", default=DEFAULT_USER)
    parser.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    parser.add_argument("--since", help="server-local (IST) time, e.g. '2026-09-23 13:05'")
    parser.add_argument("--hours", type=float, default=6.0, help="window when --since is not given")
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    since = datetime.fromisoformat(args.since) if args.since else datetime.now() - timedelta(hours=args.hours)
    conn = get_db_connection(args.server, args.database, args.user, args.password)
    try:
        report = build_report(conn.cursor(), since)
    finally:
        conn.close()
    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print_markdown(report, args.limit)
    return 1 if any(report["invariants"].values()) else 0


if __name__ == "__main__":
    sys.exit(main())
