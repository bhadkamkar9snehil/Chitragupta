#!/usr/bin/env python3
"""Governed deterministic retrieval for Chitragupta L2.

Reusable Solutions are never read directly from live Solution SQL here. Only
hash-approved exports under ``solutions/approved`` are eligible. Canonical Git
Knowledge, reviewed facts and explicitly-scoped GBrain search complete the
retrieval surface. Live XStudio/SQL remains current-ticket truth.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

from l2_context_envelope import make_context_item

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "Knowledge" / "manifest.json"
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


def load_manifest(path: Path | None = None) -> dict[str, Any]:
    path = path or MANIFEST_PATH
    data = json.loads(path.read_text(encoding="utf-8"))
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


def read_canonical_reference(reference: str, *, root: Path | None = None, max_chars: int = 7000) -> dict[str, Any]:
    root = root or ROOT; rel = reference.removeprefix("Knowledge/"); filename, sep, anchor = rel.partition("#")
    path = root / "Knowledge" / filename; source_ref = f"Knowledge/{rel}"
    if not path.is_file():
        return {"ok": False, "source_ref": source_ref, "error": "canonical document missing"}
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
    if len(text) > max_chars: text = text[:max_chars] + "\n[canonical excerpt truncated]"
    return {"ok": True, **make_context_item(
        source_type="canonical_knowledge", source_ref=source_ref, trust_class="canonical_reference",
        title=_first_heading(text, filename), content=text, verification_required=True,
    )}


def load_canonical_documents(manifest: dict[str, Any], routes: list[dict[str, Any]], *, root: Path | None = None):
    out = []
    for rank, ref in enumerate(knowledge_docs_for_routes(manifest, routes), 1):
        value = read_canonical_reference(ref["path"], root=root); value = dict(value)
        if value.pop("ok", False): value["retrieval_rank"] = rank
        value.update(reason=ref.get("reason"), route=ref.get("route")); out.append(value)
    return out


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


def _rank_markdown(directory: Path, query: str, *, source_type: str, source_prefix: str,
                   allowed_trust: frozenset[str], limit: int, max_chars: int) -> list[dict[str, Any]]:
    q = tokenize(query); ranked = []
    if not directory.exists() or not q: return []
    for path in sorted(directory.glob("*.md")):
        meta, body = _frontmatter(path.read_text(encoding="utf-8", errors="replace")); trust = str(meta.get("trust") or "")
        if trust not in allowed_trust: continue
        overlap = sorted(q & tokenize(body))
        if len(overlap) < MIN_MATCHED_TERMS: continue
        content = body.strip()
        if len(content) > max_chars: content = content[:max_chars] + "\n[retrieved excerpt truncated]"
        item = make_context_item(
            source_type=source_type, source_ref=f"{source_prefix}/{path.name}", trust_class=trust,
            title=str(meta.get("title") or _first_heading(content, path.stem)), content=content,
            retrieval_score=float(len(overlap)), verification_required=True, matched_terms=overlap,
        )
        if meta.get("solution_id") not in (None, ""): item["solution_id"] = meta["solution_id"]
        if meta.get("content_sha256") not in (None, ""): item["governance_content_sha256"] = meta["content_sha256"]
        for key in ("approved_by", "approved_at", "review_evidence", "reviewed_by", "promoted_at"):
            if meta.get(key) not in (None, ""): item[key] = meta[key]
        ranked.append((len(overlap), path.name, item))
    ranked.sort(key=lambda v: (-v[0], v[1])); out = []
    for rank, (_, _, item) in enumerate(ranked[:max(1, limit)], 1):
        item = dict(item); item["retrieval_rank"] = rank; out.append(item)
    return out


def promoted_facts(query: str, *, vault: Path | None = None, limit: int = MAX_RESULTS):
    return _rank_markdown((vault or _vault()) / "facts", query, source_type="promoted_fact", source_prefix="facts",
                          allowed_trust=frozenset({"reviewed_operational", "reviewed_operational_heuristic"}), limit=limit, max_chars=5000)


def governed_solutions(query: str, *, vault: Path | None = None, limit: int = MAX_RESULTS):
    return _rank_markdown((vault or _vault()) / "solutions" / "approved", query, source_type="governed_solution",
                          source_prefix="solutions/approved", allowed_trust=frozenset({"governed_reusable_solution"}),
                          limit=limit, max_chars=7000)


def gbrain_trusted_search(query: str, *, limit: int = 5) -> dict[str, Any]:
    try:
        from l2_gbrain import available, search
        if not available(): raise RuntimeError("isolated GBrain unavailable")
        result = search(query, scope="trusted", mode="hybrid", limit=limit, automatic=True)
    except Exception as exc:
        return {"ok": False, "backend": "gbrain", "source_ids": ["l2-knowledge", "l2-facts", "l2-solutions"],
                "error": f"{type(exc).__name__}: {exc}"[:800], "results": []}
    return result if result.get("ok") else {"ok": False, "backend": "gbrain", "source_ids": result.get("source_ids"),
                                             "error": result.get("error"), "results": []}


def retrieve(query_or_conn: Any, query_or_manifest: str | dict[str, Any] | None = None,
             legacy_manifest: dict[str, Any] | None = None, *, vault: Path | None = None,
             root: Path | None = None, top: int = 3, include_gbrain: bool = True) -> dict[str, Any]:
    # Old retrieve(conn, query, manifest) callers are accepted, but conn is ignored.
    if isinstance(query_or_conn, str): query, manifest = query_or_conn, (query_or_manifest if isinstance(query_or_manifest, dict) else legacy_manifest)
    else: query, manifest = str(query_or_manifest or ""), legacy_manifest
    manifest = manifest or load_manifest(); top = max(1, min(MAX_RESULTS, int(top)))
    routes = route_candidates(query, manifest, top=min(3, top)); canonical = load_canonical_documents(manifest, routes, root=root)
    facts = promoted_facts(query, vault=vault, limit=top); solutions = governed_solutions(query, vault=vault, limit=top)
    gbrain = gbrain_trusted_search(query, limit=min(10, top + 2)) if include_gbrain and query.strip() else {"ok": True, "source_ids": [], "results": []}
    errors = [str(v.get("error")) for v in canonical if v.get("error")]
    if not gbrain.get("ok"): errors.append(str(gbrain.get("error") or "GBrain retrieval failed"))
    return {
        "schema_version": 1, "query": query, "route_candidates": routes, "canonical_documents": canonical,
        "live_sql_leads": live_sql_leads_for_routes(manifest, routes), "promoted_facts": facts,
        "governed_solutions": solutions, "solutions": solutions, "gbrain_trusted": gbrain,
        "retrieval_degraded": bool(errors), "degradation_reasons": errors,
        "retrieval_policy": {"live_solution_sql_read_allowed": False, "governed_solution_export_required": True,
                             "trusted_gbrain_scope": "trusted", "automatic_gbrain_scope_is_explicit": True,
                             "live_verification_required": True},
    }


def _wsl_path(path: Path) -> str:
    value = str(path.resolve()); m = re.match(r"^([A-Za-z]):\\(.*)$", value)
    return value.replace("\\", "/") if not m else f"/mnt/{m.group(1).lower()}/{m.group(2).replace(chr(92), '/')}"


def _proxy_to_wsl(args: argparse.Namespace) -> dict[str, Any] | None:
    if os.name != "nt" or args.wsl_inner: return None
    cmd = ["wsl", "-d", os.environ.get("CHITRAGUPTA_WSL_DISTRO", "Ubuntu"), "--", "python3", _wsl_path(Path(__file__)),
           "--query", args.query, "--top", str(args.top), "--wsl-inner"]
    try: proc = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except (OSError, subprocess.TimeoutExpired): return None
    if proc.returncode != 0: return None
    try: value = json.loads(proc.stdout)
    except json.JSONDecodeError: return None
    return value if isinstance(value, dict) else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    for flag in ("server", "database", "username", "password"): ap.add_argument(f"--{flag}", default=None)
    ap.add_argument("--query", required=True); ap.add_argument("--top", type=int, default=3); ap.add_argument("--wsl-inner", action="store_true", help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    proxied = _proxy_to_wsl(args)
    if proxied is not None:
        result = proxied
    else:
        result = retrieve(args.query, top=args.top)
        if os.name == "nt" and not args.wsl_inner:
            result["retrieval_degraded"] = True
            result.setdefault("degradation_reasons", []).append("WSL retrieval proxy unavailable")
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str)); return 0


if __name__ == "__main__": raise SystemExit(main())
