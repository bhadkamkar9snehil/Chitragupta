# XStudio_Xbatch.dbo.Shift_Operator_Incharge_Selection_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference operator, shift, charge, dateyyyymmdd, yard.

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-11-18T12:34:45.1770000 to 2026-05-14T13:57:39.0000000  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Shift | varchar | YES | 100 | — |
| CP1Operator | varchar | YES | 36 | — |
| CP2Operator | varchar | YES | 36 | — |
| CP3Operator | varchar | YES | 36 | — |
| CP4Operator | varchar | YES | 36 | — |
| YardOperator | varchar | YES | 36 | — |
| ShiftInCharge | varchar | YES | 36 | — |
| Dateyyyymmdd | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 888174F8-5873-4423-A6C2-F1D86747A399 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-18T11:25:40.4670000 | 2025-11-18T12:34:45.1770000 | True | False | NULL |
| 16382FAE-9ED5-48E5-9C83-EAB27473093C | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-14T10:18:00.5600000 | 2026-05-14T10:18:00.0000000 | False | False | NULL |
| BBBF0C7A-E3B7-4EF6-8426-8361890CC3B0 | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-14T13:57:39.7130000 | 2026-05-14T13:57:39.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Shift_Operator_Incharge_Selection_Trn_Tbl.CP1Operator` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Shift_Operator_Incharge_Selection_Trn_Tbl.CP2Operator` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Shift_Operator_Incharge_Selection_Trn_Tbl.CP3Operator` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Shift_Operator_Incharge_Selection_Trn_Tbl.CP4Operator` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Shift_Operator_Incharge_Selection_Trn_Tbl.ShiftInCharge` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Shift_Operator_Incharge_Selection_Trn_Tbl.YardOperator` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
