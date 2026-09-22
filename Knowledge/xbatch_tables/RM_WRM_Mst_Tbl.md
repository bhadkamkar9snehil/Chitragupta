# XStudio_Xbatch.dbo.RM_WRM_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference module, type, area, asset, equipment, identification, properties, template.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-09-16T15:26:29.0000000 to 2025-09-16T15:26:29.0000000  

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
| AssetIdentificationProperties | varchar | YES | -1 | — |
| ModuleID | varchar | YES | 36 | — |
| ModuleType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3ED74825-A26A-4C87-8198-A8B507890686 | WRM | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-16T15:26:29.6970000 | 2025-09-16T15:26:29.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_WRM_Block.EquipmentID` -> `XStudio_XBatch.RM_WRM_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_WRM_Data.EquipmentID` -> `XStudio_XBatch.RM_WRM_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_WRM_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_WRM_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.RM_WRM_Mst_Tbl.ID` (Many to One)
