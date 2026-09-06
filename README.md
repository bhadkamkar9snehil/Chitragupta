# Chitragupta — Autonomous XStudio / Hermes L2 Helpdesk

Chitragupta is an AI-driven L2 support system around the existing XStudio Helpdesk. The model investigates and reasons; deterministic code owns incident identity, ticket lifecycle, independent review, publication, knowledge promotion, and the boundary around any future XBatch side effect.

This branch is deliberately building beyond a read-only support bot toward a system that:

```text
handles tickets autonomously
-> records its experience
-> learns from reviewer/publisher outcomes
-> measures whether retrieval/reasoning changes help
-> discovers repeated human corrective work
-> turns verified repeated work into typed XBatch capabilities
-> earns supervised/autonomous execution per capability
```

Branch north star: `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md`.

## Current multi-plane architecture

```text
                         XStudio Helpdesk
                               |
                        deterministic claim
                               v
                         INVESTIGATOR
              ┌────────────────┼────────────────┐
              v                v                v
        xstudio_l2          l2_recall        l2_action
        live evidence      prior experience  capability plan
              |                |                |
              +----------------+----------------+
                               v
                      structured proposal
                               v
                    deterministic normalize
                               v
                       fresh REVIEWER
                    frozen proposal_json
                         /           \
                    approve         reject
                       |              |
                       v              v
             deterministic publish   rework
                       |
                       v
              publisher postconditions
                       |
                       v
                 LEARNING SIDECAR
            outcomes -> cases -> candidates
                       |
                       +--> reusable lesson backlog
                       +--> repeated human-action capability backlog
                       +--> historical retrieval replay
```

There is one Kanban board. Reviewers are deferred until an investigator/rework completion is structurally reviewable; they are not pre-created or parent-gated.

## Deterministic control plane

`Model_Bench/l2_pipeline_runtime.py` is the lifecycle authority.

Current scheduling contract:

- global SQL WIP: `1`;
- reviewer priority: `30`;
- rework priority: `20`;
- new investigation priority: `10`;
- bounded `review_cycle`, independent of SQL `AttemptNo`;
- frozen `proposal_json` is what the reviewer judges and publisher later publishes;
- Helpdesk workflow states come from observed binding, not model prose;
- publication is deterministic and postcondition-checked.

`ticket_scout.py` remains the reconciliation/claim backstop. Learning is invoked only as one best-effort sidecar boundary and is never lifecycle authority.

## Evidence plane

Workers use the typed `xstudio_l2` tool for database/schema/ticket/run work. The harness owns Windows/WSL/Python/pyodbc transport and credentials.

The model does not construct SQL transport. Raw write/DDL/EXEC SQL is not available through the worker surface.

### Harness-owned incident identity

`Model_Bench/xstudio_l2_identity_plugin/` closes a separate correctness gap: the model must not decide which run/ticket receives its evidence or action-plan provenance.

The pre-tool guard resolves the actual Kanban task and binds:

```text
select/query/read_procedure/get_run_actions/save_ledger -> current run_id
get_ticket_context                                      -> current ticket_id
l2_action plan/plans                                    -> current run_id + ticket_id
l2_action validate_plan                                 -> rejects cross-run/cross-ticket plan
```

Pure schema discovery remains independent. Conflicting model-supplied identifiers are blocked.

## Experience and learning plane

Shared vault:

```text
~/.hermes/l2-learning/
  sessions/
  cases/approved/
  cases/rejected/
  cases/reopened/
  facts/
  candidates/
  knowledge/
  solutions/approved/
  actions/plans/
  actions/candidates/
  actions/receipts/
  eval/
  archive/
```

`zvec-grep` is the local BM25 + vector + RRF retrieval substrate. The index is disposable.

### Sessions are recorded

Completed L2 turns are stored as redacted `unverified_episodic` Markdown with best-effort run/ticket/stage correlation. Successful reasoning, dead ends, reviewer-corrected mistakes and tool failures are all useful future evaluation data.

### Generic automatic prefetch is intentionally absent

Similarity does not imply truth. Old assistant mistakes, rejected hypotheses and stale state are useful history but should not silently enter every new prompt with equal epistemic weight.

`l2_recall` therefore requires an explicit trust scope:

| Scope | Use |
|---|---|
| `trusted` | governed Git reference + promoted facts + approved reusable solutions |
| `approved_cases` | historical proposals that passed independent review and publisher postconditions |
| `rejected_cases` | reviewer-rejected counterexamples |
| `reopened_cases` | historical resolutions that later regressed/reopened |
| `sessions` | raw historical reasoning/dead ends |
| `candidates` | unreviewed proposed lessons |

Historical cases are deliberately excluded from `trusted`.

## Governed SQL Solution retrieval

The SQL KB table `dbo.Hermes_Solution_Article_Mst_Tbl` remains a reusable-knowledge source, but `IsActive=1` alone does not make a Solution trusted retrieval material.

`Model_Bench/sync_l2_approved_solutions.py` and `deploy/solution_export_policy.json` require an explicit approval record containing:

```text
solution_id
semantic content_sha256
approved_by
approved_at
review_evidence
```

The exporter re-reads live SQL and exports only exact approved semantics into:

```text
solutions/approved/<solution-id>.md
trust: governed_reusable_solution
```

The hash covers reusable knowledge fields and deliberately excludes mutable telemetry such as `UsageCount`. Governed semantic drift fails closed and archives a stale managed trusted export until the changed content is reviewed. `--preview-live` lists active Solution IDs and review hashes without trusting them.

## Outcome-conditioned learning

`sync_l2_outcomes.py` converts lifecycle truth into labelled history:

```text
reviewer reject                           -> cases/rejected
reviewer approve + successful publication -> cases/approved
published resolution later regresses      -> cases/reopened
```

`mine_l2_learning_candidates.py` conservatively turns those outcomes into unverified lesson candidates. It can identify reviewer failure patterns, reopened-resolution patterns and repeated lexically equivalent approved root causes across distinct tickets.

`l2_lesson` also lets an investigator/reviewer propose a reusable lesson, but it can write only to the unverified candidate queue.

Promotion is separate. A model saying it learned something is not the same thing as the system learning it.

## Detecting what XBatch work should be automated

`mine_l2_action_capability_candidates.py` examines **approved** `NEEDS_HUMAN_ACTION` historical cases.

When the same normalized corrective action appears across multiple distinct tickets it creates/updates:

```text
actions/candidates/<id>.json
```

This is a capability-engineering backlog. It records repeated human effort and source cases, while leaving these deliberately unknown until verified:

```text
risk
parameter schema
real executor/SP/API/service path
preconditions
idempotency
verification
rollback/compensation
approval policy
```

The backlog tells us what is worth automating; it does not invent how to automate it.

### Governed capability design

`Model_Bench/l2_action_capability_curator.py` moves a real backlog item through:

```text
needs_executor_design
-> researching_executor
-> contract_drafted
-> shadow_ready
-> registry_entry
```

Every transition requires reviewer/evidence provenance. Before `shadow_ready`, the candidate needs a concrete supported execution target and reviewed parameter/precondition/idempotency/evidence/postcondition/rollback/approval contract.

Promotion adds only a `mode=shadow` capability and never raises registry `global_mode`. The current registry can therefore remain globally `observe` even after the first reviewed shadow contract exists.

## Action plane

Machine-readable registry:

```text
deploy/xstudio_action_capabilities.json
```

Direct model-facing toolset:

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

A plan is durable, idempotent, capability-hashed, evidence-carrying, harness-bound to the current run/ticket and always states:

```text
execution_authorized: false
execution_tool_available: false
```

This lets us measure action-selection quality before granting mutation authority.

### Action receipts already exist as a contract

No executor exists yet, but the outcome semantics do:

```text
planned -> approved -> executed -> verified
    \         \          \
     +-> failed <---------+
           |
           v
      compensated
```

`deploy/xstudio_action_receipt.schema.json` and `Model_Bench/xstudio_action_receipts.py` define append-only attempt history. `verified` requires deterministic postconditions; `compensated` requires verified rollback/compensation. A receipt records what happened—it does not grant execution authority.

### Autonomy ladder

```text
A0 observe/read-only diagnosis
A1 recommend exact human action
A2 shadow-plan registered capability
A3 supervised execute after explicit approval
A4 autonomous low-risk capability
A5 broader autonomous remediation after measured promotion
```

Autonomy is capability-specific. There is no global "allow model SQL writes" switch.

## Historical replay and measurement

The static retrieval smoke set is `Model_Bench/l2_learning_eval_cases.jsonl`.

