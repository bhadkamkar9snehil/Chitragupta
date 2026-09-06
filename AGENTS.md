# Chitragupta Agent Operating Contract

This is the stable active contract for agents working on Chitragupta.

For adaptive branch design, read `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md`.  
For exact lifecycle behavior, read `Knowledge/L2_PIPELINE_STATE_MACHINE.md`.  
For human-facing current architecture, read `README.md`.

`Plans/`, `Agent_Comms/`, old commits and dated incident notes are historical evidence only.

## 1. Product

Chitragupta is the autonomous L2 support pipeline for the existing XStudio Helpdesk.

Authoritative ticket store:

```text
SQL Server: 10.2.6.204
Database:   XStudio_Helpdesk
Ticket:     dbo.Complaint_Mst_Tbl
```

Production evidence primarily lives in `XStudio_Xbatch`.

The product goal is an autonomous, AI-driven, deterministic L2 Helpdesk that improves from experience and progressively earns safe XBatch corrective authority.

## 2. Lifecycle authority

`Model_Bench/l2_pipeline_runtime.py` is the single lifecycle authority.

Current scheduling contract:

```text
new investigation   priority 10
rework              priority 20
review              priority 30
global SQL WIP      1
MAX_REVIEW_CYCLES   3
```

Lifecycle:

```text
eligible Helpdesk ticket
    -> claim
    -> investigator
    -> normalize reviewable completion
    -> fresh reviewer with frozen proposal_json
       -> approve -> deterministic publish
       -> reject  -> bounded rework -> fresh reviewer
```

Rules:

- Reviewer creation is deferred until investigator/rework completion is structurally reviewable.
- The proposal reviewed is the proposal published.
- Investigator never publishes directly.
- Reviewer never publishes and never retypes the proposed response for publication.
- `review_cycle` counts reviewer/rework loops; SQL `AttemptNo` does not.
- All tasks use the normal Kanban board.
- The old `l2-review` board, `kanban_forward_bridge.py`, `dispatch_l2_review.py` and nudge/poll publication choreography are retired.

## 3. Reconciliation and liveness

The central reconciler owns mutation sequencing.

Current order:

```text
normalize completions
-> repair unreviewable terminal completions
-> create missing reviewers
-> process reviewer rejections
-> process reviewer approvals/publication
-> recover true SQL/Kanban orphans
```

`ticket_scout.py` runs reconciliation before claim and is the durable lifecycle backstop.

Do not create independent mutating cron jobs for compatibility wrappers such as `enforce_publish_safety_net.py` or `repair_incomplete_completions.py`.

Age alone does not make a run stale. A run is recoverable as an orphan only when it is active in SQL, no Kanban task references that exact run, and the orphan grace period has elapsed.

## 4. Helpdesk workflow binding

Models do not invent Helpdesk statuses.

Canonical binding:

```text
deploy/helpdesk_workflow_binding.json
```

Current observed values include:

```text
eligible_ticket_status    Enter
resolved_ticket_status    Closed
waiting_user_ask_status   Ask
```

Unbound L3/human-action statuses remain unbound until observed.

A `RESOLUTION` must fail closed if the resolved status binding is unavailable. Never allow Hermes to say resolved while the Helpdesk ticket remains visibly unresolved.

## 5. Publication success

Only the deterministic publisher may publish an approved frozen proposal.

For a resolution, persisted SQL/Helpdesk postconditions—not Kanban narration—define success.

A resolved ticket does not automatically become a reusable KB article.

## 6. Evidence surface

Live evidence wins over retrieved knowledge, historical cases or memory.

Workers use the typed `xstudio_l2` tool for:

```text
select
query
suggest_tables
find_objects
get_definition
validate_identifiers
read_procedure
get_ticket_context
get_run_actions
save_ledger
```

The model does not build database transport. Windows/WSL paths, Python interpreter selection, drivers, credentials, `sqlcmd`, package installation and raw transport are harness concerns.

Raw model-visible SQL remains read-only. Arbitrary writes/DDL/EXEC are not worker capabilities.

Never fabricate a table, view, column, stored procedure, status or identifier.

## 7. Incident identity is harness-owned

`xstudio-l2-identity` binds identity-sensitive tool calls to the actual assigned Kanban task.

The model may choose what evidence to inspect. It may not choose a different `run_id`/`ticket_id` for:

- incident evidence;
- run ledger writes;
- action plan provenance;
- plan validation/access.

Conflicting model-supplied identity is blocked.

## 8. Knowledge, memory and experience

Do not collapse authority classes.

```text
live SQL / Helpdesk        current-ticket truth
run ledger / trace         current-ticket execution evidence
Git Knowledge/             canonical reference
solutions/approved/        explicitly governed reusable SQL-Solution mirror
facts/                     promoted operational heuristics
cases/*                    outcome-labelled historical analogies/counterexamples
sessions/*                 redacted unverified episodic history
candidates/*               unverified lessons
mem0                       compact durable operational behavior
zvec index                 disposable retrieval substrate
```

Session recording is ON.

Generic automatic zvec prefetch is OFF. Similarity is not trust.

Use explicit `l2_recall` scopes. Historical cases and sessions still require current-ticket live verification.

