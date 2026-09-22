# XStudio_Xbatch.dbo.Quality_Spectro_File

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** chemistry, core, quality, routing, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference file, status, checksum, importedon, name, note, path.

**Primary Key:** ID  
**Row Count:** 23,023  
**Date Range (ModifiedOn):** 2025-12-17T15:41:00.8500000 to 2026-08-11T14:39:05.7630000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| FileName | varchar | YES | 1000 | — |
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
| Importedon | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| FilePath | varchar | YES | 4000 | — |
| Checksum | varchar | YES | 100 | — |
| FileStatus | varchar | YES | 30 | — |
| STatusNote | varchar | YES | 500 | — |

### Top 10 Records

| ID | FileName | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C8132F3E-9436-4E0F-BBEB-FD0513DD2394 | Result - 1506384 M1 SK - Fe-10_3SP.P - 01.11.2025 00_02_42.xml | NULL | NULL | 2025-12-17T15:41:00.5270000 | 2025-12-17T15:41:00.8500000 | False | False | NULL | NULL |
| CA80177C-9773-4604-BAAB-699CEBD7DF10 | Result - 1506384 L1 SK - Fe-10_3SP.P - 01.11.2025 00_05_22.xml | NULL | NULL | 2025-12-17T15:41:01.0400000 | 2025-12-17T15:41:01.1130000 | False | False | NULL | NULL |
| 3646DAEA-A8D0-4D03-A00B-C8372FFF6311 | Result - 1506383 TS SK - Fe-10_3SP.P - 01.11.2025 00_13_36.xml | NULL | NULL | 2025-12-17T15:41:01.2730000 | 2025-12-17T15:41:01.3330000 | False | False | NULL | NULL |
| D2AA60B2-832E-440F-A857-053FC6648AF0 | Result - 1506384 L2 SK - Fe-10_3SP.P - 01.11.2025 00_35_39.xml | NULL | NULL | 2025-12-17T15:41:01.4900000 | 2025-12-17T15:41:01.5470000 | False | False | NULL | NULL |
| 33D0B495-9606-4934-B8A6-CD0996C871B8 | Result - Fe-10_3SP.P - 01.11.2025 00_50_38.xml | NULL | NULL | 2025-12-17T15:41:01.7130000 | 2025-12-17T15:41:01.7670000 | False | False | NULL | NULL |
| 2C94BCF7-9C14-4E36-8457-A6246B383280 | Result - 1506385 M1 SK - Fe-10_3SP.P - 01.11.2025 00_55_49.xml | NULL | NULL | 2025-12-17T15:41:01.9330000 | 2025-12-17T15:41:01.9700000 | False | False | NULL | NULL |
| 446C204A-9EA5-4C66-87D8-E34464691634 | Result - 1506384 TS SK - Fe-10_3SP.P - 01.11.2025 00_58_32.xml | NULL | NULL | 2025-12-17T15:41:02.1370000 | 2025-12-17T15:41:02.2000000 | False | False | NULL | NULL |
| 913ED688-B5D6-486F-96DE-0225A2CAC05D | Result - 1506385 L2 SK - Fe-10_3SP.P - 01.11.2025 01_38_11.xml | NULL | NULL | 2025-12-17T15:41:02.3530000 | 2025-12-17T15:41:02.4400000 | False | False | NULL | NULL |
| 921C6BEF-A6C8-4158-A170-40F38C8EAE75 | Result - 1506385 TS SK - Fe-10_3SP.P - 01.11.2025 01_50_29.xml | NULL | NULL | 2025-12-17T15:41:02.6030000 | 2025-12-17T15:41:02.6570000 | False | False | NULL | NULL |
| 1EE57E5F-1F78-4CDD-B900-D1090602340B | Result - Fe-10_3SP.P - 01.11.2025 02_12_10.xml | NULL | NULL | 2025-12-17T15:41:02.8230000 | 2025-12-17T15:41:02.8570000 | False | False | NULL | NULL |

### Bottom 10 Records

| ID | FileName | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6D9FDA58-8AD3-4D57-BA9D-16C57F444FE6 | Result - Sec Std   - Fe-10_3SP.25.06 - 11.08.2026 14_37_34.xml | NULL | NULL | 2026-08-11T14:39:04.7900000 | 2026-08-11T14:39:05.7630000 | False | False | NULL | NULL |
| A2C2D7CF-E684-4EC1-9E71-A0BC9054E287 | Result - DUMMY   - Fe-10_3SP.25.06 - 11.08.2026 14_30_09.xml | NULL | NULL | 2026-08-11T14:31:04.8800000 | 2026-08-11T14:31:05.6370000 | False | False | NULL | NULL |
| 016215A2-7071-482D-8449-65EE83A8B00B | Result - Fe-10_3SP.25.06 - 05.08.2026 11_15_07.xml | NULL | NULL | 2026-08-05T11:16:04.2970000 | 2026-08-05T11:16:05.0870000 | False | False | NULL | NULL |
| 473EB3FE-CCDE-40E8-9A8C-06C493968F1C | Result - Fe-10 - 05.08.2026 10_54_35.xml | NULL | NULL | 2026-08-05T10:56:04.2830000 | 2026-08-05T10:56:04.9900000 | False | False | NULL | NULL |
| 771C20B3-96DA-4669-8A88-C8B2ED1A86BC | Result - BOLT MEC  - Fe-01 - 05.08.2026 10_52_38.xml | NULL | NULL | 2026-08-05T10:54:04.3870000 | 2026-08-05T10:54:05.1100000 | False | False | NULL | NULL |
| 1F4A1BCD-A3E3-4578-B8AB-BBB77FDE502F | Result - 154  SANTOSH - Fe-10_3SP.25.06 - 01.08.2026 21_59_29.xml | NULL | NULL | 2026-08-01T22:01:05.2330000 | 2026-08-01T22:01:05.6900000 | False | False | NULL | NULL |
| 59355A7E-9062-427C-A863-F69985DDFF42 | Result - 153  SANTOSH - Fe-10_3SP.25.06 - 01.08.2026 21_57_33.xml | NULL | NULL | 2026-08-01T21:59:05.2530000 | 2026-08-01T21:59:05.7070000 | False | False | NULL | NULL |
| 01D37822-AADC-4BAF-ADC2-C072A9CB5B1C | Result - 152  SANTOSH - Fe-10_3SP.25.06 - 01.08.2026 21_54_29.xml | NULL | NULL | 2026-08-01T21:56:05.2100000 | 2026-08-01T21:56:05.6230000 | False | False | NULL | NULL |
| 4920AB5B-6AA0-4546-AA74-E3B0A278617F | Result - 151  SANTOSH - Fe-10_3SP.25.06 - 01.08.2026 21_52_09.xml | NULL | NULL | 2026-08-01T21:53:05.2030000 | 2026-08-01T21:53:05.6130000 | False | False | NULL | NULL |
| 2310C820-6A3B-45C0-AD4F-FEDBCBA2A242 | Result - 150  SANTOSH - Fe-10_3SP.25.06 - 01.08.2026 21_49_24.xml | NULL | NULL | 2026-08-01T21:50:05.2470000 | 2026-08-01T21:50:05.6400000 | False | False | NULL | NULL |

---
