# Chitragupta — XStudio / Hermes L2 Helpdesk

Chitragupta is the deterministic L2 support pipeline around the existing XStudio Helpdesk and Hermes Agent. XStudio remains the ticket system. Hermes investigates live evidence, an independent reviewer verifies the proposed response, and deterministic code owns all lifecycle transitions and ticket publication.

The design goal is simple: keep reasoning probabilistic, keep workflow mechanics deterministic.

## Current production architecture

```text
XStudio_Helpdesk.dbo.Complaint_Mst_Tbl
        |
        | ticket_scout.py every 2 minutes
        v
reconcile all existing work
        |
        +-- active SQL run exists --> WIP_LIMIT; claim nothing new
        |
        `-- no active run --> atomically claim one ticket
                               |
                               v
                     investigator [priority 10]
                               |
                               v
                     normalize completion
                               |
                               v
                 reviewer [priority 30]
                 frozen proposal_json
                      /             \
                 approve           reject
                    |                |
                    v                v
          deterministic publish   rework investigator [20]
                                     |
                                     v
                              normalize completion
                                     |
                                     v
                              fresh reviewer [30]
```

There is one Kanban board. Reviewer cards are **not** pre-created and are not parent-gated. A reviewer is created only after an investigator or rework completion has been normalized into the required metadata contract. The proposal is frozen into the reviewer card as `proposal_json`, so the reviewer and publisher operate on the same payload.

## Lifecycle invariants

- **Global pipeline WIP = 1 SQL run.** Finish review/rework/publication before claiming another ticket.
- **Priorities:** review `30`, rework `20`, new investigation `10`.
- **Review loop:** `review_cycle`, independent of SQL `AttemptNo`; `MAX_REVIEW_CYCLES = 3`.
- **Central authority:** `Model_Bench/l2_pipeline_runtime.py` owns normalization, reviewer creation, rejection/rework, approval publication, and orphan recovery.
- **Event hook = acceleration only.** `xstudio-l2-orchestrator` triggers the same reconciler after `kanban_complete` / `kanban_block`.
- **2-minute scout = correctness backstop.** It reconciles before every claim.
- **Resolution binding fails closed.** An approved `RESOLUTION` is not published unless the live resolved Helpdesk status is bound.
- **No model-controlled ticket status.** Model-supplied `new_ticket_status` is ignored unless an operator explicitly enables overrides.
- **No automatic Solution article per ticket.** KB promotion is a separate governed lifecycle.

The normative lifecycle specification is `Knowledge/L2_PIPELINE_STATE_MACHINE.md`.

## Agent-facing investigation surface

L2 workers do not build SQL transport themselves. They use one typed plugin tool: `xstudio_l2`.

| Need | Operation |
|---|---|
| Read a known table/view with validated identifiers | `select` |
| Run composed read-only SQL | `query` |
| Narrow likely tables from ticket text | `suggest_tables` |
| Discover real SQL objects | `find_objects` |
| Read one object definition | `get_definition` |
| Validate table/column identifiers | `validate_identifiers` |
| Execute an explicitly allowlisted read procedure | `read_procedure` |
| Refresh the live ticket row | `get_ticket_context` |
| Inspect the run's SQL audit trail | `get_run_actions` |
| Persist ticket-specific findings | `save_ledger` |

`Model_Bench/xstudio_l2_tools_plugin/` registers and guards the tool. `Model_Bench/xstudio_l2_tool_bridge.py` owns the Windows-side interpreter/driver transport and returns bounded JSON.

The worker-facing safety contract is structural:

- raw SQL is read-only;
- write/DDL/EXEC statements are rejected;
- arbitrary stored procedures cannot be executed;
- databases are explicitly allowlisted;
- output is bounded;
- repeated identical failures are circuit-broken;
- model terminal attempts to recreate the database transport are blocked.

Ticket publication is not an agent tool. The deterministic publisher uses the audited Hermes SQL path only after reviewer approval.

## Worker roles

### Investigator

Profile: `l2-investigator-primary` (with `l2-investigator` retained as the dispatcher/operational profile).

The investigator:

1. reads the dispatch bundle and live evidence;
2. uses `xstudio_l2` for database/schema/ticket/ledger work;
3. treats KB/history/mem0 as leads rather than ticket-specific proof;
4. records meaningful ticket-specific findings in the run ledger;
5. completes its own Kanban card with structured metadata.

Required completion metadata:

```text
run_id
ticket_id
response_type
reply_text
```

Useful optional fields include `problem_summary`, `findings`, `root_cause`, and `resolution`.

### Reviewer

Profile: `l2-reviewer-primary` (with `l2-reviewer-fallback` available as a configured fallback role).

The reviewer receives a fresh review card containing the frozen proposal and independently checks the core claim against live evidence. Its only lifecycle decisions are:

```text
kanban_complete  -> approve
kanban_block     -> reject with a specific actionable objection
```

The reviewer never publishes the ticket and never creates its own rework card.

## Response types

| Type | Meaning |
|---|---|
| `UPDATE` | Verified progress exists, but the ticket is not finally resolved. |
| `QUESTION` | A specific requester fact is genuinely required. |
| `RESOLUTION` | The outcome/fix is verified and may be closed through the bound workflow. |
| `L3_ESCALATION` | The cause remains unresolved or is genuinely beyond L2 capability. |
| `NEEDS_HUMAN_ACTION` | Cause and required action are known, but execution is outside the L2 worker's authority. |

The current deployment binding is stored in `deploy/helpdesk_workflow_binding.json`. Do not infer workflow status names from prose or model output.

## Knowledge model

Knowledge is deliberately separated by authority and lifetime:

```text
Git-tracked Knowledge/ documents
    = canonical domain/runtime reference

