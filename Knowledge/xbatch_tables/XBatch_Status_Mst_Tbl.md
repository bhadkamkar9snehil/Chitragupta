# XStudio_Xbatch.dbo.XBatch_Status_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, description.

**Primary Key:** ID  
**Row Count:** 12  
**Date Range (ModifiedOn):** 2023-07-22T11:17:13.0000000 to 2025-12-27T11:42:37.0000000  

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
| Description | varchar | YES | -1 | — |
| Color | varchar | YES | 50 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B6D4630D-6EA0-4167-99C6-625E09EE8C94 | Error | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | NULL | 2023-07-25T18:32:04.0030000 | NULL | False | False | NULL |
| 3D99E91F-DBE3-4EB3-BA6A-E8D1DC83F57D | Scheduled | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2023-06-19T10:42:07.7430000 | 2023-07-22T11:17:13.0000000 | False | False | NULL |
| 3EED66D1-97AB-4D17-8080-5EA17727AE22 | Approved | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2023-06-19T10:42:21.1730000 | 2023-07-22T11:17:20.0000000 | False | False | NULL |
| 9458B8BD-711C-4D5F-A704-B8A830A71C3D | New | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-15T14:42:48.8230000 | 2025-12-15T14:58:17.0000000 | False | False | NULL |
| FB9ADFFF-B908-435C-A1CB-6BB13DDF122A | Running | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-06-19T10:42:14.3800000 | 2025-12-15T14:59:15.0000000 | False | False | NULL |
| 8C943206-6C64-4756-8EA5-3A6814A3E36C | OnHold | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-06-19T10:42:28.1500000 | 2025-12-15T15:01:34.0000000 | False | False | NULL |
| DEDED230-4E84-4A5B-B369-FFBD78A4F99E | Completed | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-06-19T10:42:40.1770000 | 2025-12-15T15:07:03.0000000 | False | False | NULL |
| 061F5B25-D877-4A5B-86C6-261CA5524169 | Aborted | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-06-19T10:42:34.2730000 | 2025-12-20T12:03:34.0000000 | False | False | NULL |
| 1B57B533-DA25-4D14-9CF0-604F7AF1721C | Cancelled | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-15T14:46:55.7230000 | 2025-12-20T12:03:55.0000000 | False | False | NULL |
| 852A2277-1FFB-4DC2-A68F-3E2128C2E8DC | Released | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-07-25T11:42:38.5830000 | 2025-12-20T12:05:42.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1E8BDDE-B23C-4BA1-A38C-B4FBDBA9469C | New Process Order | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-27T11:39:48.3030000 | 2025-12-27T11:42:37.0000000 | False | False | NULL |
| FC7D73F4-4D97-406C-AE1C-9FE1C63DFB7E | New Production Order | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-27T11:41:07.3170000 | 2025-12-27T11:41:48.0000000 | False | False | NULL |
| 852A2277-1FFB-4DC2-A68F-3E2128C2E8DC | Released | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-07-25T11:42:38.5830000 | 2025-12-20T12:05:42.0000000 | False | False | NULL |
| 1B57B533-DA25-4D14-9CF0-604F7AF1721C | Cancelled | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-15T14:46:55.7230000 | 2025-12-20T12:03:55.0000000 | False | False | NULL |
| 061F5B25-D877-4A5B-86C6-261CA5524169 | Aborted | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-06-19T10:42:34.2730000 | 2025-12-20T12:03:34.0000000 | False | False | NULL |
| DEDED230-4E84-4A5B-B369-FFBD78A4F99E | Completed | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-06-19T10:42:40.1770000 | 2025-12-15T15:07:03.0000000 | False | False | NULL |
| 8C943206-6C64-4756-8EA5-3A6814A3E36C | OnHold | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-06-19T10:42:28.1500000 | 2025-12-15T15:01:34.0000000 | False | False | NULL |
| FB9ADFFF-B908-435C-A1CB-6BB13DDF122A | Running | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2023-06-19T10:42:14.3800000 | 2025-12-15T14:59:15.0000000 | False | False | NULL |
| 9458B8BD-711C-4D5F-A704-B8A830A71C3D | New | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-15T14:42:48.8230000 | 2025-12-15T14:58:17.0000000 | False | False | NULL |
| 3EED66D1-97AB-4D17-8080-5EA17727AE22 | Approved | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2023-06-19T10:42:21.1730000 | 2023-07-22T11:17:20.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XBatch_Batch_Mst_Tbl.StatusID` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Operation_Mst_Tbl.StatusID` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Group_Mst_Tbl.StatusID` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Mst_Tbl.StatusID` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Phase_Trn_Tbl.StatusID` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Batch_Unit_Procedure_Mst_Tbl.StatusID` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.Status` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.Status` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.Name` (Many to One)
