# Chitragupta Knowledge Base Implementation Plan

Status: **Implementation contract**  
Branch: `main`  
Baseline validated locally: 2026-09-05  
Owner: Chitragupta / Hermes L2 support pipeline

---

## 1. Purpose

This document defines the target architecture and phased implementation plan for Chitragupta's knowledge system.

The objective is not to create a generic vector database or to dump ticket history into embeddings. The objective is to build a governed support knowledge system in which:

- authoritative knowledge remains authoritative;
- reusable support knowledge has a lifecycle and measurable quality;
- live SQL evidence remains the final source of truth for ticket-specific facts;
- ticket history, schema discovery, mem0 and reusable KB retrieval remain distinct;
- Qdrant is a rebuildable search index, never the source of truth;
- retrieval can abstain when no sufficiently good match exists;
- every retrieved item carries provenance;
- approved resolutions improve the knowledge system without automatically creating duplicate or untrusted KB articles.

This plan supersedes ad-hoc assumptions that `mem0`, ticket history, solution history, schema discovery or Qdrant are themselves "the KB".

---

## 2. Architectural invariants

The following are non-negotiable unless this document is explicitly revised.

### 2.1 Knowledge classes remain separate

| Knowledge class | Canonical store | Purpose | General reusable KB? | Ticket proof? |
|---|---|---|---:|---:|
| Verified domain/reference knowledge | Git `Knowledge/` | How XStudio/Hermes works | Yes | Sometimes |
| Reusable solution knowledge | SQL `Hermes_Solution_Article_Mst_Tbl` | Known issues, diagnostics, how-to guidance | Yes, after approval | No; applicability must be verified |
| Problem management | SQL `Hermes_Problem_Mst_Tbl` | Group recurring incidents under common root cause | Indirectly | No |
| Ticket/run ledger | SQL run/ticket history | Episodic state for one incident | No | Yes for that ticket's historical investigation |
| Live operational evidence | XStudio SQL | Current ticket-specific facts | No | **Yes** |
| Schema/catalog | schema allowlist / live SQL metadata | Determine what DB objects actually exist | No vector retrieval | Yes for schema |
| Agent operational memory | mem0 `hermes_l2` | Learned operating heuristics | No | No |
| Search index | Qdrant `hermes_kb_v1` | Retrieve relevant approved knowledge | No | No |

### 2.2 Qdrant is an index, not the source of truth

Every point in `hermes_kb_v1` must be reproducible from an authoritative source and must carry enough provenance to re-fetch that source.

Deleting and rebuilding `hermes_kb_v1` must never destroy canonical knowledge.

### 2.3 Live evidence outranks historical knowledge

If a KB article, prior ticket, mem0 lesson or previous investigation conflicts with current live SQL or a verified authoritative reference, current authoritative evidence wins.

### 2.4 A resolved ticket is not automatically a KB article

Post-resolution knowledge handling must choose one of:

```text
REUSE_EXISTING
UPDATE_EXISTING
CREATE_CANDIDATE
NONE
```

`RESOLUTION -> CREATE NEW ARTICLE` is explicitly rejected as the permanent model.

### 2.5 Retrieval must be able to abstain

`NO GOOD KB MATCH` is a valid and desirable result.

False positive reuse is initially considered more dangerous than a missed KB hit because a missed hit causes more investigation, while a wrong known-issue match can produce a wrong support answer.

### 2.6 Schema retrieval remains deterministic

Do not vector-index the schema to decide whether a table/view/column exists.

Schema discovery remains:

```text
ticket/symptom
  -> deterministic token/object discovery
  -> schema_allowlist / sys.* / known view catalog
  -> validated SQL
```

Reusable knowledge retrieval is a different subsystem.

---

## 3. Target knowledge architecture

```text
                          AUTHORITATIVE SOURCES
                          =====================

             Git                                    SQL Server
      Knowledge/*.md                         Solution Articles
      manifest/routes                        Problem Management
      verified workflows                     reuse/outcome telemetry
             |                                      |
             +------------------+-------------------+
                                |
                          KB INDEXER
                                |
                                v
                       Qdrant: hermes_kb_v1
                     dense + sparse/BM25 vectors
                       provenance in payload
                                |
                                v
                        KB RETRIEVAL SERVICE
                                |
                   +------------+------------+
                   |                         |
            pre-investigation           post-resolution
             symptom search             dedupe/curation
                   |                         |
                   v                         v
              investigator              KB lifecycle
                   |
                   +-- prior ticket ledger
                   +-- deterministic schema discovery
                   +-- LIVE SQL VERIFICATION
                                |
                                v
                             reviewer
                                |
                                v
                       deterministic publisher
```

