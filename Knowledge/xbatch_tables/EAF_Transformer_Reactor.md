# XStudio_Xbatch.dbo.EAF_Transformer_Reactor

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference temperature, hvbushing, oil, cooler, tap, changer, divertor, phase, tank, breather, flow, flowm.

**Primary Key:** ID  
**Row Count:** 477  
**Date Range (ModifiedOn):** 2025-07-21T15:19:32.0000000 to 2026-08-19T02:25:31.0000000  

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
| HeatNo | varchar | YES | 100 | — |
| TapNo | int | YES | 10,0 | — |
| TapChangerCounter | int | YES | 10,0 | — |
| OilTremperature | int | YES | 10,0 | — |
| OilLevelReactor | int | YES | 10,0 | — |
| OilLevelTapChanger | int | YES | 10,0 | — |
| DivertorTankTemperaturePhase1B7A | int | YES | 10,0 | — |
| DivertorTankTemperaturePhase2B7B | int | YES | 10,0 | — |
| DivertorTankTemperaturePhase3B7C | int | YES | 10,0 | — |
| HVBushingTemperatureU1 | decimal | YES | 18,4 | — |
| HVBushingTemperatureU2 | decimal | YES | 18,4 | — |
| HVBushingTemperatureV1 | decimal | YES | 18,4 | — |
| HVBushingTemperatureV2 | decimal | YES | 18,4 | — |
| HVBushingTemperatureW1 | decimal | YES | 18,4 | — |
| HVBushingTemperatureW2 | decimal | YES | 18,4 | — |
| OilFlowRunningCooler1 | decimal | YES | 18,4 | — |
| OilFlowRunningCooler2 | decimal | YES | 18,4 | — |
| WaterFlowm3perhrCooler1 | decimal | YES | 18,4 | — |
| WaterFlowm3perhrCooler2 | decimal | YES | 18,4 | — |
| BreatherStatusTransformer | bit | YES | — | — |
| BreatherStatusTapChanger | bit | YES | — | — |
| Remarks | varchar | YES | 100 | — |
| Attendant | varchar | YES | 36 | — |
| Shift | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A63E2632-CB3F-4214-902D-6C34886A8A99 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T14:52:38.1270000 | 2025-07-21T15:19:32.0000000 | False | False | NULL |
| BB8B547D-C464-4535-AA12-7235A39E7CBB | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T15:11:41.8170000 | 2025-08-02T10:23:12.0000000 | False | False | NULL |
| EBC883B6-32C6-43B3-985C-B779F439BAC6 | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-16T23:29:12.5800000 | 2025-08-16T23:29:12.0000000 | False | False | NULL |
| 263D6FC8-6F0B-46DB-B88F-C8E812C33C69 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-10-15T21:47:22.8470000 | 2025-10-15T22:32:07.0000000 | False | False | NULL |
| 83216056-3C06-4999-9E78-E3BB952FD8B8 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-22T20:18:14.4830000 | 2025-10-22T20:18:14.0000000 | False | False | NULL |
| 29350E61-7979-4F1C-87DB-2A7E976C7E37 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:16:06.0630000 | 2025-10-24T04:16:06.0000000 | False | False | NULL |
| F39D30A1-A826-412D-A615-C8B0FAE040F5 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-25T22:54:28.3900000 | 2025-10-25T22:54:28.0000000 | False | False | NULL |
| 8A556322-C0DE-4F14-ABCC-5FD33FA349D3 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T01:34:59.0100000 | 2025-10-27T01:34:59.0000000 | False | False | NULL |
| B3B487D2-8401-48DD-8C14-E3A5C13DA497 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T07:41:27.7970000 | 2025-10-27T07:41:27.0000000 | False | False | NULL |
| 67C77919-C428-4014-8E8F-FCE1AAD62FC5 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T21:40:29.6400000 | 2025-10-27T21:40:29.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 97DB1F74-4F66-4869-9D8A-2384E92A54DE | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-19T02:25:31.6800000 | 2026-08-19T02:25:31.0000000 | False | False | NULL |
| D4B9FC9A-5D31-4FFE-A9AF-AE443237ED2A | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T23:32:31.9400000 | 2026-07-08T23:32:31.0000000 | False | False | NULL |
| EC0B310F-A68B-4F5A-942B-5582B5B5AAC9 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T08:02:01.4970000 | 2026-07-08T08:02:01.0000000 | False | False | NULL |
| 60E06AB4-2786-4EB3-AC5C-EA16D1C9F60E | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-07T19:32:31.8300000 | 2026-07-07T19:32:31.0000000 | False | False | NULL |
| 9F5DAE26-45BC-4CC2-A63B-525FCED54267 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-07T09:03:50.9500000 | 2026-07-07T09:03:50.0000000 | False | False | NULL |
| BE64A69D-65B0-4AC1-9518-3EEF1DCEB737 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T19:40:41.7730000 | 2026-07-06T19:40:41.0000000 | False | False | NULL |
| 9C76AF6C-3EA0-4AB0-86E7-E2D086FC6AF0 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T07:50:13.6500000 | 2026-07-06T07:50:13.0000000 | False | False | NULL |
| D1C7A7C7-5AAF-4105-AF97-681307CA4EBF | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-05T19:41:02.5200000 | 2026-07-05T19:41:02.0000000 | False | False | NULL |
| 1C0B9FFF-1DF5-4235-8D41-8B0E7315AAB5 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-05T08:08:47.6400000 | 2026-07-05T08:08:47.0000000 | False | False | NULL |
| 72A5B416-15EA-4B34-8EC9-1792ED78B9DF | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-04T20:13:28.2430000 | 2026-07-04T20:23:07.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_Transformer_Reactor.Attendant` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
