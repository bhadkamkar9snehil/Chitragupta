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
- `EventOnIst`: the source event time in IST, emitted as an ISO-8601 value with
  the `+05:30` offset and stored as IST wall-clock time in SQL.
- `IngestedOnIst`: the SQL ingestion time in IST.
- `TaskID`, and a run/ticket identity either on the event itself or in a
  durable `trace_context` event for that task.

The drain calls the audited SQL procedure. The procedure performs an
idempotent insert keyed by `TraceEventID`; retries after a process crash or
cursor-save failure do not create another trace row. A filtered unique index
preserves historical rows that have no event ID.

The hook remains non-blocking. It continues to write early events immediately,
then emits exactly one `trace_context` event after its background Kanban lookup
resolves the task to `RunID` and `TicketID`. Projection views use that context
to correlate the early rows. If the Kanban lookup cannot resolve, the hook
emits an explicit `trace_correlation_failed` record rather than making the
coverage gap silent.

## Time contract

All new source times are generated with `Asia/Kolkata`; SQL defaults use
`SYSDATETIMEOFFSET() AT TIME ZONE 'India Standard Time'` and expose IST wall
clock values. Existing `EventOn` is retained for compatibility but is written
in IST for every new row. New views use `EventOnIst`/`IngestedOnIst` and name
their output `...Ist`. Existing historical values are left unchanged and are
not relabelled as IST evidence.

## Read contract

`Hermes_L2_Compute_Per_Ticket_Vw` and
`Hermes_L2_Compute_Per_Profile_Vw` retain their existing metrics and add:

- `ToolSuccessCount`, `ToolErrorCount`, `BlockedToolCallCount`;
- `CorrelationFailureCount` and `UncorrelatedEventCount`;
- `FirstEventOnIst`, `LastEventOnIst`, `IngestedFirstOnIst`,
  `IngestedLastOnIst`, and IST wall-clock duration.

A new read-only run-observability view joins L2 responses to the normalized
trace projection and reports one of:

- `OBSERVED`: correlated trace exists for the run;
- `PENDING`: the run remains active and has no correlated trace yet;
- `GAP`: the run is terminal but lacks correlated trace, or has an explicit
  correlation failure.

Tool failures and blocked calls remain distinct from model/API failures. A
published lifecycle result is not treated as proof that its tool execution was
error-free.

## Deployment and verification

Edit the numbered SQL sources (`00_tables_and_indexes.sql`,
`50_response_and_workflow.sql`, `60_metrics_and_reporting.sql`) and regenerate
`00_Hermes_L2_FULL_INSTALL.sql`. Update the trace plugin, drainer, and their
tests. Deploy through the existing L2 deployer and verify the live schema,
idempotent duplicate handling, a correlated trace, IST-only projections, and
the lifecycle-observability status without manually claiming a production
ticket.

## Non-goals

- No direct writes to `Complaint_Mst_Tbl`.
- No model-controlled SQL transport.
- No separate monitoring job or second lifecycle authority.
- No historical timestamp conversion or speculative repair of old tickets.
