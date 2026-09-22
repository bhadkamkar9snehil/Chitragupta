# XStudio_Xbatch.dbo.CCM_SMS_Event_Mst_Tbl

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
| 91E20AF1-8EC8-4064-A1C0-83D620037C08 | Delays | 40aa7b7d-0507-42bf-bf22-3e841053c72d | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-09-02T07:49:44.0000000 | NULL | False | False | NULL |
| 911F7246-39BE-4431-B0B8-8E677DB83C72 | Billet Tracking Strandwise | 40aa7b7d-0507-42bf-bf22-3e841053c72d | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2026-05-10T07:42:32.0000000 | NULL | False | False | NULL |

---
