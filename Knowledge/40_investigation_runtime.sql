SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Start_Investigation_Usp
(
    @RunID        varchar(36),
    @Route        varchar(100) = NULL,
    @HermesUserID varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Hermes_L2_Response_Trn_Tbl
    SET
        ProcessStatus = 'INVESTIGATING',
        Route = COALESCE(@Route, Route),
        HeartbeatOn = GETDATE(),
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

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Save_Investigation_State_Usp
(
    @RunID             varchar(36),
    @Route             varchar(100) = NULL,
    @ProblemSummary    nvarchar(max) = NULL,
    @Findings          nvarchar(max) = NULL,
    @RootCause         nvarchar(max) = NULL,
    @Resolution        nvarchar(max) = NULL,
    @InvestigationJson nvarchar(max) = NULL,
    @NextEligibleOn    datetime = NULL,
    @HermesUserID      varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Hermes_L2_Response_Trn_Tbl
    SET
        ProcessStatus = CASE
            WHEN ProcessStatus = 'CLAIMED' THEN 'INVESTIGATING'
            ELSE ProcessStatus
        END,
        Route = COALESCE(@Route, Route),
        ProblemSummary = COALESCE(@ProblemSummary, ProblemSummary),
        Findings = COALESCE(@Findings, Findings),
        RootCause = COALESCE(@RootCause, RootCause),
        Resolution = COALESCE(@Resolution, Resolution),
        InvestigationJson = COALESCE(@InvestigationJson, InvestigationJson),
        NextEligibleOn = COALESCE(@NextEligibleOn, NextEligibleOn),
        HeartbeatOn = GETDATE(),
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

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Heartbeat_Usp
(
    @RunID        varchar(36),
    @HermesUserID varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Hermes_L2_Response_Trn_Tbl
    SET
        HeartbeatOn = GETDATE(),
        ModifiedBy = COALESCE(@HermesUserID, ModifiedBy),
        ModifiedOn = GETDATE(),
        Source = 'T-SQL'
    WHERE ID = @RunID
      AND IsActive = 1
      AND IsDeleted = 0;

    IF @@ROWCOUNT = 0
        RAISERROR('Active Hermes run not found.', 16, 1);
END;
GO


/*
  Local model admission controller.
  Jev/deterministic work may run for several active tickets concurrently, but
  every task that actually invokes the shared local LM Studio model is queued
  on the run row and admitted through one SQL-serialized slot.
*/
CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Queue_Local_Model_Usp
(
    @RunID          varchar(36),
    @Purpose        varchar(30),
    @Priority       int,
    @WorkKey        varchar(255),
    @ExecutionMode  varchar(30) = NULL,
    @WorkJson       nvarchar(max),
    @HermesUserID   varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    IF NULLIF(LTRIM(RTRIM(@RunID)), '') IS NULL
       OR NULLIF(LTRIM(RTRIM(@Purpose)), '') IS NULL
       OR NULLIF(LTRIM(RTRIM(@WorkKey)), '') IS NULL
       OR NULLIF(LTRIM(RTRIM(@WorkJson)), '') IS NULL
    BEGIN
        RAISERROR('RunID, Purpose, WorkKey and WorkJson are required.', 16, 1);
        RETURN;
    END;

    IF ISJSON(@WorkJson) <> 1
    BEGIN
        RAISERROR('WorkJson must be valid JSON.', 16, 1);
        RETURN;
    END;

    BEGIN TRY
        BEGIN TRANSACTION;

        DECLARE
            @CurrentState varchar(20),
            @CurrentKey varchar(255);

        SELECT
            @CurrentState = LocalModelState,
            @CurrentKey = LocalModelWorkKey
        FROM dbo.Hermes_L2_Response_Trn_Tbl WITH (UPDLOCK, HOLDLOCK)
        WHERE ID = @RunID
          AND IsActive = 1
          AND IsDeleted = 0;

        IF @CurrentState IS NULL AND @CurrentKey IS NULL
           AND NOT EXISTS
           (
               SELECT 1
               FROM dbo.Hermes_L2_Response_Trn_Tbl
               WHERE ID = @RunID
                 AND IsActive = 1
                 AND IsDeleted = 0
           )
        BEGIN
            RAISERROR('Active Hermes run not found.', 16, 1);
        END;

        IF @CurrentState IN ('QUEUED', 'RUNNING') AND @CurrentKey = @WorkKey
        BEGIN
            COMMIT TRANSACTION;
            SELECT
                'ALREADY_QUEUED' AS QueueStatus,
                ID AS RunID,
                TicketID,
                LocalModelState,
                LocalModelPurpose,
                LocalModelPriority,
                LocalModelWorkKey,
                LocalModelTaskID,
                ExecutionMode
            FROM dbo.Hermes_L2_Response_Trn_Tbl
            WHERE ID = @RunID;
            RETURN;
        END;

        IF @CurrentState IN ('QUEUED', 'RUNNING') AND ISNULL(@CurrentKey, '') <> @WorkKey
        BEGIN
            RAISERROR('Run already owns different pending local-model work.', 16, 1);
        END;

        UPDATE dbo.Hermes_L2_Response_Trn_Tbl
        SET
            ExecutionMode = COALESCE(@ExecutionMode, ExecutionMode),
            LocalModelState = 'QUEUED',
            LocalModelPurpose = @Purpose,
            LocalModelPriority = @Priority,
            LocalModelWorkKey = @WorkKey,
            PendingLocalModelJson = @WorkJson,
            LocalModelTaskID = NULL,
            LocalModelQueuedOn = GETDATE(),
            LocalModelStartedOn = NULL,
            LocalModelCompletedOn = NULL,
            HeartbeatOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @RunID
          AND IsActive = 1
          AND IsDeleted = 0;

        COMMIT TRANSACTION;

        SELECT
            'QUEUED' AS QueueStatus,
            ID AS RunID,
            TicketID,
            LocalModelState,
            LocalModelPurpose,
            LocalModelPriority,
            LocalModelWorkKey,
            LocalModelTaskID,
            ExecutionMode
        FROM dbo.Hermes_L2_Response_Trn_Tbl
        WHERE ID = @RunID;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Try_Acquire_Local_Model_Usp
(
    @HermesUserID varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        DECLARE
            @LockResult int,
            @RunID varchar(36);

        EXEC @LockResult = sys.sp_getapplock
            @Resource = 'HermesL2:LocalModelSlot',
            @LockMode = 'Exclusive',
            @LockOwner = 'Transaction',
            @LockTimeout = 0;

        IF @LockResult < 0
        BEGIN
            ROLLBACK TRANSACTION;
            SELECT 'BUSY' AS AcquireStatus;
            RETURN;
        END;

        IF EXISTS
        (
            SELECT 1
            FROM dbo.Hermes_L2_Response_Trn_Tbl WITH (UPDLOCK, HOLDLOCK)
            WHERE IsActive = 1
              AND IsDeleted = 0
              AND LocalModelState = 'RUNNING'
        )
        BEGIN
            COMMIT TRANSACTION;
            SELECT 'BUSY' AS AcquireStatus;
            RETURN;
        END;

        SELECT TOP (1)
            @RunID = ID
        FROM dbo.Hermes_L2_Response_Trn_Tbl WITH (UPDLOCK, READPAST)
        WHERE IsActive = 1
          AND IsDeleted = 0
          AND LocalModelState = 'QUEUED'
          AND PendingLocalModelJson IS NOT NULL
        ORDER BY
            LocalModelPriority DESC,
            LocalModelQueuedOn ASC,
            ClaimedOn ASC,
            ID ASC;

        IF @RunID IS NULL
        BEGIN
            COMMIT TRANSACTION;
            SELECT 'EMPTY' AS AcquireStatus;
            RETURN;
        END;

        UPDATE dbo.Hermes_L2_Response_Trn_Tbl
        SET
            LocalModelState = 'RUNNING',
            LocalModelStartedOn = GETDATE(),
            HeartbeatOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @RunID
          AND LocalModelState = 'QUEUED'
          AND IsActive = 1
          AND IsDeleted = 0;

        IF @@ROWCOUNT <> 1
        BEGIN
            RAISERROR('Could not acquire queued local-model work.', 16, 1);
        END;

        COMMIT TRANSACTION;

        SELECT
            'ACQUIRED' AS AcquireStatus,
            ID AS RunID,
            TicketID,
            ExecutionMode,
            LocalModelPurpose,
            LocalModelPriority,
            LocalModelWorkKey,
            PendingLocalModelJson,
            LocalModelQueuedOn,
            LocalModelStartedOn
        FROM dbo.Hermes_L2_Response_Trn_Tbl
        WHERE ID = @RunID;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Bind_Local_Model_Task_Usp
(
    @RunID        varchar(36),
    @WorkKey      varchar(255),
    @TaskID       varchar(100),
    @HermesUserID varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Hermes_L2_Response_Trn_Tbl
    SET
        LocalModelTaskID = @TaskID,
        HeartbeatOn = GETDATE(),
        ModifiedBy = @HermesUserID,
        ModifiedOn = GETDATE(),
        Source = 'T-SQL'
    WHERE ID = @RunID
      AND IsActive = 1
      AND IsDeleted = 0
      AND LocalModelState = 'RUNNING'
      AND LocalModelWorkKey = @WorkKey;

    IF @@ROWCOUNT <> 1
        RAISERROR('Running local-model work did not match RunID/WorkKey.', 16, 1);

    SELECT
        ID AS RunID,
        TicketID,
        LocalModelState,
        LocalModelPurpose,
        LocalModelWorkKey,
        LocalModelTaskID
    FROM dbo.Hermes_L2_Response_Trn_Tbl
    WHERE ID = @RunID;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Finish_Local_Model_Usp
(
    @RunID        varchar(36),
    @TaskID       varchar(100) = NULL,
    @Outcome      varchar(20) = 'DONE',
    @HermesUserID varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    SET @Outcome = UPPER(LTRIM(RTRIM(ISNULL(@Outcome, 'DONE'))));

    IF @Outcome NOT IN ('DONE', 'REQUEUE')
    BEGIN
        RAISERROR('Outcome must be DONE or REQUEUE.', 16, 1);
        RETURN;
    END;

    IF @Outcome = 'DONE'
    BEGIN
        UPDATE dbo.Hermes_L2_Response_Trn_Tbl
        SET
            LocalModelState = 'DONE',
            LocalModelCompletedOn = GETDATE(),
            HeartbeatOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @RunID
          AND IsActive = 1
          AND IsDeleted = 0
          AND LocalModelState = 'RUNNING'
          AND (@TaskID IS NULL OR LocalModelTaskID = @TaskID);
    END
    ELSE
    BEGIN
        UPDATE dbo.Hermes_L2_Response_Trn_Tbl
        SET
            LocalModelState = 'QUEUED',
            LocalModelTaskID = NULL,
            LocalModelStartedOn = NULL,
            LocalModelCompletedOn = NULL,
            LocalModelQueuedOn = GETDATE(),
            HeartbeatOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @RunID
          AND IsActive = 1
          AND IsDeleted = 0
          AND LocalModelState = 'RUNNING'
          AND (@TaskID IS NULL OR LocalModelTaskID = @TaskID);
    END;

    IF @@ROWCOUNT <> 1
        RAISERROR('No matching running local-model work was found.', 16, 1);

    SELECT
        ID AS RunID,
        TicketID,
        LocalModelState,
        LocalModelPurpose,
        LocalModelWorkKey,
        LocalModelTaskID,
        LocalModelQueuedOn,
        LocalModelStartedOn,
        LocalModelCompletedOn
    FROM dbo.Hermes_L2_Response_Trn_Tbl
    WHERE ID = @RunID;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Execute_SQL_Usp
(
    @RunID          varchar(36),
    @DatabaseName   sysname,
    @ActionType     varchar(30),
    @SchemaName     varchar(200) = NULL,
    @ObjectName     varchar(500) = NULL,
    @OperationName  varchar(500) = NULL,
    @Purpose        nvarchar(1000) = NULL,
    @Sql            nvarchar(max),
    @ParametersJson nvarchar(max) = NULL,
    @BeforeJson     nvarchar(max) = NULL,
    @UseTransaction bit = 0,
    @HermesUserID   varchar(36) = NULL,
    @ActionID       varchar(36) OUTPUT
)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    IF DB_ID(@DatabaseName) IS NULL
    BEGIN
        RAISERROR('Database does not exist on the current SQL Server.', 16, 1);
        RETURN;
    END;

    IF NULLIF(LTRIM(RTRIM(@Sql)), N'') IS NULL
    BEGIN
        RAISERROR('SQL text is required.', 16, 1);
        RETURN;
    END;

    DECLARE
        @TicketID varchar(36),
        @ActionNo int,
        @LockResult int,
        @ExecSql nvarchar(max),
        @RowsAffected int = 0,
        @LockResource varchar(255);

    SELECT @TicketID = TicketID
    FROM dbo.Hermes_L2_Response_Trn_Tbl WITH (NOLOCK)
    WHERE ID = @RunID
      AND IsActive = 1
      AND IsDeleted = 0;

    IF @TicketID IS NULL
    BEGIN
        RAISERROR('Active Hermes run not found.', 16, 1);
        RETURN;
    END;

    SET @ActionID = CONVERT(varchar(36), NEWID());
    SET @LockResource = 'HermesL2:RunAction:' + @RunID;

    /* Allocate a per-run action sequence and persist STARTED before execution. */
    BEGIN TRY
        BEGIN TRANSACTION;

        EXEC @LockResult = sys.sp_getapplock
            @Resource = @LockResource,
            @LockMode = 'Exclusive',
            @LockOwner = 'Transaction',
            @LockTimeout = 5000;

        IF @LockResult < 0
            RAISERROR('Could not allocate Hermes SQL action sequence.', 16, 1);

        SELECT @ActionNo = ISNULL(MAX(ActionNo), 0) + 1
        FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl WITH (UPDLOCK, HOLDLOCK)
        WHERE RunID = @RunID
          AND IsDeleted = 0;

        INSERT INTO dbo.Hermes_L2_SQL_Action_Trn_Tbl
        (
            ID,
            RunID,
            TicketID,
            ActionNo,
            ActionType,
            DatabaseName,
            SchemaName,
            ObjectName,
            OperationName,
            Purpose,
            SqlText,
            ParametersJson,
            BeforeJson,
            Status,
            StartedOn,
            CreatedBy,
            CreatedOn,
            Source
        )
        VALUES
        (
            @ActionID,
            @RunID,
            @TicketID,
            @ActionNo,
            @ActionType,
            @DatabaseName,
            @SchemaName,
            @ObjectName,
            @OperationName,
            @Purpose,
            @Sql,
            @ParametersJson,
            @BeforeJson,
            'STARTED',
            GETDATE(),
            @HermesUserID,
            GETDATE(),
            'T-SQL'
        );

        UPDATE dbo.Hermes_L2_Response_Trn_Tbl
        SET
            HeartbeatOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @RunID;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
        DECLARE @LogErr nvarchar(max) =
            'Could not create Hermes SQL action log: ' + ERROR_MESSAGE();
        RAISERROR(@LogErr, 16, 1);
        RETURN;
    END CATCH;

    /*
      The SQL is intentionally not restricted to SELECT.
      Hermes may read, call official SPs, or perform direct writes/DDL according to
      the SQL identity it is given and the routed investigation plan.

      GO is not valid inside @Sql because GO is a client batch separator, not T-SQL.
    */
    SET @ExecSql =
        N'USE ' + QUOTENAME(@DatabaseName) + N';
          SET NOCOUNT ON;
          ' + @Sql + N'
          SET @__HermesRowsAffected = @@ROWCOUNT;';

    BEGIN TRY
        IF @UseTransaction = 1
            BEGIN TRANSACTION;

        EXEC sys.sp_executesql
            @ExecSql,
            N'@__HermesRowsAffected int OUTPUT',
            @__HermesRowsAffected = @RowsAffected OUTPUT;

        IF @UseTransaction = 1 AND @@TRANCOUNT > 0
            COMMIT TRANSACTION;

        UPDATE dbo.Hermes_L2_SQL_Action_Trn_Tbl
        SET
            Status = 'SUCCESS',
            RowsAffected = @RowsAffected,
            CompletedOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @ActionID;

        UPDATE dbo.Hermes_L2_Response_Trn_Tbl
        SET
            HeartbeatOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @RunID;

        SELECT
            @ActionID AS HermesActionID,
            @RowsAffected AS HermesRowsAffected,
            'SUCCESS' AS HermesActionStatus;
    END TRY
    BEGIN CATCH
        IF @UseTransaction = 1 AND @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        UPDATE dbo.Hermes_L2_SQL_Action_Trn_Tbl
        SET
            Status = 'FAILED',
            CompletedOn = GETDATE(),
            ErrorNumber = ERROR_NUMBER(),
            ErrorMessage = ERROR_MESSAGE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @ActionID;

        UPDATE dbo.Hermes_L2_Response_Trn_Tbl
        SET
            HeartbeatOn = GETDATE(),
            ModifiedBy = @HermesUserID,
            ModifiedOn = GETDATE(),
            Source = 'T-SQL'
        WHERE ID = @RunID;

        DECLARE @ExecErr nvarchar(max) =
            'Hermes SQL action failed. ActionID=' + @ActionID
            + ' | Line=' + CONVERT(varchar(20), ERROR_LINE())
            + ' | Message=' + ERROR_MESSAGE();

        RAISERROR(@ExecErr, 16, 1);
    END CATCH
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Update_SQL_Action_Evidence_Usp
(
    @ActionID     varchar(36),
    @BeforeJson   nvarchar(max) = NULL,
    @AfterJson    nvarchar(max) = NULL,
    @HermesUserID varchar(36) = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Hermes_L2_SQL_Action_Trn_Tbl
    SET
        BeforeJson = COALESCE(@BeforeJson, BeforeJson),
        AfterJson = COALESCE(@AfterJson, AfterJson),
        ModifiedBy = @HermesUserID,
        ModifiedOn = GETDATE(),
        Source = 'T-SQL'
    WHERE ID = @ActionID
      AND IsDeleted = 0;

    IF @@ROWCOUNT = 0
        RAISERROR('Hermes SQL action not found.', 16, 1);
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Get_Run_Actions_Usp
(
    @RunID varchar(36)
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT *
    FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl WITH (NOLOCK)
    WHERE RunID = @RunID
      AND IsDeleted = 0
    ORDER BY ActionNo;
END;
GO
