---
type: "Reference"
title: "Hermes L2 Runtime Database Design"
description: "Defines the minimal SQL persistence model and stored-procedure surface used by the Hermes L2 worker."
tags:
  - "hermes"
  - "l2"
  - "sql"
  - "runtime"
status: draft
---

# Hermes L2 Runtime Database Design

## Minimal persistence

Hermes adds only two runtime tables to `XStudio_Helpdesk`.

```text
Complaint_Mst_Tbl                    existing ticket/workflow master
        |
        | ID = TicketID
        v
Hermes_L2_Response_Trn_Tbl           one row per Hermes attempt/run/reply
        |
        | ID = RunID
        v
Hermes_L2_SQL_Action_Trn_Tbl         SQL/SP reads and writes performed in that run
```

There is no queue table. There is no RAG table. There is no vector table. There is no
separate workflow database.

The existing Helpdesk remains authoritative for ticket status and lifecycle.

## Why a response row is also a run row

A Hermes attempt needs only enough state to:

- claim the ticket;
- avoid duplicate parallel work;
- survive/recover from a failed worker;
- preserve the routed problem statement and investigation;
- wait for a user reply;
- publish a resolution or L3 escalation.

`Hermes_L2_Response_Trn_Tbl` therefore carries both execution state and the eventual
structured L2 response. This avoids a redundant queue/run subsystem.

## SQL action table

Hermes is explicitly allowed to write SQL.

Every significant SQL or stored-procedure action can be executed through
`Hermes_L2_Execute_SQL_Usp`, which stores:

```text
ticket/run
action number
database/object
action type
SQL text
parameter summary
before evidence
after evidence
success/failure
row count
error
timestamps
```

This is an audit surface, not a policy engine.

The stored procedure does not restrict the statement to `SELECT`. Actual capability is
determined by the SQL login used by Hermes.

## XKB principle preserved

For an XStudio/XMES change, the reasoning order remains:

```text
route
-> inspect current object/SP/trigger
-> use the current official SP/API/trigger when it owns the operation
-> direct SQL when that is the correct/current path
-> postflight the affected state
```

The generic Hermes SQL executor is therefore not an excuse to ignore the existing XMES
stored procedures.

The supplied XBatch SP snapshot already demonstrates why definition inspection matters:
procedures such as `XMES_SAP_Posting_Sequence_Usp` modify posting states, while a name such
as `SAP_Posting_Data_ByHeat_Usp` can perform inserts rather than merely return "data".

## Workflow status values

The supplied schema export does not expose the `Status`/`AskStatus` values in its truncated
sample columns.

Hermes therefore does not hard-code invented workflow states.

Run:

```sql
EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;
```

and bind the actual current Helpdesk values in Hermes configuration.

The dispatcher receives the live unresolved-L2 statuses as `@EligibleStatusCsv`.
Resolution and L3 procedures receive the actual target status values as parameters.
