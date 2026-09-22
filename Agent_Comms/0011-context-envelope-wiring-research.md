---
id: 11
type: finding
from: codex
to: claude
created: 2026-09-22T09:25:00+05:30
---

# Wiring Research & Design: GBrain-Backed Deterministic Context Delivery into Chitragupta L2

This document provides the research, architecture mapping, and concrete wiring design for integrating GBrain-backed deterministic context delivery into Chitragupta's production L2 pipeline.

Per `AGENTS.md` and the **Scope Guard**, this document is an engineering design specification only; it modifies no production code.

---

## 1. Architectural Guardrails & Ground Rules

### 1.1 Five Architectural Responsibilities

`AGENTS.md` defines exactly five architectural responsibilities in Chitragupta:
1. **XStudio Helpdesk** (`dbo.Complaint_Mst_Tbl`) — User-visible incident store and operational state.
2. **Chitragupta Control** (`Model_Bench/l2_pipeline_runtime.py`) — Deterministic lifecycle, claim/WIP/queue management, retry/recovery, review routing, and audited publication.
3. **Jev — System One** (`Model_Bench/jev/`, `jev_workflow_bridge.py`) — Fast semantic layer: triage, evidence planning, candidate rating, execution-depth choice, meta-attention scoring, and primary semantic review.
4. **Hermes / Qwen — System Two** — Local model reasoning for composition, focused investigation, bounded rework, and exceptional deep review.
5. **Evidence / Knowledge** (`xstudio_l2` tool, `Knowledge/`, SQL KB, GBrain) — Typed read-only SQL, canonical Git documents, governed Solution articles, ticket/run ledgers.

**Governed context delivery and GBrain live strictly in Responsibility 5 (Evidence / Knowledge).**
- GBrain is a derivative ranking index, never authority, never lifecycle state, and never raw current-ticket truth.
- Local workers (System Two) never construct Windows/WSL paths, database transport, or raw GBrain CLI calls; all delivered context is harness-assembled and delivered inside the task card.
- The monolithic lifecycle authority `Model_Bench/l2_pipeline_runtime.py` must **not** be refactored, split into `l2_pipeline_runtime_core.py`, or replaced by the donor branch's divergent lifecycle lineage.

### 1.2 Subsystem Status on the Current Branch

Commit `380383d` ported the pure, reusable context-delivery modules onto the active feature branch (`integration/restore-gbrain-memory-plane`):
- `Model_Bench/l2_context_envelope.py` (pure envelope validation, schema, canonical JSON hashing)
- `Model_Bench/l2_context_delivery_base.py` (budgeting, rendering, requester query construction)
- `Model_Bench/l2_context_delivery_assembly.py` (`assemble_stage_context`, `assemble_degraded_context`)
- `Model_Bench/l2_context_delivery_receipts.py` (`persist_context_receipt`, `load_context_receipt`, `receipt_path`)
- `Model_Bench/l2_gbrain.py` (GBrain CLI adapter, wired to `~/.hermes/xstudio-gbrain` and `xstudio-knowledge` in commit `7028672`)
- `deploy/l2_context_policy.json` (per-stage budget policy)
- `Model_Bench/test_l2_context_delivery.py` & `test_l2_context_envelope.py` (passing 19/19 tests)

What was excluded from the port was the donor's call-site wiring (`l2_pipeline_context_cards.py`, `l2_pipeline_context_helpers.py`, `l2_pipeline_context_scout.py`) because those modules imported a split `l2_pipeline_runtime_core` module.

---

## 2. Answers to Mandated Questions

### Question 1: What is `assemble_stage_context()`'s exact function signature?

In `Model_Bench/l2_context_delivery_assembly.py` (lines 6–24):

```python
def assemble_stage_context(
    *,
    ticket: Mapping[str, Any],
    run_id: str,
    ticket_id: str,
    ticket_no: str,
    stage: str,
    review_cycle: int,
    policy: dict[str, Any] | None = None,
    policy_path: Path | None = None,
    manifest: dict[str, Any] | None = None,
    vault: Path | None = None,
    root: Path | None = None,
    proposal: Mapping[str, Any] | None = None,
    current_run_evidence: Any = None,
    rejection_reason: str | None = None,
    original_context: Mapping[str, Any] | None = None,
    include_gbrain: bool = True,
) -> tuple[dict[str, Any], str]:
```

#### Parameter Breakdown & Stage Specifics:

