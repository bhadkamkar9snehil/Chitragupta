---
type: procedure
title: "XSTUDIO_WORKFLOW_6F954B26-CB87-40FC-8B73-26EE001C55DC_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_6F954B26-CB87-40FC-8B73-26EE001C55DC_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- CCM_Data: CCMCastingDate, CCMCastingTime
- XMES_ActiveLife_Element_Mst_Tbl: LastUsedBatch, ModifiedOn, Source
- XMES_Life_Tracker_Register_Mst_Tbl: ModifiedBy, ModifiedOn, Source, Status
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, ActualLiquidMetalWeight, ArmConsumption, ArmNo, BilletType1, BilletType2, BilletType3, BilletType4, CalcBilletsWeight1, CalcBilletsWeight2, CalcBilletsWeight3, CalcBilletsWeight4, CapturedTPH, ColdBilletCount, CrossSection, Customer, CutLenght1, CutLenght2, CutLenght3, CutLenght4, CutLength, DeltaTSTD1, DeltaTSTD2, DeltaTSTD3, DeltaTSTD4, DeltaTSTD5, DeltaTSTD6, EndCutMeter, EndTime, EntryDateTime, FlowZ1LtMinSTD1, FlowZ1LtMinSTD2, FlowZ1LtMinSTD3, FlowZ1LtMinSTD4, FlowZ1LtMinSTD5, FlowZ1LtMinSTD6, FlowZ2LtMinSTD1, FlowZ2LtMinSTD2, FlowZ2LtMinSTD3, FlowZ2LtMinSTD4, FlowZ2LtMinSTD5, FlowZ2LtMinSTD6, FlowZ3LtMinSTD1, FlowZ3LtMinSTD2, FlowZ3LtMinSTD3, FlowZ3LtMinSTD4, FlowZ3LtMinSTD5, FlowZ3LtMinSTD6, Grade, HeatID, HeatReportDate, HotBilletCount, ID, InletPressureSTD1, InletPressureSTD2, InletPressureSTD3, InletPressureSTD4, InletPressureSTD5, InletPressureSTD6, InletTempT1STD1, InletTempT1STD2, InletTempT1STD3, InletTempT1STD4, InletTempT1STD5, InletTempT1STD6, LadleSequence, LaunderLossTon, MTDPlannedProduction, Material, MonthlyTarget, MouldWaterFlowLMinSTD1, MouldWaterFlowLMinSTD2, MouldWaterFlowLMinSTD3, MouldWaterFlowLMinSTD4, MouldWaterFlowLMinSTD5, MouldWaterFlowLMinSTD6, Noof103MtrBillets, Noof117MtrBillet, Noof130mmbillets, Noof140mmbillets, Noof6mbilletsmeter, NoofBillets1, NoofBillets2, NoofBillets3, NoofBillets4, OldCapturedBilletCount, OldCapturedBilletWeightTon, OtherLossesTon, OutletPressureSTD1, OutletPressureSTD2, OutletPressureSTD3, OutletPressureSTD4, OutletPressureSTD5, OutletPressureSTD6, OutletTempT2STD1, OutletTempT2STD2, OutletTempT2STD3, OutletTempT2STD4, OutletTempT2STD5, OutletTempT2STD6, PostToSAP1, PostToSAP2, PostToSAP3, PostToSAP4, ProductionPlant, RemainingDeclaredBilletCount, RemainingDeclaredBilletWeightTon, RemainingPostedBilletCount, RemainingPostedBilletWeightTon, ReportDate, SAPPostingDate, STD1OSCSpeed, STD2OSCSpeed, STD3OSCSpeed, STD4OSCSpeed, STD5OSCSpeed, STD6OSCSpeed, SalesOrder, SetWeightTon, ShortBilletCount, StartTime, Status, Strand1BilletCounter, Strand1CastingSpeed, Strand1StraightnerPressure, Strand1WithdrawalPressure, Strand2BilletCounter, Strand2CastingSpeed, Strand2StraightnerPressure, Strand2WithdrawalPressure, Strand3BilletCounter, Strand3CastingSpeed, Strand3StraightnerPressure, Strand3WithdrawalPressure, Strand4BilletCounter, Strand4CastingSpeed, Strand4StraightnerPressure, Strand4WithdrawalPressure, Strand5BilletCounter, Strand5CastingSpeed, Strand5StraightnerPressure, Strand5WithdrawalPressure, Strand6BilletCounter, Strand6CastingSpeed, Strand6StraightnerPressure, Strand6WithdrawalPressure, SuperHeat, TodayPlannedProduction, TotalBilletsCount, TotalFlowLtMinSTD1, TotalFlowLtMinSTD2, TotalFlowLtMinSTD3, TotalFlowLtMinSTD4, TotalFlowLtMinSTD5, TotalFlowLtMinSTD6, TotalPostedBilletCount, TotalPostedBilletWeightTon, TotalProduction, TundishTemperature, TundishlossTon, WorkOrder
- EAF_PER_HEAT: HeatID, HeatReportDate, ReportDate
- XMES_ActiveLife_Element_Mst_Tbl: ElementNameID, IsDeleted
- XMES_Element_Life_Type_Mapping_Mst_Tbl: DataCaptureType, ElementType, IsDeleted, ParentID
- XMES_Life_Element_Mst_Tbl: ID, IsDeleted, ParentID
- XMES_Life_Tracker_Register_Mst_Tbl: ID

