/*
Hermes L2 - Tables and indexes
Target database: XStudio_Helpdesk

Design:
- Existing Complaint_Mst_Tbl remains the ticket/workflow master.
- No queue table.
- One Hermes response/run table stores each L2 attempt and structured reply.
- One SQL-action table stores live SQL/SP investigation and mutation evidence.

Generated from the supplied 2026-09-02 schema/SP snapshots.
Live Helpdesk workflow values must be discovered before binding status names.
*/

SET NOCOUNT ON;
SET XACT_ABORT ON;
GO

IF OBJECT_ID('dbo.Hermes_L2_Response_Trn_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_L2_Response_Trn_Tbl
    (
        ID                       varchar(36)    NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_ID DEFAULT (NEWID()),
        TicketID                 varchar(36)    NOT NULL,
        AttemptNo                int            NOT NULL,
        WorkerID                 varchar(200)   NULL,

        ProcessStatus            varchar(30)    NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_ProcessStatus DEFAULT ('CLAIMED'),
        IsActive                 bit            NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_IsActive DEFAULT (1),

        Route                    varchar(100)   NULL,
        ResponseType             varchar(30)    NULL,

        ProblemSummary           nvarchar(max)  NULL,
        Findings                 nvarchar(max)  NULL,
        RootCause                nvarchar(max)  NULL,
        Resolution               nvarchar(max)  NULL,
        ReplyText                nvarchar(max)  NULL,

        InvestigationJson        nvarchar(max)  NULL,
        ActionsTakenJson         nvarchar(max)  NULL,

        RequiresUserInput        bit            NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_RequiresUserInput DEFAULT (0),
        EscalateToL3             bit            NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_EscalateToL3 DEFAULT (0),
        IsResolved               bit            NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_IsResolved DEFAULT (0),

        TicketModifiedOnSeen     datetime        NULL,
        ClaimedOn                datetime        NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_ClaimedOn DEFAULT (GETDATE()),
        HeartbeatOn              datetime        NULL,
        NextEligibleOn           datetime        NULL,
        CompletedOn              datetime        NULL,
        ErrorMessage             nvarchar(max)  NULL,

        CreatedBy                varchar(36)    NULL,
        ModifiedBy               varchar(36)    NULL,
        CreatedOn                datetime       NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_CreatedOn DEFAULT (GETDATE()),
        ModifiedOn               datetime       NULL,
        IsDeleted               bit            NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_IsDeleted DEFAULT (0),
        IsSystem                bit            NOT NULL
            CONSTRAINT DF_Hermes_L2_Response_IsSystem DEFAULT (0),
        HostAddress             varchar(100)   NULL,
        Source                  varchar(20)    NULL,

        CONSTRAINT PK_Hermes_L2_Response_Trn PRIMARY KEY CLUSTERED (ID)
    );
END;
GO

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID('dbo.Hermes_L2_Response_Trn_Tbl')
      AND name = 'UX_Hermes_L2_Response_ActiveTicket'
)
BEGIN
    CREATE UNIQUE NONCLUSTERED INDEX UX_Hermes_L2_Response_ActiveTicket
        ON dbo.Hermes_L2_Response_Trn_Tbl(TicketID)
        WHERE IsActive = 1 AND IsDeleted = 0;
END;
GO

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID('dbo.Hermes_L2_Response_Trn_Tbl')
      AND name = 'IX_Hermes_L2_Response_TicketHistory'
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Hermes_L2_Response_TicketHistory
        ON dbo.Hermes_L2_Response_Trn_Tbl(TicketID, CreatedOn DESC, AttemptNo DESC);
END;
GO

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID('dbo.Hermes_L2_Response_Trn_Tbl')
      AND name = 'IX_Hermes_L2_Response_RunState'
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Hermes_L2_Response_RunState
        ON dbo.Hermes_L2_Response_Trn_Tbl(IsActive, ProcessStatus, NextEligibleOn, HeartbeatOn);
END;
GO

