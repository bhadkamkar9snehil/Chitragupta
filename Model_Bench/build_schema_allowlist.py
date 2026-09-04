#!/usr/bin/env python3
"""Build a machine-checkable table/column allowlist from the real, live-exported
schema docs in `Reference Documents/`.

This is the ground truth this project already has (SchemaExporter.py output,
per the xstudio-db-export skill) -- this script just makes it queryable
instead of something an agent has to read and remember. Output feeds
validate_identifiers.py.

Usage:
    python build_schema_allowlist.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
REF_DIR = ROOT / "Reference Documents"
OUT_PATH = ROOT / "Knowledge" / "schema_allowlist.json"

SOURCES = {
    "XStudio_Helpdesk": REF_DIR / "XStudio_Helpdesk_Schema.md",
    "XStudio_Xbatch": REF_DIR / "XStudio_Xbatch_Schema.md",
}

TABLE_HEADER_RE = re.compile(r"^## (dbo\.\S+)\s*$", re.MULTILINE)
SCHEMA_ROW_RE = re.compile(r"^\|\s*([A-Za-z_][A-Za-z0-9_]*)\s*\|.*\|$", re.MULTILINE)


def parse_schema_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    tables = {}
    headers = list(TABLE_HEADER_RE.finditer(text))
    for i, m in enumerate(headers):
        table_name = m.group(1)
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block = text[start:end]
        schema_idx = block.find("### Schema")
        if schema_idx == -1:
            continue
        schema_block = block[schema_idx:]
        # Stop at the next ### section (Top 10 Records, Bottom 10 Records)
        next_section = schema_block.find("\n### ", 1)
        if next_section != -1:
            schema_block = schema_block[:next_section]
        columns = []
        for row_m in SCHEMA_ROW_RE.finditer(schema_block):
            col = row_m.group(1)
            if col in ("Column", "---"):
                continue
            columns.append(col)
        if columns:
            tables[table_name] = columns
    return tables


def main():
    allowlist = {}
    for db_name, path in SOURCES.items():
        if not path.exists():
            print(f"WARNING: {path} not found, skipping {db_name}")
            continue
        tables = parse_schema_file(path)
        allowlist[db_name] = tables
        print(f"{db_name}: {len(tables)} tables parsed from {path.name}")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(allowlist, indent=2), encoding="utf-8")
    total_tables = sum(len(t) for t in allowlist.values())
    total_cols = sum(len(cols) for t in allowlist.values() for cols in t.values())
    print(f"Wrote {OUT_PATH} -- {total_tables} tables, {total_cols} columns total")


if __name__ == "__main__":
    main()