Separate from this:

```text
mem0 / hermes_l2
  -> operational heuristics only

Ticket/run history
  -> episodic knowledge for one incident only

schema_allowlist / sys.*
  -> deterministic schema discovery only
```

---

## 4. Knowledge types

`Hermes_Solution_Article_Mst_Tbl` should support a controlled `KnowledgeType`.

Initial allowed types:

### 4.1 `KnownIssue`

A reusable symptom -> root cause -> resolution pattern.

Example:

> SAP posting exists, no material document appears, and a specific SAP business rejection is present.

### 4.2 `Diagnostic`

Reusable investigation procedure where the value is knowing how to distinguish causes rather than applying one fixed resolution.

Example:

> Determine whether a missing billet is an inventory, genealogy or transfer-state issue.

### 4.3 `HowTo`

A reusable supported operating procedure.

Example:

> Safely retry a supported transaction through the approved stored procedure.

### 4.4 What remains Git reference knowledge

The following should normally stay in `Knowledge/*.md`, not be duplicated into solution articles:

- architecture;
- workflow/state-machine definitions;
- table/view semantics;
- supported SQL write model;
- reference formulas;
- general product behavior;
- stable routing/reference documentation.

---

## 5. Solution article lifecycle

Replace the effective boolean lifecycle (`IsActive`) with an explicit lifecycle while preserving `IsActive` for compatibility during migration.

Target states:

```text
Candidate
Approved
NeedsReview
Superseded
Deprecated
```

### 5.1 Candidate

Created from a verified resolved incident when no suitable existing article represents the generalizable pattern.

Rules:

- not included in normal investigator retrieval;
- included in post-resolution duplicate/curation search;
- may be reviewed manually or promoted by repeated independent evidence;
- must retain source ticket/run provenance.

### 5.2 Approved

Production-retrievable reusable knowledge.

### 5.3 NeedsReview

Knowledge whose trust has weakened, for example:

- reuse failed;
- a ticket reopened after application;
- a dependent SQL object changed materially;
- conflicting verified evidence was found;
- applicability is unclear after environment/version change.

Normal automatic retrieval should exclude it or strongly suppress it.

### 5.4 Superseded

Retained for history but replaced by a newer article.

Requires `SupersededBySolutionID` or equivalent relationship.

### 5.5 Deprecated

Known to be invalid or obsolete. Never retrieved in normal production searches.

---

## 6. Promotion policy

Initial conservative promotion policy:

```text
one verified resolved ticket
    -> Candidate

second independent verified matching resolution
    -> eligible for Approved

explicit authorized human/reviewer approval
    -> may promote Candidate to Approved earlier
```

This policy may later be tuned from observed data, but single-ticket automatic approval is not allowed.

---

## 7. Target solution article model

The existing fields remain useful but require additional governance and applicability metadata.

### 7.1 Existing core content

- `ID`
- `Title`
- `ProblemSummary`
- `RootCause`
- `ResolutionSteps`
- `RootCauseCategoryID`
- `Route`
- `RelatedViewsJson`
- `Tags`
- `UsageCount` (legacy/compatibility only after telemetry migration)
- audit columns

### 7.2 New identity/lifecycle fields

Recommended additions:

```text
KnowledgeType               varchar(30)
ArticleStatus               varchar(30)
CanonicalKey                varchar(250)
RevisionNo                  int
ContentHash                 varchar(64)
SourceTicketID              varchar(36)
SourceRunID                 varchar(36)
SupersedesSolutionID        varchar(36) NULL
SupersededBySolutionID      varchar(36) NULL
ApprovedOn                  datetime NULL
ApprovedBy                  varchar(200) NULL
LastVerifiedOn              datetime NULL
LastVerifiedRunID           varchar(36) NULL
```

### 7.3 Applicability fields

Prefer JSON for dimensions that will evolve:

```text
ApplicabilityJson
NegativeIndicatorsJson
VerificationJson
EvidenceJson
```

Suggested `ApplicabilityJson` shape:

```json
{
  "source_systems": ["XStudio_Xbatch"],
  "sites": ["Sohar"],
  "modules": ["SMS"],
  "routes": ["heat_execution"],
  "versions": [],
  "required_conditions": [],
  "entity_types": ["HeatNo"]
}
```

