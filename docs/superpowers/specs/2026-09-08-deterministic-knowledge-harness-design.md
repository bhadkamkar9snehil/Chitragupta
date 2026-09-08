# Deterministic Knowledge Harness Design

**Status:** Proposed  
**Date:** 2026-09-08  
**Scope:** Chitragupta Hermes L2 knowledge routing, investigation context, and review evidence

## 1. Outcome

For every claimed ticket, the harness must deterministically provide a compact,
provenance-rich map of likely investigation areas and the safest first evidence
recipes before Qwen starts. During investigation and review, the same registry
must support bounded follow-up retrieval without asking the model to rediscover
XStudio's schema, relationships, or database transport.

The model interprets evidence and drafts or reviews a response. It does not own
knowledge indexing, route selection, SQL transport, lifecycle transitions, or
publication.

## 2. Existing baseline and change strategy

This is an incremental hardening of the live harness, not a greenfield knowledge
platform. The implementation must extend the current owners in place:

| Existing asset | Current responsibility | Required change |
|---|---|---|
| `Model_Bench/build_xstudio_semantic_atlas.py` | Builds schema/SP atlas from authoritative exports | Add configuration relations and resolved graph edges |
| `Knowledge/xstudio_semantic_atlas.json` and `Knowledge/atlas/` | Checked-in machine and compact Markdown atlas | Extend format/version; do not create a parallel registry |
| `Knowledge/schema_allowlist.json` | Validates model-visible objects and columns | Add verified `XStudio_Configuration_Xbatch` surfaces |
| `Model_Bench/kb_retrieval.py` | Deterministic routes plus approved SQL solution matches | Add bounded, source-scoped GBrain results and health/abstention metadata |
| `deterministic_ticket_route()` | Routes SAP API, work-order/campaign, and heat tickets | Extend from atlas/domain recipes; retain exact current routes |
| `_investigation_bundle()` / `_dispatch_route_context()` | Produces compact dispatch context and executes first recipes | Enrich the existing package; do not add a second planner pipeline |
| `Model_Bench/xstudio_l2_tool_bridge.py` | Guarded SQL transport, auditing, macros, result bounds | Resolve tools/recipes through the extended atlas and add only proven domain macros |
| `xstudio-l2-tools` plugin | Small typed tool schemas, context repair, budgets | Reuse schemas and enforcement; add tools only where a macro earns one |
| Existing reviewer/reconciler | Frozen proposal, independent evidence, bounded rework | Add registry/retrieval provenance and mechanical pre-review checks in place |
| Existing ticket scout | WIP gate, reconciliation, dependency checks, observability flush | Add knowledge-readiness check here; no new daemon or cron |
| Existing Hermes SQL procedures | Claim, context, audit, evidence, ledger, publish | Preserve; revise/add read procedures only when existing audited reads cannot express a recipe |

The implementation starts with call-site and live-use audits. Existing code is kept
when it already owns the responsibility. Historical compatibility entrypoints are
not revived merely because they exist in the repository.

### Ponytail constraint

For every proposed file, abstraction, procedure, tool, or process, stop at the first
rung that works:

1. reuse an existing owner;
2. use Python/SQL/JSON capabilities already present;
3. extend an installed dependency such as GBrain;
4. add the smallest implementation that satisfies a tested gap.

Do not create duplicate stores, wrappers, managers, services, schedulers, generic
frameworks, or speculative extension points. This minimalism never removes
trust-boundary validation, auditing, data-loss protection, deterministic lifecycle
ownership, provenance, or tests. This follows Ponytail's actual YAGNI/stdlib/native/
installed-dependency/minimum-code ladder, not a project-specific reinterpretation.

## 3. Non-goals

- Do not train schema facts into Qwen as the primary knowledge store.
- Do not send the full Markdown corpus or full schema atlas to the model.
- Do not make embeddings, GBrain, or historical tickets authoritative live evidence.
- Do not infer physical SQL joins solely from an XStudio configuration relation.
- Do not replace the existing WIP=1 lifecycle, frozen proposal, bounded rework,
  deterministic publisher, auditing, or SQL safety rules.
- Do not expose arbitrary stored-procedure execution or database writes to workers.
- Do not introduce another vector database, knowledge service, registry database,
  queue, daemon, or lifecycle authority.
