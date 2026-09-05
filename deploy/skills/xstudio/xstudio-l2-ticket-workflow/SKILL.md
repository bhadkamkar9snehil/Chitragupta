---
name: xstudio-l2-ticket-workflow
description: "Investigate one claimed XStudio L2 Helpdesk ticket and hand a structured proposal to the parent-gated reviewer."
version: 1.0.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, helpdesk, l2-support, kanban, investigation]
    related_skills: [xstudio-l2-draft-verifier, xstudio-sql-write-discipline]
---

# XStudio L2 Ticket Workflow

You investigate one already-claimed ticket. You never publish the live ticket yourself.

The deterministic pipeline owns the lifecycle:

```text
claim -> investigator -> reviewer -> publish
                        -> reject -> rework investigator -> fresh reviewer
```

The runtime deliberately limits global pipeline WIP to one active SQL run because the current LM Studio deployment has one safe inference slot. Review/rework work outranks new investigation work, so finish the ticket in front of you rather than trying to open another.

## 1. Read the task body as the starting context

The task contains exact mechanical identifiers:

```text
run_id
ticket_id
ticket_no
review_cycle
pipeline_stage
```

It also contains one **dispatch-time investigation bundle**. Do not immediately re-fetch the ticket, ledger, table suggestions, or KB through separate calls; that recreates the context-assembly turn cost this pipeline was built to remove.

Re-fetch ticket state only when mutable data may have changed or a rework objection specifically requires current state.

## 2. Use the dispatch bundle correctly

The bundle separates:

- current ticket context;
- deterministic schema candidates;
- prior ticket/run ledger;
- prior attempts;
- relevance-ranked `kb_retrieval` hits.

These have different trust levels.

```text
live SQL / verified Knowledge source > prior ticket finding > KB suggestion > mem0 heuristic
```

A KB hit or prior ledger is a lead. It is never ticket-specific proof.

## 3. Choose the right evidence surface

Use domain routing only as a starting point:

- SAP posting/API -> `xstudio-sap-api-investigation`
- heat/EAF/LRF/CCM/billet -> `xstudio-sohar-heat-execution`
- quality/delay/work-order -> `xstudio-quality-delay-workorder`
- unclear/cross-domain -> discovery plus `xstudio-sql-write-discipline`

Follow evidence across domains when necessary.

## 4. Query mechanically before querying creatively

All database, schema, ticket, run-audit and ledger work goes through the typed `xstudio_l2` tool. There is no shell path to the database: the harness owns the interpreter, the driver, the credentials, auditing, read-only enforcement and output limits. Do not use terminal to reach SQL, run an interpreter, import a database driver, or install packages — those are blocked, and attempting them only burns your call budget.

| Need | `xstudio_l2` operation |
|---|---|
| Read known table/view + columns | `select` (identifiers are schema-validated first) |
| Read-only SQL you composed | `query` (writes/DDL/EXEC rejected) |
| Narrow the schema from a symptom | `suggest_tables` |
| Find real tables/views/procedures | `find_objects` |
| Full definition of one object | `get_definition` |
| Confirm a table/column exists | `validate_identifiers` |
| Allowlisted diagnostic procedure | `read_procedure` |
| Refresh this ticket's live row | `get_ticket_context` |
| This run's recorded action trail | `get_run_actions` |
| Persist findings | `save_ledger` |

Rules that still apply:

- prefer `select` over `query` when the object is known — it validates table/view and column identifiers before constructing the SELECT;
- use `suggest_tables` as a shortlist only; if insufficient, use `find_objects`/`get_definition`;
- always pass `database` explicitly;
- use `XStudio_Xbatch` for production/process/quality/heat/SAP evidence;
- use `XStudio_Helpdesk` for ticket/Hermes runtime evidence;
- never invent a plausible table, view, procedure, or column.

Your investigation budget is bounded (about 14 `xstudio_l2` calls per session). Two identical failing calls block the third: change the arguments or the evidence path instead of retrying, and narrow a query rather than repeating a truncated one.

## 5. Use KB retrieval as a candidate search

