# Chitragupta L2 Pipeline State Machine

Status: **runtime contract**


This document defines the lifecycle implemented by `Model_Bench/l2_pipeline_runtime.py`.
If this document and the runtime disagree, fix the drift immediately.

## 1. Core invariant

### Worker failure recovery (2026-09-07)

All mutating CLI entrypoints take the same WSL process lock, including scout,
completion hooks and operator reconciliation. SQL lookup failure aborts the pass;
it is never evidence that a run is inactive. Windows mutation entrypoints refuse
execution; invoke the configured WSL environment to share ownership.

New cards allow one Hermes process attempt. A blocked card with an ended crashed,
failed or timed-out attempt is recovered by central reconciliation into a fresh
rework card under the same SQL run. Running attempts and explicit reviewer
rejections do not enter this path. Rework uses the existing bounded cycle budget
and exact-source idempotency key. The escalation handoff is persisted before
failing/releasing the SQL run, so a failed handoff remains retryable.

Before new claims or failed-worker rework, the runtime probes the typed SQL bridge
and configured models' structured tool calling. A failed dependency probe pauses
that tick; subsequent scout ticks retry the probe. This is a dependency gate,
not proof that a model will solve an arbitrary ticket.

Primary investigator and reviewer sessions currently have a 65,792-token context
budget, 8,192-token output cap and 20-turn limit (verified in the deployed profiles
on 2026-09-18). Their available tools are file, skills,
Kanban and typed XStudio evidence. These bounds must be validated against actual
worker traces whenever the model deployment changes.

The current LM Studio deployment has one safe local inference slot. Chitragupta therefore uses Jev/System One to remove bounded classification, selection, and review work from that slot.

Global SQL pipeline WIP remains one active Hermes run.

```text
local deep-review priority     30
rework investigation           20
new investigation              10
```

A fresh Helpdesk claim is allowed only when `Hermes_L2_Response_Trn_Tbl` has no active run after reconciliation.

## 2. Normal lifecycle

```text
Complaint_Mst_Tbl Status=eligible
          |
          v
Hermes_L2_Claim_Ticket_Usp
          |
          v
JEV TRIAGE
  route / ambiguity / complexity /
  live-state/schema/known-issue likelihood
          |
          v
deterministic real candidates
          |
          v
JEV EVIDENCE PLAN
          |
          v
identifier-bounded probe_table reads
(max 3; no strong identifier => no broad automatic probe)
          |
          v
JEV INVESTIGATION ASSESSMENT
          |
          v
l2-jev-investigator card [priority 10]
  COMPOSE_ONLY or FOCUSED_REASONING
          |
          | kanban_complete(metadata)
          v
normalize / validate frozen proposal
          |
          v
JEV PRIMARY REVIEW
      /          |             |              \
 APPROVE       REWORK      L3_ESCALATION   LOCAL_REVIEW
    |             |             |              |
    v             v             v              v
 PUBLISH      REWORK[+1]     L3 path      qwen reviewer
                                                  |
                                           approve / reject
                                             |        |
                                             v        v
                                          PUBLISH   REWORK
```

The local reviewer is no longer mandatory. It is an exception path for Jev uncertainty, conflicting evidence, low confidence, service unavailability, or cases where Jev explicitly says deeper System-2 reasoning is useful.

Missing requester-only information uses QUESTION with an explicit customer question,
not recurring UPDATEs. The flat proposal adapter preserves investigative notes and
uses the requester question as the frozen reply. RESOLUTION publication requires
COMPLETE evidence, verified material claims with current-run references, and an
explicit verified resolution outcome. An incomplete or diagnosis-only resolution
returns to the existing bounded rework loop even if a reviewer approved it.
An incomplete UPDATE must specify `next_investigation_step`; missing continuation
is returned for bounded rework before publication. A requester-dependent step must
instead be a QUESTION. Reviewer turn instructions are role-specific, and reviewers
cannot use the investigator proposal-submission tool.

## 3. Jev-first investigation contract

The runtime assembles evidence before the local investigator receives its card.

The order is:

1. requester-grounded KB/route query;
2. Jev parallel ticket characterization;
3. deterministic schema candidate generation;
4. Jev candidate selection/rating;
5. deterministic `probe_table` reads for the highest-value candidates;
6. Jev assessment of the resulting evidence package;
7. local coordinator receives the compact package.

