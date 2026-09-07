#!/usr/bin/env python3
"""Apply a reviewed SQL Server file using environment-held credentials."""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

import pyodbc


def batches(text: str) -> list[str]:
    return [
        part.strip() for part in re.split(r"^\s*GO\s*(?:--.*)?$", text, flags=re.I | re.M)
        if part.strip()
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sql_file", type=Path)
    parser.add_argument("--database", default="XStudio_Helpdesk")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    statements = batches(args.sql_file.read_text(encoding="utf-8-sig"))
    if args.dry_run:
        print(f"{args.sql_file}: {len(statements)} SQL batch(es) parsed")
        return
    password = os.environ.get("MSSQL_MCP_PASSWORD")
    if not password:
        raise SystemExit("MSSQL_MCP_PASSWORD is required")
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.environ.get('MSSQL_MCP_SERVER', '10.2.6.204')};DATABASE={args.database};"
        f"UID={os.environ.get('MSSQL_MCP_USER', 'sa')};PWD={password};TrustServerCertificate=yes"
    )
    try:
        cursor = conn.cursor()
        for index, statement in enumerate(statements, 1):
            try:
                cursor.execute(statement)
                while cursor.nextset():
                    pass
            except Exception as exc:
                conn.rollback()
                raise RuntimeError(f"SQL batch {index}/{len(statements)} failed") from exc
        conn.commit()
    finally:
        conn.close()
    print(f"Applied {len(statements)} SQL batch(es) from {args.sql_file}")


if __name__ == "__main__":
    main()