- Do not rewrite working typed tools or lifecycle procedures to make their names fit
  a new design.

## 4. Authority model

Knowledge remains separated into four planes:

| Plane | Contents | Authority |
|---|---|---|
| Structural atlas | databases, tables, views, columns, configured relations, SQL dependencies | Versioned snapshot; advisory until live validation |
| Curated domain knowledge | routes, identifier semantics, approved evidence recipes, canonical documents | Git-reviewed knowledge |
| Reusable operational knowledge | approved solution articles and GBrain document retrieval | Hypothesis with provenance |
| Ticket evidence | current Helpdesk and Xbatch rows plus audited action IDs | Live authority for the current claim |

`mem0` remains operational memory. It cannot contain ticket-specific facts and is
not part of the reusable KB index.

## 5. Extend the existing semantic atlas

Extend `Model_Bench/build_xstudio_semantic_atlas.py` and its existing checked-in
outputs. These remain the single versioned machine-readable structural registry.
The extended build consumes:

1. `XStudio_Helpdesk` schema, views, procedures, and Hermes runtime objects;
2. `XStudio_Xbatch` schema, views, procedures, and dependencies;
3. `XStudio_Configuration_Xbatch.dbo.XStudio_EntityRelations_Mst_Tbl`;
4. validated entity and attribute metadata needed to resolve relation IDs;
5. reviewed domain recipes and identifier aliases in `Knowledge/`;
6. approved Hermes solution articles, indexed separately as operational knowledge.

The registry records:

```text
registry_version
generated_on
source database/object
source snapshot/hash
node: database/schema/object/column/entity/attribute/domain/identifier
edge: CONFIGURATION_RELATION/VIEW_DEPENDS_ON/PROCEDURE_READS/
      PROCEDURE_WRITES/IDENTIFIER_BRIDGE/DOMAIN_SURFACE
edge provenance and verification status
procedure safety: READ_ONLY_REVIEWED/MUTATING/UNKNOWN_UNSAFE
```

Configuration relations are semantic navigation edges. They become approved SQL
join edges only when both endpoint objects/columns are validated and an explicit
join recipe is reviewed. Non-relational identifiers such as CSV heat allocations
remain explicit code-owned recipes.

The existing generated JSON and compact Markdown pages remain committed. A deterministic gate
fails if counts unexpectedly collapse, endpoints cannot be resolved, duplicate
identities appear, required domains lose all surfaces, or generated files differ
from the checked-in version.

No SQL registry tables are added unless a later measured runtime constraint proves
the checked-in atlas cannot serve this responsibility. The current scale does not
justify another persistence layer.

## 6. Extend the current GBrain/KB retriever

GBrain becomes the harness-owned retriever for unstructured and semi-structured
knowledge by extending `Model_Bench/kb_retrieval.py`. It is not exposed as an
unrestricted worker tool and does not replace that module's current deterministic
route and approved-solution logic.

Before enabling production hybrid retrieval:

- the `xstudio-knowledge` source is explicitly selected;
- LM Studio `text-embedding-nomic-embed-text-v1.5` remains 768-dimensional;
- stale embeddings are backfilled to 100% for embeddable chunks;
- skipped/flagged pages are reported explicitly;
- source sync, embedding coverage, and retrieval probes pass;
- an evaluation set demonstrates identifier, symptom, domain, and abstention cases.

The existing retriever calls GBrain through one bounded internal adapter and receives
at most three compact hits:

```json
{
  "kb_id": "...",
  "source_type": "...",
  "source_ref": "...",
  "source_version": "...",
  "title": "...",
  "excerpt": "...",
  "matched_terms": [],
  "why_retrieved": [],
  "retrieval_score": 0.0,
  "verification_required": true
}
```

GBrain failure, partial coverage, timeout, or low relevance causes an explicit
abstention. It cannot block deterministic atlas routing or ticket reconciliation.

Do not add Qdrant: GBrain's current PostgreSQL/pgvector store and the configured LM
Studio embedder already satisfy the retrieval requirement. Do not add an LLM query
expansion dependency; exact terms, lexical retrieval, embeddings, and deterministic
route boosts are sufficient until evaluation proves otherwise.

