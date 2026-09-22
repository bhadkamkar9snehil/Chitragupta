# XStudio_Xbatch.dbo.EAF_LogSheet_Quantity

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, furnace, heat, production, tracking (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference per, grade, heat, jni, name, sample, shift, temperature, test.

**Primary Key:** ID  
**Row Count:** 2,132  
**Date Range (ModifiedOn):** 2025-08-19T08:31:02.8600000 to 2025-09-08T09:07:08.0000000  

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
| Sample | decimal | YES | 18,4 | — |
| PerC | decimal | YES | 18,4 | — |
| PerMn | decimal | YES | 18,4 | — |
| PerSi | decimal | YES | 18,4 | — |
| PerS | decimal | YES | 18,4 | — |
| PerP | decimal | YES | 18,4 | — |
| PerCr | decimal | YES | 18,4 | — |
| PerJNi | decimal | YES | 18,4 | — |
| PerMo | decimal | YES | 18,4 | — |
| PerCu | decimal | YES | 18,4 | — |
| PerSn | decimal | YES | 18,4 | — |
| PerAI | decimal | YES | 18,4 | — |
| PerN2 | decimal | YES | 18,4 | — |
| Temperature | decimal | YES | 18,4 | — |
| HeatNo | decimal | YES | 18,4 | — |
| Grade | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |
| TestName | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00E4DC73-2AA0-48CC-9482-68AE073D792C | NULL | NULL | NULL | NULL | 2025-08-21T18:20:20.4270000 | NULL | True | False | NULL |
| 00DDA09B-7F27-4CD0-B22B-3F90F4A62D0A | NULL | NULL | NULL | NULL | 2025-11-01T21:49:01.0200000 | NULL | False | False | NULL |
| 00D5BC12-C79D-4A6B-A90A-5911CF91AE21 | NULL | NULL | NULL | NULL | 2025-11-06T08:42:43.3530000 | NULL | False | False | NULL |
| 00D56FA2-B3B8-4774-9F22-BE98D66171C8 | NULL | NULL | NULL | NULL | 2025-11-05T09:14:28.9830000 | NULL | False | False | NULL |
| 009BBB01-3755-42C5-8BFE-7B231E991726 | NULL | NULL | NULL | NULL | 2025-11-20T04:26:46.9300000 | NULL | False | False | NULL |
| 007CE9C7-0DA8-4377-954A-7282D7FE3CF3 | NULL | NULL | NULL | NULL | 2025-08-30T04:02:45.0900000 | NULL | False | False | NULL |
| 005F8307-1CDF-470D-934F-1B084128F1F2 | NULL | NULL | NULL | NULL | 2025-08-22T11:37:40.8100000 | NULL | False | False | NULL |
| 00556826-10FE-4369-96E9-9AC482D5E604 | NULL | NULL | NULL | NULL | 2025-11-12T13:47:29.4200000 | NULL | False | False | NULL |
| 00413B3A-FDFE-4DEF-8AB3-1329BB715EB4 | NULL | NULL | NULL | NULL | 2025-09-25T07:37:23.0100000 | NULL | False | False | NULL |
| 003659A7-F4F3-4EC2-8040-E3C57514495D | NULL | NULL | NULL | NULL | 2025-09-02T16:01:50.3400000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7C1BDD1E-5AC0-4AB5-B366-F370A784B4C8 | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-09-08T09:07:08.3100000 | 2025-09-08T09:07:08.0000000 | False | False | NULL |
| D20D0CB1-3A72-4273-BB55-B66CCFB93B38 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-21T19:44:43.3700000 | 2025-08-22T10:31:48.5630000 | True | False | NULL |
| 637C733B-294D-42C2-8A57-DBA31639B91D | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-21T20:51:58.2200000 | 2025-08-22T10:31:40.8200000 | True | False | NULL |
| A1E425CE-72E0-4299-B839-2892C123516C | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-21T20:52:14.3300000 | 2025-08-22T10:31:31.5930000 | True | False | NULL |
| C32B8768-E81E-440D-ADF9-122812D3880F | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-21T20:52:03.1800000 | 2025-08-22T10:31:19.6430000 | True | False | NULL |
| D983478A-E01D-4555-AC81-505079339AC6 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-21T20:52:08.2630000 | 2025-08-22T10:31:13.4500000 | True | False | NULL |
| 2370B6F9-4342-484D-9286-98D0D1DEA1F2 | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-21T20:52:25.4800000 | 2025-08-22T10:31:06.6300000 | True | False | NULL |
| AC1CCF7A-A0B7-4CB0-9598-3D5A5477EA4C | NULL | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-21T21:49:59.2000000 | 2025-08-22T10:30:57.2130000 | True | False | NULL |
| 591CA56C-266E-401A-AF58-F59D4D65CCB9 | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-21T13:51:37.4700000 | 2025-08-19T08:31:14.3800000 | True | False | NULL |
| C804221F-4873-4E82-8D49-860ADD5B1E07 | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-07-21T13:50:23.0970000 | 2025-08-19T08:31:10.8800000 | True | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_LogSheet_Quantity.Grade` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.EAF_LogSheet_Quantity.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.HeatID` (Many to One)
- `XStudio_XBatch.EAF_LogSheet_Quantity.TestName` -> `XStudio_XBatch.Grade_Test_Master.ID` (Many to One)
