# XStudio_Xbatch.dbo.SVC_Plus_Status

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference converter, dmwater, name, status, temp, tower, chiller, conductivity, engineer, flow, iltemp, level.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-12T11:06:32.0000000 to 2026-09-02T07:59:56.0000000  

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
| SVCPDMWaterTemp | decimal | YES | 18,2 | — |
| Tower1ConverterStatus | varchar | YES | 100 | — |
| ChillerWaterILTemp | decimal | YES | 18,2 | — |
| TechnicianName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| DMWaterLevel | int | YES | 10,0 | — |
| RoomTemp | decimal | YES | 18,2 | — |
| EntryDateTime | datetime | YES | — | — |
| EngineerName | varchar | YES | 36 | — |
| RunningPump | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| Conductivity | decimal | YES | 18,3 | — |
| Shift | varchar | YES | 100 | — |
| DMWaterFlow | int | YES | 10,0 | — |
| IsProcessed | bit | YES | — | — |
| Name | varchar | YES | 100 | — |
| Tower2ConverterStatus | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0683D5C9-6772-4FC3-95BB-AA1A86B88537 | NULL | NULL | 2026-08-24T01:28:17.4370000 | NULL | False | False | NULL | NULL | NULL |
| 061F4559-24DD-4610-A89E-5E9BC12AA4FD | NULL | NULL | 2026-08-01T23:46:19.7230000 | NULL | False | False | NULL | NULL | NULL |
| 03EC8E64-BA40-4141-8D66-28DD50933E6B | NULL | NULL | 2026-07-13T00:50:22.2900000 | NULL | False | False | NULL | NULL | NULL |
| 1404158C-42E4-434C-A086-C4C8BF774DDD | NULL | NULL | 2026-07-31T01:09:14.4370000 | NULL | False | False | NULL | NULL | NULL |
| 1FB9BC64-C06C-486B-9A06-A2F8C81ECB77 | NULL | NULL | 2026-08-01T00:48:31.0100000 | NULL | False | False | NULL | NULL | NULL |
| 21BA93B4-09B9-43B6-A5DB-713064B6BAF8 | NULL | NULL | 2026-08-02T18:11:59.9600000 | NULL | False | False | NULL | NULL | NULL |
| 26348191-5267-4CA9-AB47-5E3367AE0D91 | NULL | NULL | 2026-07-21T00:19:00.8900000 | NULL | False | False | NULL | NULL | NULL |
| 29C0488C-665A-4CB2-855C-CF8D75490F86 | NULL | NULL | 2026-07-22T00:18:14.0900000 | NULL | False | False | NULL | NULL | NULL |
| 30F9A4E3-16B4-40F9-8470-0B42F4F35437 | NULL | NULL | 2026-07-14T01:17:37.6930000 | NULL | False | False | NULL | NULL | NULL |
| 31DE0875-E647-437B-97A9-0DF78472FCED | NULL | NULL | 2026-02-26T07:33:45.4800000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 027892EC-224B-4DBA-90A4-C843A505CC15 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:43.0430000 | 2026-09-02T07:59:56.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| D3B556D1-C7B3-4283-89C9-A648064656E2 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7830000 | 2026-09-02T00:35:18.0000000 | False | False | NULL |  | NULL |
| 1C026DC3-C315-4EB6-834B-12AF94584C3B | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.2130000 | 2026-09-01T08:03:54.0000000 | False | False | NULL |  | NULL |
| C1DF8266-3989-4317-A141-100A44633BF9 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.2270000 | 2026-09-01T00:11:52.0000000 | False | False | NULL |  | NULL |
| A97D7675-5774-4F68-ABBD-1006E92F071A | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.1370000 | 2026-08-30T23:32:23.0000000 | False | False | NULL |  | NULL |
| 7739BD4D-8719-4E3A-8893-469E7FEFCFEF | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.5630000 | 2026-08-30T01:18:00.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| A0F7FF12-A8FE-4910-80DF-9AA18C6A36AA | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T00:48:38.1230000 | 2026-08-29T00:58:32.0000000 | False | False | NULL |  | NULL |
| B2222D6C-CA4B-48F8-AD7B-52A7AA8F9029 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0730000 | 2026-08-26T20:21:12.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| D3F0A7D4-46DD-4212-ADD9-A228BA531395 | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.2630000 | 2026-08-25T20:34:32.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| DED89E3E-736A-4F39-8A67-FDDCD8C6CAB6 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-23T00:12:23.1530000 | 2026-08-23T00:29:48.0000000 | False | False | NULL | 172.16.4.185 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.SVC_Plus_Status.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SVC_Plus_Status.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
