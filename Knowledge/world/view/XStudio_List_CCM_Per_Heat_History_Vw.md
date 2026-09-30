---
type: view
title: "XStudio_List_CCM_Per_Heat_History_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_CCM_Per_Heat_History_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- HeatID: same values as key `HeatNo`
- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- CCM_Per_Heat
- Grade_Master
- XBatch_Work_Order_Mst_Tbl

## Columns

- Strand1CastingSpeedMPerMin decimal
- CrossSection int
- LadleBottomOpenTimeHHMM datetime
- Strand1BilletCounter int
- Strand1OscillationSpeedrpm decimal
- Strand1WithdrawalPressureBar decimal
- HeatNo int
- Strand1StraightnerPressureBar decimal
- SetWeightTon decimal
- Strand2WithdrawalPressureBar decimal
- Strand2OscillationSpeedrpm decimal
- Strand2CastingSpeedMPerMin decimal
- LadleBottomCloseTimeHHMM datetime
- Strand2StraightnerPressureBar decimal
- SteelGrade varchar(100)
- Strand2BilletCounter int
- Edit varchar(256)
- Strand3BilletCounter int
- Strand3CastingSpeedMPerMin decimal
- Strand3StraightnerPressureBar decimal
- Strand3OscillationSpeedrpm decimal
- LadleSequenceNo int
- Status varchar(100)
- Strand3WithdrawalPressureBar decimal
- Strand4StraightnerPressureBar decimal
- ArmConsumptionTon decimal
- LadleSequence varchar(100)
- Noof140mmbillets int
- Strand4CastingSpeedMPerMin decimal
- Strand4BilletCounter int
- Strand4OscillationSpeedrpm decimal
- Strand4WithdrawalPressureBar decimal
- TonPerHour decimal
- Strand5BilletCounter int
- Strand5OscillationSpeed decimal
- Strand5StraightnerPressureBar decimal
- WorkOrderNumber varchar(100)
- Strand5CastingSpeedMPerMin decimal
- Strand5WithdrawalPressureBar decimal
- Strand6BilletCounter int
- Strand6StraightnerPressureBar decimal
- Strand6OscillationSpeedrpm decimal
- LogbookManualEntry varchar(-1)
- Strand6CastingSpeedMPerMin decimal
- Strand6WithdrawalPressureBar decimal
- Noof130mmbillets int
- SAPPosting varchar(50)
- Delete varchar(100)
- ByProductPostingData varchar(-1)
- Noof6mbilletsmeter int
- ProductionPostingTransaction varchar(-1)
- CutLengthMeter int
- HeatChemistrydata varchar(-1)
- GradeChange varchar(-1)
- ProductionData varchar(-1)
- SAPPostingDate date
- ID varchar(36)
- CastingStartTimeHHMMSS varchar(100)
- BilletsDetails varchar(-1)
- TotalCapturedBilletsCount decimal
- TotalCapturedBilletWeightTon decimal
- ArmNo decimal
- TotalDeclaredBilletsCount int
- TotalDeclaredBilletWeightTon decimal
- IsProcessed bit
- TotalPostedBilletCount int
- TotalPostedBilletWeightTon decimal
- RemainingPostedBilletCount int
- RemainingPostedBilletWeightTon decimal
- EquipmentID varchar(36)
- ReportDate varchar(100)
- StartTime datetime
- Details varchar(-1)
- Dateyyyymmdd varchar(100)
- HeatReportDate date
- WorkOrderDetails varchar(-1)
- HeatID int
- GradeColorCode varchar(50)
- Grade varchar(100)
- SAPWorkflowStatus varchar(50)
- WorkOrder varchar(-1)
