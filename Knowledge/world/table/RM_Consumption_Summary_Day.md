---
type: table
title: "RM_Consumption_Summary_Day"
built: "2026-09-24T11:36:36"
---

# RM_Consumption_Summary_Day

Table in XStudio_Xbatch. Rows: 326.

## Identifiers it holds

- NGCons_MTD: same values as key `NGCons_MTD`

## Written by

- XStudio_Update_Day_RM_Consumption_Usp
- Xstudio_Day_RM_Consumption_Usp

## Read by

- XMES_Power_Consumption_report_Usp
- XMES_U_Power_consumption_Report_Usp
- XStudio_Update_Day_RM_Consumption_Usp

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
- ReportDate date
- NGCons int
- NGCons_MTD int
- NGCons_YTD int
