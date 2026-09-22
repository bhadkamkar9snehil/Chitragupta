# XStudio_Xbatch.dbo.RM_TC_Grinding_Logbook_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference roll, breakage, damage, diameter, time, after, before, cncoperator, code, condition, date, datetime.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
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
| CNCOperatorName | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| RingNo | int | YES | 10,0 | — |
| GrooveCode | int | YES | 10,0 | — |
| StdNo | int | YES | 10,0 | — |
| Section | varchar | YES | 100 | — |
| RollLoadingDateTime | datetime | YES | — | — |
| JobDescription | varchar | YES | 100 | — |
| RollDiameterBefore | int | YES | 10,0 | — |
| RollDiameterAfter | int | YES | 10,0 | — |
| RollUnloadingDatetime | datetime | YES | — | — |
| PassCondition | varchar | YES | 100 | — |
| Remarks | varchar | YES | 100 | — |
| TypeOfWheelDetails | varchar | YES | 100 | — |
| New | int | YES | 10,0 | — |
| Used | int | YES | 10,0 | — |
| OperationAtTimeOfBreakageOrDamage | datetime | YES | — | — |
| ReasonForBreakageOrDamage | varchar | YES | 100 | — |

---
