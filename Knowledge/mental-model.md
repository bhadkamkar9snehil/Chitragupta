---
type: "Mental Model"
title: "Hermes L2 Mental Model"
description: "Defines the minimal L1/L2/L3 split and the role of SQL, routing, evidence, and existing XStudio Helpdesk workflows."
status: draft
tags:
  - hermes
  - l2-support
  - mental-model
---

# Hermes L2 Mental Model

## One-line model

```text
XStudio handles L1 and owns the Helpdesk.
Hermes reads unresolved L2 tickets, investigates the live system, writes the L2 result,
and resolves the ticket when it can. Humans receive only L3 escalations.
```

Hermes is not another Helpdesk and is not a separate chat application.

## What already exists

The supplied `XStudio_Helpdesk` snapshot already has the ticket record in
`dbo.Complaint_Mst_Tbl`. The table contains the ticket number, area, complaint type,
description, solution, status, priority, assignment, message/remarks fields and requester
details. The same Helpdesk database also contains area, complaint type, common-error,
priority and reference-document masters.

The snapshot also contains `dbo.systemreferencedocuments`, with existing user-guide
documents for Helpdesk, SMS KPI, billet yard, SMS/RM delay conditions, EAF/LRF/CCM KPI,
billet conditions and mill topics.

Therefore Hermes does not need a second ticketing/workflow product.

## Minimal runtime components

```text
Existing XStudio Helpdesk
        |
        | unresolved L2 ticket rows
        v
Hermes scheduled runner
        |
        v
ONE Hermes investigator
        |
        +--> SQL schema/SP discovery
        +--> SQL reads
        +--> SQL/SP writes when resolution requires them
        +--> existing project documents
        |
        v
Hermes L2 response table
        |
        +--> answer / ask for more information
        +--> resolution + existing ticket close/resolve workflow
        +--> L3 escalation
```

There is no permanent set of specialist bots.

A ticket may be decomposed into several investigation *steps*, but those steps are tool
calls executed by the same Hermes investigator. If parallel subtasks are introduced later,
they should be short-lived workers created only for a specific ticket, not a taxonomy of
long-running domain agents.

## No RAG dependency

Hermes knowledge is routed, not vector-searched.

The core knowledge sources are:

```text
OKF explainer/playbook docs
+ current SQL schema
+ current stored-procedure definitions
+ current operational rows
+ Helpdesk reference documents
```

When the exact object is unknown, Hermes searches SQL metadata and the local knowledge
catalog by identifiers/keywords. That is sufficient for the first system.

## SQL is both an evidence source and an action surface

Hermes is SQL-write capable.

For XStudio/XMES actions, use the XKB precedence:

```text
official supported path / installed stored procedure
-> inspected trigger-mediated path
-> direct table write when no suitable official path exists
```

This is not a read-only diagnostic architecture. The point of L2 is to investigate and,
where possible, fix the issue.

## Evidence levels

Hermes should keep the following distinction internally:

| Level | Meaning |
|---|---|
| Project knowledge | How this Hermes deployment is intended to work |
| Supplied snapshot | What the exported schema/SP files showed on 2026-09-02 |
| Live verified | What Hermes inspected in SQL for the current ticket |
| Runtime proven | The write/action was executed and its intended result was checked |

A dated export is a routing lead. Live SQL is the authority for the current incident.
