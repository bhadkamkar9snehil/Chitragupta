---
type: table
title: "Ngconsumption_Summary_Day"
built: "2026-09-24T11:36:36"
---

# Ngconsumption_Summary_Day

Table in XStudio_Xbatch. Rows: 65.

## Identifiers it holds

- NGCons_MTD: same values as key `NGCons_MTD`
- NGCons_YTD: same values as key `NGCons_MTD`

## Written by

- XStudio_Update_Day_Ngconsumption_Usp
- Xstudio_Day_Ngconsumption_Usp

## Read by

- XStudio_Update_Day_Ngconsumption_Usp

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
- NGCong decimal
- Discharged int
- NGCons decimal
- NGconsMMBTPerTon decimal
- ColdDischargeBillet int
- HotDischargeBillet int
- Discharged_MTD int
- HotDischargeBillet_YTD int
- HotDischargeBillet_MTD int
- Discharged_YTD int
- TotalBillet decimal
- TotalNG decimal
- NGCons_MTD int
- TotalNG_YTD decimal
- NGCong_MTD decimal
- ColdDischargeBillet_MTD int
- ColdDischargeBillet_YTD int
- TotalNG_MTD decimal
- NGCong_YTD decimal
- TotalBillet_YTD decimal
- NGCons_YTD int
- TotalBillet_MTD decimal
- AvgResidenceTime int
