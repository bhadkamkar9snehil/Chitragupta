# XStudio_Xbatch.dbo.LRF_SMS_Event_Configuration_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference event, active, entity, mst, transaction, type.

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
| EventMstID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5964F6BE-5076-4101-BFDA-3434DA53DE8D | LRF_ProcessTime | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-23T13:46:02.1170000 | NULL | False | False | NULL |
| 3A4A0C4A-249A-4772-A956-38A6FC8699DF | LRF_Per_HeatData | 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | NULL | NULL | 2025-07-22T12:56:55.7330000 | NULL | False | False | NULL |

---
