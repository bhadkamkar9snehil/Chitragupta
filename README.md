# Chitragupta — XStudio / Hermes L2 Helpdesk

Chitragupta is the deterministic L2 support pipeline around the existing XStudio Helpdesk and Hermes Agent. XStudio remains the ticket system. Hermes investigates live evidence, an independent reviewer verifies the proposed response, and deterministic code owns all lifecycle transitions and ticket publication.

The design goal is simple: keep reasoning probabilistic, keep workflow mechanics deterministic.

## Current production architecture

```text
XStudio_Helpdesk.dbo.Complaint_Mst_Tbl
        |
        | ticket_scout.py: reconcile first, then claim only at WIP=0
        v
atomic SQL claim
        |
        v
Jev triage + governed KB retrieval
        |
        v
deterministic real SQL candidates
        |
        v
Jev evidence plan
        |
        v
identifier-bounded probe_table reads
        |
        v
Jev investigation assessment
        |
        v
l2-jev-investigator [priority 10]
compose-only / focused reasoning + very few live reads
        |
        v
frozen proposal
        |
        v
Jev PRIMARY REVIEW
   /          |             |              \
APPROVE     REWORK      L3_ESCALATION   LOCAL_REVIEW
  |           |              |               |
  v           v              v               v
publish     rework[20]    L3 path       qwen reviewer[30]
                                             |
                                      approve / reject
                                         |       |
                                         v       v
                                      publish  rework
```

There is one Kanban board and one deterministic lifecycle authority. A local reviewer card is **not** part of the normal happy path anymore; it is created only when Jev primary review cannot safely route the frozen proposal directly.

## Lifecycle invariants

- **Global pipeline WIP = 1 SQL run.** Finish Jev review/rework/local deep review/publication before claiming another ticket.
- **Priorities:** local deep review `30`, rework `20`, new investigation `10`.
- **Review loop:** `review_cycle`, independent of SQL `AttemptNo`; `MAX_REVIEW_CYCLES = 3`.
- **Central authority:** `Model_Bench/l2_pipeline_runtime.py` owns claim coordination, proposal normalization, Jev review routing, local-review fallback creation, rework/escalation, publication, and orphan recovery.
- **Jev owns semantic judgments, not mechanics.** SQL safety, workflow binding, WIP, mutations, and publication remain deterministic.
- **Event hook = acceleration only.** `xstudio-l2-orchestrator` triggers the same reconciler after Kanban completion/block.
- **2-minute scout = correctness backstop.** It reconciles before every claim.
- **Resolution binding fails closed.** A `RESOLUTION` cannot publish unless the live Helpdesk resolved status is bound.
- **No model/Jev-controlled raw Helpdesk status.** Workflow values come from the deployment binding.
- **No automatic Solution article per ticket.** KB promotion remains a separate governed lifecycle.

The normative lifecycle specification is `Knowledge/L2_PIPELINE_STATE_MACHINE.md`.

## Agent-facing investigation surface

The worker has one typed evidence surface: `xstudio_l2`. Jev is **not** exposed as a worker tool; deterministic runtime code invokes reviewed System One workflows before/after the local model.

| Need | Tool / operation |
|---|---|
| Read a known table/view with validated identifiers | `xstudio_l2.select` |
| Deterministically probe a Jev-selected real candidate by strong ticket identifier | `xstudio_l2.probe_table` |
| Run composed read-only SQL | `xstudio_l2.query` |
| Narrow likely tables from ticket text | `xstudio_l2.suggest_tables` |
| Discover real SQL objects | `xstudio_l2.find_objects` |
| Read one object definition | `xstudio_l2.get_definition` |
| Validate table/column identifiers | `xstudio_l2.validate_identifiers` |
| Execute an explicitly allowlisted read procedure | `xstudio_l2.read_procedure` |
| Refresh the live ticket row | `xstudio_l2.get_ticket_context` |
| Inspect the run SQL/action audit | `xstudio_l2.get_run_actions` |
| Persist ticket-specific findings | `xstudio_l2.save_ledger` |

The worker-facing safety contract is structural:

- arbitrary SQL is read-only;
- write/DDL/EXEC is rejected;
- stored procedures require an explicit allowlist;
- databases and schema identifiers are validated;
- automatic `probe_table` refuses broad reads without a strong identifier-to-column mapping;
- raw evidence is returned as read; Jev does not replace/filter SQL result rows inside `xstudio_l2`;
- output is bounded;
- repeated identical failures are circuit-broken;
- terminal attempts to recreate database transport are blocked.

Ticket publication and Jev orchestration are never worker tools.

## Worker roles

### Jev-first investigator

Default profile: `l2-jev-investigator`.

Most of the old context-understanding burden is completed before this profile sees the card. It receives:

- Jev ticket characterization;
- canonical route/route skill;
- deterministic real schema candidates;
- Jev candidate/evidence plan;
- bounded live probe results;
- Jev investigation assessment;
- governed KB hits with applicability/negative-indicator judgments;
- prior run ledger/history where relevant.

If the package is already sufficient, its scope is `COMPOSE_ONLY`; normally it should turn evidence into a concise structured proposal, not rediscover the schema. If evidence remains incomplete, it gets a small focused-read budget.

