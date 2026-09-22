# GBrain Knowledge World Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the existing GBrain/PostgreSQL corpus a complete, bounded, provenance-rich knowledge source that the current Hermes L2 harness automatically uses for initial ticket context.

**Architecture:** Extend `Knowledge/manifest.json`, `Model_Bench/kb_retrieval.py`, the existing investigation bundle, and the existing deployment/validation scripts. GBrain remains an internal deterministic dependency accessed with its JSON `call search` interface; Qwen never invokes GBrain directly, and the current atlas, SQL solution retrieval, typed tools, lifecycle, and publisher remain intact.

**Tech Stack:** Python 3 standard library, existing pyodbc path, GBrain 0.48.2.0 CLI/MCP operation contract, PostgreSQL 16 + pgvector, LM Studio `text-embedding-nomic-embed-text-v1.5` at 768 dimensions, JSON/JSONL, Bash, `unittest`.

**Spec:** `docs/superpowers/specs/2026-09-08-deterministic-knowledge-harness-design.md`

## Global Constraints

- Extend existing owners; do not create another vector database, registry service, planner, daemon, cron, or lifecycle authority.
- Keep WIP=1 and investigator → frozen proposal → reviewer → deterministic publish/rework unchanged.
- GBrain is retrieved by the harness, never exposed as an unrestricted model tool.
- GBrain and historical knowledge are leads; current live SQL remains ticket authority.
- Keep exact source provenance and explicit abstention in every retrieval result.
- Reject weak semantic matches below the manifest-owned acceptance threshold; GBrain
  returning a nearest neighbour does not by itself make that neighbour relevant.
- Use `gbrain call search` because it returns stable JSON and performs keyword + vector + RRF without an LLM expansion provider.
- Scope every call to source `xstudio-knowledge`; never rely on federation defaults.
- Keep output to at most 3 accepted hits, 600 characters per snippet, and 8 KB for the complete knowledge section.
- Require 100% embedding coverage for embeddable chunks before enabling the dependency gate.
- Do not upgrade GBrain while implementing this plan; validate against the installed 0.48.2.0 contract. Handle an upgrade separately.
- Never index credentials, `.env` files, untracked files, ticket-specific database rows, or per-ticket ledgers.
- Apply Ponytail: reuse existing files/functions and installed GBrain capabilities; add only the minimum tested code while retaining all safety checks.
- TDD for every behavior change; each task ends with focused tests and a commit.

---

## Current Baseline

The implementation begins from these verified facts:

```text
GBrain engine: PostgreSQL, healthy
Source: xstudio-knowledge -> current AIHelpdesk Git checkout
Pages/chunks: 142 / 601
Embedded chunks: 227 (37.8%); 374 stale/missing
Embedder: lmstudio:text-embedding-nomic-embed-text-v1.5, 768 dimensions
Search mode: balanced
Active harness KB: deterministic manifest routes + SQL solution articles
Active GBrain use by harness: none
```

`gbrain call search '<json>'` has been live-verified to return a JSON array with
`slug`, `title`, `type`, `chunk_text`, `score`, `stale`, `source_id`,
`keyword_hit`, `cosine`, and `evidence`.

## File Map and Boundaries

| File | Responsibility after this plan |
|---|---|
| `Knowledge/manifest.json` | Existing route manifest plus the single GBrain source/filter/budget contract |
| `Model_Bench/validate_knowledge_manifest.py` | Static validation of that contract and referenced paths |
| `Model_Bench/kb_retrieval.py` | Existing SQL solution retrieval plus bounded GBrain status/search adapter and merged result contract |
| `Model_Bench/test_kb_retrieval.py` | Pure unit tests for routing, SQL articles, GBrain parsing/filtering, failure and merge behavior |
| `Knowledge/eval/gbrain_retrieval_cases.jsonl` | Versioned positive, cross-domain, exact-identifier, and abstention cases |
| `Model_Bench/validate_gbrain_knowledge.py` | Read-only live readiness and retrieval evaluation command |
| `Model_Bench/test_validate_gbrain_knowledge.py` | Pure tests for evaluation scoring and exit conditions |
| `Model_Bench/l2_pipeline_runtime.py` | Existing bundle consumes the merged result and dependency probe blocks only new claims when GBrain is unready |
| `Model_Bench/test_l2_pipeline_runtime.py` | Bundle and dependency-gate regressions |
| `Model_Bench/sync_gbrain_knowledge.sh` | One idempotent maintenance entrypoint using the existing registered source and embedder |
| `Model_Bench/deploy_l2_pipeline_runtime.sh` | Calls maintenance/readiness before copying or restarting runtime artifacts |
| `Model_Bench/validate_l2_pipeline_local.sh` | Runs pure tests plus live GBrain readiness/evaluation |
| `Knowledge/VALIDATION.md` | Exact operator commands and expected gates |
| `Knowledge/PENDING_POINTS.md` | Updates KB-001 status/evidence; remains a concise parking lot |

No SQL source or stored procedure changes are part of this plan. GBrain knowledge
retrieval does not need SQL schema mutation.

---

### Task 1: Put the GBrain Contract in the Existing Knowledge Manifest

**Files:**
- Modify: `Knowledge/manifest.json`
- Modify: `Model_Bench/validate_knowledge_manifest.py`
- Modify: `Model_Bench/test_kb_retrieval.py`

**Interfaces:**
- Consumes: current `Knowledge/manifest.json` route and identifier definitions.
- Produces: `manifest["gbrain"]`, validated before runtime use.

- [ ] **Step 1: Write failing manifest-contract tests**

Add a `GBrainManifestTests` class to `Model_Bench/test_kb_retrieval.py`:

```python
class GBrainManifestTests(unittest.TestCase):
    def test_production_manifest_has_bounded_source_scoped_gbrain_contract(self):
        manifest = kb.load_manifest()
        cfg = manifest["gbrain"]
        self.assertEqual(cfg["source_id"], "xstudio-knowledge")
        self.assertEqual(cfg["candidate_limit"], 12)
        self.assertEqual(cfg["return_limit"], 3)
        self.assertEqual(cfg["snippet_chars"], 600)
        self.assertEqual(cfg["min_retrieval_score"], 0.70)
        self.assertEqual(cfg["min_embedding_coverage_pct"], 100.0)
        self.assertIn("knowledge/", cfg["allowed_slug_prefixes"])
        self.assertIn("deploy/skills/xstudio/", cfg["allowed_slug_prefixes"])
        self.assertIn("agent_comms/", cfg["excluded_slug_prefixes"])

    def test_gbrain_contract_never_allows_untracked_or_secret_surfaces(self):
        cfg = kb.load_manifest()["gbrain"]
        denied = set(cfg["excluded_slug_prefixes"])
        self.assertTrue({"agent_comms/", "plans/", "attachments/", ".env"} <= denied)
```

- [ ] **Step 2: Run the focused test and verify RED**

Run:

```bash
python3 -m unittest -v \
  Model_Bench.test_kb_retrieval.GBrainManifestTests
```

Expected: errors because `manifest["gbrain"]` does not exist.

- [ ] **Step 3: Add the minimum manifest configuration**

Add this top-level object to `Knowledge/manifest.json`:

```json
"gbrain": {
  "source_id": "xstudio-knowledge",
  "allowed_slug_prefixes": [
    "knowledge/",
    "deploy/skills/xstudio/"
  ],
  "excluded_slug_prefixes": [
    "agent_comms/",
    "plans/",
    "attachments/",
    "knowledge/eval/",
    ".env"
  ],
  "excluded_slugs": [
    "knowledge/atlas/xstudio_xbatch-schema-atlas",
    "knowledge/atlas/xstudio_xbatch-procedure-atlas",
    "knowledge/atlas/xstudio_helpdesk-schema-atlas",
    "knowledge/atlas/xstudio_helpdesk-procedure-atlas"
  ],
  "candidate_limit": 12,
  "return_limit": 3,
  "snippet_chars": 600,
  "timeout_seconds": 20,
  "min_retrieval_score": 0.70,
  "min_embedding_coverage_pct": 100.0
}
```

The four excluded slugs are the current DB-only monolithic atlas pages reported by
GBrain doctor. The checked-in per-letter atlas pages supersede them. This task only
excludes them from L2 retrieval; it does not delete GBrain data.

- [ ] **Step 4: Extend static validation**

In `Model_Bench/validate_knowledge_manifest.py`, add one focused validator:

```python
def _validate_gbrain_contract(manifest: dict, errors: list[str]) -> None:
    cfg = manifest.get("gbrain")
    if not isinstance(cfg, dict):
        errors.append("manifest gbrain contract is missing")
        return
    required = {
        "source_id", "allowed_slug_prefixes", "excluded_slug_prefixes",
        "excluded_slugs", "candidate_limit", "return_limit",
        "snippet_chars", "timeout_seconds", "min_retrieval_score",
        "min_embedding_coverage_pct",
    }
    missing = sorted(required - set(cfg))
    if missing:
        errors.append("manifest gbrain contract missing: " + ", ".join(missing))
    if cfg.get("source_id") != "xstudio-knowledge":
        errors.append("gbrain source_id must be xstudio-knowledge")
    if not (1 <= int(cfg.get("return_limit", 0)) <= 3):
        errors.append("gbrain return_limit must be 1..3")
    if int(cfg.get("candidate_limit", 0)) < int(cfg.get("return_limit", 0)):
        errors.append("gbrain candidate_limit must cover return_limit")
    if not (0.0 <= float(cfg.get("min_retrieval_score", -1)) <= 1.0):
        errors.append("gbrain min_retrieval_score must be 0..1")
    if float(cfg.get("min_embedding_coverage_pct", 0)) != 100.0:
        errors.append("gbrain embedding gate must be 100 percent")
```

Call it immediately after parsing the manifest. Do not add a new validator module.

- [ ] **Step 5: Run focused and static validation tests**

Run:

```bash
python3 -m unittest -v Model_Bench.test_kb_retrieval.GBrainManifestTests
python3 Model_Bench/validate_knowledge_manifest.py
```

Expected: both pass; static output still reports the current route/skill counts.

- [ ] **Step 6: Commit Task 1**

```bash
git add Knowledge/manifest.json \
  Model_Bench/validate_knowledge_manifest.py \
  Model_Bench/test_kb_retrieval.py
git commit -m "feat(kb): define bounded gbrain retrieval contract"
```

---

### Task 2: Add a Bounded GBrain Adapter to the Existing Retriever

**Files:**
- Modify: `Model_Bench/kb_retrieval.py`
- Modify: `Model_Bench/test_kb_retrieval.py`

**Interfaces:**
- Consumes: `manifest["gbrain"]`, installed GBrain binary, and `GBRAIN_HOME`.
- Produces: `get_gbrain_status(config, runner=None) -> dict` and
  `retrieve_gbrain(query, config, runner=None) -> dict`.

- [ ] **Step 1: Write failing status-parser tests**

Add reusable fake-result helpers and tests:

```python
class _Result:
    def __init__(self, stdout="", stderr="", returncode=0):
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


class GBrainAdapterTests(unittest.TestCase):
    def setUp(self):
        self.cfg = {
            "source_id": "xstudio-knowledge",
            "allowed_slug_prefixes": ["knowledge/", "deploy/skills/xstudio/"],
            "excluded_slug_prefixes": ["agent_comms/", "knowledge/eval/"],
            "excluded_slugs": ["knowledge/atlas/old"],
            "candidate_limit": 12,
            "return_limit": 3,
            "snippet_chars": 600,
            "timeout_seconds": 20,
            "min_retrieval_score": 0.70,
            "min_embedding_coverage_pct": 100.0,
        }

    def test_status_selects_exact_source_and_requires_full_coverage(self):
        payload = {"sources": [{
            "source_id": "xstudio-knowledge", "total_pages": 142,
            "total_chunks": 601, "embedded_chunks": 601,
            "embed_coverage_pct": 100, "failed_jobs_24h": 0,
            "queue_depth": 0,
        }]}
        status = kb.get_gbrain_status(
            self.cfg, runner=lambda *a, **k: _Result(json.dumps(payload)))
        self.assertEqual(status["status"], "READY")
        self.assertEqual(status["source_id"], "xstudio-knowledge")

    def test_status_reports_incomplete_embeddings(self):
        payload = {"sources": [{
            "source_id": "xstudio-knowledge", "total_pages": 142,
            "total_chunks": 601, "embedded_chunks": 227,
            "embed_coverage_pct": 37.8, "failed_jobs_24h": 0,
            "queue_depth": 0,
        }]}
        status = kb.get_gbrain_status(
            self.cfg, runner=lambda *a, **k: _Result(json.dumps(payload)))
        self.assertEqual(status["status"], "DEGRADED")
        self.assertIn("embedding coverage", status["reason"])
```

