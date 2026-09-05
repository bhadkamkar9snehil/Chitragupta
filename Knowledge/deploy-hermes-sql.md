---
type: "Playbook"
title: "Deploy Hermes L2 SQL Runtime"
description: "Deployment sequence for the Hermes Helpdesk runtime and deterministic L2 pipeline hardening."
tags:
  - "hermes"
  - "deployment"
  - "sql"
status: current
---

# Deploy Hermes L2 SQL Runtime

Target database:

```text
XStudio_Helpdesk
```

## 1. Deploy the base runtime

Run the generated base bundle:

```text
Knowledge/00_Hermes_L2_FULL_INSTALL.sql
```

The generated bundle remains the base schema/procedure package.

## 2. Apply required pipeline hardening overlays

Apply after the base bundle:

```text
Knowledge/25_ticket_dispatch_hardening.sql
```

This changes candidate selection so non-L2 customization requests are excluded **before** `TOP (@BatchSize)`. Without it, 20 customization rows at the front of the queue can hide valid L2 incident tickets deeper in the queue and make the scout incorrectly return `NO_CLAIMABLE_TICKET`.

If additional numbered hardening overlays exist, apply them in numeric order after the base bundle.

These overlays are additive/idempotent `CREATE OR ALTER` deployment units. They exist so hardening can be deployed without hand-editing the generated full-install artifact.

## 3. Discover and bind the live Helpdesk workflow

Run:

```sql
EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;
```

Record the exact current values for:

```text
eligible/unresolved L2 status
resolved/closed status
question/waiting ticket status if applicable
question/waiting AskStatus if applicable
L3/human-action status if applicable
```

Do not guess values such as `Open`, `Closed`, `Resolved`, or `L3`.

Then populate:

```text
deploy/helpdesk_workflow_binding.json
```

or use:

```bash
python Model_Bench/configure_helpdesk_workflow.py
python Model_Bench/configure_helpdesk_workflow.py --write \
  --resolved-status "<EXACT LIVE VALUE>" \
  [--waiting-user-status "<EXACT LIVE VALUE>"] \
  [--waiting-user-ask-status "<EXACT LIVE VALUE>"] \
  [--l3-status "<EXACT LIVE VALUE>"]
```

`RESOLUTION` publication intentionally fails closed until `resolved_ticket_status` is bound. This prevents a Hermes run being marked resolved while the actual Helpdesk ticket remains visibly unresolved.

## 4. Run postflight

Run:

```text
Knowledge/99_postflight.sql
```

Then verify the pipeline itself from WSL:

```bash
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

Expected contract:

```text
max_pipeline_wip = 1
review priority  = 30
rework priority  = 20
new investigation priority = 10
max_review_cycles = 3
```

No unexplained `ACTIVE_SQL_WITH_NO_KANBAN` anomaly should remain.

## 5. Deploy Hermes-side scripts/plugins/skills

From the repo under WSL:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

This installs the centralized deterministic lifecycle runtime, compatibility entrypoints, event reconciler plugin, and current investigator/reviewer skills.

## 6. Runtime lifecycle

The application loop is now:

```text
ticket_scout tick
  -> reconcile all in-flight work
  -> if active SQL run exists: WIP_LIMIT, claim nothing
  -> otherwise atomically claim one ticket
  -> investigator card + parent-gated reviewer card
  -> reviewer approve -> deterministic publish
  -> reviewer reject -> rework card + fresh parent-gated reviewer
  -> review-cycle cap -> human escalation
```

The 2-minute scout is also the durable reconciliation backstop. Event hooks make handoffs immediate but are not required for correctness.

See `Knowledge/L2_PIPELINE_STATE_MACHINE.md` for the full contract.

## 7. Service identity and permissions

Use the service identity's real XStudio/user ID as `@HermesUserID` where available.

The SQL login needs the actual operational permissions intended for Hermes across:

```text
XStudio_Helpdesk
XStudio_Xbatch
relevant XStudio configuration databases
```

Ticket publication still goes through the audited Hermes stored-procedure path; investigators do not directly update `Complaint_Mst_Tbl`.
