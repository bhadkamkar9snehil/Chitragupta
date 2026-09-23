# Qwen 9B Harness Review and Improvement Recommendations

**Status:** Design/recommendation document — non-normative  
**Target:** Chitragupta L2 / Hermes local-model harness  
**Primary small-model target:** Qwen-class local model around 9B parameters  
**Based on repository state:** `f940c7e37751d973be81ecfb66ea4651cd0ad6a1`  
**Date:** 2026-09-23

> This document does **not** replace `AGENTS.md` or `Knowledge/L2_PIPELINE_STATE_MACHINE.md`.
> Those remain the engineering/runtime and lifecycle authorities. This document records a detailed
> review of the current Qwen harness and concrete recommendations for making a small local model
> more reliable, less wasteful, and easier to control.

---

## 1. Executive conclusion

The current Chitragupta architecture is fundamentally **correct for a small local model**.

The strongest architectural choice is that **Qwen is not the agent architecture**. Qwen is a bounded
System-Two reasoning component inside a larger deterministic harness.

The harness already removes many responsibilities that generic agent frameworks usually leave to the
model:

- ticket claiming and lifecycle ownership;
- workflow binding;
- queueing and concurrency;
- GBrain dependency checks;
- ticket routing and semantic triage;
- deterministic schema narrowing;
- evidence planning;
- initial live SQL probes;
- execution-depth selection;
- context selection and compression;
- SQL safety and identifier validation;
- evidence persistence;
- semantic primary review;
- retry/rework limits;
- publication;
- orphan/stale recovery.

That inversion of control is exactly the right direction for a 9B model.

The next stage should therefore **not** be “give Qwen more autonomy.” It should be:

1. give Qwen **fewer choices per turn**;
2. give it **one unambiguous completion path**;
3. remove work that Jev/harness already completed;
4. expose only the smallest useful action surface;
5. keep durable evidence outside the model context;
6. make every corrective error tell the model the exact next legal action;
7. continuously improve the starting package from verified prior experience.

The central design rule for the next iteration should be:

> **Use Qwen only for the part that actually requires semantic synthesis or bounded reasoning. Everything
> else should be deterministic state, retrieval, typed execution, or validation.**

---

# 2. Current architecture

The repository defines five architectural responsibilities:

```text
                         XSTUDIO HELPDESK
                         Complaint_Mst_Tbl
                                |
                                v
                    +-----------------------+
                    | CHITRAGUPTA CONTROL   |
                    | deterministic harness |
                    +-----------+-----------+
                                |
             +------------------+------------------+
             |                                     |
             v                                     v
       JEV / SYSTEM ONE                     EVIDENCE / KNOWLEDGE
       semantic judgments                  Live SQL
       evidence planning                   GBrain
       execution depth                     Solution KB
       meta-attention                      semantic atlas / recipes
       primary review                      ticket/run evidence
             |                                     |
             +------------------+------------------+
                                |
                                v
                        EXECUTION CONTRACT
                 QWEN_FREE / COMPOSE_ONLY /
                     FOCUSED_REASONING
                                |
                       only when necessary
                                v
                        HERMES / QWEN
                       bounded System Two
                                |
                         typed tools only
                                |
                                v
                         FROZEN PROPOSAL
                                |
                                v
                       JEV PRIMARY REVIEW
                    /        |        |       \
               APPROVE    REWORK      L3   LOCAL_REVIEW
                   |         |              |
                   v         v              v
             deterministic  bounded       exceptional
             publish gates  rework        System-Two review
```

The important point is that the model sits **inside** this system. It does not own the system.

---

# 3. End-to-end runtime trace

This section follows the current harness from one function to the next.

## 3.1 Scout entry

`Model_Bench/ticket_scout.py` enters:

```text
l2_pipeline_runtime.scout()
```

`scout()` first calls:

```text
reconcile()
```

The reconciler currently owns the lifecycle repair pass:

```text
recover_failed_workers()
list_tasks()
query_active_runs()

_sync_local_model_completions()
_recover_stale_local_model_leases()

normalize_investigator_completions()
process_unreviewable_completions()
process_jev_primary_reviews()
process_rejections()
process_approvals()

recover_orphan_runs()
_dispatch_next_local_model_task()
```

This is correct. Recovery, release, review, rework and queue admission belong to the harness, not the
model.

After reconciliation, `scout()` verifies:

```text
load_workflow_binding()
check_worker_dependencies()
check_gbrain_dependency()
```

GBrain is intentionally a dependency in this architecture. New claims do not proceed if the required
knowledge plane is unavailable.