| Parameter | Type | Universal or Stage-Specific | Purpose & Usage |
| :--- | :--- | :--- | :--- |
| `ticket` | `Mapping[str, Any]` | **Universal** | Helpdesk ticket row (must contain requester fields: `BriefDetails`, `Description`, `ProblemCategory`, `HermesAreaName`, `ExtractedEntitiesJson`). |
| `run_id` | `str` | **Universal** | SQL Run identifier (`Hermes_L2_Response_Trn_Tbl.RunID`). Used for receipt path and provenance references. |
| `ticket_id` | `str` | **Universal** | Helpdesk ticket ID (`Complaint_Mst_Tbl.Complaint_ID`). |
| `ticket_no` | `str` | **Universal** | Human-readable ticket number (`TicketNo`). |
| `stage` | `str` | **Universal** | Must be one of `("investigation", "review", "rework")`. Governs budget limits and drop priority order from `l2_context_policy.json`. |
| `review_cycle` | `int` | **Universal** | 0 for fresh investigation; `cycle` for reviewer; `next_cycle` (e.g. 1 or 2) for rework. |
| `policy` | `dict \| None` | **Universal (Optional)** | Loaded policy dict. If omitted, loaded from `deploy/l2_context_policy.json`. |
| `policy_path` | `Path \| None` | **Universal (Optional)** | Override path to policy JSON file. |
| `manifest` | `dict \| None` | **Universal (Optional)** | `Knowledge/manifest.json`. If omitted, loaded from disk. |
| `vault` | `Path \| None` | **Universal (Optional)** | Root of learning vault. Defaults to `~/.hermes/l2-learning`. |
| `root` | `Path \| None` | **Universal (Optional)** | Repository root for resolving canonical documents. |
| `include_gbrain`| `bool` | **Universal (Optional)** | Flag to enable/disable GBrain search during retrieval (defaults to `True`). |
| `proposal` | `Mapping[str, Any] \| None` | **Stage-Specific: `review`, `rework`** | Frozen proposal dict from investigator. Embedded into `prior_ticket_evidence` with `source_type="frozen_proposal"`. Not used in fresh investigation. |
| `current_run_evidence` | `Any \| None` | **Stage-Specific: `review`, `rework`** | Recorded live SQL actions from `Hermes_L2_SQL_Action_Trn_Tbl`. Embedded into `prior_ticket_evidence` with `source_type="current_run_evidence"`. Not used in fresh investigation. |
| `rejection_reason` | `str \| None` | **Stage-Specific: `rework`** | The reviewer or Jev rejection text. Embedded into `prior_ticket_evidence` with `source_type="reviewer_rejection"` and `trust_class="prior_rejected_reasoning"`. |
| `original_context` | `Mapping[str, Any] \| None` | **Stage-Specific: `review`, `rework`** | The envelope dict from the initial investigation stage. Preserves context identity (`context_sha256`, `query_sha256`, `route`, `retrieval_degraded`) across review/rework cycles. |

---

### Question 2: Requester-Grounded Query & GBrain Scope/Source Selection

#### 1. Query Construction in Donor Code

In donor `Model_Bench/l2_context_delivery_base.py` (lines 35–41, 105–109):

```python
REQUESTER_FIELDS = (
    "BriefDetails",
    "Description",
    "ProblemCategory",
    "HermesAreaName",
    "ExtractedEntitiesJson",
)

def build_requester_retrieval_query(ticket: Mapping[str, Any]) -> str:
    """Build initial retrieval query only from requester/system-grounded fields."""
    parts = [_stable_field_text(ticket.get(field)) for field in REQUESTER_FIELDS]
    return normalize_whitespace(" ".join(part for part in parts if part))
```

And in donor `l2_pipeline_context_helpers.py` (lines 194–202):

```python
def _context_ticket_or_original(
    ticket: dict[str, Any], original_context: dict[str, Any] | None
) -> dict[str, Any]:
    if build_requester_retrieval_query(ticket):
        return ticket
    if original_context and str(original_context.get("requester_query") or "").strip():
        # The original query was already deterministically derived only from safe
        # requester/system fields; using it as a degraded refresh seed cannot add a
        # model hypothesis to retrieval.
        return {"BriefDetails": str(original_context["requester_query"])}
    return ticket
```

#### 2. Scope & Source Selection in Donor Code

In donor `kb_retrieval_corpus.py` (lines 106–110, 155–163):

```python
_CASE_CONFIG = {
    "approved_cases": ("cases/approved", "historical_approved_case", frozenset({"reviewed_published_historical_case"})),
    "rejected_cases": ("cases/rejected", "historical_rejected_case", frozenset({"reviewed_negative_example"})),
    "reopened_cases": ("cases/reopened", "historical_reopened_case", frozenset({"observed_resolution_regression"})),
}

scopes = ("facts", "solutions", "approved_cases", "rejected_cases", "reopened_cases")
gbrain: dict[str, dict[str, Any]] = {}
if include_gbrain and query.strip():
    for scope in scopes:
        gbrain[scope] = gbrain_scope_search(
            query, scope=scope, limit=max(1, configured[scope])
        )
```

In `l2_gbrain.py` (lines 65–77):
- Scope `trusted` $\rightarrow$ `(XSTUDIO_KNOWLEDGE_SOURCE, "l2-knowledge", "l2-facts", "l2-solutions")`
- Scope `knowledge` $\rightarrow$ `(XSTUDIO_KNOWLEDGE_SOURCE, "l2-knowledge")`
- Scope `facts` $\rightarrow$ `("l2-facts",)`
- Scope `solutions` $\rightarrow$ `("l2-solutions",)`
- Scope `approved_cases` $\rightarrow$ `("l2-approved-cases",)`
- Scope `rejected_cases` $\rightarrow$ `("l2-rejected-cases",)`
- Scope `reopened_cases` $\rightarrow$ `("l2-reopened-cases",)`

#### 3. Equivalent Data Structures on Current Branch

