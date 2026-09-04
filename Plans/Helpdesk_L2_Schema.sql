-- =============================================================================
-- Helpdesk L2 Database Schema for AI-Embedded Helpdesk (Hermes L2)
-- Based on: Helpdesk Plan 1 02092026.md sections 10-11
-- Database: XStudio_Helpdesk (Server: 10.2.6.204)
-- =============================================================================

-- =============================================================================
-- Table: Helpdesk_L2_Run_Trn
-- Purpose: Track each Hermes investigation run per ticket
-- =============================================================================
CREATE TABLE Helpdesk_L2_Run_Trn (
    RunID uniqueidentifier NOT NULL PRIMARY KEY DEFAULT NEWID(),
    TicketID uniqueidentifier NOT NULL,
    RunNo int IDENTITY(1,1) NOT NULL,
    Status varchar(20) NOT NULL DEFAULT 'AI_INVESTIGATING',
    StartedOn datetime NOT NULL DEFAULT GETUTCDATE(),
    CompletedOn datetime NULL,
    ProblemCategory varchar(100) NULL,
    ProblemSubCategory varchar(100) NULL,
    InvestigationSummary nvarchar(MAX) NULL,
    RootCause nvarchar(MAX) NULL,
    Outcome varchar(50) NULL,   -- RESOLVED, ESCALATED_L3, etc.
    Model varchar(100) NULL,
    PromptVersion varchar(50) NULL,
    CONSTRAINT FK_L2Run_Ticket FOREIGN KEY (TicketID) REFERENCES TicketScheme_Mst_Tbl(TicketNo)
);

-- =============================================================================
-- Table: Helpdesk_L2_Reply_Trn
-- Purpose: Structured L2 replies inserted into ticket thread
-- =============================================================================
CREATE TABLE Helpdesk_L2_Reply_Trn (
    ID uniqueidentifier NOT NULL PRIMARY KEY DEFAULT NEWID(),
    TicketID uniqueidentifier NOT NULL,
    RunID uniqueidentifier NOT NULL,
    ReplyType varchar(20) NOT NULL CHECK (ReplyType IN ('ANSWER','QUESTION','INVESTIGATION_UPDATE','RESOLUTION','L3_ESCALATION')),
    ReplyText nvarchar(MAX) NULL,
    RootCause nvarchar(MAX) NULL,
    Resolution nvarchar(MAX) NULL,
    EvidenceSummary nvarchar(MAX) NULL,
    RequiresUserResponse bit NOT NULL DEFAULT 0,
    IsResolution bit NOT NULL DEFAULT 0,
    EscalateToL3 bit NOT NULL DEFAULT 0,
    CreatedOn datetime NOT NULL DEFAULT GETUTCDATE(),
    CreatedBy varchar(100) NOT NULL,
    CONSTRAINT FK_L2Reply_Ticket FOREIGN KEY (TicketID) REFERENCES TicketScheme_Mst_Tbl(TicketNo),
    CONSTRAINT FK_L2Reply_Run FOREIGN KEY (RunID) REFERENCES Helpdesk_L2_Run_Trn(RunID)
);

-- =============================================================================
-- Table: Helpdesk_L2_Evidence_Trn
-- Purpose: Evidence collected during investigation (one row per check/finding)
-- =============================================================================
CREATE TABLE Helpdesk_L2_Evidence_Trn (
    ID uniqueidentifier NOT NULL PRIMARY KEY DEFAULT NEWID(),
    RunID uniqueidentifier NOT NULL,
    Investigator varchar(100) NOT NULL,       -- e.g., 'SAPBot', 'SMSBot', etc.
    CheckType varchar(100) NOT NULL,        -- e.g., 'SAP production posting', 'CCM production'
    SourceSystem varchar(100) NOT NULL,     -- e.g., 'SAP_API_TRANSACTION', 'CCM_PRODUCTION'
    SourceTable varchar(100) NULL,          -- Optional: table name if applicable
    SourceRecordID varchar(100) NULL,       -- Optional: record ID from source system
    Finding varchar(200) NOT NULL,          -- What was checked
    ObservedValue nvarchar(MAX) NULL,       -- What was observed
    ObservedOn datetime NOT NULL DEFAULT GETUTCDATE(),
    QueryReference varchar(200) NULL,       -- SQL query or tool reference
    CONSTRAINT FK_L2Evidence_Run FOREIGN KEY (RunID) REFERENCES Helpdesk_L2_Run_Trn(RunID)
);

-- =============================================================================
-- Indexes for performance
-- =============================================================================
CREATE INDEX IX_Helpdesk_L2_Run_TicketID ON Helpdesk_L2_Run_Trn(TicketID);
CREATE INDEX IX_Helpdesk_L2_Reply_TicketID ON Helpdesk_L2_Reply_Trn(TicketID);
CREATE INDEX IX_Helpdesk_L2_Reply_RunID ON Helpdesk_L2_Reply_Trn(RunID);
CREATE INDEX IX_Helpdesk_L2_Evidence_RunID ON Helpdesk_L2_Evidence_Trn(RunID);
CREATE INDEX IX_Helpdesk_L2_Evidence_CheckType ON Helpdesk_L2_Evidence_Trn(CheckType);
CREATE INDEX IX_Helpdesk_L2_Evidence_SourceSystem ON Helpdesk_L2_Evidence_Trn(SourceSystem);

