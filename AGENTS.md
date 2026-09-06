# Chitragupta Agent Contract

Chitragupta is the deterministic L2 domain layer for the existing XStudio Helpdesk. Hermes is the agent harness.

Read `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md` for the current architecture and `README.md` for the operator overview.

## Authority

`Model_Bench/l2_pipeline_runtime.py` is the single Helpdesk/Kanban lifecycle authority.

Current lifecycle:

```text
eligible ticket
-> deterministic claim
-> investigator
-> normalize frozen proposal
-> reviewer
   -> approve -> deterministic publish
   -> reject  -> bounded rework -> reviewer
```

Current scheduling contract:

```text
new investigation  10
rework             20
review             30
global SQL WIP       1
max review cycles    3
```

Do not add parallel publisher, repair, review-board, forwarding, nudge, or orphan-recovery processes. Reconciliation is centralized in the lifecycle runtime.

## Evidence

Workers use the single `xstudio-l2-tools` Hermes plugin.

It exposes:

- `xstudio_l2` for typed XStudio/Helpdesk evidence and run-ledger writes;
- `l2_recall` for read-only trust-scoped GBrain retrieval.

Current-ticket claims require live `xstudio_l2` evidence. Retrieved knowledge and historical cases are leads, not proof.

The Windows bridge owns pyodbc/SQL transport. The model does not construct connection strings, interpreter commands, `sqlcmd`, package-install fallbacks, arbitrary writes, DDL, or arbitrary `EXEC`.

Identity-sensitive `xstudio_l2` calls are bound by the plugin to the current Hermes Kanban task.

## Helpdesk workflow

Models do not choose Helpdesk statuses. Deployment binding lives in:

```text
deploy/helpdesk_workflow_binding.json
```

The deterministic publisher publishes the exact frozen proposal approved by the reviewer and verifies persisted SQL/Helpdesk postconditions.

## Retrieval and learning

Authority order:

```text
live XStudio/Helpdesk evidence
> committed Knowledge + reviewed facts + governed Solutions
> historical approved/rejected/reopened cases
> unreviewed candidates
```

GBrain is isolated derivative retrieval state. `trusted` includes only canonical Knowledge, reviewed facts, and governed Solutions. Historical cases are explicit scopes and remain analogies/counterexamples.

Small L2 workers do not own durable memory writes or lesson promotion.

`Model_Bench/l2_learning_cycle.py` is best-effort only:

```text
materialize reviewed outcomes
-> mine conservative unverified candidates
-> synchronize GBrain
```

`Model_Bench/l2_learning_curator.py` is the explicit operator promotion/rejection boundary for reusable facts.

`Model_Bench/sync_l2_approved_solutions.py` exports a Helpdesk Solution into trusted retrieval only when its semantic hash matches `deploy/solution_export_policy.json`.

Learning failure must never become lifecycle failure.

## Profiles

Current deployed profiles:

```text
l2-investigator          Hermes gateway/dispatcher profile
l2-investigator-primary  investigator worker
l2-reviewer-primary      reviewer worker
```

There is one Chitragupta plugin: `xstudio-l2-tools`.

## Repository rules

Keep one mechanism and one owner.

Before adding a file or subsystem, identify its real current caller and the boundary it owns. Do not retain benchmark scripts, one-time repair utilities, generated duplicate indexes, speculative execution frameworks, alternate memory systems, or compatibility wrappers without an active need.

The runtime `Knowledge/schema_allowlist.json` is intentionally retained because the typed bridge reads it directly. Canonical domain reference belongs under `Knowledge/`; do not duplicate the same domain material into unpinned Hermes skills.

Edit numbered SQL sources rather than hand-editing the generated full install. Keep `Knowledge/00_Hermes_L2_FULL_INSTALL.sql` aligned with those sources.

## Deployment and validation

Deploy with:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

Validate locally with:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

When deleting or consolidating a runtime component, update deployment and aggregate validation in the same change.
