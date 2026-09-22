# XStudio_Xbatch.dbo.Breakers_Details

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference breaker, ecr, counter, earth, fault, ocand, position, reading, relay, capbank, name, ate.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-12T11:02:47.0000000 to 2026-09-02T07:51:48.0000000  

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
| TechnicianName | varchar | YES | 36 | — |
| OCandEarthFaultRelayCAPBank | varchar | YES | 100 | — |
| EngineerName | varchar | YES | 36 | — |
| BreakerPositionECR4A | varchar | YES | 100 | — |
| BreakerCounterReadingECR1 | int | YES | 10,0 | — |
| BreakerCounterReadingECR4A | int | YES | 10,0 | — |
| OCandEarthFaultRelayECR4Ate | varchar | YES | 100 | — |
| BreakerCounterReadingIC2 | int | YES | 10,0 | — |
| OCandEarthFaultRelayECR3 | varchar | YES | 100 | — |
| BreakerCounterReadingECR3 | int | YES | 10,0 | — |
| BreakerPositionBC | varchar | YES | 100 | — |
| OCandEarthFaultRelayECR2te | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| BreakerPositionECR3 | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| IsProcessed | bit | YES | — | — |
| OCandEarthFaultRelayECR2A | varchar | YES | 100 | — |
| OCandEarthFaultRelayECR1 | varchar | YES | 100 | — |
| BreakerPositionIC2 | varchar | YES | 100 | — |
| BreakerCounterReadingBC | int | YES | 10,0 | — |
| BreakerCounterReadingIC1 | int | YES | 10,0 | — |
| OCandEarthFaultRelayECR4 | varchar | YES | 100 | — |
| BreakerCounterReadingECR2A | int | YES | 10,0 | — |
| ReportDate | date | YES | — | — |
| Shift | varchar | YES | 100 | — |
| BreakerPositionECR2A | varchar | YES | 100 | — |
| BreakerCounterReadingECR4 | int | YES | 10,0 | — |
| OCandEarthFaultRelayIC2 | varchar | YES | 100 | — |
| BreakerCounterReadingECR2 | int | YES | 10,0 | — |
| OCandEarthFaultRelayBC | varchar | YES | 100 | — |
| BreakerPositionCAPBANK | varchar | YES | 100 | — |
| BreakerPositionECR2 | varchar | YES | 100 | — |
| BreakerPositionECR4 | varchar | YES | 100 | — |
| OCandEarthFaultRelayIC1 | varchar | YES | 100 | — |
| BreakerPositionECR1 | varchar | YES | 100 | — |
| BreakerPositionIC1 | varchar | YES | 100 | — |
| BreakerCounterReadingCAPBank | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 066AAFD9-C4AA-4F88-AB2A-9EC5C21377A8 | NULL | NULL | 2026-02-14T09:06:38.7530000 | NULL | False | False | NULL | NULL | NULL |
| 004A9CC3-D5DE-426C-A7A2-CB6B33D5B53C | NULL | NULL | 2026-06-25T12:37:51.5000000 | NULL | False | False | NULL | NULL | NULL |
| 133EB2E8-0042-473E-8573-08D77BBB132C | NULL | NULL | 2025-12-29T22:36:43.2530000 | NULL | False | False | NULL | NULL | NULL |
| 1A0F133F-367B-4B58-B23A-81B7856D88C2 | NULL | NULL | 2026-08-11T00:30:12.3930000 | NULL | False | False | NULL | NULL | NULL |
| 1A677477-89D1-44B2-885A-926D0C990ED9 | NULL | NULL | 2026-08-06T23:59:46.4800000 | NULL | False | False | NULL | NULL | NULL |
| 1C9FC9A2-1454-488E-B8DF-22C20DCC6FA8 | NULL | NULL | 2026-07-21T00:19:00.8300000 | NULL | False | False | NULL | NULL | NULL |
| 1CED08EB-D97C-4712-B4BE-D676B66BA316 | NULL | NULL | 2026-07-11T00:10:56.6330000 | NULL | False | False | NULL | NULL | NULL |
| 2448D04B-2E3C-42B6-A7F4-B5BA83EBAF37 | NULL | NULL | 2026-01-19T17:10:37.1570000 | NULL | False | False | NULL | NULL | NULL |
| 29644C6D-7F6E-4076-B098-F4D552FB6339 | NULL | NULL | 2026-08-01T00:48:30.9500000 | NULL | False | False | NULL | NULL | NULL |
| 2E2C4E1F-2BE2-4A33-8125-FB148260DEAB | NULL | NULL | 2026-05-03T19:50:55.8500000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C2A679E6-3351-445E-8AEA-BBE5D5666849 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:43.0070000 | 2026-09-02T07:51:48.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| CF960229-D4AA-476E-9E6D-D346A3C1323F | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7470000 | 2026-09-02T00:33:44.0000000 | False | False | NULL |  | NULL |
| A72899E4-53E5-4C49-8092-28636C9BF457 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.1830000 | 2026-09-01T08:00:57.0000000 | False | False | NULL |  | NULL |
| B449D844-C16C-4B15-94D0-3C6E6524D7DF | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1970000 | 2026-08-31T23:32:34.0000000 | False | False | NULL |  | NULL |
| C55339B5-3B47-4AC3-AE04-7506F69F1155 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.1000000 | 2026-08-30T22:58:09.0000000 | False | False | NULL |  | NULL |
| E735E9AA-7C32-4492-80CA-C7328FFCC10A | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.5300000 | 2026-08-30T01:14:07.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| B99B152E-D581-431C-A7AC-6A61108A8CE2 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T00:48:38.0770000 | 2026-08-29T00:54:08.0000000 | False | False | NULL |  | NULL |
| 397216F1-9F00-4E94-BD44-7C1019CCB339 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.7670000 | 2026-08-27T23:28:29.0000000 | False | False | NULL |  | NULL |
| 0A1AE62C-94A7-4647-85FA-0CDA68F87911 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0430000 | 2026-08-26T20:34:58.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 974D30AD-687A-46AC-B814-C680E3580390 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-25T20:01:32.2370000 | 2026-08-25T21:29:01.0000000 | False | False | NULL | 10.76.5.60 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Breakers_Details.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Breakers_Details.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