Suggested `NegativeIndicatorsJson` shape:

```json
{
  "not_applicable_when": [
    "No API transaction exists",
    "Work order is cancelled",
    "SAP returned an explicit different business rejection"
  ]
}
```

Negative applicability is first-class because autonomous agents need strong evidence for when **not** to reuse a plausible historical fix.

### 7.4 Diagnostic structure

Do not rely only on a prose `ResolutionSteps` field. The article should eventually distinguish:

```text
Symptom
RootCause
DiagnosticSteps
ResolutionSteps
VerificationSteps
ExpectedResult
```

Migration may initially store some of these in JSON if changing the table shape all at once is undesirable.

---

## 8. Problem management remains separate

`Hermes_Problem_Mst_Tbl` answers:

> Why do these incidents keep happening?

A solution article answers:

> How do we recognize, diagnose, explain or resolve this pattern?

Do not collapse the two.

Add a relationship table when needed:

```text
Hermes_Problem_Solution_Link_Tbl
```

Conceptual fields:

```text
ProblemID
SolutionID
RelationshipType
CreatedOn
CreatedBy
IsDeleted
```

One recurring Problem may have multiple articles, e.g. a Diagnostic plus a temporary KnownIssue workaround.

---

## 9. Deduplication and canonical identity

Deduplication must occur before creation.

### 9.1 Exact duplicate

Use `ContentHash` over normalized reusable content.

### 9.2 Logical duplicate

Use `CanonicalKey` derived from stable dimensions such as:

```text
knowledge type
+ route/module
+ normalized symptom class
+ root-cause category
```

The precise key generator must be deterministic and versioned.

### 9.3 Near duplicate

Search Candidate + Approved knowledge using the same hybrid retrieval system.

Near similarity produces a curation suggestion only:

```text
possible_duplicate_of = solution:<ID>
```

Vector similarity must never auto-merge articles.

---

## 10. Reuse and outcome telemetry

`UsageCount` is not sufficient because retrieval, selection and successful application are different events.

### 10.1 Add retrieval telemetry

Recommended table:

```text
Hermes_KB_Retrieval_Trn_Tbl
```

Suggested fields:

```text
ID
TicketID
RunID
QueryPhase              -- PRE_INVESTIGATION | POST_RESOLUTION
QueryHash
KBID
SourceType
Rank
DenseRank
SparseRank
FusionScore
RouteMatch
ScopeMatch
RetrievedOn
Selected
SelectionDisposition
CreatedOn
```

### 10.2 Evolve ticket-solution reuse outcome

The existing ticket/solution link should distinguish actual usage:

```text
UseDisposition
  Applied
  UsedForDiagnosis
  ReferenceOnly
  RejectedNotApplicable

OutcomeStatus
  Pending
  Success
  Failed
  Unknown

OutcomeReason
OutcomeOn
```

`WasHelpful` can remain during migration but should not be the final outcome model.

### 10.3 Derived health metrics

Do not store only opaque counters. Derive/report:

```text
retrieved_count
selected_count
applied_count
verified_success_count
failed_reuse_count
reopened_after_use_count
rejected_not_applicable_count
```

These can feed a view/materialized reporting layer.

---

## 11. Separate relevance from trust

Retrieval score means similarity/relevance, not truth.

Each returned hit should expose distinct dimensions where available:

```text
relevance
scope/applicability match
article lifecycle state
freshness
successful reuse history
failed reuse history
source authority
```

Do not introduce one opaque `AIConfidence` number.

---

## 12. Two retrieval phases

### 12.1 PRE_INVESTIGATION retrieval

Question being answered:

> Have we seen a sufficiently similar symptom or diagnostic pattern before?

Primary query inputs:

```text
BriefDetails
Description
SourceSystem
Area/category context
strong entity TYPES
exact technical terms/error codes/object names
route candidates
```

Do **not** let a model-generated `SuspectedCause` dominate the query because it creates confirmation bias.

Unique instance values such as one HeatNo/GUID/TicketID should not dominate semantic similarity.

Expected retrievable types:

```text
KnownIssue
Diagnostic
HowTo
verified Git reference sections
```

### 12.2 POST_RESOLUTION retrieval

Question being answered:

> Does this verified root-cause/resolution already exist in reusable knowledge?

Inputs:

```text
verified root cause
verified resolution
relevant module/component
related DB objects
applicability
root-cause category
```

Output decision:

