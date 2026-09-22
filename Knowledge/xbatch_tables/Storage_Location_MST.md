# XStudio_Xbatch.dbo.Storage_Location_MST

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference description, location, plant, storage.

**Primary Key:** ID  
**Row Count:** 605  
**Date Range (ModifiedOn):** 2025-12-05T14:47:10.0000000 to 2025-12-05T16:30:26.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Plant | varchar | YES | 36 | — |
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
| StorageLocation | varchar | YES | 100 | — |
| Description | varchar | YES | 100 | — |

### Top 10 Records

| ID | Plant | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 018F02CD-8A42-4435-808B-B2EC766AA223 | DB9A764B-5CFD-4BDB-AEBB-8B1830CCDE2B | NULL | NULL | NULL | 2025-12-05T16:42:35.5000000 | NULL | False | False | NULL |
| 0130081E-B6CE-44C6-9E4A-8AA5CF5D5DAD | F1CD4104-9B99-4946-A75F-5C87E3730AEA | NULL | NULL | NULL | 2025-12-05T16:42:35.7400000 | NULL | False | False | NULL |
| 0074C492-A5D8-45AE-93D7-B754312A03ED | 898B0737-6A9C-4581-9A4D-C02040CA4E63 | NULL | NULL | NULL | 2025-12-05T16:42:35.6570000 | NULL | False | False | NULL |
| 02F3EA7E-989F-46F6-B511-6B21E6D8CBAD | 89C4BDED-BB44-4E00-BAFD-8D9722C113B5 | NULL | NULL | NULL | 2025-12-05T16:42:35.7300000 | NULL | False | False | NULL |
| 01F316BD-0713-4F93-87A0-CAAEFC190BB5 | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | NULL | NULL | 2025-12-05T16:42:35.4800000 | NULL | False | False | NULL |
| 01C398B0-FDE0-454F-8864-65B377B90BE7 | C0F75EC5-60F0-4392-823D-12DB631412AC | NULL | NULL | NULL | 2025-12-05T16:42:35.4930000 | NULL | False | False | NULL |
| 01BBCF17-3756-4514-AA9C-473509490D9F | DB9A764B-5CFD-4BDB-AEBB-8B1830CCDE2B | NULL | NULL | NULL | 2025-12-05T16:42:35.5130000 | NULL | False | False | NULL |
| 03C97973-1028-4FBF-8B37-6ACD09950D77 | B9CF1618-4DB1-4A8F-8418-C21FAB3EF508 | NULL | NULL | NULL | 2025-12-05T16:42:35.5230000 | NULL | False | False | NULL |
| 056B6FB0-618D-4FE0-B608-81770A96A4CA | 89C4BDED-BB44-4E00-BAFD-8D9722C113B5 | NULL | NULL | NULL | 2025-12-05T16:42:35.7300000 | NULL | False | False | NULL |
| 056F07CF-02FF-42E7-AB53-AE60D1923F94 | A30B2092-9EFE-4DCD-9DBB-9B8800AB8D11 | NULL | NULL | NULL | 2025-12-05T16:42:35.7130000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Plant | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21293A45-50EC-4130-BBF7-B77946B207A2 | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:30:26.1900000 | 2025-12-05T16:30:26.0000000 | False | False | NULL |
| 23EC3078-48FD-49E7-98E6-25E1FD9B73BB | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:30:09.5130000 | 2025-12-05T16:30:09.0000000 | False | False | NULL |
| 4071BD09-6BB1-459A-86C4-9DC4EF88A4EA | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:29:50.2600000 | 2025-12-05T16:29:50.0000000 | False | False | NULL |
| CE4B9FFE-EA0B-401C-A46B-AB36CB85314C | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:29:21.8500000 | 2025-12-05T16:29:21.0000000 | False | False | NULL |
| 106F06C8-F9DE-4B23-893C-D77C1C85BEB1 | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:28:56.2600000 | 2025-12-05T16:28:56.0000000 | False | False | NULL |
| 7EA3E4D1-81FC-4012-893E-01F0B3E99849 | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:28:38.1370000 | 2025-12-05T16:28:38.0000000 | False | False | NULL |
| 51D2AC0D-7998-4BBC-95BA-DCF238E607EB | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:28:21.4470000 | 2025-12-05T16:28:21.0000000 | False | False | NULL |
| 86C8E828-BEB5-407A-86B6-A3A4BA9823C8 | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:28:04.8300000 | 2025-12-05T16:28:04.0000000 | False | False | NULL |
| 7C70B25C-943B-4776-AA37-516B67B634AB | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:27:49.5600000 | 2025-12-05T16:27:49.0000000 | False | False | NULL |
| 53A26C3B-7ADB-4F99-938A-41FE7E05B198 | 5F05CDE5-8BCF-4D7A-955B-12C79CBF0A4D | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-05T16:27:32.8500000 | 2025-12-05T16:27:32.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Storage_Location_MST.Plant` -> `XStudio_XBatch.Plant_Name_MST.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.StorageLocation` -> `XStudio_XBatch.Storage_Location_MST.StorageLocation` (Many to One)
- `XStudio_XBatch.Xbatch_Material_Inventory_Trn_Tbl.StorageLocation` -> `XStudio_XBatch.Storage_Location_MST.StorageLocation` (Many to One)
- `XStudio_XBatch.XBatch_Material_Mst_Tbl.StoragelocationID` -> `XStudio_XBatch.Storage_Location_MST.ID` (Many to One)
- `XStudio_XBatch.XBatch_Store_Mst_Tbl.SAPStorageLocation` -> `XStudio_XBatch.Storage_Location_MST.ID` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.StorageLocation` -> `XStudio_XBatch.Storage_Location_MST.StorageLocation` (Many to One)
