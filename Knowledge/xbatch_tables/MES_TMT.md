# XStudio_Xbatch.dbo.MES_TMT

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference length, time, batch, billet, cut, heat, out, remain, status, workorder.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| BatchNo | varchar | YES | 100 | — |
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
| InTime | datetime | YES | — | — |
| OutTime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Status | varchar | YES | 50 | — |
| CutLength | decimal | YES | 18,4 | — |
| RemainLength | decimal | YES | 18,4 | — |
| HeatNo | varchar | YES | 100 | — |
| BilletNo | varchar | YES | 100 | — |
| workorder | varchar | YES | 36 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_TMT.ID` -> `XStudio_XBatch.MES_TMT_Small_Cut.ParentID` (Many to One)
- `XStudio_XBatch.MES_TMT.workorder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_TMT_Small_Cut.ID` -> `XStudio_XBatch.MES_TMT.ParentID` (Many to One)
