---
type: table
title: "SMS_Production_Summary"
built: "2026-09-24T11:36:36"
---

# SMS_Production_Summary

Table in XStudio_Xbatch. Rows: 44,051.

## Identifiers it holds

- Particulars: same values as key `Particulars`

## Written by

- SP_SMS_Producation_Summary
- XMES_U_SMS_Production_Summary_BestData_Usp
- Xstudio_SMS_Production_Summary_USP

## Read by

- SP_SMS_OEE_Daily_View
- SP_SMS_Producation_Summary
- XBatch_OEE_Dashboard_SP
- XMES_SMS_Dashboard_Delay_USP
- XMES_SMS_Production_Summary_Flashcard_Report_SP
- XMES_U_SMS_Production_Summary_BestData_Usp
- XStudio_Get_SMS_Monthly_Production_Summary
- Xstudio_SMS_Production_Summary_USP

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
- Reportdatetext varchar(100)
- Target decimal
- FTDPercentage decimal
- BestMonth decimal
- ReportDate date
- Particulars varchar(36)
- Type varchar(100)
- FTDTon decimal
- EntryDateTime datetime
- IsProcessed bit
- MTDTon decimal
- ParentID varchar(36)
- BestDay decimal
- Name varchar(100)
- UOM varchar(36)
- MTDPercentage decimal
- BestDayDate date
- BestMonthDate date
- MonthYear varchar(100)
