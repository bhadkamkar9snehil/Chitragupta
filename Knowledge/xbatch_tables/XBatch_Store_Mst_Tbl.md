# XStudio_Xbatch.dbo.XBatch_Store_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference capacity, code, colour, description, enabled, location, sapstorage, unit.

**Primary Key:** ID  
**Row Count:** 6  
**Date Range (ModifiedOn):** 2025-12-11T10:53:15.0000000 to 2026-01-06T11:22:51.0000000  

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
| Capacity | decimal | YES | 18,4 | — |
| CapacityUnitID | varchar | YES | 36 | — |
| Description | varchar | YES | -1 | — |
| IsEnabled | bit | YES | — | — |
| ColourCode | varchar | YES | 50 | — |
| SAPStorageLocation | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 29E9C69B-8BFD-4E0F-ADAD-1D76C7DC4E09 | Furnace | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-09-25T16:43:39.0300000 | 2025-12-11T10:53:15.0000000 | False | False | NULL |
| 7B56A48C-28CC-4BDD-BB9D-6013274487A8 | Mill | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-09-25T16:46:28.5530000 | 2025-12-11T10:54:13.0000000 | False | False | NULL |
| 8298A9CF-5B41-4298-A3CA-DEA299ED2808 | Scrapyard | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-09-10T13:31:14.0870000 | 2026-01-06T11:17:02.0000000 | False | False | NULL |
| DC6EF45C-E82B-4B86-AF22-DB08AF77C4E6 | BilletYard | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-06-25T16:11:41.2730000 | 2026-01-06T11:17:16.0000000 | False | False | NULL |
| C2977D13-3721-4AEC-9631-BBD451C1365E | Shop Floor Raw Materials | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-06T11:22:15.3770000 | 2026-01-06T11:22:15.0000000 | False | False | NULL |
| 59DFBE61-7836-4DB3-BCC1-A587FC3F28EC | SMS Shop Floor | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-06T11:22:51.0470000 | 2026-01-06T11:22:51.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.SAP_Posting_Tbl.StorageLocation` -> `XStudio_XBatch.XBatch_Store_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.XBatch_Storage_Area_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Store_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Store_Mst_Tbl.CapacityUnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Store_Mst_Tbl.SAPStorageLocation` -> `XStudio_XBatch.Storage_Location_MST.ID` (Many to One)
