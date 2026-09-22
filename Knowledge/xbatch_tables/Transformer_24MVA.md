# XStudio_Xbatch.dbo.Transformer_24MVA

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference current, rated, primary, secondary, changer, status, tap, breather, level, oil, transformer, voltage.

**Primary Key:** ID  
**Row Count:** 463  
**Date Range (ModifiedOn):** 2025-08-02T10:24:27.0000000 to 2026-09-01T01:17:10.0000000  

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
| OilLevelTapChanger | decimal | YES | 18,4 | — |
| RatedPrimaryCurrent276AY | decimal | YES | 18,4 | — |
| Attendant | varchar | YES | 36 | — |
| RatedPrimaryCurrentR276A | decimal | YES | 18,4 | — |
| TapChangerCounter | decimal | YES | 18,4 | — |
| IsProcessed | bit | YES | — | — |
| Remarks | varchar | YES | -1 | — |
| PrimaryVoltageKV | decimal | YES | 18,4 | — |
| SecondaryVoltageKV | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| SF6Pressure | decimal | YES | 18,4 | — |
| CoolingFansStatus | bit | YES | — | — |
| WTIHV | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| OTI | decimal | YES | 18,4 | — |
| Shift | varchar | YES | 100 | — |
| BreatherStatusTransformer | bit | YES | — | — |
| BreatherStatusTapChanger | bit | YES | — | — |
| RatedSecondaryCurrent1102AY | decimal | YES | 18,4 | — |
| RatedPrimaryCurrentB276A | decimal | YES | 18,4 | — |
| OilLevelTransformer | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| RatedSecondaryCurrent1102AR | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AB | decimal | YES | 18,4 | — |
| WTILV | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ED4367F8-2B75-4C09-AA58-30664210398D | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T14:57:23.1170000 | 2025-08-02T10:24:27.0000000 | False | False | NULL |  |  |
| 29F737CB-0ABC-41B1-BFBA-34F87580556C | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-17T19:48:26.5270000 | 2025-08-17T19:48:26.0000000 | False | False | NULL | 172.16.6.195 |  |
| 1F403A8E-4E61-4AF8-ABD2-6D76F47F047F | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-10-15T22:22:54.7100000 | 2025-10-15T22:34:48.0000000 | False | False | NULL | 172.16.6.52 |  |
| A1A7EBC1-1698-465C-8C8C-D9ED2680421C | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-22T21:06:16.3500000 | 2025-10-22T21:06:16.0000000 | False | False | NULL |  |  |
| F0E7382F-FCF5-4D58-A86F-989316A63003 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T01:42:58.3370000 | 2025-10-24T01:42:58.0000000 | False | False | NULL |  |  |
| 68312E53-00D7-4270-8255-93B50FA15352 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:26:34.5870000 | 2025-10-24T04:26:34.0000000 | False | False | NULL |  |  |
| F2FE583B-65A9-4C26-8753-3E1D9E7D80BB | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-25T20:42:26.8470000 | 2025-10-25T20:42:26.0000000 | False | False | NULL |  |  |
| 50AF1D5F-38E6-4209-9CA1-433AD5F942EF | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T02:08:54.1100000 | 2025-10-27T02:08:54.0000000 | False | False | NULL |  |  |
| AD51F57D-BE21-4028-AB6E-B98F4EB94B23 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T02:00:19.7900000 | 2025-10-28T02:16:25.0000000 | False | False | NULL |  |  |
| 4A2AC4CD-FB57-4EDA-BE1D-A914AF848615 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T09:18:43.3800000 | 2025-10-28T09:18:43.0000000 | False | False | NULL |  |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6CE1FBFE-FE76-4708-8A5A-01F07DF8D010 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T00:55:19.7500000 | 2026-09-01T01:17:10.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 0D13A515-1E8D-47C2-BC5D-D1B9EB560D9C | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T00:59:12.4500000 | 2026-09-01T00:59:12.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 41730F5E-D942-43F7-B33C-38E3F32F5B2F | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-21T18:50:51.7930000 | 2026-08-31T07:28:12.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 8B9B45BF-6240-4852-A31C-0E1C2CA6AC86 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T23:22:27.0430000 | 2026-08-30T23:22:27.0000000 | False | False | NULL |  | NULL |
| 5CF93613-9A02-4A78-A431-8063EB38C193 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-20T23:43:05.0770000 | 2026-08-21T00:42:50.0000000 | False | False | NULL |  | NULL |
| A2C97BEC-10DD-4611-BD25-28862C168187 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T05:08:48.2400000 | 2026-08-20T05:08:48.0000000 | False | False | NULL |  | NULL |
| EE515554-0973-45D4-A64D-168F6BE19516 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T04:59:55.8230000 | 2026-08-20T04:59:55.0000000 | False | False | NULL |  | NULL |
| D2A2D8FE-C9D8-4B22-B380-4B146D95CBDA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-19T01:51:54.2000000 | 2026-08-19T01:58:55.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| C92AD034-1889-4CB7-98D5-C8893DFD3B2A | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-17T01:51:56.6870000 | 2026-08-17T01:51:56.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 2C71D075-0E54-4D69-8F73-AABE0E94CBAD | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-09T00:58:30.9170000 | 2026-07-09T00:58:30.0000000 | False | False | NULL |  | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_24MVA.Attendant` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