The current branch already possesses the identical information in its existing data structures:
- **For Investigation:**
  - `poll["ticket"]` or `bundle["ticket"]`: standard Python `dict` containing `BriefDetails`, `Description`, `ProblemCategory`, `HermesAreaName`, `ExtractedEntitiesJson`.
  - In `l2_pipeline_runtime.py` lines 2491–2493 (`_run_kb_retrieval`):
    ```python
    query = " ".join(str(ticket.get(k) or "") for k in (
        "BriefDetails", "Description", "ProblemCategory", "HermesAreaName", "ExtractedEntitiesJson"
    )).strip()
    ```
    This matches `build_requester_retrieval_query()` exactly.
- **For Review:**
  - `proposal`: dict passed to `create_reviewer_card` (`proposal["ticket_id"]`, `proposal["run_id"]`).
  - `_proposal_preflight_state(args, proposal)` (lines 1518–1545) already fetches `ticket_context` using `Hermes_Orchestrator.py --get-ticket-context` and `run_actions` using `--get-run-actions`.
  - `source_task["body"]`: contains `context_receipt:` and `context_sha256:` from the investigation card.
- **For Rework:**
  - `source_task`: Kanban task dict.
  - `reason`: string parameter passed to `create_rework_card`.
  - `task_ticket_id(source_task)` and `task_run_id(source_task)`.
  - `_original_context_for_task(source_task)` loads the original receipt via `load_context_receipt()` from the receipt path recorded in `source_task["body"]`.

---

### Question 3: Overlap with Jev's Context Compiler & Merging Strategy

#### 1. What Jev Context Compilation Does on Current Branch

`Model_Bench/l2_pipeline_runtime.py` lines 1067–1342:
- **`_make_context_chunks(...)`** builds typed whole-context chunks:
  - `ticket` (Pinned: `minimum_level=2`, `fallback_level=3`)
  - `routing` (Jev triage + route candidates: `minimum_level=1`, `fallback_level=2`)
  - `prior_ledger` (Pinned: `minimum_level=1`, `fallback_level=2`)
  - `prior_attempts` (Historical runs: `fallback_level=1`)
  - `evidence_plan` (Jev evidence plan: `fallback_level=1`)
  - `candidate_backlog` (Deterministic real tables: `fallback_level=0`)
  - `kb_solution_{i}` (Known SQL solutions: `fallback_level=1`, pinned to `minimum_level=2` if chosen by Jev)
  - `live_probe_{i}` (Bounded SQL probes into XStudio: `minimum_level=2`, `fallback_level=3`)
- **`_compile_model_context(chunks, assessment, budget_chars)`**:
  - Compiles chunks by meta-attention score into FULL (level 3), COMPACT (level 2), SUMMARY (level 1), or OMIT (level 0).
  - Pinned chunks (`minimum_level > 0`) cannot be omitted.
  - Omitted chunks are recorded in `omitted` with `recover_with` instructions.
  - Output is packaged into `model_bundle` and rendered as:
    `\n--- Investigation context (Jev meta-attention compiled) ---\n`

#### 2. Does Donor Envelope Duplicate Jev Context Compilation?

**For fresh investigation cards: YES, there is substantial overlap.**
- Both systems attempt to select relevant knowledge/solution material.
- Both enforce budget limits without character truncation of raw facts (Jev degrades by structured levels; donor drops whole items via `drop_order`).
- Both emphasize current live evidence over historical analogy.

**For review and rework cards: NO, there is NO duplication.**
- On the current branch, `create_reviewer_card` and `create_rework_card` do **not** run Jev context chunk compilation.
- Reviewer cards currently contain only `proposal_json` and instructions. They receive **no** canonical documents, **no** negative historical patterns, and **no** regression cases.
- Rework cards currently receive only the verbatim rejection string and prior ledger. They receive **no** governed context or canonical procedure.

#### 3. How GBrain Context Must Be Merged (Not Appended as Competing Blocks)

If we blindly append the donor's `rendered_context` (which is 15k–30k characters of Markdown) directly before `investigation_bundle` (which is 10k–30k characters of JSON), the local model receives two huge competing context sections with contradictory instructions and duplicate routes/solutions.

The correct architectural integration respects the five responsibilities:

```text
[Responsibility 5: Evidence/Knowledge]
GBrain / Canonical Docs / SQL Solutions
                 │
                 ▼
      _make_context_chunks()
  (Typed chunks with trust & provenance)
                 │
                 ▼
[Responsibility 3: Jev System One]
  Meta-Attention Scoring & Budgeting
                 │
                 ▼
[Responsibility 2: Chitragupta Control]
  Assemble L2ContextEnvelope from delivered chunks
  Compute canonical context_sha256 & persist receipt
                 │
                 ▼
Task Card Body: Provenance Header + Single Compiled Context Bundle + Typed Contract
```

**Concrete Merge Design:**
1. **For Investigation Cards:**
   - Instead of running `assemble_stage_context` as an independent string renderer that duplicates the card body, the retrieval output (canonical procedure documents, promoted facts, and approved cases from `xstudio-knowledge` and GBrain) is passed into `_make_context_chunks()` as typed chunks:
     - `canonical_docs` chunk: `kind: "canonical_reference"`, `authority: "CANONICAL_PROCEDURE"`, `minimum_level=1` (pinned at least to summary).
     - `promoted_facts` chunk: `kind: "reviewed_facts"`, `authority: "REVIEWED_FACTS"`.
     - `historical_cases` chunk: `kind: "historical_cases"`, `authority: "HISTORICAL_ANALOGY"`.
   - Jev's meta-attention scores these chunks alongside live probes and ticket context.
   - The final delivered chunk set is recorded in an `L2ContextEnvelope`, which computes the deterministic `context_sha256` and writes the audit receipt via `persist_context_receipt()`.
   - The card body gets the compact 5-line `provenance_header(envelope, receipt)` at the top, followed by the single, unified Jev-compiled bundle and `_query_instructions()`.
