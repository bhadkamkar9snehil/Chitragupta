---
type: procedure
title: "XMES_Cummulative_RMDelay_Entry_USP"
built: "2026-09-24T11:36:36"
---

# XMES_Cummulative_RMDelay_Entry_USP


## Writes

- ShiftDelayEntry: AreaName, DelayDuration, DelayEndTime, DelayInMinutes, DelayInSecond, DelayReason, DelayStartTime, DelayType, OperatorName, RMProduct, RMSection, ReportDate, Shift, ShiftManager, Source

## Reads

- RM_Delays: EndTime, StartTime, Status
- ShiftDelayEntry_Transaction_Operator: IsDeleted, ModifiedOn, Operator, Product, ReportDate, Section, Shift, ShiftManager
