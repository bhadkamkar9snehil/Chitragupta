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

## 2. Non-goals

- Do not train schema facts into Qwen as the primary knowledge store.
- Do not send the full Markdown corpus or full schema atlas to the model.
- Do not make embeddings, GBrain, or historical tickets authoritative live evidence.
- Do not infer physical SQL joins solely from an XStudio configuration relation.
- Do not replace the existing WIP=1 lifecycle, frozen proposal, bounded rework,
  deterministic publisher, auditing, or SQL safety rules.
- Do not expose arbitrary stored-procedure execution or database writes to workers.

## 3. Authority model

Knowledge remains separated into four planes:

| Plane | Contents | Authority |
|---|---|---|
| Structural atlas | databases, tables, views, columns, configured relations, SQL dependencies | Versioned snapshot; advisory until live validation |
| Curated domain knowledge | routes, identifier semantics, approved evidence recipes, canonical documents | Git-reviewed knowledge |
| Reusable operational knowledge | approved solution articles and GBrain document retrieval | Hypothesis with provenance |
| Ticket evidence | current Helpdesk and Xbatch rows plus audited action IDs | Live authority for the current claim |

`mem0` remains operational memory. It cannot contain ticket-specific facts and is
not part of the reusable KB index.

## 4. Canonical knowledge registry

Create one versioned, machine-readable registry generated from:

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

The generated JSON and compact Markdown pages are committed. A deterministic gate
fails if counts unexpectedly collapse, endpoints cannot be resolved, duplicate
identities appear, required domains lose all surfaces, or generated files differ
from the checked-in version.

## 5. GBrain contract

GBrain is the harness-owned retriever for unstructured and semi-structured
knowledge. It is not exposed as an unrestricted worker tool.

Before enabling production hybrid retrieval:

- the `xstudio-knowledge` source is explicitly selected;
- LM Studio `text-embedding-nomic-embed-text-v1.5` remains 768-dimensional;
- stale embeddings are backfilled to 100% for embeddable chunks;
- skipped/flagged pages are reported explicitly;
- source sync, embedding coverage, and retrieval probes pass;
- an evaluation set demonstrates identifier, symptom, domain, and abstention cases.

The harness calls a bounded adapter and receives at most three compact hits:

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

## 6. Deterministic ticket planning

Add a harness-owned planner with this sequence:

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

## 7. Investigation context contract

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

During investigation, the model can call small typed tools that resolve against the
same registry. The adapter supplies database, run, ticket, validated object names,
and reviewed query templates whenever those values are deterministic. Repeated
semantic mistakes trigger argument repair, route narrowing, or explicit give-up;
they do not consume unbounded model turns.

## 8. Deterministic evidence recipes

Recipes are reviewed, parameterized, read-only operations. The preferred
implementation is small bridge functions backed by fixed SQL or narrowly scoped
read-only stored procedures. The model never supplies procedure names or SQL for a
recipe.

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

## 9. Review contract

Keep the independent reviewer. Better routing reduces review cost but does not prove
causality, resolution, applicability, or safe customer wording.

The reviewer receives:

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

## 10. Stored-procedure boundary

Retain the currently used lifecycle and auditing procedures. Add or revise only
read-only discovery/context procedures needed by approved recipes. Updating a
procedure is insufficient unless the bridge and planner invoke it through a tested
typed contract.

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

Lifecycle mutation continues through the central runtime and existing claim,
recovery, fail, and publish procedures. Convenience and compatibility procedures
remain outside the normal model path.

## 11. Failure and self-healing behavior

- Registry build failure keeps the last verified registry active.
- Registry version mismatch fails closed for recipe execution and permits only live
  discovery with an explicit warning.
- GBrain failure degrades to deterministic atlas/lexical routing and records an
  abstention; it never blocks lifecycle reconciliation.
- Missing relation endpoints are quarantined from recipes and reported.
- Missing live recipe surfaces disable only that recipe/domain path.
- Retrieval and recipe failures are audited with reason, version, duration, and
  fallback used.
- The two-minute scout remains the lifecycle backstop and also checks knowledge
  health before claiming new work.
- Claims pause when no verified registry exists, required worker dependencies fail,
  or mandatory route coverage falls below the configured gate.

## 12. Observability

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

## 13. Verification and rollout

Testing proceeds from fixtures to live shadow validation:

1. registry parser and relation-resolution unit tests;
2. deterministic rebuild/hash/count tests;
3. ticket-to-domain golden evaluation cases, including multi-domain and abstention;
4. GBrain retrieval relevance, provenance, and abstention tests;
5. recipe schema, safety, result-bound, and missing-surface tests;
6. reviewer evidence/provenance regression tests;
7. full existing lifecycle and typed-tool suites;
8. deploy to WSL with claims paused;
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

## 14. Delivery slices

1. Registry and relation atlas.
2. GBrain health, complete embedding, bounded adapter, and retrieval evaluation.
3. Deterministic planner and investigation bundle v2.
4. Expanded domain recipes and typed investigation retrieval.
5. Reviewer evidence package and mechanical pre-review gates.
6. Deployment, shadow evaluation, natural-ticket validation, and operational KPIs.

Each slice is independently testable and committed. The old bundle remains available
behind a temporary rollback switch until the v2 bundle completes live validation;
the switch is removed after cutover so failures remain visible rather than silently
falling back forever.