2. **For Review and Rework Cards:**
   - Because Jev meta-attention does not run on review/rework cards, `assemble_stage_context(stage="review")` and `assemble_stage_context(stage="rework")` run directly as designed in the donor branch.
   - Review cards receive negative historical cases (`rejected_cases`, `reopened_cases`), canonical review procedure, frozen proposal, and live run action receipts.
   - Rework cards receive the rejection reason (tagged as `prior_rejected_reasoning`), original context identity, and canonical procedure.
   - The envelope is hashed, the receipt persisted, and `rendered_context` is inserted before the reviewer contract / rework reason.

---

### Question 4: Context Receipt Persistence & Vault Directory Independence

#### 1. Exact Persistence Path Pattern

In `Model_Bench/l2_context_delivery_receipts.py` (lines 6–15):

```python
def receipt_path(
    envelope: Mapping[str, Any], *, vault: Path | None = None
) -> Path:
    vault = vault or vault_path()
    run = re.sub(r"[^A-Za-z0-9_.-]+", "-", str(envelope["run_id"])).strip("-") or "unknown-run"
    stage = re.sub(r"[^A-Za-z0-9_.-]+", "-", str(envelope["pipeline_stage"])).strip("-") or "unknown-stage"
    cycle = int(envelope["review_cycle"])
    digest = str(envelope["context_sha256"])
    return vault / "retrieval" / "receipts" / run / f"{stage}-{cycle}-{digest[:20]}.json"
```

The exact file path pattern is:
```text
~/.hermes/l2-learning/retrieval/receipts/<sanitized_run_id>/<stage>-<review_cycle>-<context_sha256[:20]>.json
```
For example:
```text
~/.hermes/l2-learning/retrieval/receipts/run-842/investigation-0-a8f3b2c1d4e5f6071829.json
~/.hermes/l2-learning/retrieval/receipts/run-842/review-0-b9e4c3d2e1f0a8b7c6d5.json
~/.hermes/l2-learning/retrieval/receipts/run-842/rework-1-c0f5d4e3b2a198765432.json
```

#### 2. Does Receipt Persistence Require the Vault Directory to Exist?

**NO.**
In `Model_Bench/l2_context_delivery_receipts.py` (lines 26–27):

```python
path = receipt_path(envelope, vault=vault)
path.parent.mkdir(parents=True, exist_ok=True)
```

Python's `pathlib.Path.mkdir(parents=True, exist_ok=True)` recursively creates all missing parent directories (`~/.hermes/l2-learning/`, `retrieval/`, `receipts/`, and `<run>/`).

#### 3. Should Receipt Persistence Be Deferred Until Vault Exists?

**NO. Receipt persistence must be active immediately and independent of vault learning lanes.**
- Receipt persistence is an **audit and reproducibility invariant**, not learning state.
- In donor `l2_pipeline_context_helpers.py` (lines 224–226):
  ```python
  # Receipt persistence is part of the provenance correctness contract. If
  # this fails, do not create a worker card whose delivered context cannot
  # later be reconstructed.
  receipt = str(persist_context_receipt(envelope, rendered))
  ```
- And in `l2_pipeline_context_scout.py` (lines 46–48):
  ```python
  # A claimed run without durable context provenance must not be handed to
  # a worker. Fail it cleanly so the normal retry mechanism can reclaim it.
  ```
- The learning vault lanes (`l2-knowledge`, `l2-facts`, `l2-solutions`, etc.) are future mined corpus files; the retrieval receipts directory (`retrieval/receipts/`) is purely an execution ledger. Persisting receipts right now works cleanly and guarantees that every delivered card is auditable and repeatable.

---

### Question 5: Degraded-Mode Semantics: Donor Code vs Current `l2_gbrain.py`

#### 1. Degraded Mode in Donor Code

There are two levels of degradation in the donor implementation:

##### Level A: Soft Degradation (Missing Sources / Partial Search Failure)
In `kb_retrieval_corpus.py` (lines 191–207):
```python
errors = [str(item.get("error")) for item in canonical if item.get("error")]
for scope in scopes:
    if not gbrain[scope].get("ok"):
        errors.append(f"{scope}: {gbrain[scope].get('error') or 'GBrain retrieval failed'}")

return {
    ...
    "retrieval_degraded": bool(errors),
    "degradation_reasons": errors,
}
```
And in `l2_context_delivery_base.py` (lines 255–261):
```python
if retrieval["retrieval_degraded"]:
    lines += [
        f"degradation_reason: {retrieval.get('degradation_reason') or 'historical retrieval degraded'}",
        "",
        "IMPORTANT: Historical retrieval is degraded/unavailable. Do not infer historical precedent. "
        "Use current live evidence and canonical procedure.",
    ]
```