## 7. Extend deterministic ticket routing

Extend `deterministic_ticket_route()`, `_investigation_bundle()`, and
`_dispatch_route_context()` with this sequence:

```text
ticket-owned text and structured fields
  -> normalize exact identifiers and aliases
  -> score candidate domains using deterministic rules
  -> expand through registry relations and domain surfaces
  -> retrieve compact GBrain and approved-solution leads
  -> select one to three approved evidence recipes
  -> execute safe dispatch-time recipes
  -> emit the investigation context package
```

Route scoring must be explainable. Exact identifiers and exact technical terms
outrank semantic matches. Embedding similarity can boost a candidate but cannot be
the only reason for selecting a database action. Multiple plausible domains remain
visible rather than being forced into one route.

The planner must abstain from live recipe execution when required identifiers are
absent or ambiguous. It still returns the likely areas and the precise missing fact.

The result remains one investigation bundle rendered into the existing investigator
card. There is no new planner service or second dispatch format.

## 8. Investigation context contract

The investigator receives one compact structured package:

```json
{
  "registry_version": "...",
  "ticket": {},
  "identifiers": [],
  "candidate_domains": [],
  "relationship_neighborhood": [],
  "knowledge_hits": [],
  "prior_ticket_state": {},
  "recommended_recipes": [],
  "live_evidence": [],
  "missing_evidence": [],
  "allowed_next_tools": []
}
```

Every candidate domain states its score and reasons. Every live evidence item has
an audited `action_id`. Context is size-capped and deterministic. Raw procedure
definitions, broad schema dumps, and irrelevant ticket history are excluded.

During investigation, the model continues to call the existing small typed tools,
which resolve against the extended atlas. The bridge supplies database, run, ticket, validated object names,
and reviewed query templates whenever those values are deterministic. Repeated
semantic mistakes trigger argument repair, route narrowing, or explicit give-up;
they do not consume unbounded model turns.

## 9. Extend deterministic evidence recipes

Recipes remain reviewed, parameterized, read-only operations in
`xstudio_l2_tool_bridge.py`. Prefer extending its existing fixed-query functions.
Use a narrowly scoped read-only stored procedure only when it materially simplifies
multi-result/database work or makes the audit boundary safer. The model never
supplies procedure names or SQL for a recipe.

Initial recipe families must cover the domains present in the atlas/evaluation set,
not only EAF/LRF/CCM:

```text
heat execution and genealogy
work order and campaign
SAP API and posting
inventory and consumption
quality / inspection / result recording
delay and equipment events
material / batch / billet state
workflow and scheduler execution
Helpdesk lifecycle and prior actions
```

Each recipe declares identifiers, databases, surfaces, safety, maximum rows,
absence semantics, and claim guidance. A recipe is unavailable unless all referenced
objects and columns exist in the active registry version.

Do not create one macro per table. Add a domain macro only when multiple ticket
fixtures share the same identifiers, surfaces, and absence semantics.

## 10. Extend the existing review contract

Keep the independent reviewer. Better routing reduces review cost but does not prove
causality, resolution, applicability, or safe customer wording.

The existing frozen reviewer card additionally receives:

- the frozen proposal;
- the exact registry version used by the investigator;
- investigator evidence references;
- a deterministic claim-to-evidence validation result;
- independently collected minimal evidence for the core material claims;
- compact GBrain contradiction/applicability hits when available.

Mechanical gates run before the reviewer:

```text
required proposal fields
response-type consistency
same-run/same-ticket evidence provenance
all material VERIFIED claims have evidence
referenced registry objects still valid
resolution workflow binding available
```

The reviewer approves or rejects semantic sufficiency. It does not publish. A normal
review rejection remains bounded rework and never creates an L3 row.

No review bypass is introduced in this version. Any future automatic approval must
be limited to a separately evaluated, mechanically provable ticket class and first
run in shadow-review mode.

## 11. Stored-procedure boundary and staleness audit

Retain the currently used lifecycle and auditing procedures. Before changing any SP,
trace its current Python/bridge caller, compare the numbered SQL source with the live
definition, and classify it as active, compatibility-only, or unused. Add or revise
only read-only discovery/context procedures needed by an approved recipe. Updating a
procedure is insufficient unless the existing bridge and route path invoke it through
a tested typed contract.

