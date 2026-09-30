---
type: procedure
title: "ShiftDelayEntry_ManagerOperatorName_Usp"
built: "2026-09-24T11:36:36"
---

# ShiftDelayEntry_ManagerOperatorName_Usp

Parameters: @ID varchar, @ShiftManager varchar, @OperatorName varchar, @DelayReason varchar.

## Writes

- ShiftDelayEntry: DelayReason, OperatorName, ShiftManager

## Reads

- ShiftDelayEntry: ID