##### Level B: Catastrophic Harness Fallback (`assemble_degraded_context`)
In `Model_Bench/l2_context_delivery_assembly.py` (lines 181–186, 225–255):
```python
def assemble_degraded_context(...) -> tuple[dict[str, Any], str]:
    """Build a valid fail-closed envelope when normal retrieval cannot run at all.

    This is intentionally not a broad-search fallback. It provides only requester-grounded
    identity plus current-run/prior provenance supplied by the harness, marks historical
    retrieval degraded, and tells the worker to rely on live typed evidence.
    """
...
    envelope = build_context_envelope(
        generated_at=utc_now(),
        run_id=run_id,
        ticket_id=ticket_id,
        ticket_no=ticket_no,
        pipeline_stage=stage,
        review_cycle=review_cycle,
        route="discover",
        route_reasons=["context assembly failed before governed retrieval completed"],
        requester_query=query,
        prior_ticket_evidence=prior,
        retrieval_backend="degraded-harness-fallback",
        gbrain_sources=[],
        gbrain_query=query,
        retrieval_degraded=True,
        degradation_reason=normalize_whitespace(reason)[:2000] or "governed context assembly failed",
        stage_policy=stage,
        delivered_counts={
            "canonical_documents": 0,
            "promoted_facts": 0,
            "governed_solutions": 0,
            "approved_cases": 0,
            "rejected_cases": 0,
            "reopened_cases": 0,
            "prior_ticket_evidence": len(prior),
        },
        dropped_counts={},
        source_hit_counts={},
        live_sql_leads=[],
    )
    return envelope, render_context_envelope(envelope)
```

#### 2. Matching with `Model_Bench/l2_gbrain.py`'s Current `search()` Contract

In `Model_Bench/l2_gbrain.py` (lines 200–245, adapted in commit `7028672`):
```python
queried: list[str] = []
missing: list[str] = []
merged_rows: list[dict[str, Any]] = []
last_hard_error: str | None = None
for source_id in sources:
    rc, out, err = run([
        "search", query,
        "--source-id", source_id,
        "--limit", str(bounded_limit),
        "--json",
    ])
    if rc != 0:
        message = (err or out).strip()
        if "unknown_source" in message or "does not exist" in message:
            missing.append(source_id)
            continue
        last_hard_error = message[-1000:] or f"gbrain search exited {rc}"
        continue
    try:
        payload = parse_json(out)
    except Exception:
        last_hard_error = "gbrain returned non-JSON output"
        continue
    queried.append(source_id)
    rows = payload if isinstance(payload, list) else payload.get("results") or []
    for row in rows:
        if isinstance(row, dict):
            merged_rows.append(row)

if not queried:
    return {
        "ok": False,
        "error": last_hard_error or "no requested source is populated yet",
        "retry_same_call": False,
        "backend": "gbrain",
        "scope": scope,
        "source_ids": list(sources),
        "missing_source_ids": missing,
    }
```

**Comparison Analysis:**
- **Exact Match:** The contract matches precisely.
  - When searching scope `knowledge` or `trusted`, `xstudio-knowledge` is queried and succeeds. The unpopulated learning lanes (`l2-knowledge`, `l2-facts`, `l2-solutions`) are logged in `missing_source_ids` and skipped; `search()` returns `ok: True`.
  - When searching a scope where *no* source is populated (e.g. `cases`, which currently only contains `l2-approved-cases`, `l2-rejected-cases`, `l2-reopened-cases`), `queried` is empty, and `search()` returns `ok: False` with `error: "no requested source is populated yet"`.
  - Upstream in `assemble_stage_context`, this triggers `retrieval_degraded = True` with the explicit degradation reason.
  - The worker card receives the degraded notice:
    `retrieval_degraded: true`
    `degradation_reason: cases: no requested source is populated yet`
    `IMPORTANT: Historical retrieval is degraded/unavailable. Do not infer historical precedent. Use current live evidence and canonical procedure.`
  - The pipeline never crashes, never hallucinated analogies, and fails closed gracefully.

---

### Question 6: Expected Envelope Shapes Revealed by Test Fixtures

From `Model_Bench/test_l2_context_delivery.py`:

#### 1. Fresh Investigation Stage
From `test_investigation_builds_hashed_governed_context` (lines 115–127):

```python
def test_investigation_builds_hashed_governed_context(self):
    with mock.patch.object(mod.kb, "retrieve", return_value=self._retrieval()):
        envelope, rendered = mod.assemble_stage_context(
            ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
            stage="investigation", review_cycle=0, policy=self.policy, vault=self.vault, manifest={},
        )
    self.assertEqual(envelope["route"], "sap_posting")
    self.assertEqual(len(envelope["context_sha256"]), 64)
    self.assertIn("HARNESS-PROVIDED GOVERNED CONTEXT", rendered)
    self.assertNotIn("CONFIRMATION_BIAS_SENTINEL", envelope["requester_query"])
    self.assertEqual(envelope["retrieval"]["stage_policy"], "investigation")
    self.assertNotIn("l2-sessions", envelope["retrieval"]["gbrain_sources"])
```

