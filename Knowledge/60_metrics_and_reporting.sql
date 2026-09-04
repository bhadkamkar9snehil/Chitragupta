-- ============================================================================
-- Hermes L2 -- Ticket Response Time Metrics
-- ============================================================================
-- Added 2026-09-02 at the user's explicit request: "start tracking this data
-- properly" (average time for one ticket response, including deep-investigation
-- tickets, not just fast ones).
--
-- Excludes:
--   - ProcessStatus = 'FAILED' rows -- these are stale-recovered/timed-out
--     abandons (the sweep sets CompletedOn to when it recovered the run, often
--     30-60+ minutes later; that is NOT investigation time, counting it would
--     wildly inflate the average with failures, not depth).
--   - ProcessStatus = 'INVESTIGATING' rows -- still open, no CompletedOn yet.
--   - DurationSeconds < 30 -- a real multi-step SQL investigation by the LLM
--     cannot complete in under 30 seconds; sub-30s rows in the historical data
--     are from the 2026-09-02 mechanism-verification/dummy-ticket testing phase
--     (WorkerID IN ('SP_VERIFY','TEST_WORKER'), or fast programmatic inserts
--     that happened to share WorkerID='HERMES_WORKER_001'), not genuine bot
--     investigations. This filter keeps the metric honest going forward without
--     needing a schema change to add a proper "is_test" flag.
-- ============================================================================

