# XStudio_Xbatch.dbo.Earthing_Transfomer

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference mva, breather, conservator, etransformer, gelandoillevel, level, name, nerstatus, oil, silica, engineer, shift.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-12-23T02:40:57.0000000 to 2026-09-02T08:04:20.0000000  

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
| NERStatus63MVA | varchar | YES | 100 | — |
| ConservatorOilLevel63MVA | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| ReportDate | date | YES | — | — |
| Shift | varchar | YES | 100 | — |
| BreatherSilicaGelandoillevelETransformer63 | varchar | YES | 100 | — |
| NERStatus125MVA | varchar | YES | 100 | — |
| TechnicianName | varchar | YES | -1 | — |
| BreatherSilicaGelandoillevelETransformer125 | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| EngineerName | varchar | YES | -1 | — |
| ParentID | varchar | YES | 36 | — |
| ConservatorOilLevel125MVA | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1253B663-CD81-4794-AAF6-CDB985A69EAF | NULL | NULL | 2026-08-14T00:44:39.2400000 | NULL | False | False | NULL | NULL | NULL |
| 23F54AEF-AAC2-4249-A47F-0AED3F70355F | NULL | NULL | 2026-05-03T19:50:55.7900000 | NULL | False | False | NULL | NULL | NULL |
| 2B92B5E8-2B04-4C41-9EE7-8D675E075859 | NULL | NULL | 2026-08-01T00:48:30.8770000 | NULL | False | False | NULL | NULL | NULL |
| 324143E7-7B44-420D-91B9-2925F93FDD20 | NULL | NULL | 2026-02-25T19:50:37.1230000 | NULL | False | False | NULL | NULL | NULL |
| 34CBBD19-5D9A-421B-ADFC-FB478F5017FC | NULL | NULL | 2026-02-05T20:53:11.0970000 | NULL | False | False | NULL | NULL | NULL |
| 35D27B92-7D24-4731-8412-FB2D8DC4ADA7 | NULL | NULL | 2026-08-04T18:45:03.9700000 | NULL | False | False | NULL | NULL | NULL |
| 3EB0A5C4-28CC-4400-94DF-64B44B6A89F2 | NULL | NULL | 2026-08-05T18:40:50.3800000 | NULL | False | False | NULL | NULL | NULL |
| 3FDBA620-EFD5-44A7-AEA0-D3E936347BA6 | NULL | NULL | 2025-09-10T09:03:55.2000000 | NULL | False | False | NULL | NULL |  |
| 42B30517-5C48-4300-B176-70925D4FD42D | NULL | NULL | 2026-07-20T00:40:26.9930000 | NULL | False | False | NULL | NULL | NULL |
| 4507CA62-422B-422B-8A71-5523B3DEFEB0 | NULL | NULL | 2026-08-11T00:30:12.3070000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B23D1AA5-ADB3-4852-92AC-FEDBFCCD5609 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9370000 | 2026-09-02T08:04:20.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 47D1BAC7-BFC0-4059-8E29-D71CFA8D5F62 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.6930000 | 2026-09-02T00:37:08.0000000 | False | False | NULL |  | NULL |
| 8ECFB8EA-9E71-4D37-AC75-5BE4914DFB59 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1400000 | 2026-08-31T23:37:06.0000000 | False | False | NULL |  | NULL |
| D7EC0C3A-564D-445F-96D7-F92DDF9EB393 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.0300000 | 2026-08-30T23:06:10.0000000 | False | False | NULL |  | NULL |
| 0CFE9FF5-332A-4326-A2D1-415A56AB643F | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.4530000 | 2026-08-30T00:43:35.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 225E46AF-AECF-478B-B71F-E36718001E3A | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:38.0030000 | 2026-08-29T01:16:08.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 4FDE6B80-C988-4911-9562-1FC77D01519F | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.7000000 | 2026-08-28T00:41:12.0000000 | False | False | NULL |  | NULL |
| 6CE598D9-3795-48F5-9D80-1CF55D294B79 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:53.9800000 | 2026-08-26T20:23:06.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 24B2A3E9-993B-481E-AFD3-6E035CE52D26 | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.1970000 | 2026-08-25T20:13:07.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 451CC0E9-24D2-45B7-B1AA-D5F1288889AA | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-23T00:12:23.0170000 | 2026-08-23T00:40:11.0000000 | False | False | NULL | 172.16.4.185 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Earthing_Transfomer.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Earthing_Transfomer.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