**Delivered Envelope Shape for Investigation:**
```json
{
  "schema_version": 1,
  "pipeline_stage": "investigation",
  "review_cycle": 0,
  "route": "sap_posting",
  "route_reasons": ["TransactionID identifier"],
  "requester_query": "SAP posting failed material document missing SAP XBatch {\"TransactionID\":\"T-100\"}",
  "canonical_documents": [
    {"source_ref": "Knowledge/mental-model.md", "trust_class": "canonical_reference", ...},
    {"source_ref": "Knowledge/execution-model.md", "trust_class": "canonical_reference", ...},
    {"source_ref": "Knowledge/sap.md#posting", "trust_class": "canonical_reference", ...}
  ],
  "promoted_facts": [ ... up to 5 items ... ],
  "governed_solutions": [ ... up to 3 items ... ],
  "approved_cases": [ ... up to 2 items ... ],
  "rejected_cases": [ ... up to 1 item ... ],
  "reopened_cases": [ ... up to 1 item ... ],
  "prior_ticket_evidence": [],
  "retrieval": {
    "stage_policy": "investigation",
    "retrieval_degraded": false,
    "delivered_counts": {"canonical_documents": 3, "promoted_facts": 5, "governed_solutions": 3, "approved_cases": 2, "rejected_cases": 1, "reopened_cases": 1, "prior_ticket_evidence": 0},
    "dropped_counts": {"reopened_cases": 0, ...}
  },
  "context_sha256": "64-char-hex",
  "query_sha256": "64-char-hex"
}
```

#### 2. Review Stage (Negative-Asymmetric & Carrying Frozen Proposal)
From `test_review_is_negative_asymmetric_and_carries_frozen_proposal` (lines 128–143):

```python
def test_review_is_negative_asymmetric_and_carries_frozen_proposal(self):
    data = self._retrieval()
    with mock.patch.object(mod.kb, "retrieve", return_value=data):
        envelope, rendered = mod.assemble_stage_context(
            ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
            stage="review", review_cycle=0, policy=self.policy, vault=self.vault, manifest={},
            proposal={"response_type": "RESOLUTION", "root_cause": "x", "reply_text": "done"},
            current_run_evidence=[{"operation": "select", "ok": True}],
        )
    self.assertEqual(len(envelope["rejected_cases"]), 1)
    self.assertEqual(len(envelope["reopened_cases"]), 1)
    refs = [v["source_type"] for v in envelope["prior_ticket_evidence"]]
    self.assertIn("frozen_proposal", refs)
    self.assertIn("current_run_evidence", refs)
    self.assertIn("REVIEWER-REJECTED", rendered)
```

**Delivered Envelope Shape for Review:**
- Emphasizes counter-examples: `rejected_cases` (2) and `reopened_cases` (2) take priority in budget over `approved_cases` (1) and `solutions` (2).
- `prior_ticket_evidence` contains:
  1. `source_type="frozen_proposal"`, `source_ref="run:run-1/proposal/review-cycle:0"`, `content={"response_type": "RESOLUTION", ...}`.
  2. `source_type="current_run_evidence"`, `source_ref="run:run-1/actions"`, `content=[{"operation": "select", "ok": True}]`.

#### 3. Rework Stage (Carrying Rejection Reason & Original Context Identity)
From `test_rework_preserves_original_context_identity_and_rejection_as_negative` (lines 144–157):

```python
def test_rework_preserves_original_context_identity_and_rejection_as_negative(self):
    original = {"context_sha256": "a"*64, "query_sha256": "b"*64, "route": "sap_posting",
                "retrieval": {"retrieval_degraded": False}}
    with mock.patch.object(mod.kb, "retrieve", return_value=self._retrieval()):
        envelope, _ = mod.assemble_stage_context(
            ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
            stage="rework", review_cycle=1, policy=self.policy, vault=self.vault, manifest={},
            rejection_reason="Evidence did not prove current state.",
            original_context=original,
        )
    trusts = [v["trust_class"] for v in envelope["prior_ticket_evidence"]]
    self.assertIn("prior_rejected_reasoning", trusts)
    self.assertTrue(any(v["source_ref"] == "context:" + "a"*64 for v in envelope["prior_ticket_evidence"]))
```

**Delivered Envelope Shape for Rework:**
- `pipeline_stage`: `"rework"`, `review_cycle`: 1 (or 2).
- `prior_ticket_evidence` contains:
  1. `source_type="reviewer_rejection"`, `trust_class="prior_rejected_reasoning"`, `content="Evidence did not prove current state."`.
  2. `source_type="original_context_identity"`, `source_ref="context:aaaa..."`, `content={"context_sha256": "aaaa...", "query_sha256": "bbbb...", "route": "sap_posting", ...}`.
  3. Optionally `frozen_proposal` and `current_run_evidence`.

---

## 3. Concrete Wiring Mapping for Current Runtime Functions

Here is the exact mapping showing what call to add, with what arguments, and where in the card body string the rendered context must be inserted.

### 3.1 Function 1: Fresh Investigation Card

#### Call Site Locations:
- `_prepare_claimed_ticket()` in `Model_Bench/l2_pipeline_runtime.py` (lines 2797–2850)
- `_investigator_task_spec()` in `Model_Bench/l2_pipeline_runtime.py` (lines 2757–2795)
- `_investigation_bundle()` in `Model_Bench/l2_pipeline_runtime.py` (lines 2544–2688)

