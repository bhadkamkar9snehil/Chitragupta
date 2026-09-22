# Deterministic Observability Writes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Persist idempotent, IST-explicit, Kanban-correlated L2 traces and expose honest existing compute projections.

**Architecture:** The observer hook retains the JSONL outbox. It stamps a UUID and IST timestamp before append; the existing drain sends these to the audited trace procedure. A single `trace_context` event, obtained exclusively through `hermes kanban show <task-id> --json`, maps early events without another table or service.

**Tech Stack:** Python 3 standard library, Hermes Kanban CLI, SQL Server T-SQL, existing L2 deploy scripts.

**Spec:** `docs/superpowers/specs/2026-09-18-l2-deterministic-observability-design.md`

## Global Constraints

- All new timestamps are IST (`Asia/Kolkata`, `+05:30`); do not add UTC fields or views.
- Retain the trace table, JSONL outbox, audited stored procedure, drain, and two compute views.
- Do not mutate `Complaint_Mst_Tbl`, add a monitoring job, use model SQL transport, or convert historical rows.
- Edit numbered SQL sources, then regenerate `Knowledge/00_Hermes_L2_FULL_INSTALL.sql`.

---

### Task 1: Stable IST trace events and Kanban context

**Files:**
- Modify: `Model_Bench/xstudio_l2_trace_plugin/__init__.py`
- Test: `Model_Bench/test_l2_trace_plugin.py`

**Interfaces:**
- Produces: `trace_event_id`, `event_on_ist`, and exactly one `trace_context` event per resolved/failed Kanban task.
- Consumes: existing `_write_event`, `_resolve_task_ids_blocking`, and `hermes kanban show <task-id> --json`.

- [ ] **Step 1: Write failing tests**

```python
def test_write_event_stamps_uuid_and_ist_offset(self):
    plugin._write_event({"event_type": "pre_tool_call"})
    event = json.loads(events_file.read_text())
    self.assertRegex(event["trace_event_id"], r"^[0-9a-f-]{36}$")
    self.assertTrue(event["event_on_ist"].endswith("+05:30"))

def test_task_lookup_writes_one_context_event(self):
    # Mock Kanban JSON with run_id/ticket_id; assert trace_context/status=resolved.
```

- [ ] **Step 2: Run the focused tests**

Run: `python Model_Bench/test_l2_trace_plugin.py`

Expected: new UUID/IST/context assertions fail.

- [ ] **Step 3: Add only the outbox fields and context row**

```python
from datetime import datetime
from zoneinfo import ZoneInfo
from uuid import uuid4

IST = ZoneInfo("Asia/Kolkata")
event.setdefault("trace_event_id", str(uuid4()))
event.setdefault("event_on_ist", datetime.now(IST).isoformat(timespec="milliseconds"))
```

After the existing asynchronous lookup completes, append one `trace_context` event: `status="resolved"` with real IDs, otherwise `status="failed"` and no inferred IDs. Guard once-per-task emission with the existing cache lock; never block hook callbacks.

- [ ] **Step 4: Re-run focused tests**

Run: `python Model_Bench/test_l2_trace_plugin.py`

Expected: all trace-plugin tests pass.

- [ ] **Step 5: Commit**

Run: `git add Model_Bench/xstudio_l2_trace_plugin/__init__.py Model_Bench/test_l2_trace_plugin.py && git commit -m "fix(l2): stamp idempotent IST trace events"`

### Task 2: Idempotent SQL trace sink

**Files:**
- Modify: `Knowledge/00_tables_and_indexes.sql`
- Modify: `Knowledge/50_response_and_workflow.sql`
- Modify: `Model_Bench/drain_l2_trace_log.py`
- Test: `Model_Bench/test_l2_trace_plugin.py`

**Interfaces:**
- Consumes: `trace_event_id` and `event_on_ist` from Task 1.
- Produces: `Hermes_Log_Agent_Trace_Usp` accepts the identity/time pair and persists a row once.

- [ ] **Step 1: Write a failing drain-parameter test**

```python
event = {"trace_event_id": "00000000-0000-0000-0000-000000000001",
         "event_on_ist": "2026-09-18T12:00:00.000+05:30"}
params = drain.trace_procedure_parameters(event)
self.assertEqual(event["trace_event_id"], params[0])
self.assertEqual("+05:30", params[1].isoformat()[-6:])
```

- [ ] **Step 2: Run the focused test**

Run: `python Model_Bench/test_l2_trace_plugin.py`

Expected: it fails because the helper and procedure arguments do not exist.

- [ ] **Step 3: Implement the minimal upgrade**

