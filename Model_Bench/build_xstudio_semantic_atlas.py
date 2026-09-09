#!/usr/bin/env python3
"""Compile authoritative schema/SP exports into a deterministic XStudio atlas.

The atlas is routing knowledge, never ticket evidence. Procedure safety is
deliberately conservative: observed writes are MUTATING; reviewed diagnostics
are READ_ONLY; everything else stays UNKNOWN_UNSAFE and cannot be executed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "Reference Documents"
SOURCES = {
    "XStudio_Helpdesk": {
        "schema": REFERENCE / "XStudio_Helpdesk_Schema.md",
        "procedures": REFERENCE / "XStudio_Helpdesk_StoredProcedures.md",
    },
    "XStudio_Xbatch": {
        "schema": REFERENCE / "XStudio_Xbatch_Schema.md",
        "procedures": REFERENCE / "XStudio_Xbatch_StoredProcedures.md",
    },
}
RELATIONSHIP_SOURCE = REFERENCE / "XStudio_Configuration_Xbatch_Relationships.json"
MANIFEST_SOURCE = ROOT / "Knowledge" / "manifest.json"
RECIPE_SOURCE = ROOT / "Knowledge" / "xbatch_investigation_recipes.json"
REVIEWED_READ_ONLY = {("XStudio_Xbatch", "XMES_Get_API_Transaction_Summary")}
WRITE_RE = re.compile(r"\b(?:INSERT|UPDATE|DELETE|MERGE|TRUNCATE|ALTER|CREATE|DROP)\b", re.I)
OBJECT_RE = re.compile(
    r"(?:(?:\[?([A-Za-z0-9_]+)\]?\.)?\[?dbo\]?\.)\[?([A-Za-z_][A-Za-z0-9_]*)\]?",
    re.I,
)

RELATIONSHIP_FIELDS = (
    "source_database", "source_object", "source_attribute", "target_database",
    "target_object", "target_attribute", "source_cardinality", "target_cardinality",
)


def load_relationships(path: Path = RELATIONSHIP_SOURCE) -> list[dict[str, Any]]:
    """Validate and collapse the configuration relationship snapshot."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("relationships")
    if not isinstance(rows, list):
        raise ValueError("relationship snapshot must contain a relationships array")
    grouped: dict[tuple[str, ...], list[dict[str, Any]]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"relationship row {index} must be an object")
        missing = [field for field in RELATIONSHIP_FIELDS if not str(row.get(field) or "").strip()]
        if missing:
            raise ValueError(f"relationship row {index} missing required fields: {', '.join(missing)}")
        key = tuple(str(row[field]).strip().casefold() for field in RELATIONSHIP_FIELDS)
        grouped.setdefault(key, []).append(row)

    normalized = []
    for key, duplicates in sorted(grouped.items()):
        row = duplicates[0]
        stable = json.dumps(list(key), separators=(",", ":"))
        normalized.append({
            "id": "rel_" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:16],
            "name": str(row.get("relation_name") or "").strip() or None,
            "source": {
                "database": str(row["source_database"]).strip(),
                "object": str(row["source_object"]).strip(),
                "attribute": str(row["source_attribute"]).strip(),
            },
            "target": {
                "database": str(row["target_database"]).strip(),
                "object": str(row["target_object"]).strip(),
                "attribute": str(row["target_attribute"]).strip(),
            },
            "cardinality": {
                "source": str(row["source_cardinality"]).strip(),
                "target": str(row["target_cardinality"]).strip(),
            },
            "provenance": {
                "kind": "xstudio_configuration_relationship",
                "source": payload.get("source"),
                "source_row_count": len(duplicates),
                "source_row_ids": sorted(str(item.get("source_row_id") or "") for item in duplicates),
                "source_attribute_resolution": row.get("source_attribute_resolution", "attribute_catalog"),
            },
        })
    return normalized


def _sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^## dbo\.([^\r\n]+)\s*$", text))
    return [
        (match.group(1).strip(), text[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(text)])
        for i, match in enumerate(matches)
    ]


def _table_rows(block: str, heading: str) -> list[list[str]]:
    match = re.search(rf"(?ms)^### {re.escape(heading)}\s*$\s*(.*?)(?=^### |^---\s*$|\Z)", block)
    if not match:
        return []
    rows = []
    for line in match.group(1).splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*---", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] not in {"Column", "Parameter"}:
            rows.append(cells)
    return rows


