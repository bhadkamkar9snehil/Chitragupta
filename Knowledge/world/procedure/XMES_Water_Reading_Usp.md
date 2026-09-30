---
type: procedure
title: "XMES_Water_Reading_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_Water_Reading_Usp

Parameters: @ID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- MES_Logbook_Water_Reading: EntirePlantReadingDifference, RMReadingDifference, SMSReadingDifference

## Reads

- MES_Logbook_Water_Reading: CommonFMReading, EntirePlantFMReading, ID, IsDeleted, RMFMReading, ReportDate, SMSFMReading

## Calls

- XMES_RM_Raw_Material_Entry_Usp
