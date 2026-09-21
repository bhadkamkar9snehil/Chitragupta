"""Small set of Jev policy values that are actually consumed at runtime."""
from __future__ import annotations

import os


def _bool_env(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() not in {"0", "false", "no", "off", "disabled"}


def _float_env(name: str, default: float) -> float:
    raw = os.environ.get(name)
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


JEV_ENABLED = _bool_env("CHITRAGUPTA_JEV_ENABLED", True)
AUDIT_ENABLED = _bool_env("CHITRAGUPTA_JEV_AUDIT_ENABLED", True)
KB_JUDGMENTS_ENABLED = _bool_env("CHITRAGUPTA_JEV_KB_ENABLED", True)
TRACE_ASSESSMENT_ENABLED = _bool_env("CHITRAGUPTA_JEV_TRACE_ENABLED", True)
SECURITY_SCREEN_ENABLED = _bool_env("CHITRAGUPTA_JEV_SECURITY_ENABLED", True)

MIN_CHOICE_CONFIDENCE = _float_env("CHITRAGUPTA_JEV_MIN_CONFIDENCE", 0.70)
HIGH_RISK_NOUL = _float_env("CHITRAGUPTA_JEV_HIGH_RISK_NOUL", 0.85)

POLICY_VERSION = os.environ.get("CHITRAGUPTA_JEV_POLICY_VERSION", "jev-fabric-v1")
