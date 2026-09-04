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