- [ ] **Step 2: Run status tests and verify RED**

Run:

```bash
python3 -m unittest -v \
  Model_Bench.test_kb_retrieval.GBrainAdapterTests.test_status_selects_exact_source_and_requires_full_coverage \
  Model_Bench.test_kb_retrieval.GBrainAdapterTests.test_status_reports_incomplete_embeddings
```

Expected: errors because `get_gbrain_status` does not exist.

- [ ] **Step 3: Implement status using the installed JSON contract**

Add to `Model_Bench/kb_retrieval.py`:

```python
GBRAIN_BIN = os.environ.get("GBRAIN_BIN", "/home/snehil/.bun/bin/gbrain")
GBRAIN_HOME = os.environ.get("GBRAIN_HOME", "/home/snehil/.hermes/xstudio-gbrain")


def _run_gbrain(argv: list[str], *, timeout: int, runner=None):
    run = runner or subprocess.run
    env = os.environ.copy()
    env["GBRAIN_HOME"] = GBRAIN_HOME
    return run(
        [GBRAIN_BIN, *argv], capture_output=True, text=True,
        timeout=timeout, env=env,
    )


def get_gbrain_status(config: dict, runner=None) -> dict:
    try:
        result = _run_gbrain(
            ["sources", "status", "--json"],
            timeout=int(config["timeout_seconds"]), runner=runner,
        )
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or f"exit {result.returncode}")
        payload = json.loads(result.stdout)
        source = next(
            row for row in payload.get("sources", [])
            if row.get("source_id") == config["source_id"]
        )
        coverage = float(source.get("embed_coverage_pct") or 0)
        minimum = float(config["min_embedding_coverage_pct"])
        ready = (
            coverage >= minimum
            and int(source.get("failed_jobs_24h") or 0) == 0
            and int(source.get("queue_depth") or 0) == 0
        )
        return {
            "status": "READY" if ready else "DEGRADED",
            "source_id": config["source_id"],
            "pages": int(source.get("total_pages") or 0),
            "chunks": int(source.get("total_chunks") or 0),
            "embedded_chunks": int(source.get("embedded_chunks") or 0),
            "embedding_coverage_pct": coverage,
            "reason": None if ready else (
                f"embedding coverage {coverage:g}% is below {minimum:g}% "
                f"or GBrain jobs are not drained"
            ),
        }
    except (OSError, subprocess.TimeoutExpired, RuntimeError,
            StopIteration, ValueError, json.JSONDecodeError) as exc:
        return {
            "status": "UNAVAILABLE", "source_id": config.get("source_id"),
            "reason": f"{type(exc).__name__}: {exc}",
        }
```

Do not parse human-readable `gbrain stats` or search output.

- [ ] **Step 4: Write failing search/filter tests**

Add tests that pass a JSON array from `gbrain call search`:

```python
    def test_search_is_source_scoped_bounded_and_filters_non_authority(self):
        rows = [
            {"slug": "agent_comms/old", "source_id": "xstudio-knowledge",
             "title": "Old handoff", "chunk_text": "stale", "score": .99,
             "stale": False, "keyword_hit": True, "evidence": "keyword_exact"},
            {"slug": "knowledge/xbatch-investigation-surfaces",
             "source_id": "xstudio-knowledge", "title": "Xbatch surfaces",
             "chunk_text": "SAP posting and material document surfaces",
             "score": .91, "stale": False, "keyword_hit": True,
             "evidence": "keyword_exact"},
            {"slug": "knowledge/eval/private-case",
             "source_id": "xstudio-knowledge", "title": "Fixture",
             "chunk_text": "fixture", "score": .90, "stale": False,
             "keyword_hit": True, "evidence": "keyword_exact"},
        ]
        calls = []
        def runner(cmd, **kwargs):
            calls.append(cmd)
            return _Result(json.dumps(rows))
        result = kb.retrieve_gbrain("SAP posting pending", self.cfg, runner=runner)
        request = json.loads(calls[0][3])
        self.assertEqual(calls[0][1:3], ["call", "search"])
        self.assertEqual(request["source_id"], "xstudio-knowledge")
        self.assertEqual(request["limit"], 12)
        self.assertEqual(request["snippet_chars"], 600)
        self.assertEqual([h["slug"] for h in result["hits"]],
                         ["knowledge/xbatch-investigation-surfaces"])

    def test_search_failure_returns_explicit_abstention(self):
        result = kb.retrieve_gbrain(
            "SAP posting", self.cfg,
            runner=lambda *a, **k: _Result(stderr="connection closed", returncode=1),
        )
        self.assertEqual(result["status"], "UNAVAILABLE")
        self.assertTrue(result["abstained"])
        self.assertEqual(result["hits"], [])

    def test_weak_nearest_neighbour_abstains(self):
        rows = [{
            "slug": "knowledge/weak-neighbour",
            "source_id": "xstudio-knowledge",
            "title": "Weak neighbour", "chunk_text": "unrelated material",
            "score": .42, "stale": False, "keyword_hit": False,
            "evidence": "semantic",
        }]
        result = kb.retrieve_gbrain(
            "employee annual leave reimbursement policy", self.cfg,
            runner=lambda *a, **k: _Result(json.dumps(rows)),
        )
        self.assertTrue(result["abstained"])
        self.assertEqual(result["hits"], [])
```

- [ ] **Step 5: Run search tests and verify RED**

