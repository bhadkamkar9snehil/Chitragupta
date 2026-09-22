# XStudio_Xbatch.dbo.SMS_DATA_DASHBOARD

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference average, heat, noof, tap, weight, cast, charge, mix, power, production, tapping, tapto.

**Primary Key:** ID  
**Row Count:** 1  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| NoofHeatTap | int | YES | 10,0 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| NoofHeatCast | int | YES | 10,0 | — |
| AveragePower | decimal | YES | 18,4 | — |
| AverageTaptoTapTime | varchar | YES | 100 | — |
| AverageChargeMixWeight | decimal | YES | 18,4 | — |
| AverageTappingWeight | decimal | YES | 18,4 | — |
| TodayProduction | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | NoofHeatTap | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 558BF558-2399-4365-BF70-0C68B89858AB | 0 | NULL | NULL | 2025-09-19T12:41:04.2230000 | NULL | False | False | NULL | NULL |

---
