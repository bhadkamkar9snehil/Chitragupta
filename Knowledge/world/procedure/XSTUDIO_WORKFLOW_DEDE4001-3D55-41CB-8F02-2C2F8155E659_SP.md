---
type: procedure
title: "XSTUDIO_WORKFLOW_DEDE4001-3D55-41CB-8F02-2C2F8155E659_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_DEDE4001-3D55-41CB-8F02-2C2F8155E659_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, ActualLiquidMetalWeight, ArmConsumption, ArmNo, BilletType1, BilletType2, BilletType3, BilletType4, CalcBilletsWeight1, CalcBilletsWeight2, CalcBilletsWeight3, CalcBilletsWeight4, CapturedTPH, ColdBilletCount, CrossSection, Customer, CutLenght1, CutLenght2, CutLenght3, CutLenght4, CutLength, DeltaTSTD1, DeltaTSTD2, DeltaTSTD3, DeltaTSTD4, DeltaTSTD5, DeltaTSTD6, EndCutMeter, EndTime, EntryDateTime, FlowZ1LtMinSTD1, FlowZ1LtMinSTD2, FlowZ1LtMinSTD3, FlowZ1LtMinSTD4, FlowZ1LtMinSTD5, FlowZ1LtMinSTD6, FlowZ2LtMinSTD1, FlowZ2LtMinSTD2, FlowZ2LtMinSTD3, FlowZ2LtMinSTD4, FlowZ2LtMinSTD5, FlowZ2LtMinSTD6, FlowZ3LtMinSTD1, FlowZ3LtMinSTD2, FlowZ3LtMinSTD3, FlowZ3LtMinSTD4, FlowZ3LtMinSTD5, FlowZ3LtMinSTD6, Grade, HeatID, HeatReportDate, HotBilletCount, ID, InletPressureSTD1, InletPressureSTD2, InletPressureSTD3, InletPressureSTD4, InletPressureSTD5, InletPressureSTD6, InletTempT1STD1, InletTempT1STD2, InletTempT1STD3, InletTempT1STD4, InletTempT1STD5, InletTempT1STD6, LadleSequence, LaunderLossTon, MTDPlannedProduction, Material, MonthlyTarget, MouldWaterFlowLMinSTD1, MouldWaterFlowLMinSTD2, MouldWaterFlowLMinSTD3, MouldWaterFlowLMinSTD4, MouldWaterFlowLMinSTD5, MouldWaterFlowLMinSTD6, Noof103MtrBillets, Noof117MtrBillet, Noof130mmbillets, Noof140mmbillets, Noof6mbilletsmeter, NoofBillets1, NoofBillets2, NoofBillets3, NoofBillets4, OtherLossesTon, OutletPressureSTD1, OutletPressureSTD2, OutletPressureSTD3, OutletPressureSTD4, OutletPressureSTD5, OutletPressureSTD6, OutletTempT2STD1, OutletTempT2STD2, OutletTempT2STD3, OutletTempT2STD4, OutletTempT2STD5, OutletTempT2STD6, PostToSAP1, PostToSAP2, PostToSAP3, PostToSAP4, ProductionPlant, RemainingDeclaredBilletCount, RemainingDeclaredBilletWeightTon, RemainingPostedBilletCount, RemainingPostedBilletWeightTon, ReportDate, SAPPostingDate, STD1OSCSpeed, STD2OSCSpeed, STD3OSCSpeed, STD4OSCSpeed, STD5OSCSpeed, STD6OSCSpeed, SalesOrder, SetWeightTon, ShortBilletCount, StartTime, Status, Strand1BilletCounter, Strand1CastingSpeed, Strand1StraightnerPressure, Strand1WithdrawalPressure, Strand2BilletCounter, Strand2CastingSpeed, Strand2StraightnerPressure, Strand2WithdrawalPressure, Strand3BilletCounter, Strand3CastingSpeed, Strand3StraightnerPressure, Strand3WithdrawalPressure, Strand4BilletCounter, Strand4CastingSpeed, Strand4StraightnerPressure, Strand4WithdrawalPressure, Strand5BilletCounter, Strand5CastingSpeed, Strand5StraightnerPressure, Strand5WithdrawalPressure, Strand6BilletCounter, Strand6CastingSpeed, Strand6StraightnerPressure, Strand6WithdrawalPressure, SuperHeat, TodayPlannedProduction, TotalBilletsCount, TotalFlowLtMinSTD1, TotalFlowLtMinSTD2, TotalFlowLtMinSTD3, TotalFlowLtMinSTD4, TotalFlowLtMinSTD5, TotalFlowLtMinSTD6, TotalPostedBilletCount, TotalPostedBilletWeightTon, TotalProduction, TundishlossTon, WorkOrder

## Writes (named in its SQL text)

- CCM_Per_Heat
