---
type: procedure
title: "XMES_Water_Reading_Recalculate_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_Water_Reading_Recalculate_Usp

Parameters: @Reportdate date.

## Writes

- MES_Logbook_Water_Reading: EntirePlantReadingDifference, RMReadingDifference, SMSReadingDifference

## Reads

- MES_Logbook_Water_Reading: EntirePlantFMReading, ID, IsDeleted, RMFMReading, ReportDate, SMSFMReading