The runtime then claims through the audited orchestrator path:

```text
run_orchestrator(--poll)
    ->
Hermes_Orchestrator
    ->
Hermes_L2_Claim_Ticket_Usp
```

The SQL procedure is the capacity/claim authority.

---

## 3.2 Claimed-ticket preparation

A successful claim enters:

```text
_prepare_claimed_ticket()
```

which calls:

```text
_investigation_bundle()
```

The bundle gathers the ticket's working world before Qwen is asked to reason.

Its inputs include:

- current Helpdesk context;
- prior run ledger;
- prior attempts;
- deterministic table/object candidates;
- canonical route material;
- governed Solution articles;
- GBrain retrieval;
- semantic atlas / route data.

The bundle then invokes the Jev-first path.

---

## 3.3 Jev-first investigation

The primary entry is:

```text
_jev_first_investigation()
```

The intended sequence is:

```text
requester-grounded ticket
        |
        v
real deterministic candidates
        |
        v
Jev evidence_plan
        |
        v
ranked/select candidate objects
        |
        v
bounded deterministic probe_table reads
        |
        +--> optional atlas relationship hops
        |
        v
Jev investigation assessment
        |
        +--> evidence sufficiency
        +--> known-solution applicability
        +--> execution depth
        +--> route skill need
        +--> per-context-chunk meta-attention
```

The initial probes are bounded. The harness does not let Qwen start with “search the database and see what
you find.”

This is one of the strongest parts of the design.

---

## 3.4 Context construction

The harness converts the state into explicit chunks through:

```text
_make_context_chunks()
```

Current chunk types include:

- current ticket;
- routing/triage;
- prior ledger;
- prior attempts;
- evidence plan;
- deterministic candidate backlog;
- governed Solution articles;
- GBrain hits;
- live SQL probes.

Each chunk carries authority/provenance metadata.

GBrain results are correctly treated as knowledge leads rather than ticket-specific live proof.

The Jev assessment also scores each chunk for how much detail the next local reasoning step needs:

```text
0 = OMIT
1 = SUMMARY
2 = COMPACT
3 = FULL
```

The deterministic compiler then runs:

```text
_compile_model_context()
```

The compiler applies floors to important evidence. Current ticket and live evidence cannot simply disappear
because a semantic score was low.

This is the right model for small-model context management:

> semantic selection can reduce optional information, but deterministic safety policy protects evidence
> that the model must see.

---

# 4. Execution depth

The harness determines one of three execution modes:

```text
QWEN_FREE
COMPOSE_ONLY
FOCUSED_REASONING
```

This is a major strength.

A small model should not be asked to decide how much autonomy it deserves.

## 4.1 QWEN_FREE

If deterministic evidence plus Jev judgment is sufficient, the harness attempts:

```text
_try_qwen_free_handoff()
    ->
_jev_primary_review()
    ->
_publish_frozen_proposal()
```

Qwen is skipped entirely.

This should remain a first-class optimization. The best small-model inference call is often the call that
does not need to happen.

## 4.2 COMPOSE_ONLY

Qwen should receive evidence that is already sufficient or nearly sufficient and perform the narrow task
of translating that evidence into a structured proposal.

The expected behavior is:

```text
read supplied evidence
    ->
synthesize
    ->
submit proposal
```

It should not rediscover the route, schema, ticket or database transport.

## 4.3 FOCUSED_REASONING

Qwen receives a small bounded recovery budget for additional evidence.

The expected behavior is:

```text
read supplied evidence
    ->
identify one material missing fact
    ->
perform a small number of typed reads
    ->
submit proposal
```

The distinction between COMPOSE_ONLY and FOCUSED_REASONING is exactly the kind of explicit cognitive
budgeting that benefits a 9B model.

---

# 5. Local-model queue and admission

If Qwen is required, the runtime constructs the exact task specification and persists it through:

```text
_queue_local_model_task()
```

The exact work package is stored before execution.

The shared model slot is admitted through SQL:

```text
_dispatch_next_local_model_task()
    ->
--local-model-action acquire
    ->
_materialize_acquired_local_model_task()
    ->
Hermes Kanban task
    ->
bind SQL lease to task ID
```

The architecture intentionally separates:

```text
pipeline concurrency != local-model concurrency
```

Several tickets can be active in deterministic/Jev phases while only one local Qwen task is running.

For the current local hardware/model constraints, this is correct.

---

# 6. Qwen's current role

The default profile is `l2-jev-investigator`.

The role is already appropriately narrow:

- consume the compiled context;
- obey `local_model_scope`;
- use only bounded typed reads;
- do not invoke Jev;
- do not rediscover already-provided context;
- do not use terminal/pyodbc/sqlcmd;
- do not mutate Helpdesk/production/configuration state;
- do not choose live workflow statuses;
- do not publish;
- do not claim unexecuted actions occurred;
- compose a structured proposal.

That is the right role for a small local model.

The worker-facing database surface is also structurally constrained through named `xstudio_*` tools.

---

# 7. Completion and proposal normalization

The preferred worker handoff is:

```text
xstudio_submit_proposal(...)
```

This is significantly better for a 9B model than requiring it to build a deeply nested claims/evidence
object.

The flat tool asks for model-friendly fields such as:

```text
response_type
summary
claim_status
action_id
reply_text
requester_question
evidence_status
problem_summary
root_cause
resolution
```

The harness then assembles the more complex evidence/claims contract.

This follows an important small-model design principle:

> **The model should provide semantic values. The harness should provide structural ceremony.**

The plugin also contains defensive repair for malformed tool markup and missing completion metadata. Those
repairs are justified because the same failure patterns have been observed live.

---

# 8. Post-Qwen flow

After the Qwen card becomes terminal, reconciliation:

1. releases the SQL local-model slot;
2. normalizes the completion if needed;
3. locates the frozen proposal;
4. runs Jev primary review;
5. routes the decision.

The review path is:

```text
_pending_primary_review()
    ->
_jev_primary_review()
    ->
_apply_primary_review()
```

The outcomes are:

```text
APPROVE
    -> pre_publish_gate_reason()
    -> _publish_frozen_proposal()

REWORK
    -> create_rework_card()

L3_ESCALATION
    -> _escalate_run()

LOCAL_REVIEW
    -> create_reviewer_card()
```

This is a strong separation of responsibilities.

The model proposes. The harness decides whether that proposal is allowed to affect ticket state.

---

# 9. Is this a good harness pattern for a 9B model?

Yes.

A generic agent often asks the model to do all of the following:

- understand the entire application;
- choose a route;
- discover tools;
- discover schemas;
- decide what evidence matters;
- plan;
- query;
- recover from query failures;
- remember prior evidence;
- decide when enough evidence exists;
- construct output;
- validate output;
- review itself;
- perform state transitions.

That is far too much branching responsibility for a small model.

Chitragupta now moves most of these decisions outside Qwen.

| Responsibility | Generic agent | Current Chitragupta |
|---|---|---|
| ticket claim | model/tool loop | deterministic SQL |
| lifecycle state | model/session | deterministic runtime + SQL |
| route | model | Jev |
| candidate objects | model | deterministic harness |
| candidate prioritization | model | Jev |
| initial evidence | model | deterministic probes |
| context selection | implicit | Jev + compiler |
| execution depth | model | harness |
| database safety | prompt | structural tool boundary |
| identifier validation | model | bridge |
| evidence identity | prose | ActionID/run audit |
| nested proposal structure | model | harness |
| semantic review | same model | Jev |
| deep review | same model | exceptional separate path |
| publication | model | deterministic runtime |
| retries/recovery | model | state machine |

This is the correct inversion of control.

---

# 10. Remaining small-model friction

The architecture is sound, but the current worker interface still contains several places where Qwen is
given unnecessary or conflicting choices.

These are the highest-value harness improvements.

---

## 10.1 Recommendation 1 — one completion mechanism only

### Current problem

The current instructions are inconsistent.

`deploy/profiles/l2-jev-investigator/SOUL.md` still tells the worker to return structured
`kanban_complete` metadata.

The workflow skill says:

```text
Preferred: xstudio_submit_proposal
```

The plugin's redirect is even stronger:

```text
Do not complete with kanban_complete.
Call xstudio_submit_proposal now...
```

For a stronger frontier model, this is untidy.

For a 9B model, this is a real source of wasted turns and wrong completion behavior.

### Recommended contract

For investigator/rework stages:

```text
The only successful completion action is:

    xstudio_submit_proposal(...)

Do not call kanban_complete directly.
Do not build nested proposal metadata yourself.
```

The harness/plugin should own the final Kanban completion after the proposal tool has validated and
assembled the structured metadata.

### Why

Small models perform better when there is:

- one finish action;
- one schema;
- one success message;
- one correction path.

There should not be two legal completion APIs with different structural complexity.

### Files likely involved

