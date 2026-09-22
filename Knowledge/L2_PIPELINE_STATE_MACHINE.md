# Chitragupta L2 — Definitive Architecture and Pipeline State Machine

Status: **sole normative architecture and lifecycle contract**

This is the sole normative architecture and lifecycle specification for Chitragupta L2.
If another document, historical plan, comment, deployment snapshot or implementation note disagrees with this document and the current runtime, it is stale and must not be treated as architecture.

Authority hierarchy:
1. `AGENTS.md` — stable engineering/runtime invariants and Scope Guard
2. `Knowledge/L2_PIPELINE_STATE_MACHINE.md` — sole normative architecture + lifecycle
3. runtime code (`Model_Bench/l2_pipeline_runtime.py`) / SQL implementation
`README.md` is only a human-facing overview.

## Architecture — Five Responsibilities

Chitragupta is organized around exactly five architectural responsibilities:

```text
                         ┌──────────────────────┐
                         │ 1. XSTUDIO HELPDESK  │
                         │                      │
                         │ Complaint_Mst_Tbl    │
                         │ user-visible state   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                     ┌───────────────────────────┐
                     │ 2. CHITRAGUPTA CONTROL    │
                     │                           │
                     │ deterministic lifecycle   │
                     │ claim / WIP / queue       │
                     │ retry / recovery          │
                     │ review routing            │
                     │ workflow / publication    │
                     └────────────┬──────────────┘
                                  │
                                  ▼
                     ┌───────────────────────────┐
                     │ 3. JEV — SYSTEM ONE       │
                     │                           │
                     │ triage                    │
                     │ evidence planning         │
                     │ semantic judgments        │
                     │ execution-depth choice    │
                     │ primary semantic review   │
                     └────────────┬──────────────┘
                                  │
                         when Qwen is required
                                  │
                                  ▼
                     ┌───────────────────────────┐
                     │ 4. HERMES / QWEN          │
                     │    SYSTEM TWO             │
                     │                           │
                     │ compose                   │
                     │ focused investigation     │
                     │ bounded rework            │
                     │ exceptional deep review   │
                     └────────────┬──────────────┘
                                  │
                                  ▼
                     ┌───────────────────────────┐
                     │ 5. EVIDENCE / KNOWLEDGE   │
                     │                           │
                     │ xstudio_l2 typed reads    │
                     │ live SQL                  │
                     │ governed KB               │
                     │ ticket/run ledger         │
                     │ canonical Knowledge docs  │
                     └───────────────────────────┘
```

The surrounding implementation mechanisms are not additional architecture:
- **SQL locks / leases / runtime tables** = persistence and coordination
- **Kanban** = execution transport for Hermes workers
- **Trace pipeline** = observability
- **Cron / event hook** = lifecycle triggering and liveness
- **Tests / postflight** = verification
- **Deployment scripts** = deployment
- **Qdrant** = retrieval index, never authority
- **mem0** = bounded operational heuristics, never ticket truth

No sixth architectural box exists.

## 1. Core invariant

The current LM Studio deployment has one safe local inference slot. Chitragupta therefore separates **pipeline concurrency** from **local-model concurrency**.

Default runtime capacities:

```text
active Hermes runs       8   (L2_MAX_PIPELINE_WIP)
RUNNING local-Qwen work  1   (hard SQL-serialized invariant)
QUEUED local-Qwen work   4*  (priority-aware L2_MAX_QWEN_WAITING threshold)
```

*Note on priority-aware queue backpressure: `L2_MAX_QWEN_WAITING` (default 4) limits new investigations (priority 10) when total queued $\ge$ 4. Higher-priority rework (priority 20) and reviews (priority 30) are admitted unless equal/higher-priority work fills the threshold. Total queued runs in SQL may therefore legitimately exceed 4 so active runs are not starved by pending new investigations.

Jev, deterministic candidate generation, bounded probes, context compilation, and QWEN_FREE review/publication may progress for several tickets while the one local Qwen slot is busy. Any COMPOSE_ONLY, FOCUSED_REASONING, rework, or local-review fallback task must acquire that same shared slot.

