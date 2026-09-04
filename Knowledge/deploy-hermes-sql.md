---
type: "Playbook"
title: "Deploy Hermes L2 SQL Runtime"
description: "Deployment sequence for the Hermes Helpdesk tables and stored procedures without changing the existing Helpdesk ticket/workflow design."
tags:
  - "hermes"
  - "deployment"
  - "sql"
status: draft
---

# Deploy Hermes L2 SQL Runtime

## 1. Deploy runtime objects

Target:

```text
XStudio_Helpdesk
```

Run:

```text
sql/00_Hermes_L2_FULL_INSTALL.sql
```

This creates two tables and the Hermes stored-procedure surface.

It does not modify `Complaint_Mst_Tbl` schema.

## 2. Discover the live Helpdesk workflow

Run:

```sql
EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;
```

Record the current values for:

```text
unresolved L2 status(es)
resolved/closed status
L3 status
question/waiting AskStatus if applicable
```

Also inspect any current SP/trigger returned by the discovery procedure before deciding
whether Hermes should update `Complaint_Mst_Tbl.Status` directly or invoke an installed
workflow procedure.

The supplied Helpdesk SP export is only a dated snapshot.

## 3. Run postflight

```text
sql/99_postflight.sql
```

It checks:

- both Hermes tables exist;
- all expected Hermes procedures exist;
- no ticket has two active Hermes runs;
- no Hermes run/action is orphaned;
- current Helpdesk workflow discovery executes;
- current XBatch object discovery works.

## 4. Configure Hermes service identity

Use the service identity's real XStudio/user ID as `@HermesUserID` where available.

The SQL login needs the actual operational permissions you intend Hermes to have across:

```text
XStudio_Helpdesk
XStudio_Xbatch
relevant XStudio configuration databases
other project databases Hermes is expected to repair
```

The package itself does not artificially downgrade Hermes to read-only.

## 5. Cron loop

The application loop should be approximately:

```text
recover stale runs
-> get candidates
-> claim ticket
-> get ticket context
-> deterministic route
-> start investigation
-> inspect live SQL objects
-> execute reads/SPs/writes
-> persist investigation state during long work
-> QUESTION / RESOLUTION / L3_ESCALATION
```

No external queue is needed.

## 6. XStudio display

Create an XStudio LV/inline grid over `Hermes_L2_Response_Trn_Tbl` filtered by the current
ticket ID and display it inside the existing Helpdesk ticket page.

That is a UI/configuration task and should follow XKB's normal XStudio configuration route,
official-SP-first rule and postflight model. It is deliberately not mixed into the Hermes
runtime SQL package.
