# XStudio_Xbatch.dbo.RM_NGConsumption

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, cold, hot, time, discharge, ngcons, total, avg, crosssection, date, discharged, from.

**Primary Key:** ID  
**Row Count:** 8,182  
**Date Range (ModifiedOn):** 2025-09-24T16:30:15.5800000 to 2025-12-10T16:00:18.0000000  

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
| Date | date | YES | — | — |
| FromTime | datetime | YES | — | — |
| ToTime | datetime | YES | — | — |
| RollingSize | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |
| Billet130Hot | int | YES | 10,0 | — |
| Billet130Cold | int | YES | 10,0 | — |
| Billet140Cold | int | YES | 10,0 | — |
| Billet140Hot | int | YES | 10,0 | — |
| Billet150Hot | int | YES | 10,0 | — |
| Billet150Cold | int | YES | 10,0 | — |
| Discharged | int | YES | 10,0 | — |
| TotalBillet | decimal | YES | 18,3 | — |
| NGCong | decimal | YES | 18,4 | — |
| NGCons | int | YES | 10,0 | — |
| TotalNG | decimal | YES | 18,4 | — |
| CP1Operator | varchar | YES | 36 | — |
| Crosssection | int | YES | 10,0 | — |
| Shift | varchar | YES | 100 | — |
| HotDischargeBillet | int | YES | 10,0 | — |
| ColdDischargeBillet | int | YES | 10,0 | — |
| NGconsMMBTPerTon | decimal | YES | 18,4 | — |
| AvgResidenceTime | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00386E26-4C68-4753-8DE5-729079B6C7A7 | NULL | NULL | NULL | NULL | 2026-02-01T05:00:00.6870000 | NULL | False | False | NULL |
| 003519C6-9885-4517-B64E-F178FA78A1CA | NULL | NULL | NULL | NULL | 2025-09-21T10:53:31.8700000 | NULL | False | False | NULL |
| 0031C7F1-BF4E-499B-B97C-7C34AD29911F | NULL | NULL | NULL | NULL | 2026-01-05T21:00:03.3270000 | NULL | False | False | NULL |
| 0027B14B-7137-4B94-80D6-1DB1BE0005EA | NULL | NULL | NULL | NULL | 2026-08-06T13:07:11.3530000 | NULL | False | False | NULL |
| 001D89C6-4A88-45E2-85D5-2F50E6F77A88 | NULL | NULL | NULL | NULL | 2026-03-05T01:00:03.9800000 | NULL | False | False | NULL |
| 001C782C-8284-45AE-84C9-42132BF00DFA | NULL | NULL | NULL | NULL | 2026-07-18T10:50:43.2400000 | NULL | False | False | NULL |
| 00105EC2-24B5-4168-AB3D-7A64C1A4E2DC | NULL | NULL | NULL | NULL | 2026-01-04T13:00:02.4930000 | NULL | False | False | NULL |
| 000BA6F2-1AC9-4C6D-B47B-FEC9EE576A46 | NULL | NULL | NULL | NULL | 2026-07-18T10:45:57.5100000 | NULL | False | False | NULL |
| 00093720-D758-47B3-A31D-493074612094 | NULL | NULL | NULL | NULL | 2026-08-29T12:00:03.8070000 | NULL | False | False | NULL |
| 00085F8A-371A-4E2E-A10D-4FF182BDF4ED | NULL | NULL | NULL | NULL | 2026-03-29T20:00:01.7030000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C0986C85-CDEB-4A75-90A7-1884585484CE | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-05T23:00:03.5930000 | 2025-12-10T16:00:18.0000000 | False | False | NULL |
| 9085DC6C-6794-443E-BD1C-EB3384D02C0C | NULL | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-12-06T00:00:04.6470000 | 2025-12-10T16:00:07.0000000 | False | False | NULL |
| C8B2797C-B0D4-4449-A9EC-C9F356A44C58 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-02T23:00:02.9670000 | 2025-12-09T09:42:50.0000000 | False | False | NULL |
| 7FB3CA37-8FBE-4951-860C-78364F1B968E | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-03T00:00:03.5670000 | 2025-12-09T09:42:36.0000000 | False | False | NULL |
| 76035230-A483-4BD0-90EB-4713BD07EB7A | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-24T16:27:35.1000000 | 2025-09-24T16:30:21.6500000 | True | False | NULL |
| 553CD5BB-1DAC-4BF3-9485-57478F672F67 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-24T16:29:09.2470000 | 2025-09-24T16:30:15.5800000 | True | False | NULL |
| 00386E26-4C68-4753-8DE5-729079B6C7A7 | NULL | NULL | NULL | NULL | 2026-02-01T05:00:00.6870000 | NULL | False | False | NULL |
| 003519C6-9885-4517-B64E-F178FA78A1CA | NULL | NULL | NULL | NULL | 2025-09-21T10:53:31.8700000 | NULL | False | False | NULL |
| 0031C7F1-BF4E-499B-B97C-7C34AD29911F | NULL | NULL | NULL | NULL | 2026-01-05T21:00:03.3270000 | NULL | False | False | NULL |
| 0027B14B-7137-4B94-80D6-1DB1BE0005EA | NULL | NULL | NULL | NULL | 2026-08-06T13:07:11.3530000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_NGConsumption.CP1Operator` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
