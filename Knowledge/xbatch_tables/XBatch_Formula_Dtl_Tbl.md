# XStudio_Xbatch.dbo.XBatch_Formula_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference quantity, description, enabled, material, max, min, type, unit.

**Primary Key:** ID  
**Row Count:** 6  
**Date Range (ModifiedOn):** 2025-12-11T13:21:58.0000000 to 2026-03-20T11:38:34.0000000  

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
| MaterialID | varchar | NO | 36 | — |
| UnitID | varchar | NO | 36 | — |
| Quantity | decimal | NO | 18,4 | — |
| QuantityType | varchar | YES | 100 | — |
| Description | varchar | YES | -1 | — |
| IsEnabled | bit | YES | — | — |
| MinQuantity | decimal | YES | 18,4 | — |
| MaxQuantity | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E7C2A1A0-5036-45EC-B33E-625EB5805DAF | NULL | 01E84C1E-21E4-4A5F-B9B9-5673923E014A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-11T13:21:58.3030000 | 2025-12-11T13:21:58.0000000 | False | False | NULL |
| D58FB9F5-AD57-4745-8DA4-4B2019605BD4 | NULL | 01E84C1E-21E4-4A5F-B9B9-5673923E014A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-11T13:39:49.2530000 | 2025-12-11T13:39:49.0000000 | False | False | NULL |
| B7072ABF-2EAD-47EA-B354-5EEAE100676C | NULL | 01E84C1E-21E4-4A5F-B9B9-5673923E014A | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-11T13:43:07.7630000 | 2025-12-23T14:22:48.0000000 | False | False | NULL |
| D4326CD9-EF33-4D10-B453-C11B41E8CEE0 | NULL | 46D7708D-6101-4961-A584-92EF5C4BC0D0 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-03-20T11:36:41.1570000 | 2026-03-20T11:37:24.0000000 | False | False | NULL |
| A54FE753-81C9-4432-A244-5923DFC24D21 | NULL | 46D7708D-6101-4961-A584-92EF5C4BC0D0 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-03-20T11:37:46.9200000 | 2026-03-20T11:38:12.0000000 | False | False | NULL |
| C521C0C9-D448-4539-890E-6DB80E998CCE | NULL | 46D7708D-6101-4961-A584-92EF5C4BC0D0 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-03-20T11:38:12.1500000 | 2026-03-20T11:38:34.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Formula_Dtl_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Dtl_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Formula_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Dtl_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
