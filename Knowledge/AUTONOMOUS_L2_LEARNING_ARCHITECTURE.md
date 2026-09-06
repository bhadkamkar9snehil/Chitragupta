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

Rules are kept because they protect that goal, not because an older design happened to contain them.

## 2. Current four-plane architecture

```text
CONTROL
  deterministic claim
  investigator
  normalize
  frozen independent review
  deterministic publish / bounded rework

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

### Session recording is implemented and ON

Completed investigator/reviewer turns are stored as redacted:

```text
trust: unverified_episodic
```

This history intentionally contains useful mistakes as well as successes.

### Generic automatic prefetch is intentionally OFF

Similarity answers "what looks related?", not "what is true?".

A prior hallucination or reviewer-rejected hypothesis is valuable replay data but must not silently enter every future ticket. Retrieval is therefore explicit and trust-scoped.

A future automatic context builder is acceptable only if it is deterministic, stage-aware and trust-aware. Generic mixed-memory top-k injection is not.

## 4. Shared learning vault

Default:

```text
~/.hermes/l2-learning/
```

Current layout:

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

`.zvec-grep/` is a disposable retrieval index.

The canonical Git mirror under `knowledge/` can be rebuilt without touching runtime experience.

## 5. Trust scopes

`l2_recall` separates source classes:

| Scope | Meaning |
|---|---|
| `trusted` | canonical Git reference + promoted facts + explicitly governed reusable Solutions |
| `knowledge` | Git/skill mirror |
| `facts` | promoted operational heuristics |
| `solutions` | explicitly governed reusable SQL Solutions |
| `approved_cases` | old proposal passed review + publication postconditions |
| `rejected_cases` | reviewer-rejected counterexamples |
| `reopened_cases` | old resolution later regressed/reopened |
| `cases` | mixed historical outcomes |
| `sessions` | raw unverified episodic history |
| `candidates` | unreviewed lesson candidates |
| `all` | explicitly mixed/untrusted retrieval |

Historical cases are deliberately excluded from `trusted`.

## 6. Outcome-conditioned learning

Implemented:

```text
reviewer reject
    -> cases/rejected

reviewer approve + publisher postconditions
    -> cases/approved

published resolution later leaves terminal state
    -> cases/reopened
```

`l2_learning_cycle.py` is the single best-effort sidecar:

```text
sync outcomes
-> mine lesson candidates
-> mine repeated human-action candidates
```

It is not lifecycle authority. A learning failure must not block ticket reconciliation, review or publication.

### Lesson candidates

`mine_l2_learning_candidates.py` creates unverified candidates from strong lifecycle signals such as reviewer rejection, reopen/regression, and repeated lexically equivalent approved root causes.

Promotion remains separate.

## 7. Governed reusable SQL Solutions

The SQL Solution table is a knowledge source, not automatic trusted memory.

Implemented governance bridge:

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
```

`solutions/approved/` has one owner: `sync_l2_approved_solutions.py`.

Consequences:

- hand-authored knowledge does not live there;
- mutable operational telemetry is not part of trusted article text;
- when synchronization runs, an unapproved, missing or semantically drifted generated article is removed from trusted scope;
- a sync error reports governance failure but does not become lifecycle/deployment authority.

The exporter is read-only to SQL.

## 8. Harness-owned incident identity

`xstudio-l2-identity` binds identity-sensitive tool calls to the actual Kanban task.

The long-term rule is:

```text
model chooses investigation/action semantics
harness chooses incident identity and authority
```

Conflicting model-supplied run/ticket identity is blocked.

## 9. Historical replay and measurement

Implemented retrieval gates:

1. static architecture/policy smoke cases;
2. runtime-derived replay cases built from recorded incident context and outcome-labelled history.

Current deterministic metrics include retrieval hit rate, latency, retrieved context size and forbidden-result checks.

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

## 10. From repeated human work to capability candidates

Implemented:

`mine_l2_action_capability_candidates.py` examines approved historical `NEEDS_HUMAN_ACTION` cases.

When the same normalized human corrective action appears on at least two distinct tickets, it creates/updates:

```text
actions/candidates/<id>.json
```

The miner owns only observed evidence:

```text
source cases
ticket/run IDs
observation count
distinct-ticket count
representative action
normalized action
```

It deliberately does not invent design facts.

If a governed candidate file becomes unreadable, the miner fails closed for that item rather than rebuilding over possible operator state.

## 11. Minimal capability governance

Implemented control-plane workflow:

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

A candidate can also be rejected.

There is no persisted "researching executor" or "contract drafted" workflow state. Research notes belong in evidence/provenance; workflow states exist only when runtime behavior needs them.

`l2_action_capability_curator.py list` is the single backlog view. It ranks valid candidates by:

1. distinct reviewed tickets;
2. observation count.

Risk remains `unclassified` until a real side effect is inspected.

Before `shadow_ready`, the reviewed `draft_contract` must identify:

```text
capability ID
risk
parameter schema
real supported executor target
preconditions
idempotency
required evidence
verification/postconditions
rollback/compensation
approval policy
```

Promotion writes only `mode=shadow` and never raises registry `global_mode`.

## 12. Current action plane

Registry:

```text
deploy/xstudio_action_capabilities.json
```

Model-facing toolset:

```text
l2_actions
```

Current operations:

```text
list
describe
plan
plans
validate_plan
```

There is no execute operation.

A plan is durable, evidence-carrying, capability/registry-hashed and bound to the current run/ticket. It explicitly records that execution is not authorized.

This lets us measure whether the system selects the correct action before granting mutation authority.

## 13. Autonomy ladder

Design direction:

```text
A0 observe
A1 recommend exact human action
A2 shadow-plan a reviewed capability
A3 supervised deterministic execution
A4 autonomous low-risk capability
A5 broader autonomous remediation
```

Only A0-A2 mechanics exist on this branch today.

A3+ is future work and must not be implied by current model-facing tools.

## 14. Future executor requirements

Do not build a standalone execution/audit framework before a real shadow capability needs it.

When the first supervised executor is justified, design its outcome record together with the real capability and failure semantics. At minimum it must deterministically capture:

```text
plan/capability/registry version
run/ticket identity
approval
preconditions checked
side effect attempted
execution result
postconditions
failure
rollback/compensation when required
```

Success means verified postconditions, not merely "the call returned without error".

This is a future requirement, not a current runtime subsystem.

## 15. Keep the architecture ponytailed

Prefer:

```text
one lifecycle authority
one learning sidecar
one generated Solution owner
one capability backlog view
one canonical action contract
```

Do not add:

```text
duplicate schedulers
duplicate backlog/report CLIs
parallel candidate representations
future-only state machines
generic memory injection
raw model-owned mutation paths
```

The next feature should be driven by a real ticket, real repeated human action, or measured failure—not by an imagined future abstraction.

## 16. Immediate next step

The structural work is sufficient.

Use real history:

```bash
python3 Model_Bench/l2_action_capability_curator.py list
```

Choose the strongest actual repeated human action by evidence, inspect the real supported XBatch SP/API/service implementation, and only then draft the first real shadow contract.

That is the next point at which new code is justified.
