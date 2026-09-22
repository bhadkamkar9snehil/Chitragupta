# XStudio_Xbatch.dbo.XBatch_Batch_Phase_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, capability, end, material, original, position, quantity, start, status, template, type.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | NO | 100 | — |
| ParentID | varchar | NO | 36 | — |
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
| Type | varchar | NO | 100 | — |
| CapabilityID | varchar | YES | 36 | — |
| MaterialID | varchar | YES | 36 | — |
| Quantity | decimal | YES | 18,4 | — |
| SrNo | int | NO | 10,0 | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| StatusID | varchar | YES | 36 | — |
| Position | varchar | YES | 100 | — |
| TemplateID | varchar | YES | 36 | — |
| OriginalID | varchar | YES | 36 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.PhaseID` -> `XStudio_XBatch.XBatch_Batch_Phase_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Mst_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_Phase_Group_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Mst_Tbl.StatusID` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Parameter_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_Phase_Mst_Tbl.ID` (Many to One)
