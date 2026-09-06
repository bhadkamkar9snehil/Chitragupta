---
name: xstudio-l2-ticket-workflow
description: "Investigate one already-claimed XStudio L2 Helpdesk ticket, learn from outcome-labelled prior experience without trusting it blindly, and hand a structured proposal to deterministic review."
version: 1.3.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, helpdesk, l2, investigation, review, learning, actions, identity]
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

The task body identifies the run and ticket. Expected fields include `run_id`, `ticket_id`, `ticket_no`, `review_cycle`, and `pipeline_stage`.

Those identifiers are not model authority. The `xstudio-l2-identity` guard resolves the actual Kanban card and injects its `run_id`/`ticket_id` into identity-sensitive evidence and action-plan calls. A conflicting identifier is blocked. Never copy an identifier from recall/history or try another one after an identity block.

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

Do not use terminal to run the orchestrator, Windows Python, sqlcmd, pyodbc, or package installation. The harness owns transport. Raw `query` is read-only. Arbitrary `EXEC` and arbitrary SQL mutation are not available.

For `select`, `query`, `read_procedure`, `get_run_actions`, and `save_ledger`, the current run is harness-bound. `get_ticket_context` is bound to the current ticket. Pure schema discovery can remain independent because discovering an object does not attach evidence to another incident.

## Experience / learning contract

Chitragupta records every completed L2 turn into a shared local zvec learning vault. Recording is automatic; **generic automatic prefetch is intentionally disabled**.

Use `l2_recall` only when prior knowledge/experience can materially shorten or challenge the investigation:

```text
scope=trusted        -> governed reference + promoted facts + approved reusable solutions
scope=knowledge      -> mirrored Git/skill reference
scope=facts          -> reviewed operational lessons
scope=solutions      -> approved reusable Solution export
scope=approved_cases -> historical proposals that passed review + publisher postconditions
scope=rejected_cases -> reviewer-rejected historical counterexamples
scope=reopened_cases -> historical resolutions later leaving terminal status
scope=cases          -> all outcome-labelled historical cases
scope=sessions       -> raw unverified historical turns/dead ends
scope=candidates     -> unreviewed learning candidates
```

`trusted` deliberately excludes historical cases. A successful old case is still an analogy, not a universal rule. A rejected case is a counterexample signal, not proof every statement was false. A reopened case is a regression signal, not a root-cause label. Verify current-ticket claims live through `xstudio_l2`.

The learning sidecar materializes reviewer/publisher outcomes and conservatively mines rejections, reopened resolutions, and repeated approved root-cause text into `unverified_candidate` artifacts. Automatic mining is not automatic promotion.

When this run teaches a genuinely reusable lesson, `l2_lesson` may also record a concise candidate plus concrete provenance. The model cannot promote its own lesson into trusted memory/KB.

## Corrective-action planning contract

`l2_action` is the model-facing surface for the future XBatch action registry. It currently exposes only:

```text
list
describe
plan
plans
validate_plan
```

There is deliberately no `execute` operation.

Use it only after the current root cause/action is known from live evidence. `plan` validates the registered capability's parameter schema and required evidence, hashes the capability contract, and writes an idempotent durable plan under the learning vault. The identity guard binds that plan to the actual current run/ticket even if the model omits those fields. The plan always has `execution_authorized=false`.

Do not invent a capability ID. Do not treat a plan as proof that the action is needed or was executed. Until a separate deterministic executor is introduced and a capability is deliberately promoted, a known corrective write still results in `NEEDS_HUMAN_ACTION`.

## Investigation procedure

1. **Read the ticket/context.** Use the task body plus `get_ticket_context` when current ticket state matters; identity is harness-bound.
2. **Route the ticket.** Use `Knowledge/manifest.json` / `task-router.md` and the narrowest domain skill.
3. **Extract strong identifiers.** Heat, work order, transaction ID, billet, inspection lot, equipment, etc.
4. **Optionally recall governed prior knowledge.** Use `l2_recall(scope="trusted")` when it can reduce search cost.
5. **Optionally inspect outcome-labelled historical cases.** Use the narrowest case scope when analogy/counterexample evidence is useful. Search raw `sessions` only for explicit forensic/history questions.
6. **Start with the narrowest high-value live read.** Prefer verified comprehensive views before hand-building joins.
7. **Discover rather than guess.** Use `suggest_tables`, `find_objects`, `get_definition`, and `validate_identifiers` when schema/object names are uncertain.
8. **Verify the actual incident.** Knowledge, old tickets, mem0, cases and sessions are leads; current live evidence is the authority.
9. **Record meaningful findings.** Use `save_ledger`; the identity guard ensures the ledger belongs to this run.
10. **If a corrective action is known, inspect the registry.** Use `l2_action list/describe`. If a matching recommend/shadow capability is active, create a validated plan with exact evidence references. If no capability matches, do not invent one.
11. **Capture a reusable lesson only if warranted.** Use `l2_lesson` with evidence; do not force a lesson from every ticket.
12. **Choose the response type conservatively and complete your own Kanban card.** Do not publish the ticket yourself.

## Response types

### `RESOLUTION`
Use only when the outcome is verified strongly enough that the user-facing ticket may be closed after independent review.

### `QUESTION`
Use only when a specific requester fact is genuinely required and cannot be established from current evidence.

### `UPDATE`
Use when there is verified progress but no final outcome yet.

### `NEEDS_HUMAN_ACTION`
Use when the cause and required corrective action are known, but execution is outside the approved L2 execution boundary. A shadow/recommend action plan may accompany this outcome; it does not change the fact that execution has not happened.

### `L3_ESCALATION`
Use when the root cause remains unresolved, evidence is contradictory beyond L2 scope, or specialist/human investigation is genuinely required.

## Mutation boundary and future autonomy

A diagnosis may reveal a production/configuration write. Do not create a raw write path.

```text
known action but no approved executor -> NEEDS_HUMAN_ACTION
unresolved/beyond L2                 -> L3_ESCALATION
```

Chitragupta progresses capability-by-capability through recommend -> shadow -> supervised -> autonomous. The current `l2_actions` surface is only planning. Future execution will sit behind a separate deterministic executor that re-checks capability version, harness identity, evidence, preconditions, approval, idempotency, postconditions and rollback at action time.

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

The completion metadata still names the current run/ticket because it is the lifecycle handoff, but do not use those fields to redirect evidence or action-plan provenance. Add useful structured fields when supported by evidence: `problem_summary`, `findings`, `root_cause`, `resolution`. If a shadow/recommend plan materially supports a `NEEDS_HUMAN_ACTION` proposal, mention its `plan_id` in `findings`/`resolution`; do not claim it executed. Do not invent `new_ticket_status`; workflow state is harness-owned.

## Rework cards

A rework card remains part of the same SQL run and carries an incremented `review_cycle` plus the review objection. Fix that objection using the minimum additional evidence necessary, then complete the rework card with a fresh structured proposal. After normalization, the reconciler creates a fresh reviewer. `review_cycle` is not SQL `AttemptNo`.

## Completion rule

Do not end by saying “done” in prose. The required handoff is the structured Kanban completion. Publication happens later, deterministically, only after reviewer approval.
