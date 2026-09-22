# XStudio_Xbatch.dbo.XBatch_ConfigParameter_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference description, value, visible.

**Primary Key:** ID  
**Row Count:** 2  

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
| Value | varchar | YES | -1 | — |
| Description | varchar | YES | -1 | — |
| IsVisible | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 741147FE-808B-47A5-8033-4A82C0F82D25 | HistorianApiEndpoint | NULL | NULL | NULL | 2023-07-20T15:56:46.6930000 | NULL | False | False | NULL |
| 181F4D99-4B3B-478E-9137-98966AC4DB39 | BatchServerWCFEndpoint | NULL | NULL | NULL | 2023-07-20T15:57:02.4270000 | NULL | False | False | NULL |

---
