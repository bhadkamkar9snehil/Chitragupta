#!/usr/bin/env python3
"""GBrain result normalization helpers for governed L2 retrieval."""
from __future__ import annotations
from kb_retrieval_routing import *

def _frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n") or (end := text.find("\n---\n", 4)) < 0: return {}, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" not in line: continue
        key, raw = line.split(":", 1); raw = raw.strip()
        try: meta[key.strip()] = json.loads(raw)
        except Exception: meta[key.strip()] = raw.strip("'\"")
    return meta, text[end + 5:]


def _vault(value: str | None = None) -> Path:
    raw = value or os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _iter_gbrain_rows(payload: Any) -> list[dict[str, Any]]:
    """Best-effort normalization of GBrain search output without trusting its synthesis."""
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("results", "hits", "items", "documents", "data"):
        value = payload.get(key)
        if isinstance(value, list):
            return [row for row in value if isinstance(row, dict)]
        if isinstance(value, dict):
            nested = _iter_gbrain_rows(value)
            if nested:
                return nested
    return []


def _gbrain_ref(row: dict[str, Any]) -> str:
    for key in ("path", "file", "file_path", "source_ref", "uri", "source"):
        value = row.get(key)
        if isinstance(value, str) and value.strip():
            return value.replace("\\", "/")
        if isinstance(value, dict):
            for nested_key in ("path", "file", "uri", "id"):
                nested = value.get(nested_key)
                if isinstance(nested, str) and nested.strip():
                    return nested.replace("\\", "/")
    meta = row.get("metadata")
    if isinstance(meta, dict):
        for key in ("path", "file", "source_ref", "uri"):
            value = meta.get(key)
            if isinstance(value, str) and value.strip():
                return value.replace("\\", "/")
    return ""


def _gbrain_score(row: dict[str, Any], fallback: float) -> float:
    for key in ("score", "retrieval_score", "similarity", "rank_score", "rrf_score"):
        value = row.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value)
    return fallback


def _gbrain_rank_hints(result: dict[str, Any]) -> dict[str, tuple[int, float]]:
    rows = _iter_gbrain_rows(result.get("results"))
    hints: dict[str, tuple[int, float]] = {}
    for rank, row in enumerate(rows, 1):
        ref = _gbrain_ref(row)
        if not ref:
            continue
        basename = Path(ref).name.lower()
        if not basename:
            continue
        score = _gbrain_score(row, max(0.0, 100.0 - rank))
        current = hints.get(basename)
        if current is None or rank < current[0]:
            hints[basename] = (rank, score)
    return hints


def gbrain_scope_search(query: str, *, scope: str, limit: int = 5) -> dict[str, Any]:
    try:
        from l2_gbrain import available, search
        if not available():
            raise RuntimeError("isolated GBrain unavailable")
        result = search(query, scope=scope, mode="hybrid", limit=limit, automatic=True)
    except Exception as exc:
        return {
            "ok": False,
            "backend": "gbrain",
            "scope": scope,
            "source_ids": [],
            "error": f"{type(exc).__name__}: {exc}"[:800],
            "results": [],
        }
    if result.get("ok"):
        return result
    return {
        "ok": False,
        "backend": "gbrain",
        "scope": scope,
        "source_ids": result.get("source_ids") or [],
        "error": result.get("error") or "GBrain retrieval failed",
        "results": [],
    }




__all__=[name for name in globals() if not name.startswith("__")]
