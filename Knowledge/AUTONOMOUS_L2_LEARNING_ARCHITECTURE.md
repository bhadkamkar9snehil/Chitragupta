# Autonomous L2 Learning Architecture

Status: **experimental branch contract**  
Branch: `development/autonomous-l2-learning-runtime`

North star:

> Chitragupta becomes an autonomous, AI-driven, deterministic L2 Helpdesk that improves from experience and progressively earns the ability to solve XBatch issues itself.

This document is the adaptive-branch architecture authority. It distinguishes **implemented now** from **future capability** so design intent does not become accidental runtime contract.

## 1. One product rule

Everything serves one goal:

```text
better autonomous L2 outcomes
without giving up deterministic identity,
workflow, evidence attribution,
side-effect control, or outcome verification
```

## 2. Current four-plane architecture

```text
CONTROL
  deterministic claim -> investigate -> normalize -> review -> publish/rework

EVIDENCE
  xstudio_l2 typed reads
  live schema/object discovery
  run ledger / SQL action history
  harness-owned run/ticket identity

EXPERIENCE
  recorded sessions
  outcome-labelled historical cases
  governed reference/solution retrieval
  conservative lesson/action candidate mining
  replay and retrieval measurement
  GBrain retrieval/graph substrate

ACTION
  typed capability registry
  non-executing action planning
  reviewed shadow-capability promotion
```

The model reasons. Deterministic code owns lifecycle transitions, identity, trust promotion and any future side-effect boundary.

## 3. Storage is not authority

Core epistemic rule:

```text
recording experience != believing experience
retrieving experience != current-ticket proof
review approval on an old case != universal truth
planning an action != executing an action
```

### Session recording is ON

Completed investigator/reviewer turns are stored redacted with:

```text
trust: unverified_episodic
```

This history intentionally retains useful mistakes as well as successes.

### Generic automatic prefetch is OFF

GBrain supports push/volunteered context, but Chitragupta does not enable that lane for L2 workers.

Similarity and entity relevance answer "what looks related?". They do not answer "what is true for this ticket?". A reviewer-rejected hypothesis is valuable historical evidence but is dangerous if silently injected before a new investigation. Therefore retrieval is explicit, stage-aware and trust-scoped through `l2_recall`.

No raw GBrain MCP surface is exposed to the worker profiles. Chitragupta keeps the narrow model-facing contract.

## 4. Learning vault and GBrain

Source material remains under:

```text
~/.hermes/l2-learning/
```

Layout:

```text
sessions/
cases/
  approved/
  rejected/
  reopened/
facts/
candidates/
knowledge/
solutions/
  approved/
actions/
  plans/
  candidates/
eval/
archive/
  candidates/
```

The vault is source material. GBrain's database, chunks, embeddings, graph edges and search telemetry are **derivative state** and may be rebuilt.

`sync_l2_gbrain.py` keeps a local-only Git checkpoint of the vault because GBrain path sources reconcile against Git state. It creates no remote and pushes nowhere.

## 5. GBrain trust topology

Every trust lane is a separate **non-federated** GBrain source:

| GBrain source | Vault material |
|---|---|
| `l2-knowledge` | `knowledge/` |
| `l2-facts` | `facts/` |
| `l2-solutions` | `solutions/approved/` |
| `l2-approved-cases` | `cases/approved/` |
| `l2-rejected-cases` | `cases/rejected/` |
| `l2-reopened-cases` | `cases/reopened/` |
| `l2-sessions` | `sessions/` |
| `l2-candidates` | `candidates/` |

Non-federation is deliberate. An unqualified GBrain search must not silently combine trusted guidance with rejected hypotheses or raw sessions.

`l2_recall` maps semantic scopes to explicit source IDs:

| Scope | Meaning |
|---|---|
| `trusted` | `l2-knowledge,l2-facts,l2-solutions` |
| `knowledge` | canonical Git/skill mirror |
| `facts` | promoted operational heuristics |
| `solutions` | governed reusable SQL Solutions |
| `approved_cases` | old proposal passed review + publication postconditions |
| `rejected_cases` | reviewer-rejected counterexamples |
| `reopened_cases` | old resolution later regressed/reopened |
| `cases` | all three historical outcome sources |
| `sessions` | raw unverified episodic history |
| `candidates` | unreviewed lesson candidates |
| `all` | every L2 source, explicitly mixed/untrusted |

Historical cases remain excluded from `trusted`.

## 6. Why GBrain replaces zvec-grep

GBrain is now the intended broad retrieval substrate for this branch rather than a second memory system beside zvec.

It adds capabilities useful to the product without changing authority:

```text
hybrid keyword/vector retrieval
explicit source isolation
search telemetry and tuning
graph edges and traversal
citation-aware synthesis
gap/contradiction analysis
Hermes transcript ingestion support
dream/maintenance machinery
local LM Studio provider support
```

Chitragupta deliberately does **not** expose the whole GBrain tool surface to the 9B workers. `l2_recall` remains the safety and trust adapter; `l2_lesson` remains the only model-facing learning write and still writes an unverified candidate, not truth.

`hybrid` uses GBrain's cheap hybrid `search` lane. `deep` explicitly opts into GBrain `query` and its heavier retrieval path. Legacy `fts` maps to the cheap lane and legacy `vector` maps to `deep` until callers are migrated.

## 7. GBrain and mem0 have different jobs

For now:

```text
live SQL        = current incident truth
run ledger      = this incident's durable evidence
Git/Solutions   = reusable authority
GBrain          = broad experience/knowledge retrieval + graph substrate
mem0            = small operational behavior hints
```

Do not create a universal "memory" bucket.

GBrain may eventually absorb mem0's narrow role, but only after real retrieval and behavior comparisons show that removal is an improvement.