`probe_table` is deliberately conservative:

- the table/view must exist in `Knowledge/schema_allowlist.json`;
- a strong ticket identifier such as HeatNo, BatchNo, TransactionID, WorkOrder, ProductionOrder, MaterialDocument, RecipeNo, or Equipment must map to a real column;
- the query is built mechanically through the existing guarded query builder;
- output is bounded;
- if no identifier maps, automatic probing returns `probe_possible=false` rather than issuing a broad read.

When Jev returns high evidence sufficiency and low need for deeper reasoning, the local profile is `COMPOSE_ONLY` and gets at most one additional live read. Otherwise it is `FOCUSED_REASONING` with a small additional-read budget.

The default profile is:

```text
l2-jev-investigator
```

`l2-investigator-primary` remains a compatibility/fallback profile.

## 4. Frozen proposal contract

The local investigator/rework worker completes with structured metadata. At minimum:

```text
run_id
ticket_id
response_type
reply_text
```

and, when supported:

```text
problem_summary
findings
root_cause
resolution
```

The deterministic runtime normalizes this into one frozen proposal. Jev primary review and any local fallback reviewer judge that exact proposal.

No reviewer or publisher should reconstruct a different proposal from free-form comments.

## 5. Jev primary review

Jev primary review is a bounded System One workflow, not a free-form reviewer agent.

Its main decision is:

```text
APPROVE
REWORK
LOCAL_REVIEW
L3_ESCALATION
```

It also independently judges evidence support, overclaim, performed-action claims, action-audit support, root-cause establishment, response-type fit, need for deep local reasoning, and publication risk.

Deterministic code—not Jev—owns the thresholds for directly acting on a typed review.

A direct Jev approval currently requires all of the following:

```text
decision                APPROVE
decision confidence     >= 0.82
evidence support        >= 0.80
overclaim probability   <= 0.20
response-type fit       >= 0.80
deep-reasoning need     <= 0.30
publication-risk score  <= 0.85
performed-action claim  absent OR action audit support >= 0.80
RESOLUTION              root-cause establishment >= 0.72
```

High-confidence `REWORK` or `L3_ESCALATION` currently require decision confidence >= 0.88.

If an approval misses any safety gate, it does **not** publish. It falls to `LOCAL_REVIEW`.

## 6. Local deep-review fallback

A local reviewer card is created only for the fallback path.

It carries:

```text
run_id
ticket_id
ticket_no
investigation_task_id
review_cycle
pipeline_stage: review
proposal_json: <frozen proposal including Jev primary review>
```

The reviewer should inspect the exact uncertainty that caused fallback and perform the smallest sufficient live verification. It must not restart the investigation by default.

Its only lifecycle outputs are:

```text
kanban_complete -> approve frozen proposal
kanban_block    -> reject with one actionable reason
```

The reviewer never publishes or mutates Helpdesk state.

## 7. One deterministic publication path

Both Jev direct approval and local-review approval call the same `_publish_frozen_proposal()` path.

That path:

1. confirms the run is still active and not already published;
2. applies `deploy/helpdesk_workflow_binding.json`;
3. calls the audited `Hermes_Orchestrator.py --publish-response --force-run-id` path;
4. verifies SQL/Helpdesk postconditions;
5. writes the human-readable ticket activity.

Jev and the local reviewer do not choose raw Helpdesk status names.

## 8. Rework-cycle semantics

`review_cycle` remains separate from SQL `AttemptNo`.

```text
cycle 0 = initial proposal
cycle 1 = first focused rework
cycle 2 = second focused rework
```

`MAX_REVIEW_CYCLES = 3` means a rejection/rework request at the cap escalates instead of creating an unbounded loop.

A Jev `REWORK` and a local-review rejection use the same deterministic rework path and preserve prior verified findings in the ledger.

## 9. Jev state and observability

Jev is another bounded investigator/reviewer of the same run. It does not have a separate business table.

Stage summaries live on `Hermes_L2_Response_Trn_Tbl`:

```text
JevTriageJson
JevInvestigationJson
JevReviewJson
JevTraceJson
JevKBCurationJson
ReviewMode
JevReviewDecision
JevReviewConfidence
JevRiskScore
LocalReviewRequired
JevModel
JevReviewedOn
```

Detailed System One calls reuse `Hermes_Agent_Trace_Trn_Tbl` with `EventType='jev_system_one'`.

