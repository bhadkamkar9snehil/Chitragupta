---
name: xstudio-l2-ticket-workflow
description: "Investigate and hand off one Helpdesk L2 ticket as a Kanban-dispatched worker in Chitragupta's current single-board parent-gated pipeline."
version: 0.6.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, helpdesk, l2-support, ticket-workflow, kanban]
    related_skills: [xstudio-sql-write-discipline]
---

# XStudio L2 Ticket Workflow Skill

This skill describes the **current live Chitragupta workflow**.

`Model_Bench/ticket_scout.py` atomically claims a Helpdesk ticket and creates two
separate tasks on the **single default Kanban board**:

1. an investigator task assigned to `l2-investigator-primary`;
2. a reviewer task assigned to `l2-reviewer-primary`, created with the investigator
   task as its native `--parent` dependency.

The reviewer begins automatically when the investigator task completes. Hermes's
native parent handoff carries the investigator's structured completion metadata to
the reviewer. There is **no separate review board and no forward-bridge hop**.
`kanban_forward_bridge.py` is retired and must not be used.

The investigator never publishes directly. The reviewer only judges the proposed
answer. After reviewer approval, `kanban_approval_publisher.py` performs the real,
deterministic database publication. Reviewer rejection is handled by
`kanban_reject_bridge.py`, which creates a fresh rework task while preserving useful
findings from the rejected attempt.

## Non-negotiable evidence hierarchy

Use evidence in this order:

1. **Current live SQL/data for this ticket** — ground truth for ticket-specific facts.
2. **Verified `Knowledge/` documents and real schema/view catalogs** — authoritative
   product/domain reference material.
3. **Existing solution articles** — reusable hypotheses from prior resolved tickets;
   verify applicability against this ticket before reuse.
4. **Prior ledger/attempt findings for this same ticket** — preserve work, but re-check
   any fact that the final answer will depend on.
5. **mem0 memory** — operating hints only. Never treat memory as authoritative product
   truth, a schema source, or proof that a prior fix applies to this ticket.

A retrieved article, memory, prior attempt, table suggestion, or skill example is a
**lead, not evidence**. Claims in the final response must be supported by current data
or a verified authoritative source.

## Procedure

### 1. Read the dispatched task; never poll

Call `kanban_show()` for the task you were spawned with. Copy the exact `run_id` and
`ticket_id` from the task body. Do not reconstruct GUIDs from memory.

The ticket is already claimed. **Never call `--poll` from a worker.** Doing so can
claim an unrelated second ticket.

The task body is deliberately enriched by the deterministic dispatcher. It may
already contain:

- the full ticket context;
- mechanically suggested real tables/columns;
- a prior investigation ledger;
- exact interpreter/script/query commands.

Use that material instead of rediscovering environment details.

If a compact investigation bundle is not already present and you need the complete
starting context in one call, use the exact interpreter/script paths supplied in the
task and run:

```text
--database XStudio_Helpdesk --investigate-bundle <ticket_id>
```

`--investigate-bundle` returns ticket context, mechanically narrowed schema
candidates, the prior ledger, recent attempts, and known-solution candidates together.
Do not replace that one bundle with four or five separate context-assembly calls.

### 2. Check ticket type before domain routing

Inspect `HermesComplaintTypeName` first.

`Request for Customization` / `Request For Customization Rights` is not a normal SQL
L2 incident. Do not burn an investigation trying to make it fit a data domain. Hand
it off as an out-of-scope product/engineering request with an accurate explanation.

### 3. Understand the database boundary

`Complaint_Mst_Tbl` and Hermes runtime/KB tables live in `XStudio_Helpdesk`.
Production/operational data — heat, billet, CCM, EAF/LRF, quality, delays, work orders,
SAP posting/API data — lives in `XStudio_Xbatch`.

There is no production-table `TicketID` relationship. Correlate a Helpdesk ticket to
production data using identifiers actually present in the ticket, for example:

- HeatNo / HeatID
- InspectionLot
- WorkOrder / ManufacturingOrder
- BilletNo / SubLotNo
- SAP TransactionID
- EquipmentID

If the ticket does not contain the identifier required to investigate safely, ask for
it rather than inventing a join that does not exist.

### 4. Route narrowly, but do not force a single domain

Use the canonical routing knowledge under `Knowledge/` and the relevant domain skill.
Strong identifiers take precedence over vague natural-language classification.

Typical routes:

- SAP posting/API -> `xstudio-sap-api-investigation`
- heat/EAF/LRF/CCM/billet -> `xstudio-sohar-heat-execution`
- quality/delay/work-order -> `xstudio-quality-delay-workorder`
- unclear/cross-domain -> discovery path plus `xstudio-sql-write-discipline`

