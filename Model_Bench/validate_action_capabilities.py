#!/usr/bin/env python3
"""Validate the future XBatch corrective-action capability registry.

This does not grant action authority. It makes the future execution contract
machine-checkable now, while the registry is still observe-only/empty.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ROOT / "deploy" / "xstudio_action_capabilities.json"
ID_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]{2,120}$")


def main(argv: list[str] | None = None) -> int:
    path = Path((argv or sys.argv[1:] or [str(DEFAULT)])[0])
    data = json.loads(path.read_text(encoding="utf-8"))
    contract = data.get("capability_contract") or {}
    required = set(contract.get("required_fields") or [])
    allowed_modes = set(contract.get("allowed_modes") or [])
    allowed_risk = set(contract.get("allowed_risk") or [])
    caps = data.get("capabilities") or []
    errors: list[str] = []
    seen: set[str] = set()

    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if data.get("global_mode") not in allowed_modes:
        errors.append("global_mode is not in allowed_modes")

    for i, cap in enumerate(caps):
        label = f"capabilities[{i}]"
        missing = sorted(required - set(cap))
        if missing:
            errors.append(f"{label} missing: {', '.join(missing)}")
        cid = str(cap.get("id") or "")
        if not ID_RE.match(cid):
            errors.append(f"{label}.id invalid: {cid!r}")
        if cid in seen:
            errors.append(f"duplicate capability id: {cid}")
        seen.add(cid)
        if cap.get("mode") not in allowed_modes:
            errors.append(f"{cid or label}: invalid mode {cap.get('mode')!r}")
        if cap.get("risk") not in allowed_risk:
            errors.append(f"{cid or label}: invalid risk {cap.get('risk')!r}")

        # Autonomous capabilities require a complete safety envelope. This is
        # deliberately structural; prose claiming an action is safe is not enough.
        if cap.get("mode") == "autonomous":
            for field in ("preconditions", "idempotency", "verification", "rollback", "required_evidence"):
                if not cap.get(field):
                    errors.append(f"{cid}: autonomous capability requires non-empty {field}")

    for error in errors:
        print("FAIL:", error)
    if errors:
        return 1
    print(f"action registry valid: global_mode={data.get('global_mode')} capabilities={len(caps)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
