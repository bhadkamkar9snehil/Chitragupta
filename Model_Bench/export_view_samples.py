#!/usr/bin/env python3
"""Export real column definitions + top-N sample rows for XStudio_Xbatch/
Helpdesk views -- the same "what does this actually contain" documentation
SchemaExporter.py already does for tables, extended to the 960 real views
that script never covered (a known, previously-flagged gap).

Given 960 views total, this is deliberately NOT a one-shot "export
everything" script -- pass specific view names (or a name-LIKE pattern) so
documentation grows around what's actually proven useful for L2
investigation, one confirmed-valuable view at a time, rather than
generating 960 mostly-unread files.

Usage:
    python export_view_samples.py --server 10.2.6.204 --database XStudio_Xbatch VIEW_NAME [VIEW_NAME ...]
    python export_view_samples.py --server 10.2.6.204 --database XStudio_Xbatch --like "%Tracability%"
"""
import os
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

OUTPUT_DIR = Path(r"C:\Users\Admin\Documents\Office\AIHelpdesk\Knowledge\view_docs")


def build_connection(server, database, username, password):
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes"
    )


def resolve_view_names(cur, names, like_pattern):
    if like_pattern:
        cur.execute("SELECT name FROM sys.views WHERE name LIKE ? ORDER BY name", like_pattern)
        return [r[0] for r in cur.fetchall()]
    return names


def document_view(cur, database, view_name, top_n):
    lines = [f"# {database}.dbo.{view_name}", ""]

    cur.execute(
        "SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS "
        "WHERE TABLE_NAME = ? ORDER BY ORDINAL_POSITION", view_name,
    )
    cols = cur.fetchall()
    if not cols:
        return None  # not a real view/table in this database

    lines.append("## Columns\n")
    lines.append("| Column | Type | Nullable |")
    lines.append("|---|---|---|")
    for col_name, data_type, nullable in cols:
        lines.append(f"| {col_name} | {data_type} | {nullable} |")

    lines.append(f"\n## Sample rows (top {top_n}, real live data)\n")
    try:
        cur.execute(f"SELECT TOP {top_n} * FROM dbo.[{view_name}]")
        rows = cur.fetchall()
        col_names = [d[0] for d in cur.description]
        if rows:
            lines.append("| " + " | ".join(col_names) + " |")
            lines.append("|" + "---|" * len(col_names))
            for row in rows:
                cells = ["" if v is None else str(v)[:80].replace("\n", " ").replace("|", "/") for v in row]
                lines.append("| " + " | ".join(cells) + " |")
        else:
            lines.append("*(view returned zero rows -- either genuinely empty or requires specific filter criteria)*")
    except pyodbc.Error as e:
        lines.append(f"*(could not sample rows: {str(e)[:300]})*")

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Xbatch")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--top-n", type=int, default=5)
    ap.add_argument("--like", default=None, help="SQL LIKE pattern to select views by name instead of listing them")
    ap.add_argument("names", nargs="*", help="Specific view names to document")
    args = ap.parse_args()

    if not args.names and not args.like:
        ap.error("pass specific view names or --like PATTERN")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    conn = build_connection(args.server, args.database, args.username, args.password)
    try:
        cur = conn.cursor()
        names = resolve_view_names(cur, args.names, args.like)
        if not names:
            print("No matching views found.")
            return

        for name in names:
            doc = document_view(cur, args.database, name, args.top_n)
            if doc is None:
                print(f"  {name}: not found, skipping")
                continue
            out_path = OUTPUT_DIR / f"{args.database}.{name}.md"
            out_path.write_text(doc, encoding="utf-8")
            print(f"  {name} -> {out_path}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
