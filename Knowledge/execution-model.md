---
type: "Execution Model"
title: "Hermes L2 Execution Model"
description: "Deterministic ticket-to-investigation-to-resolution sequence for the Hermes L2 worker."
status: draft
tags:
  - hermes
  - execution
  - sql
  - l2
---

# Hermes L2 Execution Model

## Deterministic sequence

```text
1. Read unresolved L2 tickets from the existing Helpdesk table.
2. Choose the next ticket using the existing priority/workflow fields.
3. Load the ticket plus the full existing Helpdesk context.
4. Route the problem through `task-router.md` (human-readable) / `manifest.json` (its machine-readable mirror).
5. Load only the bounded explainer/playbook documents for that route.
6. Extract identifiers from the ticket: heat, WO, transaction ID, billet, sample, etc.
7. Inspect the current live SQL objects relevant to the route.
8. Investigate by SQL reads and existing read SPs/views.
9. If the fix requires SQL mutation:
      a. search for the current official SP/API/trigger path;
      b. inspect its current signature/definition;
      c. execute it when it covers the required action;
      d. otherwise perform the direct SQL write deliberately.
10. Re-read the affected objects and prove the intended result.
11. Insert one structured L2 response row.
12. Use the existing Helpdesk workflow to:
      - continue/ask the user,
      - resolve/close,
      - or escalate to L3.
```

## Scheduler behaviour

The scheduled runner is a dispatcher, not a second workflow engine.

It should query the existing Helpdesk ticket table and left-join the latest Hermes L2
response. A ticket needs Hermes work when, for example:

```text
it is currently in an existing unresolved-L2 state
AND
(
  no Hermes response exists
  OR the ticket changed after Hermes last observed it
  OR the previous Hermes result explicitly requires continuation
)
```

Exact unresolved/status values must come from the live Helpdesk workflow; this bundle does
not invent replacement status names.

## Resume instead of restart

The L2 response row stores the ticket's `ModifiedOn` value that Hermes saw plus the structured
investigation state. When a user supplies additional information, Hermes resumes using the
previous findings instead of discarding them.

## Investigation planning

Hermes does not need domain bots. It needs an ordered plan.

Example:

```text
Ticket: "Heat 12345 production is not posting to SAP"

Route: sap_posting

Plan:
1. locate Heat 12345 in heat/execution data
2. find production transaction row(s)
3. inspect SAPPostingStatus / Saptransactionid
4. inspect API transaction summary for that transaction
5. inspect raw API error log/error table if failed
6. inspect posting-sequence procedure definition if a retry/fix is needed
7. execute the appropriate existing write path if the problem is resolvable
8. verify transaction + production row after the action
9. write the Helpdesk L2 response
```

## Escalation to L3

Escalate only when Hermes cannot safely form or complete a technical resolution from the
current system state.

The L3 response should contain the investigation already completed, not merely the original
ticket text:

- problem statement
- identifiers
- live facts
- SQL objects inspected
- relevant SP definitions
- actions attempted
- observed result
- unresolved contradiction/failure boundary
- exact reason L3 is needed

## Completion rule

A successful SQL command is not enough.

For a write:

```text
intended write path
-> execution
-> target row/state changed as expected
-> dependent transaction/log/state checked
-> ticket response written
```

Only then should Hermes treat the technical action as complete.
