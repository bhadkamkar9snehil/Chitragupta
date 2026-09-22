# XStudio_Xbatch.dbo.Quality_Spectro_Sample

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference sample, name, instrument, method, file, heat, number, operator, point, received, time, type.

**Primary Key:** ID  
**Row Count:** 23,023  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| SampleName | varchar | YES | 100 | — |
| FileID | varchar | YES | 36 | — |
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
| XMLCreatedAt | datetime | YES | — | — |
| HeatNo | varchar | YES | 100 | — |
| SamplePoint | varchar | YES | 100 | — |
| OperatorName | varchar | YES | 100 | — |
| MethodName | varchar | YES | 100 | — |
| MethodVersion | varchar | YES | 100 | — |
| Instrument | varchar | YES | 100 | — |
| InstrumentNumber | varchar | YES | 100 | — |
| SampleType | varchar | YES | 100 | — |
| SampleReceivedTime | datetime | YES | — | — |

### Top 10 Records

| ID | SampleName | FileID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001DD28A-0B1C-445B-8FE3-17AFC004D19A | 1600057 F1 DK | A787B45A-F395-4DC8-BF26-57B686F0D20A | NULL | NULL | 2026-01-03T05:59:04.3970000 | NULL | False | False | NULL |
| 001A6FAB-30D9-4E1E-814B-48DD288616B0 | 1600069 L1 DK | E6705268-E527-4709-86A6-DC1C17EC2EA2 | NULL | NULL | 2026-01-03T17:59:04.3600000 | NULL | False | False | NULL |
| 00155C3E-4DA7-4723-B119-CC01D7B103A8 | BS 1020 PRI DK | 9F21A50C-CA21-4B66-95E6-3541438A4EFA | NULL | NULL | 2026-04-18T17:29:05.9100000 | NULL | False | False | NULL |
| 0011B791-0DA8-402E-B4EB-586101F381AB | 1507446 L2 DK | 211481A0-5B0E-437A-94E1-F7605EAFA59C | NULL | NULL | 2025-12-17T15:49:05.4300000 | NULL | False | False | NULL |
| 000EFC3E-0034-4CCF-AACF-18CBF2A37E83 | 1603372 L1 SANTOSH | B15B744F-DA17-4278-A260-F6A49ECFB45D | NULL | NULL | 2026-06-05T21:11:05.0700000 | NULL | False | False | NULL |
| 00065089-8381-46B8-B2FD-34856E2974BA | 1507789 F1 DK | 67CC9FC2-A0D1-4BE3-8150-0B934850AC0B | NULL | NULL | 2025-12-27T00:34:05.1030000 | NULL | False | False | NULL |
| 000627CC-D9EB-40E1-B4E9-56F81982BE86 | 1603326 TD VP Y | AA42C85D-51AB-4450-9F9F-83460A551B27 | NULL | NULL | 2026-06-03T06:42:04.6230000 | NULL | False | False | NULL |
| 00056610-864B-493C-BAE7-DE07B4B62162 | 1601259 L1 DK | 22C8931C-5F2B-4247-8D30-32650DB1DE2A | NULL | NULL | 2026-02-22T03:59:05.1730000 | NULL | False | False | NULL |
| 0003733D-2294-46D1-BE5A-E7DDEC5C68DA | 1600933 TS SK | B005BC1C-7C92-43F4-9E46-0848C12C27B5 | NULL | NULL | 2026-02-09T18:04:04.8430000 | NULL | False | False | NULL |
| 00036C3E-777A-4435-B77F-4446CB6FE91E | 1507745 L1 SK | 2149EE9C-7D96-4FF5-A07E-C8123B2C1496 | NULL | NULL | 2025-12-25T06:24:07.7300000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | SampleName | FileID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001DD28A-0B1C-445B-8FE3-17AFC004D19A | 1600057 F1 DK | A787B45A-F395-4DC8-BF26-57B686F0D20A | NULL | NULL | 2026-01-03T05:59:04.3970000 | NULL | False | False | NULL |
| 001A6FAB-30D9-4E1E-814B-48DD288616B0 | 1600069 L1 DK | E6705268-E527-4709-86A6-DC1C17EC2EA2 | NULL | NULL | 2026-01-03T17:59:04.3600000 | NULL | False | False | NULL |
| 00155C3E-4DA7-4723-B119-CC01D7B103A8 | BS 1020 PRI DK | 9F21A50C-CA21-4B66-95E6-3541438A4EFA | NULL | NULL | 2026-04-18T17:29:05.9100000 | NULL | False | False | NULL |
| 0011B791-0DA8-402E-B4EB-586101F381AB | 1507446 L2 DK | 211481A0-5B0E-437A-94E1-F7605EAFA59C | NULL | NULL | 2025-12-17T15:49:05.4300000 | NULL | False | False | NULL |
| 000EFC3E-0034-4CCF-AACF-18CBF2A37E83 | 1603372 L1 SANTOSH | B15B744F-DA17-4278-A260-F6A49ECFB45D | NULL | NULL | 2026-06-05T21:11:05.0700000 | NULL | False | False | NULL |
| 00065089-8381-46B8-B2FD-34856E2974BA | 1507789 F1 DK | 67CC9FC2-A0D1-4BE3-8150-0B934850AC0B | NULL | NULL | 2025-12-27T00:34:05.1030000 | NULL | False | False | NULL |
| 000627CC-D9EB-40E1-B4E9-56F81982BE86 | 1603326 TD VP Y | AA42C85D-51AB-4450-9F9F-83460A551B27 | NULL | NULL | 2026-06-03T06:42:04.6230000 | NULL | False | False | NULL |
| 00056610-864B-493C-BAE7-DE07B4B62162 | 1601259 L1 DK | 22C8931C-5F2B-4247-8D30-32650DB1DE2A | NULL | NULL | 2026-02-22T03:59:05.1730000 | NULL | False | False | NULL |
| 0003733D-2294-46D1-BE5A-E7DDEC5C68DA | 1600933 TS SK | B005BC1C-7C92-43F4-9E46-0848C12C27B5 | NULL | NULL | 2026-02-09T18:04:04.8430000 | NULL | False | False | NULL |
| 00036C3E-777A-4435-B77F-4446CB6FE91E | 1507745 L1 SK | 2149EE9C-7D96-4FF5-A07E-C8123B2C1496 | NULL | NULL | 2025-12-25T06:24:07.7300000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Quality_Spectro_Result.SampleID` -> `XStudio_XBatch.Quality_Spectro_Sample.ID` (Many to One)
