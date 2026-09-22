# XStudio_Xbatch.dbo.Transformer_Sprinkler_Station_Status

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference pump, main, status, line, mva, name, station, sub, acstatus, alarm, diesel, engineer.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-12-23T02:27:50.0000000 to 2026-09-02T08:01:14.0000000  

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
| MainPump | varchar | YES | 36 | — |
| ParentID | varchar | YES | 36 | — |
| Name | varchar | YES | 100 | — |
| EngineerName | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| VDC24Supply | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| MainLinePR125MVA | int | YES | 10,0 | — |
| SVCPACStatus | varchar | YES | 100 | — |
| SubStationACStatus | varchar | YES | 100 | — |
| FireAlarmPanelStatus | varchar | YES | 100 | — |
| MainLinePR63MVA | int | YES | 10,0 | — |
| SVCPStatus | varchar | YES | 100 | — |
| PumpHouseStatus | varchar | YES | 100 | — |
| TechnicianName | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |
| P3415VACSupply | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| DieselPump | varchar | YES | 36 | — |
| JockeyPump | varchar | YES | 36 | — |
| SubStationStatus | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00AE9E46-4443-4E9D-A735-D2A5FA00F09E | NULL | NULL | 2025-12-29T22:36:43.3100000 | NULL | False | False | NULL | NULL | NULL |
| 000B5B74-E33C-4F08-8A2D-51643789ABB7 | NULL | NULL | 2026-08-05T18:40:50.4970000 | NULL | False | False | NULL | NULL | NULL |
| 02628F3E-57D8-4E55-AAE0-A02420EE88C4 | NULL | NULL | 2026-07-22T00:18:14.1170000 | NULL | False | False | NULL | NULL | NULL |
| 11493A26-9CF1-4FD5-9BA5-68FD8036B3A8 | NULL | NULL | 2026-07-30T18:26:54.9330000 | NULL | False | False | NULL | NULL | NULL |
| 175DFAF2-5C2D-4836-90C6-F615100A9444 | NULL | NULL | 2026-08-11T00:30:12.4800000 | NULL | False | False | NULL | NULL | NULL |
| 1E70FDCF-2E76-47BD-B7C7-351E5D535A62 | NULL | NULL | 2025-09-10T09:03:55.4270000 | NULL | False | False | NULL | NULL |  |
| 2159D62A-6D5D-4DD2-A4E2-77E320AC2110 | NULL | NULL | 2026-08-04T18:45:04.0970000 | NULL | False | False | NULL | NULL | NULL |
| 25A41271-2014-44AF-A6F3-49AFEBFE822F | NULL | NULL | 2026-07-31T01:09:14.4600000 | NULL | False | False | NULL | NULL | NULL |
| 27744782-7218-4401-9144-8CB7565B0645 | NULL | NULL | 2026-06-25T12:37:51.5500000 | NULL | False | False | NULL | NULL | NULL |
| 3335A063-EC4E-4145-A59A-854EE22D81FE | NULL | NULL | 2026-03-24T21:11:53.5730000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CFBFDDE0-B3CB-41BF-8614-B6F03E9C4CB1 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:43.0630000 | 2026-09-02T08:01:14.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| D6A0BE80-0A76-4D88-B01A-B078CD560C6D | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.8070000 | 2026-09-02T00:35:41.0000000 | False | False | NULL |  | NULL |
| 048E5ACF-FC0B-47D0-892C-62934B3BC8D8 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.2330000 | 2026-09-01T08:04:29.0000000 | False | False | NULL |  | NULL |
| 9F228F28-10F3-4608-981F-BE8E6617FC46 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.2430000 | 2026-08-31T23:35:44.0000000 | False | False | NULL |  | NULL |
| 11D876B4-7937-409A-9CF9-962445FF4402 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.1630000 | 2026-08-30T23:03:37.0000000 | False | False | NULL |  | NULL |
| 39A6125A-4772-4CBA-8ED3-3EB85A03C7AF | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.5830000 | 2026-08-30T00:42:20.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 1FD51E1A-BC4B-4D36-91BC-071375C065E9 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T00:48:38.1570000 | 2026-08-29T01:00:07.0000000 | False | False | NULL |  | NULL |
| 9855EC24-1DCB-46CB-B740-16E25272872E | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.8270000 | 2026-08-28T00:39:32.0000000 | False | False | NULL |  | NULL |
| C91AD3F6-07D3-4919-94D8-1561484490E4 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0900000 | 2026-08-26T20:22:19.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 48491B30-ECC6-44BB-A55E-1EAA0D0076B4 | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.2900000 | 2026-08-25T20:09:56.0000000 | False | False | NULL | 10.76.5.60 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_Sprinkler_Station_Status.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Transformer_Sprinkler_Station_Status.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
