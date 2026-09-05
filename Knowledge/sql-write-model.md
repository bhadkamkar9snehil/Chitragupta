---
type: "Mutation Boundary"
title: "Hermes L2 SQL Mutation Boundary"
description: "Defines the current read-only L2 worker boundary and the safety rules for any future deterministic corrective-action surface."
status: current
verified: "2026-09-05"
tags:
  - hermes
  - sql
  - write
  - safety
---

# Hermes L2 SQL Mutation Boundary

## Current L2 workers are read-only

The investigator and reviewer do not have an arbitrary SQL write surface.

Their database interface is the typed `xstudio_l2` tool. Its agent-facing contract permits bounded reads/discovery and rejects write/DDL/EXEC SQL. Arbitrary stored-procedure execution is unavailable; `read_procedure` is limited to an explicit reviewed read-only allowlist.

This is a structural boundary, not a prompt preference.

## What happens when diagnosis implies a write

Do not improvise a write path through terminal, Python, pyodbc, sqlcmd, package installation, or an unreviewed procedure.

Classify the outcome instead:

```text
Cause known + exact corrective action known + worker not authorized
    -> NEEDS_HUMAN_ACTION

Cause unresolved / contradictory / genuinely beyond L2
    -> L3_ESCALATION
```

The response should include the evidence already gathered and, for `NEEDS_HUMAN_ACTION`, the specific action a human/operator should evaluate.

## Ticket publication is different

Publishing an approved L2 response is a deterministic runtime responsibility, not an investigator/reviewer write.

The publisher uses the audited Hermes SQL path after reviewer approval and applies only workflow states allowed by `deploy/helpdesk_workflow_binding.json`.

A model does not call the publisher directly and does not choose arbitrary Helpdesk status values.

## Future corrective-action harnesses

If a deterministic production-fix operation is added later, expose it as a narrow reviewed operation rather than reopening raw SQL mutation to the model.

For each such operation:

```text
1. resolve the real database/object
2. identify the official supported SP/API/trigger-mediated path
3. inspect the current signature/definition
4. explicitly allowlist the operation and parameters
5. capture before-state evidence
6. execute through harness-owned code
7. re-read the affected chain
8. audit target, parameters/action, before state, after state, and result
```

If no suitable official path exists, a direct write is an operator/development decision requiring its own explicit implementation and review. It is not an agent fallback.

## Why official-path-first still matters

XStudio/XMES stored procedures and triggers often perform linked business logic, logging, derived-row creation, SAP integration work, and state transitions. A procedure name alone does not prove whether it reads or writes.

Therefore discovery and definition inspection remain useful during diagnosis, but the L2 worker reads those definitions rather than executing unreviewed mutation procedures.

## Verification checklist

- [ ] All ticket-specific database evidence came through `xstudio_l2`.
- [ ] Table/column names were validated rather than guessed.
- [ ] No agent terminal call recreated a database transport.
- [ ] No arbitrary write/DDL/EXEC SQL was attempted.
- [ ] A required production/configuration mutation was represented as `NEEDS_HUMAN_ACTION` or `L3_ESCALATION`, not silently performed.
- [ ] Ticket publication, if approved, remained deterministic and workflow-bound.