IF OBJECT_ID('dbo.Hermes_L2_SQL_Action_Trn_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_L2_SQL_Action_Trn_Tbl
    (
        ID                  varchar(36)    NOT NULL
            CONSTRAINT DF_Hermes_L2_SQL_Action_ID DEFAULT (NEWID()),
        RunID               varchar(36)    NOT NULL,
        TicketID            varchar(36)    NOT NULL,
        ActionNo            int            NOT NULL,

        ActionType          varchar(30)    NULL,
        DatabaseName        varchar(200)   NULL,
        SchemaName          varchar(200)   NULL,
        ObjectName          varchar(500)   NULL,
        OperationName       varchar(500)   NULL,
        Purpose             nvarchar(1000) NULL,

        SqlText             nvarchar(max)  NULL,
        ParametersJson      nvarchar(max)  NULL,
        BeforeJson          nvarchar(max)  NULL,
        AfterJson           nvarchar(max)  NULL,

        Status              varchar(30)    NOT NULL,
        RowsAffected        int            NULL,
        StartedOn           datetime       NOT NULL
            CONSTRAINT DF_Hermes_L2_SQL_Action_StartedOn DEFAULT (GETDATE()),
        CompletedOn         datetime       NULL,

        ErrorNumber         int            NULL,
        ErrorMessage        nvarchar(max)  NULL,

        CreatedBy           varchar(36)    NULL,
        ModifiedBy          varchar(36)    NULL,
        CreatedOn           datetime       NOT NULL
            CONSTRAINT DF_Hermes_L2_SQL_Action_CreatedOn DEFAULT (GETDATE()),
        ModifiedOn          datetime       NULL,
        IsDeleted           bit            NOT NULL
            CONSTRAINT DF_Hermes_L2_SQL_Action_IsDeleted DEFAULT (0),
        Source              varchar(20)    NULL,

        CONSTRAINT PK_Hermes_L2_SQL_Action_Trn PRIMARY KEY CLUSTERED (ID)
    );
END;
GO

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID('dbo.Hermes_L2_SQL_Action_Trn_Tbl')
      AND name = 'UX_Hermes_L2_SQL_Action_RunActionNo'
)
BEGIN
    CREATE UNIQUE NONCLUSTERED INDEX UX_Hermes_L2_SQL_Action_RunActionNo
        ON dbo.Hermes_L2_SQL_Action_Trn_Tbl(RunID, ActionNo)
        WHERE IsDeleted = 0;
END;
GO

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID('dbo.Hermes_L2_SQL_Action_Trn_Tbl')
      AND name = 'IX_Hermes_L2_SQL_Action_Ticket'
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Hermes_L2_SQL_Action_Ticket
        ON dbo.Hermes_L2_SQL_Action_Trn_Tbl(TicketID, CreatedOn DESC);
END;
GO