IF OBJECT_ID('dbo.Hermes_L2_Response_Time_Metrics_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Response_Time_Metrics_Vw;
GO

CREATE VIEW dbo.Hermes_L2_Response_Time_Metrics_Vw
AS
SELECT
    r.ID,
    r.TicketID,
    r.AttemptNo,
    r.ResponseType,
    r.WorkerID,
    r.ClaimedOn,
    r.CompletedOn,
    DATEDIFF(SECOND, r.ClaimedOn, r.CompletedOn) AS DurationSeconds
FROM dbo.Hermes_L2_Response_Trn_Tbl r
WHERE r.ProcessStatus IN ('COMPLETED', 'WAITING_USER')
  AND r.ClaimedOn IS NOT NULL
  AND r.CompletedOn IS NOT NULL
  AND DATEDIFF(SECOND, r.ClaimedOn, r.CompletedOn) >= 30;
GO

IF OBJECT_ID('dbo.Hermes_L2_Response_Time_Summary_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Response_Time_Summary_Vw;
GO

-- All-time summary. Will always include the 2026-09-02 testing-phase window;
-- prefer the _Recent_ view below once enough real production data accumulates.
CREATE VIEW dbo.Hermes_L2_Response_Time_Summary_Vw
AS
SELECT
    COUNT(*) AS SampleCount,
    AVG(DurationSeconds) AS AvgDurationSeconds,
    MIN(DurationSeconds) AS MinDurationSeconds,
    MAX(DurationSeconds) AS MaxDurationSeconds,
    CAST(AVG(DurationSeconds) / 60.0 AS DECIMAL(10, 2)) AS AvgDurationMinutes
FROM dbo.Hermes_L2_Response_Time_Metrics_Vw;
GO

IF OBJECT_ID('dbo.Hermes_L2_Response_Time_Summary_Recent_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Response_Time_Summary_Recent_Vw;
GO

-- Rolling 7-day window -- the metric that actually matters once the deployment
-- has been running for a while; ages out the one-time testing-phase noise
-- automatically without needing manual pruning.
CREATE VIEW dbo.Hermes_L2_Response_Time_Summary_Recent_Vw
AS
SELECT
    COUNT(*) AS SampleCount,
    AVG(DurationSeconds) AS AvgDurationSeconds,
    MIN(DurationSeconds) AS MinDurationSeconds,
    MAX(DurationSeconds) AS MaxDurationSeconds,
    CAST(AVG(DurationSeconds) / 60.0 AS DECIMAL(10, 2)) AS AvgDurationMinutes
FROM dbo.Hermes_L2_Response_Time_Metrics_Vw
WHERE CompletedOn >= DATEADD(DAY, -7, GETDATE());
GO

-- ============================================================================
-- Hermes L2 -- Investigation depth, outcome, and worker/model performance
-- ============================================================================
-- Added 2026-09-03 at the user's explicit request: "tracking of performance
-- of ticket investigation". The views above already measure claim-to-complete
-- duration; these add what that doesn't cover -- how many real SQL actions
-- an investigation actually took, its final outcome type, whether it needed
-- a retry, whether it was escalated to L3 and how long that human handoff
-- took, and a per-WorkerID (bot/model) rollup so different models/profiles
-- can be compared on the same real metric instead of eyeballed.
--
-- No new columns needed on Hermes_L2_Response_Trn_Tbl or
-- Hermes_L2_SQL_Action_Trn_Tbl -- everything here is derivable by joining
-- the tables that already exist, at the ticket volumes this system runs at
-- (hundreds, not millions of rows) a live join is simpler and safer than a
-- denormalized counter column that needs its own write-path/trigger upkeep.
-- ============================================================================

IF OBJECT_ID('dbo.Hermes_L2_Investigation_Metrics_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Investigation_Metrics_Vw;
GO

CREATE VIEW dbo.Hermes_L2_Investigation_Metrics_Vw
AS
SELECT
    r.ID AS RunID,
    r.TicketID,
    r.AttemptNo,
    r.WorkerID,
    r.Route,
    r.ResponseType,
    r.ProcessStatus,
    r.EscalateToL3,
    r.IsResolved,
    r.RequiresUserInput,
    r.ClaimedOn,
    r.CompletedOn,
    DATEDIFF(SECOND, r.ClaimedOn, r.CompletedOn) AS DurationSeconds,
    (SELECT COUNT(*) FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl a
      WHERE a.RunID = r.ID AND a.IsDeleted = 0) AS SqlActionCount,
    (SELECT COUNT(DISTINCT a.DatabaseName) FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl a
      WHERE a.RunID = r.ID AND a.IsDeleted = 0 AND a.DatabaseName IS NOT NULL) AS DistinctDatabasesTouched,
    (SELECT COUNT(*) FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl a
      WHERE a.RunID = r.ID AND a.IsDeleted = 0 AND a.Status = 'FAILED') AS FailedSqlActionCount,
    CASE WHEN r.AttemptNo = 1 THEN 1 ELSE 0 END AS ResolvedOnFirstAttempt
FROM dbo.Hermes_L2_Response_Trn_Tbl r
WHERE r.IsDeleted = 0;
GO

IF OBJECT_ID('dbo.Hermes_L2_Worker_Performance_Summary_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Worker_Performance_Summary_Vw;
GO

-- Per-WorkerID (bot/model/profile label) rollup -- the real-data equivalent
-- of what Model_Bench/model_scorecard.py computes externally, now queryable
-- directly. "Genuine" here means an actual RESOLUTION/QUESTION/L3_ESCALATION
-- response was published (ProcessStatus reaching a terminal non-FAILED
-- state) -- it does not by itself prove the response was CORRECT, only that
-- something concrete was published rather than the run failing/timing out.
CREATE VIEW dbo.Hermes_L2_Worker_Performance_Summary_Vw
AS
WITH RunActionCounts AS (
    SELECT
        r.ID AS RunID,
        r.WorkerID,
        r.ProcessStatus,
        r.EscalateToL3,
        r.IsResolved,
        r.ClaimedOn,
        r.CompletedOn,
        (SELECT COUNT(*) FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl a
          WHERE a.RunID = r.ID AND a.IsDeleted = 0) AS SqlActionCount
    FROM dbo.Hermes_L2_Response_Trn_Tbl r
    WHERE r.IsDeleted = 0
      AND r.WorkerID IS NOT NULL
)
SELECT
    WorkerID,
    COUNT(*) AS TotalRuns,
    SUM(CASE WHEN ProcessStatus = 'FAILED' THEN 1 ELSE 0 END) AS FailedRuns,
    SUM(CASE WHEN ProcessStatus IN ('COMPLETED', 'WAITING_USER') THEN 1 ELSE 0 END) AS TerminalRuns,
    SUM(CASE WHEN EscalateToL3 = 1 THEN 1 ELSE 0 END) AS EscalatedToL3Count,
    SUM(CASE WHEN IsResolved = 1 THEN 1 ELSE 0 END) AS ResolvedCount,
    AVG(CASE WHEN ProcessStatus IN ('COMPLETED', 'WAITING_USER') AND ClaimedOn IS NOT NULL AND CompletedOn IS NOT NULL
             THEN DATEDIFF(SECOND, ClaimedOn, CompletedOn) END) AS AvgDurationSeconds,
    AVG(CAST(SqlActionCount AS FLOAT)) AS AvgSqlActionCount
FROM RunActionCounts
GROUP BY WorkerID;
GO

IF OBJECT_ID('dbo.Hermes_L3_Escalation_Turnaround_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L3_Escalation_Turnaround_Vw;
GO

-- Human L3 handoff performance: how long escalations actually sit before a
-- human resolves them, by current status. Depends on Hermes_L3_Escalation_Trn_Tbl
-- (added 2026-09-03) actually being populated -- will be empty/NULL until
-- real escalations flow through Hermes_L2_Escalate_L3_Usp.
CREATE VIEW dbo.Hermes_L3_Escalation_Turnaround_Vw
AS
SELECT
    e.L3Status,
    COUNT(*) AS EscalationCount,
    AVG(CASE WHEN e.ResolvedOn IS NOT NULL
             THEN DATEDIFF(MINUTE, e.EscalatedOn, e.ResolvedOn) END) AS AvgMinutesToResolve,
    MIN(e.EscalatedOn) AS OldestEscalatedOn,
    MAX(e.EscalatedOn) AS NewestEscalatedOn
FROM dbo.Hermes_L3_Escalation_Trn_Tbl e
WHERE e.IsDeleted = 0
GROUP BY e.L3Status;
GO

-- ============================================================================
-- Hermes L2 -- ticket resolution time tracking
-- ============================================================================
-- Added 2026-09-03 at the user's explicit request: "tracking [of] time it
-- took to resolve ticket and sorts" -- plain duration measurement, not
-- SLA breach/at-risk status against invented targets (an earlier version
-- of this file did that; the user corrected it -- no real documented SLA
-- policy exists to judge breach against, so this only measures, it does
-- not grade).
--
-- Resolved = ticket.CreatedOn -> the ticket's real resolution moment, which
-- can come from EITHER a direct L2 RESOLUTION publish (terminal CompletedOn
-- on a RESOLUTION-type run) OR a human L3 resolution
-- (Hermes_L3_Escalation_Trn_Tbl.ResolvedOn, L3Status='Resolved') --
-- whichever exists, since either genuinely closes the loop for the
-- requester. A QUESTION/L3_ESCALATION run alone does not count as resolved.
-- ============================================================================

IF OBJECT_ID('dbo.Hermes_L2_Ticket_Resolution_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Ticket_Resolution_Vw;
GO

CREATE VIEW dbo.Hermes_L2_Ticket_Resolution_Vw
AS
WITH FirstAck AS (
    SELECT TicketID, MIN(ClaimedOn) AS FirstAcknowledgedOn
    FROM dbo.Hermes_L2_Response_Trn_Tbl
    WHERE IsDeleted = 0 AND ClaimedOn IS NOT NULL
    GROUP BY TicketID
),
L2Resolution AS (
    SELECT TicketID, MAX(CompletedOn) AS L2ResolvedOn
    FROM dbo.Hermes_L2_Response_Trn_Tbl
    WHERE IsDeleted = 0
      AND ResponseType = 'RESOLUTION'
      AND ProcessStatus IN ('COMPLETED', 'WAITING_USER')
      AND CompletedOn IS NOT NULL
    GROUP BY TicketID
),
L3Resolution AS (
    SELECT TicketID, MAX(ResolvedOn) AS L3ResolvedOn
    FROM dbo.Hermes_L3_Escalation_Trn_Tbl
    WHERE IsDeleted = 0 AND L3Status = 'Resolved' AND ResolvedOn IS NOT NULL
    GROUP BY TicketID
)
SELECT
    c.ID AS TicketID,
    c.TicketNo,
    p.priority AS PriorityName,
    ct.Name AS ComplaintTypeName,
    c.AreaID,
    c.Status AS TicketStatus,
    c.CreatedOn AS TicketCreatedOn,
    fa.FirstAcknowledgedOn,
    DATEDIFF(MINUTE, c.CreatedOn, fa.FirstAcknowledgedOn) AS TimeToFirstResponseMinutes,
    COALESCE(l2r.L2ResolvedOn, l3r.L3ResolvedOn) AS ResolvedOn,
    CASE WHEN l2r.L2ResolvedOn IS NOT NULL AND (l3r.L3ResolvedOn IS NULL OR l2r.L2ResolvedOn <= l3r.L3ResolvedOn) THEN 'L2'
         WHEN l3r.L3ResolvedOn IS NOT NULL THEN 'L3'
    END AS ResolvedVia,
    DATEDIFF(MINUTE, c.CreatedOn, COALESCE(l2r.L2ResolvedOn, l3r.L3ResolvedOn)) AS TimeToResolveMinutes,
    CAST(DATEDIFF(MINUTE, c.CreatedOn, COALESCE(l2r.L2ResolvedOn, l3r.L3ResolvedOn)) / 60.0 AS DECIMAL(10, 2)) AS TimeToResolveHours
FROM dbo.Complaint_Mst_Tbl c
LEFT JOIN dbo.priority_mst p ON p.ID = c.Priority
LEFT JOIN dbo.ComplaintType_Mst_Tbl ct ON ct.ID = c.ComplaintTypeID
LEFT JOIN FirstAck fa ON fa.TicketID = c.ID
LEFT JOIN L2Resolution l2r ON l2r.TicketID = c.ID
LEFT JOIN L3Resolution l3r ON l3r.TicketID = c.ID
WHERE c.IsDeleted = 0;
GO

IF OBJECT_ID('dbo.Hermes_L2_Resolution_Time_By_Priority_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Resolution_Time_By_Priority_Vw;
GO

CREATE VIEW dbo.Hermes_L2_Resolution_Time_By_Priority_Vw
AS
SELECT
    PriorityName,
    COUNT(*) AS TicketCount,
    SUM(CASE WHEN ResolvedOn IS NOT NULL THEN 1 ELSE 0 END) AS ResolvedCount,
    AVG(CASE WHEN ResolvedOn IS NOT NULL THEN TimeToResolveMinutes END) AS AvgTimeToResolveMinutes,
    MIN(CASE WHEN ResolvedOn IS NOT NULL THEN TimeToResolveMinutes END) AS MinTimeToResolveMinutes,
    MAX(CASE WHEN ResolvedOn IS NOT NULL THEN TimeToResolveMinutes END) AS MaxTimeToResolveMinutes,
    AVG(TimeToFirstResponseMinutes) AS AvgTimeToFirstResponseMinutes
FROM dbo.Hermes_L2_Ticket_Resolution_Vw
GROUP BY PriorityName;
GO

IF OBJECT_ID('dbo.Hermes_L2_Resolution_Time_By_Type_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Resolution_Time_By_Type_Vw;
GO

CREATE VIEW dbo.Hermes_L2_Resolution_Time_By_Type_Vw
AS
SELECT
    ComplaintTypeName,
    ResolvedVia,
    COUNT(*) AS TicketCount,
    AVG(TimeToResolveMinutes) AS AvgTimeToResolveMinutes,
    MIN(TimeToResolveMinutes) AS MinTimeToResolveMinutes,
    MAX(TimeToResolveMinutes) AS MaxTimeToResolveMinutes
FROM dbo.Hermes_L2_Ticket_Resolution_Vw
WHERE ResolvedOn IS NOT NULL
GROUP BY ComplaintTypeName, ResolvedVia;
GO

-- ============================================================================
-- Compute per ticket -- added 2026-09-04 at the user's explicit request
-- ("proper computation of compute needed and used per ticket across various
-- lifecycle events"). Derived entirely from Hermes_Agent_Trace_Trn_Tbl, which
-- the xstudio-l2-trace/xstudio-l2-orchestrator Hermes observer-hook plugins
-- populate automatically for every tool call and API request the L2 bots
-- make -- no separate instrumentation needed per ticket. TicketID/RunID are
-- resolved once per kanban session by the plugin and carried on every event
-- row, so this is a plain GROUP BY, not a cross-database join against
-- kanban's own sqlite state.
--
-- UsageJson is whatever the model provider returned on post_api_request,
-- normally OpenAI-compatible {"prompt_tokens":N,"completion_tokens":N,
-- "total_tokens":N} -- LM Studio included. OPENJSON against a NULL/malformed
-- value returns no rows, so a ticket with no captured usage data simply
-- shows 0 rather than erroring the whole view.
-- ============================================================================

IF OBJECT_ID('dbo.Hermes_L2_Compute_Per_Ticket_Vw', 'V') IS NOT NULL
    DROP VIEW dbo.Hermes_L2_Compute_Per_Ticket_Vw;
GO

CREATE VIEW dbo.Hermes_L2_Compute_Per_Ticket_Vw
AS
SELECT
    t.TicketID,
    t.RunID,
    COUNT(DISTINCT t.SessionID)                                   AS SessionCount,
    COUNT(*)                                                      AS TotalTraceEvents,
    SUM(CASE WHEN t.EventType = 'pre_tool_call' THEN 1 ELSE 0 END)  AS ToolCallCount,
    SUM(CASE WHEN t.EventType = 'post_api_request' THEN 1 ELSE 0 END) AS ApiRequestCount,
    SUM(CASE WHEN t.EventType = 'api_request_error' THEN 1 ELSE 0 END) AS ApiRequestErrorCount,
    SUM(CASE WHEN u.[key] = 'total_tokens' THEN TRY_CAST(u.[value] AS int) ELSE 0 END) AS TotalTokens,
    SUM(CASE WHEN u.[key] = 'prompt_tokens' THEN TRY_CAST(u.[value] AS int) ELSE 0 END) AS PromptTokens,
    SUM(CASE WHEN u.[key] = 'completion_tokens' THEN TRY_CAST(u.[value] AS int) ELSE 0 END) AS CompletionTokens,
    SUM(CASE WHEN t.EventType = 'post_tool_call' THEN t.DurationMs ELSE 0 END) AS ToolCallDurationMsTotal,
    MIN(t.EventOn)                                                AS FirstEventOn,
    MAX(t.EventOn)                                                AS LastEventOn,
    DATEDIFF(SECOND, MIN(t.EventOn), MAX(t.EventOn))              AS WallClockSeconds
FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
OUTER APPLY (
    SELECT [key], [value]
    FROM OPENJSON(t.UsageJson)
    WHERE ISJSON(t.UsageJson) = 1 AND [key] IN ('prompt_tokens', 'completion_tokens', 'total_tokens')
) u
WHERE t.IsDeleted = 0 AND t.TicketID IS NOT NULL
GROUP BY t.TicketID, t.RunID;
GO
