# XStudio_Xbatch.dbo.RM_Mill_Event_Configuration_Mst_Tbl

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
| C84F4A30-3096-4F72-8764-C73C9A3663B4 | Billets_Per_Stand_Tracking | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-10-30T11:29:16.5200000 | NULL | False | False | NULL |
| 50BEF313-1A52-46B9-8D3D-583A923B47E0 | Billets_Per_Stand_Tracking | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T11:29:16.5630000 | NULL | False | False | NULL |

---
