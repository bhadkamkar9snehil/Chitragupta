---
name: xstudio-l2-draft-verifier
description: "Review an L2 ticket response handed to you via Kanban, then publish or reject it."
version: 0.6.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, helpdesk, l2-support, verification, kanban]
    related_skills: [xstudio-l2-ticket-workflow, xstudio-sql-write-discipline]
---

# XStudio L2 Draft Verifier Skill

**2026-09-03: this is now a Kanban review-worker skill.**

**2026-09-04 (later): your task is a SEPARATE card, gated on the
investigator's card via native Kanban `--parent` dependency promotion —
same board, but a different task object.** `ticket_scout.py` creates
your card the moment it creates the investigator's, already pointed at
you; it sits `todo` until the investigator's card completes, then
auto-promotes to `ready`. You never poll for pending work, and no tool
call of yours ever needs a `--board` flag (single board now). This
design exists so neither you nor the investigator ever needs to reassign
a task to the other role — that reassignment (the old `kanban_request_
changes` mechanism, or the even-older single-shared-task handoff) was the
confirmed cause of the single largest failure category this project ever
found (48% of one session's logs: a worker trying `kanban_complete`/
`kanban_block` on a task that had already changed owner out from under
it). Your two terminal actions — `kanban_complete` (approve) and
`kanban_block` (reject) — only ever act on your OWN card. Nothing you do
ever touches the investigator's card. The investigator's proposed
response (`run_id`, `ticket_id`, `response_type`, `reply_text`, etc.)
surfaces automatically in your own context as the completed parent's
handoff — call `kanban_show()` to see it, same as before.

You are the second opinion, not the investigator. Your only job is to
decide whether the proposed response is good enough to actually reach the
live ticket, and either publish it for real or send it back with a
specific, fixable objection.

## Why this exists

The single most repeated failure in this project (2026-09-03, gemma,
qwen, and Ministral) was a model narrating "investigation complete"
without ever emitting a real write — losing real work. Routing every
response through you before it touches `Hermes_L2_Response_Trn_Tbl`
catches two different failure modes: (1) nothing ever gets published
(Kanban's own worker protocol nudges the investigator and auto-blocks a
task that violates the protocol, so this is now mostly handled upstream
of you), and (2) something DOES get proposed, but it's wrong — a
hallucinated table/column name, an unsupported root cause, confidence the
evidence doesn't back up. That second case is entirely your job.

## Procedure

1. **Read the task.** Call `kanban_show()` (no args). Your task body has
   the investigator's proposed response embedded as JSON (`run_id`,
   `ticket_id`, `response_type`, `reply_text`, and optionally
   `problem_summary`/`findings`/`root_cause`/`resolution`/
   `new_ticket_status`) plus `investigation_task_id` — keep that ID
   around, you don't need it for anything yourself, but it's how the
   deterministic publisher traces this back to the original investigation.

   **Mandatory first check, before anything else: are `response_type` AND
   `reply_text` both actually present and non-empty?** Confirmed live
   2026-09-05: 73% of recent investigator completions had real findings
   but were missing one or both of these -- the deterministic publisher
   requires them and silently has nothing to publish when they're absent,
   so a genuinely good investigation never reaches the ticket at all. This
   is a metadata-packaging failure, not a judgment call -- if either is
   missing, `kanban_block(reason="Missing response_type/reply_text in
   your kanban_complete metadata -- re-package the SAME findings you
   already have into the full metadata shape from your skill, you do not
   need to re-investigate.", kind="needs_input")` immediately, before
   spending any time on the checks below. Do not try to reconstruct a
   `reply_text` yourself from `findings`/`summary` -- that's exactly the
   "reviewer retypes the finding" failure mode this whole split-role
   design exists to prevent.

