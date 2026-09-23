---
name: xstudio-l2-ticket-workflow
description: "Investigate one already-claimed XStudio L2 Helpdesk ticket and hand a structured proposal to deterministic Jev-primary review/publication."
version: 2.0.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, helpdesk, l2, investigation]
    related_skills: [xstudio-sql-write-discipline]
---

# XStudio L2 Ticket Workflow

Your card belongs to one claimed run (`run_id`, `ticket_id` on the card). Jev has already
routed the ticket and the harness has already read the live rows it needs. Your job is to
read that evidence, fill a gap if there is one, and submit one proposal. Claiming, review,
publication and workflow status are not yours.

## Tools

| Tool | Use |
|---|---|
| `xstudio_read_table(table)` | Read one table/view for this ticket. Give only the table name; the harness filters by the ticket's heat/work order/billet/document and picks the columns. |
| `xstudio_heat_context(heat)` / `xstudio_work_order_context(work_order)` / `xstudio_sap_api_context(api_type)` | Fixed cross-table evidence for one identifier. |
| `xstudio_get_ticket_context`, `xstudio_get_run_actions` | The ticket and this run's evidence (action IDs). |
| `l2_recall` | Prior cases and known fixes, only when needed. |
| `xstudio_submit_proposal` | Finish. Called once. |

You never write SQL, choose columns or WHERE clauses, write files or scripts, or use a shell.

## Procedure

1. Read the card's context view; the live probe rows and their action IDs are already there.
2. If they answer the ticket, submit.
3. Otherwise `xstudio_read_table` on the table that would hold the missing fact (the card lists
   Jev's candidates), or a context tool for the identifier.
4. Submit with `xstudio_submit_proposal`.

A ticket/user identifier is not proof of database storage representation (`H99328` may be
stored as `99328` or not at all). Absence of rows is evidence of absence, not of cause.

## Choosing the outcome

- **RESOLUTION**: verified finding with `resolution` and VERIFIED claims citing action IDs.
  This includes a ticket premise that live rows disprove (values match, record exists): say
  what the rows show and close. Do not leave a conclusively disproven concern open.
- **QUESTION**: only the requester can unblock (the heat/work order/time is not identifiable).
  Give `requester_question`. Do not sample unrelated rows.
- **UPDATE**: verified progress plus a concrete `next_investigation_step`.
- **NEEDS_HUMAN_ACTION**: cause and fix are known but need a data/config change you cannot make.
- **L3_ESCALATION**: cause unresolved, evidence contradictory, or no table covers the question.

## Submitting

```text
xstudio_submit_proposal(
  response_type="RESOLUTION",       # RESOLUTION|QUESTION|UPDATE|NEEDS_HUMAN_ACTION|L3_ESCALATION
  summary="<what was checked and found>",
  reply_text="<plain-language reply to the requester>",
  claim_status="VERIFIED",          # VERIFIED needs action_id
  action_id="<action ID from the rows you rely on>",
  resolution="<verified outcome>"   # RESOLUTION only
)
```

Write `reply_text` for the requester: what was checked, what was found, what happens next.
The submit call completes the card; stop after it succeeds.

## Rework cards

A rework card carries the reviewer's objection and an incremented `review_cycle`. Fix exactly
that objection with the least additional evidence, then submit a fresh proposal.
