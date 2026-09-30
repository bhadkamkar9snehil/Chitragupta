---
type: procedure
title: "XMES_Schedule_SP_to_Refresh_Data_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_Schedule_SP_to_Refresh_Data_Usp

Parameters: @ID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- XMES_Recalculate_Data: ID, IsDeleted, Name, ReportDate, StoreProcedure

## Calls

- XStudio_Schedule_TSQL_Task_Usp
