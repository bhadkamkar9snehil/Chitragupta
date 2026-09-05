# Chitragupta L2 Pipeline State Machine

Status: **runtime contract**  
Branch: `main`

This document defines the lifecycle implemented by `Model_Bench/l2_pipeline_runtime.py`.
If this document and the runtime disagree, fix the drift immediately; neither should be allowed to remain stale.

## 1. Core invariant

The current LM Studio deployment has one safe inference slot (`max_in_progress: 1`). Throughput therefore comes from **finishing the active ticket before claiming another one**.

Global SQL pipeline WIP is one active Hermes run.

```text
review priority              30
rework investigation         20
new investigation            10
```

A fresh Helpdesk claim is allowed only when `Hermes_L2_Response_Trn_Tbl` has no active run after reconciliation.

## 2. Normal lifecycle

Reviewer creation is deliberately **deferred** until the source investigator/rework completion has been normalized and is reviewable.

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
normalize / validate proposal
          |
          | only when complete/reviewable
          v
REVIEWER card [priority 30]
  frozen proposal_json
       /     \
 approve     reject
    |           |
    v           v
PUBLISH      REWORK card [priority 20]
    |           |
    |           | kanban_complete(metadata)
    |           v
    |       normalize / validate
    |           |
    |           v
    |       NEW REVIEWER [priority 30]
    |           |
    +-----------+
          |
          v
SQL / Helpdesk terminal or waiting state
```

The investigator never publishes or creates its own reviewer. The reviewer never publishes, reassigns the ticket, or retypes the response for publication.

## 3. Frozen proposal contract

The reviewer judges a frozen `proposal_json` created from normalized investigator/rework completion metadata.

The publication payload must come from that frozen reviewed proposal rather than from a later reconstruction of task prose.

At minimum the proposal carries the fields needed for deterministic publication, including:

```text
run_id
ticket_id
response_type
reply_text
```

and, when present:

```text
problem_summary
findings
root_cause
resolution
```

A reviewer card must not exist for an incomplete/unreviewable proposal in the normal post-migration topology.

## 4. Review-cycle semantics

`review_cycle` is the pipeline counter for reviewer/rework loops and is separate from SQL `AttemptNo`.

```text
cycle 0 = initial investigation review
cycle 1 = first rework review
cycle 2 = second rework review
```

`MAX_REVIEW_CYCLES = 3` means a rejection at cycle 2 escalates instead of creating cycle 3.

SQL `AttemptNo` is reserved for genuinely new SQL claim/run attempts. It is not a reviewer-rework counter.

## 5. Rejection topology

A reject is terminal for that reviewer card.

The reconciler then:

1. records/preserves the reviewer objection;
2. persists useful prior investigation state to the run ledger;
3. creates a fresh `REWORK[n]` investigator card at priority 20;
4. waits for that rework to complete and be normalized;
5. creates a fresh reviewer for the normalized rework proposal at priority 30;
6. escalates rather than creating another rework when the review-cycle cap is reached.

The important invariant is:

> Every reviewable investigator/rework proposal must have exactly one reviewer, and reviewer creation happens after proposal normalization.

## 6. Approval and publication

A reviewer approval is represented structurally by the reviewer reaching `done`.

The deterministic publication path:

1. reads the reviewer's frozen `proposal_json`;
2. applies the verified Helpdesk workflow binding;
3. calls `Hermes_Orchestrator.py --publish-response --force-run-id`;
4. verifies SQL/Helpdesk postconditions;
5. records the human-readable activity entry.

The investigator does not publish. The reviewer does not publish.

A resolved ticket is **not** automatically converted into a solution article. KB promotion/deduplication is governed by `Knowledge/KB_IMPLEMENTATION_PLAN.md`.

## 7. Helpdesk workflow binding

Workflow status names are harness configuration, not model output.

Canonical deployment file:

```text
deploy/helpdesk_workflow_binding.json
```

Current live-verified values are:

```text
eligible_ticket_status            Enter
resolved_ticket_status            Closed
waiting_user_ask_status           Ask
l3_ticket_status                  null
needs_human_action_ticket_status  null
```

`Closed` and `Ask` were derived from live Helpdesk evidence. Unproven L3/human-action ticket statuses remain unbound rather than invented.

When `strict_resolution_status_binding=true`, `RESOLUTION` must fail closed if `resolved_ticket_status` is not configured. This prevents:

```text
Hermes run = COMPLETED / RESOLUTION
Helpdesk ticket = still visibly unresolved
```

Use `Model_Bench/configure_helpdesk_workflow.py` / live discovery before changing these values.

## 8. Reconciliation ordering

One reconciler owns lifecycle mutation. Current synchronous ordering is:

```text
1. normalize investigator/rework completions
2. convert unreviewable terminal completions into bounded rework
3. create missing reviewers for normalized reviewable completions
4. process reviewer rejections
5. process reviewer approvals / deterministic publish
6. recover true SQL/Kanban orphans
```

The old design spawned repair/reject/publisher concurrently. That race is retired and must not be reintroduced.

## 9. Event delivery and backstop

`Model_Bench/xstudio_l2_orchestrator_plugin/` triggers `reconcile_l2_pipeline.py` after successful:

```text
kanban_complete
kanban_block
```

Event delivery is the fast path, not a correctness dependency.

The 2-minute `ticket_scout.py` job runs reconciliation before every claim attempt and is the durable mutating backstop.

`run_coalesced.py` prevents overlapping event-triggered reconciler executions.

The old independently scheduled mutating jobs for publish safety-net / completion repair were deliberately removed. They are compatibility entrypoints only and must not be scheduled as separate lifecycle authorities.

The remaining completion audit is read-only.

## 10. Stale/orphan recovery

A run is not stale merely because it is old.

Any Kanban card that references the run protects it, regardless of whether it is `todo`, `ready`, `running`, `blocked`, scheduled, review-related, or a done reviewer awaiting deterministic publication.

A SQL run is auto-failed for clean retry only when:

1. it is still active in SQL;
2. no Kanban task at any stage references that exact `run_id`; and
3. it exceeds the orphan grace period.

The retired `l2-review` board is not queried by the production liveness path.

## 11. Ticket claiming

The scout first reconciles and then checks active SQL runs.

If any active run remains:

```text
status = WIP_LIMIT
```

and no ticket is claimed.

Only when WIP is zero does the scout invoke the atomic poll/claim path and create **one investigator card**.

The reviewer is **not** created during claim. It is created later by reconciliation after the investigator completion has been normalized and validated as reviewable.

If investigator-card creation fails after SQL claim, the run is failed promptly for clean retry rather than being abandoned.

Do not bypass this production gate with a manual raw `Hermes_Orchestrator.py --poll` test.

## 12. Candidate filtering

`Knowledge/25_ticket_dispatch_hardening.sql` puts the non-L2 customization exclusion inside `Hermes_L2_Get_Candidate_Tickets_Usp` **before `TOP (@BatchSize)`**.

This prevents the old failure where the first N candidates were removed client-side and the scout falsely reported `NO_CLAIMABLE_TICKET` while valid incidents existed deeper in the queue.

The `25` hardening source is now included in the regenerated `Knowledge/00_Hermes_L2_FULL_INSTALL.sql` bundle; it is no longer an omitted post-install-only change.

## 13. UPDATE continuation hardening

`Knowledge/55_update_retry_hardening.sql` is also part of the regenerated full-install bundle.

A published `UPDATE` must have bounded continuation behavior (`NextEligibleOn`) rather than becoming permanently unclaimable or immediately churning.

## 14. Pipeline status / diagnosis

Use the deployed runtime status command:

```bash
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

