# Chitragupta — XStudio Hermes L2 Helpdesk

Chitragupta is an autonomous L2 support pipeline for the XStudio/XMES manufacturing platform, built on Hermes Agent.

It works against the existing Helpdesk rather than creating a parallel ticketing system: it claims a real `Complaint_Mst_Tbl` ticket, investigates against live XStudio data, has an independent reviewer judge the proposal, and publishes through an audited deterministic SQL path.

For agent instructions, read `AGENTS.md`. For the exact lifecycle contract, read `Knowledge/L2_PIPELINE_STATE_MACHINE.md`.

---

## 1. Current architecture

The current LM Studio deployment has one safe inference slot, so Chitragupta uses **global pipeline WIP = 1**. The system finishes the active run before claiming another ticket.

```text
                    XStudio Helpdesk
              dbo.Complaint_Mst_Tbl
                  Status = Enter
                        |
                        v
             ticket_scout.py (2m cron)
                        |
                        | synchronous reconcile() first
                        |
              +---------+---------+
              | active SQL run?   |
              +---------+---------+
                        |
                yes ----+---- no
                 |             |
                 v             v
             WIP_LIMIT    atomic --poll claim
                               |
                               v
                    INVESTIGATOR [priority 10]
                    l2-investigator-primary
                               |
                               | kanban_complete(metadata)
                               v
                    deterministic normalization
                               |
                               | only when reviewable
                               v
                       REVIEWER [priority 30]
                       l2-reviewer-primary
                       frozen proposal_json
                         /             \
                    approve           reject
                       |                |
                       v                v
                deterministic       REWORK [priority 20]
                   publish          l2-investigator-primary
                       |                |
                       |                | complete + normalize
                       |                v
                       |           NEW REVIEWER [30]
                       |                |
                       +----------------+
                               |
                               v
                    SQL / Helpdesk outcome
```

### Lifecycle rules

- New investigation priority: `10`.
- Rework priority: `20`.
- Review priority: `30`.
- Reviewer cards are created **after** investigator/rework completion is normalized and reviewable; they are not pre-created during ticket claim.
- Reviewers receive a frozen `proposal_json`; the publisher uses that reviewed proposal rather than reconstructing prose later.
- `review_cycle` counts reject/rework loops. SQL `AttemptNo` counts independent SQL claim/run attempts and is not the rework counter.
- `MAX_REVIEW_CYCLES = 3`; a rejection at cycle 2 escalates rather than creating another loop.
- Every rework gets a fresh reviewer after rework completion/normalization.
- Investigator and reviewer never publish directly; publication is deterministic.
- Single Kanban board only. The old `l2-review` board and `kanban_forward_bridge.py` are retired.

---

## 2. One deterministic lifecycle authority

`Model_Bench/l2_pipeline_runtime.py` owns the lifecycle.

The reconciler executes synchronously in this order:

```text
1. normalize investigator/rework completions
2. turn unreviewable terminal completions into bounded rework
3. create missing reviewers for reviewable completed investigations
4. process reviewer rejections
5. process reviewer approvals and publish
6. recover true SQL/Kanban orphans
```

This replaces the old pattern of launching repair, reject, and publisher scripts concurrently.

`Model_Bench/xstudio_l2_orchestrator_plugin/` triggers the same reconciler immediately after successful `kanban_complete` / `kanban_block`. The event hook is the fast path; correctness does not depend on it.

The 2-minute Ticket Scout is the durable mutating backstop because it reconciles before every claim attempt.

Current L2 scheduled jobs are documented in `deploy/cron_jobs.txt`:

- **L2 Ticket Scout** — every 2 minutes, mutating/reconciling.
- **L2 Kanban Completion Audit** — every 10 minutes, read-only reviewer/SQL divergence audit.

The old independently scheduled 5-minute publish-safety-net and repair jobs were deliberately removed because they duplicated `reconcile()` and reintroduced process-level mutation races.

---

## 3. Helpdesk workflow binding

The model does not choose ticket workflow state names.

Canonical binding:

`deploy/helpdesk_workflow_binding.json`

Current live-verified values:

```text
eligible_ticket_status            Enter
resolved_ticket_status            Closed
waiting_user_ask_status           Ask
l3_ticket_status                  null
needs_human_action_ticket_status  null
```

`Closed` and `Ask` were bound from live Helpdesk evidence. L3/human-action ticket statuses stay unbound until a distinct live workflow state is proven.

`strict_resolution_status_binding=true` means `RESOLUTION` fails closed if the resolved state is unavailable. Chitragupta must not produce the contradictory state where the Hermes run says resolved while the Helpdesk ticket still looks open.

---

## 4. Publication outcomes

The deterministic publisher invokes the audited `Hermes_Orchestrator.py --publish-response --force-run-id` path and verifies persisted postconditions.

