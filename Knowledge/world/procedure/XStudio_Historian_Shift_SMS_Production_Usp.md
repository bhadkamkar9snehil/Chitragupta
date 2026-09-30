---
type: procedure
title: "XStudio_Historian_Shift_SMS_Production_Usp"
built: "2026-09-24T11:36:36"
---

# XStudio_Historian_Shift_SMS_Production_Usp

Parameters: @Entrydatetime datetime, @DatabaseName varchar, @EntityName varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- SMS_Production_Summary_Shift: Entrydatetime, EquipmentID, ShiftName, Source

## Reads

- CCM_SMS_Mst_Tbl: ID, IsDeleted, TemplateID
- XStudio_Shift_Dtl_Tbl: EndTime, IsDeleted, Name, ParentID, StartTime
- XStudio_Shift_Mst_Tbl: ID
