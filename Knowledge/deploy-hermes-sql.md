---
type: "Playbook"
title: "Deploy the L2 SQL Runtime and Engine"
description: "Deployment sequence for the Helpdesk SQL runtime, the engine service and the deterministic L2 lifecycle."
tags:
  - engine
  - deployment
  - sql
status: current
verified: "2026-09-05"
---

# Deploy the L2 SQL Runtime and Engine

Target database:

```text
XStudio_Helpdesk
```

## 1. Deploy the generated complete SQL bundle

Run:

```text
Knowledge/00_Hermes_L2_FULL_INSTALL.sql
```

The numbered SQL files are the maintainable sources. The generated full-install bundle already includes the current hardening sources, including:

```text
Knowledge/25_ticket_dispatch_hardening.sql
Knowledge/55_update_retry_hardening.sql
```

Do **not** apply those two again merely because they exist as source files. When SQL runtime logic changes:

```text
edit the numbered source
-> regenerate 00_Hermes_L2_FULL_INSTALL.sql
-> deploy the generated bundle
```

Apply a separate overlay only when it is intentionally not yet part of the generated bundle.

## 2. Discover and bind the live Helpdesk workflow

Run the read-only discovery helper:

```bash
python Model_Bench/configure_helpdesk_workflow.py
```

Underlying SQL discovery:

```sql
EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;
```

The current checked-in deployment binding is:

```text
eligible ticket status:       Enter
resolved ticket status:       Closed
waiting-user AskStatus:       Ask
waiting-user ticket status:   unbound
L3 ticket status:             unbound
needs-human-action status:    unbound
```

Canonical file:

```text
deploy/helpdesk_workflow_binding.json
```

If live workflow values change, update the binding only from observed live values. Do not guess replacements.

`RESOLUTION` publication fails closed when `resolved_ticket_status` is not configured.

## 3. Run SQL postflight

Run:

```text
Knowledge/98_pipeline_postflight.sql
```

Then verify the pipeline from the staged engine:

```powershell
build\stage\engine\python\python.exe build\stage\engine\app\Model_Bench\l2_pipeline_runtime.py status
```

Expected lifecycle contract:

```text
max_pipeline_wip = 8
max_qwen_running = 1
max_qwen_waiting = 4
review priority = 30
rework priority = 20
new investigation priority = 10
max_review_cycles = 3
execution_modes = QWEN_FREE, COMPOSE_ONLY, FOCUSED_REASONING
```

No unexplained `ACTIVE_SQL_WITH_NO_KANBAN` anomaly should remain.

## 4. Build and run the engine

```powershell
build\build.ps1          # stages API + console, embedded Python, app code, prompts, skills, plugins, WinSW, gbrain.exe
build\dev-start.ps1      # run from build\stage (or install Chitragupta-Setup.exe on a server)
```

The payload contains:

- the central lifecycle runtime, the engine (`engine.py`), the worker (`agent_loop.py`) and the SQL card board (`cards.py`);
- the typed `xstudio_l2` investigation plugin and bridge, and the trace plugin;
- the investigator/reviewer prompts (`deploy/profiles/*/SOUL.md`), skills and `deploy/engine.json`;
- the workflow-binding fallback;
- the prebuilt GBrain index (`build\build-brain.ps1`).

Connections (SQL, LM Studio, Jev, GBrain) are entered afterwards in the console under Settings, which writes `chitragupta.json`. The card tables are created on first use. The engine runs the staged copy, so a code change is live only after `build\build.ps1` and an engine restart.

## 5. Current lifecycle

```text
ticket_scout tick (every 2 minutes)
  -> reconcile all in-flight work
  -> active SQL runs < max_pipeline_wip (8) AND queued < max_qwen_waiting (4)?
       no  -> WIP_LIMIT / BACKPRESSURE; claim nothing
       yes -> claim candidate tickets up to capacity
              -> Jev triage + candidate retrieval + evidence plan
              -> deterministic bounded probes
              -> Jev investigation assessment + meta-attention scoring
                   -> QWEN_FREE -> Jev primary review -> deterministic publish
                   -> COMPOSE_ONLY / FOCUSED_REASONING -> queued in SQL
                        -> serialized single-slot admission to local model (Qwen)
                        -> investigator [10] (xstudio_l2 typed tool only)
                        -> normalize structured completion into frozen proposal
                        -> Jev primary review
                             -> APPROVE -> deterministic publish
                             -> REWORK [20] -> rework investigator -> fresh Jev review
                             -> L3_ESCALATION -> deterministic escalation
                             -> LOCAL_REVIEW -> reviewer [30] (Qwen fallback)
                                  -> approve -> deterministic publish
                                  -> reject  -> rework investigator [20]
```

Reviewer cards are created only when Jev primary review selects `LOCAL_REVIEW` fallback, is unavailable, or fails deterministic confidence/safety gates.

The 2-minute scout is the durable correctness backstop. Event hooks call the same reconciler for low-latency handoff but are not required for correctness.

See `Knowledge/L2_PIPELINE_STATE_MACHINE.md` for the normative lifecycle.

## 6. Local validation

Run:

```powershell
python -m unittest -v Model_Bench/test_l2_pipeline_runtime.py
npm --prefix l1-ui run check
```

This is the project validation authority before deployment. Do not substitute a GitHub Actions result for inspection of the real local Windows engine, SQL Server and LM Studio environment.

For the next naturally arriving ticket, confirm its trace uses `xstudio_l2` for database/schema work and does not attempt to recreate Python/pyodbc/sqlcmd transport.

## 7. Service identity and permissions

Use the real XStudio service identity where the audited SQL runtime accepts a user ID.

The SQL login must have only the operational permissions required by the deterministic runtime across the relevant XStudio databases.

Investigators and reviewers do not directly update `Complaint_Mst_Tbl`; approved ticket publication goes through the audited deterministic path.