For a normal resolution, the expected state includes:

```text
Hermes_L2_Response_Trn_Tbl.ProcessStatus = COMPLETED
Hermes_L2_Response_Trn_Tbl.ResponseType  = RESOLUTION
Hermes_L2_Response_Trn_Tbl.IsResolved    = 1
Hermes_L2_Response_Trn_Tbl.IsActive      = 0
Complaint_Mst_Tbl.Status                 = Closed
```

For `QUESTION`, the run becomes waiting-user according to the existing Helpdesk workflow.

For `UPDATE`, `NextEligibleOn` provides a bounded continuation window so an update does not become permanently unclaimable.

A `RESOLUTION` no longer automatically creates a new solution article. KB promotion is governed separately by `Knowledge/KB_IMPLEMENTATION_PLAN.md`.

---

## 5. Reject / rework semantics

A reviewer rejection is terminal for that review card.

The central runtime:

1. preserves the reviewer objection;
2. persists/reuses relevant prior investigation ledger information;
3. creates `REWORK[n]` at priority 20;
4. waits for the rework to complete and be normalized;
5. creates a fresh reviewer at priority 30;
6. escalates when the bounded review-cycle limit is reached.

This is intentionally separate from SQL `AttemptNo`.

---

## 6. Stale/orphan recovery

A run is not stale merely because it is old.

Any Kanban task referencing a run protects it, including `todo`, `ready`, `running`, `blocked`, scheduled/review work, and a done reviewer waiting for deterministic publication.

A SQL run is recovered as an orphan only when:

1. it is still active in SQL;
2. no Kanban task at any stage references that `run_id`; and
3. the orphan grace period has elapsed.

The retired two-board liveness check is not part of the current design.

---

## 7. Ticket candidate selection

`Knowledge/25_ticket_dispatch_hardening.sql` excludes unsupported customization work inside `Hermes_L2_Get_Candidate_Tickets_Usp` **before** `TOP (@BatchSize)`.

This prevents an earlier failure mode where SQL returned the top N rows, Python discarded all unsupported rows, and the scout incorrectly concluded there was no claimable ticket while valid work existed deeper in the queue.

Global WIP=1 supersedes the temporary older `MAX_INVESTIGATOR_BACKLOG=3` design.

Do not manually use raw `Hermes_Orchestrator.py --poll` for production lifecycle testing because it bypasses the scout's WIP gate.

---

## 8. Investigation and evidence

Investigator profile:

`l2-investigator-primary`

Reviewer profile:

`l2-reviewer-primary`

Fallback reviewer profile:

`l2-reviewer-fallback`

`l2-investigator` remains the dispatcher/host profile and compatibility script location.

The current loaded LM Studio model is a deployment fact, not an architecture constant. Verify it live rather than relying on a model name in documentation.

Investigation starts from the dispatch-time bundle and uses deterministic schema narrowing/query helpers. Live SQL evidence wins over retrieved KB suggestions, prior ticket ledgers, or mem0 hints.

Preferred tools include:

- `--build-query` for schema-validated reads when the entity is known;
- `--suggest-tables` for deterministic table narrowing;
- `--find-sql-objects` / live metadata for discovery;
- `--query` for explicit read-only SQL;
- `--save-ledger` for per-ticket episodic state.

Never write the ticket directly from an investigator turn.

---

## 9. Knowledge and memory

The current deterministic solution retriever is intentionally conservative:

- route alone cannot retrieve an article;
- generic weak overlap should abstain;
- hits carry provenance;
- applicability must be verified live;
- pre-investigation retrieval does not use `SuspectedCause` as a primary search signal.

The larger KB architecture is documented in `Knowledge/KB_IMPLEMENTATION_PLAN.md`.

The conceptual boundaries are deliberate:

```text
Live SQL evidence       != KB
Schema discovery        != KB
Ticket/run history      != reusable KB
mem0                    != KB
Qdrant                  != source of truth
Resolved ticket         != automatically approved knowledge
```

mem0 uses a Qdrant server-backed provider for shared operational memory. Qdrant server mode replaced embedded/local-path mode because embedded Qdrant is single-process and Kanban workers are separate processes.

---

## 10. Repository layout