## Writes (named in its SQL text)

- CCM_Per_Heat

## Calls

- Quality_Spectro_IsLatestSample_Update_Usp
- XMES_SMS_Temperature_Per_Heat_USP

## What its own log shows

8,290 log rows, 2026-05-21 16:04 to 2026-07-08 18:50.

Steps:
- 1 Entered
- 2 Procedure Quality spectro islatest sample update Start
- 2 Update CCM Casting Date and CCM Casting Time in CCM data Start
- 2 Update CCM Casting Date in CCM data Start
- 3 Procedure Quality spectro islatest sample update End
- 3 Update CCM Casting Date 01-Jul-2026 and CCM Casting Time 04:56:21 in CCM data End
- 3 Update CCM Casting Date 02-Jul-2026 and CCM Casting Time 05:03:58 in CCM data End
- 3 Update CCM Casting Date 03-Jul-2026 and CCM Casting Time 02:00:21 in CCM data End
- 3 Update CCM Casting Date 04-Jul-2026 and CCM Casting Time 04:51:57 in CCM data End
- 3 Update CCM Casting Date 05-Jul-2026 and CCM Casting Time 05:03:02 in CCM data End
- 3 Update CCM Casting Date 05-Jul-2026 and CCM Casting Time 17:51:59 in CCM data End
- 3 Update CCM Casting Date 06-Jul-2026 and CCM Casting Time 05:14:47 in CCM data End
- 3 Update CCM Casting Date 07-Jul-2026 and CCM Casting Time 05:02:54 in CCM data End
- 3 Update CCM Casting Date 08-Jul-2026 and CCM Casting Time 02:57:33 in CCM data End
- 3 Update CCM Casting Date 25-Jun-2026 and CCM Casting Time 04:55:32 in CCM data End
- 3 Update CCM Casting Date 26-Jun-2026 and CCM Casting Time 01:52:51 in CCM data End
- 3 Update CCM Casting Date 27-Jun-2026 and CCM Casting Time 04:33:05 in CCM data End
- 3 Update CCM Casting Date 28-Jun-2026 and CCM Casting Time 13:10:51 in CCM data End
- 3 Update CCM Casting Date 29-Jun-2026 and CCM Casting Time 04:56:36 in CCM data End
- 3 Update CCM Casting Date 30-Jun-2026 and CCM Casting Time 04:47:19 in CCM data End
- 3 Update CCM Casting Date in CCM data End
- 4 Get Heat Report Date and Report date from EAF PER HEAT Start
- 4 Procedure Quality spectro islatest sample update Start
- 4 Update Last USed batch 1603733 of Active Life element Start
- 4 Update Last USed batch 1603734 of Active Life element Start
- 4 Update Last USed batch 1603735 of Active Life element Start
- 4 Update Last USed batch 1603736 of Active Life element Start
- 4 Update Last USed batch 1603737 of Active Life element Start
- 4 Update Last USed batch 1603738 of Active Life element Start
- 4 Update Last USed batch 1603739 of Active Life element Start

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_6F954B26-CB87-40FC-8B73-26EE001C55DC_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='CF587DA9-0FDF-494E-8044-7620D00418AE', @p_RecordId='Completed', @p_StatusAttributeName='FADC25D4-738B-4C89-B504-85517DD166A2', @p_Status='WorkflowStatus'`
