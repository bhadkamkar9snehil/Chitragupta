# XStudio_Xbatch.dbo.XBatch_Storage_Area_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference capacity, description, enabled, grade, type, unit.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2025-09-10T13:32:28.0000000 to 2026-01-06T11:23:59.0000000  

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
| GradeType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A3B967E9-7488-4C91-A170-82156685FC4B | Scrapyard | 8298A9CF-5B41-4298-A3CA-DEA299ED2808 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-10T13:32:01.8200000 | 2025-09-10T13:32:28.0000000 | False | False | NULL |
| 8F1248AD-8102-462B-8351-A0B1CF141DE3 | Stack A | DC6EF45C-E82B-4B86-AF22-DB08AF77C4E6 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-06-25T16:14:12.6930000 | 2025-09-11T10:56:38.0000000 | False | False | NULL |
| 8F251D9B-34FC-4CF3-B00C-7578857583CA | Stack B | DC6EF45C-E82B-4B86-AF22-DB08AF77C4E6 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-06-25T16:15:52.6300000 | 2025-09-11T11:01:14.0000000 | False | False | NULL |
| AAAD80E9-72E3-41F5-9472-5C6D464B9E96 | Stack C | DC6EF45C-E82B-4B86-AF22-DB08AF77C4E6 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-06-25T16:14:55.5730000 | 2025-09-11T11:01:51.0000000 | False | False | NULL |
| 02E5D1F5-139C-46DD-9F7A-303C1E22AD2A | Stack D | DC6EF45C-E82B-4B86-AF22-DB08AF77C4E6 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-06-25T16:16:14.7630000 | 2025-09-11T11:01:55.0000000 | False | False | NULL |
| 36905E99-E126-41D5-AC7C-49525DF6F6E8 | Stack E | DC6EF45C-E82B-4B86-AF22-DB08AF77C4E6 | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 99D414BA-932E-4B50-851B-9750A6ECB16A | 2025-06-25T16:16:29.4430000 | 2025-09-11T11:01:59.0000000 | False | False | NULL |
| CD315EF2-798A-4F85-8F33-FCD0DBC4D729 | Furnace | 29E9C69B-8BFD-4E0F-ADAD-1D76C7DC4E09 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-25T16:44:14.4700000 | 2025-09-25T16:44:14.0000000 | False | False | NULL |
| 02A14F00-DCD7-4E18-9587-65D08F151B82 | Mill | 7B56A48C-28CC-4BDD-BB9D-6013274487A8 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-30T13:06:00.2300000 | 2025-09-30T13:06:00.0000000 | False | False | NULL |
| D54AE55E-6CEF-45EA-A583-20859F8660F7 | Shop Floor Raw Materials | C2977D13-3721-4AEC-9631-BBD451C1365E | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-06T11:23:16.6970000 | 2026-01-06T11:23:16.0000000 | False | False | NULL |
| CB24F7D8-D49E-4EBE-BC58-4CDE85FF98D0 | SMS Shop Floor | 59DFBE61-7836-4DB3-BCC1-A587FC3F28EC | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-01-06T11:23:59.8600000 | 2026-01-06T11:23:59.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Storage_Area_Mst_Tbl.CapacityUnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Storage_Area_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Store_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Storage_Rack_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Storage_Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_UpdateStackLocation.StackID` -> `XStudio_XBatch.XBatch_Storage_Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Xstudio_Xbatch_ChargingPlan_Mst_Tbl.Stackid` -> `XStudio_XBatch.XBatch_Storage_Area_Mst_Tbl.ID` (Many to One)
