# XStudio_Xbatch.dbo.XBatch_OutwardLocation_Mst_Tbl

**table_kind:** production_data

### What this table is for

- No curated business description or distinguishing column vocabulary found for this table; treat as low-confidence for semantic matching.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-09-17T14:11:17.0000000 to 2025-09-17T14:11:46.0000000  

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

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 41564A24-7812-4F0A-B342-E82ABF01AA19 | Mill | NULL | 99D414BA-932E-4B50-851B-9750A6ECB16A | NULL | 2025-09-24T16:37:10.5830000 | NULL | False | False | NULL |
| 0577F0AF-E2B7-42A8-BB52-F899942B0901 | Sydan | NULL | 99D414BA-932E-4B50-851B-9750A6ECB16A | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-09-17T14:11:17.3770000 | 2025-09-17T14:11:17.0000000 | False | False | NULL |
| BA4E547C-12D7-4758-B557-F7362E94D898 | Furnace | NULL | 99D414BA-932E-4B50-851B-9750A6ECB16A | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-09-17T14:11:38.2230000 | 2025-09-17T14:11:38.0000000 | False | False | NULL |
| CF0D9AC0-33B4-4AFB-AF62-4C395120C866 | RM | NULL | 99D414BA-932E-4B50-851B-9750A6ECB16A | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-09-17T14:11:46.9270000 | 2025-09-17T14:11:46.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.OutwardLocation` -> `XStudio_XBatch.XBatch_OutwardLocation_Mst_Tbl.ID` (Many to One)