- `deploy/profiles/l2-jev-investigator/SOUL.md`
- `deploy/skills/xstudio/xstudio-l2-ticket-workflow/SKILL.md`
- `Model_Bench/xstudio_l2_tools_plugin/__init__.py`
- relevant plugin tests

---

## 10.2 Recommendation 2 — do not ask Qwen to route a ticket that Jev already routed

### Current problem

The workflow skill currently includes:

```text
2. Route the ticket.
   Use Knowledge/manifest.json / task-router.md and the narrowest domain skill.
```

But before Qwen starts, the harness has already executed:

- ticket characterization;
- route candidate evaluation;
- evidence planning;
- deterministic candidate construction;
- route-skill selection.

Asking Qwen to route again creates unnecessary branching and an opportunity to contradict the harness.

### Recommended contract

The card should instead state:

```text
HARNESS ROUTE
route: sap_posting
route_authority: Jev/harness

Do not reroute the ticket.
Use this route unless the supplied live evidence directly demonstrates that the harness package is
internally inconsistent. If so, submit a bounded uncertainty/rework outcome rather than inventing a new
route.
```

### Why

A small model should not be asked to recompute an already-decided control-plane decision.

The principle is:

```text
harness decides route
model reasons within route
```

---

## 10.3 Recommendation 3 — add an explicit next-action frontier

The execution contract currently expresses execution mode and read budget. It can be made even easier for
a small model by explicitly expressing the **legal next-action frontier**.

Example:

```text
EXECUTION MODE: FOCUSED_REASONING

CURRENT MATERIAL GAP:
Whether MaterialDocument exists for ProductionOrder 123456.

ALREADY VERIFIED:
- Production order exists.
- SAP interface request completed.
- No posting error in supplied log evidence.

LEGAL NEXT ACTIONS:
1. xstudio_sap_api_context
2. xstudio_get_run_actions
3. xstudio_submit_proposal

MAX ADDITIONAL LIVE READS:
1

DONE CONDITION:
- verify the material document and submit the correct outcome; OR
- establish that the fact cannot be obtained inside L2 scope and submit the appropriate non-resolution
  outcome.
```

This is stronger than a general instruction such as “investigate the ticket with at most one additional
read.”

It turns the model's job into a small decision problem.

### Implementation principle

The harness should derive the frontier from information it already owns:

- execution mode;
- route;
- Jev evidence gap;
- available typed tool capabilities;
- read budget;
- current evidence state.

Do not add a new planner just to produce this block.

---

## 10.4 Recommendation 4 — fewer visible tools, not deferred tool discovery

### Current state

The profile can expose a substantial list of named XStudio tools plus generic Hermes surfaces.

The repository already contains a real reason not to rely on deferred tool discovery for the 9B model:
`patch_tool_search_off.py` documents Ticket_360, where the worker searched for the correct tool, found it,
then failed to actually call it and incorrectly concluded that database access was unavailable.

### External comparison: Codex tool search

Current OpenAI agent tooling supports deferred tool discovery so capable models can dynamically search and
load tool definitions instead of carrying every tool schema in context.

Reference:
- https://developers.openai.com/api/docs/guides/tools-tool-search

That is useful for stronger models and very large tool catalogs.

It is **not** the pattern recommended here.

### Small-model adaptation

For Qwen 9B:

> **Eagerly expose a very small action set.**

Conceptually:

```text
COMPOSE_ONLY
    xstudio_get_run_actions
    xstudio_submit_proposal
    [optional l2_recall only when recovery is explicitly allowed]

FOCUSED_REASONING / HEAT
    xstudio_heat_context
    xstudio_select
    xstudio_query
    xstudio_get_run_actions
    l2_recall
    xstudio_submit_proposal

FOCUSED_REASONING / SAP
    xstudio_sap_api_context
    xstudio_select
    xstudio_query
    xstudio_get_run_actions
    l2_recall
    xstudio_submit_proposal
```

### Important constraint

Do **not** create a separate long-lived agent/profile for every route.

Prefer, in order:

1. per-task/per-stage tool visibility if Hermes supports it cleanly;
2. a small number of existing role surfaces;
3. current eager tool surface if dynamic restriction would require architectural complexity.

The benefit must justify the implementation.

---

# 11. Recommendation 5 — account for the entire model input, not only compiled chunks

The current context compiler correctly budgets the Jev-selected context chunks.

However, the model's actual input consists of more than those chunks:

```text
Hermes/base system prompt
+ SOUL
+ skill instructions
+ tool definitions
+ task/card body
+ compiled context
+ conversation history
+ prior tool calls
+ prior tool results
+ wrapper/provider metadata
```