```text
REUSE_EXISTING
UPDATE_EXISTING
CREATE_CANDIDATE
NONE
```

These two searches must not be treated as the same retrieval call.

---

## 13. Authoritative Git knowledge

Verified reference knowledge remains in `Knowledge/`.

Each retrievable reference document should gradually adopt metadata/frontmatter such as:

```yaml
kb_id: xbatch.performance.delay-analysis
title: Delay Analysis Model
type: domain_reference
status: approved
routes:
  - performance
source_system: XStudio_Xbatch
authority: verified_internal
verified_on: 2026-09-05
```

### 13.1 Chunk by semantic section, not arbitrary token windows

Index headings/meaningful sections:

```text
Knowledge/sohar-sms-event-workflows.md
  -> EAF event sequence
  -> LRF event sequence
  -> CCM event sequence
  -> Billets Cast Count / data insert flow
```

Each indexed section must retain a source reference such as:

```text
Knowledge/sohar-sms-event-workflows.md#billets-cast-count--data-insert-flow
```

The Markdown file remains canonical.

---

## 14. Canonical routing/catalog source

`Knowledge/manifest.json` is the canonical machine-readable routing/catalog source.

Rules:

- route names are defined once;
- identifier routing is defined once;
- route -> skill mapping is defined once;
- route -> Git knowledge documents is defined once;
- route -> preferred live SQL leads is defined once;
- `task-router.md` must not become a separately maintained divergent machine configuration.

Target end state:

- `manifest.json` is authoritative structured configuration;
- human-readable router sections are generated or mechanically validated against it;
- local validation is required before deployment;
- GitHub-hosted CI is not a dependency for this project.

---

## 15. Qdrant target design

Use the existing Qdrant server with separate collections:

```text
hermes_l2
  -> mem0 operational memory

hermes_kb_v1
  -> reusable KB retrieval index
```

Never mix these collections.

### 15.1 Vector model

Each KB point should support:

```text
dense
sparse
```

Initial target:

- dense: existing Nomic embedding path, 768 dimensions unless deployment testing changes it;
- sparse: local BM25-compatible sparse representation;
- fusion: plain Reciprocal Rank Fusion (RRF).

Do not add weighted fusion or reranking before an evaluation set demonstrates the need.

### 15.2 Hard filters

Safe hard filters include:

```text
ArticleStatus = Approved
source system/site applicability when explicitly known
validity/deprecation state
knowledge type when explicitly requested
```

Do not hard-filter exclusively by inferred route. Route can be wrong and should be a retrieval boost/preference rather than an absolute barrier.

### 15.3 Qdrant payload schema

Every indexed item should carry at least:

```text
kb_id
source_type
source_ref
source_version
content_hash
knowledge_type
article_status
title
routes
source_systems
sites
modules
authority
verified_on
successful_reuses
failed_reuses
```

SQL solution article provenance should include:

```text
solution_id
revision
source_ticket_id
source_run_id
```

Git provenance should include:

```text
file path
heading/section
Git commit SHA
```

### 15.4 Collection versioning

Use versioned collections:

```text
hermes_kb_v1
hermes_kb_v2
...
```

Changing embedding model, dimensions, sparse model, payload contract or chunking strategy requires a deliberate index version/rebuild rather than silently mixing incompatible representations.

Maintain index metadata containing:

```text
index version
dense model
dense dimensions
sparse model
chunking strategy version
payload schema version
created_on
source revision
```

---

## 16. KB indexing pipeline

Target indexer responsibilities:

```text
read authoritative Git docs
read Approved SQL solution articles
normalize content
split Git docs by semantic heading
build deterministic kb_id/source_ref
calculate content hash
create dense vector
create sparse vector
write/update Qdrant point
remove/deactivate points whose authoritative source is no longer retrievable
emit indexing report
```

The indexer must be idempotent.

A source's `content_hash` should determine whether re-embedding is required.

No ticket transcript dumping into `hermes_kb_v1`.

---

## 17. Retrieval pipeline

Target first-stage retrieval:

```text
normalize ticket query
   |
extract exact technical terms
   |
derive deterministic route candidates
   |
apply reliable metadata filters
   |
+---------------------------+
|                           |
dense search           sparse/BM25 search
|                           |
+-------------+-------------+
              |
             RRF
              |
       relevance gate
              |
      provenance-rich hits
              |
     abstain if insufficient
```

Initially return top **3** compact hits rather than pushing five full articles into the investigator context.

Full article content should be fetched only when the investigator needs it.

