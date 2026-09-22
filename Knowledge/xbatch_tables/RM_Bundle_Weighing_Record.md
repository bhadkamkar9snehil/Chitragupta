# XStudio_Xbatch.dbo.RM_Bundle_Weighing_Record

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference bundle, number, grade, heat, quality, remarks, shift, size, weight.

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
| Shift | varchar | YES | 100 | — |
| Size | int | YES | 10,0 | — |
| QualityOrGrade | varchar | YES | 100 | — |
| SlNo | int | YES | 10,0 | — |
| HeatNumber | int | YES | 10,0 | — |
| BundleNumber | int | YES | 10,0 | — |
| BundleWeight | decimal | YES | 18,4 | — |
| Remarks | varchar | YES | 100 | — |

---