A card can therefore be “within context budget” while still being cognitively expensive.

## Recommended addition

Create a lightweight deterministic **L2 Model Input Report** for every local-model task.

Example:

```text
L2 MODEL INPUT REPORT

profile_static_chars:       ...
soul_chars:                 ...
skill_chars:                ...
tool_schema_chars:          ...
card_chars:                 ...
compiled_context_chars:     ...
existing_history_chars:     ...
tool_result_chars:          ...
estimated_total_tokens:     ...

execution_mode: COMPOSE_ONLY
visible_tool_count: 4
compiled_chunk_count: 6
omitted_chunk_count: 9
```

This should be observability, not another lifecycle dependency.

## Why

The optimization target for a 9B model should not merely be:

```text
fits inside the context window
```

It should be:

```text
minimum relevant cognitive context
```

---

# 12. Recommendation 6 — deterministic evidence compaction

OpenClaw distinguishes conversation compaction from lighter-weight tool-result pruning.

Relevant references:

- https://github.com/openclaw/openclaw/blob/main/docs/concepts/context.md
- https://github.com/openclaw/openclaw/blob/main/docs/concepts/compaction.md

The useful idea for Chitragupta is **not generic conversation summarization**.

Chitragupta already has a stronger durable evidence store:

```text
Hermes_L2_SQL_Action_Trn_Tbl
```

The model should not need to retain every raw tool result in its active reasoning context after that result
has been persisted.

## Recommended pattern

A live read may initially return the bounded evidence necessary for the current turn.

On later turns, the model should be able to see a compact reference such as:

```text
ACTION A123
tool: xstudio_heat_context
object: EAF_Per_Heat
rows: 1

KEY EVIDENCE
- HeatNo = 1604015
- PowerOnTime = ...
- MaterialDocument = ...

FULL AUDIT
Hermes_L2_SQL_Action_Trn_Tbl.ActionID = A123
```

If deeper inspection is necessary, a typed action can recover it.

## Benefits

- less repeated raw JSON;
- lower attention burden;
- evidence identity is preserved;
- reviewers can cite the exact same ActionID;
- no loss of auditability;
- no model-generated summary becomes the source of truth.

This should be called **evidence compaction**, not memory summarization.

---

# 13. Recommendation 7 — keep the stable prompt prefix stable

Current Codex/Agents guidance separates the harness from the execution environment and explicitly treats
tool/prompt organization and caching as part of agent engineering.

References:

- https://developers.openai.com/api/docs/guides/agents
- https://developers.openai.com/api/docs/guides/agents-api/architecture

For the local-model path, arrange the prompt conceptually as:

```text
STATIC
------
Hermes system
small-model behavioral contract
stable tool schemas

MOSTLY STATIC
-------------
role / narrow skill

VARIABLE
--------
execution contract
ticket
compiled evidence
latest tool results
```

Do not reorder or regenerate large static blocks unnecessarily.

If the active LM Studio/llama.cpp backend can reuse prefix/KV state, this layout also gives it the best
opportunity to do so.

This recommendation should remain backend-agnostic: do not add a cache subsystem unless the actual local
backend exposes one that can be verified.

---

# 14. Recommendation 8 — make corrective errors executable

A 9B model should not receive vague errors.

Bad:

```text
Missing required argument.
```

Better:

```text
CALL REJECTED

missing: database

Retry the SAME operation once with:
database="XStudio_Xbatch"

Do not change the table or broaden the query.
```

Best, where deterministic context already knows the correction:

```text
CALL REPAIRED BY HARNESS
database="XStudio_Xbatch" was injected from the current route contract.
```

The repository already follows this direction for:

- missing run identity;
- database routing;
- columns;
- malformed submit markup;
- proposal completion.

Continue that pattern.

The general rule should be:

> **If the harness knows the answer deterministically, repair it. If it does not, return one exact bounded
> correction instruction.**

Do not consume a model turn on ceremony that code can perform safely.

---

# 15. Recommendation 9 — use OpenCode's permission idea, not its agent count

OpenCode's current design supports per-agent permissions and the ability to hide skills/tools entirely.

References:

- https://github.com/mudrii/opencode-docs/blob/main/docs/official/agents.md
- https://github.com/mudrii/opencode-docs/blob/main/docs/official/skills.md

The useful principle is:

```text
role/stage -> explicit allowed action surface
```

Chitragupta should **not** turn that into dozens of domain agents.

Do not create:

```text
heat-agent
sap-agent
batch-agent
material-agent
configuration-agent
...
```

