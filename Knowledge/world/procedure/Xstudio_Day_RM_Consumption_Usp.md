---
type: procedure
title: "Xstudio_Day_RM_Consumption_Usp"
built: "2026-09-24T11:36:36"
---

# Xstudio_Day_RM_Consumption_Usp

Parameters: @ID varchar, @DatabaseName varchar, @EntityName varchar.

## Writes

- RM_Consumption_Summary_Day: ModifiedOn, NGCons, ReportDate, Source

## Reads

- RM_NGConsumption: Date, ID, IsDeleted, NGCons

## Calls

- XStudio_Update_Day_RM_Consumption_Usp
