#!/usr/bin/env python3
"""Fail-fast consistency checks for Chitragupta's knowledge routing layer.

This validator intentionally checks things that otherwise fail silently at runtime:
- a manifest route points at a missing Knowledge document;
- an identifier maps to a route that no longer exists;
- a route names a skill that is not deployable;
- manifest/task-router route taxonomies drift apart;
- the live L2 workflow skill regresses to retired board/bridge instructions.

It does not judge the semantic correctness of domain documentation. That belongs to
retrieval evaluation and live verification, not a filesystem consistency check.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "Knowledge"
MANIFEST = KNOWLEDGE / "manifest.json"
TASK_ROUTER = KNOWLEDGE / "task-router.md"
DEPLOY_SKILLS = ROOT / "deploy" / "skills" / "xstudio"
L2_SKILL = DEPLOY_SKILLS / "xstudio-l2-ticket-workflow" / "SKILL.md"


def _targets(value) -> list[str]:
    if isinstance(value, list):
        return [str(v) for v in value if v]
    if isinstance(value, str):
        return [part.strip() for part in value.split(" or ") if part.strip()]
    return []


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

    # Every declared skill and every route skill must actually be deployable.
    for skill in sorted(skill_set):
        skill_path = DEPLOY_SKILLS / skill / "SKILL.md"
        if not skill_path.exists():
            errors.append(f"manifest skill has no deployable SKILL.md: {skill}")

    for route in route_defs:
        route_name = route.get("route") or "<unnamed>"
        skill = route.get("skill")
        if skill and skill not in skill_set:
            errors.append(f"route {route_name!r} references undeclared skill {skill!r}")

    # Every knowledge file referenced by the machine router must exist. Anchors are
    # intentionally stripped because the filesystem validator cannot verify markdown
    # heading semantics without turning into another markdown parser.
    referenced = list(manifest.get("always_load") or [])
    for route in route_defs:
        referenced.extend(route.get("load") or [])
    for rel in sorted(set(referenced)):
        base = str(rel).split("#", 1)[0]
        if not (KNOWLEDGE / base).exists():
            errors.append(f"manifest references missing Knowledge file: {rel}")

    # Identifier mappings must point only at canonical routes.
    for identifier, configured in (manifest.get("identifier_routing") or {}).items():
        targets = _targets(configured)
        if not targets:
            errors.append(f"identifier_routing[{identifier!r}] has no usable route target")
            continue
        for target in targets:
            if target not in route_set:
                errors.append(f"identifier {identifier!r} points at unknown route {target!r}")

    # The human router may contain richer prose, but it must at least expose the same
    # canonical route names. This catches the common silent failure where one side is
    # renamed/added and the other side is forgotten.
    if TASK_ROUTER.exists():
        router_text = TASK_ROUTER.read_text(encoding="utf-8")
        for route in sorted(route_set):
            if not re.search(rf"`{re.escape(route)}`", router_text):
                errors.append(f"task-router.md does not mention manifest route `{route}`")
    else:
        errors.append("Knowledge/task-router.md is missing")

    # Prevent the exact stale-workflow regression fixed on 2026-09-05.
    if L2_SKILL.exists():
        skill_text = L2_SKILL.read_text(encoding="utf-8")
        forbidden = {
            "separate `l2-review` board": "retired separate review-board architecture",
            "kanban_forward_bridge.py` watches": "retired forward bridge",
            "l2-gemma-verifier": "retired model-based reviewer profile",
            "l2-qwen-verifier": "retired model-based reviewer profile",
        }
        for needle, why in forbidden.items():
            if needle in skill_text:
                errors.append(f"workflow skill contains {why}: {needle}")
    else:
        errors.append("deployable xstudio-l2-ticket-workflow skill is missing")

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
