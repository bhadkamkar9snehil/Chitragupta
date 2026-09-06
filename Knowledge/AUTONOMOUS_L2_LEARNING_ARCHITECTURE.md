# Chitragupta L2 Architecture

Status: current branch contract.

## Product boundary

Hermes is the agent harness. Chitragupta is an XStudio/Helpdesk domain application running on Hermes.

Hermes owns model/session lifecycle, Kanban worker dispatch, gateway/scheduling, plugin/tool loading and durable conversation state.

Chitragupta owns only:

- deterministic Helpdesk claim/review/rework/publication semantics;
- typed XStudio/Helpdesk evidence access;
- trust-scoped GBrain indexing/retrieval;
- reviewed outcome history;
- governed reusable Solution export.

Do not add a second agent harness around Hermes.

## Deployment topology

```text
Laptop WSL2
  Hermes backend + Kanban + Chitragupta runtime + GBrain

Laptop Windows
  Hermes Web
  Windows Python/pyodbc bridge

Desktop Windows
  LM Studio inference server

Separate Windows VM
  Helpdesk / XStudio SQL Server
```

The Windows SQL bridge is a real environment boundary today. It should be removed only after a WSL-native SQL path is proven operationally equivalent.

## Runtime

```text
Helpdesk claim
-> investigator Kanban card
-> frozen proposal
-> reviewer Kanban card
   -> approve -> deterministic publish
   -> reject  -> bounded rework -> reviewer
```

The model never chooses lifecycle state or publishes directly.

## Model-facing tools

One Hermes plugin registers only:

- `xstudio_l2` — typed live XStudio/Helpdesk evidence and run-ledger operations;
- `l2_recall` — read-only source-scoped GBrain search.

Identity-sensitive XStudio calls are bound to the current Kanban task before crossing the SQL bridge.

## Evidence authority

1. current live XStudio/Helpdesk evidence;
2. committed Knowledge and Reference Documents, reviewed facts, governed Solutions;
3. approved/rejected/reopened historical cases.

Historical similarity is a lead, not proof.

## GBrain

GBrain is disposable derivative retrieval state under an isolated `GBRAIN_HOME`.

| Source | Content |
|---|---|
| `l2-knowledge` | committed `Knowledge/` |
| `l2-reference` | committed `Reference Documents/` |
| `l2-facts` | explicitly reviewed facts |
| `l2-solutions` | governed Solution exports |
| `l2-approved-cases` | reviewed/published successes |
| `l2-rejected-cases` | reviewer counterexamples |
| `l2-reopened-cases` | regressions/reopens |

All sources are non-federated. Chitragupta uses `gbrain search`; workers do not receive raw GBrain management or synthesis tools.

## Learning

The best-effort learning cycle has only two responsibilities:

```text
reviewed lifecycle outcomes
-> approved/rejected/reopened historical cases
-> GBrain synchronization
```

There is no automatic lesson-candidate miner or curator pipeline. GBrain can already retrieve the reviewed outcomes directly. Add canonical-promotion machinery later only if observed operations prove a need.

## Governed Solutions

A live active Solution row is not trusted by default. `sync_l2_approved_solutions.py` exports only semantic-hash-approved material from `deploy/solution_export_policy.json`.

## Mutation boundary

Autonomous L2 diagnoses and recommends. It does not execute arbitrary production/configuration changes. Known required changes outside the approved interface become `NEEDS_HUMAN_ACTION`; unresolved cases become `L3_ESCALATION`.

## Current justified files

| File | Reason |
|---|---|
| `l2_pipeline_runtime.py` | deterministic Helpdesk/Kanban lifecycle |
| `ticket_scout.py` | current scheduled wrapper; slated for consolidation into runtime |
| `xstudio_l2_tools_plugin/` | single Hermes domain plugin |
| `xstudio_l2_tool_bridge.py` | current WSL/Windows/pyodbc boundary |
| `l2_gbrain.py` | GBrain source/scope policy |
| `sync_l2_gbrain.py` | source convergence |
| `sync_l2_outcomes.py` | reviewed outcome materialization |
| `l2_learning_cycle.py` | outcome + GBrain convergence |
| `sync_l2_approved_solutions.py` | fail-closed Solution export |
| `solution_export_policy.json` | reviewed Solution hashes |

Every surviving file must continue to justify itself against the same question: why is Hermes or GBrain not already doing this?
