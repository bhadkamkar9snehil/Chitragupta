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

## TypeSafe Jev System-One control fabric

Jev is now a **primary semantic control layer** inside Chitragupta. It is not a free-form agent and it is not a parallel lifecycle engine. TypeSafe System One performs narrow typed semantic work (Choice, Noul, Score) while deterministic code retains authorization, SQL safety, workflow state, WIP, mutation, publication, and retry/rework limits.

~~~text
SQL claim
  -> Jev ticket triage
       route / ambiguity / complexity / domain / known-issue likelihood
  -> deterministic candidate generation
       real tables/views/SPs/KB only
  -> Jev evidence plan + candidate rerank
  -> deterministic identifier-bounded live probes
  -> Jev investigation assessment
       evidence sufficiency / response type / known-solution fit /
       root-cause family / human-action need / local-reasoning need
  -> l2-jev-investigator
       normally synthesis + at most a few missing live reads
  -> frozen proposal
  -> Jev PRIMARY REVIEW
       APPROVE       -> deterministic publish
       REWORK        -> bounded rework
       L3_ESCALATION -> deterministic escalation
       LOCAL_REVIEW  -> qwen local reviewer only for ambiguity/conflict/deep reasoning
  -> deterministic publish/rework/escalation

xstudio-l2-trace
  -> local append only
  -> SQL trace drain
  -> Jev trace assessment
  -> semantic quality / silent-failure / attention metrics

verified RESOLUTION
  -> Jev near-duplicate KB rerank
  -> REUSE_EXISTING / UPDATE_EXISTING / CREATE_CANDIDATE / NONE
  -> governed KB workflow; no direct article promotion by Jev
~~~

This deliberately removes the old assumption that every proposal must consume a second local-model review. The local reviewer is now an **exception/deep-review path**. Jev is the normal semantic reviewer; deterministic code decides whether its typed result meets the configured thresholds for direct publish/rework/escalation.

### Jev-first investigation

l2-jev-investigator is the default investigator profile. It is a bounded Hermes coordinator, not a second broad reasoning agent.

Before the profile starts, the runtime already:

1. runs parallel Jev ticket characterization;
2. narrows real SQL candidates deterministically;
3. has Jev choose/rate the useful candidates;
4. runs probe_table only where a strong ticket identifier maps to a real allowlisted column;
5. sends those bounded live rows plus approved KB candidates back through Jev investigation assessment.

The local model receives this compact evidence package. If Jev judges the evidence sufficient and deeper reasoning unnecessary, the profile is told to **compose only** and is budgeted one additional live read. Otherwise it gets a small focused-reasoning budget rather than the old open-ended discovery problem.

probe_table never issues a broad automatic query when no strong identifier maps to the candidate schema. In that case the package explicitly says automatic probing was not possible and the bounded coordinator decides whether one focused live read is justified.

### Bounded Hermes Jev plugin

xstudio-l2-jev registers the typed xstudio_jev toolset. It exposes reviewed workflows only: ticket triage, evidence planning, investigation assessment, candidate reranking, primary review / proposal preflight, KB applicability and curation, trace assessment, untrusted-context screening, model/profile routing, and L1 support-action selection.

There is no arbitrary "ask Jev anything" operation.

### Storage: reuse the run and trace model

Jev is another investigator/reviewer for the same Hermes run, so there is **no separate Jev business table**.

Hermes_L2_Response_Trn_Tbl carries stage summaries:

~~~text
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
~~~

Every System One call is also written to the existing Hermes_Agent_Trace_Trn_Tbl as EventType=jev_system_one. KB retrieval telemetry likewise reuses the trace stream. This keeps one run spine and one observability stream.

### Shared implementation

~~~text
Model_Bench/jev/client.py                   one System One transport adapter
Model_Bench/jev/ticket_triage.py           ticket classification
Model_Bench/jev/evidence_plan.py           bounded evidence selection
Model_Bench/jev/investigation_assessment.py structured evidence interpretation
Model_Bench/jev/reviewer.py                 primary semantic reviewer
Model_Bench/jev/candidate_rerank.py         real-candidate reranking
Model_Bench/jev/kb_applicability.py         KB applicability
Model_Bench/jev/kb_curation.py              KB curation
Model_Bench/jev/trace_assessment.py         trace quality
Model_Bench/jev/security.py                 untrusted-context screening
Model_Bench/jev/tool_semantics.py           semantic tool circuit breaker
Model_Bench/jev/model_routing.py            bounded profile routing
Model_Bench/jev/l1_action.py                L1 action selection
Model_Bench/jev/audit.py                    existing-run + trace persistence
Model_Bench/jev_workflow_bridge.py          Windows deterministic bridge
Model_Bench/xstudio_l2_jev_plugin/          bounded Hermes xstudio_jev toolset
deploy/profiles/l2-jev-investigator/        default Jev-first coordinator
~~~

Model_Bench/typesafe_jev.py remains only as a compatibility facade for the original choose_route() entrypoint. The upstream TypeSafe skill is installed project-locally at .agents/skills/typesafe-ai/SKILL.md.

### Active behavior and configuration

There is no Jev shadow mode. Jev routing, KB reranking, Jev-first evidence planning, primary semantic review, and semantic query circuit-breaking are active integrations. Deterministic structural rules remain higher authority where applicable: a single explicit identifier route, schema existence, read-only SQL, procedure allowlists, workflow binding, and publication state are still code-owned.

~~~text
TYPESAFE_DEFAULT_MODEL                           default jev-latest
TYPESAFE_BASE_URL                                optional API base override
CHITRAGUPTA_JEV_ENABLED                          default 1
CHITRAGUPTA_JEV_MIN_CONFIDENCE                   default 0.70
CHITRAGUPTA_JEV_TIMEOUT_SECONDS                  default 10
CHITRAGUPTA_JEV_TOOL_RERANK_ENABLED              default 1
CHITRAGUPTA_JEV_KB_ENABLED                       default 1
CHITRAGUPTA_JEV_TRACE_ENABLED                    default 1
CHITRAGUPTA_JEV_SECURITY_ENABLED                 default 1
CHITRAGUPTA_JEV_ADAPTIVE_REVIEW_ENABLED          default 1
CHITRAGUPTA_JEV_SEMANTIC_TOOL_BLOCKING_ENABLED   default 1
CHITRAGUPTA_JEV_PRIMARY_REVIEW_ENABLED            default 1
CHITRAGUPTA_JEV_FIRST_INVESTIGATION_ENABLED       default 1
CHITRAGUPTA_JEV_DIRECT_APPROVAL_CONFIDENCE        default 0.82
CHITRAGUPTA_JEV_DIRECT_REWORK_CONFIDENCE          default 0.88
~~~

For this dev deployment the explicitly supplied TypeSafe credential is wired through deploy/dev/typesafe.env. client.py prefers a normal TYPESAFE_API_KEY environment value when present and otherwise reads that dev file. The credential is used only to create the HTTP Authorization header; do not put it into prompts, Kanban cards, ticket text, trace payloads, or model-visible configuration.
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

Model_Bench/jev/
Model_Bench/typesafe_jev.py
Model_Bench/jev_workflow_bridge.py
    Shared System-One judgment fabric, compatibility facade, and harness-owned
    Windows bridge for semantic workflows/audit persistence.

Model_Bench/jev_trace_assessor.py
Model_Bench/jev_post_resolution_curation.py
    Out-of-band trace-quality assessment and advisory KB curation.

Model_Bench/kb_retrieval.py
    Deterministic relevance gate plus shadow-mode Jev triage, applicability,
    negative-indicator, and untrusted-context judgments.

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
