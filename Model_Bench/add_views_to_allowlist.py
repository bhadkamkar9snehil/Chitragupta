#!/usr/bin/env python3
"""Extend schema_allowlist.json with real SQL views -- a known gap flagged
earlier this project ("SchemaExporter.py covers tables, not views") and
confirmed costly 2026-09-03: 960 real views exist across both databases
(666 in XStudio_Xbatch, 294 in XStudio_Helpdesk), completely absent from
the allowlist, meaning validate_identifiers.py would wrongly flag any of
them as hallucinated and --query's auto-suggestion would never point an
investigator toward one. Several are exactly the comprehensive,
pre-joined views investigations have been reconstructing badly by hand
via ad-hoc base-table queries (e.g. XBatch_Tracability_Heat_Details_Vw).

Queries live via INFORMATION_SCHEMA (read-only, same discipline as every
other script here) rather than re-running the full markdown export
pipeline -- faster, and this allowlist only needs names/columns, not the
full documentation SchemaExporter.py produces.

Usage:
    python add_views_to_allowlist.py --server 10.2.6.204
"""
import os
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

ALLOWLIST_PATH = Path(__file__).parent.parent / "Knowledge" / "schema_allowlist.json"
DATABASES = ["XStudio_Helpdesk", "XStudio_Xbatch"]


def fetch_views(server, database, username, password):
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes"
    )
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT v.TABLE_NAME, c.COLUMN_NAME
            FROM INFORMATION_SCHEMA.VIEWS v
            JOIN INFORMATION_SCHEMA.COLUMNS c
              ON c.TABLE_NAME = v.TABLE_NAME AND c.TABLE_SCHEMA = v.TABLE_SCHEMA
            ORDER BY v.TABLE_NAME, c.ORDINAL_POSITION
        """)
        views = {}
        for table_name, col_name in cur.fetchall():
            qname = f"dbo.{table_name}"
            views.setdefault(qname, []).append(col_name)
        return views
    finally:
        conn.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    args = ap.parse_args()

    allowlist = json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8")) if ALLOWLIST_PATH.exists() else {}

    for database in DATABASES:
        views = fetch_views(args.server, database, args.username, args.password)
        allowlist.setdefault(database, {})
        allowlist[database].update(views)
        print(f"{database}: added {len(views)} views")

    ALLOWLIST_PATH.write_text(json.dumps(allowlist, indent=2), encoding="utf-8")
    total_tables = sum(1 for db in allowlist.values() for k in db)
    print(f"\nWrote {ALLOWLIST_PATH} -- {total_tables} total tables+views across {len(allowlist)} database(s).")


if __name__ == "__main__":
    main()
