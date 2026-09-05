---
type: "Playbook"
title: "Deploy Hermes L2 SQL Runtime"
description: "Deployment sequence for the Hermes Helpdesk SQL runtime and deterministic L2 lifecycle."
tags:
  - hermes
  - deployment
  - sql
status: current
verified: "2026-09-05"
---

# Deploy Hermes L2 SQL Runtime

Target database:

```text
XStudio_Helpdesk
```

## 1. Deploy the generated complete SQL bundle

Run:

```text
Knowledge/00_Hermes_L2_FULL_INSTALL.sql
```

The numbered SQL files are the maintainable sources. The generated full-install bundle already includes the current hardening sources, including:

```text
Knowledge/25_ticket_dispatch_hardening.sql
Knowledge/55_update_retry_hardening.sql
```

Do **not** apply those two again merely because they exist as source files. When SQL runtime logic changes:

```text
edit the numbered source
-> regenerate 00_Hermes_L2_FULL_INSTALL.sql
-> deploy the generated bundle
```

Apply a separate overlay only when it is intentionally not yet part of the generated bundle.

## 2. Discover and bind the live Helpdesk workflow

Run the read-only discovery helper:

```bash
python Model_Bench/configure_helpdesk_workflow.py
```

Underlying SQL discovery:

```sql
EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;
```

The current checked-in deployment binding is:

```text
eligible ticket status:       Enter
resolved ticket status:       Closed
waiting-user AskStatus:       Ask
waiting-user ticket status:   unbound
L3 ticket status:             unbound
needs-human-action status:    unbound
```

Canonical file:

```text
deploy/helpdesk_workflow_binding.json
```

If live workflow values change, update the binding only from observed live values. Do not guess replacements.

`RESOLUTION` publication fails closed when `resolved_ticket_status` is not configured.

## 3. Run SQL postflight

Run:

```text
Knowledge/98_pipeline_postflight.sql
```

Then verify the Hermes-side pipeline from WSL:

```bash
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

Expected lifecycle contract:

```text
max_pipeline_wip = 1
review priority = 30
rework priority = 20
new investigation priority = 10
max_review_cycles = 3
```

No unexplained `ACTIVE_SQL_WITH_NO_KANBAN` anomaly should remain.

## 4. Deploy Hermes-side runtime, plugins, profiles, and skills

From the repository under WSL:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

This deploys:

- the central lifecycle runtime and small compatibility entrypoints;
- the event reconciler plugin;
- the typed `xstudio_l2` investigation plugin and bridge configuration;
- current investigator/reviewer SOULs and skills;
- workflow-binding fallback;
- current profile configuration changes.

The deployment script is intended to be idempotent.

## 5. Current lifecycle

```text
ticket_scout tick
  -> reconcile all in-flight work
  -> active SQL run?
       yes -> WIP_LIMIT; claim nothing
       no  -> claim one ticket
             -> investigator [10]
             -> normalize structured completion
             -> create reviewer [30] with frozen proposal_json
                  -> approve -> deterministic publish
                  -> reject  -> rework investigator [20]
                               -> normalize
                               -> fresh reviewer [30]
             -> bounded review_cycle -> human escalation when exhausted
```

Reviewer cards are created **after** the source completion becomes reviewable. There is no pre-created or parent-gated reviewer.

The 2-minute scout is the durable correctness backstop. Event hooks call the same reconciler for low-latency handoff but are not required for correctness.

See `Knowledge/L2_PIPELINE_STATE_MACHINE.md` for the normative lifecycle.

## 6. Local validation

Run:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

This is the project validation authority before deployment. Do not substitute a GitHub Actions result for inspection of the real local Windows/WSL/Hermes environment.

For the next naturally arriving ticket, confirm its trace uses `xstudio_l2` for database/schema work and does not attempt to recreate Python/pyodbc/sqlcmd transport.

## 7. Service identity and permissions

Use the real Hermes/XStudio service identity where the audited SQL runtime accepts a user ID.

The SQL login must have only the operational permissions required by the deterministic runtime across the relevant XStudio databases.

Investigators and reviewers do not directly update `Complaint_Mst_Tbl`; approved ticket publication goes through the audited deterministic path.