`build_l2_historical_retrieval_eval.py` additionally builds a runtime replay set from real history:

```text
earliest recorded user/task text for a run
      -> expected outcome-labelled case for that run
```

`benchmark_l2_learning_retrieval.py` measures deterministic retrieval hit rate, p50/p95 latency, context size and explicit false-positive guards without an LLM judge.

The evaluation plane should keep expanding toward resolution correctness, reject/reopen rates, false resolutions, tool/token efficiency, live-evidence coverage, shadow-plan agreement and eventually supervised/autonomous action success/rollback rates.

## Memory/knowledge roles

Do not collapse all storage into one concept:

```text
live SQL                  current incident truth
run ledger / traces       current incident execution evidence
Git Knowledge/            canonical project/domain reference
SQL Solution lifecycle    reusable source requiring explicit trust governance
solutions/approved        hash-pinned governed reusable retrieval guidance
mem0                      compact durable operational behavior
zvec learning vault       high-recall experience/cases/replay substrate
```

## Core adaptive runtime files

```text
Model_Bench/l2_pipeline_runtime.py
    deterministic Helpdesk lifecycle

Model_Bench/ticket_scout.py
    reconcile-first backstop + one best-effort learning-cycle call

Model_Bench/xstudio_l2_tools_plugin/
Model_Bench/xstudio_l2_tool_bridge.py
    typed bounded read-only evidence surface + harness transport

Model_Bench/xstudio_l2_identity_plugin/
    cross-cutting run/ticket identity binding

Model_Bench/xstudio_l2_learning_plugin/
    session recording + explicit trust-scoped recall + lesson proposal

Model_Bench/sync_l2_outcomes.py
    reviewer/publisher outcome labels

Model_Bench/sync_l2_approved_solutions.py
deploy/solution_export_policy.json
    semantic-hash-governed SQL Solution -> trusted retrieval export

Model_Bench/mine_l2_learning_candidates.py
    outcome -> unverified lesson candidates

Model_Bench/mine_l2_action_capability_candidates.py
    repeated reviewed human actions -> action-capability backlog

Model_Bench/l2_action_capability_curator.py
    reviewed backlog candidate -> shadow registry workflow

Model_Bench/l2_learning_cycle.py
    single learning sidecar coordinator

Model_Bench/build_l2_historical_retrieval_eval.py
Model_Bench/benchmark_l2_learning_retrieval.py
    measurable historical retrieval replay

Model_Bench/xstudio_l2_actions_plugin/
    non-executing action planner

Model_Bench/validate_action_capabilities.py
    capability promotion/safety policy validator

deploy/xstudio_action_receipt.schema.json
Model_Bench/xstudio_action_receipts.py
    future append-only execution outcome contract
```

## Response types

| Type | Meaning |
|---|---|
| `UPDATE` | verified progress, not final |
| `QUESTION` | requester fact genuinely required |
| `RESOLUTION` | verified current outcome/fix |
| `NEEDS_HUMAN_ACTION` | cause/action known but no approved executor has performed it |
| `L3_ESCALATION` | root cause/safe path still unresolved or beyond L2 |

As the action plane matures, some cases that currently end as `NEEDS_HUMAN_ACTION` should become shadow, then supervised, then autonomous remediation—without weakening evidence or postcondition requirements.

## Immediate next work

The core structural continuation points are now present. The next useful sequence is evidence-driven rather than more framework scaffolding:

1. preview active SQL Solutions and explicitly approve only reusable articles worth entering `trusted` retrieval;
2. run the real learning cycle and inspect `actions/candidates/**`;
3. choose the strongest repeated real human action by independent-ticket evidence;
4. inspect its actual XBatch implementation and classify risk only after understanding the side effect;
5. move it through the capability curator into the first genuine shadow registry contract;
6. collect shadow-plan agreement/outcome evidence before introducing a supervised executor.

Synthetic test capability names are not real candidates and must not be promoted.

## Direction

The target loop is:

```text
observe
-> reason
-> independent review
-> deterministic publication or typed action
-> verify outcome
-> record experience
-> label outcome
-> mine lessons and repeated human work
-> replay/evaluate
-> promote what earns trust
-> expand safe autonomous capability
```

That—not a larger prompt or a universal memory store—is how Chitragupta becomes a progressively better autonomous L2 system.
