SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
GO

CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Discover_Helpdesk_Workflow_Usp
AS
BEGIN
    SET NOCOUNT ON;

    /* Result 1: observed live ticket workflow values. */
    SELECT
        Status,
        AskStatus,
        messages,
        COUNT_BIG(1) AS TicketCount,
        MIN(CreatedOn) AS FirstSeenOn,
        MAX(ISNULL(ModifiedOn, CreatedOn)) AS LastSeenOn
    FROM dbo.Complaint_Mst_Tbl WITH (NOLOCK)
    WHERE ISNULL(IsDeleted, 0) = 0
    GROUP BY Status, AskStatus, messages
    ORDER BY TicketCount DESC, Status, AskStatus, messages;

    /* Result 2: priority IDs and display values. */
    SELECT ID, priority, IsDeleted, ModifiedOn
    FROM dbo.priority_mst WITH (NOLOCK)
    ORDER BY
        CASE LOWER(ISNULL(priority, ''))
            WHEN 'critical' THEN 1
            WHEN 'high priority' THEN 2
            WHEN 'standard' THEN 3
            ELSE 4
        END,
        priority;

    /* Result 3: complaint types. */
    SELECT ID, Name, subarea, IsDeleted, ModifiedOn
    FROM dbo.ComplaintType_Mst_Tbl WITH (NOLOCK)
    ORDER BY Name;

    /* Result 4: current SQL modules that touch the ticket table. */
    SELECT
        OBJECT_SCHEMA_NAME(m.object_id) AS SchemaName,
        OBJECT_NAME(m.object_id) AS ObjectName,
        o.type_desc AS ObjectType,
        m.definition
    FROM sys.sql_modules AS m
    JOIN sys.objects AS o ON o.object_id = m.object_id
    WHERE m.definition LIKE '%Complaint_Mst_Tbl%'
       OR m.definition LIKE '%AskStatus%'
       OR m.definition LIKE '%SupportExecutiveRemarks%'
       OR m.definition LIKE '%ReplyRemarks%'
    ORDER BY ObjectType, SchemaName, ObjectName;

    /* Result 5: current triggers directly attached to the ticket table. */
    SELECT
        tr.name AS TriggerName,
        tr.is_disabled,
        OBJECT_DEFINITION(tr.object_id) AS TriggerDefinition
    FROM sys.triggers AS tr
    WHERE tr.parent_id = OBJECT_ID('dbo.Complaint_Mst_Tbl')
    ORDER BY tr.name;

    /* Result 6: recent tickets with workflow/reply fields. */
    SELECT TOP (50)
        ID,
        TicketNo,
        AreaID,
        ComplaintTypeID,
        BriefDetails,
        Description,
        Priority,
        Status,
        AskStatus,
        messages,
        Solution,
        SupportExecutiveRemarks,
        AskRemarks,
        ReplyRemarks,
        ssmmessage,
        Soharmessage,
        AssignedUserID,
        CreatedBy,
        CreatedOn,
        ModifiedBy,
        ModifiedOn
    FROM dbo.Complaint_Mst_Tbl WITH (NOLOCK)
    WHERE ISNULL(IsDeleted, 0) = 0
    ORDER BY ISNULL(ModifiedOn, CreatedOn) DESC;
END;
GO
