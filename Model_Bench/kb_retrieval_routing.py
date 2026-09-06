#!/usr/bin/env python3
"""Governed deterministic retrieval for Chitragupta L2.

Reusable Solutions are never read directly from live Solution SQL here. Only
hash-approved exports under ``solutions/approved`` are eligible. Canonical Git
Knowledge, reviewed facts and explicitly-scoped GBrain search complete the
retrieval surface. Live XStudio/SQL remains current-ticket truth.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

from l2_context_envelope import make_context_item

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "Knowledge" / "manifest.json"
DEPLOYED_MANIFEST_PATH = Path(__file__).resolve().parent / "knowledge_manifest.json"
DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
MIN_MATCHED_TERMS = 2
MAX_RESULTS = 5
STOPWORDS = {
    "the", "a", "an", "is", "was", "were", "are", "be", "and", "or", "for",
    "with", "this", "that", "on", "in", "at", "to", "of", "it", "as", "by",
    "from", "has", "have", "not", "no", "why", "what", "when", "where", "how",
    "issue", "problem", "ticket", "please", "check", "getting", "showing",
}
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_\-]*")


def tokenize(text: str) -> set[str]:
    return {t.lower() for t in TOKEN_RE.findall(text or "")
            if len(t) > 2 and t.lower() not in STOPWORDS}


def _manifest_candidates(path: Path | None = None) -> list[Path]:
    if path is not None:
        return [path]
    configured = os.environ.get("CHITRAGUPTA_L2_KNOWLEDGE_MANIFEST", "").strip()
    out = [Path(configured).expanduser()] if configured else []
    out.extend([MANIFEST_PATH, DEPLOYED_MANIFEST_PATH])
    return out


def load_manifest(path: Path | None = None) -> dict[str, Any]:
    candidates = _manifest_candidates(path)
    selected = next((candidate for candidate in candidates if candidate.is_file()), None)
    if selected is None:
        raise FileNotFoundError(
            "Knowledge routing manifest not found; checked: "
            + ", ".join(str(candidate) for candidate in candidates)
        )
    data = json.loads(selected.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Knowledge manifest must be an object")
    return data


def _identifier_routes(manifest: dict[str, Any]):
    for identifier, configured in (manifest.get("identifier_routing") or {}).items():
        if isinstance(configured, list):
            routes = tuple(str(v) for v in configured if v)
        elif isinstance(configured, str):
            routes = tuple(v.strip() for v in configured.split(" or ") if v.strip())
        else:
            continue
        if routes:
            yield re.compile(rf"\b{re.escape(str(identifier))}\b", re.I), routes, f"{identifier} identifier"


def route_candidates(query: str, manifest: dict[str, Any], top: int = 3) -> list[dict[str, Any]]:
    q = tokenize(query); scores: dict[str, float] = {}; reasons: dict[str, list[str]] = {}
    for pattern, routes, reason in _identifier_routes(manifest):
        if pattern.search(query):
            for route in routes:
                scores[route] = scores.get(route, 0.0) + 30.0
                reasons.setdefault(route, []).append(reason)
    lower = query.lower()
    for rd in manifest.get("routes", []):
        route = rd.get("route")
        if not route or route == "discover":
            continue
        route_tokens = tokenize(" ".join([
            str(route).replace("_", " "), str(rd.get("description") or ""),
            " ".join(str(v) for v in (rd.get("keywords") or [])),
        ]))
        overlap = sorted(q & route_tokens)
        if overlap:
            scores[route] = scores.get(route, 0.0) + 3.0 * len(overlap)
            reasons.setdefault(route, []).append("keywords: " + ", ".join(overlap[:8]))
        phrases = [str(v) for v in (rd.get("keywords") or []) if " " in str(v) and str(v).lower() in lower]
        if phrases:
            scores[route] = scores.get(route, 0.0) + 5.0 * len(phrases)
            reasons.setdefault(route, []).append("phrases: " + ", ".join(phrases[:4]))
    ranked = sorted(scores.items(), key=lambda v: (-v[1], v[0]))[:max(1, top)]
    if not ranked:
        return [{"route": "discover", "score": 0.0, "reasons": ["no deterministic route signal"]}]
    return [{"route": r, "score": round(s, 2), "reasons": reasons.get(r, [])} for r, s in ranked]


def knowledge_docs_for_routes(manifest: dict[str, Any], routes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    defs = {r.get("route"): r for r in manifest.get("routes", [])}; seen = set(); out = []
    for path in manifest.get("always_load", []):
        path = str(path)
        if path not in seen:
            seen.add(path); out.append({"path": f"Knowledge/{path}", "reason": "always_load", "route": None})
    for candidate in routes:
        route = candidate["route"]; rd = defs.get(route) or {}
        configured = rd.get("canonical_docs") if rd.get("canonical_docs") is not None else (rd.get("load") or [])
        for path in configured:
            path = str(path)
            if path not in seen:
                seen.add(path); out.append({"path": f"Knowledge/{path}", "reason": "route", "route": route})
    return out


def live_sql_leads_for_routes(manifest: dict[str, Any], routes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    defs = {r.get("route"): r for r in manifest.get("routes", [])}; seen = set(); out = []
    for candidate in routes:
        route = candidate["route"]
        for value in (defs.get(route) or {}).get("live_sql_leads", []):
            value = str(value)
            if value not in seen:
                seen.add(value); out.append({"object": value, "route": route, "verification_required": True})
    return out


def _anchor(value: str) -> str:
    return re.sub(r"[^a-z0-9 _-]", "", value.lower()).replace(" ", "-")


def _first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        m = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return fallback


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _vault(value: str | None = None) -> Path:
    raw = value or os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _vault_canonical_path(vault: Path, filename: str) -> tuple[Path | None, str | None]:
    path = vault / "knowledge" / "git" / filename
    manifest_path = vault / "corpus_manifest.json"
    if not path.is_file():
        return None, "canonical document missing from governed vault mirror"
    if not manifest_path.is_file():
        return None, "learning corpus manifest missing; cannot trust deployed canonical mirror"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, f"learning corpus manifest invalid: {exc}"
    expected = None
    source_name = f"Knowledge/{filename}".replace("\\", "/")
    for item in manifest.get("files") or []:
        if isinstance(item, dict) and str(item.get("source") or "").replace("\\", "/") == source_name:
            expected = str(item.get("sha256") or "")
            break
    if not expected:
        return None, "canonical document is not declared in learning corpus manifest"
    actual = _sha256_file(path)
    if actual != expected:
        return None, f"canonical mirror hash mismatch: expected {expected}, got {actual}"
    return path, None


def read_canonical_reference(
    reference: str, *, root: Path | None = None, vault: Path | None = None,
    max_chars: int | None = None,
) -> dict[str, Any]:
    root = root or ROOT
    vault = vault or _vault()
    rel = reference.removeprefix("Knowledge/")
    filename, sep, anchor = rel.partition("#")
    source_ref = f"Knowledge/{rel}"
    repo_path = root / "Knowledge" / filename
    if repo_path.is_file():
        path = repo_path
    else:
        path, error = _vault_canonical_path(vault, filename)
        if path is None:
            return {"ok": False, "source_ref": source_ref, "error": error or "canonical document missing"}
    text = path.read_text(encoding="utf-8", errors="replace")
    if sep:
        lines = text.splitlines(); start = level = None
        for i, line in enumerate(lines):
            m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if m and _anchor(m.group(2)) == anchor.lower(): start, level = i, len(m.group(1)); break
        if start is None:
            return {"ok": False, "source_ref": source_ref, "error": f"anchor not found: {anchor}"}
        end = len(lines)
        for i in range(start + 1, len(lines)):
            m = re.match(r"^(#{1,6})\s+", lines[i])
            if m and len(m.group(1)) <= int(level or 6): end = i; break
        text = "\n".join(lines[start:end])
    text = text.strip()
    if max_chars is not None and len(text) > max_chars:
        return {"ok": False, "source_ref": source_ref, "error": f"canonical item exceeds per-item policy: {len(text)} > {max_chars}"}
    return {"ok": True, **make_context_item(
        source_type="canonical_knowledge", source_ref=source_ref, trust_class="canonical_reference",
        title=_first_heading(text, filename), content=text, verification_required=True,
    )}


def load_canonical_documents(
    manifest: dict[str, Any], routes: list[dict[str, Any]], *,
    root: Path | None = None, vault: Path | None = None,
):
    out = []
    for rank, ref in enumerate(knowledge_docs_for_routes(manifest, routes), 1):
        value = read_canonical_reference(ref["path"], root=root, vault=vault); value = dict(value)
        if value.pop("ok", False): value["retrieval_rank"] = rank
        value.update(reason=ref.get("reason"), route=ref.get("route")); out.append(value)
    return out



__all__=[name for name in globals() if not name.startswith("__")]
