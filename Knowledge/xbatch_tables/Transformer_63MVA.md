# XStudio_Xbatch.dbo.Transformer_63MVA

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference current, rated, primary, secondary, changer, status, tap, breather, level, oil, transformer, voltage.

**Primary Key:** ID  
**Row Count:** 466  
**Date Range (ModifiedOn):** 2025-08-04T10:36:16.0000000 to 2026-09-01T01:09:27.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| PrimaryVoltageKV | decimal | YES | 18,4 | — |
| SecondaryVoltageKV | decimal | YES | 18,4 | — |
| RatedPrimaryCurrentR276A | decimal | YES | 18,4 | — |
| RatedPrimaryCurrent276AY | decimal | YES | 18,4 | — |
| RatedPrimaryCurrentB276A | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AR | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AY | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AB | decimal | YES | 18,4 | — |
| TapChangerCounter | decimal | YES | 18,4 | — |
| OTI | decimal | YES | 18,4 | — |
| WTIHV | decimal | YES | 18,4 | — |
| SF6Pressure | decimal | YES | 18,4 | — |
| OilLevelTransformer | decimal | YES | 18,4 | — |
| OilLevelTapChanger | decimal | YES | 18,4 | — |
| BreatherStatusTransformer | bit | YES | — | — |
| BreatherStatusTapChanger | bit | YES | — | — |
| CoolingFansStatus | bit | YES | — | — |
| Remarks | varchar | YES | -1 | — |
| Attendant | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |
| WTILV | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16E5BD30-58A4-4071-8EA4-2A554B9CB36B | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-20T10:26:57.7530000 | 2025-08-04T10:36:16.0000000 | False | False | NULL |
| 3C3C674D-9996-4325-AFBC-5FD0642D219B | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-17T19:45:13.6300000 | 2025-08-17T19:45:13.0000000 | False | False | NULL |
| 6CE97E7B-07EA-45BB-AEDD-B511341EBC00 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-10-15T22:13:56.1630000 | 2025-10-15T22:13:56.0000000 | False | False | NULL |
| 89E52ED2-DCE6-448D-908B-516DFB00A195 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-10-15T22:11:40.8330000 | 2025-10-15T22:33:34.0000000 | False | False | NULL |
| B43CFE50-FBED-43F9-AE9C-E3774C48D9C7 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-22T21:01:42.2770000 | 2025-10-22T21:01:42.0000000 | False | False | NULL |
| 57993B34-871D-4E82-9FC6-00E0C87C3609 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T01:38:42.3500000 | 2025-10-24T01:38:42.0000000 | False | False | NULL |
| BC056ED5-D33E-4613-9664-33481313FB80 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:22:59.1800000 | 2025-10-24T04:22:59.0000000 | False | False | NULL |
| 8CF580B9-0C95-4B11-86D5-4E9995277702 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-25T20:35:05.9930000 | 2025-10-25T20:35:05.0000000 | False | False | NULL |
| 3FB5EBFB-AAB1-4BE3-89FF-C96CFF1342F6 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T01:48:17.6430000 | 2025-10-28T01:48:17.0000000 | False | False | NULL |
| 3B0C778B-EE99-45F5-ACBE-0F44DA7CD8C5 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T01:49:43.1200000 | 2025-10-28T02:17:30.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4BA3007C-58CD-4784-B4A7-0EC66D7BCC54 | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T00:53:42.1100000 | 2026-09-01T01:09:27.0000000 | False | False | NULL |
| D5DCDC05-38A2-409D-847A-AA69A7869785 | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T00:53:04.3330000 | 2026-09-01T01:01:37.0000000 | False | False | NULL |
| F8A8C00E-3017-4F37-B5A5-FDD46CE61A6D | NULL | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-21T18:46:43.4530000 | 2026-08-31T07:29:52.0000000 | False | False | NULL |
| 27C8DDFA-1587-4CA5-AB91-FBE74789848A | NULL | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T23:20:05.6800000 | 2026-08-30T23:20:05.0000000 | False | False | NULL |
| 8218FC0E-1141-45DD-AC15-56A9DD09FFEA | NULL | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-20T23:42:20.6700000 | 2026-08-21T00:40:27.0000000 | False | False | NULL |
| 05F266C2-1851-40EE-9F8C-2181AFF3DA5C | NULL | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T05:06:11.7300000 | 2026-08-20T05:06:11.0000000 | False | False | NULL |
| 98D63F6B-B9D9-44EA-9006-DDDD90917D93 | NULL | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T04:57:20.1230000 | 2026-08-20T04:57:20.0000000 | False | False | NULL |
| 1799B94F-BB9E-4051-8D4A-E3299F080C74 | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-19T01:49:43.0070000 | 2026-08-19T22:38:52.0000000 | False | False | NULL |
| 26082DD5-1811-4E60-9DE7-6E23507FA1DB | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-17T01:47:26.3000000 | 2026-08-17T01:48:05.0000000 | False | False | NULL |
| 341A2083-C9E4-4918-AEE0-123D61DA0883 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-09T00:56:02.8900000 | 2026-07-09T00:56:02.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_63MVA.Attendant` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