Normal worker access continues through:

```text
Hermes_L2_Get_Ticket_Context_Usp
Hermes_L2_Find_SQL_Objects_Usp
Hermes_L2_Get_SQL_Object_Definition_Usp
Hermes_L2_Execute_SQL_Usp (harness-guarded read path)
Hermes_L2_Update_SQL_Action_Evidence_Usp
Hermes_L2_Get_Run_Actions_Usp
Hermes_L2_Save_Investigation_State_Usp
```

Lifecycle mutation continues unchanged through the central runtime and existing claim,
recovery, fail, and publish procedures. Convenience and compatibility procedures
remain outside the normal model path.

## 12. Failure and self-healing behavior

- Registry build failure keeps the last verified registry active.
- Registry version mismatch fails closed for recipe execution and permits only live
  discovery with an explicit warning.
- GBrain failure degrades to deterministic atlas/lexical routing and records an
  abstention; it never blocks lifecycle reconciliation.
- Missing relation endpoints are quarantined from recipes and reported.
- Missing live recipe surfaces disable only that recipe/domain path.
- Retrieval and recipe failures are audited with reason, version, duration, and
  fallback used.
- The two-minute scout remains the lifecycle backstop and uses the existing dependency
  gate to check knowledge health before claiming new work.
- Claims pause when no verified registry exists, required worker dependencies fail,
  or mandatory route coverage falls below the configured gate.

No separate knowledge watchdog is introduced. Existing scout/trace/activity plumbing
owns the new health and retrieval events.

## 13. Observability

Record per run:

```text
registry version and age
route candidates and selected recipes
GBrain query, hit IDs, abstention, coverage and latency
recipe calls, action IDs, row counts and failures
context size and truncation
model tool calls and repair events
review evidence reuse versus independent reads
approval/rejection reason and review cycles
publish outcome
```

System KPIs include route coverage, identifier extraction accuracy, retrieval
precision/recall, abstention correctness, recipe success, unsupported-domain rate,
evidence completeness, reviewer rejection rate, rework rate, resolution rate,
time/compute per ticket, and failures by layer.

## 14. Verification and rollout

Testing proceeds from fixtures to live shadow validation:

1. extend existing atlas tests with configuration-relation resolution;
2. deterministic rebuild/hash/count tests;
3. ticket-to-domain golden evaluation cases, including multi-domain and abstention;
4. GBrain retrieval relevance, provenance, and abstention tests;
5. recipe schema, safety, result-bound, and missing-surface tests;
6. reviewer evidence/provenance regression tests;
7. full existing lifecycle and typed-tool suites;
8. deploy through the existing idempotent WSL deployment script with claims paused;
9. shadow planner against historical real tickets without publication;
10. compare proposed routes/evidence with known outcomes;
11. enable one natural-ticket live run at WIP=1;
12. verify SQL, Kanban, observability, Helpdesk postconditions, and self-healing.

Acceptance requires:

- 100% embedding coverage for embeddable GBrain chunks;
- deterministic registry reproduction from the same sources;
- no unresolved relation endpoint used by a recipe;
- every evaluation ticket returns the expected area or a correct abstention;
- malformed retrieval/tool calls never reach SQL or consume live-query budget;
- no model-created database transport;
- investigator and reviewer use the bounded context contracts;
- lifecycle and publication invariants remain unchanged;
- one naturally arriving ticket completes with persisted evidence and observability.

## 15. Incremental delivery slices

1. Extend the existing atlas and schema allowlist with configuration relations.
2. Repair GBrain coverage and extend `kb_retrieval.py` with bounded retrieval.
3. Extend the existing route/bundle functions and their golden cases.
4. Add only evidence-backed domain recipes to the existing bridge/toolset.
5. Enrich the existing reviewer package and mechanical gates.
6. Deploy with the existing scripts, shadow historical tickets, then validate one
   naturally arriving ticket and its operational KPIs.

Each slice is independently testable and committed. Changes are additive within the
current owners until live validation passes. Compatibility is retained only where a
real current caller requires it; do not add a broad fallback switch that can silently
hide a broken new path.
