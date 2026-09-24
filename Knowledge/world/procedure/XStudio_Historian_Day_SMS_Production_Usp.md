---
type: procedure
title: "XStudio_Historian_Day_SMS_Production_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Historian_Day_SMS_Production_Usp

Parameters: @Entrydate datetime, @DatabaseName varchar, @EntityName varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- SMS_Production_Summary_Day: AskingRate, EquipmentID, MTDAchievedpercentage, ModifiedOn, Month, ReportDate, RunningRate, Source, TodayAchievedpercentage, TodayPlannedProduction, WeeklyAchievedProduction, WeeklyAchievedpercentage, Year, YesterdayAchievedpercentage

## Reads

- CCM_SMS_Mst_Tbl: ID, IsDeleted, TemplateID
- ProductionWeeklyTargets: WeekEndTime, WeekStartTime
- SMS_Production_Summary_Day: MTDPlannedTon, MonthlyTarget, ReportDate, TodayPlannedProduction_YD, TotalProduction, TotalProduction_MTD, TotalProduction_YD, WeeklyTarget

## Calls

- XStudio_Update_Day_SMS_Production_Usp
