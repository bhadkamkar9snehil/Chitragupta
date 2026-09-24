---
type: view
title: "XStudio_List_CCM_Per_Heat_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_CCM_Per_Heat_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- HeatID: same values as key `HeatNo`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- CCM_Per_Heat
- Grade_Master
- XBatch_Work_Order_Mst_Tbl

## Read by

- XMES_SMS_Dashboard_Delay_USP
- usp_SMS_EAF_LRF_CCM_KPI_PerDate

## Columns

- LadleBottomOpenTimeHHMM datetime
- Strand1BilletCounter int
- Strand1StraightnerPressureBar decimal
- CrossSection int
- HeatNo int
- Strand1WithdrawalPressureBar decimal
- Strand1OscillationSpeedrpm decimal
- Strand1CastingSpeedMPerMin decimal
- LadleBottomCloseTimeHHMM datetime
- Strand2CastingSpeedMPerMin decimal
- Strand2OscillationSpeedrpm decimal
- Strand2BilletCounter int
- Strand2StraightnerPressureBar decimal
- Strand2WithdrawalPressureBar decimal
- SetWeightTon decimal
- SteelGrade varchar(100)
- Strand3StraightnerPressureBar decimal
- Strand3OscillationSpeedrpm decimal
- Status varchar(100)
- Strand3WithdrawalPressureBar decimal
- Strand3CastingSpeedMPerMin decimal
- Delete varchar(100)
- LadleSequenceNo int
- Strand3BilletCounter int
- Strand4CastingSpeedMPerMin decimal
- Strand4OscillationSpeedrpm decimal
- Edit varchar(242)
- Strand4StraightnerPressureBar decimal
- ArmConsumptionTon decimal
- Strand4WithdrawalPressureBar decimal
- Strand4BilletCounter int
- Strand5BilletCounter int
- Strand5StraightnerPressureBar decimal
- Strand5WithdrawalPressureBar decimal
- Noof140mmbillets int
- Strand5OscillationSpeed decimal
- Strand5CastingSpeedMPerMin decimal
- LadleSequence varchar(100)
- CastingDuration varchar(100)
- Noof130mmbillets int
- Strand6WithdrawalPressureBar decimal
- Strand6CastingSpeedMPerMin decimal
- Strand6OscillationSpeedrpm decimal
- Strand6BilletCounter int
- WorkOrderNumber varchar(100)
- Strand6StraightnerPressureBar decimal
- TonPerHour decimal
- LogbookManualEntry varchar(-1)
- CapturedTonPerHour decimal
- SAPPosting varchar(50)
- Noof6mbilletsmeter int
- ByProductPostingData varchar(-1)
- ProductionPostingTransaction varchar(-1)
- CutLengthMeter int
- HeatChemistrydata varchar(-1)
- GradeChange varchar(-1)
- SAPPostingDate date
- CastingStartTimeHHMMSS varchar(100)
- ProductionData varchar(-1)
- TotalCapturedBilletsCountfromPLC decimal
- ID varchar(36)
- TotalCapturedBilletWeightTonfromPLC decimal
- TotalDeclaredBilletsCount int
- TotalDeclaredBilletWeightTon decimal
- BilletsDetails varchar(-1)
- TotalPostedBilletCount int
- TotalPostedBilletWeightTon decimal
- ArmNo decimal
- RemainingPostedBilletCount int
- RemainingPostedBilletWeightTon decimal
- ActualLiquidMetalWeightTon decimal
- CasterYieldPercentage decimal
- IsProcessed bit
- EquipmentID varchar(36)
- ReportDate varchar(100)
- TundishTemperature decimal
- Dateyyyymmdd varchar(100)
- StartTime datetime
- HeatReportDate date
- WorkOrderDetails varchar(-1)
- HeatID int
- Details varchar(-1)
- SuperHeat decimal
- Grade_GradeName varchar(100)
- GradeColorCode varchar(50)
- Grade varchar(100)
- SAPWorkflowStatus varchar(50)
- WorkOrder varchar(-1)
- CastingStartTimeHHmm varchar(100)
- NoofStrands decimal