-- =============================================================================
-- Sample stored procedure: Claim next ticket for Hermes worker
-- =============================================================================
CREATE PROCEDURE sp_Hermes_ClaimTicket
    @WorkerID varchar(100),
    @MinutesSinceLastClaim int = 5
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRANSACTION;
    
    SELECT TOP 1 TicketID, CreatedOn, Priority/*, other relevant columns */ 
    FROM TicketScheme_Mst_Tbl WITH (UPDLOCK, READPAST, ROWLOCK)
    WHERE
        Status IN ('OPEN', 'REOPENED')
        AND SupportLevel = 'L2'
        AND (AIProcessingStatus IS NULL OR AIProcessingStatus IN ('READY', 'RETRY'))
    ORDER BY CreatedOn ASC;  -- Could add ageing: + DATEDIFF(minute, CreatedOn, GETUTCDATE())
    
    -- Update the claimed ticket
    UPDATE TicketScheme_Mst_Tbl WITH (
        UPDLOCK
    ) SET
        AIProcessingStatus = 'RUNNING',
        AIClaimedBy = @WorkerID,
        AIClaimedOn = SYSUTCDATETIME()
    WHERE CurrentTicketID = @@ROWCOUNT;  -- Or match by the selected TicketID
    
    COMMIT;
END;
GO

-- =============================================================================
-- Sample stored procedure: Update ticket status after L2 resolution
-- =============================================================================
CREATE PROCEDURE sp_Hermes_ResolveTicket
    @RunID uniqueidentifier,
    @ReplyType varchar(20),
    @ReplyText nvarchar(MAX),
    @RootCause nvarchar(MAX),
    @Resolution nvarchar(MAX),
    @EscalateToL3 bit = 0
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Insert structured reply
    INSERT INTO Helpdesk_L2_Reply_Trn (
        TicketID, RunID, ReplyType, ReplyText, RootCause, Resolution,
        EvidenceSummary, RequiresUserResponse, IsResolution, EscalateToL3, CreatedBy
    )
    SELECT
        TicketID,
        @RunID,
        @ReplyType,
        @ReplyText,
        @RootCause,
        @Resolution,
        -- Summary of evidence from this run
        (SELECT TOP 1 STRING_AGG(Finding + ': ' + ObservedValue, CHAR(10)) 
         FROM Helpdesk_L2_Evidence_Trn WHERE RunID = @RunID),
        0,  -- RequiresUserResponse
        1,  -- IsResolution
        @EscalateToL3,
        @WorkerID  -- or system user
    FROM Helpdesk_L2_Run_Trn WHERE RunID = @RunID;
    
    -- Update ticket status
    UPDATE TicketScheme_Mst_Tbl SET
        Status = CASE WHEN @EscalateToL3 = 1 THEN 'ESCALATED_L3' ELSE 'RESOLVED' END,
        AIProcessingStatus = 'COMPLETED',
        ResolvedOn = GETUTCDATE()
    WHERE TicketID = (SELECT TicketID FROM Helpdesk_L2_Run_Trn WHERE RunID = @RunID);
    
    -- If escalating to L3, also populate escalation fields
    IF @EscalateToL3 = 1
    BEGIN
        -- Could insert L3 escalation record here
    END
END;
GO

-- =============================================================================
-- Index/view for tracking investigation progress
-- =============================================================================
CREATE VIEW vw_Hermes_InvestigationStatus AS
SELECT
    t.TicketNo,
    t.Subject,
    t.SupportLevel,
    t.Status,
    t.AIProcessingStatus,
    r.RunID,
    r.Status as RunStatus,
    r.StartedOn,
    r.CompletedOn,
    r.Outcome,
    r.ProblemCategory,
    rl.ReplyType,
    rl.RequiresUserResponse,
    rl.IsResolution,
    rl.EscalateToL3,
    rl.CreatedOn as ReplyCreatedOn
FROM TicketScheme_Mst_Tbl t
LEFT JOIN Helpdesk_L2_Run_Trn r ON t.TicketNo = r.TicketID
LEFT JOIN Helpdesk_L2_Reply_Trn rl ON r.RunID = rl.RunID
ORDER BY r.StartedOn DESC;

-- Grant read-only access for Hermes AI identity
-- (This should be configured at the SQL account level, not in the DDL)
-- GRANT SELECT ON vw_Hermes_InvestigationStatus TO Hermes_L2_User;
-- GRANT SELECT, INSERT, UPDATE ON Helpdesk_L2_* TO Hermes_L2_User;
-- DENY INSERT, UPDATE, DELETE ON MES tables TO Hermes_L2_User;

-- =============================================================================
-- Notes per Helpdesk Plan 1 02092026.md:
-- 
-- Section 10: L2 reply table - dedicated transactional table joined through Ticket ID
-- Section 11: Keep detailed investigation separately (Run_Trn + Evidence_Trn)
-- Section 12: Hermes should be able to ask user questions - RequiresUserResponse flag
-- Section 13: Hermes should be able to close tickets directly
-- Section 14: L3 escalation package prepared with complete investigation history
-- =============================================================================