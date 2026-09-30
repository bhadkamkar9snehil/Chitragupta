---
type: table
title: "SMS_Production_Summary_Day"
built: "2026-09-24T11:36:36"
---

# SMS_Production_Summary_Day

Table in XStudio_Xbatch. Rows: 314.

## Identifiers it holds

- LastHeatNo: same values as key `HeatNo`

## Written by

- XStudio_Historian_Day_SMS_Production_Usp
- XStudio_Update_Day_SMS_Production_Usp

## Read by

- XStudio_Historian_Day_SMS_Production_Usp
- XStudio_Update_Day_SMS_Production_Usp

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(36)
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
- TodayAchievedpercentage decimal
- MTDPlannedTon decimal
- MonthlyTarget decimal
- TodayPlannedProduction decimal
- Month varchar(100)
- MTDAchievedpercentage decimal
- RunningRate decimal
- TotalProduction decimal
- AskingRate decimal
- Year decimal
- YesterdayAchievedpercentage decimal
- EquipmentID varchar(36)
- TotalProduction_YD decimal
- TotalProduction_MTD decimal
- TodayPlannedProduction_YD decimal
- TotalProduction_YTD decimal
- WeeklyAchievedpercentage decimal
- WeeklyAchievedProduction decimal
- WeeklyTarget decimal
- YearlyTarget decimal
- LastHeatNo int
