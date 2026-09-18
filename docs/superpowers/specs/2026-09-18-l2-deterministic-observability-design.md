# Deterministic L2 observability writes

## Objective

Make every L2 trace, compute, and lifecycle-observability record durable,
idempotent, correlated to its ticket/run, and expressed in India Standard Time
(IST). The system must never emit or expose UTC timestamps.

## Scope

The change covers the observer-hook outbox, its SQL drain, the audited trace
stored procedure/table, and the read-only compute and lifecycle-observability
views. It does not mutate Helpdesk tickets, responses, or historical trace
rows.

## Write contract

Each newly emitted trace event has:

- `TraceEventID`: UUID created once before its JSONL line is appended. It is
  persisted through retries and is unique in SQL.
- `EventOnIst`: the source event time as `datetimeoffset(3)` in IST, carrying
  the `+05:30` offset rather than an unlabelled wall-clock value.
- `IngestedOnIst`: the SQL ingestion time as `datetimeoffset(3)` in IST.
- `TaskID`, and a run/ticket identity either on the event itself or in a
  durable `trace_context` event for that task.

The drain calls the audited SQL procedure. The procedure performs an
idempotent insert keyed by `TraceEventID`; retries after a process crash or
cursor-save failure do not create another trace row. A filtered unique index
preserves historical rows that have no event ID.

The hook remains non-blocking. It continues to write early events immediately,
then emits exactly one `trace_context` row after its background
`hermes kanban show <task-id> --json` lookup finishes. A resolved context row
maps `TaskID` to `RunID`/`TicketID`; a failed context row records a failed
status with no inferred IDs. Projection views use this one existing-table
mapping to correlate early rows. They never silently treat a missing mapping
as successful coverage.

## Time contract

All new source times are generated with `Asia/Kolkata`; SQL stores and exposes
them as `datetimeoffset(3)` at `+05:30`. Existing `EventOn` is retained only
for compatibility and is written in IST wall-clock time for every new row.
New views use `EventOnIst`/`IngestedOnIst` and name their output `...Ist`.
Existing historical values are left unchanged and are not relabelled as IST
evidence.

## Read contract

`Hermes_L2_Compute_Per_Ticket_Vw` and
`Hermes_L2_Compute_Per_Profile_Vw` retain their existing metrics and add:

- `ToolSuccessCount`, `ToolErrorCount`, `BlockedToolCallCount`;
- `CorrelationFailureCount` and `UncorrelatedEventCount`;
- `FirstEventOnIst`, `LastEventOnIst`, `IngestedFirstOnIst`,
  `IngestedLastOnIst`, and IST wall-clock duration.

`trace_context` rows establish correlation but are excluded from all tool,
API, token, duration, and event-count metrics.

One new read-only run-observability view joins L2 responses to the normalized
trace projection and reports one of:

- `OBSERVED`: correlated trace exists for the run;
- `PENDING`: the run remains active and has no correlated trace yet;
- `GAP`: the run is terminal but lacks a valid task-context mapping or has a
  failed context row.

Tool failures and blocked calls remain distinct from model/API failures. A
published lifecycle result is not treated as proof that its tool execution was
error-free.

## Deployment and verification

Edit the numbered SQL sources (`00_tables_and_indexes.sql`,
`50_response_and_workflow.sql`, `60_metrics_and_reporting.sql`) and regenerate
`00_Hermes_L2_FULL_INSTALL.sql`. Update the trace plugin, drainer, and their
existing tests. Deploy through the existing L2 deployer and verify the live
schema, idempotent duplicate handling, task-context correlation of early
events, IST-only projections, and lifecycle-observability status without
manually claiming a production ticket.

## Non-goals

- No direct writes to `Complaint_Mst_Tbl`.
- No model-controlled SQL transport.
- No separate monitoring job or second lifecycle authority.
- No historical timestamp conversion or speculative repair of old tickets.
