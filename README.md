# Chitragupta — XStudio / Hermes L2 Helpdesk

Chitragupta is the XStudio/Helpdesk domain layer running on the Hermes agent harness. Hermes owns the agent loop, sessions, Kanban, gateways, scheduling, plugins and model integration. Chitragupta owns only the deterministic Helpdesk lifecycle, typed XStudio evidence boundary, GBrain source policy, reviewed outcome history and governed Solution export.

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

`Model_Bench/l2_pipeline_runtime.py` is the lifecycle authority. Global SQL WIP is 1. Review outranks rework, and rework outranks new investigation.

## Actual deployment topology

- Hermes backend: WSL2 on the laptop.
- Hermes Web: Windows on the laptop.
- LM Studio: Windows on the desktop.
- Helpdesk/XStudio SQL Server: separate Windows VM.
- The current typed XStudio bridge uses Windows Python/pyodbc. Keep that boundary until a WSL-native SQL path is deliberately proven equivalent.

## Hermes boundary

There is one Chitragupta Hermes plugin: `xstudio-l2-tools`.

It exposes:

- `xstudio_l2` — typed XStudio/Helpdesk evidence, schema discovery, ticket/run reads and investigation-ledger writes;
- `l2_recall` — read-only trust-scoped GBrain retrieval.

Generic worker terminal/file/browser/code-execution/memory-management surfaces are disabled for the autonomous L2 profiles.

## Evidence and retrieval

Current-ticket truth comes from live `xstudio_l2` evidence.

GBrain indexes explicit non-federated sources:

```text
l2-knowledge        committed Knowledge/
l2-reference        committed Reference Documents/
l2-facts            explicitly reviewed operational facts
l2-solutions        hash-approved reusable Helpdesk Solutions
l2-approved-cases   reviewed/published historical successes
l2-rejected-cases   reviewer-rejected counterexamples
l2-reopened-cases   regression/reopen signals
```

`trusted` retrieval contains only knowledge, references, reviewed facts and governed Solutions. Historical cases remain analogies/counterexamples and never become current-ticket proof by similarity alone.

## Learning

The current learning loop is intentionally minimal:

```text
reviewed/published/reopened outcomes
-> historical approved/rejected/reopened cases
-> GBrain synchronization
```

There is no automatic candidate-mining or candidate-promotion subsystem. If repeated experience later proves that explicit canonical promotion is valuable, add that capability from a real requirement rather than prebuilding a framework.

## Governed Solutions

An active row in `dbo.Hermes_Solution_Article_Mst_Tbl` is not automatically trusted.

`Model_Bench/sync_l2_approved_solutions.py` exports a Solution only when its current semantic hash matches `deploy/solution_export_policy.json`. Drift fails closed until reviewed again.

## Profiles

```text
l2-investigator          gateway / Kanban dispatcher
l2-investigator-primary  investigator worker
l2-reviewer-primary      reviewer worker
```

## Design rule

Keep one mechanism and one owner. A new Chitragupta subsystem must represent a real XStudio/Helpdesk boundary or deterministic business rule that Hermes or GBrain does not already provide.
