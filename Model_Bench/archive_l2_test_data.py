#!/usr/bin/env python3
"""Operator tool: archive seeded/test tickets and everything the L2 pipeline wrote about them.

Every affected row is copied into XStudio_Helpdesk.archive.<table>_<stamp> and then removed from dbo,
in one transaction. Configuration/master tables (root-cause categories, action catalog, escalation
rules) are untouched. Tickets are selected by Source (seeders write 'T-SQL'; the L1 chat writes
'L1-Chat'), so real Helpdesk tickets are never touched. Dry run by default.

    python Model_Bench/archive_l2_test_data.py            # show what would move
    python Model_Bench/archive_l2_test_data.py --apply
"""
from __future__ import annotations

import argparse
import datetime
import os

import pyodbc

TEST_SOURCES = ("T-SQL",)
# Tables the pipeline writes per ticket/run: everything in them is derived from test traffic.
RUN_TABLES = ("Hermes_L2_Response_Trn_Tbl", "Hermes_L2_SQL_Action_Trn_Tbl", "Hermes_Ticket_Activity_Trn_Tbl",
              "Hermes_L3_Escalation_Trn_Tbl", "Hermes_Agent_Trace_Trn_Tbl", "Hermes_Solution_Article_Mst_Tbl",
              "Hermes_Ticket_Feedback_Trn_Tbl", "Hermes_Ticket_Solution_Link_Tbl", "Hermes_Problem_Mst_Tbl",
              "Hermes_Problem_Ticket_Link_Tbl")
# Leftover whole tables: moved into the archive schema as they are.
LEFTOVER_TABLES = ("Hermes_L2_Response_Trn_Tbl_OldTickets_Backup",)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    conn = pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=" + os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
                          + ";UID=" + os.environ.get("MSSQL_MCP_USER", "sa") + ";PWD=" + os.environ["MSSQL_MCP_PASSWORD"]
                          + ";TrustServerCertificate=yes;DATABASE=XStudio_Helpdesk;", autocommit=False)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE IsActive = 1 AND IsDeleted = 0")
    if cur.fetchone()[0]:
        raise SystemExit("refusing: an L2 run is active; wait for it to finish")
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    sources = ",".join(f"'{s}'" for s in TEST_SOURCES)
    plan = [("Complaint_Mst_Tbl", f"Source IN ({sources})")] + [(t, "1 = 1") for t in RUN_TABLES]
    for table, where in plan:
        cur.execute(f"SELECT COUNT(*) FROM dbo.[{table}] WHERE {where}")
        print(f"{table:48} {cur.fetchone()[0]:>7} row(s) -> archive.{table}_{stamp}")
    for table in LEFTOVER_TABLES:
        print(f"{table:48} whole table -> archive.{table}")
    if not args.apply:
        print("dry run: pass --apply to move them")
        return 0
    cur.execute("IF SCHEMA_ID('archive') IS NULL EXEC('CREATE SCHEMA archive')")
    for table, where in plan:
        cur.execute(f"SELECT * INTO archive.[{table}_{stamp}] FROM dbo.[{table}] WHERE {where}")
        cur.execute(f"DELETE FROM dbo.[{table}] WHERE {where}")
    for table in LEFTOVER_TABLES:
        cur.execute(f"IF OBJECT_ID('dbo.[{table}]') IS NOT NULL ALTER SCHEMA archive TRANSFER dbo.[{table}]")
    conn.commit()
    print(f"archived; tables archive.*_{stamp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
