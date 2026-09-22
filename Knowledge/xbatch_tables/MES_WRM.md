# XStudio_Xbatch.dbo.MES_WRM

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, batch, billetno, bundle, heatno, out, status, workorder.

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
| InTIme | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| OutTIme | datetime | YES | — | — |
| Status | varchar | YES | 50 | ('Entered') |
| BundleNo | varchar | YES | 100 | — |
| Heatno | varchar | YES | 100 | — |
| Billetno | varchar | YES | 100 | — |
| Workorder | varchar | YES | 36 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_WRM.Workorder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
