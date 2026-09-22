# XStudio_Xbatch.dbo.Lightning_Arrestor_Counter_Reading

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference end, cable, xmer, name, engineer, shift, technician.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-12-23T02:28:15.0000000 to 2026-09-02T08:01:32.0000000  

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
| F2CableEndY | int | YES | 10,0 | — |
| F1CableEndB | int | YES | 10,0 | — |
| F1CableEndR | int | YES | 10,0 | — |
| F2CableEndB | int | YES | 10,0 | — |
| F1XmerEndB | int | YES | 10,0 | — |
| F2XmerEndY | int | YES | 10,0 | — |
| F1XmerEndR | int | YES | 10,0 | — |
| Shift | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| F1XmerEndY | int | YES | 10,0 | — |
| EngineerName | varchar | YES | -1 | — |
| F2CableEndR | int | YES | 10,0 | — |
| IsProcessed | bit | YES | — | — |
| F1CableEndY | int | YES | 10,0 | — |
| TechnicianName | varchar | YES | -1 | — |
| Name | varchar | YES | 100 | — |
| F2XmerEndR | int | YES | 10,0 | — |
| F2XmerEndB | int | YES | 10,0 | — |
| ReportDate | date | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00E94F7E-9DBC-4E3A-A16F-7BBCD2A81EC4 | NULL | NULL | 2026-05-14T08:04:15.3000000 | NULL | False | False | NULL | NULL | NULL |
| 04CBD0B4-A9A8-4509-9369-1A4958610F96 | NULL | NULL | 2026-01-22T19:43:13.9230000 | NULL | False | False | NULL | NULL | NULL |
| 0A3E54BC-9BDB-4AA2-B2BB-56AD20798423 | NULL | NULL | 2025-12-27T06:24:18.8870000 | NULL | False | False | NULL | NULL | NULL |
| 0B2EBFC9-F775-4A89-9066-269D1DD6A70A | NULL | NULL | 2026-02-24T19:44:37.7830000 | NULL | False | False | NULL | NULL | NULL |
| 0C51F651-4DDD-4DFD-A4FC-FC92D3E61209 | NULL | NULL | 2026-07-23T00:20:25.4970000 | NULL | False | False | NULL | NULL | NULL |
| 18CC7B13-DE91-47BC-90CE-AF00BB63428F | NULL | NULL | 2026-07-11T00:10:56.5570000 | NULL | False | False | NULL | NULL | NULL |
| 22173498-24F3-4BF6-ACF9-513454482474 | NULL | NULL | 2026-01-14T08:40:14.4600000 | NULL | False | False | NULL | NULL | NULL |
| 28A8A83D-4FFD-4629-BBFC-52DCA95750ED | NULL | NULL | 2026-02-26T07:33:45.3030000 | NULL | False | False | NULL | NULL | NULL |
| 2E9E84A9-3B18-41D7-AB98-3C93919C0477 | NULL | NULL | 2025-12-27T23:25:44.2200000 | NULL | False | False | NULL | NULL | NULL |
| 31FBB9E9-1751-4488-8EB3-D15C574194F1 | NULL | NULL | 2026-06-25T12:37:51.3770000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 75A929DA-C50D-4F95-BED0-5C19924CA11E | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9170000 | 2026-09-02T08:01:32.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| B8984673-B38E-4F18-BA09-361DCDB9D1DB | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.6700000 | 2026-09-02T00:35:50.0000000 | False | False | NULL |  | NULL |
| A8E24582-7DF0-4472-B948-62A026279A5C | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.0930000 | 2026-09-01T08:04:49.0000000 | False | False | NULL |  | NULL |
| 47808213-6826-4A20-887D-D9904BCEF43A | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1170000 | 2026-08-31T23:35:56.0000000 | False | False | NULL |  | NULL |
| 1040CC5B-EE24-4D93-B3EE-DB22E45E88F6 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.0100000 | 2026-08-30T23:03:50.0000000 | False | False | NULL |  | NULL |
| 51C14251-5F82-498C-92E9-45DC6E9FEB5F | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.4300000 | 2026-08-30T00:42:37.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 625C9E20-ABDA-4300-B0F6-5004957107E6 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T00:48:37.9800000 | 2026-08-29T01:00:22.0000000 | False | False | NULL |  | NULL |
| EA3327F8-098C-41DF-8A9F-571CC82217D0 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.6800000 | 2026-08-27T23:31:39.0000000 | False | False | NULL |  | NULL |
| 727A522D-34FF-4694-9BF9-25631C98FE29 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:53.9570000 | 2026-08-26T20:22:34.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 11002CAD-19ED-4A7C-922E-213D4ACF0960 | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.1830000 | 2026-08-25T20:11:40.0000000 | False | False | NULL | 10.76.5.60 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Lightning_Arrestor_Counter_Reading.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Lightning_Arrestor_Counter_Reading.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
