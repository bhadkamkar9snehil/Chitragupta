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
| L3-002 | Done | Lifecycle | Prevent reviewer rework blocks from opening L3 escalations. | Runtime fix in `025be8c`; legacy SP now fails closed unless a terminal L3 outcome exists. |
| KB-001 | Done | Knowledge | Make committed GBrain knowledge complete, bounded, provenance-rich, and automatic in initial L2 context. | Live validated 2026-09-08: 100% embeddings, 10/10 retrieval cases, bundle/deploy/runtime gates; `31c271d..a49eb45`. |
| KB-002 | Done | Knowledge | Expand the fixed XBatch table/view relationship atlas without creating a second registry. | `ced5998`: 534 configured rows, 530 semantic edges, object-addressable bounded GBrain pages; 12/12 live retrieval cases. |
| KB-003 | Done | Knowledge | Add deterministic domain investigation recipes and reviewer evidence context on top of the verified GBrain interface. | `f1c848a..544d7e9`: 10/10 routes have recipes; dispatch context and reviewer evidence matrix deployed. |
| KB-004 | Open | Reliability | Probe live query-embedding health before new claims and never run embedding backfill while L2 model work is active. | Add a cheap semantic canary, maintenance/WIP interlock, and timeout telemetry. |
| KPI-002 | Open | Measurement | Establish a post-GBrain ticket benchmark for retrieval latency, tokens, tool errors, review cycles, and resolution outcome. | Measure naturally arriving tickets against the existing SQL/trace baseline. |
| REPLY-001 | Open | Requester safety | Trace where the published requester reply comes from on terminal L3 escalations. Ticket #35 (2026-09-26) shows internal text as "What the requester was told": "Automated L2 did not reach an evidence-supported conclusion within its bounded review/rework budget (3 cycles)… Proposal claim contradicts live evidence…"; the activity feed shows similar "Investigation Status: L3 Escalation Required" notes. | Confirm whether that text reached the Helpdesk reply; if so, route max-cycle escalations through the fixed requester-facing reply, keeping the review notes internal. |
| KPI-001 | Good-to-have | Reporting | Add a concise Helpdesk-facing L2 operations scorecard using existing metric views. | Agree audience and KPI definitions. |

## Maintenance rule

- Add a row when a concrete follow-up emerges.
- Keep wording short; link to a ticket or commit only when useful.
- Set `Done` with the validating commit/result; remove obsolete rows only when their history has no value.
