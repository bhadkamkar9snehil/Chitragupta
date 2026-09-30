---
type: procedure
title: "Xstudio_Day_SMS_Target_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Day_SMS_Target_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- SMS_Target_Summary_Day: ActualBilletWeightTon, AskingRate, HeatID, MTDAchievedpercentage, MTDPlannedProduction, ModifiedOn, Month, MonthlyTarget, ReportDate, RunningRate, Source, TodayAchievedpercentage, TodayPlannedProduction, WeeklyAchievedProduction, WeeklyAchievedpercentage, WeeklyTarget, Year, YearlyTarget

## Reads

- CCM_Per_Heat: ActualBilletWeightTon, HeatID, HeatReportDate, ID, IsDeleted, Month, MonthlyTarget, WeeklyTarget, Year, YearlyTarget
- ProductionWeeklyTargets: WeekEndTime, WeekStartTime
- SMS_Target_Summary_Day: ActualBilletWeightTon, ActualBilletWeightTon_MTD, ReportDate

## Calls

- XStudio_Update_Day_SMS_Target_Usp
