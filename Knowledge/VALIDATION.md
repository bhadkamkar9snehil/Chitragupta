# Hermes L2 Validation Guide

This file is a validation procedure, not a permanent PASS certificate. Runtime, model, workflow, and live SQL state can change after any commit.

## Local validation authority

Run from the checked-out repository in the real Windows/WSL/Hermes environment:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

That script performs:

- Python syntax checks for current lifecycle/tooling files;
- deterministic lifecycle contract tests;
- typed `xstudio_l2` contract tests;
- knowledge manifest/retrieval checks;
- read-only workflow discovery;
- read-only pipeline status;
- reconcile dry-run.

Do not treat a GitHub Actions result as the production validation authority for this project.

## SQL deployment validation

`Knowledge/00_Hermes_L2_FULL_INSTALL.sql` is the generated complete bundle and already contains the current ticket-dispatch and UPDATE-continuation hardening sources.

After deploying the generated bundle, run:

```text
Knowledge/98_pipeline_postflight.sql
```

Then check:

```bash
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

Expected contract:

```text
max_pipeline_wip = 1
review priority = 30
rework priority = 20
new investigation priority = 10
max_review_cycles = 3
workflow binding ready = true
```

No unexplained active SQL run should exist without corresponding Kanban lifecycle state.

## Architecture regression checks

Current operational instructions must continue to describe:

```text
claim one ticket
-> investigator
-> normalize
-> deferred reviewer with frozen proposal_json
-> approve/publish OR reject/rework
-> normalize
-> fresh reviewer
```

The following are retired and must not reappear as current instructions or runtime dependencies:

- separate `l2-review` board;
- `kanban_forward_bridge.py`;
- parent-gated/pre-created reviewer cards;
- backlog `< 3` claim admission;
- SQL `AttemptNo` as the review counter;
- model-based verifier profile names;
- investigator-driven draft/approve/reject publication choreography.

## Typed-tool regression check

For a naturally arriving fresh ticket, inspect the worker trace. Database/schema/ticket evidence should use `xstudio_l2`.

A production worker should not attempt terminal execution of:

```text
Hermes_Orchestrator.py
Windows Python as a database bridge
sqlcmd
pyodbc import/installation
pip/uv/conda/apt package installation for SQL transport
```

Those are harness concerns, not model decisions.

## Knowledge routing regression set

The canonical routes remain:

```text
helpdesk_ticket
sap_posting
api_transaction
work_order
heat_execution
billet_inventory
quality
performance
hermes_runtime
discover
```

Run:

```bash
python3 Model_Bench/validate_knowledge_manifest.py
python3 Model_Bench/test_kb_retrieval.py
```

Ticket-specific conclusions still require live evidence; routing-test success does not prove a production diagnosis.