Instead preserve the existing five-box architecture and, where practical, vary the action surface attached
to the existing investigator/rework/reviewer roles.

The small-model benefit comes from **fewer visible choices**, not from multiplying agent identities.

---

# 16. Recommendation 10 — borrow MUSE's structured-experience idea carefully

MUSE is an experience-driven agent framework that converts completed trajectories into structured
experience and reuses that experience in later tasks.

Reference:

- https://github.com/KnowledgeXLab/MUSE

The relevant idea is valuable because the published system demonstrates that structured experience can
improve a comparatively lightweight model rather than relying entirely on a much larger reasoning model.

Chitragupta already has a safer foundation than a generic self-reflecting agent:

```text
ticket
    ->
live evidence
    ->
Qwen proposal
    ->
Jev review
    ->
deterministic gates
    ->
verified resolution
    ->
post-resolution curation
    ->
Solution article / GBrain
```

Do not copy autonomous self-reflection directly.

A Qwen reflection is not a fact.

## Recommended Chitragupta experience object

From a **verified resolved** run, derive:

```text
route
symptom / trigger
strong identifiers
objects that were actually useful
objects/queries that were dead ends
minimal successful evidence path
verified root cause when known
verified resolution
negative applicability conditions
source TicketID
source RunID
supporting ActionIDs
```

Jev can judge whether this resembles:

```text
REUSE_EXISTING
UPDATE_EXISTING
CREATE_CANDIDATE
NONE
```

Deterministic SQL remains the only writer.

This gives future 9B runs the most useful possible prior:

> “Here is the shortest verified evidence path that solved a materially similar incident.”

rather than:

> “Here is a long previous conversation.”

---

# 17. Ideas from external harnesses: adopt / adapt / reject

| Source | Idea | Chitragupta decision |
|---|---|---|
| Codex / OpenAI Agents | harness separated from execution environment | **Already aligned; keep** |
| Codex / OpenAI Agents | deterministic/app-level tool handling | **Already aligned; keep** |
| Codex tool search | deferred discovery of large tool catalogs | **Do not use for current 9B worker; live evidence shows the extra discovery step is harmful** |
| Codex / prompt organization | stable reusable prefix | **Adopt where backend supports it naturally** |
| OpenClaw | context accounting | **Adopt** |
| OpenClaw | tool-result pruning | **Adapt as evidence compaction backed by ActionID/SQL audit** |
| OpenClaw | generic conversation compaction | **Not needed for normal frozen L2 tasks; use only if sessions genuinely become long** |
| OpenClaw | explicit writer/session ownership | **Already mostly covered by RunID, WorkKey, SQL lease and task binding** |
| OpenCode | role-specific permissions | **Adopt conceptually for stage-specific action surfaces** |
| OpenCode | many specialized agents | **Do not copy unless a real role boundary appears** |
| OpenCode | hide unused skills | **Useful where Hermes can do so without profile explosion** |
| MUSE | structured experience accumulation | **Adopt from verified outcomes** |
| MUSE | autonomous self-reflection as memory | **Do not trust directly; gate through evidence/Jev/curation** |

---

# 18. Recommended target card for Qwen 9B

A small-model work card should look closer to this than to a generic agent task.

```text
L2 TASK

RUN
run_id: ...
ticket_id: ...
ticket_no: ...
review_cycle: 0

HARNESS ROUTE
sap_posting
Do not reroute.

EXECUTION MODE
FOCUSED_REASONING

YOUR JOB
Determine whether MaterialDocument exists for ProductionOrder 123456.

ALREADY VERIFIED
1. Production order exists. [Action A101]
2. SAP interface request completed. [Action A102]
3. No posting-error row appears in the bounded supplied evidence. [Action A103]

KNOWLEDGE LEAD
Approved solution S17 suggests checking MaterialDocument after successful interface completion.
This is a lead, not ticket-specific proof.

MISSING MATERIAL FACT
MaterialDocument existence/status.

LEGAL NEXT ACTIONS
- xstudio_sap_api_context
- xstudio_get_run_actions
- xstudio_submit_proposal

MAX ADDITIONAL LIVE READS
1

DO NOT
- reroute the ticket
- rediscover the schema
- use terminal/sqlcmd/pyodbc
- publish or mutate Helpdesk
- call Jev
- call kanban_complete directly

FINISH
Call xstudio_submit_proposal exactly once when the evidence state is clear.
```

This format minimizes branching.

---

# 19. Recommended implementation sequence

These should be implemented in the smallest sufficient steps.

## Phase 1 — remove contradictory choices

### 1. One completion path

