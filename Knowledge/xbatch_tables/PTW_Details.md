# XStudio_Xbatch.dbo.PTW_Details

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference name, engineer, noof, ptwissued, ptwno, shift, technician.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-12-30T15:18:00.0000000 to 2026-09-02T08:00:21.0000000  

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
| EngineerName | varchar | YES | 36 | — |
| PTWNO | decimal | YES | 18,2 | — |
| Shift | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| NOofPTWIssued | decimal | YES | 18,2 | — |
| ReportDate | date | YES | — | — |
| TechnicianName | varchar | YES | 36 | — |
| ParentID | varchar | YES | 36 | — |
| IsProcessed | bit | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 061504D9-C943-4A4A-B0B0-5D51B6814173 | NULL | NULL | 2026-02-24T19:44:37.7870000 | NULL | False | False | NULL | NULL | NULL |
| 04C54ECF-94B8-4D0E-BE27-911DEA733338 | NULL | NULL | 2026-06-13T07:20:57.1900000 | NULL | False | False | NULL | NULL | NULL |
| 08DD292D-BA04-4E1E-80C5-3019E2983740 | NULL | NULL | 2026-01-29T09:19:17.9500000 | NULL | False | False | NULL | NULL | NULL |
| 0A5FAA36-67F2-48F3-B85F-1C903209E2FC | NULL | NULL | 2026-07-22T00:18:14.1300000 | NULL | False | False | NULL | NULL | NULL |
| 0F0B3AFC-78DA-497B-BD63-F2C2F1737A3E | NULL | NULL | 2026-05-27T19:23:04.9170000 | NULL | False | False | NULL | NULL | NULL |
| 1006C67F-4AD5-49D1-84C6-5496BCD0E459 | NULL | NULL | 2026-01-14T08:40:14.6800000 | NULL | False | False | NULL | NULL | NULL |
| 11CFE6FF-138A-4B79-A288-89CC43E4CC21 | NULL | NULL | 2026-02-26T07:33:45.5200000 | NULL | False | False | NULL | NULL | NULL |
| 166214E4-58F2-41C0-9ECB-BB97D78DEAC6 | NULL | NULL | 2026-01-31T19:49:12.0270000 | NULL | False | False | NULL | NULL | NULL |
| 1AD65939-1F39-47DF-A9E6-F2B58042A6F9 | NULL | NULL | 2026-07-31T01:09:14.4700000 | NULL | False | False | NULL | NULL | NULL |
| 1C195A12-87E2-4FE0-A9F0-267233B1EFCD | NULL | NULL | 2026-05-09T07:35:13.1300000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6887B059-260A-4D34-BF26-913830ACB84A | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:43.0770000 | 2026-09-02T08:00:21.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 8F70FF38-3D4D-4AE6-8BB5-3E5F1053B451 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.8200000 | 2026-09-02T00:35:28.0000000 | False | False | NULL |  | NULL |
| 400A3B3A-6BF8-453A-974C-CB805DA4E50B | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.2430000 | 2026-09-01T08:04:06.0000000 | False | False | NULL |  | NULL |
| ED88704E-C93B-40CF-94A9-414EE2FEE4EA | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.2530000 | 2026-08-31T23:35:31.0000000 | False | False | NULL |  | NULL |
| 672200D7-A187-4432-A56F-38EAAA098357 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.1730000 | 2026-08-30T23:03:02.0000000 | False | False | NULL |  | NULL |
| F4EE8047-B894-48EA-A9A0-32019A68D4D4 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.5930000 | 2026-08-30T00:41:59.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| B86619F6-C138-481F-BD96-585232D0C63E | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:38.1670000 | 2026-08-29T01:12:50.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| E6ADC130-7398-4DCB-BAE7-DB665CA65CB4 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.8400000 | 2026-08-27T23:31:22.0000000 | False | False | NULL |  | NULL |
| D0EC8844-8952-4759-88EC-4E635D070390 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.1000000 | 2026-08-26T20:21:43.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 4ED6347D-876E-4B64-B08C-4827CA3154AC | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-25T20:01:32.2930000 | 2026-08-25T21:27:52.0000000 | False | False | NULL | 10.76.5.60 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.PTW_Details.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.PTW_Details.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