Run:

```bash
python3 -m unittest -v Model_Bench.test_kb_retrieval.GBrainAdapterTests
```

Expected: errors because `retrieve_gbrain` does not exist.

- [ ] **Step 6: Implement bounded retrieval and stable hit projection**

Add these functions to `Model_Bench/kb_retrieval.py`:

```python
def _slug_allowed(slug: str, config: dict) -> bool:
    value = slug.casefold()
    allowed = any(value.startswith(p.casefold())
                  for p in config["allowed_slug_prefixes"])
    excluded = any(value.startswith(p.casefold())
                   for p in config["excluded_slug_prefixes"])
    denied_exact = value in {s.casefold() for s in config["excluded_slugs"]}
    return allowed and not excluded and not denied_exact


def retrieve_gbrain(query: str, config: dict, runner=None) -> dict:
    request = {
        "query": query,
        "limit": int(config["candidate_limit"]),
        "source_id": config["source_id"],
        "snippet_chars": int(config["snippet_chars"]),
        "mode": "balanced",
        "salience": "off",
        "recency": "off",
    }
    try:
        result = _run_gbrain(
            ["call", "search", json.dumps(request, separators=(",", ":"))],
            timeout=int(config["timeout_seconds"]), runner=runner,
        )
        if result.returncode:
            raise RuntimeError(result.stderr.strip() or f"exit {result.returncode}")
        rows = json.loads(result.stdout)
        if not isinstance(rows, list):
            raise ValueError("gbrain search returned a non-list")
        hits = []
        for row in rows:
            slug = str(row.get("slug") or "")
            if row.get("source_id") != config["source_id"] or not _slug_allowed(slug, config):
                continue
            score = float(row.get("score") or 0)
            if score < float(config["min_retrieval_score"]):
                continue
            hits.append({
                "kb_id": f"gbrain:{config['source_id']}:{slug}",
                "source_type": "gbrain_page",
                "source_ref": f"{config['source_id']}:{slug}",
                "slug": slug,
                "title": row.get("title"),
                "excerpt": row.get("chunk_text"),
                "retrieval_score": round(score, 6),
                "keyword_hit": bool(row.get("keyword_hit")),
                "evidence": row.get("evidence"),
                "verification_required": True,
            })
            if len(hits) >= int(config["return_limit"]):
                break
        return {
            "status": "READY", "source_id": config["source_id"],
            "hits": hits, "abstained": not hits,
            "abstention_reason": None if hits else
                "GBrain returned no allowed knowledge hit.",
        }
    except (OSError, subprocess.TimeoutExpired, RuntimeError,
            ValueError, TypeError, json.JSONDecodeError) as exc:
        return {
            "status": "UNAVAILABLE", "source_id": config.get("source_id"),
            "hits": [], "abstained": True,
            "abstention_reason": f"GBrain retrieval failed: {type(exc).__name__}: {exc}",
        }
```

Import `subprocess`. Keep all transport inside this existing module.

- [ ] **Step 7: Run all KB unit tests**

Run:

```bash
python3 -m unittest -v Model_Bench.test_kb_retrieval
python3 -m py_compile Model_Bench/kb_retrieval.py
```

Expected: all tests pass.

- [ ] **Step 8: Commit Task 2**

```bash
git add Model_Bench/kb_retrieval.py Model_Bench/test_kb_retrieval.py
git commit -m "feat(kb): add bounded gbrain search adapter"
```

---

### Task 3: Merge GBrain with Current Route and Solution Retrieval

**Files:**
- Modify: `Model_Bench/kb_retrieval.py`
- Modify: `Model_Bench/test_kb_retrieval.py`

**Interfaces:**
- Consumes: `retrieve_gbrain(query, manifest["gbrain"])`, current route candidates,
  and current SQL solution ranking.
- Produces: current retrieval response plus a separate `gbrain` object; no knowledge
  source is silently merged with live evidence.

- [ ] **Step 1: Write failing merge tests**

```python
class CombinedRetrievalTests(unittest.TestCase):
    def test_retrieve_keeps_routes_solutions_and_gbrain_separate(self):
        articles = [{
            "ID": "C", "Title": "Equipment delay missing",
            "ProblemSummary": "equipment mapping missing",
            "RootCause": "mapping gap", "ResolutionSteps": "verify mapping",
            "Route": "performance", "Tags": "delay,equipment,mapping",
            "UsageCount": 1, "CreatedOn": None, "ModifiedOn": None,
        }]
        conn = type("Conn", (), {})()
        gbrain_result = {
            "status": "READY", "source_id": "xstudio-knowledge",
            "hits": [{"kb_id": "gbrain:x:y"}], "abstained": False,
            "abstention_reason": None,
        }
        with patch.object(kb, "fetch_articles", return_value=articles), \
             patch.object(kb, "retrieve_gbrain", return_value=gbrain_result):
            result = kb.retrieve(conn, "equipment delay mapping missing", MANIFEST)
        self.assertIn("route_candidates", result)
        self.assertIn("solutions", result)
        self.assertEqual(result["gbrain"], gbrain_result)
        self.assertTrue(result["retrieval_policy"]["live_verification_required"])

    def test_gbrain_failure_does_not_remove_deterministic_routes(self):
        unavailable = {
            "status": "UNAVAILABLE", "hits": [], "abstained": True,
            "abstention_reason": "connection closed",
        }
        with patch.object(kb, "fetch_articles", return_value=[]), \
             patch.object(kb, "retrieve_gbrain", return_value=unavailable):
            result = kb.retrieve(object(), "HeatNo 1604015", MANIFEST)
        self.assertEqual(result["route_candidates"][0]["route"], "heat_execution")
        self.assertEqual(result["gbrain"]["status"], "UNAVAILABLE")
```

Add `gbrain` configuration to the in-test `MANIFEST` fixture.

- [ ] **Step 2: Run merge tests and verify RED**

Run:

```bash
python3 -m unittest -v Model_Bench.test_kb_retrieval.CombinedRetrievalTests
```

Expected: fail because `retrieve()` does not include `gbrain`.

- [ ] **Step 3: Call GBrain once inside current retrieval**

