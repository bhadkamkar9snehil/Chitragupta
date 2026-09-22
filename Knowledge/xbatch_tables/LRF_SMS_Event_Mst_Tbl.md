# XStudio_Xbatch.dbo.LRF_SMS_Event_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference active, entity, event, transaction, type.

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
| EventType | varchar | YES | 100 | — |
| TransactionEntity | varchar | YES | 100 | — |
| IsActive | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7CB7E84B-2D97-4B26-ACA0-9AB4EB87E98A | LRF_Per_HeatData | daf22a63-e305-47f0-8ff1-11521ed545e6 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | NULL | 2025-07-22T12:56:55.0000000 | NULL | False | False | NULL |
| 01EBE60E-6E2E-4C1B-9470-758F66BB7DB2 | LRF_ProcessTime | daf22a63-e305-47f0-8ff1-11521ed545e6 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | NULL | 2025-07-23T13:46:02.0000000 | NULL | False | False | NULL |

---