/*
Hermes_L3_Escalation_Trn_Tbl
Closes a real gap: Hermes_L2_Escalate_L3_Usp today only writes a text reply into
Complaint_Mst_Tbl.SupportExecutiveRemarks / Hermes_L2_Response_Trn_Tbl -- there is no
queryable table a human L3 agent can pull a work queue from, with the full structured
investigation package (problem/findings/root cause/evidence/views checked) and their own
assign -> in-progress -> resolved workflow state, separate from the ticket's own
Status/AskStatus. One row per escalation event (snapshot at escalation time, not a live
mirror of the run).
*/
IF OBJECT_ID('dbo.Hermes_L3_Escalation_Trn_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_L3_Escalation_Trn_Tbl
    (
        ID                    varchar(36)    NOT NULL
            CONSTRAINT DF_Hermes_L3_Escalation_ID DEFAULT (NEWID()),
        RunID                 varchar(36)    NOT NULL,
        TicketID              varchar(36)    NOT NULL,
        TicketNo              varchar(100)   NULL,

        EscalatedOn           datetime       NOT NULL
            CONSTRAINT DF_Hermes_L3_Escalation_EscalatedOn DEFAULT (GETDATE()),
        EscalatedByBot        varchar(200)   NULL,

        ProblemSummary        nvarchar(max)  NULL,
        Findings              nvarchar(max)  NULL,
        RootCause             nvarchar(max)  NULL,
        SuggestedAction       nvarchar(max)  NULL,
        ReplyText             nvarchar(max)  NULL,

        InvestigationJson     nvarchar(max)  NULL,
        EvidenceViewsJson     nvarchar(max)  NULL,

        L3Status              varchar(30)    NOT NULL
            CONSTRAINT DF_Hermes_L3_Escalation_L3Status DEFAULT ('Open'),
        AssignedToUserID      varchar(36)    NULL,
        AssignedOn            datetime       NULL,
        L3Remarks             nvarchar(max)  NULL,
        L3ResolutionSummary   nvarchar(max)  NULL,
        ResolvedByUserID      varchar(36)    NULL,
        ResolvedOn            datetime       NULL,

        CreatedBy             varchar(36)    NULL,
        ModifiedBy            varchar(36)    NULL,
        CreatedOn              datetime      NOT NULL
            CONSTRAINT DF_Hermes_L3_Escalation_CreatedOn DEFAULT (GETDATE()),
        ModifiedOn             datetime      NULL,
        IsDeleted               bit          NOT NULL
            CONSTRAINT DF_Hermes_L3_Escalation_IsDeleted DEFAULT (0),
        Source                  varchar(20)  NULL,

        CONSTRAINT PK_Hermes_L3_Escalation_Trn PRIMARY KEY CLUSTERED (ID),
        CONSTRAINT CK_Hermes_L3_Escalation_L3Status
            CHECK (L3Status IN ('Open', 'Assigned', 'InProgress', 'Resolved', 'Rejected'))
    );
END;
GO

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID('dbo.Hermes_L3_Escalation_Trn_Tbl')
      AND name = 'IX_Hermes_L3_Escalation_Queue'
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Hermes_L3_Escalation_Queue
        ON dbo.Hermes_L3_Escalation_Trn_Tbl(L3Status, EscalatedOn)
        WHERE IsDeleted = 0;
END;
GO

IF NOT EXISTS
(
    SELECT 1
    FROM sys.indexes
    WHERE object_id = OBJECT_ID('dbo.Hermes_L3_Escalation_Trn_Tbl')
      AND name = 'IX_Hermes_L3_Escalation_Ticket'
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Hermes_L3_Escalation_Ticket
        ON dbo.Hermes_L3_Escalation_Trn_Tbl(TicketID, EscalatedOn DESC);
END;
GO

/* ============================================================================
   Advanced Helpdesk enhancements (2026-09-03, user's explicit request):
   activity/work-log timeline, knowledge base + solution linking, problem
   management, root-cause taxonomy, CSAT/reopen feedback, escalation rules.
   Modeled on what mature ITSM systems (ServiceNow/Zendesk/Jira Service
   Management class) carry that this Helpdesk didn't -- see the design
   discussion this was built from for the full comparison.
   ============================================================================ */

/*
Hermes_Ticket_Activity_Trn_Tbl
The single highest-leverage gap: every touch on a ticket as its own
timestamped row (note, status change, escalation, resolution, reopen),
not one overwritable SupportExecutiveRemarks field. Human engineers AND
bots both write here going forward -- this is the real work log a human
reviewing ticket history actually needs.
*/
IF OBJECT_ID('dbo.Hermes_Ticket_Activity_Trn_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_Ticket_Activity_Trn_Tbl
    (
        ID                varchar(36)    NOT NULL
            CONSTRAINT DF_Hermes_Ticket_Activity_ID DEFAULT (NEWID()),
        TicketID          varchar(36)    NOT NULL,
        RunID             varchar(36)    NULL,
        ActivityType      varchar(30)    NOT NULL,
        ActorType         varchar(20)    NOT NULL
            CONSTRAINT DF_Hermes_Ticket_Activity_ActorType DEFAULT ('Bot'),
        ActorName         varchar(200)   NULL,
        NoteText          nvarchar(max)  NULL,
        OldValue          nvarchar(500)  NULL,
        NewValue          nvarchar(500)  NULL,
        IsCustomerVisible bit            NOT NULL
            CONSTRAINT DF_Hermes_Ticket_Activity_CustomerVisible DEFAULT (0),

        CreatedBy         varchar(36)    NULL,
        CreatedOn         datetime       NOT NULL
            CONSTRAINT DF_Hermes_Ticket_Activity_CreatedOn DEFAULT (GETDATE()),
        IsDeleted         bit            NOT NULL
            CONSTRAINT DF_Hermes_Ticket_Activity_IsDeleted DEFAULT (0),
        Source            varchar(20)    NULL,

        CONSTRAINT PK_Hermes_Ticket_Activity_Trn PRIMARY KEY CLUSTERED (ID),
        CONSTRAINT CK_Hermes_Ticket_Activity_Type
            CHECK (ActivityType IN ('Note', 'StatusChange', 'Escalation', 'Resolution', 'Reopen', 'SolutionLinked', 'ProblemLinked')),
        CONSTRAINT CK_Hermes_Ticket_Activity_ActorType
            CHECK (ActorType IN ('Bot', 'Human', 'System'))
    );
END;
GO

IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE object_id = OBJECT_ID('dbo.Hermes_Ticket_Activity_Trn_Tbl') AND name = 'IX_Hermes_Ticket_Activity_Ticket')
    CREATE NONCLUSTERED INDEX IX_Hermes_Ticket_Activity_Ticket
        ON dbo.Hermes_Ticket_Activity_Trn_Tbl(TicketID, CreatedOn ASC)
        WHERE IsDeleted = 0;
GO

/*
Hermes_Root_Cause_Category_Mst_Tbl
Controlled taxonomy replacing free-text SuspectedCause for reporting
("40% of tickets this quarter were X"). Self-referencing for a shallow
hierarchy. Seeded with categories observed across real investigations this
session, not invented from nothing.
*/
IF OBJECT_ID('dbo.Hermes_Root_Cause_Category_Mst_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_Root_Cause_Category_Mst_Tbl
    (
        ID                  varchar(36)   NOT NULL
            CONSTRAINT DF_Hermes_RCC_ID DEFAULT (NEWID()),
        CategoryName        varchar(200)  NOT NULL,
        ParentCategoryID    varchar(36)   NULL,
        Description         nvarchar(500) NULL,
        IsActive            bit           NOT NULL
            CONSTRAINT DF_Hermes_RCC_IsActive DEFAULT (1),
        CreatedOn           datetime      NOT NULL
            CONSTRAINT DF_Hermes_RCC_CreatedOn DEFAULT (GETDATE()),
        IsDeleted           bit           NOT NULL
            CONSTRAINT DF_Hermes_RCC_IsDeleted DEFAULT (0),

        CONSTRAINT PK_Hermes_Root_Cause_Category PRIMARY KEY CLUSTERED (ID),
        CONSTRAINT UQ_Hermes_RCC_Name UNIQUE (CategoryName)
    );
END;
GO

INSERT INTO dbo.Hermes_Root_Cause_Category_Mst_Tbl (CategoryName, Description)
SELECT v.CategoryName, v.Description
FROM (VALUES
    ('Data Entry Error', 'Value entered incorrectly by an operator, not a system defect'),
    ('SAP Integration Failure', 'API/posting call failed, was never sent, or SAP rejected it'),
    ('Sensor/Data Sync Delay', 'Real event happened but the record/view lags or is temporarily out of sync'),
    ('Configuration Gap', 'A limit, mapping, or workflow rule was never configured for this case'),
    ('Genuine Process Deviation', 'The underlying production/process event was real and outside normal range'),
    ('Duplicate/Known Issue', 'Same root cause as an existing Problem record'),
    ('User Training Gap', 'System behaved correctly; requester misunderstood the workflow'),
    ('Software Defect', 'Confirmed bug in a view/SP/application logic (e.g. the Heat_Details_Vw subquery bug)'),
    ('Infrastructure/Environment', 'Investigation itself was blocked by tooling/environment, not a ticket-domain issue'),
    ('Not Part of L2', 'Ticket type is out of scope for automated L2 (e.g. Request for Customization)')
) AS v(CategoryName, Description)
WHERE NOT EXISTS (SELECT 1 FROM dbo.Hermes_Root_Cause_Category_Mst_Tbl WHERE CategoryName = v.CategoryName);
GO

/*
Hermes_Solution_Article_Mst_Tbl + Hermes_Ticket_Solution_Link_Tbl
Knowledge base: a reusable, searchable "known issue -> known fix" record,
separate from any one ticket. UsageCount lets a future router prefer
proven solutions over re-investigating from scratch.
*/
IF OBJECT_ID('dbo.Hermes_Solution_Article_Mst_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_Solution_Article_Mst_Tbl
    (
        ID                  varchar(36)   NOT NULL
            CONSTRAINT DF_Hermes_Solution_ID DEFAULT (NEWID()),
        Title               nvarchar(300) NOT NULL,
        ProblemSummary      nvarchar(max) NULL,
        RootCause           nvarchar(max) NULL,
        ResolutionSteps     nvarchar(max) NOT NULL,
        RootCauseCategoryID varchar(36)   NULL,
        Route               varchar(100)  NULL,
        RelatedViewsJson    nvarchar(max) NULL,
        Tags                nvarchar(500) NULL,
        UsageCount          int           NOT NULL
            CONSTRAINT DF_Hermes_Solution_UsageCount DEFAULT (0),
        IsActive            bit           NOT NULL
            CONSTRAINT DF_Hermes_Solution_IsActive DEFAULT (1),

        CreatedBy           varchar(36)   NULL,
        ModifiedBy          varchar(36)   NULL,
        CreatedOn           datetime      NOT NULL
            CONSTRAINT DF_Hermes_Solution_CreatedOn DEFAULT (GETDATE()),
        ModifiedOn          datetime      NULL,
        IsDeleted           bit           NOT NULL
            CONSTRAINT DF_Hermes_Solution_IsDeleted DEFAULT (0),
        Source              varchar(20)   NULL,

        CONSTRAINT PK_Hermes_Solution_Article PRIMARY KEY CLUSTERED (ID)
    );
END;
GO

IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE object_id = OBJECT_ID('dbo.Hermes_Solution_Article_Mst_Tbl') AND name = 'IX_Hermes_Solution_Route')
    CREATE NONCLUSTERED INDEX IX_Hermes_Solution_Route
        ON dbo.Hermes_Solution_Article_Mst_Tbl(Route, IsActive)
        WHERE IsDeleted = 0;
GO

IF OBJECT_ID('dbo.Hermes_Ticket_Solution_Link_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_Ticket_Solution_Link_Tbl
    (
        ID           varchar(36)   NOT NULL
            CONSTRAINT DF_Hermes_TSL_ID DEFAULT (NEWID()),
        TicketID     varchar(36)   NOT NULL,
        SolutionID   varchar(36)   NOT NULL,
        RunID        varchar(36)   NULL,
        WasHelpful   bit           NULL,
        LinkedOn     datetime      NOT NULL
            CONSTRAINT DF_Hermes_TSL_LinkedOn DEFAULT (GETDATE()),
        LinkedBy     varchar(36)   NULL,
        IsDeleted    bit           NOT NULL
            CONSTRAINT DF_Hermes_TSL_IsDeleted DEFAULT (0),

        CONSTRAINT PK_Hermes_Ticket_Solution_Link PRIMARY KEY CLUSTERED (ID)
    );
END;
GO

IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE object_id = OBJECT_ID('dbo.Hermes_Ticket_Solution_Link_Tbl') AND name = 'IX_Hermes_TSL_Solution')
    CREATE NONCLUSTERED INDEX IX_Hermes_TSL_Solution
        ON dbo.Hermes_Ticket_Solution_Link_Tbl(SolutionID, LinkedOn DESC)
        WHERE IsDeleted = 0;
GO

/*
Hermes_Problem_Mst_Tbl + Hermes_Problem_Ticket_Link_Tbl
Problem management: group N recurring incidents under one root cause so
it gets fixed once instead of re-investigated every time it recurs.
*/
IF OBJECT_ID('dbo.Hermes_Problem_Mst_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_Problem_Mst_Tbl
    (
        ID                  varchar(36)   NOT NULL
            CONSTRAINT DF_Hermes_Problem_ID DEFAULT (NEWID()),
        Title               nvarchar(300) NOT NULL,
        RootCauseSummary    nvarchar(max) NULL,
        RootCauseCategoryID varchar(36)   NULL,
        Status              varchar(30)   NOT NULL
            CONSTRAINT DF_Hermes_Problem_Status DEFAULT ('Open'),
        IdentifiedOn        datetime      NOT NULL
            CONSTRAINT DF_Hermes_Problem_IdentifiedOn DEFAULT (GETDATE()),
        ResolvedOn          datetime      NULL,
        SolutionID          varchar(36)   NULL,

        CreatedBy           varchar(36)   NULL,
        ModifiedBy          varchar(36)   NULL,
        CreatedOn           datetime      NOT NULL
            CONSTRAINT DF_Hermes_Problem_CreatedOn DEFAULT (GETDATE()),
        ModifiedOn          datetime      NULL,
        IsDeleted           bit           NOT NULL
            CONSTRAINT DF_Hermes_Problem_IsDeleted DEFAULT (0),

        CONSTRAINT PK_Hermes_Problem PRIMARY KEY CLUSTERED (ID),
        CONSTRAINT CK_Hermes_Problem_Status CHECK (Status IN ('Open', 'RootCauseIdentified', 'Resolved'))
    );
END;
GO

IF OBJECT_ID('dbo.Hermes_Problem_Ticket_Link_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_Problem_Ticket_Link_Tbl
    (
        ID          varchar(36)   NOT NULL
            CONSTRAINT DF_Hermes_PTL_ID DEFAULT (NEWID()),
        ProblemID   varchar(36)   NOT NULL,
        TicketID    varchar(36)   NOT NULL,
        LinkedOn    datetime      NOT NULL
            CONSTRAINT DF_Hermes_PTL_LinkedOn DEFAULT (GETDATE()),
        LinkedBy    varchar(36)   NULL,
        IsDeleted   bit           NOT NULL
            CONSTRAINT DF_Hermes_PTL_IsDeleted DEFAULT (0),

        CONSTRAINT PK_Hermes_Problem_Ticket_Link PRIMARY KEY CLUSTERED (ID)
    );
END;
GO

IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE object_id = OBJECT_ID('dbo.Hermes_Problem_Ticket_Link_Tbl') AND name = 'UX_Hermes_PTL_ProblemTicket')
    CREATE UNIQUE NONCLUSTERED INDEX UX_Hermes_PTL_ProblemTicket
        ON dbo.Hermes_Problem_Ticket_Link_Tbl(ProblemID, TicketID)
        WHERE IsDeleted = 0;
GO

/*
Hermes_Ticket_Feedback_Trn_Tbl
CSAT + reopen tracking. A resolved ticket today is just trusted -- this is
the confirmation loop a real support org relies on. ReopenedFromTicketID
self-references the prior ticket when a "fixed" issue comes back.
*/
IF OBJECT_ID('dbo.Hermes_Ticket_Feedback_Trn_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_Ticket_Feedback_Trn_Tbl
    (
        ID                    varchar(36)   NOT NULL
            CONSTRAINT DF_Hermes_Feedback_ID DEFAULT (NEWID()),
        TicketID              varchar(36)   NOT NULL,
        SatisfactionRating    int           NULL,
        FeedbackText          nvarchar(max) NULL,
        IsReopen              bit           NOT NULL
            CONSTRAINT DF_Hermes_Feedback_IsReopen DEFAULT (0),
        ReopenedFromTicketID  varchar(36)   NULL,

        SubmittedBy           varchar(36)   NULL,
        SubmittedOn           datetime      NOT NULL
            CONSTRAINT DF_Hermes_Feedback_SubmittedOn DEFAULT (GETDATE()),
        IsDeleted             bit           NOT NULL
            CONSTRAINT DF_Hermes_Feedback_IsDeleted DEFAULT (0),

        CONSTRAINT PK_Hermes_Ticket_Feedback PRIMARY KEY CLUSTERED (ID),
        CONSTRAINT CK_Hermes_Feedback_Rating CHECK (SatisfactionRating IS NULL OR SatisfactionRating BETWEEN 1 AND 5)
    );
END;
GO

/*
Hermes_Escalation_Rule_Mst_Tbl
The config an escalation matrix actually needs: priority x elapsed time ->
who/what gets notified. Separate from Hermes_L3_Escalation_Trn_Tbl, which
is the RECORD of an escalation that already happened, not the rule that
should trigger one. Not yet wired to any SP/cron -- config only for now.
*/
IF OBJECT_ID('dbo.Hermes_Escalation_Rule_Mst_Tbl', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Hermes_Escalation_Rule_Mst_Tbl
    (
        ID                    varchar(36)   NOT NULL
            CONSTRAINT DF_Hermes_EscRule_ID DEFAULT (NEWID()),
        PriorityID            varchar(36)   NOT NULL,
        TriggerAfterMinutes   int           NOT NULL,
        EscalateToRole        varchar(200)  NULL,
        EscalateToUserID      varchar(36)   NULL,
        NotifyMethod          varchar(30)   NULL,
        IsActive              bit           NOT NULL
            CONSTRAINT DF_Hermes_EscRule_IsActive DEFAULT (1),

        CreatedOn             datetime      NOT NULL
            CONSTRAINT DF_Hermes_EscRule_CreatedOn DEFAULT (GETDATE()),
        IsDeleted             bit           NOT NULL
            CONSTRAINT DF_Hermes_EscRule_IsDeleted DEFAULT (0),

        CONSTRAINT PK_Hermes_Escalation_Rule PRIMARY KEY CLUSTERED (ID)
    );
END;
GO

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
/*
  Pipeline continuation hardening for ResponseType='UPDATE'.

  Hermes_L2_Publish_Response_Usp supports @NextEligibleOn, but the current CLI
  path does not expose it. An UPDATE with NextEligibleOn=NULL therefore becomes
  permanently ineligible unless the requester edits the ticket, even though
  UPDATE explicitly means useful progress without a final outcome.

  This trigger supplies a conservative 15-minute continuation window only when
  an UPDATE is completed with no explicit NextEligibleOn. QUESTION, RESOLUTION,
  L3_ESCALATION and NEEDS_HUMAN_ACTION are untouched.
*/
SET ANSI_NULLS ON;
SET QUOTED_IDENTIFIER ON;
GO

CREATE OR ALTER TRIGGER dbo.Hermes_L2_Default_Update_Continuation_Trg
ON dbo.Hermes_L2_Response_Trn_Tbl
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE r
    SET
        NextEligibleOn = DATEADD(MINUTE, 15, GETDATE()),
        ModifiedOn = GETDATE()
    FROM dbo.Hermes_L2_Response_Trn_Tbl AS r
    INNER JOIN inserted AS i ON i.ID = r.ID
    WHERE i.ResponseType = 'UPDATE'
      AND i.ProcessStatus = 'COMPLETED'
      AND i.IsActive = 0
      AND i.IsDeleted = 0
      AND i.NextEligibleOn IS NULL
      AND r.NextEligibleOn IS NULL;
END;
GO
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
