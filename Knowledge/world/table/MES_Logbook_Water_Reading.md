---
type: table
title: "MES_Logbook_Water_Reading"
built: "2026-09-24T11:36:36"
---

# MES_Logbook_Water_Reading

Table in XStudio_Xbatch. Rows: 244.

## Written by

- XMES_Water_Reading_Recalculate_Usp
- XMES_Water_Reading_Usp

## Read by

- XMES_RM_Production_Summary_Usp
- XMES_Water_Reading_Recalculate_Usp
- XMES_Water_Reading_Usp

## Columns

- ID varchar(36)
- CommonFMReading int
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- ReportDate date
- IsProcessed bit
- RMFMReading int
- SMSFMReading int
- MillScale decimal
- SMSScale decimal
- EntirePlantFMReading int
- RMReadingDifference int
- SMSReadingDifference int
- EntirePlantReadingDifference int
