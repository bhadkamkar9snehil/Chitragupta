# XStudio_Xbatch.dbo.XBatch_Recipe_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference process, cell, material, position, status, time, version.

**Primary Key:** ID  
**Row Count:** 7  
**Date Range (ModifiedOn):** 2025-07-03T18:14:07.0000000 to 2025-07-09T15:47:19.0000000  

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
| MaterialID | varchar | NO | 36 | — |
| ProcessCellID | varchar | YES | -1 | — |
| Version | varchar | NO | 100 | — |
| Status | varchar | YES | 100 | — |
| Position | varchar | YES | 100 | — |
| ProcessTime | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9D7D88D3-FDC6-4A16-9476-40478DE8B163 | WR_P00026 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-01T18:31:28.9000000 | 2025-07-03T18:14:07.0000000 | False | False | NULL |
| EDD2D764-F8F3-4FDB-9EA4-576CFD2689BB | WR_P00025 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-03T14:08:15.3130000 | 2025-07-03T18:14:18.0000000 | False | False | NULL |
| 398219E3-7869-4C79-8BBC-848F51B729F1 | WR_P00024 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-01T12:46:09.7700000 | 2025-07-03T18:14:24.0000000 | False | False | NULL |
| 243B6D65-5BF0-4610-9798-D8240615DEDA | WR_P00027 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-03T18:14:41.4430000 | 2025-07-03T18:14:40.0000000 | False | False | NULL |
| 26EF76C8-71F8-424D-AB96-9CB90E51C6BB | WR_P00028 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-03T18:14:48.0500000 | 2025-07-03T18:14:47.0000000 | False | False | NULL |
| A121D7CE-4D51-4130-A904-7D0FDBA64521 | WR_P00023 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-05T11:59:14.8770000 | 2025-07-05T11:59:14.0000000 | False | False | NULL |
| DC2E2DF3-BE67-4D50-A76C-6F5C829F5558 | RC_B500B_8.0DIA | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-09T15:47:19.9870000 | 2025-07-09T15:47:19.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Recipe_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Connection_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Recipe_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Mst_Tbl.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Mst_Tbl.ProcessCellID` -> `XStudio_XBatch.XBatch_Process_Cell_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Recipe_Unit_Procedure_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Recipe_Mst_Tbl.ID` (Many to One)