In `retrieve()`, after deterministic routes and SQL articles are computed:

```python
gbrain = retrieve_gbrain(query, manifest["gbrain"])
```

Return it as its own object:

```python
return {
    "query": query,
    "route_candidates": routes,
    "knowledge_documents": knowledge_docs_for_routes(manifest, routes),
    "solutions": ranked,
    "gbrain": gbrain,
    "abstained": not ranked and gbrain.get("abstained", True),
    "abstention_reason": (
        None if ranked or not gbrain.get("abstained", True)
        else "No approved solution or allowed GBrain page met the retrieval gate."
    ),
    "retrieval_policy": {
        "route_only_match_allowed": False,
        "min_score": min_score,
        "min_matched_terms": min_matched_terms,
        "top": top,
        "gbrain_max_hits": int(manifest["gbrain"]["return_limit"]),
        "provenance_required": True,
        "live_verification_required": True,
    },
}
```

Do not combine `solutions` and GBrain `hits` into one score space.

- [ ] **Step 4: Add a read-only GBrain health CLI mode**

Update `main()` arguments:

```python
group = ap.add_mutually_exclusive_group(required=True)
group.add_argument("--query", help="Ticket text/problem description")
group.add_argument("--check-gbrain", action="store_true")
```

Before opening SQL:

```python
manifest = load_manifest()
if args.check_gbrain:
    status = get_gbrain_status(manifest["gbrain"])
    print(json.dumps(status, indent=2))
    return 0 if status["status"] == "READY" else 1
```

This preserves the current query CLI and provides one reusable readiness boundary.

- [ ] **Step 5: Run all retriever tests and compilation**

```bash
python3 -m unittest -v Model_Bench.test_kb_retrieval
python3 -m py_compile Model_Bench/kb_retrieval.py
```

Expected: pass.

- [ ] **Step 6: Commit Task 3**

```bash
git add Model_Bench/kb_retrieval.py Model_Bench/test_kb_retrieval.py
git commit -m "feat(kb): combine gbrain with current retrieval"
```

---

### Task 4: Add a Real Retrieval Evaluation Gate

**Files:**
- Create: `Knowledge/eval/gbrain_retrieval_cases.jsonl`
- Create: `Model_Bench/validate_gbrain_knowledge.py`
- Create: `Model_Bench/test_validate_gbrain_knowledge.py`

**Interfaces:**
- Consumes: `get_gbrain_status()` and `retrieve_gbrain()`.
- Produces: deterministic JSON summary and process exit code for deployment/local gates.

- [ ] **Step 1: Create the golden evaluation cases**

Create JSONL with these exact initial cases:

```jsonl
{"id":"sap-posting","query":"SAP production posting pending without material document","expect_any_prefix":["knowledge/xbatch-investigation-surfaces","knowledge/view_docs/xstudio_xbatch.xstudio_list_sap_posting"],"forbid_prefix":["agent_comms/","plans/"]}
{"id":"api-usage-decision","query":"UsageDecision API response error for inspection lot","expect_any_prefix":["knowledge/xbatch-investigation-surfaces","knowledge/view_docs/xstudio_xbatch.xstudio_list_xmes_sap_api_usagedecision"],"forbid_prefix":["agent_comms/","plans/"]}
{"id":"work-order-campaign","query":"work order missing from campaign plan","expect_any_prefix":["deploy/skills/xstudio/xstudio-quality-delay-workorder/skill","knowledge/view_docs/xstudio_xbatch.xstudio_xmes_campaign_plan_work_order_vw"],"forbid_prefix":["agent_comms/","plans/"]}
{"id":"heat-execution","query":"heat missing LRF CCM status and billet count","expect_any_prefix":["knowledge/sohar-sms-event-workflows","knowledge/xbatch-investigation-surfaces","deploy/skills/xstudio/xstudio-sohar-heat-execution/skill"],"forbid_prefix":["agent_comms/","plans/"]}
{"id":"billet-genealogy","query":"billet genealogy strand sequence for heat","expect_any_prefix":["knowledge/view_docs/xstudio_xbatch.xstudio_list_xmes_ccm_billet_genealogy","knowledge/xbatch-investigation-surfaces"],"forbid_prefix":["agent_comms/","plans/"]}
{"id":"quality-spectro","query":"spectro chemistry result missing for inspection lot","expect_any_prefix":["knowledge/view_docs/xstudio_xbatch.xstudio_list_quality_spectro_result","knowledge/xbatch-investigation-surfaces","deploy/skills/xstudio/xstudio-quality-delay-workorder/skill"],"forbid_prefix":["agent_comms/","plans/"]}
{"id":"delay-equipment","query":"equipment delay missing from delay analysis OEE","expect_any_prefix":["knowledge/view_docs/xstudio_xbatch.xbatch_delay_analysis_vw","knowledge/xbatch-investigation-surfaces","deploy/skills/xstudio/xstudio-quality-delay-workorder/skill"],"forbid_prefix":["agent_comms/","plans/"]}
{"id":"helpdesk-runtime","query":"Hermes L2 SQL action audit and ticket response","expect_any_prefix":["knowledge/hermes-runtime-database-design","knowledge/hermes-sp-catalog"],"forbid_prefix":["agent_comms/","plans/"]}
{"id":"irrelevant-hr","query":"employee annual leave reimbursement policy","expect_abstention":true,"forbid_prefix":["agent_comms/","plans/"]}
{"id":"irrelevant-consumer","query":"best wireless headphones for running","expect_abstention":true,"forbid_prefix":["agent_comms/","plans/"]}
```

- [ ] **Step 2: Write failing evaluator unit tests**

In `Model_Bench/test_validate_gbrain_knowledge.py`:

```python
import unittest
from Model_Bench.validate_gbrain_knowledge import evaluate_case


class GBrainEvaluationTests(unittest.TestCase):
    def test_positive_case_accepts_any_expected_prefix(self):
        case = {"expect_any_prefix": ["knowledge/quality/"],
                "forbid_prefix": ["agent_comms/"]}
        result = {"hits": [{"slug": "knowledge/quality/spectro"}]}
        self.assertEqual(evaluate_case(case, result), [])

    def test_negative_case_requires_abstention(self):
        case = {"expect_abstention": True, "forbid_prefix": ["agent_comms/"]}
        errors = evaluate_case(case, {"hits": [{"slug": "knowledge/random"}],
                                      "abstained": False})
        self.assertIn("expected abstention", errors)

    def test_forbidden_prefix_always_fails(self):
        case = {"expect_any_prefix": ["knowledge/"],
                "forbid_prefix": ["agent_comms/"]}
        errors = evaluate_case(case, {"hits": [{"slug": "agent_comms/old"}]})
        self.assertTrue(any("forbidden" in error for error in errors))
```

- [ ] **Step 3: Run evaluator tests and verify RED**

```bash
python3 -m unittest -v Model_Bench.test_validate_gbrain_knowledge
```

Expected: import failure because the evaluator does not exist.

- [ ] **Step 4: Implement the focused live validator**

`Model_Bench/validate_gbrain_knowledge.py` must:

```python
def evaluate_case(case: dict, result: dict) -> list[str]:
    slugs = [str(hit.get("slug") or "") for hit in result.get("hits", [])]
    errors = []
    if case.get("expect_abstention") and not result.get("abstained"):
        errors.append("expected abstention")
    expected = case.get("expect_any_prefix") or []
    if expected and not any(any(slug.startswith(p) for p in expected) for slug in slugs):
        errors.append("no expected knowledge prefix retrieved")
    for prefix in case.get("forbid_prefix") or []:
        if any(slug.startswith(prefix) for slug in slugs):
            errors.append(f"forbidden prefix retrieved: {prefix}")
    return errors
```

Its `main()` loads the production manifest and JSONL, calls
`get_gbrain_status()` once, refuses evaluation unless status is `READY`, calls
`retrieve_gbrain()` once per case, and prints:

```json
{
  "status": "PASS",
  "source_id": "xstudio-knowledge",
  "embedding_coverage_pct": 100.0,
  "cases": 10,
  "passed": 10,
  "failed": 0,
  "failures": []
}
```

Exit `0` only when readiness and every case pass; otherwise exit `1`. Do not add
LLM judging, fuzzy assertions, network search, or automatic fixture rewrites.

- [ ] **Step 5: Run evaluator unit tests and compile**

```bash
python3 -m unittest -v Model_Bench.test_validate_gbrain_knowledge
python3 -m py_compile Model_Bench/validate_gbrain_knowledge.py
```

Expected: pass.

- [ ] **Step 6: Commit Task 4**

```bash
git add Knowledge/eval/gbrain_retrieval_cases.jsonl \
  Model_Bench/validate_gbrain_knowledge.py \
  Model_Bench/test_validate_gbrain_knowledge.py
git commit -m "test(kb): add live gbrain retrieval gate"
```

---

### Task 5: Put GBrain Results into the Existing Investigation Bundle

**Files:**
- Modify: `Model_Bench/l2_pipeline_runtime.py`
- Modify: `Model_Bench/test_l2_pipeline_runtime.py`

**Interfaces:**
- Consumes: existing `_run_kb_retrieval()` response with separate `solutions`,
  `route_candidates`, and `gbrain`.
- Produces: a bounded `kb.gbrain` section in the current card body.

- [ ] **Step 1: Write failing bundle tests**

Add a test around `_investigation_bundle()` using mocked orchestrator and retriever:

```python
def test_investigation_bundle_contains_bounded_gbrain_provenance(self):
    args = mod.default_args()
    ticket = {"ID": "ticket-1", "BriefDetails": "SAP posting pending"}
    kb_result = {
        "solutions": [],
        "route_candidates": [{"route": "sap_posting", "score": 10}],
        "gbrain": {
            "status": "READY", "source_id": "xstudio-knowledge",
            "hits": [{
                "kb_id": "gbrain:xstudio-knowledge:knowledge/sap",
                "source_ref": "xstudio-knowledge:knowledge/sap",
                "title": "SAP posting", "excerpt": "bounded evidence lead",
                "retrieval_score": .9, "verification_required": True,
            }],
            "abstained": False, "abstention_reason": None,
        },
    }
    with patch.object(mod, "run_orchestrator", return_value={"ticket": {"ticket": ticket}}), \
         patch.object(mod, "_run_kb_retrieval", return_value=kb_result):
        rendered = mod._investigation_bundle(args, "ticket-1", ticket)
    self.assertIn('"source_id": "xstudio-knowledge"', rendered)
    self.assertIn('"source_ref": "xstudio-knowledge:knowledge/sap"', rendered)
    self.assertIn('"verification_required": true', rendered)


def test_investigation_bundle_preserves_explicit_gbrain_failure(self):
    args = mod.default_args()
    ticket = {"ID": "ticket-1", "BriefDetails": "unknown symptom"}
    kb_result = {
        "solutions": [], "route_candidates": [],
        "gbrain": {"status": "UNAVAILABLE", "hits": [], "abstained": True,
                   "abstention_reason": "GBrain retrieval failed: timeout"},
    }
    with patch.object(mod, "run_orchestrator", return_value={"ticket": {"ticket": ticket}}), \
         patch.object(mod, "_run_kb_retrieval", return_value=kb_result):
        rendered = mod._investigation_bundle(args, "ticket-1", ticket)
    self.assertIn("GBrain retrieval failed: timeout", rendered)
```

- [ ] **Step 2: Run bundle tests and verify RED**

Run the two exact tests by their final class-qualified names after placing them in
`PipelineContractTests`:

```bash
python3 -m unittest -v \
  Model_Bench.test_l2_pipeline_runtime.PipelineContractTests.test_investigation_bundle_contains_bounded_gbrain_provenance \
  Model_Bench.test_l2_pipeline_runtime.PipelineContractTests.test_investigation_bundle_preserves_explicit_gbrain_failure
```

Expected: fail because the compact bundle drops `gbrain`.

- [ ] **Step 3: Extend only the existing compact KB object**

In `_investigation_bundle()`, add:

