# XStudio_Xbatch.dbo.Round_Steps_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference page, entity, equipment, isscanable, physical, record, round, status, tag, view.

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
| RoundID | varchar | YES | 36 | — |
| EntityID | varchar | YES | 36 | — |
| EquipmentID | varchar | YES | 36 | — |
| PageID | varchar | YES | 36 | — |
| ViewPageID | varchar | YES | 36 | — |
| RecordID | varchar | YES | 36 | — |
| EntryDateTime | datetime | YES | — | — |
| Status | varchar | YES | 50 | — |
| Isscanable | bit | YES | — | — |
| PhysicalTag | varchar | YES | 100 | — |

---
