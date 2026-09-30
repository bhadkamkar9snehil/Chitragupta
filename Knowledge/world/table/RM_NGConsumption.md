---
type: table
title: "RM_NGConsumption"
built: "2026-09-24T11:36:36"
---

# RM_NGConsumption

Table in XStudio_Xbatch. Rows: 8,182.

## Written by

- SP_ReCalculate_NG_Configuration_Block_USP (text)
- Xstudio_Historian_RM_NGConsumption_Report_usp (text)
- Xstudio_RM_NGConsumption_USP

## Read by

- XMES_RM_Production_Summary_Usp
- Xstudio_Day_Ngconsumption_Usp
- Xstudio_Day_RM_Consumption_Usp
- Xstudio_RM_NGConsumption_USP

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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Date date
- FromTime datetime
- ToTime datetime
- RollingSize varchar(100)
- Grade varchar(100)
- Billet130Hot int
- Billet130Cold int
- Billet140Cold int
- Billet140Hot int
- Billet150Hot int
- Billet150Cold int
- Discharged int
- TotalBillet decimal
- NGCong decimal
- NGCons int
- TotalNG decimal
- CP1Operator varchar(36)
- Crosssection int
- Shift varchar(100)
- HotDischargeBillet int
- ColdDischargeBillet int
- NGconsMMBTPerTon decimal
- AvgResidenceTime int