```text
local deep-review priority     30
rework investigation           20
new investigation              10
```

A fresh Helpdesk claim is allowed while active-run count is below the configured pipeline cap and total queued local-model work is below `L2_MAX_QWEN_WAITING` (default 4). `Hermes_L2_Claim_Ticket_Usp` enforces capacity atomically under `sp_getapplock('HermesL2:PipelineCapacity')`, so overlapping scouts cannot over-claim.

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
PERSIST FROZEN LOCAL-MODEL WORK PACKAGE
  LocalModelState=QUEUED
  priority: review 30 > rework 20 > investigation 10
          |
          v
SQL LOCAL-MODEL ADMISSION
  exactly one RUNNING task across all profiles
          |
          v
l2-jev-investigator / rework / local-review task
  COMPOSE_ONLY or FOCUSED_REASONING
          |
          | kanban_complete / kanban_block
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

## 5a. Shared local-model admission

All local-model purposes use one run-owned queue on `Hermes_L2_Response_Trn_Tbl`:

```text
ExecutionMode
LocalModelState        QUEUED | RUNNING | DONE
LocalModelPurpose      INVESTIGATION | REWORK | REVIEW
LocalModelPriority
LocalModelWorkKey
PendingLocalModelJson
LocalModelTaskID
LocalModelQueuedOn
LocalModelStartedOn
LocalModelCompletedOn
```

The exact Kanban task specification is persisted in `PendingLocalModelJson` before any task is created. `Hermes_L2_Queue_Local_Model_Usp` enforces priority-aware queue admission under `sp_getapplock` using `@MaxWaiting`:
- `@Priority <= 10` (new investigations): rejected with `QueueStatus = 'BACKPRESSURE'` if total currently queued runs $\ge$ `@MaxWaiting`.
- `@Priority > 10` (rework 20, reviews 30): rejected only if currently queued work with `LocalModelPriority >= @Priority` $\ge$ `@MaxWaiting`.
This guarantees ongoing rework and reviews cannot be starved by pending investigations, and means total queued runs in SQL may legitimately exceed `@MaxWaiting`.

`Hermes_L2_Try_Acquire_Local_Model_Usp` uses `sp_getapplock('HermesL2:LocalModelSlot')` plus the run table to guarantee at most one active local-model lease.

Admission order is:

```text
review 30 > rework 20 > new investigation 10
then LocalModelQueuedOn ASC
```

A QUEUED run with no Kanban card is intentional, not an orphan. The card is created only after SQL admission. Terminal cards release the slot during reconciliation; a stale RUNNING lease is requeued only when no live local-model Kanban task still owns that run.

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

### Knowledge authority hierarchy

| Source | Role | Authority |
|---|---|---|
| Live SQL for this ticket | Current incident authority | Factual proof |
| Git-tracked `Knowledge/` | Canonical domain/runtime reference | Authoritative reference |
| Approved SQL Solution article | Reusable known-issue guidance | Governing hypothesis (requires live verification) |
| Problem/ticket history | Episodic and recurring-root-cause evidence | Historical lead |
| mem0 | Compact durable operational heuristics | Operational hints only |
| Qdrant | Fast semantic retrieval index | Index only (never authority) |

A KB hit, previous ticket, snapshot, or memory item is a lead. A current-ticket factual claim must be verified against live evidence whenever live verification is possible.

## 12. Response semantics and mutation boundary

### Response types

| Type | Meaning | Workflow Behavior |
|---|---|---|
| `UPDATE` | Verified progress exists, but incident is not finally resolved | Posts activity note; ticket remains `Enter`; bounded continuation window via `NextEligibleOn` (+15m) |
| `QUESTION` | Specific requester fact is genuinely required | Applies configured `waiting_user_ask_status` (`Ask`) |
| `RESOLUTION` | Outcome/fix is verified and complete | Moves ticket to `resolved_ticket_status` (`Closed`); fails closed if unbound |
| `L3_ESCALATION` | Root cause unresolved or genuinely beyond L2 capability | Enters `Hermes_L3_Escalation_Trn_Tbl`; remains `Enter` (unbound L3 status) |
| `NEEDS_HUMAN_ACTION` | Cause/fix known but action is unauthorized for L2 worker | Documents necessary operational action; routed to human action workflow |

