#!/usr/bin/env python3
"""Govern repeated-human-action candidates into typed XBatch capabilities.

This is an operator/control-plane workflow, never a model execution surface.
Candidates discovered from reviewed NEEDS_HUMAN_ACTION outcomes move through:

    needs_executor_design
      -> researching_executor
      -> contract_drafted
      -> shadow_ready
      -> registry_entry

A registry promotion never raises deploy/xstudio_action_capabilities.json's
`global_mode`. The promoted capability is written at mode=shadow, so with the
current global_mode=observe it remains inactive even after its contract is
accepted. Enabling shadow/supervised/autonomous operation is a separate policy
change backed by replay/live evidence.
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

STATES = (
    "needs_executor_design",
    "researching_executor",
    "contract_drafted",
    "shadow_ready",
    "registry_entry",
    "rejected",
)
TRANSITIONS = {
    "needs_executor_design": {"researching_executor", "rejected"},
    "researching_executor": {"contract_drafted", "rejected"},
    "contract_drafted": {"researching_executor", "shadow_ready", "rejected"},
    "shadow_ready": {"contract_drafted", "registry_entry", "rejected"},
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


def _history(candidate: dict[str, Any]) -> list[dict[str, Any]]:
    value = candidate.setdefault("governance_history", [])
    if not isinstance(value, list):
        value = []
        candidate["governance_history"] = value
    return value


def _record(candidate: dict[str, Any], *, event: str, reviewed_by: str, evidence: str,
            from_status: str | None = None, to_status: str | None = None) -> None:
    _history(candidate).append({
        "event": event,
        "at": _now(),
        "reviewed_by": reviewed_by,
        "evidence": evidence,
        "from_status": from_status,
        "to_status": to_status,
    })
    candidate["updated_at"] = _now()


def _require_review(reviewed_by: str, evidence: str) -> None:
    if not reviewed_by.strip():
        raise ValueError("reviewed_by is required")
    if not evidence.strip():
        raise ValueError("evidence is required")


def _transition(candidate: dict[str, Any], target: str, *, reviewed_by: str, evidence: str) -> None:
    _require_review(reviewed_by, evidence)
    if target not in STATES:
        raise ValueError(f"unknown target status: {target}")
    current = str(candidate.get("status") or "needs_executor_design")
    if target == current:
        return
    if target not in TRANSITIONS.get(current, set()):
        raise ValueError(f"invalid capability-candidate transition: {current} -> {target}")
    candidate["status"] = target
    _record(candidate, event="status_transition", reviewed_by=reviewed_by, evidence=evidence,
            from_status=current, to_status=target)


def _read_contract(path: Path) -> dict[str, Any]:
    contract = _load_json(path)
    if str(contract.get("mode") or "") not in {"observe", "recommend", "shadow"}:
        raise ValueError("candidate design may target only observe/recommend/shadow; supervised/autonomous promotion is separate")
    # Candidate promotion itself always lands at shadow. This prevents a contract
    # file from quietly asking the curator for a stronger execution mode.
    contract = dict(contract)
    contract["mode"] = "shadow"
    return contract


def _validate_contract_against_registry(contract: dict[str, Any], registry: dict[str, Any]) -> list[str]:
    probe = dict(registry)
    caps = [dict(x) for x in registry.get("capabilities", []) if isinstance(x, dict)]
    cid = str(contract.get("id") or "")
    caps = [x for x in caps if str(x.get("id") or "") != cid]
    caps.append(contract)
    probe["capabilities"] = caps
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "registry.json"
        path.write_text(json.dumps(probe), encoding="utf-8")
        return validate_registry(path)


def _shadow_readiness_errors(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    execution = contract.get("execution") if isinstance(contract.get("execution"), dict) else {}
    if execution.get("type") in {None, "", "none"}:
        errors.append("execution.type must identify the verified future executor path before shadow_ready")
    if not str(execution.get("target") or "").strip():
        errors.append("execution.target is required before shadow_ready")
    for field in ("preconditions", "verification", "required_evidence"):
        if not contract.get(field):
            errors.append(f"{field} must be non-empty before shadow_ready")
    if not isinstance(contract.get("idempotency"), dict) or not contract.get("idempotency"):
        errors.append("idempotency must be non-empty before shadow_ready")
    if not isinstance(contract.get("approval_policy"), dict) or not contract.get("approval_policy"):
        errors.append("approval_policy must be non-empty before shadow_ready")
    rollback = contract.get("rollback")
    if not isinstance(rollback, dict) or not rollback:
        errors.append("rollback/compensation contract must be explicit before shadow_ready")
    return errors


def list_candidates(vault: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    root = vault / "actions" / "candidates"
    for path in sorted(root.glob("*.json")) if root.exists() else []:
        try:
            data = _load_json(path)
            out.append({
                "candidate": path.name,
                "status": data.get("status"),
                "distinct_ticket_count": data.get("distinct_ticket_count"),
                "representative_human_action": data.get("representative_human_action"),
                "draft_capability_id": (data.get("draft_contract") or {}).get("id") if isinstance(data.get("draft_contract"), dict) else None,
            })
        except Exception:
            out.append({"candidate": path.name, "status": "invalid"})
    return out


def start_research(candidate_path: Path, *, reviewed_by: str, evidence: str) -> dict[str, Any]:
    candidate = _load_json(candidate_path)
    _transition(candidate, "researching_executor", reviewed_by=reviewed_by, evidence=evidence)
    _save_json(candidate_path, candidate)
    return candidate


def apply_contract(candidate_path: Path, contract_path: Path, registry_path: Path, *,
                   reviewed_by: str, evidence: str) -> dict[str, Any]:
    _require_review(reviewed_by, evidence)
    candidate = _load_json(candidate_path)
    if str(candidate.get("status") or "needs_executor_design") not in {"researching_executor", "contract_drafted"}:
        raise ValueError("contract can be drafted only while researching_executor or contract_drafted")
    contract = _read_contract(contract_path)
    registry = _load_json(registry_path)
    errors = _validate_contract_against_registry(contract, registry)
    if errors:
        raise ValueError("capability contract failed registry validation: " + "; ".join(errors))
    candidate["draft_contract"] = contract
    candidate["design_requirements"] = {
        "capability_id": contract.get("id"),
        "risk": contract.get("risk"),
        "parameter_schema": contract.get("parameter_schema"),
        "preconditions": contract.get("preconditions"),
        "execution": contract.get("execution"),
        "idempotency": contract.get("idempotency"),
        "verification": contract.get("verification"),
        "rollback": contract.get("rollback"),
        "required_evidence": contract.get("required_evidence"),
        "approval_policy": contract.get("approval_policy"),
    }
    current = str(candidate.get("status") or "needs_executor_design")
    if current != "contract_drafted":
        _transition(candidate, "contract_drafted", reviewed_by=reviewed_by, evidence=evidence)
    else:
        _record(candidate, event="contract_revised", reviewed_by=reviewed_by, evidence=evidence)
    _save_json(candidate_path, candidate)
    return candidate


def mark_shadow_ready(candidate_path: Path, registry_path: Path, *, reviewed_by: str, evidence: str) -> dict[str, Any]:
    _require_review(reviewed_by, evidence)
    candidate = _load_json(candidate_path)
    if str(candidate.get("status") or "") != "contract_drafted":
        raise ValueError("candidate must be contract_drafted before shadow_ready")
    contract = candidate.get("draft_contract")
    if not isinstance(contract, dict):
        raise ValueError("draft_contract is missing")
    registry = _load_json(registry_path)
    errors = _validate_contract_against_registry(contract, registry) + _shadow_readiness_errors(contract)
    if errors:
        raise ValueError("candidate is not shadow-ready: " + "; ".join(errors))
    _transition(candidate, "shadow_ready", reviewed_by=reviewed_by, evidence=evidence)
    candidate["shadow_readiness"] = {
        "reviewed_at": _now(),
        "reviewed_by": reviewed_by,
        "evidence": evidence,
        "note": "Contract is eligible for registry inclusion only. No execution permission is granted.",
    }
    _save_json(candidate_path, candidate)
    return candidate


def promote_to_registry(candidate_path: Path, registry_path: Path, *, reviewed_by: str, evidence: str) -> dict[str, Any]:
    _require_review(reviewed_by, evidence)
    candidate = _load_json(candidate_path)
    if str(candidate.get("status") or "") != "shadow_ready":
        raise ValueError("candidate must be shadow_ready before registry promotion")
    contract = candidate.get("draft_contract")
    if not isinstance(contract, dict):
        raise ValueError("draft_contract is missing")
    contract = dict(contract)
    contract["mode"] = "shadow"
    registry = _load_json(registry_path)
    errors = _validate_contract_against_registry(contract, registry) + _shadow_readiness_errors(contract)
    if errors:
        raise ValueError("registry promotion refused: " + "; ".join(errors))
    caps = [dict(x) for x in registry.get("capabilities", []) if isinstance(x, dict)]
    cid = str(contract.get("id") or "")
    existing = next((x for x in caps if str(x.get("id") or "") == cid), None)
    if existing and existing != contract:
        raise ValueError(f"registry already contains a different capability with id={cid}")
    if not existing:
        caps.append(contract)
    # Critical invariant: this workflow never raises global mode.
    prior_global = registry.get("global_mode")
    registry["capabilities"] = caps
    registry["global_mode"] = prior_global
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "registry.json"
        probe.write_text(json.dumps(registry), encoding="utf-8")
        final_errors = validate_registry(probe)
    if final_errors:
        raise ValueError("final registry validation failed: " + "; ".join(final_errors))
    _save_json(registry_path, registry)
    digest = hashlib.sha256(registry_path.read_bytes()).hexdigest()
    _transition(candidate, "registry_entry", reviewed_by=reviewed_by, evidence=evidence)
    candidate["registry_entry"] = {
        "capability_id": cid,
        "mode": "shadow",
        "registry": str(registry_path),
        "registry_sha256": digest,
        "global_mode_at_promotion": prior_global,
        "promoted_at": _now(),
        "reviewed_by": reviewed_by,
        "evidence": evidence,
        "execution_authorized": False,
    }
    _save_json(candidate_path, candidate)
    return candidate


def reject(candidate_path: Path, *, reviewed_by: str, evidence: str) -> dict[str, Any]:
    candidate = _load_json(candidate_path)
    _transition(candidate, "rejected", reviewed_by=reviewed_by, evidence=evidence)
    _save_json(candidate_path, candidate)
    return candidate


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("list")

    def reviewed_parser(name: str) -> argparse.ArgumentParser:
        p = sub.add_parser(name)
        p.add_argument("candidate")
        p.add_argument("--reviewed-by", required=True)
        p.add_argument("--evidence", required=True)
        return p

    reviewed_parser("research")
    d = reviewed_parser("draft-contract")
    d.add_argument("--contract", required=True)
    reviewed_parser("shadow-ready")
    reviewed_parser("promote")
    reviewed_parser("reject")

    ns = ap.parse_args(argv)
    vault = _vault(ns.vault)
    registry = Path(ns.registry).expanduser()
    if ns.command == "list":
        print(json.dumps({"candidates": list_candidates(vault)}, indent=2, ensure_ascii=False)); return 0
    candidate_path = _candidate_path(vault, ns.candidate)
    kwargs = {"reviewed_by": ns.reviewed_by, "evidence": ns.evidence}
    if ns.command == "research": result = start_research(candidate_path, **kwargs)
    elif ns.command == "draft-contract": result = apply_contract(candidate_path, Path(ns.contract).expanduser(), registry, **kwargs)
    elif ns.command == "shadow-ready": result = mark_shadow_ready(candidate_path, registry, **kwargs)
    elif ns.command == "promote": result = promote_to_registry(candidate_path, registry, **kwargs)
    else: result = reject(candidate_path, **kwargs)
    print(json.dumps({"ok": True, "candidate": candidate_path.name, "status": result.get("status")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
