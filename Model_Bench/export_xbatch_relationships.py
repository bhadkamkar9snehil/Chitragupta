#!/usr/bin/env python3
"""Export the active XBatch configuration relationship graph.

The output is a deterministic, non-secret source snapshot for the offline
semantic-atlas builder. Only configuration metadata is read.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

QUERY = """
SELECT
    r.ID AS source_row_id,
    'XStudio_XBatch' AS source_database,
    src.Name AS source_object,
    COALESCE(sa.Name,
        CASE WHEN CHARINDEX('-', r.RelationName) > 1
             THEN LEFT(r.RelationName, CHARINDEX('-', r.RelationName) - 1)
        END) AS source_attribute,
    r.RelationEntityDatabase AS target_database,
    COALESCE(NULLIF(r.RelationEntity, ''), dst.Name) AS target_object,
    COALESCE(NULLIF(r.RelationAttribute, ''), da.Name) AS target_attribute,
    r.Cardinality AS source_cardinality,
    r.RelationColumnCardinality AS target_cardinality,
    r.RelationName AS relation_name,
    CASE WHEN sa.Name IS NULL THEN 'relation_name_fallback' ELSE 'attribute_catalog' END
        AS source_attribute_resolution
FROM dbo.XStudio_EntityRelations_Mst_Tbl r
LEFT JOIN dbo.XStudio_Entities_Mst_Tbl src ON src.ID = r.EntityID
LEFT JOIN dbo.XStudio_Attribute_Mst_Tbl sa ON sa.ID = r.AttributeID
LEFT JOIN dbo.XStudio_Entities_Mst_Tbl dst ON dst.ID = r.RelationEntityID
LEFT JOIN dbo.XStudio_Attribute_Mst_Tbl da ON da.ID = r.RelationAttributeID
WHERE ISNULL(r.IsDeleted, 0) = 0
ORDER BY src.Name, source_attribute, target_database, target_object,
         target_attribute, r.ID
"""


def trust_server_certificate_value(value: str | None) -> str:
    return "yes" if str(value or "yes").strip().casefold() in {"1", "true", "yes", "on"} else "no"


def export(output: Path) -> int:
    import pyodbc

    server = os.environ["MSSQL_MCP_SERVER"]
    username = os.environ["MSSQL_MCP_USER"]
    password = os.environ["MSSQL_MCP_PASSWORD"]
    trust = trust_server_certificate_value(os.environ.get("MSSQL_MCP_TRUST_SERVER_CERTIFICATE"))
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};DATABASE=XStudio_Configuration_Xbatch;"
        f"UID={username};PWD={password};Encrypt=yes;TrustServerCertificate={trust};",
        timeout=30,
    )
    try:
        cursor = connection.cursor()
        cursor.execute(QUERY)
        names = [column[0] for column in cursor.description]
        rows = [dict(zip(names, row)) for row in cursor.fetchall()]
    finally:
        connection.close()
    payload = {
        "schema_version": 1,
        "source": "XStudio_Configuration_Xbatch.dbo.XStudio_EntityRelations_Mst_Tbl",
        "active_relationship_count": len(rows),
        "relationships": rows,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1] / "Reference Documents" /
        "XStudio_Configuration_Xbatch_Relationships.json",
    )
    args = parser.parse_args()
    print(json.dumps({"relationships": export(args.output), "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
