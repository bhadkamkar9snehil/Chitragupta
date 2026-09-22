# XStudio_Xbatch.dbo.Tool_Breakage_Report

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference breakage, damage, details, for, new, operation, reason, remarks, time, type, used, wheel.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
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
| TypeOfWheelDetails | varchar | YES | 100 | — |
| New | varchar | YES | 100 | — |
| Used | varchar | YES | 100 | — |
| OperationAtTimeOfBreakageOrDamage | varchar | YES | 100 | — |
| ReasonForBreakageOrDamage | varchar | YES | 100 | — |
| Remarks | varchar | YES | -1 | — |

---
