---
type: procedure
title: "XStudio_Update_Day_SMS_Target_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Update_Day_SMS_Target_Usp

Parameters: @ReportDate date.

## Writes

- SMS_Target_Summary_Day: ActualBilletWeightTon_MTD, ActualBilletWeightTon_YD, ActualBilletWeightTon_YTD, ModifiedOn, Source, TodayAchievedpercentage_YD, TodayPlannedProduction_YD

## Reads

- SMS_Target_Summary_Day: ActualBilletWeightTon, IsDeleted, ReportDate, TodayAchievedpercentage, TodayPlannedProduction
