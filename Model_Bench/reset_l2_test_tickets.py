#!/usr/bin/env python3
"""Operator tool: return test tickets to the eligible queue for a fresh end-to-end L2 run.

For each named ticket: back up the ticket row, its Hermes runs and L3 rows to a JSON
file, soft-delete the runs and L3 rows (IsDeleted=1, reversible), and reset the ticket
to Status/AskStatus 'Enter' with bot-mirrored remarks cleared, so no earlier reply can
bias the rerun. Refuses tickets that have an active run. One transaction.

Dry run by default; pass --apply to write.

    python Model_Bench/reset_l2_test_tickets.py Ticket_318 Ticket_315
    python Model_Bench/reset_l2_test_tickets.py Ticket_318 Ticket_315 --apply
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
from pathlib import Path

import pyodbc

BACKUP_DIR = Path(__file__).resolve().parent / "results" / "ticket_resets"


def _rows(cur, sql: str, *params) -> list[dict]:
    cur.execute(sql, *params)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, r)) for r in cur.fetchall()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tickets", nargs="+", help="TicketNo values, e.g. Ticket_318")
    ap.add_argument("--apply", action="store_true", help="write the reset (default: dry run)")
    args = ap.parse_args()

    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.environ.get('MSSQL_MCP_SERVER', '10.2.6.204')};DATABASE=XStudio_Helpdesk;"
        f"UID={os.environ.get('MSSQL_MCP_USER', 'sa')};PWD={os.environ['MSSQL_MCP_PASSWORD']};"
        "TrustServerCertificate=yes;Connection Timeout=60",
        autocommit=False,
    )
    cur = conn.cursor()
    marks = ",".join("?" * len(args.tickets))
    tickets = _rows(cur, f"SELECT * FROM dbo.Complaint_Mst_Tbl WHERE TicketNo IN ({marks}) AND IsDeleted = 0",
                    *args.tickets)
    if not tickets:
        print("no matching tickets")
        return 1
    ids = [t["ID"] for t in tickets]
    idm = ",".join("?" * len(ids))
    active = _rows(cur, f"SELECT TicketID FROM dbo.Hermes_L2_Response_Trn_Tbl "
                        f"WHERE TicketID IN ({idm}) AND IsActive = 1 AND IsDeleted = 0", *ids)
    if active:
        print(f"refusing: active runs on {sorted({str(a['TicketID']) for a in active})}")
        return 1
    runs = _rows(cur, f"SELECT * FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE TicketID IN ({idm}) AND IsDeleted = 0", *ids)
    l3 = _rows(cur, f"SELECT * FROM dbo.Hermes_L3_Escalation_Trn_Tbl WHERE TicketID IN ({idm}) AND IsDeleted = 0", *ids)
    print(f"{len(tickets)} ticket(s), {len(runs)} run(s), {len(l3)} L3 row(s): "
          + ", ".join(f"{t['TicketNo']}={t['Status']}" for t in tickets))
    if not args.apply:
        print("dry run; pass --apply to reset")
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup = BACKUP_DIR / f"reset_{datetime.datetime.now():%Y%m%d_%H%M%S}.json"
    backup.write_text(json.dumps({"tickets": tickets, "runs": runs, "l3": l3}, default=str, indent=1),
                      encoding="utf-8")
    cur.execute(f"UPDATE dbo.Hermes_L2_Response_Trn_Tbl SET IsDeleted = 1, IsActive = 0, ModifiedOn = GETDATE() "
                f"WHERE TicketID IN ({idm}) AND IsDeleted = 0", *ids)
    cur.execute(f"UPDATE dbo.Hermes_L3_Escalation_Trn_Tbl SET IsDeleted = 1, ModifiedOn = GETDATE() "
                f"WHERE TicketID IN ({idm}) AND IsDeleted = 0", *ids)
    cur.execute(f"UPDATE dbo.Complaint_Mst_Tbl SET Status = 'Enter', AskStatus = 'Enter', "
                f"SupportExecutiveRemarks = NULL, AskRemarks = NULL, ReplyRemarks = NULL, ModifiedOn = GETDATE() "
                f"WHERE ID IN ({idm})", *ids)
    conn.commit()
    print(f"reset applied; backup {backup}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
