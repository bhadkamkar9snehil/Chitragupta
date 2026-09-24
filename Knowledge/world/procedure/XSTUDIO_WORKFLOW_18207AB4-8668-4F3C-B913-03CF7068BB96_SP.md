---
type: procedure
title: "XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- CCM_Data: LiquidSteelWeight
- SMS_Plant_Process_EventTime: ActualHeatID, ModifiedOn
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- LRF_Per_Heat: HeatID, LiquidMetalWeight
- SMS_Plant_Process_EventTime: CreatedOn, EndTime, HeatID, ID, StartTime, Status

## What its own log shows

29,676 log rows, 2026-05-28 11:00 to 2026-08-12 11:12.

Steps:
- 1 Entered
- 2 Get Latest Heatid of LRF Roof Open when status is ladle move from lrf to ccm, ladle at ccm arm 1 rest position, ladle at ccm arm 2 rest position and turrent rotation Start
- 2 Get Latest Heatid of Ladle At CCM Arm 1 rest position and ladle at ccm arm 2 rest position when status is CCM Arm 2 Casting Position or CCM Arm 1 Casting Position or Billets Production or CCM Turret Control Start
- 3 Get Latest Heatid of LRF Roof Open when status is ladle move from lrf to ccm or ladle at ccm arm 1 rest position or ladle at ccm arm 2 rest position or turrent rotation End
- 3 Get Latest Heatid of Ladle At CCM Arm 1 rest position and ladle at ccm arm 2 rest position when status is CCM Arm 2 Casting Position or CCM Arm 1 Casting Position or Billets Production or CCM Turret Control End
- 4 Set Actual HeatID as Heatid -1 Start
- 5 Set Actual HeatID as Heatid -1 End
- 6 Update ActualHeatID in SMS plant Procss EventTime Start
- 7 Update ActualHeatID in SMS plant Procss EventTime End
- 8 Completed
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603225 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603226 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603227 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603228 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603229 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603230 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603231 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603232 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603233 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603234 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603235 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603236 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603237 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603238 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603239 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603240 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603241 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603242 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603243 Start
- 8 Get LiquidMetal weight From LRF PER HEAT of heatid 1603244 Start

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Entered', @p_StatusAttributeName='FFE60C3D-8A2A-4241-8D6B-F9F014A4A68A', @p_Status='WorkflowStatus'`
