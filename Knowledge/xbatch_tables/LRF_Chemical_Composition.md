# XStudio_Xbatch.dbo.LRF_Chemical_Composition

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference per, grade, heat, name, sample, shift, temperature, test.

**Primary Key:** ID  
**Row Count:** 9  
**Date Range (ModifiedOn):** 2025-07-22T15:16:40.0000000 to 2025-11-27T08:15:11.0000000  

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
| PerSn | decimal | YES | 18,4 | — |
| PerMo | decimal | YES | 18,4 | — |
| PerS | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| PerCr | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| PerN2 | decimal | YES | 18,4 | — |
| PerNi | decimal | YES | 18,4 | — |
| PerSi | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| IsProcessed | bit | YES | — | — |
| PerP | decimal | YES | 18,4 | — |
| PerAI | decimal | YES | 18,4 | — |
| PerCu | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| PerMn | decimal | YES | 18,4 | — |
| PerC | decimal | YES | 18,4 | — |
| HeatNo | varchar | YES | 100 | — |
| Grade | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |
| Sample | varchar | YES | 100 | — |
| Temperature | decimal | YES | 18,4 | — |
| TestName | varchar | YES | 36 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F6298B05-1447-41CA-A571-D2A76182535A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T15:47:31.1230000 | 2025-07-22T15:16:40.0000000 | False | False | NULL | 172.16.6.76 |  |
| D3FFC148-D249-456F-A5FE-9578A9FBE863 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-23T08:56:18.8800000 | 2025-07-23T08:56:34.0000000 | False | False | NULL | 172.16.6.76 |  |
| 8E42F6D4-91B3-49F3-969C-986F2955B093 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-23T08:59:47.5630000 | 2025-07-23T09:00:09.0000000 | False | False | NULL | 172.16.6.76 |  |
| A3450D59-9B63-48E6-9FEF-32E4E08FAA04 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-23T09:01:08.5770000 | 2025-07-23T09:01:08.0000000 | False | False | NULL | 172.16.6.76 |  |
| 756E5C16-E3DC-4352-AAAD-519FC796B2D5 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-23T09:02:21.5500000 | 2025-07-23T09:02:21.0000000 | False | False | NULL | 172.16.6.76 |  |
| AD5DE200-D02E-4072-8F67-E917E7138BE5 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-23T09:03:34.4430000 | 2025-08-02T10:28:19.0000000 | False | False | NULL |  |  |
| 8336956E-471B-435B-A9B2-02B14BBFE2F9 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-25T10:11:21.6770000 | 2025-11-25T10:11:21.0000000 | False | False | NULL |  |  |
| 36D80B4D-CD9D-41FC-9965-3CDC46BE249B | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-25T10:26:38.7300000 | 2025-11-25T10:26:38.0000000 | False | False | NULL |  |  |
| B20A9BEF-A116-4E13-B65F-2CABE0A3FAB9 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-27T08:15:11.1300000 | 2025-11-27T08:15:11.0000000 | False | False | NULL |  |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.LRF_Chemical_Composition.Grade` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.LRF_Chemical_Composition.TestName` -> `XStudio_XBatch.Grade_Test_Master.ID` (Many to One)