This reduces anchoring and context consumption for the local 9B model.

---

## 18. Retrieval result contract

Target hit shape:

```json
{
  "kb_id": "solution:abc",
  "source_type": "solution_article",
  "source_ref": "Hermes_Solution_Article_Mst_Tbl:abc",
  "title": "...",
  "knowledge_type": "KnownIssue",
  "article_status": "Approved",
  "symptom_summary": "...",
  "applicability": {},
  "why_retrieved": [
    "semantic symptom match",
    "exact UsageDecision term match",
    "preferred route api_transaction"
  ],
  "last_verified_on": "...",
  "successful_reuses": 4,
  "failed_reuses": 0,
  "verification_required": true
}
```

The retriever must distinguish:

```text
retrieval relevance
from
source trust/applicability
```

---

## 19. Investigation bundle contract

Target `--investigate-bundle` structure:

```json
{
  "ticket": {},
  "identifiers": {},
  "route_candidates": [],

  "kb": {
    "hits": [],
    "abstained": false,
    "abstention_reason": null
  },

  "ticket_history": {
    "prior_ledger": {},
    "prior_attempts": []
  },

  "schema_candidates": []
}
```

The bundle deliberately keeps four concepts separate:

```text
KB candidates
same-ticket history
schema candidates
live evidence gathered during investigation
```

Do not merge them into one undifferentiated context block.

---

## 20. Knowledge-use workflow during investigation

When an investigator receives a KB hit:

1. compare the ticket symptom with the article symptom;
2. check applicability/negative indicators;
3. perform the article's diagnostic verification against current live SQL or verified reference knowledge;
4. reject the article explicitly if current evidence contradicts it;
5. only then apply/reuse the resolution;
6. record SolutionID/KBID in structured completion metadata when materially used.

A KB hit is a hypothesis/lead, never proof.

---

## 21. Post-resolution curation workflow

After reviewer approval and successful deterministic publication:

```text
verified resolution
    |
POST_RESOLUTION retrieval
    |
+-------------------------------+
|               |               |
exact/strong   near existing    no reusable pattern
match          match            or one-off case
|               |               |
REUSE          UPDATE or        NONE
EXISTING       CREATE_CANDIDATE
```

### 21.1 REUSE_EXISTING

- link existing article to the ticket/run;
- do not create a duplicate;
- create reuse outcome record;
- increment derived success only after outcome is known.

### 21.2 UPDATE_EXISTING

Used when the existing reusable pattern is correct but this resolution contributes verified new applicability/diagnostic/verification information.

Updates should create a new revision/history trail rather than silently overwriting provenance.

### 21.3 CREATE_CANDIDATE

Create only when:

- the resolution is verified;
- the finding is generalizable;
- no existing article adequately represents it.

### 21.4 NONE

Use for:

- one-off data correction;
- requester-specific issue;
- non-generalizable isolated event;
- administrative resolution;
- cases where durable KB content would add noise.

---

## 22. Reopen and failed-reuse feedback

When an article was applied and the ticket subsequently reopens or verification fails:

```text
reuse outcome -> Failed/Reopened
article health -> recalculate
```

Repeated verified failures should transition:

```text
Approved -> NeedsReview
```

Do not automatically delete or rewrite the article.

---

## 23. Dependency-aware freshness

Where feasible, an article should record the authoritative objects it depends on.

For SQL objects, capture at verification time:

```text
database
schema
object name
object type
modify_date
definition hash when available
```

If a dependency later changes materially:

```text
article -> NeedsReview candidate
```

For Git knowledge:

- record source commit SHA;
- record content hash;
- reindex when the authoritative section changes.

This is preferred over arbitrary blanket review intervals.

---

## 24. mem0 scope reduction

`hermes_l2` mem0 is not the KB.

Target mem0 contents:

- genuine learned operating heuristics;
- non-authoritative lessons that improve tool use;
- temporary operational discoveries worth recalling across attempts.

Move out of mem0 over time:

- fixed interpreter paths;
- fixed server/database configuration;
- response-type enum/policy;
- mandatory workflow rules;
- domain-specific product truth;
- canonical DB relationships;
- known diagnostic facts that belong in Approved KB/reference knowledge.

Stable deployment facts belong in config/dispatcher/skills.

Verified domain facts belong in Git or SQL KB.

Per-ticket findings belong in the ledger.

Future repeated mem0 lessons may be candidates for promotion into canonical documentation/KB, but promotion must be explicit.

