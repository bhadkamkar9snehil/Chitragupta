---
type: procedure
title: "XBatch_Add_Heat_start_end_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Add_Heat_start_end_Usp

Parameters: @ReportDate date, @FirstHeat int, @LastHeat int, @UserID varchar.

## Writes

- CCM_Per_Heat: HeatReportDate, ReportDate
- EAF_PER_HEAT: HeatReportDate
- Heat_End_Selection_Trn_Tbl: CalTimeinMinutes, CalTimeinSecond, FIrstHeatStartTime, FirstHeatNo, LastHeatNo, LastHeatTapTime, ModifiedBy, ModifiedOn, ReportDate
- LRF_Per_Heat: HeatReportDate, ReportDate
- SMS_Target_Summary_Day: HeatID

## Reads

- CCM_Per_Heat: HeatID
- EAF_PER_HEAT: HeatID, HeatStart, IsDeleted, TapStart
- LRF_Per_Heat: HeatID
- SMS_Target_Summary_Day: ReportDate

## Calls

- SP_SMS_Producation_Summary
- XBatch_Recalculate_Summary_CCM_Usp
- XBatch_Recalculate_Summary_EAF_Usp
- XBatch_Recalculate_Summary_LRF_Usp
