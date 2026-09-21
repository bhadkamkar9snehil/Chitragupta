#!/usr/bin/env python3
"""Post-resolution Jev knowledge-curation suggestions.

This job never creates, updates, promotes, or links a Solution article. It
produces auditable REUSE_EXISTING / UPDATE_EXISTING / CREATE_CANDIDATE / NONE
judgments for verified resolved runs so KB governance can act separately.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

import pyodbc

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Model_Bench.jev.audit import persist_rows, rows_for_result
from Model_Bench.jev.client import typesafe_available
from Model_Bench.jev.candidate_rerank import rerank_candidates
from Model_Bench.jev.kb_curation import assess_curation
from Model_Bench.jev.policy import KB_JUDGMENTS_ENABLED

SERVER = os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
DATABASE = os.environ.get("MSSQL_MCP_DATABASE", "XStudio_Helpdesk")
USERNAME = os.environ.get("MSSQL_MCP_USER", "sa")
PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")


def connect():
    if not PASSWORD:
        raise RuntimeError("MSSQL_MCP_PASSWORD is required")
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};"
        "TrustServerCertificate=yes;Encrypt=no;",
        timeout=10,
    )


def _dict_rows(cur) -> list[dict[str, Any]]:
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def pending_resolutions(cur, top: int = 20) -> list[dict[str, Any]]:
    cur.execute(
        """
        SELECT TOP (?)
            r.ID AS RunID, r.TicketID, r.Route, r.ResponseType,
            r.ProblemSummary, r.Findings, r.RootCause, r.Resolution, r.ReplyText,
            r.InvestigationJson, r.CompletedOn,
            c.TicketNo, c.BriefDetails, c.Description, c.ProblemCategory
        FROM dbo.Hermes_L2_Response_Trn_Tbl r
        JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
        WHERE r.IsDeleted = 0
          AND r.ResponseType = 'RESOLUTION'
          AND r.CompletedOn IS NOT NULL
          AND NULLIF(LTRIM(RTRIM(r.RootCause)), '') IS NOT NULL
          AND NOT EXISTS (
              SELECT 1 FROM dbo.Hermes_Jev_Judgment_Trn_Tbl j
              WHERE j.RunID = r.ID AND j.Stage = 'POST_RESOLUTION_KB'
                AND j.IsDeleted = 0
          )
        ORDER BY r.CompletedOn ASC;
        """,
        top,
    )
    return _dict_rows(cur)


def candidate_articles(cur, run: dict[str, Any], top: int = 8) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    route = run.get("Route")
    cur.execute(
        """
        SELECT TOP 24
            ID, Title, ProblemSummary, RootCause, ResolutionSteps, Route, Tags,
            UsageCount, CreatedOn, ModifiedOn, KnowledgeType, ArticleStatus,
            CanonicalKey, RevisionNo, LastVerifiedOn, ApplicabilityJson,
            NegativeIndicatorsJson, VerificationJson, DiagnosticSteps,
            VerificationSteps, ExpectedResult
        FROM dbo.Hermes_Solution_Article_Mst_Tbl
        WHERE IsDeleted = 0
          AND ArticleStatus IN ('Approved','Candidate')
        ORDER BY
            CASE WHEN Route = ? THEN 0 ELSE 1 END,
            UsageCount DESC,
            COALESCE(ModifiedOn, CreatedOn) DESC;
        """,
        route,
    )
    pool = _dict_rows(cur)
    query = " ".join(str(run.get(k) or "") for k in (
        "ProblemSummary", "RootCause", "Resolution", "Findings", "Route"
    )).strip()
    rerank = rerank_candidates(
        query,
        pool,
        top=min(top, len(pool) or top),
        candidate_kind="existing governed Solution article",
    )
    return (list(rerank.get("ranked") or pool[:top]), rerank)


def main() -> int:
    if not KB_JUDGMENTS_ENABLED:
        print("Jev KB judgments disabled.")
        return 0
    if not typesafe_available():
        print("TypeSafe Jev credential not configured; skipping Jev KB curation.")
        return 0

    conn = connect()
    assessed = 0
    try:
        cur = conn.cursor()
        for run in pending_resolutions(cur):
            candidates, rerank = candidate_articles(cur, run)
            if rerank.get("ok"):
                persist_rows(rows_for_result(
                    result=rerank,
                    stage="POST_RESOLUTION_KB_RERANK",
                    state={"run": str(run["RunID"]), "candidate_count": len(candidates)},
                    ticket_id=str(run["TicketID"]),
                    run_id=str(run["RunID"]),
                ))
            state = {
                "verified_resolution": {
                    "route": run.get("Route"),
                    "problem_summary": run.get("ProblemSummary"),
                    "findings": run.get("Findings"),
                    "root_cause": run.get("RootCause"),
                    "resolution": run.get("Resolution"),
                    "reply_text": run.get("ReplyText"),
                    "investigation": run.get("InvestigationJson"),
                },
                "ticket": {
                    "ticket_no": run.get("TicketNo"),
                    "brief_details": run.get("BriefDetails"),
                    "description": run.get("Description"),
                    "problem_category": run.get("ProblemCategory"),
                },
                "existing_articles": candidates,
                "governance": {
                    "single_resolved_ticket_auto_approves_article": False,
                    "candidate_requires_governance": True,
                    "vector_or_semantic_similarity_never_auto_merges": True,
                },
            }
            result = assess_curation(state)
            if not result.get("ok"):
                print(f"Jev KB curation unavailable for {run['RunID']}: {result.get('reason')}")
                continue
            audit = persist_rows(rows_for_result(
                result=result,
                stage="POST_RESOLUTION_KB",
                state=state,
                ticket_id=str(run["TicketID"]),
                run_id=str(run["RunID"]),
            ))
            assessed += int(audit.get("persisted") or 0) > 0
            disp = (result.get("answers") or {}).get("curation_disposition") or {}
            print(f"Jev KB curation {run['RunID']}: {disp.get('choice')} ({disp.get('confidence')})")
    finally:
        conn.close()
    print(f"Jev KB curation complete: {assessed} newly assessed resolution(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
