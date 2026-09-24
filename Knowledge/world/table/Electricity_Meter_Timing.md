---
type: table
title: "Electricity_Meter_Timing"
built: "2026-09-24T11:36:36"
---

# Electricity_Meter_Timing

Table in XStudio_Xbatch. Rows: 8.

## Read by

- XMES_Electricity_Bill_Calculator_USP

## Columns

- ID varchar(36)
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
- RateBand varchar(36)
- FromTime time
- ToTime time
- DayOfWeek varchar(100)
- SrNo int
- Year varchar(-1)
- EntryDatetime datetime
- Weekdays varchar(100)
- ColorCode varchar(50)
