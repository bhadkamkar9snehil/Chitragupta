---
type: procedure
title: "XMES_Delay_Split_Entry_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_Delay_Split_Entry_Usp

Parameters: @ID varchar, @SplitDT varchar, @Userid varchar.

## Writes

- ShiftDelayEntry: AreaName, DelayEndTime, DelayStartTime, HeatNo, ID, Issplit, ModifiedBy, ModifiedOn, Source

## Reads

- ShiftDelayEntry: IsDeleted
