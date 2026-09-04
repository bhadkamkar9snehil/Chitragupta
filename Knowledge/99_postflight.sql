/*
Hermes L2 - non-destructive postflight
Run in XStudio_Helpdesk after installation.
*/

SET NOCOUNT ON;

SELECT
    OBJECT_ID('dbo.Hermes_L2_Response_Trn_Tbl') AS ResponseTableObjectID,
    OBJECT_ID('dbo.Hermes_L2_SQL_Action_Trn_Tbl') AS SQLActionTableObjectID,
    OBJECT_ID('dbo.Hermes_L3_Escalation_Trn_Tbl') AS L3EscalationTableObjectID,
    OBJECT_ID('dbo.Hermes_L2_Investigation_Metrics_Vw') AS InvestigationMetricsViewObjectID,
    OBJECT_ID('dbo.Hermes_L2_Worker_Performance_Summary_Vw') AS WorkerPerformanceViewObjectID,
    OBJECT_ID('dbo.Hermes_L3_Escalation_Turnaround_Vw') AS L3TurnaroundViewObjectID,
    OBJECT_ID('dbo.Hermes_L2_Ticket_Resolution_Vw') AS TicketResolutionViewObjectID,
    OBJECT_ID('dbo.Hermes_L2_Resolution_Time_By_Priority_Vw') AS ResolutionByPriorityViewObjectID,
    OBJECT_ID('dbo.Hermes_L2_Resolution_Time_By_Type_Vw') AS ResolutionByTypeViewObjectID,
    OBJECT_ID('dbo.Hermes_Ticket_Activity_Trn_Tbl') AS ActivityTableObjectID,
    OBJECT_ID('dbo.Hermes_Root_Cause_Category_Mst_Tbl') AS RootCauseCategoryTableObjectID,
    OBJECT_ID('dbo.Hermes_Solution_Article_Mst_Tbl') AS SolutionArticleTableObjectID,
    OBJECT_ID('dbo.Hermes_Ticket_Solution_Link_Tbl') AS TicketSolutionLinkTableObjectID,
    OBJECT_ID('dbo.Hermes_Problem_Mst_Tbl') AS ProblemTableObjectID,
    OBJECT_ID('dbo.Hermes_Problem_Ticket_Link_Tbl') AS ProblemTicketLinkTableObjectID,
    OBJECT_ID('dbo.Hermes_Ticket_Feedback_Trn_Tbl') AS FeedbackTableObjectID,
    OBJECT_ID('dbo.Hermes_Escalation_Rule_Mst_Tbl') AS EscalationRuleTableObjectID;

DECLARE @Expected TABLE(ProcedureName sysname);
INSERT INTO @Expected(ProcedureName)
VALUES
('Hermes_L2_Discover_Helpdesk_Workflow_Usp'),
('Hermes_L2_Get_Candidate_Tickets_Usp'),
('Hermes_L2_Claim_Ticket_Usp'),
('Hermes_L2_Recover_Stale_Runs_Usp'),
('Hermes_Log_Agent_Trace_Usp'),
('Hermes_L2_Log_Blocked_Escalation_Usp'),
('Hermes_L2_Get_Ticket_Context_Usp'),
('Hermes_L2_Get_Run_Usp'),
('Hermes_L2_Get_Reference_Documents_Usp'),
('Hermes_L2_Find_SQL_Objects_Usp'),
('Hermes_L2_Get_SQL_Object_Definition_Usp'),
('Hermes_L2_Start_Investigation_Usp'),
('Hermes_L2_Save_Investigation_State_Usp'),
('Hermes_L2_Heartbeat_Usp'),
('Hermes_L2_Execute_SQL_Usp'),
('Hermes_L2_Update_SQL_Action_Evidence_Usp'),
('Hermes_L2_Get_Run_Actions_Usp'),
('Hermes_L2_Publish_Response_Usp'),
('Hermes_L2_Ask_Question_Usp'),
('Hermes_L2_Resolve_Ticket_Usp'),
('Hermes_L2_Escalate_L3_Usp'),
('Hermes_L2_Fail_Run_Usp'),
('Hermes_L3_Get_Open_Escalations_Usp'),
('Hermes_L3_Update_Escalation_Status_Usp'),
('Hermes_Log_Ticket_Activity_Usp'),
('Hermes_Get_Ticket_Activity_Usp'),
('Hermes_Create_Solution_Article_Usp'),
('Hermes_Link_Solution_To_Ticket_Usp'),
('Hermes_Create_Problem_Usp'),
('Hermes_Link_Ticket_To_Problem_Usp'),
('Hermes_Submit_Ticket_Feedback_Usp');

SELECT
    e.ProcedureName,
    CASE WHEN p.object_id IS NULL THEN 0 ELSE 1 END AS ExistsFlag,
    p.modify_date
FROM @Expected AS e
LEFT JOIN sys.procedures AS p
    ON p.name = e.ProcedureName
   AND SCHEMA_NAME(p.schema_id) = 'dbo'
ORDER BY ExistsFlag, e.ProcedureName;

SELECT
    TicketID,
    COUNT(1) AS ActiveRunCount
FROM dbo.Hermes_L2_Response_Trn_Tbl
WHERE IsActive = 1
  AND IsDeleted = 0
GROUP BY TicketID
HAVING COUNT(1) > 1;

SELECT
    r.ID AS OrphanRunID,
    r.TicketID
FROM dbo.Hermes_L2_Response_Trn_Tbl AS r
LEFT JOIN dbo.Complaint_Mst_Tbl AS c ON c.ID = r.TicketID
WHERE r.IsDeleted = 0
  AND c.ID IS NULL;

SELECT
    a.ID AS OrphanActionID,
    a.RunID,
    a.TicketID
FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl AS a
LEFT JOIN dbo.Hermes_L2_Response_Trn_Tbl AS r ON r.ID = a.RunID
WHERE a.IsDeleted = 0
  AND r.ID IS NULL;

/* The most important deployment discovery: bind real workflow values after reviewing this. */
EXEC dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp;

/* Every escalation row must trace back to a real run -- catch orphans early. */
SELECT
    e.ID AS OrphanEscalationID,
    e.RunID,
    e.TicketID
FROM dbo.Hermes_L3_Escalation_Trn_Tbl AS e
LEFT JOIN dbo.Hermes_L2_Response_Trn_Tbl AS r ON r.ID = e.RunID
WHERE e.IsDeleted = 0
  AND r.ID IS NULL;

/* Confirm Hermes can discover current XBatch objects. */
IF DB_ID('XStudio_Xbatch') IS NOT NULL
BEGIN
    EXEC dbo.Hermes_L2_Find_SQL_Objects_Usp
        @DatabaseName = 'XStudio_Xbatch',
        @SearchText = N'XMES_API_Transaction_Summary_Fact_Tbl',
        @ObjectType = 'TABLE',
        @TopN = 20;
END;