```python
"gbrain": {
    "status": (kb.get("gbrain") or {}).get("status"),
    "source_id": (kb.get("gbrain") or {}).get("source_id"),
    "hits": [
        {key: hit.get(key) for key in (
            "kb_id", "source_ref", "title", "excerpt",
            "retrieval_score", "verification_required",
        ) if hit.get(key) is not None}
        for hit in list((kb.get("gbrain") or {}).get("hits") or [])[:3]
    ],
    "abstained": (kb.get("gbrain") or {}).get("abstained"),
    "abstention_reason": (kb.get("gbrain") or {}).get("abstention_reason"),
},
```

Raise the existing complete-bundle cap from 5,000 to 8,000 characters. Keep every
individual excerpt capped by GBrain at 600 characters. Do not add another card
section or a model-callable GBrain tool.

- [ ] **Step 4: Add explicit worker guidance in the existing bundle preamble**

Replace the current lead warning with:

```text
KB/GBrain hits, prior findings, relationships, and suggested tables are leads,
not ticket proof. Use source_ref for provenance. Material current claims still
require current audited SQL evidence.
```

- [ ] **Step 5: Run lifecycle and KB tests**

```bash
python3 -m unittest -v \
  Model_Bench.test_l2_pipeline_runtime \
  Model_Bench.test_kb_retrieval
```

Expected: pass with existing lifecycle behavior unchanged.

- [ ] **Step 6: Commit Task 5**

```bash
git add Model_Bench/l2_pipeline_runtime.py \
  Model_Bench/test_l2_pipeline_runtime.py
git commit -m "feat(l2): inject bounded gbrain context"
```

---

### Task 6: Add GBrain Readiness to the Existing Claim Gate

**Files:**
- Modify: `Model_Bench/l2_pipeline_runtime.py`
- Modify: `Model_Bench/test_l2_pipeline_runtime.py`

**Interfaces:**
- Consumes: `kb_retrieval.py --check-gbrain`.
- Produces: new-claim dependency failure when the knowledge world is incomplete;
  reconciliation of existing work remains unaffected.

- [ ] **Step 1: Write failing dependency-gate tests**

```python
def test_gbrain_dependency_failure_pauses_new_claims(self):
    args = mod.default_args()
    calls = []
    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        if "--check-gbrain" in cmd:
            return type("R", (), {"returncode": 1, "stdout": "{}",
                                   "stderr": "embedding coverage 37.8%"})()
        return type("R", (), {"returncode": 0, "stdout": "{}", "stderr": ""})()
    with patch.object(mod.subprocess, "run", side_effect=fake_run):
        with self.assertRaisesRegex(RuntimeError, "GBrain knowledge is not ready"):
            mod.check_gbrain_dependency(args)


def test_reconcile_runs_before_gbrain_claim_gate(self):
    args = mod.default_args()
    order = []
    with patch.object(mod, "reconcile", side_effect=lambda *a, **k: order.append("reconcile") or {}), \
         patch.object(mod, "query_active_runs", return_value=[]), \
         patch.object(mod, "check_worker_dependencies", side_effect=lambda: order.append("worker")), \
         patch.object(mod, "check_gbrain_dependency", side_effect=lambda a: order.append("gbrain") or (_ for _ in ()).throw(RuntimeError("not ready"))):
        with self.assertRaisesRegex(RuntimeError, "not ready"):
            mod.scout(args)
    self.assertEqual(order[:3], ["reconcile", "worker", "gbrain"])
```

- [ ] **Step 2: Run focused tests and verify RED**

```bash
python3 -m unittest -v \
  Model_Bench.test_l2_pipeline_runtime.PipelineContractTests.test_gbrain_dependency_failure_pauses_new_claims \
  Model_Bench.test_l2_pipeline_runtime.PipelineContractTests.test_reconcile_runs_before_gbrain_claim_gate
```

Expected: fail because `check_gbrain_dependency` does not exist.

- [ ] **Step 3: Implement one dependency call**

Add:

```python
def check_gbrain_dependency(args: argparse.Namespace) -> None:
    result = subprocess.run(
        [_orch_python(), _kb_retriever_path(), "--check-gbrain"],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()[:300]
        raise RuntimeError(
            "WORKER_DEPENDENCY_UNAVAILABLE: GBrain knowledge is not ready: " + detail
        )
```

Call it in `scout()` after reconciliation, workflow/WIP checks, and
`check_worker_dependencies()`, but before `--poll`. This means:

```text
existing active work -> always reconcile
no active work + GBrain unready -> claim nothing new
GBrain fails after a run was claimed -> bundle records explicit UNAVAILABLE and
                                       deterministic routes remain usable
```

Do not put GBrain into the event-triggered reconciler.

- [ ] **Step 4: Run the lifecycle suite**

```bash
python3 -m unittest -v Model_Bench.test_l2_pipeline_runtime
```

Expected: pass; WIP and lifecycle ordering tests remain unchanged.

- [ ] **Step 5: Commit Task 6**

```bash
git add Model_Bench/l2_pipeline_runtime.py \
  Model_Bench/test_l2_pipeline_runtime.py
git commit -m "fix(l2): gate new claims on gbrain readiness"
```

---

### Task 7: Make GBrain Sync, Embedding, and Evaluation Reproducible

**Files:**
- Create: `Model_Bench/sync_gbrain_knowledge.sh`
- Modify: `Model_Bench/deploy_l2_pipeline_runtime.sh`
- Modify: `Model_Bench/validate_l2_pipeline_local.sh`
- Modify: `Knowledge/VALIDATION.md`

**Interfaces:**
- Consumes: registered `xstudio-knowledge` source, committed Git files, LM Studio
  embedding endpoint, and Task 4 validator.
- Produces: one idempotent maintenance command and fail-closed deployment gate.

- [ ] **Step 1: Create the maintenance script**

Use this exact shape:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GBRAIN_BIN="${GBRAIN_BIN:-/home/snehil/.bun/bin/gbrain}"
export GBRAIN_HOME="${GBRAIN_HOME:-/home/snehil/.hermes/xstudio-gbrain}"

