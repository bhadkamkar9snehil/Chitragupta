#!/usr/bin/env python3
"""Fail-fast consistency checks for Chitragupta's current knowledge/runtime contract.

Checks structural drift that otherwise fails silently:
- routed Knowledge documents or deployable skills disappear;
- manifest/task-router route taxonomies diverge;
- current workflow skills regress to retired review-board/parent-gating instructions;
- runtime docs regress to model-owned arbitrary SQL mutation/publication;
- retired duplicate lifecycle or model-owned SQL-transport scripts reappear.

Semantic domain correctness still requires retrieval evaluation and live verification.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "Knowledge"
MANIFEST = KNOWLEDGE / "manifest.json"
TASK_ROUTER = KNOWLEDGE / "task-router.md"
RUNTIME_DESIGN = KNOWLEDGE / "hermes-runtime-database-design.md"
SP_CATALOG = KNOWLEDGE / "hermes-sp-catalog.md"
DEPLOY_SKILLS = ROOT / "deploy" / "skills" / "xstudio"
L2_SKILL = DEPLOY_SKILLS / "xstudio-l2-ticket-workflow" / "SKILL.md"
REVIEW_SKILL = DEPLOY_SKILLS / "xstudio-l2-draft-verifier" / "SKILL.md"

RETIRED_RUNTIME_PATHS = (
    ROOT / "Model_Bench" / "dispatch_l2_review.py",
    ROOT / "Model_Bench" / "kanban_forward_bridge.py",
    ROOT / "Model_Bench" / "nudge_unpublished_runs.py",
    ROOT / "Model_Bench" / "_tmp_restart_gateways.sh",
    ROOT / "Model_Bench" / "_tmp_switch_to_qwen.sh",
    ROOT / "Model_Bench" / "_tmp_test_invoke.sh",
    ROOT / "deploy" / "profiles" / "l2-gemma",
    ROOT / "investigate_sap_posting.py",
    ROOT / "test_conn.py",
)


def _targets(value) -> list[str]:
    if isinstance(value, list):
        return [str(v) for v in value if v]
    if isinstance(value, str):
        return [part.strip() for part in value.split(" or ") if part.strip()]
    return []


def _check_forbidden(path: Path, label: str, forbidden: dict[str, str], errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"missing {label}: {path}")
        return
    text = path.read_text(encoding="utf-8")
    for needle, why in forbidden.items():
        if needle in text:
            errors.append(f"{label} contains {why}: {needle}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not MANIFEST.exists():
        print(f"FAIL: missing {MANIFEST}")
        return 1

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: manifest is not valid JSON: {exc}")
        return 1

    route_defs = manifest.get("routes") or []
    route_names = [r.get("route") for r in route_defs if r.get("route")]
    route_set = set(route_names)
    if len(route_names) != len(route_set):
        errors.append("duplicate route names in Knowledge/manifest.json")
    if "discover" not in route_set:
        errors.append("required fallback route 'discover' is missing")

    skill_defs = manifest.get("skills") or []
    skill_names = [s.get("name") for s in skill_defs if s.get("name")]
    skill_set = set(skill_names)
    if len(skill_names) != len(skill_set):
        errors.append("duplicate skill names in Knowledge/manifest.json")

    for skill in sorted(skill_set):
        skill_path = DEPLOY_SKILLS / skill / "SKILL.md"
        if not skill_path.exists():
            errors.append(f"manifest skill has no deployable SKILL.md: {skill}")

    for route in route_defs:
        route_name = route.get("route") or "<unnamed>"
        skill = route.get("skill")
        if skill and skill not in skill_set:
            errors.append(f"route {route_name!r} references undeclared skill {skill!r}")

    referenced = list(manifest.get("always_load") or [])
    for route in route_defs:
        referenced.extend(route.get("load") or [])
    for rel in sorted(set(referenced)):
        base = str(rel).split("#", 1)[0]
        if not (KNOWLEDGE / base).exists():
            errors.append(f"manifest references missing Knowledge file: {rel}")

    for identifier, configured in (manifest.get("identifier_routing") or {}).items():
        targets = _targets(configured)
        if not targets:
            errors.append(f"identifier_routing[{identifier!r}] has no usable route target")
            continue
        for target in targets:
            if target not in route_set:
                errors.append(f"identifier {identifier!r} points at unknown route {target!r}")

    if TASK_ROUTER.exists():
        router_text = TASK_ROUTER.read_text(encoding="utf-8")
        for route in sorted(route_set):
            if not re.search(rf"`{re.escape(route)}`", router_text):
                errors.append(f"task-router.md does not mention manifest route `{route}`")
    else:
        errors.append("Knowledge/task-router.md is missing")

    skill_forbidden = {
        "separate `l2-review` board": "retired separate review-board architecture",
        "kanban_forward_bridge.py": "retired cross-board forward bridge",
        "parent-gated reviewer child": "retired pre-created/parent-gated reviewer topology",
        "parent-gated reviewer flow": "retired pre-created/parent-gated reviewer topology",
        "fresh parent-gated reviewer": "retired pre-created/parent-gated reviewer topology",
        "l2-gemma-verifier": "retired model-based reviewer profile",
        "l2-qwen-verifier": "retired model-based reviewer profile",
    }
    _check_forbidden(L2_SKILL, "investigator workflow skill", skill_forbidden, errors)
    _check_forbidden(REVIEW_SKILL, "reviewer skill", skill_forbidden, errors)

    runtime_forbidden = {
        "Hermes is explicitly allowed to write SQL": "retired model-owned arbitrary SQL authority",
        "worker can execute that SP through": "retired worker mutation path",
        "creates + links a solution article": "retired automatic per-resolution Solution promotion",
        "poll/investigate/publish": "retired worker-owned publication choreography",
    }
    _check_forbidden(RUNTIME_DESIGN, "runtime database design", runtime_forbidden, errors)
    _check_forbidden(SP_CATALOG, "stored procedure catalog", runtime_forbidden, errors)

    for path in RETIRED_RUNTIME_PATHS:
        if path.exists():
            errors.append(f"retired lifecycle/transport artifact has reappeared: {path.relative_to(ROOT)}")

    verified = manifest.get("verified")
    if not verified:
        warnings.append("manifest has no verified date")

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"FAIL: {error}")

    if errors:
        print(f"knowledge validation failed: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(
        "knowledge validation ok: "
        f"{len(route_set)} routes, {len(skill_set)} skills, "
        f"{len(set(referenced))} routed document reference(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
