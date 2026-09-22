# XStudio_Xbatch.dbo.EAF_SMS_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference module, type, area, equipment, template.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-07-11T11:48:33.0000000 to 2025-07-11T11:48:33.0000000  

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
| BCC64E43-7BF7-47FF-8A35-BCA3B6F4DAEB | Electric_Arc_Furnace | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11T11:48:33.8200000 | 2025-07-11T11:48:33.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_Custom.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_PER_HEAT.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_ProcessTime.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_SMS_5.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_SMS_Block.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_SMS_Data.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_SMS_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_SMS_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.EAF_SMS_Mst_Tbl.ID` (Many to One)