## 8. Outcome-conditioned learning

Implemented:

```text
reviewer reject
    -> cases/rejected

reviewer approve + publisher postconditions
    -> cases/approved

published resolution later leaves terminal state
    -> cases/reopened
```

`l2_learning_cycle.py` remains the single best-effort lifecycle-side learning boundary:

```text
sync outcomes
-> mine lesson candidates
-> mine repeated human-action candidates
```

It is not lifecycle authority. A learning failure must not block ticket reconciliation, review or publication.

GBrain synchronization is derivative corpus maintenance and is kept outside lifecycle correctness.

## 9. Governed reusable SQL Solutions

An active SQL Solution is a knowledge source, not automatic trusted memory.

```text
active SQL Solution
    |
    | operator reviews semantics
    v
deploy/solution_export_policy.json
    solution_id
    semantic content_sha256
    approved_by / approved_at
    review_evidence
    |
    | sync re-reads live SQL
    v
solutions/approved/<id>.md
    |
    v
GBrain source l2-solutions
```

`solutions/approved/` has one owner: `sync_l2_approved_solutions.py`.

An unapproved, missing or semantically drifted generated article leaves trusted scope when synchronization runs. The exporter is read-only to SQL.

## 10. Harness-owned incident identity

`xstudio-l2-identity` binds identity-sensitive tool calls to the actual Kanban task.

```text
model chooses investigation/action semantics
harness chooses incident identity and authority
```

GBrain retrieval can suggest an analogy. It cannot change the run/ticket to which evidence or an action plan belongs.

## 11. Historical replay and measurement

Retrieval gates include:

1. static architecture/policy smoke cases;
2. runtime-derived replay cases built from recorded incident context and outcome-labelled history.

Metrics include retrieval hit rate, false-positive guards, latency and delivered context size. GBrain additionally gives us search telemetry that can be used to tune the derivative retrieval layer without changing the lifecycle.

Evaluation should grow toward:

```text
resolution correctness
review rejection rate
reopen / false-resolution rate
tool and token efficiency
live-evidence coverage
shadow-plan agreement with human action
```

A claimed improvement should be demonstrated by replay/live outcomes, not intuition.

## 12. Repeated human work -> action candidates

`mine_l2_action_capability_candidates.py` examines approved historical `NEEDS_HUMAN_ACTION` cases. Repeated normalized corrective actions across distinct tickets become:

```text
actions/candidates/<id>.json
```

The miner owns only observed evidence and does not invent executor details or risk classification.

## 13. Minimal capability governance

Current workflow:

```text
needs_executor_design
    |
    | one reviewed draft_contract
    v
shadow_ready
    |
    v
registry_entry
```

A candidate can also be rejected. There is no persisted research mini-workflow.

Before `shadow_ready`, the contract must identify the capability ID, risk, parameter schema, supported executor target, preconditions, idempotency, required evidence, verification, rollback/compensation and approval policy.

Promotion writes only `mode=shadow` and never raises registry `global_mode`.

## 14. Current action plane

Registry:

```text
deploy/xstudio_action_capabilities.json
```

Model-facing operations:

```text
list
describe
plan
plans
validate_plan
```

There is no execute operation.

A plan is durable, evidence-carrying, capability/registry-hashed, incident-bound and explicitly records that execution is not authorized.

## 15. Autonomy ladder

```text
A0 observe
A1 recommend exact human action
A2 shadow-plan a reviewed capability
A3 supervised deterministic execution
A4 autonomous low-risk capability
A5 broader autonomous remediation
```

Only A0-A2 mechanics exist today. A3+ must be justified by a real capability and measured shadow evidence.

## 16. GBrain expansion path

GBrain has useful features that should be adopted only where they improve this product:

**Now**
- trust-separated hybrid retrieval behind `l2_recall`;
- search telemetry;
- source-level provenance;
- indexing of correlated sessions, historical outcomes and governed reference material.

**Next, after retrieval evaluation**
- graph extraction over stable XBatch concepts: procedures, tables/views, modules, error classes, capabilities and Solution articles;
- graph-assisted retrieval for relationship questions such as which procedure touches which transaction flow;
- contradiction/gap analysis over governed reference and historical outcomes.

**Offline only at first**
- GBrain dream/synthesis over historical sessions/cases to propose lesson candidates;
- any synthesized result remains a candidate until Chitragupta's governance accepts it.

**Not enabled**
- generic push/reflex context into L2 prompts;
- ambient GBrain memory writes from worker prose;
- raw GBrain MCP write tools for workers;
- GBrain as lifecycle or side-effect authority.

## 17. Local model posture

GBrain supports LM Studio through its OpenAI-compatible local provider. Chitragupta setup therefore does not require a hosted embedding provider.

The operator supplies the actual loaded embedding model ID and native dimensions:

```bash
gbrain init --pglite \
  --embedding-model lmstudio:<model-id> \
  --embedding-dimensions <N>
```

Chitragupta pins `search.mode=conservative` for a small-model retrieval budget. `l2_recall` independently caps result count and returned characters.

PGLite is acceptable while Chitragupta keeps one effective inference/work slot and uses short harness-owned calls. If the brain becomes genuinely concurrent or multi-machine, moving GBrain to Postgres is an infrastructure change, not a model-behavior change.

## 18. Keep the architecture ponytailed

Prefer:

```text
one lifecycle authority
one learning sidecar
one GBrain adapter
one generated Solution owner
one capability backlog view
one canonical action contract
```

Do not add:

```text
zvec beside GBrain
direct GBrain MCP beside l2_recall
duplicate schedulers
generic memory injection
parallel candidate representations
future-only state machines
raw model-owned mutation paths
```

The next feature should be driven by a real ticket, measured retrieval failure, or repeated human action.
