#!/usr/bin/env python3
"""Check a table name (and optionally column names) against the real,
live-exported schema in schema_allowlist.json before trusting it in any
SQL or ticket-response text.

Ground truth source: Reference Documents/*_Schema.md (SchemaExporter.py
output), indexed by Model_Bench/build_schema_allowlist.py. Regenerate the
index after any schema change: `python Model_Bench/build_schema_allowlist.py`.

Usage:
    python validate_identifiers.py <table_name> [column1 column2 ...]
    python validate_identifiers.py dbo.Complaint_Mst_Tbl ProblemCategory SourceSystem
    python validate_identifiers.py COMPLAIN_MST_TBL          # hallucination -> suggestion

Exit code 0 = table (and all given columns) verified real. Exit code 1 =
unknown table/column, with closest-match suggestions -- do not use the name
until this passes.
"""
import difflib
import json
import sys
from pathlib import Path

ALLOWLIST_PATH = Path(__file__).parent / "schema_allowlist.json"


def load_allowlist():
    if not ALLOWLIST_PATH.exists():
        print(f"ERROR: {ALLOWLIST_PATH} missing. Run build_schema_allowlist.py first.")
        sys.exit(2)
    return json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8"))


def normalize(name: str) -> str:
    return name.split(".")[-1].lower()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)

    table_arg = sys.argv[1]
    columns_arg = sys.argv[2:]
    allowlist = load_allowlist()

    # Flat index: normalized table name -> (db, real_qualified_name, columns)
    flat = {}
    for db, tables in allowlist.items():
        for qname, cols in tables.items():
            flat[normalize(qname)] = (db, qname, cols)

    target = normalize(table_arg)
    ok = True

    if target not in flat:
        ok = False
        all_names = list(flat.keys())
        suggestions = difflib.get_close_matches(target, all_names, n=3, cutoff=0.5)
        print(f"UNKNOWN TABLE: {table_arg!r} does not match any real table.")
        if suggestions:
            for s in suggestions:
                db, qname, _ = flat[s]
                print(f"  did you mean: {qname}  (in {db})?")
        else:
            print("  no close match found -- this table name does not exist in the real schema")
    else:
        db, qname, real_columns = flat[target]
        print(f"OK: table {qname} verified real (in {db}, {len(real_columns)} columns)")
        real_cols_lower = {c.lower(): c for c in real_columns}
        for col in columns_arg:
            if col.lower() not in real_cols_lower:
                ok = False
                suggestions = difflib.get_close_matches(col.lower(), real_cols_lower.keys(), n=3, cutoff=0.5)
                print(f"UNKNOWN COLUMN: {col!r} is not a real column of {qname}.")
                if suggestions:
                    for s in suggestions:
                        print(f"  did you mean: {real_cols_lower[s]}?")
                else:
                    print(f"  no close match -- real columns of {qname}: {', '.join(real_columns[:15])}"
                          f"{' ...' if len(real_columns) > 15 else ''}")
            else:
                print(f"OK: column {real_cols_lower[col.lower()]} verified real")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
