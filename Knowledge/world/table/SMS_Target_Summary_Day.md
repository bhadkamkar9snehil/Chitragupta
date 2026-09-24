---
type: table
title: "SMS_Target_Summary_Day"
built: "2026-09-24T11:36:36"
---

# SMS_Target_Summary_Day

Table in XStudio_Xbatch. Rows: 378.

## Identifiers it holds

- HeatID: same values as key `HeatNo`

## Written by

- XBatch_Add_Default_Heat_start_end_Usp
- XBatch_Add_Heat_start_end_Usp
- XStudio_Update_Day_SMS_Target_Usp
- Xstudio_Day_SMS_Target_Usp

## Read by

- SP_SMS_OEE_Daily_View
- XBatch_Add_Default_Heat_start_end_Usp
- XBatch_Add_Heat_start_end_Usp
- XBatch_OEE_Dashboard_SP
- XMES_SMS_Production_Summary_Flashcard_Report_SP
- XStudio_Update_Day_SMS_Target_Usp
- Xstudio_Day_SMS_Target_Usp

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
- AskingRate decimal
- TodayPlannedProduction decimal
- YearlyTarget decimal
- WeeklyTarget decimal
- ActualBilletWeightTon decimal
- TodayAchievedpercentage decimal
- MTDPlannedProduction decimal
- MTDAchievedpercentage decimal
- MonthlyTarget decimal
- WeeklyAchievedProduction decimal
- RunningRate decimal
- WeeklyAchievedpercentage decimal
- TodayAchievedpercentage_YD decimal
- TodayPlannedProduction_YD decimal
- ActualBilletWeightTon_YTD decimal
- ActualBilletWeightTon_MTD decimal
- ActualBilletWeightTon_YD decimal
- Month varchar(100)
- HeatID int
- Year int
