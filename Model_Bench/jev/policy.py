"""Central Jev policy/configuration for Chitragupta."""
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
TOOL_RERANK_ENABLED = _bool_env("CHITRAGUPTA_JEV_TOOL_RERANK_ENABLED", True)
ROW_RERANK_ENABLED = _bool_env("CHITRAGUPTA_JEV_ROW_RERANK_ENABLED", True)
KB_JUDGMENTS_ENABLED = _bool_env("CHITRAGUPTA_JEV_KB_ENABLED", True)
PREFLIGHT_ENABLED = _bool_env("CHITRAGUPTA_JEV_PREFLIGHT_ENABLED", True)
TRACE_ASSESSMENT_ENABLED = _bool_env("CHITRAGUPTA_JEV_TRACE_ENABLED", True)
SECURITY_SCREEN_ENABLED = _bool_env("CHITRAGUPTA_JEV_SECURITY_ENABLED", True)
ADAPTIVE_REVIEW_ENABLED = _bool_env("CHITRAGUPTA_JEV_ADAPTIVE_REVIEW_ENABLED", True)
SEMANTIC_TOOL_BLOCKING_ENABLED = _bool_env("CHITRAGUPTA_JEV_SEMANTIC_TOOL_BLOCKING_ENABLED", True)

MIN_CHOICE_CONFIDENCE = _float_env("CHITRAGUPTA_JEV_MIN_CONFIDENCE", 0.70)
HIGH_RISK_NOUL = _float_env("CHITRAGUPTA_JEV_HIGH_RISK_NOUL", 0.85)
LOW_RISK_NOUL = _float_env("CHITRAGUPTA_JEV_LOW_RISK_NOUL", 0.15)

POLICY_VERSION = os.environ.get("CHITRAGUPTA_JEV_POLICY_VERSION", "jev-fabric-v1")

JEV_PRIMARY_REVIEW_ENABLED = _bool_env("CHITRAGUPTA_JEV_PRIMARY_REVIEW_ENABLED", True)
JEV_FIRST_INVESTIGATION_ENABLED = _bool_env("CHITRAGUPTA_JEV_FIRST_INVESTIGATION_ENABLED", True)
LOCAL_REVIEW_ON_UNCERTAINTY = _bool_env("CHITRAGUPTA_JEV_LOCAL_REVIEW_ON_UNCERTAINTY", True)
DIRECT_JEV_APPROVAL_CONFIDENCE = _float_env("CHITRAGUPTA_JEV_DIRECT_APPROVAL_CONFIDENCE", 0.82)
DIRECT_JEV_REWORK_CONFIDENCE = _float_env("CHITRAGUPTA_JEV_DIRECT_REWORK_CONFIDENCE", 0.88)
