/*
  Required post-install hardening for Hermes_L2_Get_Candidate_Tickets_Usp.

  Why this exists:
  the runtime used to fetch TOP 20 candidates and then remove customization
  request types in Python. If the first 20 rows were all customization work,
  the bot reported NO_CLAIMABLE_TICKET even when valid incident tickets existed
  at row 21+. Filtering belongs in SQL before TOP/ORDER BY.
*/
SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Get_Candidate_Tickets_Usp
(
    @EligibleStatusCsv varchar(max),
    @BatchSize         int = 20
)
AS
BEGIN
    SET NOCOUNT ON;

    IF NULLIF(LTRIM(RTRIM(@EligibleStatusCsv)), '') IS NULL
    BEGIN
        RAISERROR('Eligible Helpdesk status list is required. Discover the live workflow first.', 16, 1);
        RETURN;
    END;

    IF @BatchSize IS NULL OR @BatchSize < 1 SET @BatchSize = 20;
    IF @BatchSize > 500 SET @BatchSize = 500;

    SELECT TOP (@BatchSize)
        c.ID AS TicketID,
        c.TicketNo,
        c.AreaID,
        COALESCE(a.Name, c.AreaID) AS AreaName,
        c.ComplaintTypeID,
        COALESCE(ct.Name, c.ComplaintTypeID) AS ComplaintTypeName,
        c.BriefDetails,
        c.Description,
        c.Priority,
        COALESCE(p.priority, c.Priority) AS PriorityName,
        c.Status,
        c.AskStatus,
        c.messages,
        c.AssignedUserID,
        c.FirstLastName,
        c.EmailID,
        c.ContactNo,
        c.CreatedOn,
        c.ModifiedOn,
        latest.ID AS LatestHermesRunID,
        latest.ResponseType AS LatestHermesResponseType,
        latest.ProcessStatus AS LatestHermesProcessStatus,
        latest.RequiresUserInput,
        latest.EscalateToL3,
        latest.IsResolved,
        latest.TicketModifiedOnSeen,
        latest.NextEligibleOn
    FROM dbo.Complaint_Mst_Tbl AS c WITH (NOLOCK)
    LEFT JOIN dbo.priority_mst AS p WITH (NOLOCK)
        ON ISNULL(p.IsDeleted, 0) = 0
       AND (p.ID = c.Priority OR p.priority = c.Priority)
    LEFT JOIN dbo.Area_Mst_Tbl AS a WITH (NOLOCK)
        ON ISNULL(a.IsDeleted, 0) = 0
       AND (a.ID = c.AreaID OR a.Name = c.AreaID)
    LEFT JOIN dbo.ComplaintType_Mst_Tbl AS ct WITH (NOLOCK)
        ON ISNULL(ct.IsDeleted, 0) = 0
       AND (ct.ID = c.ComplaintTypeID OR ct.Name = c.ComplaintTypeID)
    OUTER APPLY
    (
        SELECT TOP (1) r.*
        FROM dbo.Hermes_L2_Response_Trn_Tbl AS r WITH (NOLOCK)
        WHERE r.TicketID = c.ID
          AND r.IsDeleted = 0
        ORDER BY r.CreatedOn DESC, r.AttemptNo DESC
    ) AS latest
    WHERE ISNULL(c.IsDeleted, 0) = 0
      AND EXISTS
      (
          SELECT 1
          FROM STRING_SPLIT(@EligibleStatusCsv, ',') AS s
          WHERE LTRIM(RTRIM(s.value)) = c.Status
      )
      /* L2 incidents only. Apply BEFORE TOP so customization rows cannot hide
         valid claimable tickets further down the queue. */
      AND ISNULL(COALESCE(ct.Name, c.ComplaintTypeID), '') NOT IN
      (
          'Request for Customization',
          'Request For Customization Rights'
      )
      AND NOT EXISTS
      (
          SELECT 1
          FROM dbo.Hermes_L2_Response_Trn_Tbl AS activeRun WITH (NOLOCK)
          WHERE activeRun.TicketID = c.ID
            AND activeRun.IsActive = 1
            AND activeRun.IsDeleted = 0
      )
      AND NOT EXISTS
      (
          SELECT 1
          FROM dbo.Hermes_L3_Escalation_Trn_Tbl AS l3 WITH (NOLOCK)
          WHERE l3.TicketID = c.ID
            AND l3.IsDeleted = 0
            AND l3.L3Status IN ('Open', 'Assigned', 'InProgress')
      )
      AND
      (
          latest.ID IS NULL
          OR ISNULL(c.ModifiedOn, c.CreatedOn)
             > ISNULL(latest.TicketModifiedOnSeen, CONVERT(datetime, '19000101', 112))
          OR
          (
              latest.ResponseType = 'UPDATE'
              AND latest.NextEligibleOn IS NOT NULL
              AND latest.NextEligibleOn <= GETDATE()
          )
          OR
          (
              latest.ProcessStatus = 'FAILED'
              AND latest.NextEligibleOn IS NOT NULL
              AND latest.NextEligibleOn <= GETDATE()
          )
      )
    ORDER BY
        CASE LOWER(ISNULL(COALESCE(p.priority, c.Priority), ''))
            WHEN 'critical' THEN 1
            WHEN 'high priority' THEN 2
            WHEN 'standard' THEN 3
            ELSE 4
        END,
        c.CreatedOn ASC,
        c.ID ASC;
END;
GO
