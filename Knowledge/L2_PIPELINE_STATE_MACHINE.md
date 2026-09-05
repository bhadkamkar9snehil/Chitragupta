# Chitragupta L2 Pipeline State Machine

Status: **runtime contract**  
Branch: `main`

This document defines the ticket lifecycle implemented by `Model_Bench/l2_pipeline_runtime.py`.

## 1. Core invariant

The current LM Studio deployment has one safe inference slot (`max_in_progress: 1`). Therefore the system maximizes throughput by **finishing the active ticket before claiming another one**.

Global SQL pipeline WIP is one active Hermes run.

```text
review priority              30
rework investigation         20
new investigation            10
```

A fresh Helpdesk claim is allowed only when `Hermes_L2_Response_Trn_Tbl` contains no active run after reconciliation.

## 2. Normal lifecycle

```text
Complaint_Mst_Tbl Status=eligible
          |
          v
Hermes_L2_Claim_Ticket_Usp
          |
          v
INVESTIGATOR card [priority 10]
          |
          | kanban_complete(metadata)
          v
REVIEWER card [priority 30, --parent investigator]
       /     \
 approve     reject
    |           |
    v           v
PUBLISH      REWORK card [priority 20]
    |           |
    |           v
    |       NEW REVIEWER [priority 30, --parent rework]
    |           |
    +-----------+
          |
          v
SQL / Helpdesk terminal state
```

The reviewer never publishes and never reassigns work. The investigator never publishes or creates its own reviewer.

## 3. Review-cycle semantics

`review_cycle` is a Kanban pipeline concept, separate from SQL `AttemptNo`.

```text
cycle 0 = initial investigation review
cycle 1 = first rework review
cycle 2 = second rework review
```

`MAX_REVIEW_CYCLES = 3` means a rejection at cycle 2 is escalated instead of creating cycle 3.

SQL `AttemptNo` is reserved for a genuinely new SQL claim/run. It is not used to count reviewer rework loops.

## 4. Rejection topology

A reject is terminal for that reviewer card. `l2_pipeline_runtime.py` then:

1. persists the rejected investigator's findings to the run ledger;
2. creates a fresh `REWORK[n]` investigator card;
3. creates a fresh reviewer card with `--parent <rework-task-id>`;
4. archives the rejected reviewer card so it no longer falsely represents current live ownership;
5. escalates instead of reworking when the review-cycle cap is reached.

Every investigator/rework card that can produce a publishable proposal must have exactly one reviewer child.

## 5. Approval and publication

A reviewer approval is represented structurally by the reviewer task reaching `done`.

The deterministic publisher:

1. resolves the original investigator/rework card ID from the reviewer body;
2. reads the investigator's completion metadata;
3. never asks the reviewer to retype the response;
4. applies the verified Helpdesk workflow binding;
5. calls `Hermes_Orchestrator.py --publish-response --force-run-id`;
6. verifies SQL/Helpdesk postconditions after publication;
7. logs the human-readable activity record.

A resolved ticket is **not** automatically turned into a solution article. KB curation is governed separately by `KB_IMPLEMENTATION_PLAN.md`.

## 6. Helpdesk workflow binding

The model does not decide workflow status names.

Canonical deployment file:

```text
deploy/helpdesk_workflow_binding.json
```

Populate it only after running:

```text
Hermes_Orchestrator.py --discover-workflow
```

`RESOLUTION` fails closed when `strict_resolution_status_binding=true` and `resolved_ticket_status` is not configured. This prevents the contradictory state:

```text
Hermes run = COMPLETED / RESOLUTION
Helpdesk ticket = still visibly unresolved
```

Use `Model_Bench/configure_helpdesk_workflow.py` to inspect the live workflow and write the exact observed values.

## 7. Reconciliation ordering

One reconciler owns lifecycle sequencing. It runs synchronously in this exact order:

```text
1. normalize substantive investigator completions missing metadata
2. repair missing reviewer children
3. process reviewer rejects
4. process reviewer approvals / publish
5. recover true SQL/Kanban orphans
```

The old design spawned repair/reject/publisher concurrently. That allowed publisher to inspect metadata before repair completed. That race is removed.

## 8. Event delivery and backstop

The `xstudio-l2-orchestrator` plugin triggers `reconcile_l2_pipeline.py` immediately after successful:

```text
kanban_complete
kanban_block
```

Correctness does **not** depend on the hook firing. The existing 2-minute `ticket_scout.py` cron executes reconciliation before every claim attempt, so the scout itself is the durable backstop.

`run_coalesced.py` still prevents overlapping event-triggered reconciler runs.

## 9. Stale/orphan recovery

A run is not stale just because it is old.

The pipeline treats all Kanban stages as ownership, including:

```text
todo
ready
blocked
triage
running
review
scheduled
done reviewer awaiting deterministic publish
```

`todo` is important because parent-gated reviewer cards intentionally remain there until their parent completes.

A SQL run is auto-failed for retry only when:

1. it is still active in SQL;
2. **no Kanban task at any stage references that exact run_id**; and
3. it exceeds the orphan grace period.

This removes the retired `l2-review` board dependency and prevents wall-clock recovery from killing valid queued/review work.

## 10. Ticket claiming

The scout first reconciles, then checks active SQL runs. If any remain:

```text
status = WIP_LIMIT
```

and no new ticket is claimed.

Only when WIP is zero does it call `--poll` and create the investigator + reviewer pair.

If investigator-card creation fails after SQL claim, the new run is failed immediately for clean retry instead of being abandoned for an hour.

If initial reviewer creation fails, the active investigation remains valid; the reconciler repairs the missing reviewer child after investigator completion.

## 11. Candidate filtering

`Knowledge/25_ticket_dispatch_hardening.sql` moves the non-L2 customization exclusion into `Hermes_L2_Get_Candidate_Tickets_Usp` **before `TOP (@BatchSize)`**.

This fixes the failure where the first 20 candidates were customization requests, Python removed all 20, and the scout incorrectly reported `NO_CLAIMABLE_TICKET` while valid incident tickets existed deeper in the queue.

The hardening SQL is a required post-install overlay until it is folded into the generated full-install bundle.

## 12. Pipeline status / diagnosis

Run:

```bash
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

It reports:

- active SQL runs;
- all Kanban cards grouped by `run_id`;
- topology anomalies;
- current workflow binding;
- priority/WIP/review-cycle contract.

Useful anomalies include:

```text
ACTIVE_SQL_WITH_NO_KANBAN
ACTIVE_RUN_WITHOUT_INVESTIGATOR_CARD
DONE_INVESTIGATION_WITHOUT_REVIEWER
```

## 13. Deployment

From the repo under WSL:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

Then configure the real workflow binding and apply:

```text
Knowledge/25_ticket_dispatch_hardening.sql
```

Finally run the local regression tests and live status command before allowing normal ticket flow.

Do not use GitHub Actions as a substitute for this deployment validation; the pipeline depends on the real Hermes/Kanban/SQL/LM Studio environment.
