# XStudio_Xbatch.dbo.Power_Meter_Reading_Time

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference feeder, mwh, kvf, mvah, amvah, amwh, mvamwh, name, eaffeeder, ecr, engineer, fdrmwh.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-12-30T16:43:46.0000000 to 2026-09-02T07:59:17.0000000  

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
| TX1TX5MVAH | decimal | YES | 18,6 | — |
| TX1TX5MWH | decimal | YES | 18,6 | — |
| NOofHeatTapped | decimal | YES | 18,6 | — |
| Feeder33KVF2MWH | decimal | YES | 18,6 | — |
| TX2TX2AMVAH | decimal | YES | 18,6 | — |
| Feeder15MVAMWH | decimal | YES | 18,6 | — |
| IC1MWH66 | decimal | YES | 18,6 | — |
| Feeder132KVF2MWH | decimal | YES | 18,6 | — |
| IsProcessed | bit | YES | — | — |
| Feeder33KVF1MVAH | decimal | YES | 18,3 | — |
| Feeder33KVF1MWH | decimal | YES | 18,6 | — |
| ParentID | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| Feeder132KVF1MWH | decimal | YES | 18,6 | — |
| Feeder33KVF2MVAH | decimal | YES | 18,6 | — |
| TX4TX4AMWH | decimal | YES | 18,6 | — |
| Shift | varchar | YES | 100 | — |
| RollingMillFDRMWH | decimal | YES | 18,6 | — |
| Feeder132KVF2MVAH | decimal | YES | 18,3 | — |
| Feeder132KVF1MVAH | decimal | YES | 18,6 | — |
| IC2MWH66 | decimal | YES | 18,6 | — |
| ECR5MWH | decimal | YES | 18,6 | — |
| TX2TX2AMWH | decimal | YES | 18,6 | — |
| TX4TX4AMVAH | decimal | YES | 18,6 | — |
| Name | varchar | YES | 100 | — |
| TX3TX3AMWH | decimal | YES | 18,6 | — |
| TechnicianName | varchar | YES | 36 | — |
| TX3TX3AMVAH | decimal | YES | 18,6 | — |
| LRFFeederMWH | decimal | YES | 18,6 | — |
| EngineerName | varchar | YES | 36 | — |
| Feeder24MVAMWH | decimal | YES | 18,6 | — |
| EntryDateTime | datetime | YES | — | — |
| EAFFeederMWH | decimal | YES | 18,6 | — |
| WRMMWH | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0AB25F8A-7E1B-4BE7-B3DB-1D2CFD0182F8 | NULL | NULL | 2026-05-31T19:42:25.0230000 | NULL | False | False | NULL | NULL | NULL |
| 04E1A85F-EFA1-431B-B1C4-5362D1EDE4B0 | NULL | NULL | 2026-01-29T20:19:52.4630000 | NULL | False | False | NULL | NULL | NULL |
| 03474353-4222-4635-B71C-99C528528283 | NULL | NULL | 2026-04-30T08:06:41.9300000 | NULL | False | False | NULL | NULL | NULL |
| 0DE561A6-AD36-45B4-B422-E198A2DF851C | NULL | NULL | 2026-06-25T12:37:51.5230000 | NULL | False | False | NULL | NULL | NULL |
| 26117CC3-ED7F-4937-9B49-AE3DD6770F99 | NULL | NULL | 2026-02-02T19:30:47.1470000 | NULL | False | False | NULL | NULL | NULL |
| 27C97B19-BE08-4CE9-B9EE-9FA41E6281A7 | NULL | NULL | 2026-09-01T07:57:43.2030000 | NULL | False | False | NULL | NULL | NULL |
| 318E2FD0-A672-4922-95B1-FC56610E90FA | NULL | NULL | 2026-01-23T09:09:31.5270000 | NULL | False | False | NULL | NULL | NULL |
| 342A7C93-EFCB-4033-8462-974127536F44 | NULL | NULL | 2026-06-12T08:29:02.4630000 | NULL | False | False | NULL | NULL | NULL |
| 3A3D7923-DCEA-4BFF-B556-01C9EB356729 | NULL | NULL | 2025-09-10T09:03:55.3670000 | NULL | False | False | NULL | NULL |  |
| 3B0B3F6E-BDA0-4BAC-B492-26FE43C2480A | NULL | NULL | 2026-01-19T17:10:37.1800000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D36297E4-6E86-4157-A405-0BD3FBE6CCD9 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:43.0300000 | 2026-09-02T07:59:17.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 7730F621-770E-4DDB-861F-16A32078E8ED | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7730000 | 2026-09-02T00:28:08.0000000 | False | False | NULL |  | NULL |
| 99654E5D-5C85-4639-BCBB-73FE1A0294FC | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.2130000 | 2026-09-01T00:15:04.0000000 | False | False | NULL |  | NULL |
| 7C6002B7-7359-4408-84DE-01F574537BFF | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T00:48:38.1000000 | 2026-08-31T06:29:17.0000000 | False | False | NULL |  | NULL |
| 3A02D260-3CE6-4A8F-AE02-9AFD47899242 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-27T23:25:11.7900000 | 2026-08-31T06:28:54.0000000 | False | False | NULL |  | NULL |
| 8A2CE6F5-B3FE-46B8-8E79-E80D30D5E732 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0630000 | 2026-08-31T06:28:22.0000000 | False | False | NULL |  | NULL |
| C126A386-C902-44A8-B11A-DF059B104D2D | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-25T20:01:32.2530000 | 2026-08-31T06:27:55.0000000 | False | False | NULL |  | NULL |
| 311D8284-5CA1-495E-9159-63F4879A427C | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-25T00:58:05.6000000 | 2026-08-31T06:27:27.0000000 | False | False | NULL |  | NULL |
| 4A6AF4E0-4912-4A2A-8414-156B33006FE5 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-24T01:28:17.4270000 | 2026-08-31T06:26:26.0000000 | False | False | NULL |  | NULL |
| CE562BA5-43ED-4296-8628-E2D72F29F34D | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.1230000 | 2026-08-31T00:03:44.0000000 | False | False | NULL |  | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Power_Meter_Reading_Time.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Power_Meter_Reading_Time.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
