---
type: "Playbook"
title: "Deploy Chitragupta L2"
description: "Current deployment sequence for the Helpdesk SQL runtime and Hermes L2 domain layer."
status: current
verified: "2026-09-07"
---

# Deploy Chitragupta L2

## 1. SQL runtime

Target database: `XStudio_Helpdesk`.

Deploy the generated complete bundle:

```text
Knowledge/00_Hermes_L2_FULL_INSTALL.sql
```

The numbered SQL files are maintainable source. Do not separately re-apply numbered hardening files already included in the generated bundle.

Then run:

```text
Knowledge/98_pipeline_postflight.sql
```

## 2. Helpdesk workflow binding

Discover the real live workflow rather than guessing status names:

```bash
python Model_Bench/configure_helpdesk_workflow.py
```

Canonical deployment binding:

```text
deploy/helpdesk_workflow_binding.json
```

Current observed values:

```text
eligible ticket status:       Enter
resolved ticket status:       Closed
waiting-user AskStatus:       Ask
waiting-user ticket status:   unbound
L3 ticket status:             unbound
needs-human-action status:    unbound
```

`RESOLUTION` fails closed if the resolved status is not bound.

## 3. Hermes/GBrain prerequisites

Hermes runs in WSL2. The shared organizational GBrain is already installed separately at:

```text
~/.hermes/xstudio-gbrain
```

GBrain is connected through native Hermes MCP. Chitragupta does not deploy a GBrain wrapper, synchronizer or maintenance daemon.

## 4. Deploy L2

From the repository under WSL2:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

The deploy installs only:

- the central deterministic lifecycle runtime;
- reviewed-outcome materialization;
- current workflow binding;
- the `xstudio-l2-tools` plugin on investigator/reviewer worker profiles;
- the three current profile configs and SOULs.

It also removes known retired GBrain wrappers, procedural skills, duplicate plugins and the retired reviewer-fallback profile from the live Hermes profile directories.

There is no event-reconciler plugin and no separate publisher/reject/repair/audit job.

## 5. Current lifecycle

```text
2-minute scout
  -> reconcile existing work
  -> active SQL run?
       yes -> claim nothing
       no  -> claim one eligible ticket
             -> investigator [10]
             -> normalize structured completion
             -> reviewer [30] with frozen proposal_json
                  -> approve -> deterministic publish
                  -> reject  -> rework [20] -> fresh reviewer
             -> cycle cap -> L3/human escalation path
  -> best-effort reviewed-outcome materialization
```

Reviewer cards are created only after the investigator/rework completion is structurally reviewable.

## 6. Validate

Run:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Validation checks:

- Python/shell syntax;
- focused lifecycle/tool/outcome/Solution tests;
- governed Solution policy dry-run;
- outcome materialization dry-run;
- GBrain health/source state;
- native Hermes→GBrain MCP connectivity;
- absence of retired compatibility artifacts;
- live read-only workflow discovery, status and reconcile dry-run.

For a real ticket, verify the worker actually receives and calls `xstudio_l2` and native GBrain MCP as appropriate.

## 7. Runtime authority

Workers do not mutate the visible Helpdesk ticket directly.

The deterministic lifecycle owns claim, recovery, publish and workflow transitions. The investigator and reviewer only produce/verify structured evidence-backed proposals.
