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

