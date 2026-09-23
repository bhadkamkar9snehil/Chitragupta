/*
Hermes L2 - XBatch diagnostic procedures (read-only)
Target database: XStudio_Helpdesk (reads XStudio_Xbatch cross-database)

One call per failure class from Knowledge/XBATCH_DIAGNOSTIC_PLAYBOOK.md. Each returns a
flat, time-ordered evidence set (Stage, Source, EventTime, Status, Detail) that the harness
turns into numbered lines for Jev. Every column used here was verified live on 2026-09-23.
These procedures only SELECT; they never write.
*/

SET NOCOUNT ON;
GO

/*
Heat journey (playbook classes A-D): everything XBatch recorded for one heat, in time order.
Where the timeline stops, or which stage shows an error, is the diagnosis.
*/
CREATE OR ALTER PROCEDURE dbo.Hermes_Diag_Heat_Journey_Usp
(
    @HeatID int
)
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @Heat varchar(20) = CONVERT(varchar(20), @HeatID);

    DECLARE @J TABLE (Stage varchar(40), Source varchar(80), EventTime datetime, Status nvarchar(200),
                      Detail nvarchar(2000));

    /* Process timing chain. States 11+ store ActualHeatID = HeatID - 1 (vendor-flagged). */
    INSERT @J
    SELECT 'process_state', 'SMS_Plant_Process_EventTime', p.StartTime,
           CONCAT(p.StateSequence, ' ', p.Status),
           CONCAT('workflow=', ISNULL(p.WorkflowStatus, '-'), '; end=', CONVERT(varchar(19), p.EndTime, 120),
                  '; duration=', ISNULL(p.DurationMMSS, '-'), '; HeatID=', CONVERT(int, p.HeatID),
                  '; ActualHeatID=', p.ActualHeatID)
    FROM XStudio_Xbatch.dbo.SMS_Plant_Process_EventTime p
    WHERE ISNULL(p.IsDeleted, 0) = 0 AND (p.ActualHeatID = @HeatID OR p.HeatID = @HeatID);

    INSERT @J
    SELECT 'area_process_time', 'EAF_ProcessTime', t.StartTime, t.Status,
           CONCAT('workflow=', ISNULL(t.WorkflowStatus, '-'), '; end=', CONVERT(varchar(19), t.EndTime, 120))
    FROM XStudio_Xbatch.dbo.EAF_ProcessTime t WHERE ISNULL(t.IsDeleted, 0) = 0 AND t.HeatID = @HeatID
    UNION ALL
    SELECT 'area_process_time', 'LRF_ProcessTime', t.StartTime, t.Status,
           CONCAT('end=', CONVERT(varchar(19), t.EndTime, 120), '; LRFHeatID=', t.LRFHeatID)
    FROM XStudio_Xbatch.dbo.LRF_ProcessTime t WHERE ISNULL(t.IsDeleted, 0) = 0 AND t.HeatID = @HeatID
    UNION ALL
    SELECT 'area_process_time', 'CCM_ProcessTime', t.StartTime, t.Status,
           CONCAT('workflow=', ISNULL(t.WorkFlowStatus, '-'), '; end=', CONVERT(varchar(19), t.EndTime, 120))
    FROM XStudio_Xbatch.dbo.CCM_ProcessTime t WHERE ISNULL(t.IsDeleted, 0) = 0 AND t.CCMHeatNo = @HeatID;

    /* Per-heat event records written by the area workflows. */
    INSERT @J
    SELECT 'per_heat_record', 'EAF_PER_HEAT', e.StartTime, e.Status,
           CONCAT('SAPWorkflowStatus=', ISNULL(e.SAPWorkflowStatus, '-'), '; WorkOrder=', ISNULL(e.WorkOrder, '-'),
                  '; SteelGrade=', ISNULL(e.SteelGrade, '-'), '; PowerOnTime=', ISNULL(e.PowerOnTime, '-'),
                  '; PowerOffTime=', ISNULL(e.PowerOffTime, '-'), '; HeatTime=', ISNULL(e.HeatTime, '-'),
                  '; LiquidMetalWeight=', e.LiquidMetalWeight, '; modified=', CONVERT(varchar(19), e.ModifiedOn, 120))
    FROM XStudio_Xbatch.dbo.EAF_PER_HEAT e WHERE ISNULL(e.IsDeleted, 0) = 0 AND e.HeatID = @HeatID
    UNION ALL
    SELECT 'per_heat_record', 'LRF_Per_Heat', l.StartTime, l.Status,
           CONCAT('workflow=', ISNULL(l.WorkFlowStatus, '-'), '; SAPWorkflowStatus=', ISNULL(l.SAPWorkflowStatus, '-'),
                  '; WorkOrder=', ISNULL(l.WorkOrder, '-'), '; Grade=', ISNULL(l.Grade, '-'),
                  '; ArcingTime=', l.ArcingTime, '; PowerONTime=', l.PowerONTime, '; PowerOFFTime=', l.PowerOFFTime,
                  '; LiquidMetalWeight=', l.LiquidMetalWeight, '; modified=', CONVERT(varchar(19), l.ModifiedOn, 120))
    FROM XStudio_Xbatch.dbo.LRF_Per_Heat l WHERE ISNULL(l.IsDeleted, 0) = 0 AND l.HeatID = @HeatID
    UNION ALL
    SELECT 'per_heat_record', 'CCM_Per_Heat', c.StartTime, c.Status,
           CONCAT('SAPWorkflowStatus=', ISNULL(c.SAPWorkflowStatus, '-'), '; ArmNo=', c.ArmNo,
                  '; TotalBilletsCount=', c.TotalBilletsCount, '; end=', CONVERT(varchar(19), c.EndTime, 120),
                  '; modified=', CONVERT(varchar(19), c.ModifiedOn, 120))
    FROM XStudio_Xbatch.dbo.CCM_Per_Heat c WHERE ISNULL(c.IsDeleted, 0) = 0 AND c.HeatID = @HeatID
    UNION ALL
    SELECT 'per_heat_record', 'BilletsCastCount', b.StartTime, b.Status,
           CONCAT('workflow=', ISNULL(b.WorkFlowStatus, '-'), '; ActualBilletsCountbyOperator=',
                  b.ActualBilletsCountbyOperator, '; end=', CONVERT(varchar(19), b.EndTime, 120))
    FROM XStudio_Xbatch.dbo.BilletsCastCount b WHERE ISNULL(b.IsDeleted, 0) = 0 AND b.HeatID = @HeatID;

    /* Billet genealogy, summarised (a heat has tens of billets). */
    INSERT @J
    SELECT 'billet_genealogy', 'XMES_CCM_Billet_Genealogy_Trn_Tbl', MIN(g.CutStartTime),
           CONCAT(COUNT(*), ' billets'),
           CONCAT('strands=', COUNT(DISTINCT g.StrandNo), '; first_cut=', CONVERT(varchar(19), MIN(g.CutStartTime), 120),
                  '; last_cut=', CONVERT(varchar(19), MAX(g.CutStartTime), 120),
                  '; unprocessed=', SUM(CASE WHEN ISNULL(g.IsProcessed, 0) = 0 THEN 1 ELSE 0 END))
    FROM XStudio_Xbatch.dbo.XMES_CCM_Billet_Genealogy_Trn_Tbl g
    WHERE ISNULL(g.IsDeleted, 0) = 0 AND g.HeatNo = @Heat
    HAVING COUNT(*) > 0;

    /* SAP: domain transactions, outbound postings, API errors for this heat. */
    INSERT @J
    SELECT 'sap_production', 'MES_SAP_Production_Trn_Tbl', COALESCE(s.PostingDate, s.CreatedOn),
           ISNULL(s.SAPPostingStatus, '-'),
           CONCAT('Batch=', ISNULL(s.Batch, '-'), '; Material=', ISNULL(s.Material, '-'),
                  '; MaterialDocument=', s.MaterialDocument, '; MO=', ISNULL(s.ManufacturingOrder, '-'),
                  '; Qty=', s.QuantityInEntryUnit)
    FROM XStudio_Xbatch.dbo.MES_SAP_Production_Trn_Tbl s WHERE ISNULL(s.IsDeleted, 0) = 0 AND s.HeatNo = @HeatID
    UNION ALL
    SELECT 'sap_consumption', 'MES_SAP_Consumption_Trn_Tbl', COALESCE(s.PostingDate, s.CreatedOn),
           ISNULL(s.SAPPostingStatus, '-'),
           CONCAT('Material=', ISNULL(s.Material, '-'), '; MaterialDocument=', ISNULL(s.MaterialDocument, '-'),
                  '; Qty=', s.QuantityInEntryUnit)
    FROM XStudio_Xbatch.dbo.MES_SAP_Consumption_Trn_Tbl s WHERE ISNULL(s.IsDeleted, 0) = 0 AND s.HeatNo = @HeatID
    UNION ALL
    SELECT 'sap_posting', 'SAP_Posting_Tbl', COALESCE(s.PostingDate, s.CreatedOn), ISNULL(s.SAP_Status, '-'),
           CONCAT('PostingType=', ISNULL(s.PostingType, '-'), '; IsProcessed=', s.IsProcessed,
                  '; DocumentNo=', ISNULL(s.SAP_DocumentNo, '-'), '; Batch=', ISNULL(s.BatchNo, '-'),
                  '; Message=', LEFT(ISNULL(s.SAP_Message, '-'), 300))
    FROM XStudio_Xbatch.dbo.SAP_Posting_Tbl s WHERE ISNULL(s.IsDeleted, 0) = 0 AND s.HeatNo = @Heat
    UNION ALL
    SELECT 'sap_api_error', 'XMES_SAP_API_GoodsMovement_Error', a.CreatedOn, ISNULL(a.Status, '-'),
           CONCAT('MO=', ISNULL(a.ManufacturingOrder, '-'), '; MovementType=', ISNULL(a.MovementType, '-'),
                  '; Error=', LEFT(ISNULL(a.ErrorMessage, a.SuccessMessage), 400))
    FROM XStudio_Xbatch.dbo.XMES_SAP_API_GoodsMovement_Error a WHERE ISNULL(a.IsDeleted, 0) = 0 AND a.Batch = @Heat
    UNION ALL
    SELECT 'sap_api_error', 'XMES_SAP_API_UsageDecision_Error', a.CreatedOn, ISNULL(a.Status, '-'),
           CONCAT('InspectionLot=', ISNULL(a.InspectionLot, '-'), '; Error=', LEFT(ISNULL(a.ErrorMessage, a.SuccessMessage), 400))
    FROM XStudio_Xbatch.dbo.XMES_SAP_API_UsageDecision_Error a WHERE ISNULL(a.IsDeleted, 0) = 0 AND a.HeatNo = @Heat
    UNION ALL
    SELECT 'sap_api_error', 'XMES_SAP_API_ResultRecording_Error', a.CreatedOn, ISNULL(a.Status, '-'),
           CONCAT('InspectionLot=', ISNULL(a.InspectionLot, '-'), '; Error=', LEFT(ISNULL(a.ErrorMessage, a.SuccessMessage), 400))
    FROM XStudio_Xbatch.dbo.XMES_SAP_API_ResultRecording_Error a WHERE ISNULL(a.IsDeleted, 0) = 0 AND a.HeatNo = @Heat;

    SELECT ROW_NUMBER() OVER (ORDER BY EventTime, Stage) AS Seq, Stage, Source, EventTime, Status, Detail
    FROM @J
    ORDER BY Seq;
END
GO