The dispatch bundle contains `kb_retrieval` produced from requester-grounded problem text. It intentionally excludes `SuspectedCause` from the primary retrieval query to avoid confirmation bias.

For each returned hit:

1. compare symptom/root-cause pattern with the ticket;
2. verify applicability against current live rows/views;
3. reject the hit if current evidence contradicts it;
4. use it only after ticket-specific verification.

Do not repeat the retired route-only `--search-solutions <route>` call merely because a route exists.

If retrieval abstains, continue normal investigation. `NO GOOD KB MATCH` is valid.

## 6. Preserve ticket-specific investigation state

Before completing meaningful work, write a compact ledger through `xstudio_l2` `save_ledger` for the exact `run_id`.

Useful fields:

```text
tables/views actually queried
key identifiers and values found
hypotheses ruled out
evidence still missing
current conclusion
```

Do not write per-ticket facts to shared mem0.

## 7. Choose the response type from evidence

| Type | Use when |
|---|---|
| `UPDATE` | useful verified progress exists, but no final verified outcome yet |
| `QUESTION` | a specific requester fact/identifier is genuinely required |
| `RESOLUTION` | the fix/result is verified against live evidence |
| `L3_ESCALATION` | the cause remains unresolved or is genuinely beyond L2 capability |
| `NEEDS_HUMAN_ACTION` | cause and concrete fix are known, but execution is outside bot authority or requires a human |

Do not call something a resolution because it is plausible.

## 8. Complete with the full structured contract

Your only lifecycle write is `kanban_complete` on your own investigator/rework card.

Required metadata:

```text
run_id
ticket_id
response_type
reply_text
```

Include when known:

```text
problem_summary
findings
root_cause
resolution
new_ticket_status
```

Example:

```text
kanban_complete(
    summary="<one-sentence verified finding/proposal>",
    metadata={
        "run_id": "<exact run_id>",
        "ticket_id": "<exact ticket_id>",
        "response_type": "UPDATE | QUESTION | RESOLUTION | L3_ESCALATION | NEEDS_HUMAN_ACTION",
        "reply_text": "<self-contained support-facing response>",
        "problem_summary": "<optional>",
        "findings": "<optional>",
        "root_cause": "<optional>",
        "resolution": "<optional>"
    }
)
```

The deterministic runtime may normalize a substantive summary when a small model drops metadata, but that is a recovery mechanism, not permission to omit the contract.

`new_ticket_status` is not authoritative. The publisher uses the deployment's verified Helpdesk workflow binding; do not guess a status name.

## 9. Rework behavior

A reviewer rejection arrives as a fresh `REWORK[n]` investigator card containing:

- the exact reviewer objection;
- the prior investigation task ID;
- prior findings/ledger where available;
- the same SQL run ID;
- a new `review_cycle` value.

Fix the rejected point. Reuse already verified evidence. Do not restart from zero unless the objection invalidates the earlier investigation.

Every rework gets its own fresh parent-gated reviewer. The runtime caps review cycles and escalates instead of looping forever.

## Prohibited actions

- Do not publish the response yourself; the deterministic publisher owns that.
- Do not write directly to `Complaint_Mst_Tbl`.
- Do not create a reviewer card yourself.
- Do not reassign the investigator task.
- Do not use retired two-board/forward-bridge/request-changes flow.
- Do not treat KB, prior ticket history, or mem0 as proof.
- Do not guess a Helpdesk workflow status.
- Do not reach the database through terminal, an interpreter, a driver import, or a package install. Use `xstudio_l2`; those paths are blocked and only waste budget.

## Completion checklist

- [ ] Exact ticket/run IDs preserved mechanically.
- [ ] Current live evidence supports every specific factual claim.
- [ ] Evidence gathered through `xstudio_l2`, with `database` set on every read.
- [ ] Any KB hit was verified for applicability.
- [ ] Ledger saved for meaningful investigation/rework.
- [ ] Response type matches evidence strength.
- [ ] `kanban_complete` includes `response_type` and `reply_text` metadata.
