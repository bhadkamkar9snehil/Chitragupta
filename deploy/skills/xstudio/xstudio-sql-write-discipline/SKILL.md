---
name: xstudio-sql-write-discipline
description: "Enforce the L2 mutation boundary: diagnose through typed read-only tools and hand off any required write instead of improvising one."
version: 1.0.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, sql, write, safety, handoff]
    related_skills: [xstudio-l2-ticket-workflow]
---

# XStudio SQL Mutation Boundary Skill

This skill exists so an L2 worker stops at the right boundary when diagnosis suggests a write.

## Current rule

The L2 worker-facing database surface is `xstudio_l2` and is read-only for arbitrary SQL.

Do not use terminal, Python, pyodbc, sqlcmd, package installation, or an unreviewed stored procedure to create a write path that the typed tool does not expose.

## During investigation

Use typed operations instead of shell recipes:

```text
validate_identifiers  -> prove table/column names
suggest_tables        -> narrow candidate surfaces
find_objects          -> discover real procedures/views/triggers
get_definition        -> inspect current SQL definition
select / query        -> read live evidence
read_procedure        -> only the explicit reviewed read-only allowlist
get_run_actions       -> inspect audited run evidence
save_ledger           -> persist ticket-specific findings
```

A procedure definition may be useful evidence even when the procedure itself is not callable by the worker.

## If a corrective write is required

Classify the handoff:

### `NEEDS_HUMAN_ACTION`

Use when:

- root cause is known;
- the exact corrective action is known well enough to describe;
- the action is outside the current L2 worker's approved interface.

Include:

```text
what is wrong
which live evidence proves it
the exact object/record involved
the supported/likely corrective path if verified
what should be checked after the action
```

Do not claim the action was executed.

### `L3_ESCALATION`

Use when the root cause or safe corrective path is still unresolved, contradictory, or genuinely beyond L2.

## Official-path-first principle

For a human/operator or a future deterministic corrective-action harness, the preferred implementation order remains:

```text
resolve real target
-> find official supported SP/API/trigger-mediated path
-> inspect current definition/signature
-> explicitly review/allowlist it
-> capture before state
-> execute deterministically
-> verify affected chain
-> audit before/action/after/result
```

A direct SQL write is never an agent fallback. If one is required, it needs an explicit operator/development decision and implementation.

## Ticket publication is not your write

The investigator/reviewer never publishes `Complaint_Mst_Tbl` workflow state. After review approval, deterministic code publishes the frozen proposal through the audited Hermes SQL runtime using `deploy/helpdesk_workflow_binding.json`.

## Pitfalls

- A read-sounding procedure can still mutate data. Inspect definitions; do not infer safety from names.
- A copied KB example can be stale. Verify the current object before citing it.
- A model statement that “the fix was applied” is invalid without an approved execution surface and post-action evidence.
- A required write does not turn a read-only incident into a failed investigation; it often means `NEEDS_HUMAN_ACTION` is the correct L2 result.

## Verification

- [ ] Every ticket-specific identifier used in evidence was verified through the typed surface.
- [ ] No model-driven shell/database transport was used.
- [ ] No arbitrary write/DDL/EXEC was attempted.
- [ ] Any required mutation was handed off honestly rather than represented as executed.
- [ ] Any future deterministic corrective action would use an explicitly reviewed supported path plus before/after verification.
