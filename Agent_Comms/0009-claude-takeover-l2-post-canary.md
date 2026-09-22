---
id: 9
type: finding
from: codex
to: claude
created: 2026-09-22T06:51:00+05:30
---

## Finding

This is a **non-normative project handover** for Claude to continue the current Chitragupta L2 work. It is historical/current-state evidence only. Do not treat this file as an architecture specification.

Read the project authority chain first:

```text
AGENTS.md
    -> stable engineering/runtime invariants and Scope Guard
Knowledge/L2_PIPELINE_STATE_MACHINE.md
    -> sole normative architecture/lifecycle specification
runtime code / SQL
    -> implementation
```

Do not use old Plans/, Agent_Comms/, old commit messages, or this handover to override those sources.

### 1. Repository / branch state at handover

Repository:

```text
bhadkamkar9snehil/Chitragupta
```

Active branch:

```text
feature/jev-parallel-pipeline-serialized-qwen
```

Remote HEAD immediately before this handover file is added:

```text
c911784b2ac7cf651e4844c43bc1985c0723ac4d
docs(l2-audit): add post-fix live xstudio_l2 canary evidence
```

Recent lineage:

```text
7e419931  refactor(l2): freeze architecture and remove obsolete lifecycle paths
7b0e9b0f  docs(l2-audit): document live database analysis for Ticket_232 and Ticket_233
4a0d3cfd  fix(l2-tools): enforce xstudio_l2 operation contracts and database guidance
cca83dfc  docs(l2-audit): correct Jev action and database-routing interpretation
c911784b  docs(l2-audit): add post-fix live xstudio_l2 canary evidence
```

After reading this file, fetch the branch again because the handover commit itself will advance HEAD by one commit.

### 2. Architecture is frozen

There are exactly five responsibilities:

```text
1. XStudio Helpdesk
2. Chitragupta deterministic control
3. Jev System One
4. Hermes/Qwen System Two
5. Evidence/Knowledge
```

Do not add:
- a sixth architecture box;
- another lifecycle engine;
- another queue;
- another reviewer path;
- another persistence store;
- a new execution taxonomy;
- compatibility wrappers without a demonstrated caller.

Existing execution depths remain:

```text
QWEN_FREE
COMPOSE_ONLY
FOCUSED_REASONING
```

Existing Jev primary-review outcomes remain:

```text
APPROVE
REWORK
LOCAL_REVIEW
L3_ESCALATION
```

The next task is a narrow quality/reliability follow-up, not architecture work.

### 3. What was actually fixed

The live investigation of Ticket_232 and Ticket_233 found systemic misuse of the single typed `xstudio_l2` tool.

The pre-fix evidence established:

```text
379 actual xstudio_l2 calls
181 successful
170 error
28 blocked
```

Important failure classes included:

```text
73  database missing
12  validate_identifiers missing table
10  suggest_tables missing search
 8  save_ledger missing run_id
 8  get_definition missing object_name
 3  find_objects missing search
 3  select missing table
 3  select missing columns
```

The main root causes were:
1. the model-facing schema published only `operation` as formally required while the bridge had operation-specific required fields;
2. workers frequently looked for production/plant evidence in `XStudio_Helpdesk` instead of `XStudio_Xbatch`.

Commit `4a0d3cfd` hardened the existing single tool rather than creating new tools:
- operation-specific requirements are clearly described at the tool boundary;
- database routing is injected into the tool context;
- bridge-side deterministic validation remains authoritative;
- no hidden default database was added;
- missing `identifiers`, `ticket`, and `parameters` cases were tightened;
- focused regression tests were added;
- the active L2 profiles received concise database-routing guidance.

The intended routing is:

```text
XStudio_Helpdesk
    Helpdesk tickets, Hermes runs, workflow/runtime state

XStudio_Xbatch
    production / plant process evidence:
    heats, EAF, LRF, CCM, billets, work orders, SAP/process evidence

XStudio_Configuration_Xbatch
    XStudio configuration metadata
```

### 4. Jev reporting correction already made

Do not confuse the raw Jev answer stored in `JevReviewDecision` with the effective deterministic action.

Example from Ticket_232:

```text
raw Jev choice = APPROVE
confidence = 0.08 or 0.25
```