---

## 25. Evaluation dataset

Create:

```text
Knowledge/eval/kb_retrieval_cases.jsonl
```

Case format:

```json
{
  "case_id": "performance-delay-001",
  "phase": "PRE_INVESTIGATION",
  "query": "...",
  "context": {},
  "expected_routes": ["performance"],
  "expected_kb_ids": ["solution:..."],
  "forbidden_kb_ids": [],
  "should_abstain": false
}
```

Required case categories:

1. clear known issue;
2. paraphrased known issue;
3. exact technical identifier/error term;
4. cross-domain ticket;
5. broad route but wrong article;
6. one generic shared word;
7. no relevant KB answer;
8. stale/deprecated article exclusion;
9. wrong-site/wrong-module applicability exclusion;
10. post-resolution duplicate detection.

---

## 26. Retrieval metrics

Initial metrics:

```text
Route accuracy
Recall@3
Precision@3
MRR@3
No-answer precision
False-known-issue rate
Wrong-scope retrieval rate
Deprecated/stale retrieval rate
Duplicate-solution rate
```

Operational outcome metrics:

```text
KB-hit-to-selection rate
successful reuse rate
failed reuse rate
reopen-after-reuse rate
average evidence queries with useful KB hit
average investigation time with/without useful KB hit
```

Initial optimization priority:

1. minimize false-known-issue matches;
2. preserve strong no-answer behavior;
3. improve Recall@3;
4. only then tune ranking sophistication.

---

## 27. Deferred techniques

Do **not** implement these until the basic architecture is working and evaluation shows a need:

- GraphRAG;
- Neo4j/knowledge graph;
- embeddings over all historical tickets;
- raw ticket transcript indexing;
- cross-encoder/late-interaction reranking;
- weighted RRF;
- LLM-generated hidden confidence scores;
- automatic semantic article merging;
- Qdrant as canonical storage.

---

# 28. Phased implementation roadmap

The order below is mandatory unless a blocking dependency is discovered.

## Phase 0 — Baseline and safety

Status: **current baseline substantially complete / locally validated**.

Existing baseline includes:

- single-board parent-gated investigator/reviewer workflow;
- one dispatch-time investigation bundle;
- deterministic schema narrowing;
- same-ticket ledger carry-forward;
- interim conservative lexical KB retriever;
- route-only retrieval prevented;
- abstention supported;
- provenance-bearing SolutionID returned;
- manifest/task-router aligned;
- local validation preferred over GitHub-hosted CI.

Exit criteria:

- local validation passes;
- no stale live workflow instructions;
- no duplicate context assembly in `ticket_scout.py`;
- retrieval baseline demonstrably abstains on weak matches.

---

## Phase 1 — Fix the SQL knowledge lifecycle

**Goal:** stop polluting the KB before introducing more powerful retrieval.

Implement:

1. schema migration for lifecycle/identity/provenance fields;
2. `KnowledgeType`;
3. `ArticleStatus`;
4. `CanonicalKey`;
5. `ContentHash`;
6. source ticket/run provenance;
7. applicability/negative-indicator/evidence/verification metadata;
8. explicit status constraints/indexes;
9. compatibility with existing articles.

Change publisher behavior:

```text
RESOLUTION
  != unconditional create article
```

Initially, if post-resolution curation is not yet implemented, default new reusable findings to `Candidate`, never `Approved`.

### Phase 1 acceptance criteria

- a resolved ticket can publish without creating an Approved article;
- existing Approved articles remain readable;
- Candidate articles are excluded from normal investigator retrieval;
- each new article has source ticket/run provenance;
- duplicate-safe canonical identity fields exist;
- rollback SQL is documented.

---

## Phase 2 — Reuse/outcome telemetry

Implement:

- `Hermes_KB_Retrieval_Trn_Tbl`;
- richer ticket-solution use/outcome state;
- retrieval logging;
- article selection/rejection logging;
- successful/failed/reopened reuse outcome updates;
- reporting views.

### Phase 2 acceptance criteria

For one ticket we can answer independently:

- which KB hits were retrieved;
- their rank;
- which one was selected;
- whether it was applied;
- whether the ticket was ultimately resolved;
- whether it later reopened.

`UsageCount` is no longer used as a proxy for quality.

---

## Phase 3 — Post-resolution curation and dedupe

Implement `POST_RESOLUTION` knowledge decision logic:

```text
REUSE_EXISTING
UPDATE_EXISTING
CREATE_CANDIDATE
NONE
```

