#!/usr/bin/env python3
"""Govern repeated human-action candidates into reviewed shadow capabilities.

A candidate contains observed evidence plus, at most, one operator-reviewed
`draft_contract`. There is no persisted "research workflow". A valid draft can
be marked shadow-ready and then added to the registry at mode=shadow.

This tool never raises registry global_mode and never executes an XBatch action.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from validate_action_capabilities import validate as validate_registry

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
DEFAULT_REGISTRY = ROOT / "deploy" / "xstudio_action_capabilities.json"

DEFAULT_STATUS = "needs_executor_design"
STATES = {DEFAULT_STATUS, "shadow_ready", "registry_entry", "rejected"}
TRANSITIONS = {
    DEFAULT_STATUS: {"shadow_ready", "rejected"},
    "shadow_ready": {"registry_entry", "rejected"},
    "registry_entry": set(),
    "rejected": set(),
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _vault(raw: str | None = None) -> Path:
    if raw:
        return Path(raw).expanduser()
    env = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(env).expanduser() if env else DEFAULT_VAULT


def _candidate_path(vault: Path, value: str) -> Path:
    raw = Path(value)
    path = raw if raw.is_absolute() else vault / "actions" / "candidates" / value
    if path.suffix != ".json":
        path = path.with_suffix(".json")
    path = path.resolve()
    root = (vault / "actions" / "candidates").resolve()
    if root not in path.parents:
        raise ValueError("candidate must be under vault/actions/candidates")
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def _load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _save_json(path: Path, data: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def _require_review(reviewed_by: str, evidence: str) -> None:
    if not reviewed_by.strip():
        raise ValueError("reviewed_by is required")
    if not evidence.strip():
        raise ValueError("evidence is required")


def _status(candidate: dict[str, Any]) -> str:
    status = str(candidate.get("status") or DEFAULT_STATUS)
    if status not in STATES:
        raise ValueError(f"unknown capability-candidate status: {status}")
    return status


def _record(candidate: dict[str, Any], *, event: str, reviewed_by: str,
            evidence: str, status: str | None = None) -> None:
    history = candidate.setdefault("governance_history", [])
    if not isinstance(history, list):
        raise ValueError("governance_history must be an array")
    history.append({
        "event": event,
        "at": _now(),
        "reviewed_by": reviewed_by,
        "evidence": evidence,
        "status": status,
    })
    candidate["updated_at"] = _now()


def _transition(candidate: dict[str, Any], target: str, *, reviewed_by: str,
                evidence: str) -> None:
    _require_review(reviewed_by, evidence)
    current = _status(candidate)
    if target not in TRANSITIONS[current]:
        raise ValueError(f"invalid capability-candidate transition: {current} -> {target}")
    candidate["status"] = target
    _record(
        candidate,
        event="status_transition",
        reviewed_by=reviewed_by,
        evidence=evidence,
        status=target,
    )


def _read_contract(path: Path) -> dict[str, Any]:
    contract = _load_json(path)
    if str(contract.get("mode") or "") not in {"observe", "recommend", "shadow"}:
        raise ValueError("candidate contract may target only observe/recommend/shadow")
    contract = dict(contract)
    contract["mode"] = "shadow"
    return contract


def _capabilities_without(registry: dict[str, Any], capability_id: str) -> list[dict[str, Any]]:
    return [
        dict(item)
        for item in registry.get("capabilities", [])
        if isinstance(item, dict) and str(item.get("id") or "") != capability_id
    ]


def _registry_probe(registry: dict[str, Any], contract: dict[str, Any]) -> dict[str, Any]:
    probe = dict(registry)
    capability_id = str(contract.get("id") or "")
    probe["capabilities"] = _capabilities_without(registry, capability_id) + [contract]
    return probe


def _validate_contract(contract: dict[str, Any], registry: dict[str, Any]) -> list[str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "registry.json"
        path.write_text(json.dumps(_registry_probe(registry, contract)), encoding="utf-8")
        return validate_registry(path)


def _required_nonempty(contract: dict[str, Any], fields: tuple[str, ...]) -> list[str]:
    return [f"{field} must be non-empty" for field in fields if not contract.get(field)]


def _required_objects(contract: dict[str, Any], fields: tuple[str, ...]) -> list[str]:
    errors: list[str] = []
    for field in fields:
        value = contract.get(field)
        if not isinstance(value, dict) or not value:
            errors.append(f"{field} must be a non-empty object")
    return errors


def _shadow_readiness_errors(contract: dict[str, Any]) -> list[str]:
    execution = contract.get("execution") if isinstance(contract.get("execution"), dict) else {}
    errors = _required_nonempty(contract, ("preconditions", "verification", "required_evidence"))
    errors += _required_objects(contract, ("idempotency", "approval_policy", "rollback"))
    if execution.get("type") in {None, "", "none"}:
        errors.append("execution.type must identify the supported future executor")
    if not str(execution.get("target") or "").strip():
        errors.append("execution.target is required")
    return errors


def _candidate_row(path: Path) -> dict[str, Any] | None:
    data = _load_json(path)
    if data.get("kind") != "xstudio_action_capability_candidate":
        return None
    draft = data.get("draft_contract") if isinstance(data.get("draft_contract"), dict) else {}
    return {
        "candidate": path.name,
        "candidate_id": data.get("candidate_id"),
        "status": _status(data),
        "distinct_ticket_count": int(data.get("distinct_ticket_count") or 0),
        "observation_count": int(data.get("observation_count") or 0),
        "risk": draft.get("risk") or "unclassified",
        "draft_capability_id": draft.get("id"),
        "representative_human_action": data.get("representative_human_action"),
        "first_seen_at": data.get("first_seen_at"),
    }


def _rank_key(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        -int(row["distinct_ticket_count"]),
        -int(row["observation_count"]),
        str(row.get("first_seen_at") or ""),
        str(row.get("candidate_id") or ""),
    )


def list_candidates(vault: Path) -> list[dict[str, Any]]:
    valid: list[dict[str, Any]] = []
    invalid: list[dict[str, Any]] = []
    root = vault / "actions" / "candidates"
    for path in sorted(root.glob("*.json")) if root.exists() else []:
        try:
            row = _candidate_row(path)
            if row:
                valid.append(row)
        except Exception as exc:
            invalid.append({"candidate": path.name, "status": "invalid", "error": str(exc)[:500]})
    valid.sort(key=_rank_key)
    return valid + invalid


def apply_contract(candidate_path: Path, contract_path: Path, registry_path: Path, *,
                   reviewed_by: str, evidence: str) -> dict[str, Any]:
    _require_review(reviewed_by, evidence)
    candidate = _load_json(candidate_path)
    if _status(candidate) != DEFAULT_STATUS:
        raise ValueError("contract can be drafted only while candidate needs executor design")
    contract = _read_contract(contract_path)
    registry = _load_json(registry_path)
    errors = _validate_contract(contract, registry)
    if errors:
        raise ValueError("capability contract failed registry validation: " + "; ".join(errors))
    candidate["draft_contract"] = contract
    _record(candidate, event="contract_drafted", reviewed_by=reviewed_by, evidence=evidence)
    _save_json(candidate_path, candidate)
    return candidate


def mark_shadow_ready(candidate_path: Path, registry_path: Path, *,
                      reviewed_by: str, evidence: str) -> dict[str, Any]:
    candidate = _load_json(candidate_path)
    if _status(candidate) != DEFAULT_STATUS:
        raise ValueError("candidate must need executor design before shadow_ready")
    contract = candidate.get("draft_contract")
    if not isinstance(contract, dict):
        raise ValueError("draft_contract is missing")
    registry = _load_json(registry_path)
    errors = _validate_contract(contract, registry) + _shadow_readiness_errors(contract)
    if errors:
        raise ValueError("candidate is not shadow-ready: " + "; ".join(errors))
    _transition(candidate, "shadow_ready", reviewed_by=reviewed_by, evidence=evidence)
    _save_json(candidate_path, candidate)
    return candidate


def _existing_capability(registry: dict[str, Any], capability_id: str) -> dict[str, Any] | None:
    for item in registry.get("capabilities", []):
        if isinstance(item, dict) and str(item.get("id") or "") == capability_id:
            return item
    return None


def _promoted_registry(registry: dict[str, Any], contract: dict[str, Any]) -> dict[str, Any]:
    capability_id = str(contract.get("id") or "")
    existing = _existing_capability(registry, capability_id)
    if existing and existing != contract:
        raise ValueError(f"registry already contains a different capability with id={capability_id}")
    if existing:
        return registry
    updated = dict(registry)
    updated["capabilities"] = [
        dict(item) for item in registry.get("capabilities", []) if isinstance(item, dict)
    ] + [contract]
    return updated


def promote_to_registry(candidate_path: Path, registry_path: Path, *,
                        reviewed_by: str, evidence: str) -> dict[str, Any]:
    candidate = _load_json(candidate_path)
    if _status(candidate) != "shadow_ready":
        raise ValueError("candidate must be shadow_ready before registry promotion")
    contract = candidate.get("draft_contract")
    if not isinstance(contract, dict):
        raise ValueError("draft_contract is missing")

    registry = _load_json(registry_path)
    errors = _validate_contract(contract, registry) + _shadow_readiness_errors(contract)
    if errors:
        raise ValueError("registry promotion refused: " + "; ".join(errors))

    updated_registry = _promoted_registry(registry, contract)
    _save_json(registry_path, updated_registry)

    _transition(candidate, "registry_entry", reviewed_by=reviewed_by, evidence=evidence)
    candidate["registered_capability_id"] = str(contract.get("id") or "")
    candidate["registry_sha256"] = hashlib.sha256(registry_path.read_bytes()).hexdigest()
    _save_json(candidate_path, candidate)
    return candidate


def reject(candidate_path: Path, *, reviewed_by: str, evidence: str) -> dict[str, Any]:
    candidate = _load_json(candidate_path)
    _transition(candidate, "rejected", reviewed_by=reviewed_by, evidence=evidence)
    _save_json(candidate_path, candidate)
    return candidate


def _reviewed_parser(sub: argparse._SubParsersAction, name: str) -> argparse.ArgumentParser:
    parser = sub.add_parser(name)
    parser.add_argument("candidate")
    parser.add_argument("--reviewed-by", required=True)
    parser.add_argument("--evidence", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    draft = _reviewed_parser(sub, "draft-contract")
    draft.add_argument("--contract", required=True)
    _reviewed_parser(sub, "shadow-ready")
    _reviewed_parser(sub, "promote")
    _reviewed_parser(sub, "reject")
    ns = ap.parse_args(argv)

    vault = _vault(ns.vault)
    registry = Path(ns.registry).expanduser()
    if ns.command == "list":
        print(json.dumps({"candidates": list_candidates(vault)}, indent=2, ensure_ascii=False))
        return 0

    candidate_path = _candidate_path(vault, ns.candidate)
    kwargs = {"reviewed_by": ns.reviewed_by, "evidence": ns.evidence}
    handlers = {
        "draft-contract": lambda: apply_contract(
            candidate_path, Path(ns.contract).expanduser(), registry, **kwargs
        ),
        "shadow-ready": lambda: mark_shadow_ready(candidate_path, registry, **kwargs),
        "promote": lambda: promote_to_registry(candidate_path, registry, **kwargs),
        "reject": lambda: reject(candidate_path, **kwargs),
    }
    result = handlers[ns.command]()
    print(json.dumps({
        "ok": True,
        "candidate": candidate_path.name,
        "status": result.get("status"),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
