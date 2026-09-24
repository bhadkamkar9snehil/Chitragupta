---
type: procedure
title: "Xstudio_Day_CCM_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Day_CCM_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- CCM_Summary_Day: ActualBilletCount, ActualBilletWeightTon, HeatID, MTDPlannedProduction, ModifiedOn, MonthlyTarget, ReportDate, STD1OSCSpeed, STD2OSCSpeed, STD3OSCSpeed, STD4OSCSpeed, STD5OSCSpeed, STD6OSCSpeed, Source, Strand1BilletCounter, Strand1CastingSpeed, Strand2BilletCounter, Strand2CastingSpeed, Strand3BilletCounter, Strand3CastingSpeed, Strand4BilletCounter, Strand4CastingSpeed, Strand5BilletCounter, Strand5CastingSpeed, Strand6BilletCounter, Strand6CastingSpeed, TodayPlannedProduction, TotalBilletsCount, TotalProduction

## Reads

- CCM_Per_Heat: ActualBilletCount, ActualBilletWeightTon, HeatID, HeatReportDate, ID, IsDeleted, MTDPlannedProduction, MonthlyTarget, STD1OSCSpeed, STD2OSCSpeed, STD3OSCSpeed, STD4OSCSpeed, STD5OSCSpeed, STD6OSCSpeed, Strand1BilletCounter, Strand1CastingSpeed, Strand2BilletCounter, Strand2CastingSpeed, Strand3BilletCounter, Strand3CastingSpeed, Strand4BilletCounter, Strand4CastingSpeed, Strand5BilletCounter, Strand5CastingSpeed, Strand6BilletCounter, Strand6CastingSpeed, TotalBilletsCount, TotalProduction
- CCM_Summary_Day: TotalProduction_YD

## Calls

- XStudio_Update_Day_CCM_Usp
