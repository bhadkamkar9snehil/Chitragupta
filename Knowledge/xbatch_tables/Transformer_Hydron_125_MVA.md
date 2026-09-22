# XStudio_Xbatch.dbo.Transformer_Hydron_125_MVA

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference pre, transformer, hydron, name, olevel, ppm, rhlevel, rhsence, temp, engineer, shift, technician.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-10T09:05:09.0000000 to 2026-09-02T08:00:14.0000000  

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
| Shift | varchar | YES | 100 | — |
| PreRHSenceTemp | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| HydronPPM | varchar | YES | 100 | — |
| H2OLevel | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| Name | varchar | YES | 100 | — |
| TechnicianName | varchar | YES | 36 | — |
| ParentID | varchar | YES | 36 | — |
| EngineerName | varchar | YES | 36 | — |
| PreRHLevel | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| TransformerPreRHSenceTemp | decimal | YES | 18,4 | — |
| TransformerHydronPPM | decimal | YES | 18,4 | — |
| TransformerPreRHLevel | decimal | YES | 18,4 | — |
| TransformerH2OLevel | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0162C9BD-735F-4AB6-9F80-A1F0B1497459 | NULL | NULL | 2026-01-09T19:41:08.6130000 | NULL | False | False | NULL | NULL | NULL |
| 126AB36B-BC28-4B8C-B548-458238BD46CA | NULL | NULL | 2026-07-22T00:18:14.1030000 | NULL | False | False | NULL | NULL | NULL |
| 129E815A-366D-43B3-AE43-F36FC905EB56 | NULL | NULL | 2026-07-31T01:09:14.4470000 | NULL | False | False | NULL | NULL | NULL |
| 18EC46D8-AE1A-46D8-8A14-863720EE19D9 | NULL | NULL | 2025-12-31T21:41:01.0900000 | NULL | False | False | NULL | NULL | NULL |
| 1933F4E2-93E3-4748-8B18-FA6629BD05BF | NULL | NULL | 2026-05-29T10:57:37.1900000 | NULL | False | False | NULL | NULL | NULL |
| 1CABF9AD-B6F1-4163-A85D-F90362BB2604 | NULL | NULL | 2026-07-24T00:00:32.7000000 | NULL | False | False | NULL | NULL | NULL |
| 1CC1B56B-CF27-462D-B2E7-1B2EF46F5D2D | NULL | NULL | 2026-05-23T19:21:06.9400000 | NULL | False | False | NULL | NULL | NULL |
| 2396F354-211D-4430-BF16-EE9ACAEF73DD | NULL | NULL | 2026-08-05T18:40:50.4870000 | NULL | False | False | NULL | NULL | NULL |
| 2AA86D3D-1C94-4CA6-B7CF-44D0894EE07E | NULL | NULL | 2026-08-02T18:11:59.9700000 | NULL | False | False | NULL | NULL | NULL |
| 2D059EB9-17F6-4063-8A4A-880D55338100 | NULL | NULL | 2026-08-15T00:12:41.4130000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6B91EA81-BB6C-4978-B45C-11EDAFC02555 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:43.0530000 | 2026-09-02T08:00:14.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 56BE7072-37B3-459A-B28C-BAE2D58FC634 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7970000 | 2026-09-02T00:35:27.0000000 | False | False | NULL |  | NULL |
| E37D4AA6-B7A5-48C5-87A9-224DE4FC680C | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.2230000 | 2026-09-01T08:04:01.0000000 | False | False | NULL |  | NULL |
| 03E48764-F6AB-4733-B411-9ABA9286D5BA | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.2330000 | 2026-08-31T23:35:32.0000000 | False | False | NULL |  | NULL |
| 7AB5EE86-11D9-4C7A-BA15-08403B9F253F | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.1500000 | 2026-08-30T23:02:59.0000000 | False | False | NULL |  | NULL |
| A3E1E164-6852-414B-B4AA-3563CA1A4ABA | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.5730000 | 2026-08-30T00:41:50.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 7A509CC7-B499-4AE7-855B-7625E6812FAF | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:38.1430000 | 2026-08-29T01:12:39.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 4DF551C9-7107-4B06-B67F-DCBAD6B839C8 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.8130000 | 2026-08-27T23:31:23.0000000 | False | False | NULL |  | NULL |
| FD0335A6-8C1C-4DBF-BEB8-F7BD18BB287F | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0800000 | 2026-08-26T20:21:32.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 82D28037-088A-47CE-A65E-503879D657E6 | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.2800000 | 2026-08-25T20:07:18.0000000 | False | False | NULL | 10.76.5.60 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_Hydron_125_MVA.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Transformer_Hydron_125_MVA.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
