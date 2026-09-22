# XStudio_Xbatch.dbo.LayerConfiguration

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference capacity, decrement, min, start, value.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-09-15T15:11:05.0000000 to 2025-09-15T15:11:05.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| ParentID | varchar | YES | 36 | — |
| Name | varchar | YES | 100 | — |
| decrementValue | int | YES | 10,0 | — |
| StartCapacity | int | YES | 10,0 | — |
| MinCapacity | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 90DC2C37-741B-4413-B158-0713CBDCFAF9 | 99D414BA-932E-4B50-851B-9750A6ECB16A | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-09-11T10:43:11.0300000 | 2025-09-15T15:11:05.0000000 | False | False | NULL | 172.16.3.201 |  |

---
