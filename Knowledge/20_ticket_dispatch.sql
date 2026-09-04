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
      AND NOT EXISTS
      (
          SELECT 1
          FROM dbo.Hermes_L2_Response_Trn_Tbl AS activeRun WITH (NOLOCK)
          WHERE activeRun.TicketID = c.ID
            AND activeRun.IsActive = 1
            AND activeRun.IsDeleted = 0
      )
      /* 2026-09-05: a ticket with an open L3 escalation is a human's job now,
         not the bot's -- confirmed live that this was missing entirely: a
         real L3_ESCALATION publish leaves Complaint_Mst_Tbl.Status
         unchanged ('Enter'), so the moment ANY later event marks that
         ticket's run FAILED (a genuine crash, or even just the routine
         60-minute staleness sweep on a NEW unrelated claim), the ticket
         silently became eligible again with zero awareness that it was
         already sitting in the human queue -- confirmed live burning 615K
         tokens re-investigating a ticket already escalated with the real
         root cause on file. Exclude outright while a human still owns it. */
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

          /* The ticket changed after Hermes last published/observed it. */
          OR ISNULL(c.ModifiedOn, c.CreatedOn)
             > ISNULL(latest.TicketModifiedOnSeen, CONVERT(datetime, '19000101', 112))

          /* Timed continuation after an UPDATE. */
          OR
          (
              latest.ResponseType = 'UPDATE'
              AND latest.NextEligibleOn IS NOT NULL
              AND latest.NextEligibleOn <= GETDATE()
          )

          /* Retry a failed run after the retry time. */
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

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Claim_Ticket_Usp
(
    @TicketID          varchar(36),
    @EligibleStatusCsv varchar(max),
    @WorkerID          varchar(200),
    @HermesUserID      varchar(36) = NULL,
    @HostAddress       varchar(100) = NULL,
    @RunID             varchar(36) OUTPUT
)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    IF NULLIF(@TicketID, '') IS NULL
    BEGIN
        RAISERROR('TicketID is required.', 16, 1);
        RETURN;
    END;

    IF NULLIF(LTRIM(RTRIM(@EligibleStatusCsv)), '') IS NULL
    BEGIN
        RAISERROR('Eligible Helpdesk status list is required.', 16, 1);
        RETURN;
    END;

    DECLARE
        @LockResult int,
        @AttemptNo int,
        @TicketModifiedOn datetime,
        @TicketStatus varchar(50),
        @LockResource varchar(255);

    SET @RunID = CONVERT(varchar(36), NEWID());
    SET @LockResource = 'HermesL2:Ticket:' + @TicketID;

    BEGIN TRY
        BEGIN TRANSACTION;

        EXEC @LockResult = sys.sp_getapplock
            @Resource = @LockResource,
            @LockMode = 'Exclusive',
            @LockOwner = 'Transaction',
            @LockTimeout = 0;

        IF @LockResult < 0
        BEGIN
            RAISERROR('Ticket is already being claimed by another Hermes worker.', 16, 1);
        END;

        SELECT
            @TicketModifiedOn = ISNULL(ModifiedOn, CreatedOn),
            @TicketStatus = Status
        FROM dbo.Complaint_Mst_Tbl WITH (UPDLOCK, HOLDLOCK)
        WHERE ID = @TicketID
          AND ISNULL(IsDeleted, 0) = 0;

        IF @TicketModifiedOn IS NULL
        BEGIN
            RAISERROR('Ticket not found or deleted.', 16, 1);
        END;

        IF NOT EXISTS
        (
            SELECT 1
            FROM STRING_SPLIT(@EligibleStatusCsv, ',') AS s
            WHERE LTRIM(RTRIM(s.value)) = @TicketStatus
        )
        BEGIN
            RAISERROR('Ticket is no longer in an eligible L2 Helpdesk status.', 16, 1);
        END;

        IF EXISTS
        (
            SELECT 1
            FROM dbo.Hermes_L2_Response_Trn_Tbl WITH (UPDLOCK, HOLDLOCK)
            WHERE TicketID = @TicketID
              AND IsActive = 1
              AND IsDeleted = 0
        )
        BEGIN
            RAISERROR('Ticket already has an active Hermes run.', 16, 1);
        END;

        SELECT @AttemptNo = ISNULL(MAX(AttemptNo), 0) + 1
        FROM dbo.Hermes_L2_Response_Trn_Tbl WITH (UPDLOCK, HOLDLOCK)
        WHERE TicketID = @TicketID
          AND IsDeleted = 0;

        INSERT INTO dbo.Hermes_L2_Response_Trn_Tbl
        (
            ID,
            TicketID,
            AttemptNo,
            WorkerID,
            ProcessStatus,
            IsActive,
            TicketModifiedOnSeen,
            ClaimedOn,
            HeartbeatOn,
            CreatedBy,
            CreatedOn,
            HostAddress,
            Source
        )
        VALUES
        (
            @RunID,
            @TicketID,
            @AttemptNo,
            @WorkerID,
            'CLAIMED',
            1,
            @TicketModifiedOn,
            GETDATE(),
            GETDATE(),
            @HermesUserID,
            GETDATE(),
            @HostAddress,
            'T-SQL'
        );

        COMMIT TRANSACTION;

        SELECT *
        FROM dbo.Hermes_L2_Response_Trn_Tbl
        WHERE ID = @RunID;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;

        DECLARE @Err nvarchar(max) =
            'SP : Hermes_L2_Claim_Ticket_Usp | Line : '
            + CONVERT(varchar(20), ERROR_LINE())
            + ' | Message : ' + ERROR_MESSAGE();

        RAISERROR(@Err, 16, 1);
    END CATCH
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Recover_Stale_Runs_Usp
(
    @StaleMinutes int = 60,
    @HermesUserID varchar(36) = NULL,
    -- Added 2026-09-04: this SP is pure T-SQL and has no visibility into
    -- Kanban, so a run whose kanban task is still legitimately queued
    -- (ready/blocked/running -- just backed up behind other work, not
    -- abandoned) was being yanked out from under it purely on wall-clock
    -- elapsed time. Confirmed live: one ticket accumulated 22 consecutive
    -- forced-FAILED-and-reclaimed cycles this way, and a separate bug
    -- (the l2-review board never being dispatched) meant every one of
    -- those cycles was actually still "being worked" from Kanban's point
    -- of view the whole time. The caller (Hermes_Orchestrator.py) now
    -- checks live Kanban state before invoking this SP and passes the
    -- run_ids that still have a live task here, so they're skipped
    -- regardless of how long they've been claimed -- this SP no longer
    -- has to be the sole judge of "stale." Comma-separated GUIDs; NULL
    -- (default) preserves the prior blind-timeout behavior exactly, for
    -- backward compatibility with any other caller.
    @ExcludeRunIDs varchar(max) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    IF @StaleMinutes IS NULL OR @StaleMinutes < 1 SET @StaleMinutes = 60;

    UPDATE dbo.Hermes_L2_Response_Trn_Tbl
    SET
        ProcessStatus = 'FAILED',
        IsActive = 0,
        ErrorMessage = COALESCE(
            ErrorMessage + CHAR(13) + CHAR(10),
            N''
        ) + N'Recovered as stale by Hermes scheduler.',
        NextEligibleOn = GETDATE(),
        CompletedOn = GETDATE(),
        ModifiedBy = @HermesUserID,
        ModifiedOn = GETDATE(),
        Source = 'T-SQL'
    WHERE IsActive = 1
      AND IsDeleted = 0
      AND ISNULL(HeartbeatOn, ClaimedOn) < DATEADD(MINUTE, -@StaleMinutes, GETDATE())
      AND (
          @ExcludeRunIDs IS NULL
          OR ID NOT IN (SELECT LTRIM(RTRIM(value)) FROM STRING_SPLIT(@ExcludeRunIDs, ','))
      );

    SELECT @@ROWCOUNT AS RecoveredRunCount;
END;
GO
