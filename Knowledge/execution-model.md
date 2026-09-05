---
type: "Execution Model"
title: "Hermes L2 Execution Model"
description: "Deterministic ticket-to-investigation-to-review-to-publication sequence for the current Hermes L2 pipeline."
status: current
verified: "2026-09-05"
tags:
  - hermes
  - execution
  - l2
  - review
---

# Hermes L2 Execution Model

## Deterministic sequence

```text
1. ticket_scout reconciles all existing work.
2. If any active SQL run exists, claim nothing new (global WIP = 1).
3. Otherwise atomically claim one eligible Helpdesk ticket.
4. Create one investigator card at priority 10.
5. Investigator reads the dispatch bundle and routes the ticket.
6. Investigator uses xstudio_l2 for live database/schema/ticket/run evidence.
7. Investigator records meaningful ticket-specific evidence in the run ledger.
8. Investigator completes its own card with structured proposal metadata.
9. Reconciler normalizes the completion if required.
10. Only after the completion is reviewable, create a reviewer at priority 30.
11. Freeze the exact proposal into the reviewer card as proposal_json.
12. Reviewer independently verifies the proposal against live evidence.
13a. APPROVE -> deterministic publisher publishes that frozen proposal.
13b. REJECT  -> reconciler creates a rework investigator at priority 20.
14. Rework completion is normalized, then a fresh reviewer is created.
15. Bound review_cycle; after the configured cap, escalate rather than loop forever.
```

The LLM never choreographs these transitions.

## Structured proposal contract

A reviewable investigator/rework completion contains at least:

```text
run_id
ticket_id
response_type
reply_text
```

Optional structured fields may include:

```text
problem_summary
findings
root_cause
resolution
```

The normalizer may repair missing structural metadata from a sufficiently meaningful completion summary, but it does not invent a terminal resolution from ambiguous prose. Ambiguous normalized output defaults toward `UPDATE` rather than a fabricated `RESOLUTION`.

## Frozen reviewer input

A reviewer card carries:

```text
run_id
ticket_id
ticket_no
investigation_task_id
review_cycle
pipeline_stage: review
proposal_json: <exact structured proposal>
```

The reviewer judges `proposal_json`. The publisher later publishes that same frozen proposal. Neither stage reconstructs the candidate answer from mutable parent state or free-form comments.

## Investigation rules

The investigator should:

1. prefer the narrowest routed knowledge/evidence path;
2. treat project knowledge, old tickets, retrieval hits, and memory as leads;
3. verify ticket-specific claims live through `xstudio_l2`;
4. use `validate_identifiers` / `suggest_tables` / `find_objects` before guessing schema;
5. keep evidence calls bounded and change the evidence path after repeated identical failures;
6. never recreate Python/pyodbc/sqlcmd transport in terminal;
7. never execute arbitrary SQL writes or arbitrary stored procedures;
8. finish by emitting structured Kanban completion metadata, not by narrating that work is complete.

## Reviewer rules

The reviewer should verify the smallest sufficient evidence set for the proposal's core claim. It is not a second full investigation by default.

Approve only when the claim, response type, and proposed user-facing answer are supported. Reject with a specific actionable objection when evidence is missing, contradictory, or the response type is unsafe.

Reviewer lifecycle actions are only:

```text
kanban_complete -> approve
kanban_block    -> reject
```

## Response semantics

### UPDATE

Use when verified progress exists but the incident is not finally resolved. The SQL publish path supplies a default continuation eligibility window when none is explicitly provided.

### QUESTION

Use only when a specific requester fact is genuinely required. The deterministic workflow binding supplies the configured AskStatus / waiting state.

### RESOLUTION

Use only when the outcome is verified. Publication fails closed if `resolved_ticket_status` is not bound to an observed live Helpdesk value.

### NEEDS_HUMAN_ACTION

Use when the cause and required action are known but the L2 worker cannot execute that action through its approved interface.

### L3_ESCALATION

Use when the root cause remains unresolved, evidence is contradictory beyond L2 scope, or specialist/human investigation is genuinely required.

## Mutation boundary

The current worker-facing database interface is read-only. A production/configuration write is not an implicit next step after diagnosis.

```text
known cause + unauthorized corrective action -> NEEDS_HUMAN_ACTION
unknown/unresolved cause                    -> L3_ESCALATION
```

Ticket publication is different: it is an audited deterministic runtime action performed only after reviewer approval.

## Scheduling and liveness

- `ticket_scout.py` runs every 2 minutes and is the durable mutating backstop.
- `xstudio-l2-orchestrator` triggers the same reconciler after relevant Kanban lifecycle events for low-latency handoff.
- The event plugin is not required for correctness.
- Reviewer/rework priority is higher than new work so one inference slot finishes the current run before admitting another.
- Orphan recovery protects any run still referenced by Kanban state and only acts on true active-run orphans after the grace period.

## Completion rule

A ticket is not successfully handled because an agent stopped, a card changed status, or a SQL command returned success.

For a normal reviewed response:

```text
live evidence
-> structured proposal
-> normalization
-> independent review
-> approved frozen proposal
-> deterministic publish
-> published SQL/ticket state verified
```

For a rejected proposal:

```text
review rejection
-> bounded rework
-> normalization
-> fresh independent review
```

Only those deterministic states define pipeline progress.