## 9. Governed SQL Solutions

`Hermes_Solution_Article_Mst_Tbl.IsActive` is not trust approval.

`sync_l2_approved_solutions.py` exports a Solution into trusted retrieval only when `deploy/solution_export_policy.json` explicitly approves:

```text
solution_id
semantic content_sha256
approved_by
approved_at
review_evidence
```

`solutions/approved/` is generated output owned only by that exporter. Human-authored knowledge belongs in Git or promoted facts.

When Solution synchronization runs, missing or semantically drifted approved entries are removed from trusted scope and reported for re-review.

## 10. Learning sidecar

`l2_learning_cycle.py` is the one learning sidecar boundary.

It may:

```text
materialize reviewer/publisher outcomes
mine unverified lesson candidates
mine repeated reviewed human-action candidates
```

It may not:

```text
change ticket lifecycle
publish responses
promote knowledge by itself
change action registry policy
perform XBatch mutation
```

Learning failures must not become lifecycle failures.

## 11. Corrective-action capability boundary

Current model-facing `l2_actions` operations:

```text
list
describe
plan
plans
validate_plan
```

There is no execute operation.

Repeated reviewed `NEEDS_HUMAN_ACTION` outcomes can create unverified action candidates. The miner owns observed evidence only and must not invent risk, parameters, execution target, preconditions, idempotency, verification, rollback or approval policy.

The operator/control-plane curator has only the states that currently matter:

```text
needs_executor_design
-> shadow_ready
-> registry_entry
```

A candidate may also be rejected.

The candidate carries at most one reviewed `draft_contract`; do not create parallel design representations.

Before `shadow_ready`, inspect and verify the real supported XBatch SP/API/service operation and complete contract.

Promotion adds only `mode=shadow` and never raises registry `global_mode`.

## 12. Future XBatch execution

Current arbitrary SQL mutation remains unavailable to workers. That is the current authority boundary, not the forever product destination.

Do not add a generic "allow SQL writes" switch.

A future supervised/autonomous executor must be capability-specific, deterministic, identity-bound, approval-aware, idempotent and postcondition-verified.

Do not build speculative execution state machines before a real shadow capability and measured shadow evidence require them.

## 13. Current profiles

Active/compatibility profiles:

```text
l2-investigator
l2-investigator-primary
l2-reviewer-primary
l2-reviewer-fallback
```

Expected adaptive plugins:

```text
xstudio-l2-tools
xstudio-l2-identity
xstudio-l2-learning
xstudio-l2-actions
```

Direct toolsets:

```text
xstudio_l2
l2_learning
l2_actions
```

`tool_search` remains off for these narrow specialist profiles.

## 14. Repository authority order

When sources disagree:

1. live SQL/Hermes state for runtime facts;
2. `Model_Bench/l2_pipeline_runtime.py` for lifecycle behavior;
3. `Knowledge/L2_PIPELINE_STATE_MACHINE.md`;
4. `deploy/helpdesk_workflow_binding.json`;
5. `deploy/xstudio_action_capabilities.json`;
6. `deploy/solution_export_policy.json`;
7. deployable worker skills;
8. `Knowledge/AUTONOMOUS_L2_LEARNING_ARCHITECTURE.md`;
9. `Knowledge/manifest.json` / `Knowledge/task-router.md`;
10. `README.md`;
11. historical `Plans/` / `Agent_Comms/`.

The runtime learning vault is experience/derived retrieval material, not canonical project policy.

## 15. SQL deployment

Edit numbered SQL sources, not the generated full-install bundle directly.

The full install is generated from:

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

`98_pipeline_postflight.sql` and `99_postflight.sql` are validation, not bundle inputs.

Keep `Knowledge/00_Hermes_L2_FULL_INSTALL.sql` aligned with the numbered sources.

## 16. Deployment and validation

`deploy/` is the reproducible mirror of live Hermes profile artifacts.

`Model_Bench/deploy_l2_pipeline_runtime.sh` installs lifecycle/adaptive runtime components. Learning-vault refresh is best-effort and must not leave deterministic runtime deployment half-finished.

Validation is local:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Do not use GitHub Actions as validation authority.

The aggregate validator must include every active contract test. When adding/removing an adaptive component, update the validator in the same change.

## 17. Security and repository hygiene

Do not commit or print credentials.

Do not litter the project root with one-off scripts or SQL files. Reusable utilities belong intentionally under `Model_Bench/` and need tests.

Do not reintroduce model-driven database transport or package installation as a fallback.

## 18. Change discipline

Ponytail the system:

```text
understand first
trace callers
reuse an existing authority
delete obsolete paths
make the shortest correct change
```

Prefer one mechanism and one owner.

Any lifecycle change must preserve or deliberately revise:

- explicit WIP ownership;
- one lifecycle mutation authority;
- exactly one reviewer per publishable completion;
- immutable reviewer proposal;
- deterministic/idempotent publication;
- bounded review cycles;
- reconciliation after event loss;
- persisted SQL/Helpdesk postconditions;
- live evidence over retrieval;
- harness-owned incident identity.

Do not add future-only architecture without a current caller, current failure, real ticket evidence or measured need.
