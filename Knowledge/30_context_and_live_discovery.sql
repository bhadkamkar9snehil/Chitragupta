SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Get_Ticket_Context_Usp
(
    @TicketID    varchar(36),
    @HistoryRows int = 10
)
AS
BEGIN
    SET NOCOUNT ON;

    IF @HistoryRows IS NULL OR @HistoryRows < 1 SET @HistoryRows = 10;
    IF @HistoryRows > 100 SET @HistoryRows = 100;

    /* Result 1: ticket + readable master values. */
    SELECT
        c.*,
        COALESCE(a.Name, c.AreaID) AS HermesAreaName,
        COALESCE(ct.Name, c.ComplaintTypeID) AS HermesComplaintTypeName,
        COALESCE(p.priority, c.Priority) AS HermesPriorityName,
        COALESCE(ce.Name, c.commonerror) AS HermesCommonErrorName
    FROM dbo.Complaint_Mst_Tbl AS c WITH (NOLOCK)
    LEFT JOIN dbo.Area_Mst_Tbl AS a WITH (NOLOCK)
        ON ISNULL(a.IsDeleted, 0) = 0
       AND (a.ID = c.AreaID OR a.Name = c.AreaID)
    LEFT JOIN dbo.ComplaintType_Mst_Tbl AS ct WITH (NOLOCK)
        ON ISNULL(ct.IsDeleted, 0) = 0
       AND (ct.ID = c.ComplaintTypeID OR ct.Name = c.ComplaintTypeID)
    LEFT JOIN dbo.priority_mst AS p WITH (NOLOCK)
        ON ISNULL(p.IsDeleted, 0) = 0
       AND (p.ID = c.Priority OR p.priority = c.Priority)
    LEFT JOIN dbo.CommonErrors AS ce WITH (NOLOCK)
        ON ISNULL(ce.IsDeleted, 0) = 0
       AND (ce.ID = c.commonerror OR ce.Name = c.commonerror)
    WHERE c.ID = @TicketID
      AND ISNULL(c.IsDeleted, 0) = 0;

    /* Result 2: previous Hermes runs/responses. */
    SELECT TOP (@HistoryRows)
        r.*
    FROM dbo.Hermes_L2_Response_Trn_Tbl AS r WITH (NOLOCK)
    WHERE r.TicketID = @TicketID
      AND r.IsDeleted = 0
    ORDER BY r.CreatedOn DESC, r.AttemptNo DESC;

    /* Result 3: recent SQL actions for this ticket. */
    SELECT TOP (@HistoryRows * 20)
        a.*
    FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl AS a WITH (NOLOCK)
    WHERE a.TicketID = @TicketID
      AND a.IsDeleted = 0
    ORDER BY a.CreatedOn DESC, a.ActionNo DESC;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Get_Run_Usp
