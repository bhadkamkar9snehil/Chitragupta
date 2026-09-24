---
type: procedure
title: "MES_U_Delay_Merge"
built: "2026-09-24T11:36:36"
---

# MES_U_Delay_Merge

Parameters: @UserId varchar, @SystemId varchar, @RecordIds varchar, @Status varchar, @DataCollection nvarchar.

## Writes

- ShiftDelayEntry: AreaName, DelayEndTime, DelayStartTime, HeatNo, IsDeleted, ReportDate, SMSReportDate

## Reads

- ShiftDelayEntry: ID