KB retrieval telemetry also reuses Agent Trace.

## 10. Trace assessment

`xstudio-l2-trace` remains a cheap local observer and does not call TypeSafe in the hot hook.

After `drain_l2_trace_log.py` persists events, Jev assesses completed runs for:

- task completion;
- evidence actually gathered;
- silent failure;
- false success;
- unnecessary tool repetition;
- investigation efficiency;
- policy violation;
- transport flailing;
- human-attention need and priority;
- failure class.

This feeds semantic quality reporting and model comparison without making the trace hook a network dependency.

## 11. KB lifecycle

Route similarity or semantic similarity is not truth.

Normal retrieval uses governed approved Solution articles, then Jev adds:

- relevance;
- applicability;
- negative-indicator probability;
- same-failure-pattern probability;
- same-root-cause-family probability.

Current-ticket claims still require live evidence.

After a verified `RESOLUTION`, Jev may suggest:

```text
REUSE_EXISTING
UPDATE_EXISTING
CREATE_CANDIDATE
NONE
```

That suggestion does not directly promote or mutate an article.

## 12. Helpdesk workflow binding

Workflow status names remain deterministic configuration.

Canonical deployment file:

```text
deploy/helpdesk_workflow_binding.json
```

Current live-verified values remain:

```text
eligible_ticket_status            Enter
resolved_ticket_status            Closed
waiting_user_ask_status           Ask
l3_ticket_status                  null
needs_human_action_ticket_status  null
```

When strict resolution binding is enabled, `RESOLUTION` fails closed if the resolved ticket status is not configured.

## 13. Reconciliation ordering

One reconciler owns lifecycle mutation.

Current synchronous order:

```text
1. normalize investigator/rework completions
2. convert unreviewable completions into bounded rework
3. run Jev primary reviews
     - direct approve/publish where safety gates pass
     - direct focused rework where accepted
     - direct L3 escalation where accepted
     - create local reviewer only for fallback
4. process local-review rejections
5. process local-review approvals through the same publisher
6. recover true SQL/Kanban orphans
```

Do not restore separate publisher/reject/reviewer schedulers.

## 14. Event delivery and backstop

`xstudio-l2-orchestrator` triggers reconciliation after successful Kanban completion/block events.

Event delivery is the fast path.

The 2-minute `ticket_scout.py` run remains the durable reconcile-first backstop and only claims when global WIP is zero.

## 15. Stale/orphan recovery

Age alone never makes a run stale.

Any Kanban card referencing the exact run protects it, including investigation, rework, or local-review fallback.

A run is auto-failed for clean retry only when it is active in SQL, has no Kanban task referencing it, and exceeds the orphan grace period.

## 16. Candidate filtering / UPDATE continuation

`Knowledge/25_ticket_dispatch_hardening.sql` performs non-L2 customization filtering before `TOP (@BatchSize)`.

`Knowledge/55_update_retry_hardening.sql` provides bounded continuation behavior for published `UPDATE` responses.

Both are part of the generated full-install bundle.

## 17. Deployment and validation

From the repo under WSL:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
bash Model_Bench/validate_l2_pipeline_local.sh
python3 -m unittest -v Model_Bench/test_l2_pipeline_runtime.py
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

Jev is active, not shadowed. The dev deployment loads the explicitly approved TypeSafe credential from `deploy/dev/typesafe.env` when `TYPESAFE_API_KEY` is absent.

Run `Knowledge/98_pipeline_postflight.sql` and `Knowledge/99_postflight.sql` after SQL deployment as appropriate.

Correctness still requires validation on the real Hermes/Kanban/SQL/WSL/LM Studio host.

## 18. Historical designs that are not current

Do not restore:

- mandatory local-model review for every proposal;
- pre-created/parent-gated reviewer cards;
- a separate `l2-review` board;
- separate Jev business/audit tables;
- Jev shadow mode as the normal operating topology;
- backlog threshold 3 as claim governor;
- SQL `AttemptNo` as the rework counter;
- `kanban_forward_bridge.py`;
- independently scheduled publisher/reject/repair lifecycle authorities;
- model-based profile names used as role identity;
- agent-built Python/pyodbc/sqlcmd database transport.

Do not use historical `Plans/` or `Agent_Comms/` material to override this state-machine contract.
