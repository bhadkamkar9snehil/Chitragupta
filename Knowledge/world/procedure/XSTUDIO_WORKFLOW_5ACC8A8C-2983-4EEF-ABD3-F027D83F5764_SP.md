---
type: procedure
title: "XSTUDIO_WORKFLOW_5ACC8A8C-2983-4EEF-ABD3-F027D83F5764_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_5ACC8A8C-2983-4EEF-ABD3-F027D83F5764_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Billet_Track_Per_Strand: CreatedOn, EndTime, EquipmentID, HeatNo, ID, IsDeleted, IsProcessed, ReportDate, S1BilletCount, S2BilletCount, S3BilletCount, S4BilletCount, S5BilletCount, S6BilletCount, StartTime, Status, StrandwiseCount
- BilletsCastCount: HeatID, IsDeleted, StartTime, WorkFlowStatus

## Writes (named in its SQL text)

- Billet_Track_Per_Strand

## Calls

- XMES_CCM_BILLET_CUT_USP
- XMES_CREATE_BILLETNO_USP

## What its own log shows

362,814 log rows, 2026-05-30 11:59 to 2026-08-10 14:56.

Steps:
- 1 Entered
- 2 Get Latest Heatno of entered workflow status from billets cast count Start
- 3 Get Latest Heatno 1603432 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603433 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603434 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603435 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603436 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603437 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603438 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603439 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603440 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603441 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603442 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603443 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603444 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603445 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603446 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603447 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603448 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603449 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603450 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603451 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603452 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603453 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603454 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603455 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603456 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603457 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603458 of entered workflow status from billets cast count End
- 3 Get Latest Heatno 1603459 of entered workflow status from billets cast count End

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_5ACC8A8C-2983-4EEF-ABD3-F027D83F5764_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Entered', @p_StatusAttributeName='FFFFA523-B4D0-4221-95A0-CDE12A560324', @p_Status='WorkflowStatus'`