```text
Hermes_Orchestrator.py
    Mechanical/audited SQL primitives: claim, publish, read-only query,
    schema discovery, ledger, workflow helpers.

Model_Bench/l2_pipeline_runtime.py
    Single deterministic lifecycle authority.

Model_Bench/ticket_scout.py
    2-minute reconciliation + WIP gate + new claim entrypoint.

Model_Bench/reconcile_l2_pipeline.py
    Immediate deterministic reconciliation entrypoint used by hooks/backstops.

Model_Bench/kanban_approval_publisher.py
Model_Bench/kanban_reject_bridge.py
Model_Bench/repair_incomplete_completions.py
Model_Bench/enforce_publish_safety_net.py
    Compatibility entrypoints into l2_pipeline_runtime.py; not independent
    lifecycle authorities or separately scheduled mutating jobs.

Model_Bench/audit_kanban_completions.py
    Read-only reviewer/SQL divergence audit.

Model_Bench/xstudio_l2_orchestrator_plugin/
    Event hook that launches the central reconciler after Kanban terminal actions.

Model_Bench/xstudio_l2_trace_plugin/
    Tool/API/hardware trace capture.

Knowledge/L2_PIPELINE_STATE_MACHINE.md
    Normative lifecycle documentation.

Knowledge/KB_IMPLEMENTATION_PLAN.md
    KB architecture and rollout contract.

Knowledge/manifest.json
    Machine-readable KB routing/catalog source.

Knowledge/00_Hermes_L2_FULL_INSTALL.sql
    Generated SQL install bundle.

Knowledge/98_pipeline_postflight.sql
Knowledge/99_postflight.sql
    Deployment/postflight validation.

deploy/helpdesk_workflow_binding.json
    Verified Helpdesk state mapping.

deploy/cron_jobs.txt
    Mirrored current schedule.

deploy/profiles/
deploy/skills/xstudio/
    Reproducible Hermes profile/skill mirror.

Plans/
Agent_Comms/
    Historical/research material only; not live instructions.
```

---

## 11. SQL installation

Edit the numbered SQL sources, not the generated bundle directly.

`Knowledge/00_Hermes_L2_FULL_INSTALL.sql` currently concatenates these nine sources in order:

```text
00_tables_and_indexes.sql
10_helpdesk_discovery.sql
20_ticket_dispatch.sql
25_ticket_dispatch_hardening.sql
30_context_and_live_discovery.sql
40_investigation_runtime.sql
50_response_and_workflow.sql
55_update_retry_hardening.sql
60_metrics_and_reporting.sql
```

`98_pipeline_postflight.sql` and `99_postflight.sql` are validation scripts and are not part of the concatenated install input.

The full-install bundle has already been regenerated to include the `25` and `55` hardening layers.

`.gitattributes` forces LF for `*.sh` and `*.sql` because Windows CRLF conversion previously broke WSL shell execution and could make generated SQL drift.

Deploy SQL with a tool that correctly handles `GO` batch separators, then run the postflights.

---

## 12. Local deployment / validation

This pipeline depends on the actual Windows + WSL + Hermes + Kanban + SQL Server + LM Studio environment. GitHub Actions is not a substitute for live validation.

Useful local commands:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
python3 -m unittest -v Model_Bench/test_l2_pipeline_runtime.py
bash Model_Bench/deploy_l2_pipeline_runtime.sh
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py reconcile --dry-run
```

To discover/rebind Helpdesk workflow values:

```bash
python3 Model_Bench/configure_helpdesk_workflow.py
```

Do not invent unresolved/resolved/L3 workflow states.

---

## 13. Current cron policy

The mirrored schedule is `deploy/cron_jobs.txt`.

For L2 lifecycle mutation there is one scheduled authority:

```text
L2 Ticket Scout -> ticket_scout.py -> central reconcile + optional claim
```

The completion audit is read-only and may run independently.

Session maintenance and mem0 patch maintenance are unrelated infrastructure jobs and remain separate.

---

## 14. After a Hermes update

Read `patches/POST_UPDATE.md`.

Important recovery checks include:

- Qdrant server health;
- mem0 LM Studio compatibility patch;
- profile/skill/plugin redeployment if profile directories were rebuilt;
- central L2 pipeline runtime deployment;
- SQL full-install/postflight alignment;
- cron mirror versus live schedule.

After changing live profile artifacts, refresh `deploy/` with `Model_Bench/mirror_wsl_artifacts.sh` and inspect the resulting diff.

---

## 15. Historical architectures

The repository intentionally keeps earlier designs for provenance. These are not current production instructions:

- poll-into-one-long-lived-chat;
- separate `l2-review` board;
- `kanban_forward_bridge.py`;
- model-based role names such as `l2-eval-investigator` / `l2-gemma-verifier` / `l2-qwen-verifier`;
- backlog threshold 3 as the claim governor;
- SQL `AttemptNo` as the reject/rework counter;
- independently scheduled publisher/reject/repair lifecycle authorities.

If a historical document conflicts with `AGENTS.md`, `Knowledge/L2_PIPELINE_STATE_MACHINE.md`, or `Model_Bench/l2_pipeline_runtime.py`, the historical document is provenance only.

---

## 16. Experimental Conductor work

Microsoft Conductor work in `Plans/` / `Model_Bench/` is an experiment only. Kanban remains the live L2 pipeline until an explicit cutover is performed, tested, and documented. Do not silently treat the experiment as production.