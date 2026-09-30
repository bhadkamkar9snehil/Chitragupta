# After any `hermes update` (or a fresh install on new infra)

Things in this repo that live partly or entirely inside Hermes's own install
(`~/.hermes/...`) and do NOT survive an update/reinstall on their own.
Run these, in order, after any `hermes update` or when standing this up on
new infra.

## 1. Re-deploy the deterministic L2 pipeline runtime

Run this after every update that touched profile/plugin/script directories,
and on every fresh install:

```bash
bash Model_Bench/deploy_l2_pipeline_runtime.sh
```

This copies the centralized lifecycle runtime and compatibility entrypoints
into the live Hermes script directory, deploys the current event plugin,
and refreshes the investigator/reviewer skills.

The runtime contract is:

```text
global active SQL WIP = 1
review priority        = 30
rework priority        = 20
new investigation     = 10
max review cycles      = 3
```

The event plugin is only an accelerator. `ticket_scout.py` runs the same
reconciler before every new claim, so the 2-minute scout is the durable
backstop if a hook event is missed.

## 2. Verify the Helpdesk workflow binding

The model does not choose Helpdesk status names.

Inspect the current live workflow:

```bash
python3 Model_Bench/configure_helpdesk_workflow.py
```

Then verify `deploy/helpdesk_workflow_binding.json` contains the exact live
values, especially `resolved_ticket_status`.

`RESOLUTION` intentionally fails closed while that value is null. Do not
work around this by enabling model-provided status overrides or guessing a
status such as `Closed`/`Resolved`.

## 3. Re-deploy the SQL layer + hardening overlays

Deploy:

```text
Knowledge/00_Hermes_L2_FULL_INSTALL.sql
Knowledge/25_ticket_dispatch_hardening.sql
Knowledge/55_update_retry_hardening.sql
Knowledge/99_postflight.sql
Knowledge/98_pipeline_postflight.sql
```

The two hardening overlays are required:

- `25_ticket_dispatch_hardening.sql` filters customization requests before
  candidate `TOP`, so valid L2 incidents cannot be hidden behind the first
  20 non-L2 rows.
- `55_update_retry_hardening.sql` gives `UPDATE` a default bounded
  continuation time instead of allowing an UPDATE with `NextEligibleOn=NULL`
  to disappear from the queue forever.

All are idempotent deployment units.

## 4. Re-deploy remaining SOUL.md / plugins if needed

For any profile-specific artifacts not covered by the pipeline deploy script,
copy `deploy/profiles/<profile>/SOUL.md`, remaining `deploy/skills/xstudio/*`
skills, and relevant plugin code into the corresponding
`~/.hermes/profiles/<profile>/...` paths. Restart the affected gateway after
plugin/config changes.

## 5. Re-create cron jobs if the scheduler was rebuilt

`deploy/cron_jobs.txt` is the reference schedule snapshot. The important
correctness point is that the existing Ticket Scout job remains active: it
now reconciles approvals/rejections/repair before it attempts any claim, so
separate publisher/reject polling jobs are no longer required for delivery
correctness.

## 6. Local validation before normal ticket flow

Do not use a GitHub Action as a substitute for this environment-specific
validation. Run it on the real WSL/Hermes/SQL/LM Studio machine:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```

Then run:

```bash
python3 ~/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py status
```

Investigate every reported anomaly before enabling normal ticket claiming.
In particular, there should be no unexplained:

```text
ACTIVE_SQL_WITH_NO_KANBAN
DONE_INVESTIGATION_WITHOUT_REVIEWER
```

## Ongoing self-healing

Ticket lifecycle correctness is protected
separately by deterministic reconciliation on every scout tick and on every
Kanban complete/block event.
