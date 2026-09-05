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