A route selects the starting evidence surface. It does not forbid following evidence
into another domain.

### 5. Treat retrieved knowledge as candidates, not answers

The investigation bundle may contain `known_solutions`. Do not automatically apply
them and do not perform a second legacy `--search-solutions <route>` call merely to
repeat the same lookup.

For every candidate solution:

1. compare its problem/root-cause pattern with this ticket;
2. verify the relevant live rows/views for this ticket;
3. reject it explicitly if current evidence contradicts it;
4. only reuse it when applicability is demonstrated.

Do not create or link a solution article yourself during investigation. Reusable KB
creation/linking belongs after reviewer-approved publication in the deterministic
publisher path.

### 6. Investigate using deterministic schema discovery first

Prefer the query commands supplied by the task.

When you know the entity, prefer `--build-query` because it validates the table and
columns against the real schema before execution.

When you do not know the entity, use `--suggest-tables` as a short-list generator.
Suggested tables are not verified answers. If the correct surface is absent, use
`--find-sql-objects` / live metadata discovery.

Use raw `--query` only for read-only investigation and always specify the database.
Never guess a table, view, procedure, or column because its name sounds plausible.

For writes, follow `xstudio-sql-write-discipline`. Ticket publication never goes
through an investigator's ad-hoc SQL write.

### 7. Preserve investigation state

Before completing a meaningful investigation, record a compact ledger using
`--save-ledger` for the current `run_id`.

A useful ledger records:

- tables/views actually queried;
- identifiers and key values found;
- hypotheses ruled out;
- evidence still missing;
- current conclusion.

Do not put per-ticket findings into shared mem0. The ledger is the correct home for
per-ticket episodic state and is carried into rework/retry flows.

### 8. Complete with structured metadata; never publish directly

Finish the investigator task with `kanban_complete` and structured metadata. This
completion automatically makes the parent-gated reviewer task eligible on the same
board.

Required publication fields are:

```text
response_type
reply_text
```

Also include the exact `run_id` and `ticket_id`, plus structured fields when known:

```text
problem_summary
findings
root_cause
resolution
new_ticket_status
```

Valid `response_type` values are exactly:

| Type | Use when |
|---|---|
| `UPDATE` | Investigation produced useful progress but is not yet a verified resolution. |
| `QUESTION` | A specific missing requester fact/identifier is required. |
| `RESOLUTION` | The fix/result is verified against live evidence. |
| `L3_ESCALATION` | The cause could not be determined or the investigation is genuinely beyond L2 capability. Do not invent a resolution. |
| `NEEDS_HUMAN_ACTION` | The cause and concrete fix are known, but execution requires a human or is outside the bot's write authority. Put the actionable step in `resolution`. |

Example shape:

```text
kanban_complete(
    summary="<one-sentence finding/proposal>",
    metadata={
        "run_id": "<exact run_id>",
        "ticket_id": "<exact ticket_id>",
        "response_type": "UPDATE | QUESTION | RESOLUTION | L3_ESCALATION | NEEDS_HUMAN_ACTION",
        "reply_text": "<complete support-facing response>",
        "problem_summary": "<optional>",
        "findings": "<optional>",
        "root_cause": "<optional>",
        "resolution": "<optional>",
        "new_ticket_status": "<optional>"
    }
)
```

`reply_text` must be self-contained and state what was actually checked, what was
found, and the next action if the case is incomplete.

**Do not call `--publish-response`. Do not create a reviewer task. Do not reassign the
investigator task. Do not call a retired model-based reviewer profile.** The existing
parent-gated reviewer and deterministic publisher own those steps.

### 9. Rework only the rejected point

A reviewer rejection arrives as a fresh `REWORK:` task created by
`kanban_reject_bridge.py`. Its body contains the review objection and prior findings.

Re-fetch current ticket state if the objection depends on mutable data, then address
the specific rejected claim. Reuse the carried ledger where valid; do not restart the
whole investigation unless the rejection genuinely invalidates the earlier evidence.

## Failure rules

- Tool unavailable: use only tools actually exposed in the current worker session.
- Identifier/table uncertain: discover/validate; do not guess.
- KB candidate conflicts with live data: live data wins; record the contradiction.
- Prior ledger conflicts with live data: live data wins; update the ledger.
- mem0 conflicts with repo/config/live evidence: ignore the memory and use the
  authoritative source.
- Missing essential ticket identifier: `QUESTION`, not fabricated inference.
- Cause diagnosed but execution outside bot authority: `NEEDS_HUMAN_ACTION`, not
  `L3_ESCALATION`.
- Cause genuinely unresolved after bounded investigation: `L3_ESCALATION`.
