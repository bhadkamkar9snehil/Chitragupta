---
type: procedure
title: "XStudio_Update_Day_RM_Consumption_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Update_Day_RM_Consumption_Usp

Parameters: @ReportDate date.

## Writes

- RM_Consumption_Summary_Day: ModifiedOn, NGCons_MTD, NGCons_YTD, Source

## Reads

- RM_Consumption_Summary_Day: IsDeleted, NGCons, ReportDate