`l2-investigator-primary` remains available as a compatibility/fallback profile.

### Jev primary reviewer

Jev is the default semantic reviewer of the frozen proposal. Deterministic thresholds decide whether its typed result can route directly to publish/rework/escalation.

### Local deep reviewer

Profiles: `l2-reviewer-primary` and `l2-reviewer-fallback`.

They are invoked only for `LOCAL_REVIEW`, Jev unavailability/low-confidence safety-gate failure, contradictory evidence, or genuinely deep reasoning. They verify the smallest disputed live fact rather than replaying the whole investigation.

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
  -> Jev investigation assessment + meta-attention
       evidence sufficiency / response type / known-solution fit /
       root-cause family / human-action need / local-reasoning need /
       per-context-chunk presentation Score
  -> deterministic context compiler
       whole-chunk FULL / COMPACT / SUMMARY / OMIT
       current ticket + live SQL evidence pinned
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
5. sends those bounded live rows plus approved KB candidates back through Jev investigation assessment;
6. asks independent per-chunk meta-attention Scores in that **same** System One request;
7. deterministically builds a model-facing context view by whole chunks rather than dumping/truncating the raw bundle.

The current ticket and gathered live-SQL evidence cannot be attention-omitted; a Jev-selected known solution is likewise pinned to at least a compact representation. Lower-value history, KB alternatives and discovery backlog can be summarized or omitted, with recovery hints retained.

The local model receives this compiled evidence view. If Jev judges the evidence sufficient and deeper reasoning unnecessary, the profile is told to **compose only** and is budgeted one additional live read. Otherwise it gets a small focused-reasoning budget rather than the old open-ended discovery problem.

probe_table never issues a broad automatic query when no strong identifier maps to the candidate schema. In that case the package explicitly says automatic probing was not possible and the bounded coordinator decides whether one focused live read is justified.

### Harness-owned Jev workflows

Deterministic runtime code owns Jev invocation. The Windows bridge exposes only the production workflows the runtime currently needs: bounded evidence planning, investigation assessment/meta-attention, and primary proposal review. Ticket trust screening is coalesced into ticket triage; KB trust screening is coalesced into KB applicability, so identical state is not sent through separate Jev requests. There is no model-facing Jev tool and no arbitrary-question surface.

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
Model_Bench/jev/client.py                    one System One transport adapter
Model_Bench/jev/ticket_triage.py            ticket characterization/routing
Model_Bench/jev/evidence_plan.py            bounded evidence selection
Model_Bench/jev/investigation_assessment.py structured evidence interpretation + meta-attention
Model_Bench/jev/reviewer.py                 primary semantic reviewer
Model_Bench/jev/kb_applicability.py         KB applicability
Model_Bench/jev/kb_curation.py              KB curation
Model_Bench/jev/trace_assessment.py         trace quality
Model_Bench/jev/audit.py                    existing-run + trace persistence
Model_Bench/jev_workflow_bridge.py          Windows harness bridge
deploy/profiles/l2-jev-investigator/        default Jev-first synthesis coordinator
~~~

The upstream TypeSafe skill is installed project-locally at `.agents/skills/typesafe-ai/SKILL.md`.

### Active behavior and configuration

Jev is active in harness-owned triage/trust screening, evidence planning/assessment/meta-attention, KB applicability/trust checks, trace assessment, and primary review. Deterministic structural rules remain higher authority: explicit identifier routing, schema existence, read-only SQL, procedure allowlists, workflow binding, WIP, and publication state are code-owned.

~~~text
TYPESAFE_API_KEY                              required in Windows Python/service environment
TYPESAFE_DEFAULT_MODEL                        default jev-latest
TYPESAFE_BASE_URL                             optional API base override
CHITRAGUPTA_JEV_ENABLED                       default 1
CHITRAGUPTA_JEV_AUDIT_ENABLED                 default 1
CHITRAGUPTA_JEV_MIN_CONFIDENCE                default 0.70
CHITRAGUPTA_JEV_TIMEOUT_SECONDS               default 10
CHITRAGUPTA_JEV_KB_ENABLED                    default 1
CHITRAGUPTA_JEV_TRACE_ENABLED                 default 1
CHITRAGUPTA_JEV_SECURITY_ENABLED              default 1
CHITRAGUPTA_JEV_FIRST_INVESTIGATION_ENABLED   default 1
CHITRAGUPTA_JEV_DIRECT_APPROVAL_CONFIDENCE    default 0.82
CHITRAGUPTA_JEV_DIRECT_REWORK_CONFIDENCE      default 0.88
~~~

There is no repository credential fallback. Never commit `.env` secrets or put TypeSafe credentials into prompts, Kanban cards, ticket text, trace payloads, or model-visible configuration.

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
Model_Bench/jev_workflow_bridge.py
    Harness-owned System-One workflows and Windows bridge.

Model_Bench/jev_trace_assessor.py
Model_Bench/jev_post_resolution_curation.py
    Out-of-band trace-quality assessment and advisory KB curation.

Model_Bench/kb_retrieval.py
    Deterministic relevance gate plus Jev triage, applicability,
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
