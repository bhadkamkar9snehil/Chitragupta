# XStudio_Xbatch.dbo.Xstudio_Xbatch_ChargingPlan_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference stackid.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-09-24T18:08:47.8100000 to 2025-09-24T18:08:47.8100000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Stackid | varchar | YES | -1 | — |
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

### Top 10 Records

| ID | Stackid | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B9D1E5A0-32C0-4AEF-96FE-9C9AB1A3562A | 02E5D1F5-139C-46DD-9F7A-303C1E22AD2A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-23T18:32:24.9100000 | 2025-09-24T18:08:47.8100000 | False | False | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Xstudio_Xbatch_ChargingPlan_Mst_Tbl.Stackid` -> `XStudio_XBatch.XBatch_Storage_Area_Mst_Tbl.ID` (Many to One)