Governed SQL Solution articles
    = reusable known-issue knowledge with lifecycle state

Problem / ticket history
    = episodic evidence and recurring-root-cause history

mem0
    = compact reusable operational heuristics only

Qdrant
    = retrieval index, not source of truth
```

For current-ticket claims, live SQL evidence outranks snapshots, prior tickets, retrieval hits, and memory.

Start routing with:

- `Knowledge/manifest.json` — machine-readable route map;
- `Knowledge/task-router.md` — human-readable mirror;
- `Knowledge/mental-model.md` and `Knowledge/execution-model.md` — always-loaded current operating model.

## SQL runtime and deployment

`Knowledge/00_Hermes_L2_FULL_INSTALL.sql` is the generated complete SQL bundle. The numbered source files are authoritative inputs; hardening sources `25_ticket_dispatch_hardening.sql` and `55_update_retry_hardening.sql` are already included in the generated full-install bundle.

Do not apply those two files again merely because their source files exist. Edit the numbered source, regenerate the bundle, then deploy the generated bundle.

Deployment sequence is documented in `Knowledge/deploy-hermes-sql.md`.

Hermes-side runtime deployment:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

Local validation:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Validation is intentionally local against the real Windows/WSL/Hermes environment. This project does not rely on GitHub Actions as the authority for production validation.

## Important runtime files

```text
Model_Bench/l2_pipeline_runtime.py
    Single deterministic lifecycle state machine.

Model_Bench/ticket_scout.py
    2-minute reconcile-first claim backstop.

Model_Bench/reconcile_l2_pipeline.py
    Small entrypoint into the central reconciler.

Model_Bench/xstudio_l2_orchestrator_plugin/
    Event-driven reconciler trigger; no lifecycle logic of its own.

Model_Bench/xstudio_l2_tools_plugin/
    Typed xstudio_l2 tool registration and execution guard.

Model_Bench/xstudio_l2_tool_bridge.py
    Harness-owned Windows/SQL transport behind the typed tool.

Model_Bench/kanban_approval_publisher.py
Model_Bench/kanban_reject_bridge.py
Model_Bench/repair_incomplete_completions.py
Model_Bench/enforce_publish_safety_net.py
    Compatibility entrypoints that delegate to l2_pipeline_runtime.py.
    They are not independent workflow engines.

deploy/profiles/
    Current deployable Hermes profile artifacts.

deploy/skills/xstudio/
    Current investigator/reviewer/domain skills.

deploy/cron_jobs.txt
    Mirrored schedule documentation; the scout is the sole mutating lifecycle cron backstop.
```

## Retired architecture

The following designs are historical and must not be restored into current runtime code or instructions:

- a separate `l2-review` board;
- `kanban_forward_bridge.py` cross-board choreography;
- independently scheduled review-board dispatch;
- pre-created / parent-gated reviewer cards;
- backlog `< 3` claiming;
- using SQL `AttemptNo` as the review-loop counter;
- model-based verifier profile names;
- investigator-driven `--draft-response` / `--approve-draft` choreography;
- agent-composed Python/pyodbc/sqlcmd database transport.

Historical documents under `Plans/` and `Agent_Comms/` may describe those designs as history. They are not current operating instructions.

## Change discipline

Before changing lifecycle behavior:

1. read `AGENTS.md`;
2. read `Knowledge/L2_PIPELINE_STATE_MACHINE.md`;
3. trace current callers into `l2_pipeline_runtime.py`;
4. prefer removing dead duplicate paths over adding another coordinator;
5. preserve WIP, frozen-proposal, workflow-binding, publication, and audit safety unless a concrete defect requires changing them;
6. run the local validation suite and inspect live pipeline state before deployment.

The repository should have one current explanation for each mechanism and one implementation authority for each lifecycle transition.
