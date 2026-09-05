#!/usr/bin/env python3
"""Build Knowledge/table_keyword_index.json -- a mechanical keyword ->
real-table-name index used by Hermes_Orchestrator.py's suggest_tables_
mechanically() to narrow ~1200 tables down to the handful actually
relevant to a ticket's own text, without an LLM or embeddings.

Source of truth: the curated domain docs already in Knowledge/
(xbatch-investigation-surfaces.md, sohar-sms-event-workflows.md,
task-router.md) -- these already say, in prose, which real tables matter
for which kind of problem. This script doesn't invent new knowledge, it
extracts an existing structure: for each markdown heading, find every
real table/view name (validated against schema_allowlist.json, never a
name-guess) mentioned under it before the next heading, and index the
heading's own words as keywords pointing at those tables.

Re-run whenever a domain doc changes. Idempotent -- always a full
rebuild, never incremental.

Usage: python build_table_keyword_index.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
ALLOWLIST_PATH = ROOT / "Knowledge" / "schema_allowlist.json"
OUTPUT_PATH = ROOT / "Knowledge" / "table_keyword_index.json"
DOMAIN_DOCS = [
    ROOT / "Knowledge" / "xbatch-investigation-surfaces.md",
    ROOT / "Knowledge" / "sohar-sms-event-workflows.md",
    ROOT / "Knowledge" / "task-router.md",
]

_HEADING_RE = re.compile(r"^#{2,4}\s+(.+)$", re.MULTILINE)
_STOPWORDS = {
    "the", "a", "an", "is", "was", "and", "or", "for", "with", "this",
    "that", "on", "in", "at", "to", "of", "workflow", "workflows", "table",
    "tables", "view", "views", "family", "families", "surface", "surfaces",
}


def _load_real_table_names() -> dict:
    """lowercase bare name -> real qualified name, across both databases."""
    allowlist = json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8"))
    names = {}
    for db, tables in allowlist.items():
        for qname in tables:
            bare = qname.split(".")[-1]
            names[bare.lower()] = qname
    return names


def _heading_keywords(heading_text: str) -> list:
    words = re.findall(r"[A-Za-z][A-Za-z0-9]*", heading_text)
    return [w.lower() for w in words if len(w) > 2 and w.lower() not in _STOPWORDS]


def build_index() -> dict:
    real_names = _load_real_table_names()
    # Match any real table's bare name as a whole word in doc text --
    # sorted longest-first so a longer name isn't shadowed by a shorter
    # substring match (e.g. 'Heat' vs 'Heat_Chemistry_Trn_Tbl').
    name_pattern = re.compile(
        r"\b(" + "|".join(re.escape(n) for n in sorted(real_names, key=len, reverse=True)) + r")\b",
        re.IGNORECASE,
    )

    index: dict = {}
    for doc_path in DOMAIN_DOCS:
        if not doc_path.exists():
            print(f"SKIP (not found): {doc_path}")
            continue
        text = doc_path.read_text(encoding="utf-8")
        headings = list(_HEADING_RE.finditer(text))
        sections = []
        for i, m in enumerate(headings):
            start = m.end()
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            sections.append((m.group(1), text[start:end]))

        for heading_text, body in sections:
            keywords = _heading_keywords(heading_text)
            if not keywords:
                continue
            found_tables = {real_names[m.group(1).lower()] for m in name_pattern.finditer(body)}
            if not found_tables:
                continue
            for kw in keywords:
                index.setdefault(kw, [])
                for t in found_tables:
                    if t not in index[kw]:
                        index[kw].append(t)
        print(f"{doc_path.name}: {len(sections)} heading section(s) scanned")

    return index


if __name__ == "__main__":
    idx = build_index()
    OUTPUT_PATH.write_text(json.dumps(idx, indent=2, sort_keys=True), encoding="utf-8")
    total_tables = len({t for tbls in idx.values() for t in tbls})
    print(f"\nWrote {len(idx)} keyword(s) -> {total_tables} distinct table(s) to {OUTPUT_PATH}")