#### Data Available at Call Site:
- `run_id = str(poll["run_id"])`
- `ticket_id = str(poll["ticket_id"])`
- `ticket = poll.get("ticket") or {}`
- `ticket_no = str(ticket.get("TicketNo") or ticket_id)`
- `route_skill`
- `qwen_free_fallback_reason`

#### Exact Call to Add:
In `_prepare_claimed_ticket()` (or inside helper `_build_and_persist_stage_context`):

```python
envelope, rendered_context, receipt = _build_and_persist_stage_context(
    args=args,
    ticket=ticket,
    run_id=run_id,
    ticket_id=ticket_id,
    ticket_no=ticket_no,
    stage="investigation",
    review_cycle=0,
    dry_run=False,
)
```

#### Insertion in Task Body String:
In `_investigator_task_spec()` (lines 2766–2782), insert `provenance_header(envelope, receipt)` and `rendered_context` immediately after the header fields and before `investigation_bundle`:

```python
body = (
    f"run_id: {run_id}\n"
    f"ticket_id: {ticket_id}\n"
    f"ticket_no: {ticket_no}\n"
    "review_cycle: 0\n"
    "pipeline_stage: investigation\n"
    + provenance_header(envelope, receipt)
    + "\n"
    + rendered_context
    + investigation_bundle
    + (
        "\n--- Qwen-free fast-path fallback ---\n"
        + qwen_free_fallback_reason
        + "\nThe deterministic fast path made no Helpdesk mutation. Continue using the "
          "local_model_scope and compiled context above; do not restart discovery.\n"
        if qwen_free_fallback_reason
        else ""
    )
    + _query_instructions(run_id, ticket_id)
)
```

