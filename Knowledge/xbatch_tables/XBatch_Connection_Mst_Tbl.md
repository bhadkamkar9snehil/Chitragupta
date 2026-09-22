# XStudio_Xbatch.dbo.XBatch_Connection_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference equipment, name, destination, source, channel, collector, status.

**Primary Key:** ID  
**Row Count:** 0  

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
| CollectorName | varchar | YES | 100 | — |
| ChannelName | varchar | YES | 100 | — |
| SourceEquipmentID | varchar | NO | 36 | — |
| DestinationEquipmentID | varchar | NO | 36 | — |
| SourceEquipmentName | varchar | YES | 100 | — |
| DestinationEquipmentName | varchar | YES | 100 | — |
| Status | varchar | YES | 15 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Connection_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.ID` (Many to One)
