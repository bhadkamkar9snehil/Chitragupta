---
type: procedure
title: "XStudio_Update_Day_SMS_Production_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Update_Day_SMS_Production_Usp

Parameters: @ReportDate date.

## Writes

- SMS_Production_Summary_Day: ModifiedOn, Source, TodayPlannedProduction_YD, TotalProduction_MTD, TotalProduction_YD, TotalProduction_YTD

## Reads

- SMS_Production_Summary_Day: EquipmentID, IsDeleted, ReportDate, TodayPlannedProduction, TotalProduction
