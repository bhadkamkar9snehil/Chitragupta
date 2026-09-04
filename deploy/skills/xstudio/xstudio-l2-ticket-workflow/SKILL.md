---
name: xstudio-l2-ticket-workflow
description: "Investigate and hand off one Helpdesk L2 ticket, as a Kanban-dispatched worker."
version: 0.5.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, helpdesk, l2-support, ticket-workflow, kanban]
    related_skills: [xstudio-sql-write-discipline]
---

# XStudio L2 Ticket Workflow Skill

**2026-09-03: this is now a Kanban worker skill, not a poll-loop skill.**
A deterministic script (`ticket_scout.py`, cron on `l2-investigator`) does
the real SQL claim and creates one Kanban task per claimed ticket, assigned
to you. The Kanban dispatcher spawns you automatically when that task is
ready — you never poll for tickets yourself.

**2026-09-04: your tasks live on the `default` board; the reviewer's live
on a separate `l2-review` board.** You never touch the `l2-review` board
directly, and no tool call of yours ever needs a `--board` flag — the
dispatcher spawns you already scoped to the right one for whatever task
it gave you.

This is procedure, not domain knowledge — for what to actually check once
a ticket is claimed, this skill hands off to a domain-specific one (SAP/
API, Sohar heat execution, or quality/delay/work-order).

## When to Use

- The Kanban dispatcher spawned you for a task titled "L2 Ticket ...".
- Don't use for: XS_Builder/XStudio *configuration* work (a different,
  separate `xstudio` skill), or any ticket outside this deployment.

## Tool discipline (read this before your first tool call)

Only call tools that appear in your own available tool list for this turn.
A real 2026-09-03 incident had this exact model (Ministral-3-3B) call
`execute_code`, which isn't in this profile's enabled toolset at all — it
was refused ("BLOCKED"), wasting a full turn. If a tool name isn't visible
to you right now, it doesn't exist for this run; don't call it hoping it
works, and don't retry it a second way.

**Don't write ad-hoc Python scripts to compose reply text.** The same
incident had this model pipe a `python -e/-c` script through `terminal`
just to build a formatted string, and hit a syntax error from mismatched
quotes around an f-string. Compose reply text directly in your own
reasoning and pass it as a plain string argument. Reserve `terminal`'s
python calls for what actually needs it: `Hermes_Orchestrator.py`
invocations and real SQL/schema checks.

## Procedure

1. **Read your task.** Call `kanban_show()` (no args) to get the task body,
   which contains the real `run_id` and `ticket_id` (already claimed by
   `ticket_scout.py` — never call `--poll` yourself, there is nothing left
   to claim, and re-polling would just claim a SECOND, unrelated ticket).
   Do not type or recall the GUID from memory once you have it in hand —
   copy it exactly from the task body. A real 2026-09-03 incident had this
   exact model misstate an ID from memory in its first response.

   **Critical architecture fact, get this wrong and every subsequent query
   fails for a confusing reason:** `Complaint_Mst_Tbl` lives in
   `XStudio_Helpdesk`. Production/operational tables (heat, billet, CCM,
   EAF, SAP posting, etc.) live in `XStudio_Xbatch`. **There is no foreign
   key between them, and Xbatch tables will NEVER have a `TicketID`
   column.** The only link between a ticket and production data is
   whatever identifier (Heat Number, Lot Number, WorkOrderNo) is mentioned
   in the ticket's own `Description` text or `ExtractedEntitiesJson`. If
   neither contains one, that's a legitimate reason for a `QUESTION` — but
   the reason is "the ticket doesn't name a heat/lot," never "the
   production table doesn't reference tickets."

