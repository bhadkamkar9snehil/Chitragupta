# XStudio_Xbatch.dbo.RM_Furnace_Combustion_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference module, type, area, equipment, template.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-08-14T12:49:14.0000000 to 2026-08-14T12:49:14.0000000  

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
| EquipmentTypeID | varchar | YES | 36 | — |
| TemplateID | varchar | YES | 36 | — |
| AreaID | varchar | YES | 36 | — |
| ModuleID | varchar | YES | 36 | — |
| ModuleType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0E50E6EA-7769-4A41-B526-8E94258584B3 | RM_Furnace_Combustion | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-08-14T12:49:14.4870000 | 2026-08-14T12:49:14.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Furnace_Combustion_5.EquipmentID` -> `XStudio_XBatch.RM_Furnace_Combustion_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Furnace_Combustion_Data.EquipmentID` -> `XStudio_XBatch.RM_Furnace_Combustion_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Furnace_Combustion_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Furnace_Combustion_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.RM_Furnace_Combustion_Mst_Tbl.ID` (Many to One)
