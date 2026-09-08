# Pending Points Register

Concise parking lot for follow-ups, work in progress, and good-to-have ideas.
This is not lifecycle authority, a deployment plan, or a ticket queue.

| ID | Status | Type | Point | Next condition |
|---|---|---|---|---|
| OBS-001 | Open | Reliability | Alert when trace drain fails, cursor stalls, or buffered-event backlog exceeds a limit. | Define owner and notification route. |
| OBS-002 | Good-to-have | Reliability | Quarantine malformed trace JSON instead of skipping it silently. | Preserve bad line and emit a health record. |
| OBS-003 | Done | Reliability | Flush trace and readable Helpdesk activity from the two-minute scout. | Implemented in `f93daa1`; keep live-checking backlog. |
| OBS-004 | Done | KPI integrity | Attribute hardware samples to the investigator/reviewer profile. | Implemented in `f93daa1`; historical `unknown` rows remain. |
| L3-001 | Open | Workflow | Bind a verified visible Helpdesk status for L3 / human action. | Demonstrate one unambiguous live workflow status; do not guess. |
| L3-002 | Done | Lifecycle | Prevent reviewer rework blocks from opening L3 escalations. | Implemented in `025be8c`; retain regression test. |
| KPI-001 | Good-to-have | Reporting | Add a concise Helpdesk-facing L2 operations scorecard using existing metric views. | Agree audience and KPI definitions. |

## Maintenance rule

- Add a row when a concrete follow-up emerges.
- Keep wording short; link to a ticket or commit only when useful.
- Set `Done` with the validating commit/result; remove obsolete rows only when their history has no value.
