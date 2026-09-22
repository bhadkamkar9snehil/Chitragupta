# XStudio_Xbatch.dbo.XBatch_Batch_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, actual, approved, batch, end, quantity, scheduled, start, cell, mode, number, order.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-07-02T12:52:55.0000000 to 2025-07-02T12:52:55.0000000  

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
| BatchNumber | varchar | NO | 100 | — |
| BatchMode | varchar | YES | 100 | — |
| ProcessCellID | varchar | YES | -1 | — |
| Quantity | decimal | NO | 18,4 | — |
| QuantityUnitID | varchar | NO | 36 | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| StatusID | varchar | YES | 36 | — |
| Version | varchar | YES | 100 | — |
| Position | varchar | YES | 100 | — |
| ApprovedBy | varchar | YES | 36 | — |
| ApprovedOn | datetime | YES | — | — |
| ScheduledBy | varchar | YES | 36 | — |
| ScheduledOn | datetime | YES | — | — |
| ActualStartTime | datetime | YES | — | — |
| ActualEndTime | datetime | YES | — | — |
| WorkOrderID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EE0C3964-623F-428E-AF0A-64E87BE13C49 | P11091 | 9D7D88D3-FDC6-4A16-9476-40478DE8B163 | E4B2A0FA-FF23-44C9-97E3-BE9AD20BD6A0 | E4B2A0FA-FF23-44C9-97E3-BE9AD20BD6A0 | 2025-07-02T12:52:57.5200000 | 2025-07-02T12:52:55.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Batch_BOM_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Recipe_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ProcessCellID` -> `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.QuantityUnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.StatusID` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.WorkOrderID` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Unit_Procedure_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.CurrentBatchID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Equipment_Mst_Tbl.CurrentBatchID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Unit_Mst_Tbl.CurrentBatchID` -> `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ID` (Many to One)
