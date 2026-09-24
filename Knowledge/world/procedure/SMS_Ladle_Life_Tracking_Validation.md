---
type: procedure
title: "SMS_Ladle_Life_Tracking_Validation"
built: "2026-09-24T11:36:36"
---

# SMS_Ladle_Life_Tracking_Validation

Parameters: @LadleID varchar, @HeatID varchar.

## Reads

- Life_Tracking_Transaction_tbl: HeatID, IsDeleted, LifeType
- XMES_Life_Element_Mst_Tbl: ID, Name