Build deterministic exact/logical dedupe first:

- ContentHash;
- CanonicalKey.

Then use the interim lexical retriever to identify near-duplicate candidates until Qdrant is ready.

### Phase 3 acceptance criteria

- repeated identical resolutions link the same article rather than create duplicates;
- one-off fixes can explicitly produce `NONE`;
- new generalizable material is Candidate by default;
- existing article update retains revision/provenance history;
- duplicate rate is measurable.

---

## Phase 4 — Normalize authoritative Git knowledge

Add metadata/frontmatter incrementally to the verified documents actually used by current routes.

Do not rewrite all documentation at once.

Start with:

- `sohar-sms-event-workflows.md`;
- `xbatch-investigation-surfaces.md`;
- `view_catalog.md`;
- `sql-write-model.md`;
- `helpdesk-workflow-binding.md`;
- Hermes runtime reference docs.

Implement a local validator for:

- unique `kb_id`;
- valid route names;
- valid status/type values;
- real referenced files/anchors where practical;
- required provenance metadata.

### Phase 4 acceptance criteria

- every indexed Git section can map back to a stable `kb_id` and file/section;
- no need to embed entire documents as opaque blobs;
- manifest remains the canonical routing catalog.

---

## Phase 5 — Build `hermes_kb_v1`

Implement Qdrant collection/index metadata and idempotent indexer.

Index only:

```text
Approved SQL solution articles
Approved/verified Git knowledge sections
```

Do not index Candidate, NeedsReview, Superseded or Deprecated articles into the normal searchable production set.

Implement:

- dense vectors;
- sparse/BM25 vectors;
- payload indexes for lifecycle/source-system/site/module/type fields;
- content-hash based incremental reindex;
- full rebuild command;
- health/report command.

### Phase 5 acceptance criteria

- collection can be deleted and rebuilt entirely from Git + SQL;
- indexed point count/source count reconciles to authoritative sources;
- every point has valid provenance;
- no mem0 points appear in `hermes_kb_v1`;
- no raw ticket history appears in `hermes_kb_v1`.

---

## Phase 6 — Hybrid production retrieval

Replace the interim lexical article search with hybrid retrieval:

```text
dense + BM25 sparse -> RRF -> relevance gate -> top 3 compact hits
```

Keep deterministic route candidates and exact technical-term extraction.

Route acts as preference/boost, not an absolute gate.

Implement explicit abstention thresholds based on the evaluation dataset rather than arbitrary production intuition.

### Phase 6 acceptance criteria

- route-only relevance cannot surface an unrelated article;
- exact XStudio terms can rescue lexical matches;
- paraphrases can be found semantically;
- no-answer cases abstain reliably;
- provenance is preserved through retrieval;
- result payload clearly distinguishes relevance from trust/history.

---

## Phase 7 — Integrate unified KB retrieval into bundle

Target bundle contains:

```text
route candidates
KB hits from SQL + Git
same-ticket history
schema candidates
```

Remove legacy solution lookup paths once hybrid retrieval proves itself.

Do not send full article text unless selected/expanded.

### Phase 7 acceptance criteria

- one canonical KB retrieval path exists;
- no worker sees competing `known_solutions` mechanisms;
- normal dispatch survives Qdrant outage with explicit KB abstention/unavailable state;
- SQL/schema investigation still works when KB is unavailable.

---

## Phase 8 — Knowledge health and freshness

Implement:

- SQL object dependency fingerprinting where useful;
- Git source hash/commit tracking;
- failed reuse / reopen health transitions;
- `NeedsReview` workflow;
- stale source reporting.

### Phase 8 acceptance criteria

- changed evidence dependencies can flag affected articles;
- failed/reopened reuse is visible in article health;
- stale knowledge is not silently treated as fresh Approved knowledge.

---

## Phase 9 — mem0 cleanup and promotion path

Audit all seeded/shared mem0 lessons.

For each memory classify:

```text
config/policy -> move to config/skill
verified domain fact -> move to Git/KB
per-ticket fact -> remove / ledger only
true operational heuristic -> keep in mem0
```

Add a deliberate process for promoting repeated useful heuristics into canonical knowledge.

### Phase 9 acceptance criteria

- mem0 contains no canonical DB/product truth that should live elsewhere;
- workers can lose/rebuild mem0 without losing system knowledge;
- mem0 and `hermes_kb_v1` remain separate collections and responsibilities.

---

