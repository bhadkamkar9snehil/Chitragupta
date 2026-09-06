# Claude Entry Point — Chitragupta Adaptive L2 Branch

Branch:

```text
development/autonomous-l2-learning-runtime
```

Product rule:

> Build an autonomous, AI-driven, deterministic L2 Helpdesk that gets measurably better from experience and progressively earns the ability to solve XBatch issues itself.

Read, in order:

1. `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md`
2. `AGENTS.md`
3. `Knowledge/L2_PIPELINE_STATE_MACHINE.md` when changing lifecycle behavior

Do not treat `Plans/`, `Agent_Comms/`, old commits, or dated incident notes as current runtime instructions.

## Current authority split

```text
l2_pipeline_runtime.py
    lifecycle / WIP / review / publish / recovery

xstudio_l2
    typed read-only evidence

xstudio-l2-identity
    harness-owned run/ticket attribution

l2_learning
    session recording + explicit trust-scoped recall + lesson proposal

l2_gbrain.py / sync_l2_gbrain.py
    derivative GBrain retrieval/index with non-federated trust sources

l2_learning_cycle.py
    outcome labels + conservative candidate mining

sync_l2_approved_solutions.py
    explicit semantic-hash governance bridge for SQL Solutions

l2_actions
    non-executing capability list/describe/plan/plans/validate_plan

l2_action_capability_curator.py
    observed candidate -> reviewed shadow registry entry
```

## Preserve these invariants

- One deterministic lifecycle authority.
- Global SQL WIP currently 1.
- Priorities: review 30, rework 20, new investigation 10.
- Reviewer creation is deferred until completion is normalized/reviewable.
- Reviewer receives frozen `proposal_json`; publisher publishes that exact proposal.
- Live evidence wins over memory/history.
- Model-driven raw SQL mutation/transport remains unavailable.
- Identity-sensitive evidence and action plans are bound to the actual Kanban task.
- Sessions are recorded as unverified episodic history.
- Generic automatic prefetch stays off, including GBrain push/reflex context.
- Every GBrain L2 source is non-federated and retrieval names its source(s) explicitly.
- Raw GBrain MCP tools are not a second model-facing memory surface.
- Historical cases do not enter `trusted` automatically.
- Active SQL Solutions are not trusted unless explicitly hash-approved.
- Action candidates are evidence backlogs, not executable capabilities.
- `l2_actions` has no execute operation.
- Capability curation may add `mode=shadow` only and never raises registry `global_mode`.
- No GitHub Actions workflow is the validation authority.

## Adaptive learning rule

```text
record != trust
retrieve != prove
reviewed old case != current-ticket truth
plan != execute
```

Use explicit `l2_recall` scopes and verify ticket-specific claims live.

GBrain is derivative search/graph state. `trusted` maps only to `l2-knowledge`, `l2-facts`, and `l2-solutions`; sessions, historical outcomes, and candidates require explicit scopes.

`solutions/approved/` is generated output owned only by `sync_l2_approved_solutions.py`. Human-authored durable knowledge belongs in Git or promoted facts.

## Capability design rule

The capability miner records only repeated reviewed human work. It must not invent risk, parameter schema, SP/API/service target, preconditions, idempotency, verification, rollback/compensation, or approval policy.

The curator stores at most one reviewed `draft_contract` on the candidate:

```text
needs_executor_design
-> shadow_ready
-> registry_entry
```

Before `shadow_ready`, inspect the real supported XBatch operation and verify the complete contract.

## Future execution

Do not add an executor merely because the architecture anticipates one.

The first supervised executor should be built only after a real shadow capability and measured shadow evidence justify it. Its deterministic outcome/audit record should be designed with the executor and its actual failure/rollback semantics.

## Validation

Use:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Keep validation local. When adding or deleting an adaptive component, update the aggregate validator in the same change.
