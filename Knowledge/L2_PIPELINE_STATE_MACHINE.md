# Chitragupta L2 Pipeline State Machine

Status: **runtime contract**

This document defines the lifecycle implemented by `Model_Bench/l2_pipeline_runtime.py`.
If this document and the runtime disagree, fix the drift immediately.

## 1. Core invariant

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
 + per-chunk meta-attention Scores
 + typed execution depth
 + typed route-skill need
          |
          v
DETERMINISTIC EXECUTION + CONTEXT COMPILER
 whole chunks; pinned ticket/live evidence
 mode-specific context budget
          |
          +-- QWEN_FREE handoff candidate
          |       -> exact workflow binding required
          |       -> full-ticket trust gate
          |       -> fresh Jev primary review
          |       -> deterministic publish only if approved
          |
          v
l2-jev-investigator card [priority 10, only when needed]
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

## 3. Jev-first investigation contract

The runtime assembles evidence before the local investigator receives its card.

The order is:

1. requester-grounded KB/route query;
2. Jev parallel ticket characterization;
3. deterministic schema candidate generation;
4. Jev candidate selection/rating;
5. deterministic `probe_table` reads for the highest-value candidates;
6. Jev assessment of the resulting evidence package **and**, in the same System One request, a 0-3 Score for how much of each explicit context chunk the next local reasoning step needs;
7. deterministic code compiles the model-facing context by whole chunks;
8. local coordinator receives only that compiled view plus recovery hints for omitted chunks.

`probe_table` is deliberately conservative:

- the table/view must exist in `Knowledge/schema_allowlist.json`;
- a strong ticket identifier such as HeatNo, BatchNo, TransactionID, WorkOrder, ProductionOrder, MaterialDocument, RecipeNo, or Equipment must map to a real column;
- the query is built mechanically through the existing guarded query builder;
- output is bounded;
- if no identifier maps, automatic probing returns `probe_possible=false` rather than issuing a broad read.

### Meta-attention/context compiler

The investigation state is represented as explicit chunks such as current ticket, route/triage, prior ledger, prior attempts, evidence plan, deterministic candidate backlog, approved KB candidates, and each live probe. Each chunk carries source and authority metadata.

The same `JEV_INVESTIGATION` request that judges evidence sufficiency also gives each chunk a four-level Score:

```text
0  OMIT
1  SUMMARY
2  COMPACT
3  FULL
```

Deterministic policy then applies safety floors:

- current ticket context: minimum `COMPACT`;
- each gathered live-SQL probe: minimum `COMPACT`;
- a known solution explicitly selected by Jev: minimum `COMPACT`;
- routing/prior-ledger provenance remains at least a summary when present.

The context budget is applied to **whole chunks**. Optional material degrades `FULL -> COMPACT -> SUMMARY -> OMIT` according to meta-attention and budget. The assembled JSON is never globally sliced at an arbitrary character offset. Omitted chunks remain listed with source/recovery hints, so `FOCUSED_REASONING` can fetch one deliberately rather than rediscovering everything.

This compiler changes only what is shown to the local model. It does not mutate raw evidence, change evidence authority, or make historical/KB material proof of the current incident.

The same assessment also returns an advisory execution mode: `QWEN_FREE`, `COMPOSE_ONLY`, or `FOCUSED_REASONING`. Runtime policy independently resolves that recommendation.

`QWEN_FREE` is intentionally not a generic "Jev is confident" shortcut. It is accepted only for high-confidence `L3_ESCALATION` or `NEEDS_HUMAN_ACTION` outcomes, with strong evidence quality, low remaining probe/System-2 need, and (for human action) high human-action probability. Full-ticket security screening can veto it. The live workflow binding must contain an exact terminal handoff status, and the resulting deterministic proposal must still pass the normal Jev primary review before publication. Any failure falls back to the local-model path without mutating Helpdesk state.

`COMPOSE_ONLY` uses a smaller model-facing context budget and normally zero additional live reads. `FOCUSED_REASONING` gets the larger bounded context/recovery budget. The route-specific skill is loaded only when Jev's `needs_route_skill` judgment crosses deterministic policy; base lifecycle/safety skills remain attached.

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

Jev is harness-owned. `TYPESAFE_API_KEY` must come from the Windows Python/service environment; there is no repository credential fallback.

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
- agent-built Python/pyodbc/sqlcmd database transport.