Make investigator/rework instructions unambiguously require:

```text
xstudio_submit_proposal
```

Remove normal-worker instructions telling Qwen to directly construct `kanban_complete` metadata.

Keep direct nested completion only as an internal/backward-compatible harness path if runtime compatibility
still requires it; do not advertise it to the 9B worker.

### 2. Remove rerouting from the worker procedure

Replace:

```text
Route the ticket.
```

with:

```text
Use the harness-selected route.
```

### 3. Add the next-action frontier to cards

Use the already-existing execution contract and evidence gap.

No new service or planner.

---

## Phase 2 — reduce action-space size

Only if Hermes supports this without architectural expansion:

- expose a smaller action set for COMPOSE_ONLY;
- expose only route-relevant context helpers for FOCUSED_REASONING;
- keep `xstudio_submit_proposal` always visible;
- keep critical recovery/evidence inspection tools visible where justified.

Do **not** restore deferred `tool_search` for the 9B model as a substitute.

---

## Phase 3 — measure and compact actual model input

Add:

- total rendered input accounting;
- visible-tool count;
- tool-schema contribution;
- skill contribution;
- card contribution;
- compiled-context contribution;
- tool-result contribution.

Then implement deterministic evidence compaction for repeated/older tool results where the full result is
already durably stored by ActionID.

---

## Phase 4 — strengthen experience reuse

Extend the governed post-resolution curation payload with the successful evidence path and negative/dead-end
signals that are useful to future investigation.

Do not add free-form model memory as authority.

---

# 20. What not to do

The following changes are specifically **not recommended** for the current architecture.

## 20.1 Do not give Qwen raw GBrain access

Keep the narrow `l2_recall` interface and harness-owned GBrain retrieval.

The model should not manage the knowledge backend.

## 20.2 Do not make Qwen choose workflow status

Keep status binding deterministic.

## 20.3 Do not expose publishing as a model tool

Proposal and publication should remain separate authorities.

## 20.4 Do not restore arbitrary database transport

No terminal + pyodbc/sqlcmd path for the worker.

## 20.5 Do not create route-specific agent proliferation

The current architecture does not need a new agent type for each plant/problem domain.

## 20.6 Do not make the model review itself

Jev primary review plus exceptional separate local review is preferable.

## 20.7 Do not rely on generic prompt text for safety that can be structural

If a constraint can be implemented in the typed tool/plugin/runtime, implement it there.

## 20.8 Do not add generic long-term conversational memory

The authoritative reusable memory should remain:

- canonical Git knowledge;
- governed GBrain retrieval;
- governed SQL Solution articles;
- run/ticket evidence;
- verified curated experience.

---

# 21. Small-model harness design principles for this project

The following principles summarize the desired direction.

## Principle 1 — deterministic outer loop

The model does not own lifecycle transitions.

## Principle 2 — semantic inner loop

The model handles the irreducibly semantic part: synthesis, bounded reasoning, and user-facing explanation.

## Principle 3 — one decision owner

Routing, completion, publication, schema validation and retry limits must each have one owner.

## Principle 4 — one legal finish action

A small model should not need to choose between equivalent completion APIs.

## Principle 5 — precompute before prompting

If the harness can safely determine route, schema candidates, identifiers, relationships or initial
evidence, do it before the model turn.

## Principle 6 — give evidence references, not giant history

ActionIDs and durable SQL evidence are preferable to replaying old tool output.

## Principle 7 — correct deterministically when possible

Do not spend a model retry on a missing field the harness already knows.

## Principle 8 — narrow uncertainty

FOCUSED_REASONING should name the exact unresolved material fact.

## Principle 9 — knowledge is guidance; live evidence is proof

GBrain/Solution articles help choose what to inspect. They do not replace current ticket-specific
verification.

## Principle 10 — successful experience should shorten future work

A verified previous run should reduce exploration, not merely add more text to context.

---

# 22. Suggested tests for the next harness iteration

No broad new test framework is required.

Add focused tests around the changed contracts.

## Completion contract

Verify:

- investigator instruction exposes `xstudio_submit_proposal` as the only normal completion action;
- a successful submit produces terminal structured metadata;
- the worker is not instructed to call `kanban_complete` directly.

## Route ownership

Verify:

- the card carries the selected route;
- the card explicitly says not to reroute;
- worker skill text no longer asks the model to route independently.

## Next-action frontier

Verify:

- COMPOSE_ONLY presents no unnecessary discovery action;
- FOCUSED_REASONING identifies a bounded unresolved fact;
- read allowance and visible allowed actions agree.

