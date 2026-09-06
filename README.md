# Chitragupta — Autonomous XStudio / Hermes L2 Helpdesk

Chitragupta is an AI-driven L2 support system around the existing XStudio Helpdesk. The model investigates and reasons; deterministic code owns incident identity, ticket lifecycle, independent review, publication and the boundary around any future XBatch side effect.

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
  eval/
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
SQL Solution lifecycle    governed reusable support knowledge
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

Model_Bench/mine_l2_learning_candidates.py
    outcome -> unverified lesson candidates

Model_Bench/mine_l2_action_capability_candidates.py
    repeated reviewed human actions -> action-capability backlog

Model_Bench/l2_learning_cycle.py
    single learning sidecar coordinator

Model_Bench/build_l2_historical_retrieval_eval.py
Model_Bench/benchmark_l2_learning_retrieval.py
    measurable historical retrieval replay

Model_Bench/xstudio_l2_actions_plugin/
    non-executing action planner

Model_Bench/validate_action_capabilities.py
    capability promotion/safety policy validator
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
