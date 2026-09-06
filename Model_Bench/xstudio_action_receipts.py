#!/usr/bin/env python3
"""Append-only receipt ledger for future deterministic XBatch action execution.

This module does not execute actions and does not grant permission. It defines the
audit/result semantics a future executor must use from day one:

    planned -> approved -> executed -> verified
                       \-> failed -> compensated

Failures may also occur before approval/execution and are recorded explicitly.
Prior history events are never rewritten; each transition appends one event and
updates only the current-state summary.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
STATES = ("planned", "approved", "executed", "verified", "failed", "compensated")
TRANSITIONS = {
    "planned": {"approved", "failed"},
    "approved": {"executed", "failed"},
    "executed": {"verified", "failed"},
    "verified": set(),
    "failed": {"compensated"},
    "compensated": set(),
}
HEX32 = re.compile(r"^[0-9a-f]{32}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _vault(raw: str | None = None) -> Path:
    if raw:
        return Path(raw).expanduser()
    env = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(env).expanduser() if env else DEFAULT_VAULT


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)


def _sha(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _receipt_dir(vault: Path) -> Path:
    path = vault / "actions" / "receipts"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _receipt_path(vault: Path, receipt_id: str) -> Path:
    if not HEX32.fullmatch(receipt_id or ""):
        raise ValueError("receipt_id must be 32 lowercase hex characters")
    return _receipt_dir(vault) / f"{receipt_id}.json"


def _load(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("receipt must be a JSON object")
    return data


def _save(path: Path, data: dict[str, Any]) -> None:
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def _validate_plan(plan: dict[str, Any]) -> None:
    required = ("plan_id", "capability_id", "capability_sha256", "registry_sha256", "context")
    missing = [k for k in required if not plan.get(k)]
    if missing:
        raise ValueError("plan missing required receipt identity: " + ", ".join(missing))
    if not HEX32.fullmatch(str(plan.get("plan_id") or "")):
        raise ValueError("plan_id must be 32 lowercase hex characters")
    for field in ("capability_sha256", "registry_sha256"):
        if not HEX64.fullmatch(str(plan.get(field) or "")):
            raise ValueError(f"{field} must be 64 lowercase hex characters")
    context = plan.get("context")
    if not isinstance(context, dict) or not context.get("run_id") or not context.get("ticket_id"):
        raise ValueError("plan context must include run_id and ticket_id")


def _identity_from_receipt(receipt: dict[str, Any]) -> dict[str, Any]:
    return {
        "plan_id": receipt.get("plan_id"),
        "capability_id": receipt.get("capability_id"),
        "run_id": receipt.get("run_id"),
        "ticket_id": receipt.get("ticket_id"),
        "attempt_no": receipt.get("attempt_no"),
    }


def begin_receipt(plan: dict[str, Any], *, vault: Path | None = None, attempt_no: int = 1,
                  actor: str, evidence: str) -> dict[str, Any]:
    if not actor.strip():
        raise ValueError("actor is required")
    if not evidence.strip():
        raise ValueError("evidence is required")
    if attempt_no < 1:
        raise ValueError("attempt_no must be >= 1")
    _validate_plan(plan)
    vault = vault or _vault()
    identity = {
        "plan_id": str(plan["plan_id"]),
        "capability_id": str(plan["capability_id"]),
        "run_id": str(plan["context"]["run_id"]),
        "ticket_id": str(plan["context"]["ticket_id"]),
        "attempt_no": int(attempt_no),
    }
    receipt_id = _sha(identity)[:32]
    plan_digest = _sha(plan)
    path = _receipt_path(vault, receipt_id)
    if path.exists():
        existing = _load(path)
        errors = validate_receipt(existing)
        if errors:
            raise ValueError("existing receipt is invalid: " + "; ".join(errors))
        if existing.get("identity") != identity:
            raise ValueError("receipt_id collision with different identity")
        if existing.get("plan_sha256") != plan_digest:
            raise ValueError("existing receipt pins different plan content for the same action-attempt identity")
        if existing.get("capability_sha256") != str(plan["capability_sha256"]):
            raise ValueError("existing receipt pins a different capability contract")
        if existing.get("registry_sha256") != str(plan["registry_sha256"]):
            raise ValueError("existing receipt pins a different registry version")
        return existing
    now = _now()
    receipt = {
        "schema_version": 1,
        "kind": "xstudio_action_execution_receipt",
        "receipt_id": receipt_id,
        "identity": identity,
        "plan_id": identity["plan_id"],
        "capability_id": identity["capability_id"],
        "run_id": identity["run_id"],
        "ticket_id": identity["ticket_id"],
        "attempt_no": identity["attempt_no"],
        "plan_sha256": plan_digest,
        "capability_sha256": str(plan["capability_sha256"]),
        "registry_sha256": str(plan["registry_sha256"]),
        "risk": plan.get("risk"),
        "effective_mode_at_plan": plan.get("effective_mode"),
        "state": "planned",
        "created_at": now,
        "updated_at": now,
        "events": [{
            "sequence": 1,
            "state": "planned",
            "at": now,
            "actor": actor,
            "evidence": evidence,
            "details": {
                "execution_authorized": False,
                "note": "Receipt creation records intent only; capability/approval policy still governs execution.",
            },
        }],
    }
    errors = validate_receipt(receipt)
    if errors:
        raise ValueError("new receipt failed validation: " + "; ".join(errors))
    _save(path, receipt)
    return receipt


def transition_receipt(receipt_id: str, target: str, *, vault: Path | None = None,
                       actor: str, evidence: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
    if not actor.strip():
        raise ValueError("actor is required")
    if not evidence.strip():
        raise ValueError("evidence is required")
    if target not in STATES:
        raise ValueError(f"unknown receipt state: {target}")
    vault = vault or _vault()
    path = _receipt_path(vault, receipt_id)
    if not path.is_file():
        raise FileNotFoundError(path)
    receipt = _load(path)
    prior_errors = validate_receipt(receipt)
    if prior_errors:
        raise ValueError("refusing to transition invalid receipt: " + "; ".join(prior_errors))
    current = str(receipt.get("state") or "")
    if target == current:
        return receipt
    if target not in TRANSITIONS.get(current, set()):
        raise ValueError(f"invalid action receipt transition: {current} -> {target}")
    if details is not None and not isinstance(details, dict):
        raise ValueError("details must be an object")
    if target == "verified":
        if not isinstance(details, dict) or details.get("postconditions_verified") is not True:
            raise ValueError("verified transition requires details.postconditions_verified=true")
    if target == "compensated":
        if not isinstance(details, dict) or details.get("compensation_verified") is not True:
            raise ValueError("compensated transition requires details.compensation_verified=true")
    events = receipt.get("events")
    assert isinstance(events, list)  # validated above
    now = _now()
    events.append({
        "sequence": len(events) + 1,
        "from_state": current,
        "state": target,
        "at": now,
        "actor": actor,
        "evidence": evidence,
        "details": details or {},
    })
    receipt["state"] = target
    receipt["updated_at"] = now
    errors = validate_receipt(receipt)
    if errors:
        raise ValueError("receipt transition produced invalid history: " + "; ".join(errors))
    _save(path, receipt)
    return receipt


def validate_receipt(receipt: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if receipt.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if receipt.get("kind") != "xstudio_action_execution_receipt":
        errors.append("kind must be xstudio_action_execution_receipt")
    for field in (
        "receipt_id", "plan_id", "capability_id", "run_id", "ticket_id", "attempt_no",
        "plan_sha256", "capability_sha256", "registry_sha256", "state", "events",
    ):
        if receipt.get(field) in (None, "", []):
            errors.append(f"missing {field}")
    if not HEX32.fullmatch(str(receipt.get("receipt_id") or "")):
        errors.append("receipt_id must be 32 lowercase hex characters")
    for field in ("plan_sha256", "capability_sha256", "registry_sha256"):
        if not HEX64.fullmatch(str(receipt.get(field) or "")):
            errors.append(f"{field} must be 64 lowercase hex characters")
    if not isinstance(receipt.get("attempt_no"), int) or isinstance(receipt.get("attempt_no"), bool) or int(receipt.get("attempt_no") or 0) < 1:
        errors.append("attempt_no must be an integer >= 1")
    if receipt.get("state") not in STATES:
        errors.append(f"unknown current state: {receipt.get('state')!r}")

    identity = receipt.get("identity")
    if not isinstance(identity, dict):
        errors.append("identity must be an object")
    else:
        expected_identity = _identity_from_receipt(receipt)
        if identity != expected_identity:
            errors.append("identity does not match top-level action-attempt fields")
        if str(receipt.get("receipt_id") or "") != _sha(expected_identity)[:32]:
            errors.append("receipt_id does not match deterministic action-attempt identity hash")

    events = receipt.get("events")
    if not isinstance(events, list) or not events:
        return errors + ["events must be a non-empty array"]
    expected = "planned"
    for i, event in enumerate(events):
        if not isinstance(event, dict):
            errors.append(f"events[{i}] must be an object"); continue
        state = event.get("state")
        if state not in STATES:
            errors.append(f"events[{i}] has unknown state {state!r}")
        if i == 0:
            if state != "planned": errors.append("first event must be planned")
            if event.get("from_state") not in (None, ""):
                errors.append("first planned event must not have from_state")
        else:
            if event.get("from_state") != expected:
                errors.append(f"events[{i}].from_state must equal prior state {expected!r}")
            if state not in TRANSITIONS.get(expected, set()):
                errors.append(f"illegal historical transition: {expected} -> {state}")
        expected = str(state or "")
        if event.get("sequence") != i + 1:
            errors.append(f"events[{i}].sequence must equal {i + 1}")
        if not str(event.get("at") or "").strip(): errors.append(f"events[{i}].at required")
        if not str(event.get("actor") or "").strip(): errors.append(f"events[{i}].actor required")
        if not str(event.get("evidence") or "").strip(): errors.append(f"events[{i}].evidence required")
        details = event.get("details")
        if not isinstance(details, dict):
            errors.append(f"events[{i}].details must be an object"); details = {}
        if state == "verified" and details.get("postconditions_verified") is not True:
            errors.append("verified event lacks postconditions_verified=true")
        if state == "compensated" and details.get("compensation_verified") is not True:
            errors.append("compensated event lacks compensation_verified=true")
    if receipt.get("state") != expected:
        errors.append("receipt current state does not match last event")
    return errors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    sub = ap.add_subparsers(dest="command", required=True)

    b = sub.add_parser("begin")
    b.add_argument("--plan", required=True)
    b.add_argument("--attempt-no", type=int, default=1)
    b.add_argument("--actor", required=True)
    b.add_argument("--evidence", required=True)

    t = sub.add_parser("transition")
    t.add_argument("receipt_id")
    t.add_argument("--state", choices=STATES, required=True)
    t.add_argument("--actor", required=True)
    t.add_argument("--evidence", required=True)
    t.add_argument("--details-json", default="{}")

    v = sub.add_parser("validate")
    v.add_argument("receipt_id")

    ns = ap.parse_args(argv)
    vault = _vault(ns.vault)
    if ns.command == "begin":
        plan = json.loads(Path(ns.plan).read_text(encoding="utf-8"))
        result = begin_receipt(plan, vault=vault, attempt_no=ns.attempt_no, actor=ns.actor, evidence=ns.evidence)
    elif ns.command == "transition":
        details = json.loads(ns.details_json)
        if not isinstance(details, dict): raise ValueError("--details-json must be a JSON object")
        result = transition_receipt(ns.receipt_id, ns.state, vault=vault, actor=ns.actor,
                                    evidence=ns.evidence, details=details)
    else:
        result = _load(_receipt_path(vault, ns.receipt_id))
        errors = validate_receipt(result)
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2)); return 0 if not errors else 1
    print(json.dumps({"ok": True, "receipt_id": result["receipt_id"], "state": result["state"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
