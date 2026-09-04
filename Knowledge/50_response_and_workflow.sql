SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Publish_Response_Usp
(
    @RunID                        varchar(36),
    @ResponseType                 varchar(30),
    @ReplyText                    nvarchar(max),
    @ProblemSummary               nvarchar(max) = NULL,
    @Findings                     nvarchar(max) = NULL,
    @RootCause                    nvarchar(max) = NULL,
    @Resolution                   nvarchar(max) = NULL,
    @InvestigationJson            nvarchar(max) = NULL,
    @NewTicketStatus              varchar(50) = NULL,
    @NewAskStatus                 varchar(50) = NULL,
    @NextEligibleOn               datetime = NULL,
    @MirrorReplyToSupportRemarks  bit = 0,
    @MirrorQuestionToAskRemarks   bit = 0,
    @HermesUserID                 varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    SET @ResponseType = UPPER(LTRIM(RTRIM(@ResponseType)));

    /*
      2026-09-05: NEEDS_HUMAN_ACTION added as a genuinely distinct
      category from L3_ESCALATION, per explicit user direction --
      L3_ESCALATION means the bot could NOT diagnose/solve the problem;
      NEEDS_HUMAN_ACTION means the bot DID diagnose it and knows the fix,
      but a human has to actually execute it (outside the bot's write
      authority, a floor/business action, etc.). Conflating these into one
      "L3_ESCALATION" bucket was exactly what made the human queue
      unreadable -- a human opening it couldn't tell "nobody knows what's
      wrong" from "we know exactly what's wrong and what to do about it"
      without reading every row.
    */
    IF @ResponseType NOT IN ('QUESTION', 'UPDATE', 'RESOLUTION', 'L3_ESCALATION', 'NEEDS_HUMAN_ACTION')
    BEGIN
        RAISERROR('ResponseType must be QUESTION, UPDATE, RESOLUTION, L3_ESCALATION, or NEEDS_HUMAN_ACTION.', 16, 1);
        RETURN;
    END;

    IF NULLIF(LTRIM(RTRIM(@ReplyText)), N'') IS NULL
    BEGIN
        RAISERROR('ReplyText is required.', 16, 1);
        RETURN;
    END;

    DECLARE
        @TicketID varchar(36),
        @TicketModifiedOn datetime,
        @AutoActionsJson nvarchar(max);

    SELECT @TicketID = TicketID
    FROM dbo.Hermes_L2_Response_Trn_Tbl WITH (UPDLOCK)
    WHERE ID = @RunID
      AND IsActive = 1
      AND IsDeleted = 0;

    IF @TicketID IS NULL
    BEGIN
        RAISERROR('Active Hermes run not found.', 16, 1);
        RETURN;
    END;

    SELECT @AutoActionsJson =
    (
        SELECT
            ActionNo,
            ActionType,
            DatabaseName,
            SchemaName,
            ObjectName,
            OperationName,
            Purpose,
            Status,
            RowsAffected,
            StartedOn,
            CompletedOn,
            ErrorNumber,
            ErrorMessage
        FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl WITH (NOLOCK)
        WHERE RunID = @RunID
          AND IsDeleted = 0
        ORDER BY ActionNo
        FOR JSON PATH
    );

    BEGIN TRY
        BEGIN TRANSACTION;

        /*
          Existing Helpdesk remains the workflow owner.
          Status strings are supplied from the live-discovered workflow; this SP does not
          invent "Open", "L2", "Closed", "L3", etc.
        */
        UPDATE dbo.Complaint_Mst_Tbl
        SET
            Status = COALESCE(@NewTicketStatus, Status),
            AskStatus = COALESCE(@NewAskStatus, AskStatus),
            Solution =
                CASE
                    WHEN @ResponseType = 'RESOLUTION'
                     AND NULLIF(@Resolution, N'') IS NOT NULL
                    THEN CONVERT(varchar(max), @Resolution)
                    ELSE Solution
                END,
            SupportExecutiveRemarks =
                CASE
                    WHEN @MirrorReplyToSupportRemarks = 1
                    THEN CONVERT(varchar(max), @ReplyText)
                    ELSE SupportExecutiveRemarks
                END,
            AskRemarks =
                CASE
                    WHEN @ResponseType = 'QUESTION'
                     AND @MirrorQuestionToAskRemarks = 1
                    THEN CONVERT(varchar(max), @ReplyText)
                    ELSE AskRemarks
                END,
            ModifiedBy = COALESCE(@HermesUserID, ModifiedBy),
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @TicketID
          AND ISNULL(IsDeleted, 0) = 0;

        IF @@ROWCOUNT = 0
            RAISERROR('Helpdesk ticket not found while publishing Hermes response.', 16, 1);

        SELECT @TicketModifiedOn = ISNULL(ModifiedOn, CreatedOn)
        FROM dbo.Complaint_Mst_Tbl WITH (NOLOCK)
        WHERE ID = @TicketID;

        UPDATE dbo.Hermes_L2_Response_Trn_Tbl
        SET
            ProcessStatus =
                CASE
                    WHEN @ResponseType = 'QUESTION' THEN 'WAITING_USER'
                    ELSE 'COMPLETED'
                END,
            IsActive = 0,
            ResponseType = @ResponseType,
            ProblemSummary = COALESCE(@ProblemSummary, ProblemSummary),
            Findings = COALESCE(@Findings, Findings),
            RootCause = COALESCE(@RootCause, RootCause),
            Resolution = COALESCE(@Resolution, Resolution),
            ReplyText = @ReplyText,
            InvestigationJson = COALESCE(@InvestigationJson, InvestigationJson),
            ActionsTakenJson = @AutoActionsJson,
            RequiresUserInput = CASE WHEN @ResponseType = 'QUESTION' THEN 1 ELSE 0 END,
            EscalateToL3 = CASE WHEN @ResponseType IN ('L3_ESCALATION', 'NEEDS_HUMAN_ACTION') THEN 1 ELSE 0 END,
            IsResolved = CASE WHEN @ResponseType = 'RESOLUTION' THEN 1 ELSE 0 END,
            TicketModifiedOnSeen = @TicketModifiedOn,
            NextEligibleOn =
                CASE
                    WHEN @ResponseType = 'UPDATE' THEN @NextEligibleOn
                    ELSE NULL
                END,
            HeartbeatOn = GETDATE(),
            CompletedOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @RunID
          AND IsActive = 1
          AND IsDeleted = 0;

        IF @@ROWCOUNT = 0
            RAISERROR('Hermes run changed before response publication.', 16, 1);

        /*
          2026-09-04 fix: this insert used to live ONLY inside
          Hermes_L2_Escalate_L3_Usp, which nothing in the live pipeline
          ever actually calls (kanban_approval_publisher.py always calls
          --publish-response directly, regardless of ResponseType) --
          confirmed live: 62 real ResponseType='L3_ESCALATION' rows existed
          with ZERO matching rows in Hermes_L3_Escalation_Trn_Tbl. Moved
          here so every call path that publishes an L3_ESCALATION response
          populates the human L3 work queue, not just one specific wrapper.
        */
        /*
          2026-09-05: two genuinely distinct human-queue categories, per
          explicit direction -- do not conflate "couldn't solve it" with
          "solved it, needs a human to execute." EscalationCategory:
            UNRESOLVED         = L3_ESCALATION: the bot could not
                                  diagnose/solve the problem.
            NEEDS_HUMAN_ACTION = NEEDS_HUMAN_ACTION: the bot diagnosed the
                                  problem and knows the fix (@Resolution),
                                  but a human must actually execute it.
          The generic safety-net "didn't publish in time" rescue no longer
          reaches this table at all -- it was never a real escalation of
          either kind, just the pipeline losing track of a run, and
          dumping it in the human queue was pure noise. That case now goes
          through Hermes_L2_Fail_Run_Usp instead (plain retry, no human
          queue), see enforce_publish_safety_net.py.
        */
        IF @ResponseType IN ('L3_ESCALATION', 'NEEDS_HUMAN_ACTION')
        BEGIN
            INSERT INTO dbo.Hermes_L3_Escalation_Trn_Tbl
            (
                RunID, TicketID, TicketNo, EscalatedByBot,
                ProblemSummary, Findings, RootCause, SuggestedAction, ReplyText,
                InvestigationJson, EscalationCategory, CreatedBy, Source
            )
            SELECT
                r.ID, r.TicketID, c.TicketNo, r.WorkerID,
                @ProblemSummary, @Findings, @RootCause,
                CASE WHEN @ResponseType = 'NEEDS_HUMAN_ACTION' THEN @Resolution ELSE NULL END,
                @ReplyText,
                @InvestigationJson,
                CASE WHEN @ResponseType = 'NEEDS_HUMAN_ACTION' THEN 'NEEDS_HUMAN_ACTION' ELSE 'UNRESOLVED' END,
                @HermesUserID, 'T-SQL'
            FROM dbo.Hermes_L2_Response_Trn_Tbl r
            LEFT JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
            WHERE r.ID = @RunID
              AND NOT EXISTS (
                  SELECT 1 FROM dbo.Hermes_L3_Escalation_Trn_Tbl e
                  WHERE e.RunID = @RunID AND e.IsDeleted = 0
              );
        END;

        COMMIT TRANSACTION;

        SELECT *
        FROM dbo.Hermes_L2_Response_Trn_Tbl
        WHERE ID = @RunID;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;

        DECLARE @Err nvarchar(max) =
            'SP : Hermes_L2_Publish_Response_Usp | Line : '
            + CONVERT(varchar(20), ERROR_LINE())
            + ' | Message : ' + ERROR_MESSAGE();

        RAISERROR(@Err, 16, 1);
    END CATCH
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Ask_Question_Usp
(
    @RunID                       varchar(36),
    @Question                    nvarchar(max),
    @NewTicketStatus             varchar(50) = NULL,
    @NewAskStatus                varchar(50) = NULL,
    @MirrorQuestionToAskRemarks  bit = 0,
    @HermesUserID                varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    EXEC dbo.Hermes_L2_Publish_Response_Usp
        @RunID = @RunID,
        @ResponseType = 'QUESTION',
        @ReplyText = @Question,
        @NewTicketStatus = @NewTicketStatus,
        @NewAskStatus = @NewAskStatus,
        @MirrorQuestionToAskRemarks = @MirrorQuestionToAskRemarks,
        @HermesUserID = @HermesUserID;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Resolve_Ticket_Usp
(
    @RunID                varchar(36),
    @ReplyText             nvarchar(max),
    @Resolution            nvarchar(max),
    @ResolvedTicketStatus  varchar(50),
    @ProblemSummary        nvarchar(max) = NULL,
    @Findings              nvarchar(max) = NULL,
    @RootCause             nvarchar(max) = NULL,
    @InvestigationJson     nvarchar(max) = NULL,
    @MirrorToSupportRemarks bit = 0,
    @HermesUserID          varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    IF NULLIF(LTRIM(RTRIM(@ResolvedTicketStatus)), '') IS NULL
    BEGIN
        RAISERROR('ResolvedTicketStatus is required and must be the live Helpdesk workflow value.', 16, 1);
        RETURN;
    END;

    EXEC dbo.Hermes_L2_Publish_Response_Usp
        @RunID = @RunID,
        @ResponseType = 'RESOLUTION',
        @ReplyText = @ReplyText,
        @ProblemSummary = @ProblemSummary,
        @Findings = @Findings,
        @RootCause = @RootCause,
        @Resolution = @Resolution,
        @InvestigationJson = @InvestigationJson,
        @NewTicketStatus = @ResolvedTicketStatus,
        @MirrorReplyToSupportRemarks = @MirrorToSupportRemarks,
        @HermesUserID = @HermesUserID;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Escalate_L3_Usp
(
    @RunID                varchar(36),
    @ReplyText             nvarchar(max),
    @L3TicketStatus        varchar(50),
    @ProblemSummary        nvarchar(max) = NULL,
    @Findings              nvarchar(max) = NULL,
    @RootCause             nvarchar(max) = NULL,
    @InvestigationJson     nvarchar(max) = NULL,
    @MirrorToSupportRemarks bit = 0,
    @HermesUserID          varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    IF NULLIF(LTRIM(RTRIM(@L3TicketStatus)), '') IS NULL
    BEGIN
        RAISERROR('L3TicketStatus is required and must be the live Helpdesk workflow value.', 16, 1);
        RETURN;
    END;

    -- The Hermes_L3_Escalation_Trn_Tbl insert now lives inside
    -- Hermes_L2_Publish_Response_Usp itself (gated on ResponseType =
    -- 'L3_ESCALATION', with a NOT EXISTS guard against double-insert) --
    -- fixed 2026-09-04 so every call path populates the L3 queue, not just
    -- this one convenience wrapper, which nothing in the live pipeline
    -- actually calls.
    EXEC dbo.Hermes_L2_Publish_Response_Usp
        @RunID = @RunID,
        @ResponseType = 'L3_ESCALATION',
        @ReplyText = @ReplyText,
        @ProblemSummary = @ProblemSummary,
        @Findings = @Findings,
        @RootCause = @RootCause,
        @InvestigationJson = @InvestigationJson,
        @NewTicketStatus = @L3TicketStatus,
        @MirrorReplyToSupportRemarks = @MirrorToSupportRemarks,
        @HermesUserID = @HermesUserID;
END;
GO

/*
  2026-09-04: pure-visibility escalation for a run that hit a genuine
  kanban_block (capability gap -- ambiguous schema, missing data, etc.)
  while a live kanban task still tracks it. Deliberately does NOT touch
  Hermes_L2_Response_Trn_Tbl or the ticket's own Status/AskStatus -- unlike
  Hermes_L2_Escalate_L3_Usp / Hermes_L2_Publish_Response_Usp, this does not
  complete or fail the run; Kanban is still free to retry it. Its only job
  is making sure a human sees the block reason and what was actually
  checked, instead of the task sitting silently 'blocked' forever with
  zero visibility -- confirmed live 2026-09-04: a ticket sat blocked 3+
  hours on a real, unresolved schema ambiguity with no escalation of any
  kind. Guarded by the same NOT EXISTS pattern as the other L3 insert so a
  run already escalated (by this path or the ResponseType='L3_ESCALATION'
  path) is never double-inserted.
*/
CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Log_Blocked_Escalation_Usp
(
    @RunID          varchar(36),
    @TicketID        varchar(36),
    @BlockReason     nvarchar(max),
    @Findings        nvarchar(max) = NULL,
    @HermesUserID    varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (SELECT 1 FROM dbo.Hermes_L3_Escalation_Trn_Tbl WHERE RunID = @RunID AND IsDeleted = 0)
        RETURN;

    INSERT INTO dbo.Hermes_L3_Escalation_Trn_Tbl
    (
        RunID, TicketID, TicketNo, EscalatedByBot,
        ProblemSummary, Findings, RootCause, SuggestedAction,
        CreatedBy, Source
    )
    SELECT
        @RunID, @TicketID, c.TicketNo, r.WorkerID,
        COALESCE(c.ConversationSummary, c.BriefDetails), @Findings, @BlockReason,
        'Automated investigation blocked on a genuine capability gap -- needs human review.',
        @HermesUserID, 'T-SQL'
    FROM dbo.Complaint_Mst_Tbl c
    LEFT JOIN dbo.Hermes_L2_Response_Trn_Tbl r ON r.ID = @RunID
    WHERE c.ID = @TicketID;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L3_Get_Open_Escalations_Usp
(
    @L3Status varchar(30) = NULL   -- NULL returns Open + Assigned + InProgress (the active queue)
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        e.ID, e.RunID, e.TicketID, e.TicketNo, e.EscalatedOn, e.EscalatedByBot,
        e.ProblemSummary, e.Findings, e.RootCause, e.SuggestedAction, e.ReplyText,
        e.InvestigationJson, e.EvidenceViewsJson,
        e.L3Status, e.AssignedToUserID, e.AssignedOn, e.L3Remarks
    FROM dbo.Hermes_L3_Escalation_Trn_Tbl e
    WHERE e.IsDeleted = 0
      AND (
            (@L3Status IS NULL AND e.L3Status IN ('Open', 'Assigned', 'InProgress'))
            OR e.L3Status = @L3Status
          )
    ORDER BY e.EscalatedOn ASC;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L3_Update_Escalation_Status_Usp
(
    @EscalationID       varchar(36),
    @NewL3Status        varchar(30),
    @AssignedToUserID   varchar(36)   = NULL,
    @L3Remarks          nvarchar(max) = NULL,
    @L3ResolutionSummary nvarchar(max) = NULL,
    @HermesUserID       varchar(36)   = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    IF @NewL3Status NOT IN ('Open', 'Assigned', 'InProgress', 'Resolved', 'Rejected')
    BEGIN
        RAISERROR('NewL3Status must be one of Open/Assigned/InProgress/Resolved/Rejected.', 16, 1);
        RETURN;
    END;

    UPDATE dbo.Hermes_L3_Escalation_Trn_Tbl
    SET
        L3Status            = @NewL3Status,
        AssignedToUserID    = COALESCE(@AssignedToUserID, AssignedToUserID),
        AssignedOn          = CASE WHEN @AssignedToUserID IS NOT NULL AND AssignedOn IS NULL
                                    THEN GETDATE() ELSE AssignedOn END,
        L3Remarks           = COALESCE(@L3Remarks, L3Remarks),
        L3ResolutionSummary = COALESCE(@L3ResolutionSummary, L3ResolutionSummary),
        ResolvedByUserID    = CASE WHEN @NewL3Status = 'Resolved' THEN @HermesUserID ELSE ResolvedByUserID END,
        ResolvedOn          = CASE WHEN @NewL3Status = 'Resolved' THEN GETDATE() ELSE ResolvedOn END,
        ModifiedBy          = @HermesUserID,
        ModifiedOn          = GETDATE(),
        Source              = 'T-SQL'
    WHERE ID = @EscalationID
      AND IsDeleted = 0;

    IF @@ROWCOUNT = 0
        RAISERROR('Escalation row not found.', 16, 1);
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Fail_Run_Usp
(
    @RunID             varchar(36),
    @ErrorMessage      nvarchar(max),
    @RetryAfterMinutes int = 5,
    @HermesUserID      varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    IF @RetryAfterMinutes IS NULL OR @RetryAfterMinutes < 0
        SET @RetryAfterMinutes = 5;

    UPDATE dbo.Hermes_L2_Response_Trn_Tbl
    SET
        ProcessStatus = 'FAILED',
        IsActive = 0,
        ErrorMessage = @ErrorMessage,
        NextEligibleOn = DATEADD(MINUTE, @RetryAfterMinutes, GETDATE()),
        HeartbeatOn = GETDATE(),
        CompletedOn = GETDATE(),
        ModifiedBy = @HermesUserID,
        ModifiedOn = GETDATE(),
        Source = 'T-SQL'
    WHERE ID = @RunID
      AND IsActive = 1
      AND IsDeleted = 0;

    IF @@ROWCOUNT = 0
        RAISERROR('Active Hermes run not found.', 16, 1);
END;
GO

-- ============================================================================
-- Advanced Helpdesk enhancements (2026-09-03) -- write SPs for the new
-- activity log / knowledge base / feedback tables in 00_tables_and_indexes.sql.
-- ============================================================================

CREATE OR ALTER PROCEDURE dbo.Hermes_Log_Ticket_Activity_Usp
(
    @TicketID          varchar(36),
    @ActivityType       varchar(30),
    @ActorType          varchar(20) = 'Bot',
    @ActorName          varchar(200) = NULL,
    @NoteText           nvarchar(max) = NULL,
    @OldValue           nvarchar(500) = NULL,
    @NewValue           nvarchar(500) = NULL,
    @IsCustomerVisible  bit = 0,
    @RunID              varchar(36) = NULL,
    @HermesUserID       varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    IF @ActivityType NOT IN ('Note', 'StatusChange', 'Escalation', 'Resolution', 'Reopen', 'SolutionLinked', 'ProblemLinked')
    BEGIN
        RAISERROR('ActivityType must be one of Note/StatusChange/Escalation/Resolution/Reopen/SolutionLinked/ProblemLinked.', 16, 1);
        RETURN;
    END;

    INSERT INTO dbo.Hermes_Ticket_Activity_Trn_Tbl
        (TicketID, RunID, ActivityType, ActorType, ActorName, NoteText, OldValue, NewValue, IsCustomerVisible, CreatedBy, Source)
    VALUES
        (@TicketID, @RunID, @ActivityType, @ActorType, @ActorName, @NoteText, @OldValue, @NewValue, @IsCustomerVisible, @HermesUserID, 'T-SQL');
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_Get_Ticket_Activity_Usp
(
    @TicketID varchar(36)
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT ID, RunID, ActivityType, ActorType, ActorName, NoteText, OldValue, NewValue, IsCustomerVisible, CreatedOn
    FROM dbo.Hermes_Ticket_Activity_Trn_Tbl
    WHERE TicketID = @TicketID AND IsDeleted = 0
    ORDER BY CreatedOn ASC;
END;
GO

/*
Hermes_Log_Agent_Trace_Usp
Sink for Model_Bench/drain_l2_trace_log.py, which drains the
xstudio-l2-trace Hermes observer-hook plugin's local JSONL event log
(~/.hermes/plugin-data/xstudio-l2-trace/events.jsonl) into
Hermes_Agent_Trace_Trn_Tbl. Added 2026-09-04 -- the plugin captures every
tool call and API request the L2 bots make at the platform layer,
regardless of what the model remembers to log itself (the same "stop
trusting narration, consult ground truth" fix already applied to the
kanban staleness logic and the --query audit gap this same session).
Plain insert, no branching -- this is telemetry, not a business
transaction, and the source is a trusted local process, not user input.
*/
CREATE OR ALTER PROCEDURE dbo.Hermes_Log_Agent_Trace_Usp
(
    @EventType          varchar(50),
    @EventOn            datetime,
    @SessionID          varchar(100) = NULL,
    @TaskID             varchar(100) = NULL,
    @TurnID             varchar(100) = NULL,
    @ToolCallID         varchar(100) = NULL,
    @ApiRequestID       varchar(100) = NULL,
    @ToolName           varchar(200) = NULL,
    @Status             varchar(30)  = NULL,
    @DurationMs         int          = NULL,
    @ArgsJson           nvarchar(max) = NULL,
    @ResultJson         nvarchar(max) = NULL,
    @ErrorMessage       nvarchar(max) = NULL,
    @Model              varchar(200) = NULL,
    @Provider           varchar(100) = NULL,
    @UsageJson          nvarchar(max) = NULL,
    -- Added 2026-09-04: resolved once per kanban session (task_id -> run_id/
    -- ticket_id via `hermes kanban show`) and carried on every event for
    -- that session, so a per-ticket compute rollup (tokens used, GPU
    -- samples, tool-call counts) is a direct GROUP BY TicketID over this
    -- table -- no join back to kanban's own sqlite state needed.
    @RunID              varchar(36)  = NULL,
    @TicketID           varchar(36)  = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO dbo.Hermes_Agent_Trace_Trn_Tbl
        (EventType, EventOn, SessionID, TaskID, TurnID, ToolCallID, ApiRequestID,
         ToolName, Status, DurationMs, ArgsJson, ResultJson, ErrorMessage,
         Model, Provider, UsageJson, RunID, TicketID, Source)
    VALUES
        (@EventType, @EventOn, @SessionID, @TaskID, @TurnID, @ToolCallID, @ApiRequestID,
         @ToolName, @Status, @DurationMs, @ArgsJson, @ResultJson, @ErrorMessage,
         @Model, @Provider, @UsageJson, @RunID, @TicketID, 'T-SQL');
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_Create_Solution_Article_Usp
(
    @Title               nvarchar(300),
    @ResolutionSteps     nvarchar(max),
    @ProblemSummary      nvarchar(max) = NULL,
    @RootCause           nvarchar(max) = NULL,
    @RootCauseCategoryID varchar(36) = NULL,
    @Route               varchar(100) = NULL,
    @RelatedViewsJson    nvarchar(max) = NULL,
    @Tags                nvarchar(500) = NULL,
    @HermesUserID        varchar(36) = NULL,
    @NewSolutionID       varchar(36) OUTPUT
)
AS
BEGIN
    SET NOCOUNT ON;

    SET @NewSolutionID = CONVERT(varchar(36), NEWID());

    INSERT INTO dbo.Hermes_Solution_Article_Mst_Tbl
        (ID, Title, ProblemSummary, RootCause, ResolutionSteps, RootCauseCategoryID, Route, RelatedViewsJson, Tags, CreatedBy, Source)
    VALUES
        (@NewSolutionID, @Title, @ProblemSummary, @RootCause, @ResolutionSteps, @RootCauseCategoryID, @Route, @RelatedViewsJson, @Tags, @HermesUserID, 'T-SQL');
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_Link_Solution_To_Ticket_Usp
(
    @TicketID      varchar(36),
    @SolutionID    varchar(36),
    @RunID         varchar(36) = NULL,
    @WasHelpful    bit = NULL,
    @HermesUserID  varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO dbo.Hermes_Ticket_Solution_Link_Tbl (TicketID, SolutionID, RunID, WasHelpful, LinkedBy)
    VALUES (@TicketID, @SolutionID, @RunID, @WasHelpful, @HermesUserID);

    UPDATE dbo.Hermes_Solution_Article_Mst_Tbl
    SET UsageCount = UsageCount + 1, ModifiedOn = GETDATE()
    WHERE ID = @SolutionID;

    EXEC dbo.Hermes_Log_Ticket_Activity_Usp
        @TicketID = @TicketID, @ActivityType = 'SolutionLinked', @ActorType = 'Bot',
        @NoteText = 'Linked to an existing solution article.', @RunID = @RunID, @HermesUserID = @HermesUserID;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_Create_Problem_Usp
(
    @Title               nvarchar(300),
    @RootCauseSummary    nvarchar(max) = NULL,
    @RootCauseCategoryID varchar(36) = NULL,
    @HermesUserID        varchar(36) = NULL,
    @NewProblemID        varchar(36) OUTPUT
)
AS
BEGIN
    SET NOCOUNT ON;

    SET @NewProblemID = CONVERT(varchar(36), NEWID());

    INSERT INTO dbo.Hermes_Problem_Mst_Tbl (ID, Title, RootCauseSummary, RootCauseCategoryID, CreatedBy)
    VALUES (@NewProblemID, @Title, @RootCauseSummary, @RootCauseCategoryID, @HermesUserID);
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_Link_Ticket_To_Problem_Usp
(
    @ProblemID     varchar(36),
    @TicketID      varchar(36),
    @HermesUserID  varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM dbo.Hermes_Problem_Ticket_Link_Tbl WHERE ProblemID = @ProblemID AND TicketID = @TicketID AND IsDeleted = 0)
    BEGIN
        INSERT INTO dbo.Hermes_Problem_Ticket_Link_Tbl (ProblemID, TicketID, LinkedBy)
        VALUES (@ProblemID, @TicketID, @HermesUserID);

        EXEC dbo.Hermes_Log_Ticket_Activity_Usp
            @TicketID = @TicketID, @ActivityType = 'ProblemLinked', @ActorType = 'Bot',
            @NoteText = 'Linked to a recurring Problem record.', @HermesUserID = @HermesUserID;
    END;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_Submit_Ticket_Feedback_Usp
(
    @TicketID              varchar(36),
    @SatisfactionRating    int = NULL,
    @FeedbackText          nvarchar(max) = NULL,
    @IsReopen              bit = 0,
    @ReopenedFromTicketID  varchar(36) = NULL,
    @HermesUserID          varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO dbo.Hermes_Ticket_Feedback_Trn_Tbl
        (TicketID, SatisfactionRating, FeedbackText, IsReopen, ReopenedFromTicketID, SubmittedBy)
    VALUES
        (@TicketID, @SatisfactionRating, @FeedbackText, @IsReopen, @ReopenedFromTicketID, @HermesUserID);

    IF @IsReopen = 1
        EXEC dbo.Hermes_Log_Ticket_Activity_Usp
            @TicketID = @TicketID, @ActivityType = 'Reopen', @ActorType = 'Human',
            @NoteText = @FeedbackText, @IsCustomerVisible = 1, @HermesUserID = @HermesUserID;
END;
GO
