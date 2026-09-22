# XStudio_Xbatch.dbo.Laddle_Life_for_Each_Heat

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference laddle, life, number.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2025-07-25T08:50:54.4770000 to 2025-07-25T08:56:47.0000000  

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
| EntryDateTime | datetime | YES | — | — |
| LaddleLife | int | YES | 10,0 | — |
| ReportDate | date | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| LaddleNumber | varchar | YES | 36 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C052C54B-8225-422E-8DD1-120106220D45 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:50:54.4770000 | True | False | NULL | 172.16.100.58 |  |
| F229CE89-850A-4A9D-ACB0-4B0505513AF8 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:51:04.1530000 | True | False | NULL | 172.16.100.58 |  |
| 12E74B11-82B2-4BE2-86B5-0E30607DF6B5 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:52:11.0000000 | False | False | NULL | 172.16.100.58 |  |
| 3798E289-B664-45DC-9641-F31A6F8D49CB | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:55:54.0000000 | False | False | NULL | 172.16.6.48 |  |
| 380451A0-0E12-4828-9277-8BEB7958FC9E | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:56:03.0000000 | False | False | NULL | 172.16.6.48 |  |
| 4A7066A8-82E8-4CBD-9CF8-73757E6D3BC9 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:56:11.0000000 | False | False | NULL | 172.16.6.48 |  |
| 4E09C32A-2EDD-4C34-B4AA-20B04494DEC2 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:56:19.0000000 | False | False | NULL | 172.16.6.48 |  |
| 59E74ABA-AF77-4BFD-AF5E-7762BDB0EBB2 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:56:29.0000000 | False | False | NULL | 172.16.6.48 |  |
| 78EDB832-A3A0-4737-B848-33C033D6EF22 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:56:39.0000000 | False | False | NULL | 172.16.6.48 |  |
| EA7644A2-8A6B-4003-BA11-E993517ECD18 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-24T14:15:18.4430000 | 2025-07-25T08:56:47.0000000 | False | False | NULL | 172.16.6.48 |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Laddle_Life_for_Each_Heat.LaddleNumber` -> `XStudio_XBatch.LRF_Ladle_Number_Master.ID` (Many to One)
