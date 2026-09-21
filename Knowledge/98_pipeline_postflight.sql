/* Deterministic L2 pipeline hardening postflight. Read-only. */
SET NOCOUNT ON;

DECLARE @Failures table (CheckName varchar(200), Details nvarchar(max));

IF OBJECT_ID('dbo.Hermes_L2_Get_Candidate_Tickets_Usp', 'P') IS NULL
    INSERT INTO @Failures VALUES ('candidate_proc_exists', 'Hermes_L2_Get_Candidate_Tickets_Usp is missing.');
ELSE IF OBJECT_DEFINITION(OBJECT_ID('dbo.Hermes_L2_Get_Candidate_Tickets_Usp')) NOT LIKE '%Request for Customization%'
    INSERT INTO @Failures VALUES ('candidate_filter_hardening', 'Apply Knowledge/25_ticket_dispatch_hardening.sql; customization filtering is not present in the candidate procedure.');

IF OBJECT_ID('dbo.Hermes_L2_Default_Update_Continuation_Trg', 'TR') IS NULL
    INSERT INTO @Failures VALUES ('update_continuation_hardening', 'Apply Knowledge/55_update_retry_hardening.sql; UPDATE responses can otherwise become permanently ineligible.');

IF OBJECT_ID('dbo.Hermes_Agent_Trace_Trn_Tbl', 'U') IS NULL
    INSERT INTO @Failures VALUES ('agent_trace_table', 'Hermes_Agent_Trace_Trn_Tbl is missing; trace observability and Jev trace assessment cannot operate.');

IF COL_LENGTH('dbo.Hermes_L2_Response_Trn_Tbl', 'JevReviewJson') IS NULL
    INSERT INTO @Failures VALUES ('jev_run_state', 'Jev run/review columns are missing on Hermes_L2_Response_Trn_Tbl.');

IF COL_LENGTH('dbo.Hermes_L2_Response_Trn_Tbl', 'JevInvestigationJson') IS NULL
    INSERT INTO @Failures VALUES ('jev_investigation_state', 'Jev investigation state column is missing on Hermes_L2_Response_Trn_Tbl.');

IF OBJECT_ID('dbo.Hermes_Jev_Run_Assessment_Vw', 'V') IS NULL
    INSERT INTO @Failures VALUES ('jev_assessment_view', 'Hermes_Jev_Run_Assessment_Vw is missing; deploy Knowledge/60_metrics_and_reporting.sql from the current bundle.');

IF OBJECT_ID('dbo.Hermes_Agent_Trace_Trn_Tbl', 'U') IS NULL
    INSERT INTO @Failures VALUES ('agent_trace', 'Hermes_Agent_Trace_Trn_Tbl is missing; Jev call/retrieval telemetry reuses this existing trace store.');

IF COL_LENGTH('dbo.Hermes_Solution_Article_Mst_Tbl', 'ArticleStatus') IS NULL
    INSERT INTO @Failures VALUES ('kb_article_lifecycle', 'Solution article governance columns are missing (ArticleStatus/KnowledgeType/applicability).');

IF COL_LENGTH('dbo.Hermes_Solution_Article_Mst_Tbl', 'ApplicabilityJson') IS NULL
    INSERT INTO @Failures VALUES ('kb_applicability', 'ApplicabilityJson is missing from Hermes_Solution_Article_Mst_Tbl.');

IF EXISTS
(
    SELECT TicketID
    FROM dbo.Hermes_L2_Response_Trn_Tbl
    WHERE IsActive = 1 AND IsDeleted = 0
    GROUP BY TicketID
    HAVING COUNT(*) > 1
)
    INSERT INTO @Failures VALUES ('one_active_run_per_ticket', 'At least one ticket has multiple active Hermes runs.');

DECLARE @ActiveRunCount int =
(
    SELECT COUNT(*)
    FROM dbo.Hermes_L2_Response_Trn_Tbl
    WHERE IsActive = 1 AND IsDeleted = 0
);

SELECT
    'active_pipeline_runs' AS CheckName,
    @ActiveRunCount AS CurrentValue,
    CASE WHEN @ActiveRunCount <= 1 THEN 'OK' ELSE 'WARN: current runtime contract is global WIP=1; reconcile/drain existing backlog before enabling scout.' END AS Result;

IF EXISTS (SELECT 1 FROM @Failures)
BEGIN
    SELECT * FROM @Failures ORDER BY CheckName;
    RAISERROR('L2 pipeline hardening postflight failed. See result set.', 16, 1);
    RETURN;
END;

SELECT 'pipeline_hardening' AS CheckName, 'OK' AS Result;