*(Note: Under the recommended unified approach in §4, `rendered_context` is merged into Jev's context chunks so that `investigation_bundle` itself contains the budgeted items, leaving only `provenance_header(envelope, receipt)` at the top of the body).*

---

### 3.2 Function 2: Review Card

#### Call Site Location:
- `create_reviewer_card()` in `Model_Bench/l2_pipeline_runtime.py` (lines 1619–1674)

#### Data Available at Call Site:
- `args: argparse.Namespace`
- `proposal: dict[str, Any]` (contains `run_id`, `ticket_id`, `proposal_json`, `response_type`, `reply_text`, etc.)
- `source_task: dict[str, Any]` (investigator task dict)
- `run_id = str(proposal["run_id"])`
- `ticket_id = str(proposal["ticket_id"])`
- `ticket_no = body_field(source_task.get("body"), "ticket_no") or ticket_id`
- `cycle = task_review_cycle(source_task)`
- `proposal_json = json.dumps(proposal, separators=(",", ":"), default=str)`

#### Exact Call to Add:
Before building `body`:

```python
original_context, original_receipt = _original_context_for_task(source_task)
ticket = _ticket_snapshot(args, ticket_id)
current_run_evidence = _run_evidence_snapshot(args, run_id)

envelope, rendered_context, receipt = _build_and_persist_stage_context(
    args=args,
    ticket=ticket,
    run_id=run_id,
    ticket_id=ticket_id,
    ticket_no=ticket_no,
    stage="review",
    review_cycle=cycle,
    dry_run=dry_run,
    proposal=proposal,
    current_run_evidence=current_run_evidence,
    original_context=original_context,
)

source_context_sha = (original_context or {}).get("context_sha256") or body_field(source_task.get("body"), "context_sha256") or "unknown"
source_receipt_value = original_receipt or task_context_receipt(source_task) or "unknown"
```

#### Insertion in Task Body String:
In `create_reviewer_card()` (lines 1633–1649):

```python
body = (
    f"run_id: {run_id}\n"
    f"ticket_id: {ticket_id}\n"
    f"ticket_no: {ticket_no}\n"
    f"investigation_task_id: {source_task['id']}\n"
    f"review_cycle: {cycle}\n"
    "pipeline_stage: review\n"
    + provenance_header(envelope, receipt)
    + f"source_context_sha256: {source_context_sha}\n"
    + f"source_context_receipt: {source_receipt_value}\n"
    + f"proposal_json: {proposal_json}\n\n"
    + rendered_context
    + "\n--- Reviewer contract ---\n"
    "This local review exists because Jev primary review selected LOCAL_REVIEW, was unavailable, "
    "or failed deterministic confidence/safety gates. Do not repeat the whole investigation. "
    "Inspect the Jev primary-review result embedded in proposal_json, identify the exact disputed "
    "or underdetermined claim, and verify only the smallest sufficient live evidence set. "
    "Approve with kanban_complete; reject with kanban_block. The deterministic reconciler owns "
    "publication/rework.\n"
)
body += _query_instructions(run_id, ticket_id)
```

---

### 3.3 Function 3: Rework Card

#### Call Site Location:
- `create_rework_card()` in `Model_Bench/l2_pipeline_runtime.py` (lines 1929–1998)

#### Data Available at Call Site:
- `args: argparse.Namespace`
- `source_task: dict[str, Any]` (the reviewer card that rejected, or the investigator card rejected by Jev primary review)
- `reason: str` (rejection reason)
- `investigation_task_id: Optional[str]`
- `run_id = task_run_id(source_task)`
- `ticket_id = task_ticket_id(source_task)`
- `current_cycle = task_review_cycle(source_task)`
- `next_cycle = current_cycle + 1`
- `ticket_no = body_field(source_task.get("body"), "ticket_no") or ticket_id`
- `prior = "" if dry_run else _persist_rejected_ledger(args, investigation_task_id, run_id)`

#### Exact Call to Add:
Before building `body`:

```python
original_context, original_receipt = _original_context_for_task(source_task)
ticket = _ticket_snapshot(args, ticket_id)
current_run_evidence = _run_evidence_snapshot(args, run_id)
original_proposal = task_proposal(source_task)

envelope, rendered_context, receipt = _build_and_persist_stage_context(
    args=args,
    ticket=ticket,
    run_id=run_id,
    ticket_id=ticket_id,
    ticket_no=ticket_no,
    stage="rework",
    review_cycle=next_cycle,
    dry_run=dry_run,
    proposal=original_proposal,
    current_run_evidence=current_run_evidence,
    rejection_reason=reason,
    original_context=original_context,
)

source_context_sha = (original_context or {}).get("context_sha256") or body_field(source_task.get("body"), "source_context_sha256") or "unknown"
source_receipt_value = original_receipt or task_source_context_receipt(source_task) or task_context_receipt(source_task) or "unknown"
```

#### Insertion in Task Body String:
In `create_rework_card()` (lines 1955–1971):

```python
body = (
    f"run_id: {run_id}\n"
    f"ticket_id: {ticket_id}\n"
    f"ticket_no: {ticket_no}\n"
    f"review_cycle: {next_cycle}\n"
    f"rework_source_id: {source_task['id']}\n"
    f"prior_investigation_task_id: {investigation_task_id or 'unknown'}\n"
    "pipeline_stage: rework\n"
    + provenance_header(envelope, receipt)
    + f"source_context_sha256: {source_context_sha}\n"
    + f"source_context_receipt: {source_receipt_value}\n\n"
    + rendered_context
    + f"\nREWORK REASON:\n{reason}\n\n"
    "Address this exact rejected/invalid point using current live evidence. Reuse prior verified "
    "findings; do not restart the entire investigation unless the objection invalidates them. "
    "Complete with the full structured metadata contract.\n"
)
if prior:
    body += f"\nPRIOR FINDINGS (verbatim):\n{prior}\n"
body += _query_instructions(run_id, ticket_id)
```

---

## 4. Key Discovery: Retriever Interface Reconciliation

During research, an essential signature discrepancy was identified between the donor branch and the current feature branch:

1. **On the donor branch:**
   `kb_retrieval.py` was replaced with `kb_retrieval_corpus.py`, which had the signature:
   `retrieve(query_or_conn, query_or_manifest, ..., vault=..., include_gbrain=..., limits=...)`
   and returned `promoted_facts`, `approved_cases`, `rejected_cases`, `reopened_cases`, `gbrain`.
2. **On the current branch:**
   `kb_retrieval.py` is the live SQL + Jev retriever:
   `retrieve(conn, query, manifest, top=5, min_score=7.0, min_matched_terms=MIN_MATCHED_TERMS, *, ticket_id=..., run_id=...)`
   which queries `dbo.Hermes_Solution_Article_Mst_Tbl` and runs Jev `assess_kb_candidates`.
3. **In `l2_context_delivery_assembly.py` (lines 33–41):**
   The code directly calls `kb.retrieve(query, manifest, vault=vault, root=root, top=..., include_gbrain=include_gbrain, limits=limits)`.
   In `test_l2_context_delivery.py`, this was tested with a mock (`mock.patch.object(mod.kb, "retrieve")`).

### Recommended Resolution (Preserving Scope Guard)
Do **not** overwrite `kb_retrieval.py` with the donor version! That would break the live SQL Solution Article retrieval and Jev KB applicability evaluation.

Instead, introduce an adapter module `Model_Bench/l2_context_retriever.py` (or assign `_assembly.kb = l2_context_retriever`):
- For canonical documents: loads directly from `Knowledge/` using `manifest.json`.
- For governed solutions: searches SQL `Hermes_Solution_Article_Mst_Tbl` using current `kb_retrieval.py`.
- For facts/cases: queries `l2_gbrain.search()` against the active scopes (`knowledge`, `trusted`, `cases`).
- Returns the composite dict containing `canonical_documents`, `promoted_facts`, `governed_solutions`, `approved_cases`, `rejected_cases`, `reopened_cases`, and `gbrain` telemetry.

This cleanly harmonizes GBrain with SQL Solutions and Git Knowledge without deleting or replacing either subsystem.

---

## 5. Summary & Next Steps

1. **No lifecycle fork required:** The donor's card construction and context assembly logic can be added cleanly to the existing functions in `Model_Bench/l2_pipeline_runtime.py` without splitting the file or touching the state machine.
2. **Review & rework benefit immediately:** Review and rework cards currently lack historical negative cases and regression warnings; wiring the envelope into `create_reviewer_card()` and `create_rework_card()` directly provides them.
3. **Receipts are active today:** `persist_context_receipt()` creates `~/.hermes/l2-learning/retrieval/receipts/` on the fly; it does not depend on unpopulated learning lanes and should be active from day one.
4. **Degraded mode is safe and verified:** When learning vault lanes do not exist, `l2_gbrain.py` skips them gracefully if `xstudio-knowledge` answers, or returns `retrieval_degraded: true` with instructions to rely on live SQL evidence, failing closed.