def parse_schema(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig")
    objects = {}
    for name, block in _sections(text):
        columns = []
        for row in _table_rows(block, "Schema"):
            if len(row) >= 3:
                columns.append({"name": row[0], "type": row[1], "nullable": row[2] == "YES"})
        row_count = re.search(r"\*\*Row Count:\*\*\s*([0-9,]+)", block)
        objects[name] = {
            "schema": "dbo", "columns": columns,
            "documented_row_count": int(row_count.group(1).replace(",", "")) if row_count else None,
        }
    return {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "objects": objects}


def _definition(block: str) -> str:
    match = re.search(r"(?ms)^### Full Definition\s*$.*?```sql\s*(.*?)```", block)
    return match.group(1) if match else ""


def parse_procedures(database: str, path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig")
    procedures = {}
    for name, block in _sections(text):
        definition = _definition(block)
        parameters = []
        for row in _table_rows(block, "Parameters"):
            if len(row) >= 3:
                parameters.append({"name": row[0].lstrip("@"), "type": row[1], "output": row[2] == "YES"})
        writes = sorted(set(token.upper() for token in WRITE_RE.findall(definition)))
        if (database, name) in REVIEWED_READ_ONLY:
            safety = "READ_ONLY_REVIEWED"
        elif writes:
            safety = "MUTATING"
        else:
            safety = "UNKNOWN_UNSAFE"
        refs = sorted({
            f"{db or database}.dbo.{obj}"
            for db, obj in OBJECT_RE.findall(definition)
            if obj.casefold() != name.casefold()
        }, key=lambda value: (value.casefold(), value))
        procedures[name] = {
            "schema": "dbo", "parameters": parameters, "safety": safety,
            "observed_write_tokens": writes, "referenced_objects": refs,
        }
    return {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "procedures": procedures}


def build() -> dict[str, Any]:
    databases = {}
    for database, paths in SOURCES.items():
        databases[database] = {
            **parse_schema(paths["schema"]),
            **parse_procedures(database, paths["procedures"]),
            "sources": {key: str(path.relative_to(ROOT)).replace("\\", "/") for key, path in paths.items()},
        }
    manifest = json.loads(MANIFEST_SOURCE.read_text(encoding="utf-8"))
    recipes = json.loads(RECIPE_SOURCE.read_text(encoding="utf-8"))["recipes"]
    recipes_by_id = {recipe["recipe_id"]: recipe for recipe in recipes}
    domains = {}
    for route in manifest.get("routes", []):
        recipe_id = route.get("recipe")
        if recipe_id not in recipes_by_id:
            raise ValueError(f"manifest route {route.get('route')} has unknown recipe {recipe_id}")
        domains[route["route"]] = {
            "description": route.get("description"),
            "keywords": route.get("keywords", []),
            "knowledge_documents": route.get("load", []),
            "preferred_live_objects": route.get("live_sql_leads", []),
            "recipe_id": recipe_id,
        }
    return {
        "schema_version": 2,
        "authority": "static routing/query-construction knowledge only; live reads are required for ticket claims",
        "procedure_policy": "Only READ_ONLY_REVIEWED procedures may be exposed by the bridge allowlist.",
        "databases": databases,
        "relationships": load_relationships(),
        "domains": domains,
        "recipes": recipes,
        "relationship_source": {
            "path": str(RELATIONSHIP_SOURCE.relative_to(ROOT)).replace("\\", "/"),
            "sha256": hashlib.sha256(RELATIONSHIP_SOURCE.read_bytes()).hexdigest(),
        },
        "catalog_sources": {
            "manifest": {"path": "Knowledge/manifest.json", "sha256": hashlib.sha256(MANIFEST_SOURCE.read_bytes()).hexdigest()},
            "recipes": {"path": "Knowledge/xbatch_investigation_recipes.json", "sha256": hashlib.sha256(RECIPE_SOURCE.read_bytes()).hexdigest()},
        },
    }


def render_gbrain_pages(atlas: dict[str, Any]) -> dict[str, str]:
    """Render compact searchable pages; the model never receives them wholesale."""
    pages: dict[str, str] = {}
    for database, data in atlas["databases"].items():
        schema_groups: dict[str, list[str]] = {}
        for name, item in data["objects"].items():
            columns = ", ".join(f"{col['name']}:{col['type']}" for col in item["columns"])
            key = name[0].lower() if name[:1].isalnum() else "other"
            schema_groups.setdefault(key, []).extend((f"## dbo.{name}", columns or "No exported columns.", ""))
        for key, lines in schema_groups.items():
            header = [
                "---", "type: note", "subtype: schema-reference", f"database: {database}",
                "authority: static-advisory", "---",
                f"# {database} schema atlas: {key.upper()}", "",
                "Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.", "",
            ]
            pages[f"{database.lower()}-schema-{key}-atlas.md"] = "\n".join(header + lines) + "\n"

        sp_groups: dict[str, list[str]] = {}
        for name, item in data["procedures"].items():
            params = ", ".join(f"@{p['name']}:{p['type']}" for p in item["parameters"]) or "none"
            refs = ", ".join(item["referenced_objects"]) or "none detected"
            key = name[0].lower() if name[:1].isalnum() else "other"
            sp_groups.setdefault(key, []).extend((
                f"## dbo.{name}", f"Safety: {item['safety']}", f"Parameters: {params}",
                f"Referenced objects: {refs}", "",
            ))
        for key, lines in sp_groups.items():
            header = [
                "---", "type: note", "subtype: procedure-reference", f"database: {database}",
                "authority: static-advisory", "---",
                f"# {database} stored-procedure atlas: {key.upper()}", "",
                "Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.", "",
            ]
            pages[f"{database.lower()}-procedure-{key}-atlas.md"] = "\n".join(header + lines) + "\n"

    relationship_groups: dict[str, list[list[str]]] = {}
    for edge in atlas.get("relationships", []):
        source = edge["source"]
        target = edge["target"]
        key = source["object"][0].lower() if source["object"][:1].isalnum() else "other"
        relationship_groups.setdefault(key, []).append([
            f"## {source['object']}.{source['attribute']} -> {target['object']}.{target['attribute']}",
            f"Databases: {source['database']} -> {target['database']}",
            f"Cardinality: {edge['cardinality']['source']} -> {edge['cardinality']['target']}",
            f"Relation: {edge.get('name') or edge['id']}",
            f"Provenance: {edge['provenance']['kind']} ({edge['provenance']['source_row_count']} source row(s))",
            "",
        ])
    relationship_page_size = 40
    for key, blocks in relationship_groups.items():
        for offset in range(0, len(blocks), relationship_page_size):
            part = offset // relationship_page_size + 1
            lines = [line for block in blocks[offset:offset + relationship_page_size] for line in block]
            header = [
                "---", "type: note", "subtype: configured-relationship",
                "database: XStudio_Configuration_Xbatch",
                "authority: configuration-observed", "---",
                f"# XBatch configured relationships: {key.upper()} part {part}", "",
                "Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.", "",
            ]
            pages[f"xstudio_xbatch-relationship-{key}-{part:02d}-atlas.md"] = (
                "\n".join(header + lines).rstrip() + "\n"
            )

    for recipe in atlas.get("recipes", []):
        evidence = ", ".join(item["category"] for item in recipe.get("required_evidence", [])) or "none"
        probes = ", ".join(item["tool"] for item in recipe.get("probes", [])) or "none"
        lines = [
            "---", "type: note", "subtype: investigation-recipe", f"route: {recipe['route']}",
            "authority: harness-contract", "---", f"# {recipe['description']}", "",
            f"Recipe ID: {recipe['recipe_id']}", f"Typed probes: {probes}",
            f"Required evidence: {evidence}", "", "## Interpretation rules",
            *[f"- {item}" for item in recipe.get("interpretation_rules", [])],
            "", "## Stop conditions", *[f"- {item}" for item in recipe.get("stop_conditions", [])],
            "", "## Escalation conditions", *[f"- {item}" for item in recipe.get("escalation_conditions", [])], "",
        ]
        pages[f"xstudio_xbatch-recipe-{recipe['route'].replace('_', '-')}.md"] = "\n".join(lines).rstrip() + "\n"
    return pages


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "Knowledge" / "xstudio_semantic_atlas.json")
    parser.add_argument("--markdown-dir", type=Path, default=ROOT / "Knowledge" / "atlas")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build(), indent=2, sort_keys=True) + "\n"
    pages = render_gbrain_pages(build())
    if args.check:
        json_ok = args.output.exists() and args.output.read_text(encoding="utf-8") == rendered
        pages_ok = all((args.markdown_dir / name).exists() and
                       (args.markdown_dir / name).read_text(encoding="utf-8") == content
                       for name, content in pages.items())
        return 0 if json_ok and pages_ok else 1
    args.output.write_text(rendered, encoding="utf-8", newline="\n")
    args.markdown_dir.mkdir(parents=True, exist_ok=True)
    for stale in args.markdown_dir.glob("*-atlas.md"):
        stale.unlink()
    for name, content in pages.items():
        (args.markdown_dir / name).write_text(content, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