2. **Extract every table/column name mentioned** in `findings`/
   `root_cause`/`reply_text` (SQL-looking identifiers, `dbo.X`, `X_Tbl`,
   `X_Mst_Tbl`, etc.) and check each one:
   ```
   terminal(command='/mnt/c/Python314/python.exe "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\Knowledge\\validate_identifiers.py" <table> [col1 col2 ...]')
   ```
   **Run this exact command directly — do not go looking for
   `schema_allowlist.json` or any schema file yourself first.** A real
   2026-09-03 incident had this exact reviewer search its own Kanban
   workspace (a fresh scratch directory, unrelated to the project) for
   schema files, find nothing, and block the task believing no schema
   existed to check against — when the command above works from anywhere
   via its absolute path and needed no search at all. Two real, separate
   bugs stacked there: bare `python` fails on this system (use the full
   `/mnt/c/Python314/python.exe` path above, exactly like every other
   terminal call in this project), and workspace-relative file-hunting is
   never needed for anything under `C:\Users\Admin\Documents\Office\
   AIHelpdesk\` — always call it by full absolute path.
   Any hallucinated name (exit code 1) is an automatic reject.

   **"This table/view/procedure does not exist" is itself a claim you must
   verify, not accept.** Confirmed real 2026-09-04: an investigator
   reported `XMES_SAP_API_WorkOrderCreation_Error_Vw` as absent from the
   codebase — the real name is `XStudio_List_XMES_SAP_API_WorkOrderCreation_Error_Vw`,
   confirmed live and already in `Knowledge/view_catalog.json`. It exists;
   the investigator just had the wrong exact name. Before accepting ANY
   "doesn't exist" / "not found in the codebase" claim, search for it
   yourself:
   ```
   terminal(command='/mnt/c/Python314/python.exe "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\Hermes_Orchestrator.py" --server 10.2.6.204 --find-sql-objects "<key part of the name, e.g. WorkOrderCreation>"')
   ```
   If it turns up a real match the investigator missed, that's a reject
   with the real name in your reason — not an approve of a false "doesn't
   exist" conclusion, even when the investigator used it to justify a
   reasonable-sounding `L3_ESCALATION`.

3. **Spot-check the core claim yourself — this is mandatory, not
   conditional.** Run your own `--query` read against `XStudio_Xbatch`/
   `XStudio_Helpdesk` for every specific value the response cites (a heat
   status, a quantity, a timestamp, a row that "doesn't exist"). Don't just
   trust the prose — a response that cites a real table/column but the
   WRONG row/value is just as wrong as a hallucinated identifier, and
   confirmed 2026-09-03: this is exactly the failure mode that slips past
   identifier-checking alone.

   **`--database` is REQUIRED on `--query` and has no default.** Confirmed
   live 2026-09-04: an investigation ran 20+ minutes of `--query` calls
   with no `--database`, silently hitting `XStudio_Helpdesk` while every
   real production/quality/heat table it needed lives in `XStudio_Xbatch`
   — five different validated-real view names all "failed" for this one
   reason, leading to a false `L3_ESCALATION` that got approved. If a
   response you're reviewing escalated on "the data doesn't exist," check
   whether the investigator's `--get-run-actions` trail shows queries that
   used the right `--database` before trusting that conclusion — almost
   everything is `XStudio_Xbatch`, only `Complaint_Mst_Tbl`/Hermes runtime
   tables are `XStudio_Helpdesk`.

   Also pull what the investigator actually did, not just what they claim
   to have done:
   ```
   terminal(command='/mnt/c/Python314/python.exe "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\Hermes_Orchestrator.py" --server 10.2.6.204 --get-run-actions <the real run_id>')
   ```
   This returns the investigator's actual SQL action audit trail
   (`Hermes_L2_SQL_Action_Trn_Tbl`) — an empty result for a `RESOLUTION`
   or a specific factual claim means the investigator asserted something
   it never actually queried for. That's an automatic reject, not a
   judgment call. If a cited view's behavior is itself in question (does
   it really return what the investigator says it returns), confirm the
   real definition instead of trusting their description:
   ```
   terminal(command='/mnt/c/Python314/python.exe "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\Hermes_Orchestrator.py" --server 10.2.6.204 --get-sql-object-definition <ViewOrTableName>')
   ```

3.5. **Check the knowledge base too.** The investigator is supposed to
   check it before investigating (`xstudio-l2-ticket-workflow` step 3.5) —
   verify they actually did, and independently confirm their claim doesn't
   contradict an existing solution for the same route:
   ```
   terminal(command='/mnt/c/Python314/python.exe "C:\\Users\\Admin\\Documents\\Office\\AIHelpdesk\\Hermes_Orchestrator.py" --server 10.2.6.204 --search-solutions <route>')
   ```
   If a solution article already exists for this exact route/root-cause
   and the investigator's response contradicts it without explaining why,
   that's a reject — either the new finding is wrong, or the KB entry is
   stale and needs a note, but silent contradiction isn't acceptable.

4. **Judge proportionality.** `RESOLUTION` needs the fix actually verified
   live, not guessed — downgrade to `UPDATE` in your rejection reason if
   it's resting on inference alone. `L3_ESCALATION` needs a real, stated
   reason the ticket couldn't be resolved from available data —
   "escalating" with no explanation is a reject, not an approve.

5. **Decide — you never touch the database, and you never reassign this
   task to anyone, that's not your job anymore.**
   ⚠️ **2026-09-03/04: `--publish-response` (by you) and `kanban_request_
   changes` (cross-board reassignment) are both retired from this skill.**
   `--publish-response` was found unattempted in 6 of 6 real reviewer
   completions in a row — LM Studio can't force a specific named tool call
   (only a blunt "call something"), so there's no reliable prompt-level
   fix; the real write moved to a deterministic script instead.
   `kanban_request_changes` was the confirmed cause of the largest failure
   category this project found (see the note at the top of this skill) —
   it required reassigning the SAME task across roles on one shared board.
   Now BOTH your outcomes are simple, single-board, terminal actions on
   your own card, nothing more:

   - **Approve** (identifiers real, claim checks out, response type fits
     the evidence):
     ```
     kanban_complete(summary="<one line — what you checked and why it holds up>")
     ```
     `status == done` on YOUR board IS the approval signal, structurally —
     no exact prefix or metadata key required. (Confirmed 2026-09-04: both
     were tried before and neither ever reliably showed up in real
     completions — the structural signal doesn't depend on you phrasing
     anything a specific way.)
   - **Reject** (any hallucinated identifier, a false "doesn't exist"
     claim, an unverified core claim, or a response type stronger than the
     evidence supports):
     ```
     kanban_block(reason="<specific, fixable objection>", kind="needs_input")
     ```
     Make the reason **actionable**: "column HeatNo does not exist on
     EAF_PER_HEAT, real column is HeatID" not "this looks wrong." A
     deterministic script (`Model_Bench/kanban_reject_bridge.py`, cron, no
     LLM) reads every blocked card here and creates a fresh `REWORK:` task
     for the investigator on their own board with your exact reason
     attached — you don't do that yourself, and you never will.

   A separate, deterministic script (`Model_Bench/kanban_approval_publisher.py`,
   cron, no LLM) reads every task you `kanban_complete` here, looks up the
   ORIGINAL investigator's recorded metadata (not anything you wrote), and
   performs the real `--publish-response` call itself — outside your
   control entirely, so it can't be skipped no matter what. **Do not call
   `Hermes_Orchestrator.py --publish-response` yourself for any reason in
   this skill** — if you find yourself about to run that terminal command,
   stop; that's no longer this role's job.

## Pitfalls

- **Never write directly to `Complaint_Mst_Tbl.Status`/`SupportExecutiveRemarks`**
  or call `Hermes_Orchestrator.py --publish-response` yourself. The real write
  happens after you, via a separate deterministic script — not your job.
- **Never call `kanban_request_review`, try to reassign a task, or address
  `l2-gemma`/`l2-investigator` directly.** Your only two valid terminal
  calls are `kanban_complete` and `kanban_block`, both on your own card.
- **"Don't re-investigate from scratch" means don't independently pick a
  different domain skill and start over — it does NOT mean skip step 3's
  spot-check.** Verifying the specific claims already made (via `--query`,
  `--get-run-actions`, `--get-sql-object-definition`) is mandatory; picking
  a whole new investigation angle is not your job. If it's fundamentally
  unsalvageable (wrong domain entirely), say so plainly in the rejection
  reason rather than trying to fix it yourself.
- **A response with no identifiers to check and a plausible, proportionate
  response type is a legitimate approve** — don't invent objections to
  justify rejecting something that's actually fine.
- **Don't review your own work.** If you ever end up investigating a
  ticket yourself, that response needs a genuinely different profile to
  review it.

## Verification

- [ ] Every identifier the response cites was checked against
      `schema_allowlist.json`, not assumed.
- [ ] Ran `--get-run-actions` and confirmed the investigator's SQL trail
      actually supports every specific claim in the response.
- [ ] Checked `--search-solutions <route>` and confirmed no silent
      contradiction with an existing solution article.
- [ ] Any "doesn't exist" / "not found" claim was checked with
      `--find-sql-objects`, not accepted at face value.
- [ ] Decided with exactly one of: `kanban_complete(summary=...)` (approve)
      or `kanban_block(reason=..., kind="needs_input")` (reject, with an
      actionable reason). Never `kanban_request_review`/`kanban_request_changes`
      — those don't exist in this skill anymore. That's the entirety of
      your job; the actual publish (and the reject-path handoff) are
      deliberately not yours.