It should expose:

- active SQL runs;
- Kanban cards grouped/correlated by `run_id`;
- topology anomalies;
- workflow binding;
- priority/WIP/review-cycle contract.

A healthy active run should be explainable as one of the current pipeline stages rather than as an unexplained SQL row.

## 15. Cron contract

Current L2 scheduling is intentionally simple:

```text
L2 Ticket Scout                every 2m   mutating central reconcile + optional claim
L2 Kanban Completion Audit     every 10m  read-only divergence audit
```

Session maintenance and mem0 patch maintenance are unrelated infrastructure jobs.

Do not recreate independent publisher/reject/repair cron loops.

## 16. Deployment

From the repo under WSL:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
bash Model_Bench/validate_l2_pipeline_local.sh
python3 -m unittest -v Model_Bench/test_l2_pipeline_runtime.py
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

The generated SQL install bundle already includes the `25` and `55` hardening files. Run `Knowledge/98_pipeline_postflight.sql` and `Knowledge/99_postflight.sql` after deployment as appropriate.

Do not use GitHub Actions as a substitute for live pipeline validation; correctness depends on the real Hermes/Kanban/SQL/WSL/LM Studio environment.

## 17. Historical designs that are not current

The following are historical only:

- backlog threshold 3 as the claim governor;
- creating investigator and reviewer as a pair during claim;
- SQL `AttemptNo` as the rework counter;
- separate `l2-review` board;
- `kanban_forward_bridge.py`;
- separately scheduled publisher/reject/repair lifecycle authorities;
- model-based profile names used as role identity.

Do not use historical `Plans/` or `Agent_Comms/` material to override this state-machine contract.