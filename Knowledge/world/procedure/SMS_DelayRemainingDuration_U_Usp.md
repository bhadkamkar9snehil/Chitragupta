---
type: procedure
title: "SMS_DelayRemainingDuration_U_Usp"
built: "2026-09-24T11:36:36"
---

# SMS_DelayRemainingDuration_U_Usp

Parameters: @MSTDelayID varchar, @AgencyID varchar.

## Writes

- Agency_Wise_Delay: RemainingDuration
- ShiftDelayEntry: RemainingDuration

## Reads

- Agency_Wise_Delay: Duration, ID, IsDeleted, ParentID
- Equipment_Wise_Delay: Duration, IsDeleted, ParentID
- ShiftDelayEntry: DelayInMinutes, ID