Those were **not direct approvals** because deterministic gates require the configured direct-approval confidence threshold (currently 0.82) plus evidence, overclaim, response-fit, deep-reasoning and risk gates.

Those low-confidence raw choices went to `LOCAL_REVIEW`, where a local reviewer independently approved.

Commit `cca83dfc` corrected the audit to make this distinction explicit.

### 5. Live post-fix canary evidence

Commit `c911784b` added the live canary evidence to:

```text
Knowledge/INVESTIGATION_TICKETS_232_233_ANALYSIS.md
```

Key runs:

#### Ticket_241, attempt 2

```text
TicketID = 739D297C-C8D6-470D-BCAC-C18ED64A7312
RunID    = F2DB9885-2943-4E89-ABC9-664FF2FACCA9
```

The investigator immediately queried:

```text
XStudio_Xbatch.dbo.LRF_Per_Heat
HeatID = 1604013
```

and retrieved:

```text
ArcingTime  = 22.0000
PowerONTime = 25.0000
PowerOFFTime = 28.0000
```

The investigator used 2 xstudio_l2 calls with 0 errors. Jev raw review returned REWORK with insufficient confidence for a deterministic direct rework decision, so the runtime used local-review fallback. The local reviewer independently verified live evidence and approved. Deterministic publication finished:

```text
ProcessStatus = COMPLETED
ResponseType  = UPDATE
IsActive      = 0
```

This is the strongest live proof that the main malformed-call/wrong-database defect was materially fixed.

#### Ticket_242, attempt 2

```text
TicketID = E1835201-9F31-473D-9F59-E3CFF1654D28
RunID    = 7698DD3A-02E7-4417-B0F1-16136D5364E0
```

The normal investigator stage correctly targeted `XStudio_Xbatch` and retrieved `dbo.LRF_Per_Heat` evidence for Heat 1604012.

The local reviewer made one wrong-column request (`HeatNo`). The bridge returned a deterministic fuzzy suggestion (`HeatID`), and the reviewer corrected itself immediately. This is productive error recovery, not the old retry loop.

The remaining defect appeared during bounded rework:
- two rework tool attempts omitted `database`;
- the bridge rejected them before SQL execution;
- one rework session reached the 14-call budget.

This is now a **residual rework-context problem**, not the old systemic investigation failure.

### 6. Important audit corrections still required

The current Section 9 in `Knowledge/INVESTIGATION_TICKETS_232_233_ANALYSIS.md` contains several reporting inaccuracies. Correct these before treating the audit as final.

#### A. Tool invocation count is double-counted

The audit says:

```text
Pre-fix xstudio_l2 Tool Invocations = 758
Post-fix = 68
```

The pre-fix investigation already established **379 actual calls**.

The 758 figure comes from counting all trace rows where `ToolName='xstudio_l2'`, which includes both `pre_tool_call` and `post_tool_call`.

For actual invocation counts, count one side only, normally:

```sql
EventType = 'post_tool_call'
AND ToolName = 'xstudio_l2'
```

Recalculate both pre- and post-fix values from SQL before editing the document. Do not assume the post-fix value is exactly half without checking.

#### B. Missing-required-argument subtotal is wrong

The audit says 42 non-database missing-required-argument failures but lists:

```text
table       15
search      13
object_name  8
run_id       8
columns      3
             --
             47
```

Re-query the trace and report the actual counts. Do not preserve the arithmetic error.

If `database` is included in the broader required-argument class, the earlier diagnosis was at least 120 malformed-required-argument events across the listed categories, but the final audit must use fresh SQL-derived totals.

#### C. Routing claim is too absolute

Do not say:

```text
100% of heat/plant evidence queries correctly targeted XStudio_Xbatch
```

without qualification, because two rework attempts omitted `database` entirely.

The accurate formulation is closer to:

```text
All post-fix plant queries that successfully reached SQL used XStudio_Xbatch.
Two bounded-rework tool attempts omitted database and were rejected by the bridge before SQL execution.
```

Use the actual trace evidence.

### 7. Immediate next bounded task

Do **not** start another architecture or global quality pass.

The next task has exactly two parts:

#### Part A — correct the audit numbers

Use direct read-only SQL against `XStudio_Helpdesk`.

