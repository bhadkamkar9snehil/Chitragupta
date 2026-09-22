# XStudio_Xbatch.dbo.Communication_System_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference module, type, area, asset, equipment, identification, idlist, properties, role, template.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-07-27T08:22:09.0000000 to 2026-07-27T08:22:09.0000000  

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
| RoleIDList | varchar | YES | -1 | — |
| ModuleID | varchar | YES | 36 | — |
| ModuleType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6A63684F-1806-4C6B-BD7C-F973AA84463F | PLC_Status | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:22:09.5200000 | 2026-07-27T08:22:09.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Communication_System_Block.EquipmentID` -> `XStudio_XBatch.Communication_System_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Communication_System_Data.EquipmentID` -> `XStudio_XBatch.Communication_System_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Communication_System_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Communication_System_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.Communication_System_Mst_Tbl.ID` (Many to One)
