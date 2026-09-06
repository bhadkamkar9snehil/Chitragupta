# Chitragupta — Autonomous XStudio / Hermes L2 Helpdesk

Chitragupta is an AI-driven L2 support system around the existing XStudio Helpdesk. The model investigates and reasons; deterministic code owns incident identity, lifecycle transitions, independent review, publication, knowledge promotion, and the boundary around any future XBatch side effect.

Branch: `development/autonomous-l2-learning-runtime`

North star:

> An autonomous, AI-driven, deterministic L2 Helpdesk that keeps getting better from experience and progressively earns the ability to solve XBatch issues itself.

The detailed adaptive design lives in `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md`. This README describes what exists now.

## Current runtime

```text
Helpdesk ticket
    |
    v
deterministic claim
    |
    v
investigator [priority 10]
    |
    | live evidence via xstudio_l2
    | explicit experience lookup via l2_recall
    | optional non-executing action plan via l2_actions
    v
normalized frozen proposal
    |
    v
independent reviewer [priority 30]
   / \
approve reject
  |      |
  v      v
publish  rework [priority 20]
  |         |
  |         v
  |      fresh reviewer
  v
Helpdesk/SQL postconditions
```

`Model_Bench/l2_pipeline_runtime.py` remains the lifecycle authority. Global SQL WIP is currently 1. Reviewer creation is deferred until an investigator/rework completion is structurally reviewable. The reviewer judges frozen `proposal_json`; the deterministic publisher publishes that same proposal.

## Typed evidence and identity

Workers use `xstudio_l2` for database/schema/ticket/run evidence. The harness owns Windows/WSL/Python/driver transport and credentials.

Arbitrary model-built SQL mutation, `sqlcmd`, pyodbc setup, package installation and raw `EXEC` fallback are not worker capabilities.

`xstudio-l2-identity` binds identity-sensitive calls to the actual Kanban task. The model may choose what to investigate, but it may not attach evidence or an action plan to a different run/ticket.

## Experience and learning

Shared learning vault:

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

`zvec-grep` is a local BM25 + vector + RRF retrieval substrate. Its index is disposable.

### Sessions are recorded

Completed L2 turns are recorded as redacted `unverified_episodic` history. Successful reasoning, dead ends, reviewer-corrected mistakes and tool failures are all useful replay/evaluation data.

### Generic automatic prefetch is off

Similarity is not truth. Historical sessions include rejected hypotheses and stale state, so mixed top-k memory is not injected automatically into every new ticket.

`l2_recall` is explicit and trust-scoped. `trusted` contains canonical Git reference, promoted facts and explicitly governed reusable Solutions. Historical cases and raw sessions remain separate scopes and still require current-ticket verification.

## Outcome-conditioned learning

`Model_Bench/l2_learning_cycle.py` is the single best-effort learning sidecar. It:

1. materializes reviewer/publisher outcomes as historical cases;
2. mines conservative unverified lesson candidates;
3. mines repeated reviewed `NEEDS_HUMAN_ACTION` patterns into action-capability candidates.

Learning failure is not lifecycle authority and does not stop deterministic ticket processing.

The important rule is:

```text
recorded experience != trusted knowledge
retrieved history != current evidence
candidate lesson != promoted fact
```

## Governed reusable Solutions

`dbo.Hermes_Solution_Article_Mst_Tbl` is a reusable-knowledge source, but an active row is not automatically trusted.

`Model_Bench/sync_l2_approved_solutions.py` exports only entries explicitly approved in `deploy/solution_export_policy.json` by:

```text
solution_id
semantic content_sha256
approved_by
approved_at
review_evidence
```

`solutions/approved/` is generated output owned only by that exporter. Trusted text contains governed reusable guidance, not mutable operational telemetry.

When synchronization runs, missing or semantically drifted approved Solutions are removed from trusted scope and reported until re-reviewed.

## Action-capability backlog

`mine_l2_action_capability_candidates.py` looks only at approved historical `NEEDS_HUMAN_ACTION` cases. Repeated lexically equivalent human actions across distinct tickets create an unverified candidate under:

```text
actions/candidates/
```

The miner records observed evidence only. It does not invent risk, parameters, executor paths, preconditions, verification or rollback.

`l2_action_capability_curator.py` is the operator/control-plane path:

```text
needs_executor_design
    |
    | reviewed draft_contract
    v
shadow_ready
    |
    v
registry_entry
```

The curator's `list` command is also the backlog view and ranks candidates by distinct reviewed tickets, then observation count.

Promotion adds only a `mode=shadow` registry entry and never raises `global_mode`.

## Current action surface

Registry:

```text
deploy/xstudio_action_capabilities.json
```

Model-facing toolset:

```text
l2_actions
```

Operations:

```text
list
describe
plan
plans
validate_plan
```

There is no execute operation.

Plans are durable, capability-hashed, evidence-carrying and harness-bound to the current run/ticket. They explicitly state that execution is not authorized.

## Current storage roles

```text
live SQL / Helpdesk      current incident truth
run ledger / traces      current incident execution evidence
Git Knowledge/           canonical project/domain reference
solutions/approved       governed reusable SQL-Solution mirror
mem0                     compact durable operational behavior
zvec learning vault      high-recall experience/replay substrate
```

Do not collapse those authority classes.

## Validation

Repository validation is local, not GitHub Actions:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

The validator covers lifecycle contracts, typed tools, identity binding, learning-vault preservation, outcome learning, governed Solution export, capability mining/curation, action planning, retrieval checks, live profile configuration, workflow discovery and reconciliation dry-run.

## Next evidence-driven step

Do not add more framework before there is evidence for it.

Use the real learning history to identify the strongest repeated human corrective action:

```bash
python3 Model_Bench/l2_action_capability_curator.py list
```

Then inspect the actual supported XBatch SP/API/service implementation and only after that draft the first real shadow contract.

The future supervised/autonomous executor should be introduced only when a real shadow capability and measured shadow evidence justify it. Its audit/outcome mechanism should be designed together with that executor, not as speculative standalone scaffolding.