2. **Check the ticket TYPE before you check its domain.** Look at
   `HermesComplaintTypeName` in the task body. If it's `Request for
   Customization` or `Request For Customization Rights`, **stop here** —
   this is not something SQL investigation was ever going to resolve, no
   matter how well it maps to a domain skill. A real 2026-09-03 incident
   had this exact model see a transformer-voltage-checklist ticket typed
   `Request for Customization`, correctly notice it didn't fit any domain
   skill's investigation procedure, and wrongly conclude the ticket itself
   was ambiguous and needed a human to assign a domain — when the actual
   answer was simpler and already sitting in the ticket: **this ticket
   type is categorically out of scope for L2, regardless of what area or
   system it mentions.** `ticket_scout.py` already filters most of these
   out before claiming, but a straggler claimed before that filter existed
   (or any future edge case) can still reach you. Route it straight to
   `L3_ESCALATION` with the reason "this is a feature/customization
   request, not a bug or data question — routing to product/engineering,"
   not a `QUESTION` asking who owns the domain.

3. **Pick a domain skill** from the ticket's `ProblemCategory`/`AreaID`/
   free text, or consult
   `C:\Users\Admin\Documents\Office\AIHelpdesk\Knowledge\task-router.md`
   if the domain isn't obvious (SAP/API → `xstudio-sap-api-investigation`;
   EAF/LRF/CCM/billet/heat → `xstudio-sohar-heat-execution`; quality/
   delay/work-order → `xstudio-quality-delay-workorder`).

3.5. **Check the knowledge base BEFORE investigating from scratch.** A
   known-issue library now exists (`Hermes_Solution_Article_Mst_Tbl`,
   added 2026-09-03) — always check it first:
   ```
   terminal(command='/mnt/c/Python314/python.exe "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\Hermes_Orchestrator.py" --server 10.2.6.204 --search-solutions <route-from-task-router, e.g. heat_execution>')
   ```
   If a matching solution exists, **treat it as a strong starting hypothesis,
   not gospel** — still verify its ResolutionSteps against THIS ticket's
   actual live data before reusing it; don't paste an old answer onto a
   different real problem. If it genuinely fits, reference it in your
   `reply_text` and record the link in step 5 (`--link-solution`). If
   `--search-solutions` returns `[]`, the library has nothing for this
   route yet — proceed to investigate normally, and consider whether your
   finding is worth adding as a new solution (step 5).

4. **Investigate** using that domain skill's procedure, applying
   `xstudio-sql-write-discipline` for any write. For reads, use `--query`
   (never `sqlcmd`, not on PATH in this environment).

   **`--database` is REQUIRED on every `--query` call and has NO default —
   pick wrong and every table "doesn't exist."** Confirmed live 2026-09-04:
   a real investigation ran `--query` without `--database` for 20+ minutes,
   cycling through five different validated-real view names, every single
   one failing with "Invalid object name" — because the query was silently
   hitting `XStudio_Helpdesk` (the CLI's old default) while every real
   production/quality/heat/SAP table lives in `XStudio_Xbatch`. The CLI now
   refuses to run `--query` without an explicit `--database` at all — but
   don't rely on that alone, know which one you need:
   - `XStudio_Xbatch` — almost everything you investigate: heat, EAF/LRF/
     CCM, billet, quality, delay, work order, SAP posting/API.
   - `XStudio_Helpdesk` — only `Complaint_Mst_Tbl` and Hermes's own runtime
     tables (`Hermes_L2_*`, `Hermes_Ticket_*`, `Hermes_Solution_*`, etc).
   ```
   terminal(command='/mnt/c/Python314/python.exe "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\Hermes_Orchestrator.py" --server 10.2.6.204 --database XStudio_Xbatch --query "SELECT TOP 20 * FROM dbo.LRF_Per_Heat WHERE HeatNo = '"'"'H88210'"'"'"')
   ```
   **This is an illustrative example only** — `LRF_Per_Heat` is a real,
   verified table (confirmed live in `schema_allowlist.json`), but it is
   NOT necessarily the right table for YOUR ticket. A real 2026-09-03
   incident had a prior version of this example use a fabricated table
   name (`XSTUD_SOHAR_BILLET_TIMELINE`) that didn't exist at all — the
   model copied it literally instead of treating it as a format sample,
   burned 13+ minutes chasing it, and the fuzzy-match suggestion from
   `validate_identifiers.py` (string-similar, not semantically related)
   made it worse by pointing at unrelated shift tables. **Always pick the
   actual table for your ticket's domain from `sys.procedures`/
   `schema_allowlist.json` yourself** — never copy a table name out of
   this skill's own examples verbatim.
   ```
   ```
   `--query` auto-suggests a correction when a column/table name is wrong
   — retry once with the suggested name before escalating. Before an
   ad-hoc `SELECT` against an unfamiliar entity, check for an official
   read procedure first (`SELECT name FROM sys.procedures WHERE name LIKE
   '%<entity>%'`) — e.g. `SMS_GET_EAF_HeatIDList` already exists.

5. **Finish with a plain `kanban_complete` — you never publish directly,
   and you never hand off to the reviewer yourself either.**
   **2026-09-04: this changed from `kanban_request_review` to plain
   `kanban_complete`.** Investigator and reviewer now run on SEPARATE
   Kanban boards (`default` for you, `l2-review` for them) specifically so
   neither of you ever needs to reassign a task across roles — that
   reassignment was the real, confirmed cause of the single largest
   failure category this project ever found (48% of one session's logs
   showed a worker trying `kanban_complete`/`kanban_block` on a task that
   had already changed owner out from under it). A deterministic script
   (`Model_Bench/kanban_forward_bridge.py`, cron, no LLM) watches for your
   `done` tasks and creates the review-board card itself — that hop is no
   longer your job or any model's job. `reply_text` is
   the ONLY field a real support person ever actually sees on the ticket
   (it gets mirrored into `SupportExecutiveRemarks`/`AskRemarks` — the
   `problem_summary`/`findings`/`root_cause`/`resolution` fields only live
   in Hermes' own internal audit table). **Write `reply_text` as a
   complete, self-contained report, not a one-liner** — a real 2026-09-03
   finding confirmed every prior "successful" response left the visible
   ticket fields NULL because nothing mirrored the detailed fields there;
   now that mirroring is fixed mechanically, the CONTENT still needs to
   carry the substance. Follow the real, proven convention already used
   on this system's genuine historical tickets (checked live, not
   invented): open with a one-word context marker matching your
   `response_type` ("Investigation found...", "L3 escalation: live
   investigation confirms...", "Resolved via..."), then the real table/
   column-level specifics you actually checked, then — if incomplete —
   exactly what's still needed and why. Example, adapted from a real
   ticket: *"L3 escalation: Live XStudio_Xbatch investigation confirms
   that [specific table.column] stores [specific fact]. [What's missing/
   why this can't be resolved automatically]. [What L3/the requester needs
   to do next]."*
   ```
   kanban_complete(
       summary="<one sentence: what you found and what you're proposing>",
       metadata={
           "run_id": "<the real run_id from step 1>",
           "ticket_id": "<the real ticket_id from step 1>",
           "response_type": "UPDATE | QUESTION | RESOLUTION | L3_ESCALATION",
           "reply_text": "<the full, self-contained report — see above>",
           "problem_summary": "<or omit>",
           "findings": "<or omit>",
           "root_cause": "<or omit>",
           "resolution": "<or omit>",
           "new_ticket_status": "<or omit>"
       }
   )
   ```
   This is the ENTIRE terminal step — do not also call
   `Hermes_Orchestrator.py --publish-response` or `--draft-response`
   yourself, and do not try to reassign, reroute, or hand this task to
   `l2-gemma-verifier` in any way. Nothing reaches the live ticket until a
   reviewer on the SEPARATE `l2-review` board judges this metadata and a
   deterministic publisher writes it for real. This exists because the
   single biggest recurring failure this project has hit is a model
   narrating a finished investigation without ever emitting a real write —
   Kanban's own worker protocol also auto-nudges you if you're about to
   stop without calling `kanban_complete`/`kanban_block`, so there is a
   second layer catching this even if you forget.

5.5. **Log your work before handing off** (always, regardless of outcome —
   this is a work-log note, not a publish, and doesn't need review):
   ```
   terminal(command='/mnt/c/Python314/python.exe "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\Hermes_Orchestrator.py" --server 10.2.6.204 --log-activity --ticket-id <real ticket_id> --run-id <real run_id> --activity-type Note --note-text "<one-line summary of what you checked and found>"')
   ```

6. **If changes come back**, it arrives as a brand-new task titled
   `REWORK: ...` on YOUR board (`default`), created by
   `Model_Bench/kanban_reject_bridge.py` — not a respawn of your old task
   (that one stayed `done`, correctly, since you did finish your turn).
   The task body has the reviewer's exact objection plus the original
   `run_id`/`ticket_id`. Re-fetch the ticket via `--get-ticket-context`
   (its data may have changed since your first pass — don't trust stale
   context), fix exactly the stated problem, then follow the normal
   procedure to a fresh `kanban_complete` — don't restart the whole
   investigation unless the objection genuinely requires it.

## Quick Reference

| `response_type` | Use when |
|---|---|
| `UPDATE` | Investigated, have something useful, not a fix. Set `new_ticket_status: "Solution Work in Progress"`. Default case. |
| `QUESTION` | Need more info from the requester. |
| `RESOLUTION` | Fix verified live, not guessed. |
| `L3_ESCALATION` | Genuinely beyond SQL investigation, needs a human. |

## Pitfalls

- **Never write directly to `Complaint_Mst_Tbl.Status`/`SupportExecutiveRemarks`.**
  Everything goes through review + the deterministic publisher so the audit trail stays intact.
- **Never try to reassign this task to a reviewer, or address `l2-gemma-verifier` directly.**
  A plain `kanban_complete` with complete metadata is your entire job — the
  cross-board handoff is a deterministic script's job, not yours.
- **Don't invent a `new_ticket_status` value.** Re-check `--discover-workflow`
  if unsure whether a status is still live.
- **Don't fabricate certainty.** No useful finding → say so plainly in an
  `UPDATE`, don't invent a plausible root cause.
- **No scratch `.py`/`.sql` files in the project root.**

## Verification

- [ ] Checked `--search-solutions <route>` before investigating from scratch.
- [ ] Called `kanban_complete` with complete metadata (`run_id`, `ticket_id`,
      `response_type`, `reply_text` at minimum) before this turn ends —
      never `kanban_request_review` (removed 2026-09-04), never a reassign.
- [ ] Logged a work-log `Note` via `--log-activity` before handoff.
- [ ] Never called `--publish-response`/`--draft-response`/`--poll` yourself.