## Context accounting

Verify:

- report includes static/tool/card/compiled-context/tool-result contributions;
- the accounting itself is not inserted back into the model prompt unless specifically useful.

## Evidence compaction

Verify:

- full raw result remains durably accessible by ActionID;
- compact representation preserves material values and provenance;
- reviewer can recover the underlying action if needed.

## Experience reuse

Verify:

- only verified terminal outcomes can create reusable experience;
- every reusable item carries TicketID/RunID/ActionID provenance;
- the next ticket receives applicable evidence-path guidance without treating it as live proof.

---

# 23. How success should be judged

The goal is not “Qwen used fewer tokens” in isolation.

The harness is better if real tickets show:

- fewer tool-selection mistakes;
- fewer malformed completion attempts;
- fewer duplicated route/schema discovery steps;
- fewer repeated reads of already-known evidence;
- fewer generic “database unavailable” false conclusions;
- more first-attempt valid `xstudio_submit_proposal` calls;
- fewer reviewer fallbacks caused only by formatting/harness friction;
- fewer rework cycles caused by missing evidence that the harness could have supplied;
- preserved or improved resolution correctness;
- preserved auditability and deterministic lifecycle safety.

The existing trace and SQL action tables are sufficient to measure most of these.

---

# 24. Final target architecture

No sixth architecture box is required.

The target remains:

```text
XStudio Helpdesk
      |
      v
Chitragupta deterministic control
      |
      +--------------------------+
      |                          |
      v                          v
Jev System One             Evidence / Knowledge
      |                          |
      +------------+-------------+
                   |
             execution contract
                   |
          +--------+---------+
          |                  |
      QWEN_FREE         Qwen System Two
                             |
                      tiny action frontier
                             |
                       frozen proposal
                             |
                       Jev review
                             |
                     deterministic publish
```

The improvement is inside the boundary between the execution contract and Qwen:

```text
CURRENT
execution contract
    + broad instructions
    + several possible tools
    + duplicated route/completion choices
        ->
Qwen

TARGET
execution contract
    + exact route
    + exact unresolved fact
    + smallest legal action frontier
    + compact evidence references
    + one finish action
        ->
Qwen
```

That is the recommended small-model harness direction.

---

# 25. External references

These are design references only. Chitragupta remains governed by its own repository contracts.

## OpenAI / Codex / Agents

- Agents overview: https://developers.openai.com/api/docs/guides/agents
- Agents API architecture: https://developers.openai.com/api/docs/guides/agents-api/architecture
- Tool search: https://developers.openai.com/api/docs/guides/tools-tool-search

Useful ideas:

- harness/environment separation;
- application-owned tool execution;
- explicit context/tool lifecycle;
- stable prompt organization.

Not recommended for the current Qwen worker:

- model-driven deferred tool discovery as the primary way to reach a relatively small known tool surface.

## OpenClaw

- Agent loop: https://github.com/openclaw/openclaw/blob/main/docs/concepts/agent-loop.md
- Context: https://github.com/openclaw/openclaw/blob/main/docs/concepts/context.md
- Compaction: https://github.com/openclaw/openclaw/blob/main/docs/concepts/compaction.md

Useful ideas:

- explicit context accounting;
- separating durable history from active model context;
- pruning old tool results independently from durable transcript/history.

## OpenCode

- Agents: https://github.com/mudrii/opencode-docs/blob/main/docs/official/agents.md
- Skills: https://github.com/mudrii/opencode-docs/blob/main/docs/official/skills.md

Useful ideas:

- role-specific permission surfaces;
- hiding unavailable/unneeded skills and tools;
- keeping capability exposure explicit.

## MUSE

- Repository/paper implementation: https://github.com/KnowledgeXLab/MUSE

Useful idea:

- converting successful task trajectories into structured reusable experience.

Chitragupta adaptation:

- only verified evidence and governed outcomes become reusable experience;
- Qwen self-reflection never becomes authority by itself.

---

# 26. Recommended immediate next work

If this design is accepted, the next implementation should be deliberately small:

1. **Unify completion instructions around `xstudio_submit_proposal`.**
2. **Remove worker-side ticket rerouting.**
3. **Add an explicit next-action frontier to the existing task specification.**
4. **Measure the full rendered model input before deciding whether stage-specific tool hiding is necessary.**
5. **Then add evidence compaction if traces show tool-result carryover remains material.**

Do not implement all external-framework ideas at once.

The harness is already structurally strong. The next gains should come from making the local model's job
smaller, clearer and more deterministic.
