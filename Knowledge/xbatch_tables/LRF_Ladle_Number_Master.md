# XStudio_Xbatch.dbo.LRF_Ladle_Number_Master

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ladle, number.

**Primary Key:** ID  
**Row Count:** 8  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| LadleNumber | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |
| EntryDateTime | datetime | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FA7904DF-7FC6-473B-8568-AAEE31167553 | NULL | NULL | 2025-07-25T08:46:43.7730000 | NULL | False | False | NULL | NULL |  |
| ECA9A806-204F-4CAB-AAAB-11096D8FFD45 | NULL | NULL | 2025-07-25T08:46:43.7730000 | NULL | False | False | NULL | NULL |  |
| E176B905-9085-4E69-A28D-553F0FA15A4C | NULL | NULL | 2025-07-25T08:46:43.7730000 | NULL | False | False | NULL | NULL |  |
| DD1D11CC-770D-4295-B355-6FFBCF690F72 | NULL | NULL | 2025-07-25T08:46:43.7730000 | NULL | False | False | NULL | NULL |  |
| BCB829F0-B94A-455B-99B3-C00F8E0740B5 | NULL | NULL | 2025-07-25T08:46:43.7730000 | NULL | False | False | NULL | NULL |  |
| 6EC6E31E-7043-4214-8507-0916DA731317 | NULL | NULL | 2025-07-25T08:46:43.7730000 | NULL | False | False | NULL | NULL |  |
| 3F0F5847-EF41-4020-A3B1-1D4EDD6D7FF1 | NULL | NULL | 2025-07-25T08:46:43.7730000 | NULL | False | False | NULL | NULL |  |
| 1F2BFBE8-248A-44FB-8997-E0F8763B6FBB | NULL | NULL | 2025-07-25T08:46:43.7730000 | NULL | False | False | NULL | NULL |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_LogSheet_Ladle_Details.LaddleNumber` -> `XStudio_XBatch.LRF_Ladle_Number_Master.LadleNumber` (Many to One)
- `XStudio_XBatch.Laddle_Life_for_Each_Heat.LaddleNumber` -> `XStudio_XBatch.LRF_Ladle_Number_Master.ID` (Many to One)
- `XStudio_XBatch.LRF_Ladle_No_Per_Heat.ActiveLadle` -> `XStudio_XBatch.LRF_Ladle_Number_Master.ID` (Many to One)
