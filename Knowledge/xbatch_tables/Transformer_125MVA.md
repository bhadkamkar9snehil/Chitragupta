# XStudio_Xbatch.dbo.Transformer_125MVA

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference current, rated, primary, secondary, changer, status, tap, breather, level, oil, transformer, voltage.

**Primary Key:** ID  
**Row Count:** 463  
**Date Range (ModifiedOn):** 2025-08-02T10:24:18.0000000 to 2026-09-01T01:15:18.0000000  

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
| FBB27A0B-CC47-4AC5-B931-1FEDC340757D | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T14:55:43.8930000 | 2025-08-02T10:24:18.0000000 | False | False | NULL |  |  |
| 71C98F27-17F4-483B-A8AA-FF8E3BDA88D0 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-17T19:46:40.0830000 | 2025-08-17T19:46:40.0000000 | False | False | NULL | 172.16.6.195 |  |
| 320BA1EF-59D7-45FF-94B8-FCA0F3A6D274 | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-10-15T22:18:46.7270000 | 2025-10-15T22:34:08.0000000 | False | False | NULL | 172.16.6.52 |  |
| 762F71BA-68CB-4A53-A7FD-699834C372A5 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-22T21:04:17.0300000 | 2025-10-22T21:04:17.0000000 | False | False | NULL |  |  |
| 61DC2FB8-0451-492B-9C2B-59A38F5A3FEA | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T01:41:08.9900000 | 2025-10-24T01:41:08.0000000 | False | False | NULL |  |  |
| 275E3C81-4AEF-48BE-8EF4-CAB16C343B45 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:24:49.4730000 | 2025-10-24T04:24:49.0000000 | False | False | NULL |  |  |
| DCE1AA32-59E8-45EE-881A-64944957FF4A | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-25T20:37:18.3870000 | 2025-10-25T20:37:18.0000000 | False | False | NULL |  |  |
| D14057D5-EC21-4DB7-8A27-16389EDD3929 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T01:53:31.9800000 | 2025-10-27T01:53:31.0000000 | False | False | NULL |  |  |
| 151BE6F5-BB55-4DDE-BF29-22AA664CB0B1 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T01:57:20.6730000 | 2025-10-28T02:17:09.0000000 | False | False | NULL |  |  |
| 8E2EC174-B8E4-4087-9E41-C49D7D5CDD8A | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T09:16:09.3570000 | 2025-10-28T09:16:09.0000000 | False | False | NULL |  |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2784D817-5B25-4ABC-8929-CF08918A2031 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T00:54:46.5830000 | 2026-09-01T01:15:18.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| F001E270-A3DB-437F-A359-6DEA34E2AD75 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T00:57:54.3200000 | 2026-09-01T00:57:54.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 3518709E-61A0-4A41-A379-D7BA57E4C18D | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-21T18:48:50.2230000 | 2026-08-31T07:28:37.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 7F306825-FFCA-4B94-95F5-28D8120A8569 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T23:21:14.8770000 | 2026-08-30T23:21:14.0000000 | False | False | NULL |  | NULL |
| 49A21802-84FD-4CFD-B8A2-5A041425411C | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-20T23:42:37.1530000 | 2026-08-21T00:41:25.0000000 | False | False | NULL |  | NULL |
| 8EA47404-1A4A-4403-8CFF-880D26A31D35 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T05:07:37.0100000 | 2026-08-20T05:07:37.0000000 | False | False | NULL |  | NULL |
| 70305711-D5A9-4D96-A128-7A2691811D55 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T04:58:31.9800000 | 2026-08-20T04:58:31.0000000 | False | False | NULL |  | NULL |
| 6F4180B4-8741-47BC-9D13-72CDB06C7843 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-19T01:50:52.4000000 | 2026-08-19T22:39:20.0000000 | False | False | NULL |  | NULL |
| 136B6DB5-856F-4DC3-8CC3-C497F6AA0A3B | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-17T01:49:52.4370000 | 2026-08-17T01:49:52.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| B38FAB09-33A3-487E-A8AC-9B01FF2324B6 | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-09T00:57:12.3200000 | 2026-07-09T00:57:35.0000000 | False | False | NULL |  | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_125MVA.Attendant` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