Recalculate:
- actual pre-fix xstudio_l2 calls using `post_tool_call` only;
- actual post-fix canary calls using `post_tool_call` only;
- OK/error/blocked totals;
- exact missing-argument categories;
- exact missing-`database` totals;
- exact budget/repeated-failure blocks;
- successful plant calls and their database argument.

Update the existing audit document only. Do not create another audit file.

#### Part B — diagnose the residual rework-only database omission

Start with:

```text
Model_Bench/l2_pipeline_runtime.py
create_rework_card()
```

At current code around the handover point, `create_rework_card()` constructs a rework body containing:

```text
run_id
ticket_id
ticket_no
review_cycle
rework_source_id
prior_investigation_task_id
pipeline_stage
REWORK REASON
PRIOR FINDINGS
```

but it does **not visibly carry an explicit evidence-database target** in that rework body.

Do not assume this is the cause. Prove it.

Compare, for the Ticket_242 residual case:
1. original investigator task body / frozen work package;
2. reviewer task body / frozen proposal;
3. rework task body;
4. `PendingLocalModelJson` for the rework;
5. profile SOUL and `xstudio_l2` pre-LLM injected routing context;
6. trace `ArgsJson` for the two missing-database calls.

Determine whether the target database/evidence context is lost during rework construction or whether it is present and Qwen simply ignored it.

### 8. Fix rule for the residual issue

Only change code if the diagnosis proves a reproducible propagation defect.

If rework construction is dropping an already-known evidence target, make the smallest deterministic carry-forward fix inside the existing rework work package.

Do not:
- silently default missing database to Helpdesk or Xbatch;
- infer databases from arbitrary table-name prefixes;
- add a routing service;
- add a new tool;
- increase the 14-call budget;
- weaken bridge validation;
- change Jev thresholds;
- change queue priorities/WIP;
- create another execution mode.

If the correct database context is already present in the rework package and the model ignored it only twice, document that evidence. The bridge already failed closed correctly; a code change may not be justified.

### 9. Verification standard for any residual fix

Reuse existing tests first:

```bash
python3 Model_Bench/test_xstudio_l2_tools_plugin.py
python3 Model_Bench/test_l2_pipeline_runtime.py
python3 Model_Bench/test_jev_fabric.py
python3 Model_Bench/test_kb_retrieval.py
bash Model_Bench/validate_l2_pipeline_local.sh --fast
```

If deployment-facing files change:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
bash Model_Bench/validate_l2_pipeline_local.sh --live-only
```

Use one bounded rework canary only if an existing safe path exists. Do not invent a new test-ticket or database script.

Success for the residual issue means:

```text
rework receives the same relevant database/evidence target as the verified prior investigation
missing database errors in the tested rework path = 0
no malformed retry loop
no rework budget exhaustion caused by omitted database
bridge validation remains fail-closed
```

### 10. Key files for Claude

Read these before changing code:

```text
AGENTS.md
Knowledge/L2_PIPELINE_STATE_MACHINE.md
Knowledge/INVESTIGATION_TICKETS_232_233_ANALYSIS.md

Model_Bench/l2_pipeline_runtime.py
Model_Bench/xstudio_l2_tools_plugin/__init__.py
Model_Bench/xstudio_l2_tool_bridge.py
Model_Bench/test_xstudio_l2_tools_plugin.py
Model_Bench/test_l2_pipeline_runtime.py

deploy/profiles/l2-jev-investigator/SOUL.md
deploy/profiles/l2-investigator-primary/SOUL.md
deploy/profiles/l2-investigator/SOUL.md
deploy/profiles/l2-reviewer-primary/SOUL.md
deploy/profiles/l2-reviewer-fallback/SOUL.md
```

Use existing deployment/validation scripts. Do not create replacements.

### 11. Current judgment

The original defect is no longer systemic.

Current evidence supports:

```text
Main xstudio_l2 contract hardening:       effective live
Normal investigator routing:              fixed in canaries
Normal local-review routing:              materially fixed
Plant evidence retrieval:                 working
Bridge fail-closed behavior:              working
Repeated-failure breaker:                 working
Architecture changes required:            none

Residual:
rework can still emit database-less calls
one rework session still hit tool budget
audit metrics need correction
```

The next engineer should finish those bounded items and stop. Do not restart architecture work.
