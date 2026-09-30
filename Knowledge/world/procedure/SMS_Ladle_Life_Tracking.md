---
type: procedure
title: "SMS_Ladle_Life_Tracking"
built: "2026-09-24T11:36:36"
---

# SMS_Ladle_Life_Tracking

Parameters: @LadleID varchar, @HeatID varchar, @ShellID varchar.

## Writes

- Per_Heat_LadleNo: LadleNoAtEAFDatetime
- XMES_ActiveLife_Element_Mst_Tbl: LastUsedBatch, Source, Status

## Reads

- EAF_PER_HEAT: HeatID, StartTime
- Per_Heat_LadleNo: HeatNo
- XMES_ActiveLife_Element_Mst_Tbl: ElementNameID, IsDeleted
