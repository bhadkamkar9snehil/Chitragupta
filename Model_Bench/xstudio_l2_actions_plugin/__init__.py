"""xstudio-l2-actions — deterministic shadow planning for future XBatch remediation.

This plugin intentionally has NO execution operation. It turns the capability
registry into a model-visible, machine-validated planning surface while keeping
side effects impossible from this toolset.

The separation is deliberate:

    reasoning about a corrective action
        != a valid capability plan
        != permission to execute
        != successful postcondition verification

Future supervised/autonomous execution belongs behind a separate deterministic
executor that consumes a validated plan and re-checks the registry, evidence,
preconditions, approval policy, idempotency, and postconditions at execution
time. This planner can therefore be deployed while the action registry is empty
and global_mode=observe.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PLUGIN_NAME = "xstudio-l2-actions"
TOOLSET = "l2_actions"
TOOL_NAME = "l2_action"

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
_PLAN_ID_RE = re.compile(r"^[a-f0-9]{32}$")
_CAPABILITY_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]{2,120}$")
_MODE_RANK = {"observe": 0, "recommend": 1, "shadow": 2, "supervised": 3, "autonomous": 4}
_MAX_RATIONALE_CHARS = max(500, int(os.environ.get("L2_ACTION_MAX_RATIONALE_CHARS", "4000")))
_MAX_EVIDENCE_ITEMS = max(1, int(os.environ.get("L2_ACTION_MAX_EVIDENCE_ITEMS", "20")))
_MAX_PLAN_RESULTS = max(1, int(os.environ.get("L2_ACTION_MAX_PLAN_RESULTS", "10")))


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _vault() -> Path:
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _registry_candidates() -> list[Path]:
    values: list[Path] = []
    if os.environ.get("CHITRAGUPTA_XSTUDIO_ACTION_REGISTRY"):
        values.append(Path(os.environ["CHITRAGUPTA_XSTUDIO_ACTION_REGISTRY"]).expanduser())
    here = Path(__file__).resolve()
    values.extend([
        here.parent.parent / "scripts" / "xstudio_action_capabilities.json",
        Path.home() / ".hermes" / "profiles" / "l2-investigator" / "scripts" / "xstudio_action_capabilities.json",
        here.parent.parent.parent / "deploy" / "xstudio_action_capabilities.json",
    ])
    seen: set[str] = set()
    out: list[Path] = []
    for p in values:
        key = str(p)
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


def _load_registry() -> tuple[Path, dict[str, Any], str]:
    for path in _registry_candidates():
        if not path.exists():
            continue
        raw = path.read_bytes()
        try:
            data = json.loads(raw.decode("utf-8"))
        except Exception as exc:
            raise ValueError(f"invalid action registry {path}: {exc}") from exc
        if not isinstance(data, dict):
            raise ValueError(f"invalid action registry {path}: top level must be object")
        return path, data, hashlib.sha256(raw).hexdigest()
    raise FileNotFoundError(
        "xstudio_action_capabilities.json not found; deploy the adaptive L2 runtime "
        "or set CHITRAGUPTA_XSTUDIO_ACTION_REGISTRY"
    )


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)


def _hash(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _capabilities(registry: dict[str, Any]) -> list[dict[str, Any]]:
    caps = registry.get("capabilities") or []
    return [x for x in caps if isinstance(x, dict)]


def _find_capability(registry: dict[str, Any], capability_id: str) -> dict[str, Any] | None:
    for cap in _capabilities(registry):
        if str(cap.get("id") or "") == capability_id:
            return cap
    return None


def _effective_mode(registry: dict[str, Any], capability: dict[str, Any]) -> str:
    gr = _MODE_RANK.get(str(registry.get("global_mode") or "observe"), 0)
    cr = _MODE_RANK.get(str(capability.get("mode") or "observe"), 0)
    target = min(gr, cr)
    return next((mode for mode, rank in _MODE_RANK.items() if rank == target), "observe")


def _type_ok(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def _validate_value(value: Any, schema: dict[str, Any], path: str, errors: list[str]) -> None:
    expected = schema.get("type")
    if isinstance(expected, str) and not _type_ok(value, expected):
        errors.append(f"{path}: expected {expected}")
        return
    if "enum" in schema and value not in schema.get("enum", []):
        errors.append(f"{path}: value not in enum")
        return
    if isinstance(value, dict):
        properties = schema.get("properties") or {}
        required = schema.get("required") or []
        for key in required:
            if key not in value:
                errors.append(f"{path}.{key}: required")
        if schema.get("additionalProperties") is False:
            extras = sorted(set(value) - set(properties))
            if extras:
                errors.append(f"{path}: unexpected properties {extras}")
        for key, child in value.items():
            child_schema = properties.get(key)
            if isinstance(child_schema, dict):
                _validate_value(child, child_schema, f"{path}.{key}", errors)
    if isinstance(value, list):
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for i, item in enumerate(value):
                _validate_value(item, item_schema, f"{path}[{i}]", errors)
    if isinstance(value, str):
        if isinstance(schema.get("minLength"), int) and len(value) < schema["minLength"]:
            errors.append(f"{path}: shorter than minLength")
        if isinstance(schema.get("maxLength"), int) and len(value) > schema["maxLength"]:
            errors.append(f"{path}: longer than maxLength")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if isinstance(schema.get("minimum"), (int, float)) and value < schema["minimum"]:
            errors.append(f"{path}: below minimum")
        if isinstance(schema.get("maximum"), (int, float)) and value > schema["maximum"]:
            errors.append(f"{path}: above maximum")


def _validate_parameters(capability: dict[str, Any], parameters: Any) -> list[str]:
    schema = capability.get("parameter_schema")
    if not isinstance(schema, dict):
        return ["capability parameter_schema is missing/invalid"]
    errors: list[str] = []
    _validate_value(parameters, schema, "parameters", errors)
    return errors


def _normalize_evidence(value: Any) -> tuple[list[dict[str, str]], list[str]]:
    if value is None:
        return [], []
    if not isinstance(value, list):
        return [], ["evidence must be an array"]
    if len(value) > _MAX_EVIDENCE_ITEMS:
        return [], [f"evidence exceeds maximum {_MAX_EVIDENCE_ITEMS} items"]
    items: list[dict[str, str]] = []
    errors: list[str] = []
    for i, item in enumerate(value):
        if not isinstance(item, dict):
            errors.append(f"evidence[{i}] must be an object")
            continue
        eid = str(item.get("id") or "").strip()
        source = str(item.get("source") or "").strip()
        reference = str(item.get("reference") or "").strip()
        claim = str(item.get("claim") or "").strip()
        if not eid:
            errors.append(f"evidence[{i}].id is required")
        if not source:
            errors.append(f"evidence[{i}].source is required")
        if not reference:
            errors.append(f"evidence[{i}].reference is required")
        if not claim:
            errors.append(f"evidence[{i}].claim is required")
        items.append({"id": eid[:120], "source": source[:120], "reference": reference[:500], "claim": claim[:1000]})
    return items, errors


def _required_evidence_ids(capability: dict[str, Any]) -> set[str]:
    required: set[str] = set()
    for item in capability.get("required_evidence") or []:
        value = item.strip() if isinstance(item, str) else str(item.get("id") or "").strip() if isinstance(item, dict) else ""
        if value:
            required.add(value)
    return required


def _validate_evidence(capability: dict[str, Any], evidence: list[dict[str, str]]) -> list[str]:
    present = {x.get("id", "") for x in evidence}
    missing = sorted(_required_evidence_ids(capability) - present)
    return [f"required evidence not supplied: {', '.join(missing)}"] if missing else []


def _plan_dir() -> Path:
    path = _vault() / "actions" / "plans"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _plan_context(params: dict[str, Any], kwargs: dict[str, Any]) -> dict[str, str]:
    return {
        "run_id": str(params.get("run_id") or kwargs.get("run_id") or "").strip()[:120],
        "ticket_id": str(params.get("ticket_id") or kwargs.get("ticket_id") or "").strip()[:120],
        "task_id": str(kwargs.get("task_id") or params.get("task_id") or "").strip()[:120],
        "session_id": str(kwargs.get("session_id") or "").strip()[:160],
        "profile": str(kwargs.get("profile") or os.environ.get("HERMES_PROFILE") or "").strip()[:160],
    }


def _public_capability(cap: dict[str, Any], registry: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": cap.get("id"), "description": cap.get("description"), "risk": cap.get("risk"),
        "configured_mode": cap.get("mode"), "global_mode": registry.get("global_mode"),
        "effective_mode": _effective_mode(registry, cap), "parameter_schema": cap.get("parameter_schema"),
        "preconditions": cap.get("preconditions"), "required_evidence": cap.get("required_evidence"),
        "verification": cap.get("verification"), "rollback": cap.get("rollback"),
        "approval_policy": cap.get("approval_policy"),
    }


def _list_capabilities() -> str:
    try:
        path, registry, digest = _load_registry()
    except Exception as exc:
        return json.dumps({"ok": False, "error": str(exc), "retry_same_call": False})
    return json.dumps({"ok": True, "operation": "list", "registry": str(path), "registry_sha256": digest,
                       "global_mode": registry.get("global_mode"),
                       "capabilities": [_public_capability(c, registry) for c in _capabilities(registry)],
                       "execution_tool_available": False}, ensure_ascii=False)


def _describe(params: dict[str, Any]) -> str:
    cid = str(params.get("capability_id") or "").strip()
    if not _CAPABILITY_ID_RE.match(cid):
        return json.dumps({"ok": False, "error": "valid capability_id is required", "retry_same_call": False})
    try:
        path, registry, digest = _load_registry()
    except Exception as exc:
        return json.dumps({"ok": False, "error": str(exc), "retry_same_call": False})
    cap = _find_capability(registry, cid)
    if not cap:
        return json.dumps({"ok": False, "error": f"unknown capability: {cid}", "retry_same_call": False})
    return json.dumps({"ok": True, "operation": "describe", "registry": str(path), "registry_sha256": digest,
                       "capability": _public_capability(cap, registry), "capability_sha256": _hash(cap),
                       "execution_tool_available": False}, ensure_ascii=False)


def _plan(params: dict[str, Any], **kwargs: Any) -> str:
    cid = str(params.get("capability_id") or "").strip()
    if not _CAPABILITY_ID_RE.match(cid):
        return json.dumps({"ok": False, "error": "valid capability_id is required", "retry_same_call": False})
    try:
        registry_path, registry, registry_digest = _load_registry()
    except Exception as exc:
        return json.dumps({"ok": False, "error": str(exc), "retry_same_call": False})
    cap = _find_capability(registry, cid)
    if not cap:
        return json.dumps({"ok": False, "error": f"unknown capability: {cid}", "retry_same_call": False})
    effective = _effective_mode(registry, cap)
    if _MODE_RANK.get(effective, 0) < _MODE_RANK["recommend"]:
        return json.dumps({"ok": False,
                           "error": f"capability {cid} is not active for recommendation/shadow planning (global={registry.get('global_mode')}, capability={cap.get('mode')}, effective={effective})",
                           "retry_same_call": False, "execution_authorized": False})
    parameters = params.get("parameters") if params.get("parameters") is not None else {}
    parameter_errors = _validate_parameters(cap, parameters)
    evidence, evidence_errors = _normalize_evidence(params.get("evidence"))
    evidence_errors.extend(_validate_evidence(cap, evidence))
    errors = parameter_errors + evidence_errors
    if errors:
        return json.dumps({"ok": False, "error": "plan validation failed", "validation_errors": errors,
                           "retry_same_call": False, "execution_authorized": False}, ensure_ascii=False)
    rationale = str(params.get("rationale") or "").strip()[:_MAX_RATIONALE_CHARS]
    context = _plan_context(params, kwargs)
    if not context["run_id"] or not context["ticket_id"]:
        return json.dumps({"ok": False, "error": "run_id and ticket_id are required for durable action-plan provenance",
                           "retry_same_call": False, "execution_authorized": False})
    cap_digest = _hash(cap)
    identity = {"capability_id": cid, "capability_sha256": cap_digest, "parameters": parameters,
                "evidence": evidence, "run_id": context["run_id"], "ticket_id": context["ticket_id"]}
    plan_id = _hash(identity)[:32]
    path = _plan_dir() / f"{plan_id}.json"
    plan = {
        "schema_version": 1, "kind": "xstudio_action_plan", "plan_id": plan_id, "created_at": _utc_now(),
        "trust": "validated_shadow_plan", "capability_id": cid, "capability_sha256": cap_digest,
        "registry_sha256": registry_digest, "registry_path": str(registry_path), "risk": cap.get("risk"),
        "configured_mode": cap.get("mode"), "global_mode": registry.get("global_mode"), "effective_mode": effective,
        "parameters": parameters, "evidence": evidence, "preconditions_to_recheck": cap.get("preconditions") or [],
        "verification_required": cap.get("verification") or [], "rollback_contract": cap.get("rollback") or {},
        "approval_policy": cap.get("approval_policy") or {}, "context": context, "rationale": rationale,
        "execution_authorized": False, "execution_tool_available": False,
    }
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(existing, dict) and existing.get("plan_id") == plan_id:
                return json.dumps({"ok": True, "operation": "plan", "status": "existing", "plan": existing,
                                   "path": str(path), "execution_authorized": False}, ensure_ascii=False)
        except Exception:
            pass
    path.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return json.dumps({"ok": True, "operation": "plan", "status": "created", "plan": plan, "path": str(path),
                       "execution_authorized": False,
                       "note": "Validated recommendation/shadow artifact only. It cannot execute XBatch; any future executor must re-check registry, preconditions, evidence, approval, idempotency and postconditions."}, ensure_ascii=False)


def _load_plan(plan_id: str) -> tuple[Path, dict[str, Any]]:
    if not _PLAN_ID_RE.match(plan_id):
        raise ValueError("plan_id must be a 32-character lowercase hex id")
    path = _plan_dir() / f"{plan_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"plan not found: {plan_id}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("plan file is invalid")
    return path, data


def _validate_plan(params: dict[str, Any]) -> str:
    plan_id = str(params.get("plan_id") or "").strip()
    try:
        path, plan = _load_plan(plan_id)
        registry_path, registry, registry_digest = _load_registry()
    except Exception as exc:
        return json.dumps({"ok": False, "error": str(exc), "retry_same_call": False, "execution_authorized": False})
    cid = str(plan.get("capability_id") or "")
    cap = _find_capability(registry, cid)
    errors: list[str] = []
    if not cap:
        errors.append("capability no longer exists")
    else:
        if _hash(cap) != plan.get("capability_sha256"):
            errors.append("capability changed since plan creation")
        errors.extend(_validate_parameters(cap, plan.get("parameters")))
        evidence = plan.get("evidence") if isinstance(plan.get("evidence"), list) else []
        errors.extend(_validate_evidence(cap, evidence))
        current_effective = _effective_mode(registry, cap)
        if _MODE_RANK.get(current_effective, 0) < _MODE_RANK["recommend"]:
            errors.append(f"capability is no longer active for planning (effective={current_effective})")
    return json.dumps({"ok": not errors, "operation": "validate_plan",
                       "status": "valid" if not errors else "stale_or_invalid", "plan_id": plan_id,
                       "path": str(path), "registry": str(registry_path),
                       "registry_drift": registry_digest != plan.get("registry_sha256"),
                       "validation_errors": errors, "execution_authorized": False,
                       "execution_tool_available": False}, ensure_ascii=False)


def _plans(params: dict[str, Any]) -> str:
    run_id = str(params.get("run_id") or "").strip()
    ticket_id = str(params.get("ticket_id") or "").strip()
    if not run_id and not ticket_id:
        return json.dumps({"ok": False, "error": "run_id or ticket_id is required", "retry_same_call": False})
    found: list[dict[str, Any]] = []
    for path in sorted(_plan_dir().glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
        if len(found) >= _MAX_PLAN_RESULTS:
            break
        try:
            plan = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        context = plan.get("context") if isinstance(plan.get("context"), dict) else {}
        if run_id and str(context.get("run_id") or "") != run_id:
            continue
        if ticket_id and str(context.get("ticket_id") or "") != ticket_id:
            continue
        found.append({"plan_id": plan.get("plan_id"), "capability_id": plan.get("capability_id"),
                      "risk": plan.get("risk"), "effective_mode": plan.get("effective_mode"),
                      "created_at": plan.get("created_at"), "parameters": plan.get("parameters"),
                      "execution_authorized": False})
    return json.dumps({"ok": True, "operation": "plans", "run_id": run_id, "ticket_id": ticket_id,
                       "plans": found, "execution_authorized": False}, ensure_ascii=False)


def _handler(params: dict[str, Any], **kwargs: Any) -> str:
    operation = str(params.get("operation") or "list")
    if operation == "list":
        return _list_capabilities()
    if operation == "describe":
        return _describe(params)
    if operation == "plan":
        return _plan(params, **kwargs)
    if operation == "validate_plan":
        return _validate_plan(params)
    if operation == "plans":
        return _plans(params)
    return json.dumps({"ok": False, "error": f"unknown operation: {operation}", "retry_same_call": False})


_SCHEMA = {
    "name": TOOL_NAME,
    "description": (
        "Deterministic XBatch corrective-action planning surface. It can list registered capabilities, describe their safety contracts, create validated recommendation/shadow plans, find plans for a run, and revalidate a plan against the current registry. It CANNOT execute an action. Use only after the current-ticket cause/evidence is established; planning is not evidence and never authorizes a write."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "operation": {"type": "string", "enum": ["list", "describe", "plan", "plans", "validate_plan"]},
            "capability_id": {"type": "string"}, "parameters": {"type": "object"},
            "evidence": {"type": "array", "items": {"type": "object", "properties": {
                "id": {"type": "string"}, "source": {"type": "string"},
                "reference": {"type": "string"}, "claim": {"type": "string"}},
                "required": ["id", "source", "reference", "claim"], "additionalProperties": False}},
            "rationale": {"type": "string"}, "run_id": {"type": "string"}, "ticket_id": {"type": "string"},
            "task_id": {"type": "string"}, "plan_id": {"type": "string"},
        },
        "required": ["operation"], "additionalProperties": False,
    },
}


def register(ctx: Any) -> None:
    ctx.register_tool(name=TOOL_NAME, toolset=TOOLSET, schema=_SCHEMA, handler=_handler,
                      description="Validated XBatch action recommendation/shadow-plan interface; execution intentionally unavailable.")
