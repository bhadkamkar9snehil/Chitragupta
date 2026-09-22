#!/usr/bin/env python3
"""Split the XS Builder full schema+samples export into one GBrain-ready
markdown document per real XBatch table/view, cross-linked with the
relationships already captured in Knowledge/xstudio_semantic_atlas.json,
and prefixed with a grounded plain-language description.

Why this exists: candidate-table matching for investigations previously
relied on a ~60-entry hand-curated keyword file plus literal token overlap
over column names. Real schema+row-count+sample-data knowledge existed
(the semantic atlas, the XS Builder export) but was never turned into
individually retrievable, GBrain-searchable documents -- so semantic
retrieval had nothing to search. A first pass at this produced raw
column-name dumps with no natural-language description, which scored too
low against natural ticket wording (0.55-0.58, below the 0.70 production
threshold) even when the table was exactly the right one. This version
adds a "What this table is for" line per table, built only from grounded
signals (curated atlas domain descriptions, the curated keyword index,
and the table's own real column names) -- never invented.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SOURCE_EXPORT = Path(
    r"C:\Users\Admin\AppData\Local\Temp\claude\C--Users-Admin-Documents-Office-AIHelpdesk"
    r"\8e3b4e73-d355-4c01-9c82-3c46182d500f\scratchpad\XStudio_Xbatch_Schema_WithSamples.md"
)
ATLAS_PATH = REPO_ROOT / "Knowledge" / "xstudio_semantic_atlas.json"
KEYWORD_INDEX_PATH = REPO_ROOT / "Knowledge" / "table_keyword_index.json"
OUTPUT_DIR = REPO_ROOT / "Knowledge" / "xbatch_tables"

AUDIT_OR_SHADOW_SUFFIXES = ("_Audit",)
LIST_VIEW_PREFIX = "XStudio_List_"
UAT_PREFIX = "UAT_"

# Boilerplate columns every XStudio table carries; useless for describing
# what a table is actually FOR, so excluded from the column-token summary.
BOILERPLATE_COLUMNS = {
    "id", "createdby", "modifiedby", "createdon", "modifiedon", "isdeleted",
    "issystem", "assigneduserid", "hostaddress", "dbsyncstatus",
    "mobilesyncstatus", "source", "isprocessed", "name", "parentid",
    "entrydatetime", "reportdate",
}


def classify(table_name: str) -> str:
    bare = table_name.split(".")[-1]
    if bare.endswith(AUDIT_OR_SHADOW_SUFFIXES):
        return "audit_shadow"
    if bare.startswith(LIST_VIEW_PREFIX):
        return "reporting_view_duplicate"
    if bare.startswith(UAT_PREFIX):
        return "uat_test_artifact_not_production_data"
    return "production_data"


def load_relationships() -> dict[str, list[dict]]:
    atlas = json.loads(ATLAS_PATH.read_text(encoding="utf-8"))
    by_table: dict[str, list[dict]] = {}
    for rel in atlas.get("relationships", []):
        src = rel.get("source", {})
        tgt = rel.get("target", {})
        if src.get("object"):
            by_table.setdefault(src["object"], []).append(rel)
        if tgt.get("object"):
            by_table.setdefault(tgt["object"], []).append(rel)
    return by_table


def load_domain_map(atlas: dict) -> dict[str, list[dict]]:
    """Invert domains[*].preferred_live_objects -> {bare_table_name: [domain_info]}."""
    by_table: dict[str, list[dict]] = {}
    for domain_name, domain in atlas.get("domains", {}).items():
        for obj in domain.get("preferred_live_objects", []) or []:
            bare = str(obj).split(".")[-1]
            by_table.setdefault(bare.lower(), []).append({
                "domain": domain_name,
                "description": domain.get("description"),
                "keywords": domain.get("keywords") or [],
            })
    return by_table


def load_keyword_map() -> dict[str, list[str]]:
    """Invert table_keyword_index.json {keyword: [tables]} -> {bare_table: [keywords]}."""
    idx = json.loads(KEYWORD_INDEX_PATH.read_text(encoding="utf-8"))
    by_table: dict[str, list[str]] = {}
    for keyword, tables in idx.items():
        for t in tables:
            bare = str(t).split(".")[-1].lower()
            by_table.setdefault(bare, []).append(keyword)
    return by_table


def split_identifier(name: str) -> list[str]:
    # CamelCase / underscore / digit-boundary splitter, same intent as the
    # mechanical scorer in Hermes_Orchestrator.py so tokens line up.
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
    s = s.replace("_", " ")
    return [t for t in re.findall(r"[A-Za-z]+", s) if len(t) > 2]


def column_summary(schema_block: str) -> list[str]:
    """Extract the real column names from a table's '### Schema' markdown
    table and return the top distinct meaningful tokens, most-frequent first.
    """
    columns = re.findall(r"^\|\s*([A-Za-z0-9_]+)\s*\|", schema_block, re.MULTILINE)
    counts: dict[str, int] = {}
    for col in columns:
        if col.lower() in BOILERPLATE_COLUMNS or col.lower() == "column":
            continue
        for tok in split_identifier(col):
            key = tok.lower()
            counts[key] = counts.get(key, 0) + 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [tok for tok, _ in ranked[:12]]


def build_description(
    bare_table: str,
    schema_block: str,
    domain_map: dict[str, list[dict]],
    keyword_map: dict[str, list[str]],
) -> str:
    domain_hits = domain_map.get(bare_table.lower(), [])
    keyword_hits = sorted(set(keyword_map.get(bare_table.lower(), [])))
    top_tokens = column_summary(schema_block)

    lines = ["", "### What this table is for", ""]

    if domain_hits:
        for hit in domain_hits:
            lines.append(
                f"- **Curated domain match ({hit['domain']}):** {hit['description']}"
            )
        lines.append(
            "  (source: `Knowledge/xstudio_semantic_atlas.json` domains, "
            "human-curated, not inferred)"
        )
    if keyword_hits:
        lines.append(
            f"- **Indexed under investigation keywords:** {', '.join(keyword_hits)} "
            "(source: `Knowledge/table_keyword_index.json`, human-curated)"
        )
    if top_tokens:
        lines.append(
            f"- **Inferred from its own column names** (not human-verified): "
            f"columns repeatedly reference {', '.join(top_tokens)}."
        )
    if not domain_hits and not keyword_hits and not top_tokens:
        lines.append(
            "- No curated business description or distinguishing column vocabulary "
            "found for this table; treat as low-confidence for semantic matching."
        )

    return "\n".join(lines) + "\n"


def format_relationships(bare_table: str, rel_index: dict[str, list[dict]]) -> str:
    rels = rel_index.get(bare_table, [])
    if not rels:
        return ""
    lines = ["", "### Known relationships (from Knowledge/xstudio_semantic_atlas.json)", ""]
    seen = set()
    for rel in rels[:20]:
        src = rel.get("source", {})
        tgt = rel.get("target", {})
        line = (
            f"- `{src.get('database')}.{src.get('object')}.{src.get('attribute')}` -> "
            f"`{tgt.get('database')}.{tgt.get('object')}.{tgt.get('attribute')}` "
            f"({rel.get('cardinality', {}).get('source', '?')} to "
            f"{rel.get('cardinality', {}).get('target', '?')})"
        )
        if line not in seen:
            seen.add(line)
            lines.append(line)
    return "\n".join(lines)


def main() -> None:
    text = SOURCE_EXPORT.read_text(encoding="utf-8")
    marker = "## Detailed Table Information"
    idx = text.index(marker)
    body = text[idx + len(marker):]

    sections = re.split(r"\n(?=## dbo\.)", body)
    atlas = json.loads(ATLAS_PATH.read_text(encoding="utf-8"))
    rel_index = load_relationships()
    domain_map = load_domain_map(atlas)
    keyword_map = load_keyword_map()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    kind_counts: dict[str, int] = {}
    described_counts = {"domain": 0, "keyword": 0, "columns_only": 0, "none": 0}

    for section in sections:
        section = section.strip("\n")
        if not section.startswith("## dbo."):
            continue
        first_line_end = section.index("\n")
        header = section[3:first_line_end].strip()  # "dbo.TableName"
        table_only = header.split(".", 1)[-1]
        kind = classify(header)
        kind_counts[kind] = kind_counts.get(kind, 0) + 1

        body_text = section[first_line_end + 1:].strip()
        rel_block = format_relationships(table_only, rel_index)
        desc_block = build_description(table_only, body_text, domain_map, keyword_map)

        if domain_map.get(table_only.lower()):
            described_counts["domain"] += 1
        elif keyword_map.get(table_only.lower()):
            described_counts["keyword"] += 1
        elif "columns repeatedly reference" in desc_block:
            described_counts["columns_only"] += 1
        else:
            described_counts["none"] += 1

        doc = (
            f"# XStudio_Xbatch.{header}\n\n"
            f"**table_kind:** {kind}\n"
            + desc_block
            + (
                "\n> NOTE: this table's rows are manual UAT/test-signoff checklist "
                "entries (Q1/Q2/Q3 verdict columns), not live production telemetry. "
                "Do not treat its contents as real plant data.\n"
                if kind == "uat_test_artifact_not_production_data" else ""
            )
            + (
                "\n> NOTE: this is a generated audit-history shadow of another table. "
                "Prefer the base table unless the investigation specifically needs "
                "change history.\n"
                if kind == "audit_shadow" else ""
            )
            + "\n" + body_text
            + ("\n" + rel_block + "\n" if rel_block else "\n")
        )

        out_path = OUTPUT_DIR / f"{table_only}.md"
        out_path.write_text(doc, encoding="utf-8")
        written += 1

    print(f"Wrote {written} per-table documents to {OUTPUT_DIR}")
    print("Breakdown by table_kind:", kind_counts)
    print("Breakdown by description source:", described_counts)


if __name__ == "__main__":
    main()
