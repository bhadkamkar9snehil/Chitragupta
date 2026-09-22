# XStudio_Xbatch.dbo.Transformer_LRF

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference temperature, oil, cooler, flexible, flow, hvbushing, lvtube, sec, tap, breather, changer, running.

**Primary Key:** ID  
**Row Count:** 474  
**Date Range (ModifiedOn):** 2025-08-02T10:23:34.0000000 to 2026-08-19T02:26:03.0000000  

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
| HeatNo | int | YES | 10,0 | — |
| TapNo | int | YES | 10,0 | — |
| PowerMW | decimal | YES | 18,4 | — |
| TapChangerCounter | int | YES | 10,0 | — |
| OilTemperatureDegC | int | YES | 10,0 | — |
| OilLevelPercentage | int | YES | 10,0 | — |
| HVBushingTemperature1U | decimal | YES | 18,4 | — |
| HVBushingTemperature1V | decimal | YES | 18,4 | — |
| HVBushingTemperature1W | decimal | YES | 18,4 | — |
| LVTubeTemperature2UE1 | decimal | YES | 18,4 | — |
| LVTubeTemperature2VE2 | decimal | YES | 18,4 | — |
| LVTubeTemperature2WE3 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2UE1 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2VE2 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2WE3 | decimal | YES | 18,4 | — |
| OilFlowRunningCooler1 | decimal | YES | 18,4 | — |
| OilFlowRunningCooler2 | decimal | YES | 18,4 | — |
| WaterFlowM3PerHrCooler1 | decimal | YES | 18,4 | — |
| BreatherStatusTransformer | bit | YES | — | — |
| BreatherStatusTapChanger | bit | YES | — | — |
| Remarks | varchar | YES | 100 | — |
| Attendant | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |
| WindingTemperature | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B5E165CA-43A6-402E-87DC-66EAC7EEA89B | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T15:26:55.6670000 | 2025-08-02T10:23:34.0000000 | False | False | NULL |
| 4A9534B8-9183-4584-846A-42C59D505F9A | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-16T23:31:46.2570000 | 2025-08-16T23:31:46.0000000 | False | False | NULL |
| E8E25713-570E-43DB-882F-24D279EA612B | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-10-15T21:51:00.8630000 | 2025-10-15T22:32:36.0000000 | False | False | NULL |
| 6BFE6602-0265-4DE0-890D-C9CFFCB1DB17 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-22T20:23:10.6400000 | 2025-10-22T20:23:10.0000000 | False | False | NULL |
| 10A7D806-A9A6-4124-A18E-EC9E0983C54F | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:19:54.2930000 | 2025-10-24T04:19:54.0000000 | False | False | NULL |
| 53566F8B-15E2-4E44-89D8-FECD1F952282 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-25T22:59:24.1200000 | 2025-10-25T22:59:24.0000000 | False | False | NULL |
| 46981A6D-1960-4B40-8428-C2600E6E6445 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T01:38:33.7700000 | 2025-10-27T01:38:33.0000000 | False | False | NULL |
| 305C9C5D-8C75-404E-9A50-2588A1FDC09C | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T07:44:25.7670000 | 2025-10-27T07:44:25.0000000 | False | False | NULL |
| 48A1E4B3-5634-4693-AE4E-03925BB8C7D5 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T09:12:02.9530000 | 2025-10-28T09:12:02.0000000 | False | False | NULL |
| 7B82B1EA-702D-483E-BD0A-9F29185030CA | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T20:57:47.1400000 | 2025-10-28T20:57:47.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BDD3988C-1AF8-45B7-B2E8-D39626794B21 | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-19T02:26:03.2800000 | 2026-08-19T02:26:03.0000000 | False | False | NULL |
| AB712694-6BD0-4434-8C9A-5D3ADB716DA2 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T23:33:53.6930000 | 2026-07-08T23:33:53.0000000 | False | False | NULL |
| AD1D1ABB-114A-4D9D-B98E-4A4B857B94C5 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T08:08:14.0870000 | 2026-07-08T08:08:14.0000000 | False | False | NULL |
| 33983BE2-EF47-4773-B9D3-A3958A30C4B5 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-07T19:34:17.9830000 | 2026-07-07T19:34:17.0000000 | False | False | NULL |
| 44E1A70F-3CC2-40B9-8150-831F51D0672D | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-07T09:05:39.8070000 | 2026-07-07T09:05:39.0000000 | False | False | NULL |
| F213D085-2EA6-45A7-9DC0-4586EB2D3121 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T19:42:13.1030000 | 2026-07-06T19:42:13.0000000 | False | False | NULL |
| 2A0A7A2D-EF34-432B-89AF-FD6D8668A8B4 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T07:51:35.6470000 | 2026-07-06T07:51:35.0000000 | False | False | NULL |
| C5C549DF-01EE-4558-AC0C-E1F6281BA0D7 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-05T19:42:16.3000000 | 2026-07-05T19:42:16.0000000 | False | False | NULL |
| 34746DC9-516A-47DD-996E-13DDE30C4031 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-05T08:10:49.4170000 | 2026-07-05T08:10:49.0000000 | False | False | NULL |
| A922DB03-75A5-45D8-AFB0-D8E51526D4DA | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-04T20:15:51.0470000 | 2026-07-04T20:23:28.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_LRF.Attendant` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
