---
type: "Reference"
title: "Helpdesk Workflow Binding for Hermes"
description: "Current deterministic binding between reviewed Hermes L2 responses and the existing XStudio Helpdesk workflow."
tags:
  - hermes
  - helpdesk
  - workflow
status: current
verified: "2026-09-05"
---

# Helpdesk Workflow Binding for Hermes

XStudio remains the workflow engine. Hermes publishes reviewed responses through the audited SQL runtime and uses only live-observed Helpdesk state values recorded in the deployment binding.

## Canonical deployment binding

The current binding is `deploy/helpdesk_workflow_binding.json`:

```json
{
  "eligible_ticket_status": "Enter",
  "resolved_ticket_status": "Closed",
  "waiting_user_ticket_status": null,
  "waiting_user_ask_status": "Ask",
  "l3_ticket_status": null,
  "needs_human_action_ticket_status": null,
  "strict_resolution_status_binding": true,
  "allow_metadata_status_override": false
}
```

`Closed` and `Ask` were bound from observed live workflow values. The null entries are intentionally unbound; they must not be replaced with guessed names.

If the Helpdesk workflow changes, rediscover it and update the binding from live evidence.

## Discovery

Use the deployment helper/read-only discovery path:

```bash
python Model_Bench/configure_helpdesk_workflow.py
```

The SQL discovery primitive is:

```sql
EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;
```

Do not infer status names such as `Open`, `Resolved`, `L3`, or `Waiting` from convention.

## Deterministic response mapping

The model proposes a `response_type`; deterministic code maps that type to the configured workflow fields.

### RESOLUTION

- Uses `resolved_ticket_status`.
- With `strict_resolution_status_binding = true`, publication fails closed if that status is absent.
- The run is not allowed to become resolved while the visible Helpdesk ticket remains unresolved.

### QUESTION

- Uses `waiting_user_ticket_status` when one is bound.
- Uses `waiting_user_ask_status` when one is bound.
- In the current binding, ticket Status is left unchanged and `AskStatus` becomes `Ask`.

### L3_ESCALATION

- Uses `l3_ticket_status` only when one is bound.
- With the current null binding, the runtime does not invent a ticket status.

### NEEDS_HUMAN_ACTION

- Uses `needs_human_action_ticket_status` when bound, otherwise falls back to `l3_ticket_status` when bound.
- With both currently null, the runtime records the structured response without inventing a workflow state.

### UPDATE

- Does not force a terminal Helpdesk status.
- The SQL publish path supplies continuation eligibility so useful progress is not treated as final resolution.

## Model status overrides are disabled

`allow_metadata_status_override` is currently false. A model-provided `new_ticket_status` is therefore ignored.

This prevents a plausible-sounding response from inventing or bypassing real Helpdesk workflow values.

## Structured L2 history

Detailed Hermes responses live in:

```text
Hermes_L2_Response_Trn_Tbl
```

linked by:

```text
Complaint_Mst_Tbl.ID = Hermes_L2_Response_Trn_Tbl.TicketID
```

Existing single-value remark fields are not the canonical Hermes history store. Mirroring to legacy fields is a deployment/publish-path concern, not an investigator action.

## Ownership rule

Investigators and reviewers never update `Complaint_Mst_Tbl` directly and never publish workflow states themselves. The deterministic publisher owns the approved transition and verifies the resulting SQL/ticket state.