Add nullable `TraceEventID varchar(36)`, `EventOnIst datetimeoffset(3)`, and `IngestedOnIst datetimeoffset(3)` to new-table DDL and `IF COL_LENGTH` upgrade guards. Add a filtered unique index on non-null `TraceEventID`. Extend the audited procedure and drain with these fields. Insert only if the event ID is absent; set `IngestedOnIst` using `SYSDATETIMEOFFSET() AT TIME ZONE 'India Standard Time'`. Pass legacy `EventOn` an IST wall-clock time.

- [ ] **Step 4: Validate sink source and tests**

Run: `python Model_Bench/test_l2_trace_plugin.py`

Run: `rg -n "TraceEventID|EventOnIst|IngestedOnIst|India Standard Time" Knowledge/00_tables_and_indexes.sql Knowledge/50_response_and_workflow.sql Model_Bench/drain_l2_trace_log.py`

Expected: tests pass and creation, upgrade, procedure, and drain paths all contain the contract.

- [ ] **Step 5: Commit**

Run: `git add Knowledge/00_tables_and_indexes.sql Knowledge/50_response_and_workflow.sql Model_Bench/drain_l2_trace_log.py Model_Bench/test_l2_trace_plugin.py && git commit -m "fix(l2): make trace sink idempotent and IST-aware"`

### Task 3: Existing compute metrics and one run projection

**Files:**
- Modify: `Knowledge/60_metrics_and_reporting.sql`
- Test: `Model_Bench/test_helpdesk_sql_contract.py`

**Interfaces:**
- Consumes: trace rows and `trace_context` mappings by `TaskID`.
- Produces: extended two existing compute views and `Hermes_L2_Run_Observability_Vw` with `OBSERVED`, `PENDING`, or `GAP`.

- [ ] **Step 1: Write a failing SQL contract test**

```python
sql = Path("Knowledge/60_metrics_and_reporting.sql").read_text(encoding="utf-8")
for token in ("ToolErrorCount", "BlockedToolCallCount", "FirstEventOnIst",
              "Hermes_L2_Run_Observability_Vw", "OBSERVED", "PENDING", "GAP"):
    self.assertIn(token, sql)
```

- [ ] **Step 2: Run the SQL contract test**

Run: `python Model_Bench/test_helpdesk_sql_contract.py`

Expected: it fails because the required metrics/view are absent.

- [ ] **Step 3: Implement normalized views without a table**

Within each existing compute view, coalesce direct IDs with a resolved `trace_context` mapping by `TaskID`. Exclude `trace_context` rows from all event/tool/API/token/duration metrics. Add success/error/blocked/correlation counters and IST first/last/ingested times. Create only `Hermes_L2_Run_Observability_Vw`: active no trace is `PENDING`; terminal missing valid context or with failed context is `GAP`; otherwise `OBSERVED`.

- [ ] **Step 4: Re-run tests and regenerate the bundle**

Run: `python Model_Bench/test_helpdesk_sql_contract.py`

Run: `python Model_Bench/test_l2_trace_plugin.py`

Expected: both pass before regenerating `Knowledge/00_Hermes_L2_FULL_INSTALL.sql` from numbered sources.

- [ ] **Step 5: Commit**

Run: `git add Knowledge/60_metrics_and_reporting.sql Knowledge/00_Hermes_L2_FULL_INSTALL.sql Model_Bench/test_helpdesk_sql_contract.py && git commit -m "feat(l2): expose deterministic trace observability"`

### Task 4: Deploy and live-verify

**Files:**
- Verify: `Model_Bench/validate_l2_pipeline_local.sh`
- Verify: `Knowledge/98_pipeline_postflight.sql`

**Interfaces:**
- Consumes: the deployed trace schema, procedure, plugin, drain, and views.
- Produces: read-only evidence of the contract without manufacturing a production claim.

- [ ] **Step 1: Run local validation**

Run: `bash Model_Bench/validate_l2_pipeline_local.sh`

Expected: syntax, lifecycle, typed-tool, and knowledge checks pass.

- [ ] **Step 2: Deploy existing runtime artifacts and the generated bundle**

Run: `bash Model_Bench/deploy_l2_pipeline_runtime.sh`

Run: `python Model_Bench/deploy_sql_file.py Knowledge/00_Hermes_L2_FULL_INSTALL.sql`

Expected: the existing deployer updates active profiles; the existing SQL deployer applies the regenerated bundle.

- [ ] **Step 3: Run postflight and read-only live checks**

Run: `python Model_Bench/deploy_sql_file.py Knowledge/98_pipeline_postflight.sql`

Query the live table/index/views for the three IST columns, unique event key, extended metrics, and run-observability status.

Expected: live schema matches the source contract; do not claim a fresh ticket.

- [ ] **Step 4: Final integrity check**

Run: `git diff --check && git status --short`

Expected: only intentional source/mirror changes remain; report test, deploy, and live evidence separately.