(
    @RunID varchar(36)
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT r.*
    FROM dbo.Hermes_L2_Response_Trn_Tbl AS r WITH (NOLOCK)
    WHERE r.ID = @RunID
      AND r.IsDeleted = 0;

    SELECT a.*
    FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl AS a WITH (NOLOCK)
    WHERE a.RunID = @RunID
      AND a.IsDeleted = 0
    ORDER BY a.ActionNo;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Get_Reference_Documents_Usp
(
    @SearchText varchar(500) = NULL,
    @Area       varchar(200) = NULL,
    @TopN       int = 50
)
AS
BEGIN
    SET NOCOUNT ON;

    IF @TopN IS NULL OR @TopN < 1 SET @TopN = 50;
    IF @TopN > 500 SET @TopN = 500;

    SELECT TOP (@TopN)
        ID,
        Name,
        versionno,
        Description,
        releasedate,
        document,
        DOCXDocument,
        documenttype,
        srno,
        ModifiedOn
    FROM dbo.systemreferencedocuments WITH (NOLOCK)
    WHERE ISNULL(IsDeleted, 0) = 0
      AND
      (
          NULLIF(LTRIM(RTRIM(@SearchText)), '') IS NULL
          OR CHARINDEX(LOWER(@SearchText), LOWER(ISNULL(Name, ''))) > 0
          OR CHARINDEX(LOWER(@SearchText), LOWER(ISNULL(Description, ''))) > 0
          OR CHARINDEX(LOWER(@SearchText), LOWER(ISNULL(documenttype, ''))) > 0
      )
      AND
      (
          NULLIF(LTRIM(RTRIM(@Area)), '') IS NULL
          OR CHARINDEX(LOWER(@Area), LOWER(ISNULL(Name, ''))) > 0
          OR CHARINDEX(LOWER(@Area), LOWER(ISNULL(Description, ''))) > 0
      )
    ORDER BY ISNULL(srno, 2147483647), Name, ModifiedOn DESC;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Find_SQL_Objects_Usp
(
    @DatabaseName sysname,
    @SearchText   nvarchar(4000),
    @ObjectType   varchar(30) = NULL,
    @TopN         int = 100
)
AS
BEGIN
    SET NOCOUNT ON;

    IF DB_ID(@DatabaseName) IS NULL
    BEGIN
        RAISERROR('Database does not exist on the current SQL Server.', 16, 1);
        RETURN;
    END;

    IF NULLIF(LTRIM(RTRIM(@SearchText)), N'') IS NULL
    BEGIN
        RAISERROR('SearchText is required.', 16, 1);
        RETURN;
    END;

    IF @TopN IS NULL OR @TopN < 1 SET @TopN = 100;
    IF @TopN > 1000 SET @TopN = 1000;

    DECLARE @Sql nvarchar(max) =
        N'USE ' + QUOTENAME(@DatabaseName) + N';
        SELECT TOP (@TopN)
            CASE o.type
                WHEN ''U''  THEN ''TABLE''
                WHEN ''V''  THEN ''VIEW''
                WHEN ''P''  THEN ''PROCEDURE''
                WHEN ''PC'' THEN ''PROCEDURE''
                WHEN ''FN'' THEN ''FUNCTION''
                WHEN ''IF'' THEN ''FUNCTION''
                WHEN ''TF'' THEN ''FUNCTION''
                WHEN ''TR'' THEN ''TRIGGER''
                ELSE o.type_desc
            END AS ObjectType,
            s.name AS SchemaName,
            o.name AS ObjectName,
            c.name AS ColumnName,
            CASE
                WHEN CHARINDEX(LOWER(@SearchText), LOWER(o.name)) > 0 THEN ''OBJECT_NAME''
                WHEN c.name IS NOT NULL
                 AND CHARINDEX(LOWER(@SearchText), LOWER(c.name)) > 0 THEN ''COLUMN_NAME''
                WHEN sm.definition IS NOT NULL
                 AND CHARINDEX(LOWER(@SearchText), LOWER(sm.definition)) > 0 THEN ''DEFINITION''
                ELSE ''OTHER''
            END AS MatchedOn,
            o.modify_date AS ObjectModifiedOn
        FROM sys.objects AS o
        JOIN sys.schemas AS s ON s.schema_id = o.schema_id
        LEFT JOIN sys.columns AS c ON c.object_id = o.object_id
        LEFT JOIN sys.sql_modules AS sm ON sm.object_id = o.object_id
        WHERE o.is_ms_shipped = 0
          AND
          (
              CHARINDEX(LOWER(@SearchText), LOWER(o.name)) > 0
              OR (c.name IS NOT NULL
                  AND CHARINDEX(LOWER(@SearchText), LOWER(c.name)) > 0)
              OR (sm.definition IS NOT NULL
                  AND CHARINDEX(LOWER(@SearchText), LOWER(sm.definition)) > 0)
          )
          AND
          (
              NULLIF(@ObjectType, '''') IS NULL
              OR UPPER(@ObjectType) =
                 CASE o.type
                    WHEN ''U''  THEN ''TABLE''
                    WHEN ''V''  THEN ''VIEW''
                    WHEN ''P''  THEN ''PROCEDURE''
                    WHEN ''PC'' THEN ''PROCEDURE''
                    WHEN ''FN'' THEN ''FUNCTION''
                    WHEN ''IF'' THEN ''FUNCTION''
                    WHEN ''TF'' THEN ''FUNCTION''
                    WHEN ''TR'' THEN ''TRIGGER''
                    ELSE UPPER(o.type_desc)
                 END
          )
        ORDER BY
            CASE
                WHEN CHARINDEX(LOWER(@SearchText), LOWER(o.name)) > 0 THEN 1
                WHEN c.name IS NOT NULL
                 AND CHARINDEX(LOWER(@SearchText), LOWER(c.name)) > 0 THEN 2
                ELSE 3
            END,
            s.name,
            o.name,
            c.column_id;';

    EXEC sys.sp_executesql
        @Sql,
        N'@SearchText nvarchar(4000), @ObjectType varchar(30), @TopN int',
        @SearchText = @SearchText,
        @ObjectType = @ObjectType,
        @TopN = @TopN;
END;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Get_SQL_Object_Definition_Usp
(
    @DatabaseName sysname,
    @SchemaName   sysname = 'dbo',
    @ObjectName   sysname
)
AS
BEGIN
    SET NOCOUNT ON;

    IF DB_ID(@DatabaseName) IS NULL
    BEGIN
        RAISERROR('Database does not exist on the current SQL Server.', 16, 1);
        RETURN;
    END;

    IF NULLIF(@ObjectName, '') IS NULL
    BEGIN
        RAISERROR('ObjectName is required.', 16, 1);
        RETURN;
    END;

    DECLARE @TwoPartName nvarchar(600) =
        QUOTENAME(ISNULL(NULLIF(@SchemaName, ''), 'dbo')) + N'.' + QUOTENAME(@ObjectName);

    DECLARE @Sql nvarchar(max) =
        N'USE ' + QUOTENAME(@DatabaseName) + N';
        DECLARE @ObjectID int = OBJECT_ID(@TwoPartName);

        IF @ObjectID IS NULL
        BEGIN
            RAISERROR(''Object not found in requested database.'', 16, 1);
            RETURN;
        END;

        /* Result 1: object metadata. */
        SELECT
            o.object_id,
            s.name AS SchemaName,
            o.name AS ObjectName,
            o.type,
            o.type_desc,
            o.create_date,
            o.modify_date
        FROM sys.objects AS o
        JOIN sys.schemas AS s ON s.schema_id = o.schema_id
        WHERE o.object_id = @ObjectID;

        /* Result 2: columns. */
        SELECT
            c.column_id,
            c.name AS ColumnName,
            t.name AS DataType,
            c.max_length,
            c.precision,
            c.scale,
            c.is_nullable,
            c.is_identity,
            c.is_computed,
            dc.definition AS DefaultDefinition,
            cc.definition AS ComputedDefinition
        FROM sys.columns AS c
        JOIN sys.types AS t ON t.user_type_id = c.user_type_id
        LEFT JOIN sys.default_constraints AS dc ON dc.object_id = c.default_object_id
        LEFT JOIN sys.computed_columns AS cc
            ON cc.object_id = c.object_id
           AND cc.column_id = c.column_id
        WHERE c.object_id = @ObjectID
        ORDER BY c.column_id;

        /* Result 3: stored-procedure/function parameters. */
        SELECT
            p.parameter_id,
            p.name AS ParameterName,
            TYPE_NAME(p.user_type_id) AS DataType,
            p.max_length,
            p.precision,
            p.scale,
            p.is_output
        FROM sys.parameters AS p
        WHERE p.object_id = @ObjectID
        ORDER BY p.parameter_id;

        /* Result 4: SQL definition for procedures/views/functions/triggers. */
        SELECT OBJECT_DEFINITION(@ObjectID) AS ObjectDefinition;

        /* Result 5: indexes. */
        SELECT
            i.index_id,
            i.name AS IndexName,
            i.type_desc,
            i.is_unique,
            i.is_primary_key,
            i.has_filter,
            i.filter_definition,
            ic.key_ordinal,
            ic.is_included_column,
            c.name AS ColumnName
        FROM sys.indexes AS i
        LEFT JOIN sys.index_columns AS ic
            ON ic.object_id = i.object_id
           AND ic.index_id = i.index_id
        LEFT JOIN sys.columns AS c
            ON c.object_id = ic.object_id
           AND c.column_id = ic.column_id
        WHERE i.object_id = @ObjectID
        ORDER BY i.index_id, ic.key_ordinal, ic.index_column_id;

        /* Result 6: triggers attached to the object. */
        SELECT
            tr.name AS TriggerName,
            tr.is_disabled,
            OBJECT_DEFINITION(tr.object_id) AS TriggerDefinition
        FROM sys.triggers AS tr
        WHERE tr.parent_id = @ObjectID
        ORDER BY tr.name;';

    EXEC sys.sp_executesql
        @Sql,
        N'@TwoPartName nvarchar(600)',
        @TwoPartName = @TwoPartName;
END;
GO
