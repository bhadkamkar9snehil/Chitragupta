# XStudio_Xbatch.dbo.Transformer_15MVA

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference current, rated, primary, secondary, changer, status, tap, breather, level, oil, transformer, voltage.

**Primary Key:** ID  
**Row Count:** 460  
**Date Range (ModifiedOn):** 2025-08-02T10:24:48.0000000 to 2026-09-01T01:17:53.0000000  

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
| RatedPrimaryCurrent263AY | decimal | YES | 18,4 | — |
| Attendant | varchar | YES | 36 | — |
| RatedPrimaryCurrentR263A | decimal | YES | 18,4 | — |
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
| RatedPrimaryCurrentB263A | decimal | YES | 18,4 | — |
| OilLevelTransformer | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| RatedSecondaryCurrent1102AR | decimal | YES | 18,4 | — |
| RatedSecondaryCurrent1102AB | decimal | YES | 18,4 | — |
| WTILV | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8A84EF66-FB9B-472A-AF55-6CCBBF10F071 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T15:04:02.3900000 | 2025-08-02T10:24:48.0000000 | False | False | NULL |  |  |
| 56AC58E5-94D7-417A-9A75-CE69D2BBF9DF | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-10-15T22:25:21.6200000 | 2025-10-15T22:35:13.0000000 | False | False | NULL | 172.16.6.52 |  |
| 1D739D5D-D744-4DEF-AFF4-518E9DDADCA6 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-22T21:08:43.4370000 | 2025-10-22T21:08:43.0000000 | False | False | NULL |  |  |
| 6BC185DD-C27E-46FE-BAB1-AED7FBBE68A0 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T01:45:02.7530000 | 2025-10-24T01:45:02.0000000 | False | False | NULL |  |  |
| 8ED52012-3733-4D64-814A-45B52E7F6FEB | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:27:51.6370000 | 2025-10-24T04:27:51.0000000 | False | False | NULL |  |  |
| 7ADF8DA2-EEF1-4188-BBA1-2D4D6B0C5ED3 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-25T20:44:28.8930000 | 2025-10-25T20:44:28.0000000 | False | False | NULL |  |  |
| C77FD96B-B0E7-4EAB-83B2-6F7B96572EC6 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T02:10:27.5230000 | 2025-10-27T02:10:27.0000000 | False | False | NULL |  |  |
| 2C03D084-E6AB-464D-9C41-0BC5ABFBD459 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T02:03:06.8430000 | 2025-10-28T02:15:04.0000000 | False | False | NULL |  |  |
| B5F2F1CF-B2F5-4D47-AEDE-3891FE4D89D3 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T09:20:25.6300000 | 2025-10-28T09:20:25.0000000 | False | False | NULL |  |  |
| 15D072AB-2D00-4AEF-BE23-E4A5B0F357D0 | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T21:13:14.0130000 | 2025-10-28T21:13:14.0000000 | False | False | NULL |  |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5170E07A-ED04-4A26-AA68-CBFCCCD4BD2D | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T00:55:39.0200000 | 2026-09-01T01:17:53.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 249AFA13-F402-4F57-9C56-20B334EA6749 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-30T23:23:45.7870000 | 2026-09-01T01:00:38.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 34230E2E-C0A2-43EF-8EF2-5A4974DB4F86 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T01:00:03.2470000 | 2026-09-01T01:00:03.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 6D9731B3-CD43-47A1-AC77-D5714CB2E5FA | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-21T18:52:19.4070000 | 2026-08-31T07:28:53.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| F39BABA1-39BB-44FA-A95D-21A3D5D28AB9 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-20T23:43:23.8200000 | 2026-08-21T18:51:27.0000000 | False | False | NULL |  | NULL |
| FF94AFAC-D0EE-4091-B5EA-5CDCCFA582A5 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T05:09:43.3330000 | 2026-08-20T05:09:43.0000000 | False | False | NULL |  | NULL |
| 441243A1-9143-43DA-9C08-7BBE63CDBD3C | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T05:00:58.0570000 | 2026-08-20T05:00:58.0000000 | False | False | NULL |  | NULL |
| 5B074600-0D4F-413E-868E-19457B90F507 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-19T01:57:17.2830000 | 2026-08-19T01:57:17.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| FB166B40-4FEF-4A8F-B88E-DA68DF9B4BFF | C2500F49-167C-4DAA-A825-049801878F93 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-07-08T13:42:48.7900000 | 2026-08-17T19:59:42.0000000 | False | False | NULL |  | NULL |
| DA0492B3-A90E-49AC-9F51-5E653704F5DE | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-17T01:52:48.3070000 | 2026-08-17T01:53:22.0000000 | False | False | NULL | 10.76.5.34 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_15MVA.Attendant` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
