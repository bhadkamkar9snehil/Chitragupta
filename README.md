# Chitragupta — XStudio / Hermes L2 Helpdesk

Chitragupta is the XStudio/Helpdesk domain layer running on the Hermes agent harness. The model investigates; deterministic code owns incident identity, workflow transitions, independent review, publication and knowledge promotion.

## Runtime

```text
Helpdesk ticket
-> deterministic claim
-> investigator
-> frozen proposal
-> independent reviewer
   -> approve -> deterministic publish
   -> reject  -> bounded rework -> fresh reviewer
```

`Model_Bench/l2_pipeline_runtime.py` is the lifecycle authority. Global SQL WIP is currently 1. Priorities are review 30, rework 20 and new investigation 10.

Reviewer cards are created only after investigator/rework output is structurally reviewable. The reviewer judges immutable `proposal_json`; the publisher publishes that same proposal and verifies persisted SQL/Helpdesk state.

## Hermes boundary

Hermes owns sessions, Kanban worker dispatch, gateways, scheduling and plugin loading.

Chitragupta adds one Hermes plugin: `xstudio-l2-tools`.

It exposes:

- `xstudio_l2` — typed XStudio/Helpdesk evidence, schema discovery, ticket/run reads and investigation-ledger writes;
- `l2_recall` — read-only trust-scoped GBrain retrieval.

The Windows bridge is the only worker-facing component that knows pyodbc/SQL transport. Arbitrary model-built database transport, writes, DDL and arbitrary stored-procedure execution are not available.

## Evidence and retrieval

Current-ticket truth comes from live `xstudio_l2` evidence.

Reusable context is separated by trust:

```text
committed Knowledge/      canonical reference
reviewed facts            explicitly promoted operational lessons
governed Solutions        semantic-hash-approved reusable Helpdesk Solutions
historical cases          approved/rejected/reopened analogies and counterexamples
```

GBrain is isolated derivative search state. `trusted` recall searches only Knowledge, reviewed facts and governed Solutions. Historical cases require explicit case scopes and never become current-ticket proof by similarity alone.

## Learning

`Model_Bench/l2_learning_cycle.py` is a best-effort sidecar:

```text
reviewed/published/reopened outcomes
-> historical cases
-> conservative unverified candidates
-> GBrain synchronization
```

Learning failure does not block ticket processing.

`Model_Bench/l2_learning_curator.py` is the explicit operator promotion/rejection boundary for reusable facts. Small L2 workers do not write trusted memory or promote their own lessons.

## Governed Solutions

An active row in `dbo.Hermes_Solution_Article_Mst_Tbl` is not automatically trusted.

`Model_Bench/sync_l2_approved_solutions.py` exports a Solution only when its current semantic hash matches `deploy/solution_export_policy.json`. Drift fails closed until it is reviewed again.

## Profiles

Current profile topology:

```text
l2-investigator          gateway / Kanban dispatcher
l2-investigator-primary  investigator worker
l2-reviewer-primary      reviewer worker
```

## Deployment

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

## Validation

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Validation is local and covers lifecycle contracts, typed evidence boundaries, GBrain isolation, outcome learning and governed Solution export.

## Design rule

Keep one mechanism and one owner. A new subsystem should exist only when it represents a real XStudio/Helpdesk boundary or deterministic business rule that Hermes does not already provide. Benchmark harnesses, one-off repair scripts, duplicate indexes, unpinned Knowledge copies and speculative execution frameworks do not belong in the production tree.
