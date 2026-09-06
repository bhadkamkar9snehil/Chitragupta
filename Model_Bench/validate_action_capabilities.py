#!/usr/bin/env python3
"""Validate the XBatch corrective-action capability registry.

The registry is executable-policy input even while the current plugin exposes
planning only. Validation is intentionally stricter than documentation: unsafe
or ambiguous capability shapes fail deployment instead of being interpreted by
an LLM at runtime.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ROOT / "deploy" / "xstudio_action_capabilities.json"
ID_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]{2,120}$")
MODE_RANK = {"observe": 0, "recommend": 1, "shadow": 2, "supervised": 3, "autonomous": 4}
ALLOWED_EXECUTION_TYPES = {"stored_procedure", "api", "service_action", "script", "none"}
ALLOWED_SCHEMA_KEYS = {
    "type", "properties", "required", "additionalProperties", "items",
    "enum", "minimum", "maximum", "minLength", "maxLength", "description",
}
ALLOWED_SCHEMA_TYPES = {"object", "array", "string", "integer", "number", "boolean", "null"}


def _validate_parameter_schema(schema: Any, path: str, errors: list[str]) -> None:
    if not isinstance(schema, dict):
        errors.append(f"{path} must be an object"); return
    unknown = sorted(set(schema) - ALLOWED_SCHEMA_KEYS)
    if unknown: errors.append(f"{path} uses unsupported schema keywords: {', '.join(unknown)}")
    stype = schema.get("type")
    if stype not in ALLOWED_SCHEMA_TYPES:
        errors.append(f"{path}.type must be one of {sorted(ALLOWED_SCHEMA_TYPES)}"); return
    if "enum" in schema and not isinstance(schema["enum"], list): errors.append(f"{path}.enum must be an array")
    if stype == "object":
        properties = schema.get("properties")
        if not isinstance(properties, dict):
            errors.append(f"{path}.properties must be an object"); properties = {}
        required = schema.get("required", [])
        if not isinstance(required, list) or not all(isinstance(x, str) for x in required):
            errors.append(f"{path}.required must be an array of property names"); required = []
        missing = sorted(set(required) - set(properties))
        if missing: errors.append(f"{path}.required references unknown properties: {', '.join(missing)}")
        if schema.get("additionalProperties") is not False:
            errors.append(f"{path}.additionalProperties must be false for corrective-action parameters")
        for name, child in properties.items():
            if not isinstance(name, str) or not name:
                errors.append(f"{path}.properties contains an invalid property name"); continue
            _validate_parameter_schema(child, f"{path}.properties.{name}", errors)
    if stype == "array":
        items = schema.get("items")
        if not isinstance(items, dict): errors.append(f"{path}.items must be an object schema")
        else: _validate_parameter_schema(items, f"{path}.items", errors)
    if stype == "string":
        for key in ("minLength", "maxLength"):
            if key in schema and (not isinstance(schema[key], int) or schema[key] < 0): errors.append(f"{path}.{key} must be a non-negative integer")
        if isinstance(schema.get("minLength"), int) and isinstance(schema.get("maxLength"), int) and schema["minLength"] > schema["maxLength"]:
            errors.append(f"{path}.minLength cannot exceed maxLength")
    if stype in {"integer", "number"}:
        for key in ("minimum", "maximum"):
            if key in schema and not isinstance(schema[key], (int, float)): errors.append(f"{path}.{key} must be numeric")
        if isinstance(schema.get("minimum"), (int, float)) and isinstance(schema.get("maximum"), (int, float)) and schema["minimum"] > schema["maximum"]:
            errors.append(f"{path}.minimum cannot exceed maximum")


def _validate_evidence_contract(value: Any, path: str, errors: list[str]) -> None:
    if not isinstance(value, list):
        errors.append(f"{path} must be an array"); return
    seen: set[str] = set()
    for i, item in enumerate(value):
        label = f"{path}[{i}]"
        if isinstance(item, str): eid = item.strip()
        elif isinstance(item, dict):
            eid = str(item.get("id") or "").strip()
            if not str(item.get("description") or "").strip(): errors.append(f"{label}.description is required")
        else:
            errors.append(f"{label} must be a string or object"); continue
        if not eid or not ID_RE.match(eid): errors.append(f"{label}.id invalid: {eid!r}")
        elif eid in seen: errors.append(f"{path} duplicate evidence id: {eid}")
        seen.add(eid)


def _validate_steps(value: Any, path: str, errors: list[str], *, require_nonempty: bool = False) -> None:
    if not isinstance(value, list):
        errors.append(f"{path} must be an array"); return
    if require_nonempty and not value: errors.append(f"{path} must be non-empty")
    for i, step in enumerate(value):
        if not isinstance(step, (str, dict)): errors.append(f"{path}[{i}] must be a string or object")
        elif isinstance(step, str) and not step.strip(): errors.append(f"{path}[{i}] must not be blank")


def _validate_capability(cap: dict[str, Any], i: int, contract: dict[str, Any], errors: list[str], seen: set[str]) -> None:
    label = f"capabilities[{i}]"
    required = set(contract.get("required_fields") or [])
    allowed_modes = set(contract.get("allowed_modes") or [])
    allowed_risk = set(contract.get("allowed_risk") or [])
    missing = sorted(required - set(cap))
    if missing: errors.append(f"{label} missing: {', '.join(missing)}")
    cid = str(cap.get("id") or "")
    if not ID_RE.match(cid): errors.append(f"{label}.id invalid: {cid!r}")
    if cid in seen: errors.append(f"duplicate capability id: {cid}")
    seen.add(cid)
    mode, risk = cap.get("mode"), cap.get("risk")
    if mode not in allowed_modes: errors.append(f"{cid or label}: invalid mode {mode!r}")
    if risk not in allowed_risk: errors.append(f"{cid or label}: invalid risk {risk!r}")
    if not str(cap.get("description") or "").strip(): errors.append(f"{cid or label}: description must not be blank")
    _validate_parameter_schema(cap.get("parameter_schema"), f"{cid or label}.parameter_schema", errors)
    _validate_steps(cap.get("preconditions"), f"{cid or label}.preconditions", errors)
    _validate_steps(cap.get("verification"), f"{cid or label}.verification", errors)
    _validate_evidence_contract(cap.get("required_evidence"), f"{cid or label}.required_evidence", errors)
    execution = cap.get("execution")
    if not isinstance(execution, dict): errors.append(f"{cid or label}.execution must be an object"); execution = {}
    exec_type = execution.get("type")
    if exec_type not in ALLOWED_EXECUTION_TYPES: errors.append(f"{cid or label}.execution.type invalid: {exec_type!r}")
    idempotency = cap.get("idempotency")
    if not isinstance(idempotency, dict): errors.append(f"{cid or label}.idempotency must be an object"); idempotency = {}
    rollback = cap.get("rollback")
    if not isinstance(rollback, dict): errors.append(f"{cid or label}.rollback must be an object"); rollback = {}
    approval = cap.get("approval_policy")
    if not isinstance(approval, dict): errors.append(f"{cid or label}.approval_policy must be an object"); approval = {}

    if mode in {"supervised", "autonomous"}:
        if exec_type in {None, "none"}: errors.append(f"{cid}: executable capability requires concrete execution.type")
        if not str(execution.get("target") or "").strip(): errors.append(f"{cid}: executable capability requires execution.target")
        _validate_steps(cap.get("preconditions"), f"{cid}.preconditions", errors, require_nonempty=True)
        _validate_steps(cap.get("verification"), f"{cid}.verification", errors, require_nonempty=True)
        if not idempotency: errors.append(f"{cid}: executable capability requires non-empty idempotency")
        if not cap.get("required_evidence"): errors.append(f"{cid}: executable capability requires non-empty required_evidence")
        if mode == "supervised" and approval.get("requires_human_approval") is not True:
            errors.append(f"{cid}: supervised capability requires approval_policy.requires_human_approval=true")
    if mode == "autonomous":
        if risk == "critical": errors.append(f"{cid}: critical-risk capability cannot be autonomous")
        if approval.get("allows_autonomous") is not True: errors.append(f"{cid}: autonomous capability requires approval_policy.allows_autonomous=true")
        if rollback.get("strategy") in {None, "", "none"} and not (rollback.get("not_required") is True and str(rollback.get("justification") or "").strip()):
            errors.append(f"{cid}: autonomous capability requires rollback/compensation, or explicit rollback.not_required=true with justification")
        promotion = cap.get("promotion_evidence")
        if not isinstance(promotion, dict) or not promotion: errors.append(f"{cid}: autonomous capability requires non-empty promotion_evidence")


def validate(path: Path) -> list[str]:
    try: data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc: return [f"invalid JSON: {exc}"]
    if not isinstance(data, dict): return ["top-level registry must be an object"]
    contract = data.get("capability_contract") or {}
    required, allowed_modes, allowed_risk = contract.get("required_fields"), contract.get("allowed_modes"), contract.get("allowed_risk")
    errors: list[str] = []
    if data.get("schema_version") != 1: errors.append("schema_version must be 1")
    if not isinstance(contract, dict): errors.append("capability_contract must be an object")
    if not isinstance(required, list) or not required: errors.append("capability_contract.required_fields must be a non-empty array")
    if not isinstance(allowed_modes, list) or set(allowed_modes) != set(MODE_RANK): errors.append(f"allowed_modes must contain exactly {sorted(MODE_RANK)}")
    if not isinstance(allowed_risk, list) or not allowed_risk: errors.append("allowed_risk must be a non-empty array")
    if data.get("global_mode") not in set(allowed_modes or []): errors.append("global_mode is not in allowed_modes")
    caps = data.get("capabilities")
    if not isinstance(caps, list): errors.append("capabilities must be an array"); caps = []
    seen: set[str] = set()
    for i, cap in enumerate(caps):
        if not isinstance(cap, dict): errors.append(f"capabilities[{i}] must be an object"); continue
        _validate_capability(cap, i, contract, errors, seen)
    return errors


def main(argv: list[str] | None = None) -> int:
    path = Path((argv or sys.argv[1:] or [str(DEFAULT)])[0])
    errors = validate(path)
    for error in errors: print("FAIL:", error)
    if errors: return 1
    data = json.loads(path.read_text(encoding="utf-8")); caps = data.get("capabilities") or []; mode = data.get("global_mode")
    active = sum(1 for c in caps if MODE_RANK.get(str(c.get("mode")), 0) and MODE_RANK[str(c.get("mode"))] <= MODE_RANK.get(mode, 0))
    print(f"action registry valid: global_mode={mode} capabilities={len(caps)} active_at_or_below_global={active}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
