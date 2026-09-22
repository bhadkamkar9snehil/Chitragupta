# XStudio_Xbatch.dbo.XBatch_Formula_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference description, enabled, quantity, unit.

**Primary Key:** ID  
**Row Count:** 2  
**Date Range (ModifiedOn):** 2025-12-22T15:40:46.0000000 to 2026-03-20T11:36:23.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | NO | 100 | — |
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
| Quantity | decimal | NO | 18,4 | — |
| UnitID | varchar | NO | 36 | — |
| Description | varchar | YES | -1 | — |
| IsEnabled | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01E84C1E-21E4-4A5F-B9B9-5673923E014A | Billet_Production_130X130 | 66F72F78-A6F3-4524-B983-10E92F1F6C7D | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-11T13:19:21.5730000 | 2025-12-22T15:40:46.0000000 | False | False | NULL |
| 46D7708D-6101-4961-A584-92EF5C4BC0D0 | BL_HHMN_16RC_150X150 | 82BA40F7-5AE4-46DE-A0E9-101F782A5FBE | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-03-20T11:36:10.2030000 | 2026-03-20T11:36:23.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Billet_Inventory.BOMid` -> `XStudio_XBatch.XBatch_Formula_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Billet_Inventory_View.BOMid` -> `XStudio_XBatch.XBatch_Formula_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Dtl_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Formula_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Formula_Mst_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
