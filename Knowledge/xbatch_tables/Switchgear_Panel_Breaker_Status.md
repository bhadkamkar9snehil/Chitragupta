# XStudio_Xbatch.dbo.Switchgear_Panel_Breaker_Status

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference panel, switchgear, bank, incomer, mva, name, bus, coupler, eafswitchgear, engineer, lrfswitchgear, mill.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-12-30T15:17:50.0000000 to 2026-09-02T08:07:24.0000000  

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
| EAFSwitchgearPanel | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Shift | varchar | YES | 100 | — |
| BusCouplerSwitchgearPanel | varchar | YES | 100 | — |
| MVA24SwitchgearPanel | varchar | YES | 100 | — |
| Incomer233kv | varchar | YES | 100 | — |
| SVCPFilterBank | varchar | YES | 100 | — |
| RollingMillSwitchgearPanel | varchar | YES | 100 | — |
| SVCTCRSwitchgearPanel | varchar | YES | 100 | — |
| LRFSwitchgearPanel | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| SVCPVSCSwitchgearPanel | varchar | YES | 100 | — |
| SVCFilterBank | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| TechnicianName | varchar | YES | 36 | — |
| Incomer133kv | varchar | YES | 100 | — |
| MVA15SwitchgearPanel | varchar | YES | 100 | — |
| EngineerName | varchar | YES | 36 | — |
| WRM | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0403F1E7-96C0-4AFF-A022-33966BFC5F33 | NULL | NULL | 2026-01-25T12:55:56.8770000 | NULL | False | False | NULL | NULL | NULL |
| 0729AAD6-BC40-49FE-BE69-45757EE1030B | NULL | NULL | 2026-02-24T19:44:37.7830000 | NULL | False | False | NULL | NULL | NULL |
| 08AEE53C-6459-4B77-B889-2999DCB52762 | NULL | NULL | 2026-07-18T00:48:14.3330000 | NULL | False | False | NULL | NULL | NULL |
| 08CB1401-3FC3-4E01-8317-4F9B43B91E9B | NULL | NULL | 2026-08-15T00:12:41.3270000 | NULL | False | False | NULL | NULL | NULL |
| 0AF26F93-5ECF-4BDD-B5AE-C33618DA0386 | NULL | NULL | 2026-08-05T18:40:50.4030000 | NULL | False | False | NULL | NULL | NULL |
| 0D2ABDE5-841D-4A37-B100-E4D11F11C202 | NULL | NULL | 2026-02-14T09:06:38.7000000 | NULL | False | False | NULL | NULL | NULL |
| 11AA07E6-E168-404A-B51E-13B05299FB21 | NULL | NULL | 2025-12-27T23:25:44.2630000 | NULL | False | False | NULL | NULL | NULL |
| 12C0E8B9-A9FC-4080-98DD-83EAABC6A9BA | NULL | NULL | 2025-12-27T06:24:18.9200000 | NULL | False | False | NULL | NULL | NULL |
| 13D06A41-C9A4-449D-B5DF-7CDC4B2EDA0A | NULL | NULL | 2026-03-24T21:11:53.4830000 | NULL | False | False | NULL | NULL | NULL |
| 1516AAFD-3AC7-4697-A2C1-F942117CFE01 | NULL | NULL | 2026-08-24T01:28:17.3500000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DBE94E4C-85A0-4399-B79F-9B354365DD14 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9600000 | 2026-09-02T08:07:24.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| F71C7727-963A-4939-99D9-B3D8B6ADB329 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7100000 | 2026-09-02T00:39:08.0000000 | False | False | NULL |  | NULL |
| 6F5740B0-E6A6-4D5B-A0ED-C5DC2BEDF13B | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1600000 | 2026-08-31T23:38:07.0000000 | False | False | NULL |  | NULL |
| C2219E9E-A47F-48D1-82B3-3E7658A0218D | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.0530000 | 2026-08-30T23:07:49.0000000 | False | False | NULL |  | NULL |
| 8051FC26-1F47-4844-9805-7380C60F55AD | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.4770000 | 2026-08-30T00:44:39.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| E9F01115-AC0F-4328-AEB6-8A0887CFF939 | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:38.0270000 | 2026-08-29T01:18:12.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 06CB7B53-871F-4552-8D85-44AC6D232A7A | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.7200000 | 2026-08-28T00:42:27.0000000 | False | False | NULL |  | NULL |
| 161D9A0C-6ECB-4C82-8715-1A07ABCFD338 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0000000 | 2026-08-26T20:23:42.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 57E832BC-296C-4564-A5B1-C0B20A9DB10D | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.2100000 | 2026-08-25T20:23:48.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 9FF16B04-698E-4B9A-80C5-C090ED792D5E | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-23T00:12:23.0600000 | 2026-08-23T00:57:34.0000000 | False | False | NULL | 172.16.4.185 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Switchgear_Panel_Breaker_Status.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Switchgear_Panel_Breaker_Status.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