## Phase 10 — Optional retrieval optimization

Only after sufficient evaluation data exists, consider:

- weighted RRF;
- reranking;
- query expansion;
- article-quality priors;
- learned threshold tuning.

Any optimization must beat the baseline evaluation set without materially worsening no-answer precision or false-known-issue rate.

---

# 29. Implementation file map

Expected areas of change by phase.

### SQL / lifecycle

```text
Knowledge/00_tables_and_indexes.sql
Knowledge/50_response_and_workflow.sql
Knowledge/60_metrics_and_reporting.sql
Knowledge/00_Hermes_L2_FULL_INSTALL.sql
```

### Publisher / curation

```text
Model_Bench/kanban_approval_publisher.py
Hermes_Orchestrator.py
```

### Retrieval/indexing

```text
Model_Bench/kb_retrieval.py
Model_Bench/kb_index.py                 # planned
Model_Bench/kb_eval.py                  # planned
Model_Bench/kb_curate.py                # planned or integrated into orchestrator
```

### Routing/reference knowledge

```text
Knowledge/manifest.json
Knowledge/task-router.md
Knowledge/*.md frontmatter/metadata
```

### Evaluation

```text
Knowledge/eval/kb_retrieval_cases.jsonl
Model_Bench/test_kb_retrieval.py
```

### Qdrant deployment

```text
deploy/qdrant/*
```

### Agent memory

```text
Model_Bench/seed_mem0_lessons.py
```

---

# 30. Local validation policy

KB implementation must be validated locally before deployment.

Do not depend on GitHub-hosted Actions for this project.

Minimum local gate for every KB phase:

```text
Python syntax/compile
unit tests
manifest/reference validation
SQL migration review/dry-run where possible
read-only integration tests
negative retrieval/abstention tests
regression audit of ticket_scout/reviewer/publisher flow
```

Production-mutating operations such as `--poll`, ticket publication or SQL writes are not to be used merely as tests.

---

# 31. Rollout safety

Each phase should be independently deployable and reversible where practical.

Rules:

- add schema before code requires it;
- preserve compatibility with existing solution articles during migration;
- do not switch production retrieval to Qdrant until the index and eval suite pass locally;
- Qdrant failure must degrade to KB-unavailable/abstain, not block ticket investigation;
- do not delete legacy fields until the replacement path has operated successfully long enough to verify migration;
- all article lifecycle mutations must be auditable.

---

# 32. Definition of done for the KB program

The KB implementation is considered complete when all of the following are true:

1. Every reusable knowledge item has an authoritative source and lifecycle state.
2. A resolved ticket does not automatically create an Approved KB article.
3. Duplicate known issues normally reuse/update an existing article.
4. Candidate knowledge can be promoted, reviewed, superseded and deprecated.
5. Retrieval events and reuse outcomes are independently auditable.
6. Qdrant `hermes_kb_v1` can be completely rebuilt from Git + SQL.
7. Git references and SQL solution articles are retrievable through one hybrid interface.
8. Dense + sparse retrieval can abstain reliably.
9. Every KB hit contains provenance.
10. Schema discovery remains deterministic and separate.
11. Same-ticket history remains episodic and separate.
12. mem0 remains operational memory, not the KB.
13. Live SQL/verified reference evidence remains mandatory before applying a historical solution.
14. Failed reuse/reopens affect article health.
15. Retrieval quality is measured against a maintained local evaluation set.
16. The investigator receives compact, ranked, provenance-bearing KB leads rather than a large undifferentiated context dump.

---

# 33. Immediate next implementation slice

After local validation of the current baseline, implement **Phase 1 only** first:

1. design and add SQL lifecycle/provenance fields;
2. preserve backward compatibility;
3. change new resolution-derived knowledge from unconditional article creation to explicit Candidate/none/reuse-ready flow;
4. ensure normal retrieval only considers Approved articles;
5. add local tests for lifecycle filtering and duplicate-safe identity.

Do **not** begin the Qdrant hybrid index before Phase 1-3 have corrected knowledge creation, lifecycle and reuse semantics. Better retrieval over a polluted article corpus would only make bad knowledge easier to find.

---

## Core principle

```text
Evidence tells us what happened now.
Reference knowledge tells us how XStudio works.
Solution knowledge tells us what has worked before.
Problem management tells us why incidents recur.
Ticket history tells us what happened on this case.
Memory helps the agent operate efficiently.
Qdrant helps find the right knowledge.

None of these substitutes for another.
```
