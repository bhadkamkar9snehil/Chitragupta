---
name: xstudio-l2-ticket-workflow
description: "Investigate one already-claimed XStudio L2 Helpdesk ticket, learn from prior experience without trusting it blindly, and hand a structured proposal to deterministic review."
version: 1.1.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, helpdesk, l2, investigation, review, learning]
    related_skills: [xstudio-sql-write-discipline]
---

# XStudio L2 Ticket Workflow

Use this skill only for an investigator/rework card that already belongs to one claimed L2 SQL run. Claiming, reviewer creation, rework scheduling, publication, and workflow transitions are deterministic runtime responsibilities.

## Current lifecycle

```text
claim
-> investigator
-> normalize completion
-> deferred reviewer with frozen proposal_json
   -> approve -> deterministic publish
   -> reject  -> rework investigator
                -> normalize
                -> fresh reviewer
```

There is one Kanban board. Reviewers are not pre-created and are not parent-gated.

## Start from the card

The task body identifies the run and ticket. Use those exact identifiers; do not poll or claim another ticket.

Expected fields include:

```text
run_id
ticket_id
ticket_no
review_cycle
pipeline_stage
```

## Database/tool contract

All database, schema, ticket, and ledger work goes through `xstudio_l2`.

Useful operations:

```text
get_ticket_context
suggest_tables
find_objects
get_definition
validate_identifiers
select
query
read_procedure
get_run_actions
save_ledger
```

Do not use terminal to run the orchestrator, Windows Python, sqlcmd, pyodbc, or package installation. The harness owns transport.

Raw `query` is read-only. Arbitrary `EXEC` and arbitrary SQL mutation are not available.

## Experience / learning contract

Chitragupta records every completed L2 turn into a shared local zvec learning vault. Recording is automatic; **generic automatic prefetch is intentionally disabled**.

Use `l2_recall` only when prior knowledge/experience can materially shorten or challenge the investigation:

```text
scope=trusted   -> normal prior reference/approved operational knowledge
scope=knowledge -> mirrored Git/skill reference
scope=facts     -> reviewed operational lessons
scope=solutions -> approved reusable Solution export when populated
scope=sessions  -> unverified historical experience/dead ends only
scope=candidates-> unreviewed learning candidates
```

A `sessions` hit may contain a rejected hypothesis or hallucination. Relevance is not authority. Verify current-ticket claims live through `xstudio_l2`.

When this run teaches a genuinely reusable lesson, `l2_lesson` may record a concise candidate plus concrete provenance. It creates only `unverified_candidate`; the model cannot promote its own lesson into trusted memory/KB. Never propose ticket IDs, specific Heat/Batch/WO identifiers, or one-off incident facts as reusable lessons.

## Investigation procedure

1. **Read the ticket/context.** Use the task body plus `get_ticket_context` when current ticket state matters.
2. **Route the ticket.** Use `Knowledge/manifest.json` / `task-router.md` and the narrowest domain skill.
3. **Extract strong identifiers.** Heat, work order, transaction ID, billet, inspection lot, equipment, etc. Prefer identifiers over speculative classification.
4. **Optionally recall trusted prior knowledge.** Use `l2_recall(scope="trusted")` when it can reduce search cost. Search `sessions` only for explicit forensic/history questions.
5. **Start with the narrowest high-value live read.** Prefer verified comprehensive views before hand-building joins.
6. **Discover rather than guess.** Use `suggest_tables`, `find_objects`, `get_definition`, and `validate_identifiers` when schema/object names are uncertain.
7. **Verify the actual incident.** Knowledge files, Solution articles, old tickets, Qdrant hits, mem0, and zvec session hits are leads; live ticket-specific evidence is the authority when available.
8. **Record meaningful findings.** Use `save_ledger` for ticket-specific evidence that the reviewer or later continuation should be able to inspect.
9. **Capture a reusable lesson only if warranted.** Use `l2_lesson` with evidence; do not force a lesson from every ticket.
10. **Choose the response type conservatively.**
11. **Complete your own Kanban card with structured metadata.** Do not publish the ticket yourself.

## Response types

### `RESOLUTION`

Use only when the outcome is verified strongly enough that the user-facing ticket may be closed after independent review.

### `QUESTION`

Use only when a specific requester fact is genuinely required and cannot be established from current evidence.

### `UPDATE`

Use when there is verified progress but no final outcome yet. This is safer than inventing a terminal result.

### `NEEDS_HUMAN_ACTION`

Use when the cause and required corrective action are known, but execution is outside the approved L2 worker interface.

### `L3_ESCALATION`

Use when the root cause remains unresolved, evidence is contradictory beyond L2 scope, or specialist/human investigation is genuinely required.

## Mutation boundary and future autonomy

A diagnosis may reveal a production/configuration write. Do not create a raw write path.

```text
known action but worker cannot execute -> NEEDS_HUMAN_ACTION
unresolved/beyond L2                -> L3_ESCALATION
```

Chitragupta is deliberately evolving toward a typed corrective-action registry with shadow, supervised, and autonomous capability modes. Until a specific action exists in that deterministic registry and is enabled by policy, this worker remains read-only. `xstudio-sql-write-discipline` defines the current boundary.

## Required completion metadata

Your `kanban_complete` must make the proposal structurally reviewable:

```json
{
  "run_id": "<exact run id>",
  "ticket_id": "<exact ticket id>",
  "response_type": "UPDATE|QUESTION|RESOLUTION|L3_ESCALATION|NEEDS_HUMAN_ACTION",
  "reply_text": "<user-facing proposed reply>"
}
```

Add useful structured fields when supported by evidence:

```text
problem_summary
findings
root_cause
resolution
```

Do not invent `new_ticket_status`; workflow state is harness-owned.

## Rework cards

A rework card remains part of the same SQL run and carries an incremented `review_cycle` plus the review objection. Fix that objection using the minimum additional evidence necessary, then complete the rework card with a fresh structured proposal.

After rework completion is normalized, the reconciler creates a **fresh reviewer**. The review cycle is not SQL `AttemptNo`.

## Completion rule

Do not end by saying “done” in prose. The required handoff is the structured Kanban completion. Publication happens later, deterministically, only after reviewer approval.
