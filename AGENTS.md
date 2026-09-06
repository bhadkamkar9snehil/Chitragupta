# Chitragupta Agent Contract

Chitragupta is the deterministic XStudio/Helpdesk L2 domain layer on the existing Hermes harness.

## Authority

`Model_Bench/l2_pipeline_runtime.py` is the single Helpdesk/Kanban lifecycle authority:

```text
eligible ticket
-> claim
-> investigator
-> frozen proposal
-> reviewer
   -> approve -> deterministic publish
   -> reject  -> bounded rework -> reviewer
```

Do not add parallel publisher, repair, forwarding, nudge, trace, memory, action-planning or reconciliation subsystems.

## Runtime topology

Hermes backend and GBrain run in WSL2 on the laptop. Hermes Web runs on laptop Windows. LM Studio runs on Windows on the desktop. Helpdesk/XStudio SQL Server is on another Windows VM.

The current Windows Python/pyodbc bridge is retained because it represents the proven SQL transport boundary. Do not remove it merely for architectural neatness; replace it only after a WSL-native path is proven equivalent.

## Model-facing tools

The only Chitragupta Hermes plugin is `xstudio-l2-tools`.

It exposes:

- `xstudio_l2` for typed live XStudio/Helpdesk evidence and run-ledger operations;
- `l2_recall` for read-only GBrain search.

Current-ticket claims require live evidence. Retrieved knowledge and historical cases are leads, not proof.

## Retrieval

GBrain indexes committed `Knowledge/`, committed `Reference Documents/`, reviewed facts, governed Solutions and reviewed historical cases as explicit non-federated sources.

Small L2 workers do not own durable memory writes or knowledge promotion.

## Learning

The current best-effort cycle is deliberately minimal:

```text
materialize reviewed outcomes
-> synchronize GBrain
```

There is no automatic candidate-mining or candidate-curation framework.

`sync_l2_approved_solutions.py` exports a Helpdesk Solution into trusted retrieval only when its semantic hash matches `deploy/solution_export_policy.json`.

## Profiles

```text
l2-investigator          Hermes gateway/dispatcher
l2-investigator-primary  investigator worker
l2-reviewer-primary      reviewer worker
```

## Repository rule

Keep one mechanism and one owner. Delete benchmark harnesses, one-off repair tools, generated duplicate indexes, speculative frameworks and compatibility wrappers once their real caller is gone.

`Knowledge/schema_allowlist.json` and the full schema/SP reference Markdown are intentionally retained because they serve different runtime/reference purposes.
