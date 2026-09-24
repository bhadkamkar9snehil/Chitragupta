---
type: table
title: "Electricity_Meter_Electricity_Rate_Tbl_Mst"
built: "2026-09-24T11:36:36"
---

# Electricity_Meter_Electricity_Rate_Tbl_Mst

Table in XStudio_Xbatch. Rows: 12.

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
- OffPeak int
- Months varchar(-1)
- NightPeak int
- WeekdayDayPeak int
- WeekendDayPeak int
- Year varchar(-1)
- EntryDatetime datetime
