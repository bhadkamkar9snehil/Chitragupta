---
type: procedure
title: "Xstudio_Shift_CCM_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Shift_CCM_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- CCM_Summary_Shift: ActualBilletCount, ActualBilletWeightTon, Entrydatetime, HeatID, MTDPlannedProduction, ModifiedOn, MonthlyTarget, STD1OSCSpeed, STD2OSCSpeed, STD3OSCSpeed, STD4OSCSpeed, STD5OSCSpeed, STD6OSCSpeed, ShiftName, Source, Strand1BilletCounter, Strand1CastingSpeed, Strand2BilletCounter, Strand2CastingSpeed, Strand3BilletCounter, Strand3CastingSpeed, Strand4BilletCounter, Strand4CastingSpeed, Strand5BilletCounter, Strand5CastingSpeed, Strand6BilletCounter, Strand6CastingSpeed, TodayPlannedProduction, TotalBilletsCount, TotalProduction

## Reads

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, HeatID, HeatReportDate, ID, IsDeleted, MTDPlannedProduction, MonthlyTarget, STD1OSCSpeed, STD2OSCSpeed, STD3OSCSpeed, STD4OSCSpeed, STD5OSCSpeed, STD6OSCSpeed, Strand1BilletCounter, Strand1CastingSpeed, Strand2BilletCounter, Strand2CastingSpeed, Strand3BilletCounter, Strand3CastingSpeed, Strand4BilletCounter, Strand4CastingSpeed, Strand5BilletCounter, Strand5CastingSpeed, Strand6BilletCounter, Strand6CastingSpeed, TodayPlannedProduction, TotalBilletsCount, TotalProduction
- XStudio_Shift_Dtl_Tbl: EndTime, IsDeleted, Name, ParentID, StartTime
- XStudio_Shift_Mst_Tbl: ID
