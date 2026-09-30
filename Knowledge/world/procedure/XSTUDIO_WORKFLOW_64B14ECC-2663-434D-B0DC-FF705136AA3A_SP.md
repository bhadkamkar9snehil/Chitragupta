---
type: procedure
title: "XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- CCM_Data: CCMHeatNo, SteelGrade
- XBatch_Work_Order_Mst_Tbl: ModifiedBy, ModifiedOn, Source, StartTime
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, ActualLiquidMetalWeight, ArmConsumption, ArmNo, BilletType1, BilletType2, BilletType3, BilletType4, CalcBilletsWeight1, CalcBilletsWeight2, CalcBilletsWeight3, CalcBilletsWeight4, CapturedTPH, ColdBilletCount, CrossSection, Customer, CutLenght1, CutLenght2, CutLenght3, CutLenght4, CutLength, DeltaTSTD1, DeltaTSTD2, DeltaTSTD3, DeltaTSTD4, DeltaTSTD5, DeltaTSTD6, EndCutMeter, EndTime, EntryDateTime, FlowZ1LtMinSTD1, FlowZ1LtMinSTD2, FlowZ1LtMinSTD3, FlowZ1LtMinSTD4, FlowZ1LtMinSTD5, FlowZ1LtMinSTD6, FlowZ2LtMinSTD1, FlowZ2LtMinSTD2, FlowZ2LtMinSTD3, FlowZ2LtMinSTD4, FlowZ2LtMinSTD5, FlowZ2LtMinSTD6, FlowZ3LtMinSTD1, FlowZ3LtMinSTD2, FlowZ3LtMinSTD3, FlowZ3LtMinSTD4, FlowZ3LtMinSTD5, FlowZ3LtMinSTD6, Grade, HeatID, HeatReportDate, HotBilletCount, ID, InletPressureSTD1, InletPressureSTD2, InletPressureSTD3, InletPressureSTD4, InletPressureSTD5, InletPressureSTD6, InletTempT1STD1, InletTempT1STD2, InletTempT1STD3, InletTempT1STD4, InletTempT1STD5, InletTempT1STD6, LadleSequence, LaunderLossTon, MTDPlannedProduction, Material, MonthlyTarget, MouldWaterFlowLMinSTD1, MouldWaterFlowLMinSTD2, MouldWaterFlowLMinSTD3, MouldWaterFlowLMinSTD4, MouldWaterFlowLMinSTD5, MouldWaterFlowLMinSTD6, Noof103MtrBillets, Noof117MtrBillet, Noof130mmbillets, Noof140mmbillets, Noof6mbilletsmeter, NoofBillets1, NoofBillets2, NoofBillets3, NoofBillets4, OldCapturedBilletCount, OldCapturedBilletWeightTon, OtherLossesTon, OutletPressureSTD1, OutletPressureSTD2, OutletPressureSTD3, OutletPressureSTD4, OutletPressureSTD5, OutletPressureSTD6, OutletTempT2STD1, OutletTempT2STD2, OutletTempT2STD3, OutletTempT2STD4, OutletTempT2STD5, OutletTempT2STD6, PostToSAP1, PostToSAP2, PostToSAP3, PostToSAP4, ProductionPlant, RemainingDeclaredBilletCount, RemainingDeclaredBilletWeightTon, RemainingPostedBilletCount, RemainingPostedBilletWeightTon, ReportDate, SAPPostingDate, STD1OSCSpeed, STD2OSCSpeed, STD3OSCSpeed, STD4OSCSpeed, STD5OSCSpeed, STD6OSCSpeed, SalesOrder, SetWeightTon, ShortBilletCount, StartTime, Status, Strand1BilletCounter, Strand1CastingSpeed, Strand1StraightnerPressure, Strand1WithdrawalPressure, Strand2BilletCounter, Strand2CastingSpeed, Strand2StraightnerPressure, Strand2WithdrawalPressure, Strand3BilletCounter, Strand3CastingSpeed, Strand3StraightnerPressure, Strand3WithdrawalPressure, Strand4BilletCounter, Strand4CastingSpeed, Strand4StraightnerPressure, Strand4WithdrawalPressure, Strand5BilletCounter, Strand5CastingSpeed, Strand5StraightnerPressure, Strand5WithdrawalPressure, Strand6BilletCounter, Strand6CastingSpeed, Strand6StraightnerPressure, Strand6WithdrawalPressure, SuperHeat, TodayPlannedProduction, TotalBilletsCount, TotalFlowLtMinSTD1, TotalFlowLtMinSTD2, TotalFlowLtMinSTD3, TotalFlowLtMinSTD4, TotalFlowLtMinSTD5, TotalFlowLtMinSTD6, TotalPostedBilletCount, TotalPostedBilletWeightTon, TotalProduction, TundishTemperature, TundishlossTon, WorkOrder
- LRF_Per_Heat: CreatedOn, HeatID, HeatReportDate, IsDeleted, LiquidMetalWeight, WorkOrder
- SMS_Plant_Process_EventTime: ActualHeatID, CreatedOn, Status
- XBatch_Material_Mst_Tbl: ID, Name
- XBatch_Work_Order_Mst_Tbl: Equipment, Grade, ID, IsDeleted, ItemID, MaterialName, SalesOrder, Status

## Writes (named in its SQL text)

- CCM_Per_Heat

## Calls

- SMS_Data_list_View
- XBatch_I_Material_Consume_NoBOM_USP

## What its own log shows

17,318 log rows, 2026-05-21 16:05 to 2026-08-12 08:44.

Steps:
- 1 Entered
- 2 Get Heat id from SMS Plant Process Eventtime Start
- 2 Get Heat id from SMS Plant Process Eventtime of latest record Start
- 3 Get Heat id 1603734 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603735 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603736 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603737 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603738 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603739 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603740 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603741 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603742 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603743 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603744 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603745 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603746 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603747 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603748 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603749 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603750 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603751 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603752 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603753 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603754 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603755 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603756 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603757 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603758 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603759 from SMS Plant Process Eventtime for latest record End
- 3 Get Heat id 1603760 from SMS Plant Process Eventtime for latest record End

Example call: `EXEC XStudio_Xbatch.dbo.XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP @p_SystemId='A0E0934F-B370-4374-819B-A60CF61E71AF', @p_UserId='', @p_RecordId='Entered', @p_StatusAttributeName='FF6AD215-15E8-47DB-80FF-F5E39178854C', @p_Status='WorkflowStatus'`
