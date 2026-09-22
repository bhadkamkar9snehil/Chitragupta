#!/usr/bin/env python3
"""Read-only readiness and golden-case validation for the L2 GBrain corpus."""
from __future__ import annotations

import json
from pathlib import Path

try:
    from . import kb_retrieval as kb
    from .xbatch_world import load_world
except ImportError:
    import kb_retrieval as kb
    from xbatch_world import load_world

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "Knowledge" / "eval" / "gbrain_retrieval_cases.jsonl"


def validate_world_artifacts() -> dict:
    try:
        world = load_world()
        atlas = world["atlas"]
        relationships = atlas.get("relationships") or []
        source_count = sum(int(edge["provenance"]["source_row_count"]) for edge in relationships)
        routes = {route["route"] for route in world["manifest"].get("routes", [])}
        recipe_routes = {recipe["route"] for recipe in world["recipes"]}
        if atlas.get("schema_version") != 2:
            raise ValueError("semantic atlas schema_version must be 2")
        if routes != recipe_routes or set(atlas.get("domains", {})) != routes:
            raise ValueError("manifest routes, domains and recipes do not agree")
        return {
            "status": "READY", "source_relationships": source_count,
            "semantic_relationships": len(relationships), "recipes": len(world["recipes"]),
        }
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        return {"status": "INVALID", "reason": f"{type(exc).__name__}: {exc}"}


def evaluate_case(case: dict, result: dict) -> list[str]:
    slugs = [str(hit.get("slug") or "") for hit in result.get("hits", [])]
    errors = []
    if case.get("expect_abstention") and not result.get("abstained"):
        errors.append("expected abstention")
    expected = case.get("expect_any_prefix") or []
    if expected and not any(any(slug.startswith(prefix) for prefix in expected) for slug in slugs):
        errors.append("no expected knowledge prefix retrieved")
    for prefix in case.get("forbid_prefix") or []:
        if any(slug.startswith(prefix) for slug in slugs):
            errors.append(f"forbidden prefix retrieved: {prefix}")
    return errors


def main() -> int:
    world_status = validate_world_artifacts()
    if world_status.get("status") != "READY":
        print(json.dumps({"status": "FAIL", "world": world_status, "cases": 0, "passed": 0, "failed": 1}, indent=2))
        return 1
    manifest = kb.load_manifest()
    status = kb.get_gbrain_status(manifest["gbrain"])
    if status.get("status") != "READY":
        print(json.dumps({**status, "world": world_status, "cases": 0, "passed": 0, "failed": 1,
                          "failures": [status.get("reason") or "GBrain is not ready"]}, indent=2))
        return 1
    cases = [json.loads(line) for line in CASES.read_text(encoding="utf-8").splitlines() if line.strip()]
    failures = []
    for case in cases:
        result = kb.retrieve_gbrain(case["query"], manifest["gbrain"])
        errors = evaluate_case(case, result)
        if errors:
            failures.append({"id": case["id"], "errors": errors,
                             "slugs": [h.get("slug") for h in result.get("hits", [])]})
    report = {"status": "PASS" if not failures else "FAIL", "source_id": status["source_id"], "world": world_status,
              "embedding_coverage_pct": status["embedding_coverage_pct"], "cases": len(cases),
              "passed": len(cases) - len(failures), "failed": len(failures), "failures": failures}
    print(json.dumps(report, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
