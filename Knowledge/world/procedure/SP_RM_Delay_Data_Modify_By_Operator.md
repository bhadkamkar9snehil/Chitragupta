---
type: procedure
title: "SP_RM_Delay_Data_Modify_By_Operator"
built: "2026-09-24T11:36:36"
---

# SP_RM_Delay_Data_Modify_By_Operator

Parameters: @Reportdate varchar, @Shift varchar, @Product varchar, @Section varchar, @Operator varchar, @ShiftManager varchar.

## Writes

- ShiftDelayEntry: OperatorName, RMProduct, RMSection, ShiftManager

## Reads

- ShiftDelayEntry: AreaName, IsDeleted, ReportDate, Shift