### Mutation boundary

The worker-facing `xstudio_l2` surface is read-only. Production or configuration writes are not an implicit next step after diagnosis.
- `known cause + unauthorized corrective action -> NEEDS_HUMAN_ACTION`
- `unknown/unresolved cause -> L3_ESCALATION`

Ticket publication is an audited deterministic runtime action performed only after Jev primary review approval or approved local-review fallback through `Hermes_Orchestrator.py --publish-response`.

## 13. Helpdesk workflow binding

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

## 14. Reconciliation ordering

One reconciler owns lifecycle mutation.

Current synchronous order:

```text
1. release terminal local-model leases
2. requeue stale local-model leases only when no live local card owns the run
3. normalize investigator/rework completions
4. convert unreviewable completions into queued bounded rework
5. run Jev primary reviews
     - direct approve/publish where safety gates pass
     - queue focused rework where accepted
     - direct L3 escalation where accepted
     - queue local reviewer only for fallback
6. process local-review rejections
7. process local-review approvals through the same publisher
8. recover true SQL/Kanban orphans
9. admit at most one next local-Qwen task
```

Do not restore separate publisher/reject/reviewer schedulers.

## 15. Event delivery and backstop

`xstudio-l2-orchestrator` triggers reconciliation after successful Kanban completion/block events.

Event delivery is the fast path.

The 2-minute `ticket_scout.py` run remains the durable reconcile-first backstop. It can fill multiple Jev/deterministic pipeline slots in one pass, stops at the SQL pipeline cap or priority-aware Qwen backlog, and never creates a local-model card outside the shared admission controller.

## 16. Stale/orphan recovery

Age alone never makes a run stale.

A run is protected from orphan recovery if:

1. it is referenced by an active Kanban card (`KANBAN_RUN_PROTECTING_STATES = {'todo', 'ready', 'blocked', 'triage', 'running', 'review', 'scheduled', 'done'}`);
2. it is queued in SQL waiting for local-model admission (`LocalModelState='QUEUED'`); or
3. it was requeued in the current reconciliation pass from a stale lease.

A run is auto-failed for clean retry only when it is active in SQL, has neither active Kanban representation nor QUEUED local-model state, and exceeds the orphan grace period (45 minutes).

## 17. Candidate filtering / UPDATE continuation

`Knowledge/25_ticket_dispatch_hardening.sql` performs non-L2 customization filtering before `TOP (@BatchSize)`.

`Knowledge/55_update_retry_hardening.sql` provides bounded continuation behavior for published `UPDATE` responses.

Both are part of the generated full-install bundle. Within the same operational priority, fresh never-run/user-changed tickets are ordered ahead of failed retries and old UPDATE continuations, preventing continuation loops from starving new incidents.

## 18. Deployment and validation

From the repo under WSL:

```bash
# Inner edit/test loop.
bash Model_Bench/validate_l2_pipeline_local.sh

# Full live pre-deployment validation.
bash Model_Bench/validate_l2_pipeline_local.sh --full

# Deploy without restarting, then re-run live-only validation if desired.
bash Model_Bench/deploy_l2_pipeline_runtime.sh --no-restart
bash Model_Bench/validate_l2_pipeline_local.sh --live-only

python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

Normal reconciliation is active-run scoped. It snapshots Kanban tasks and active SQL runs once, then examines only cards belonging to those active run IDs. Historical completed cards are not re-queried on every scout/validation tick; the separate audit owns historical reviewer/SQL divergence checks.

Jev is harness-owned. `TYPESAFE_API_KEY` must come from the Windows Python/service environment; there is no repository credential fallback.

Run `Knowledge/98_pipeline_postflight.sql` and `Knowledge/99_postflight.sql` after SQL deployment as appropriate.

Correctness still requires validation on the real Hermes/Kanban/SQL/WSL/LM Studio host.

## 19. Historical designs that are not current

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
