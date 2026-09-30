---
type: procedure
title: "SMS_EquipmentWiseDelayDuration_Validation_Usp"
built: "2026-09-24T11:36:36"
---

# SMS_EquipmentWiseDelayDuration_Validation_Usp

Parameters: @ID varchar, @Duration decimal, @Equipment nvarchar.

## Reads

- Agency_Wise_Delay: Duration, ID, IsDeleted
- Equipment_Wise_Delay: Duration, EquipmentName, IsDeleted, ParentID