test -x "$GBRAIN_BIN" || {
  echo "FATAL: GBrain binary not found: $GBRAIN_BIN" >&2
  exit 1
}

"$GBRAIN_BIN" sources current --source xstudio-knowledge --json
"$GBRAIN_BIN" sync \
  --source xstudio-knowledge \
  --repo "$ROOT" \
  --no-pull \
  --no-extract \
  --yes \
  --json
"$GBRAIN_BIN" embed --stale
python3 "$ROOT/Model_Bench/validate_gbrain_knowledge.py"
```

Do not pass `--working-tree`; GBrain must index committed knowledge only. Do not run
`dream`, atom extraction, LLM expansion, source deletion, or GBrain upgrade here.

- [ ] **Step 2: Make deployment validate knowledge before mutation**

In `Model_Bench/deploy_l2_pipeline_runtime.sh`, after determining `ROOT` and checking
the Hermes Python/ODBC prerequisites—but before copying profile artifacts—run:

```bash
echo "== GBrain knowledge sync and readiness =="
bash "$ROOT/Model_Bench/sync_gbrain_knowledge.sh"
```

If sync, embedding, LM Studio, or evaluation fails, deployment exits before profile
files are copied or gateways are restarted. No `--skip` option is added.

- [ ] **Step 3: Add validation commands to the current local suite**

Add to `PY_FILES`:

```text
Model_Bench/kb_retrieval.py
Model_Bench/validate_gbrain_knowledge.py
Model_Bench/test_validate_gbrain_knowledge.py
```

Add after existing KB tests:

```bash
python3 Model_Bench/test_validate_gbrain_knowledge.py
python3 Model_Bench/validate_gbrain_knowledge.py
```

- [ ] **Step 4: Document the operator contract**

In `Knowledge/VALIDATION.md`, add:

```text
GBrain knowledge maintenance:
  bash Model_Bench/sync_gbrain_knowledge.sh

Read-only readiness/evaluation:
  python3 Model_Bench/validate_gbrain_knowledge.py

Required production result:
  source_id=xstudio-knowledge
  embedding_coverage_pct=100
  failed=0
```

State that the maintenance command indexes committed files only and never upgrades or
deletes GBrain data.

- [ ] **Step 5: Run shell and source checks**

```bash
bash -n Model_Bench/sync_gbrain_knowledge.sh
bash -n Model_Bench/deploy_l2_pipeline_runtime.sh
bash -n Model_Bench/validate_l2_pipeline_local.sh
git diff --check
```

Expected: all exit 0.

- [ ] **Step 6: Commit Task 7**

```bash
git add Model_Bench/sync_gbrain_knowledge.sh \
  Model_Bench/deploy_l2_pipeline_runtime.sh \
  Model_Bench/validate_l2_pipeline_local.sh \
  Knowledge/VALIDATION.md
git commit -m "ops(kb): make gbrain knowledge maintenance deterministic"
```

---

### Task 8: Live Backfill, Full Validation, and Evidence Commit

**Files:**
- Modify: `Knowledge/PENDING_POINTS.md`
- No other source changes unless a preceding test exposes a defect.

**Interfaces:**
- Consumes: Tasks 1–7 and the current LM Studio embedding model.
- Produces: live verified GBrain world and updated concise work register.

- [ ] **Step 1: Confirm the working tree contains no unintended files**

```bash
git status --short
```

Expected: only the pre-existing untracked historical handoff may remain. Do not stage
`Agent_Comms/0009-uncommitted-changes-l3-escalation-bug-ticket-cleanup.md`.

- [ ] **Step 2: Run deterministic GBrain maintenance**

```bash
bash Model_Bench/sync_gbrain_knowledge.sh
```

Expected: source selection succeeds, sync succeeds, stale embedding backfill reaches
100%, and all 10 retrieval cases pass. If a positive case fails, inspect retrieval and
correct the corpus/query contract; do not weaken expected prefixes to whatever random
result appeared. If a negative case fails, tighten acceptance/filtering before retry.

- [ ] **Step 3: Run the full local validation suite**

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Expected: syntax, lifecycle, typed-tool, knowledge, workflow, status, reconcile
preview, GBrain readiness, and GBrain evaluation all pass.

- [ ] **Step 4: Run a read-only bundle shadow probe**

Use a historical real ticket context fixture or existing ticket ID through the
current bundle builder without claiming or publishing. Verify the rendered package:

```text
contains source_id=xstudio-knowledge
contains at most 3 GBrain hits
contains source_ref and verification_required=true
contains current deterministic routes and SQL solution fields
does not contain agent_comms/, plans/, credentials, or full documents
is at most 8 KB for the knowledge bundle
```

Add a regression fixture only if this probe exposes a missing deterministic case.

- [ ] **Step 5: Deploy through the existing deployment script**

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

Expected: GBrain sync/evaluation runs before profile mutation; four active gateways
restart only after the gate passes.

- [ ] **Step 6: Verify deployed runtime without claiming a ticket**

```bash
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py reconcile --dry-run
```

Expected: status succeeds, dry-run makes no mutations, and current WIP/lifecycle state
is unchanged.

- [ ] **Step 7: Update the pending register**

Change `KB-001` in `Knowledge/PENDING_POINTS.md` from `WIP` to `Done` only when:

```text
embedding coverage = 100%
all retrieval cases pass
full local validation passes
bundle shadow probe passes
deployment and deployed status/dry-run pass
```

Set its final condition to the implementation commit IDs plus the live validation
date. If any condition is missing, keep it `WIP` and state the exact remaining gate.

- [ ] **Step 8: Commit validation evidence/status**

```bash
git add Knowledge/PENDING_POINTS.md
git commit -m "docs(kb): record gbrain knowledge validation"
```

- [ ] **Step 9: Stop at the GBrain boundary**

Report:

```text
files changed
commits
source/page/chunk/embedding counts
retrieval evaluation results
bundle shadow result
deployment/runtime result
remaining relation-atlas, domain-recipe, and reviewer-plan work
```

Do not implement relation extraction, new domain SQL recipes, reviewer changes, or a
natural production ticket run in this plan. Those consume the verified GBrain
interface produced here and require their own implementation plans.
