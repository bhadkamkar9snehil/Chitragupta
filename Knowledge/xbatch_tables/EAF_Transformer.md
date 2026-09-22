# XStudio_Xbatch.dbo.EAF_Transformer

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference temperature, hvbushing, reactor, cooler, tap, changer, flexible, lvtube, oil, phase, sec, breather.

**Primary Key:** ID  
**Row Count:** 483  
**Date Range (ModifiedOn):** 2025-07-21T16:45:00.0000000 to 2026-08-19T02:24:39.0000000  

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
| TransformerCurver | int | YES | 10,0 | — |
| PowerMW | decimal | YES | 18,4 | — |
| TapChangerCounter | int | YES | 10,0 | — |
| VCBCounter | int | YES | 10,0 | — |
| OilTemperature | int | YES | 10,0 | — |
| MainTank | int | YES | 10,0 | — |
| TapChanger | int | YES | 10,0 | — |
| Phase1B7A | int | YES | 10,0 | — |
| Phase2B7B | int | YES | 10,0 | — |
| Phase3B7C | int | YES | 10,0 | — |
| HVBushingTemperature1U | decimal | YES | 18,4 | — |
| HVBushingTemperature1V | decimal | YES | 18,4 | — |
| HVBushingTemperature1W | decimal | YES | 18,4 | — |
| HVBushingReactorU1 | decimal | YES | 18,4 | — |
| HVBushingReactorU2 | decimal | YES | 18,4 | — |
| HVBushingReactorV1 | decimal | YES | 18,4 | — |
| HVBushingReactorV2 | decimal | YES | 18,4 | — |
| HVBushingReactorW1 | decimal | YES | 18,4 | — |
| HVBushingReactorW2 | decimal | YES | 18,4 | — |
| LVTubeTemperature2UE1 | decimal | YES | 18,4 | — |
| LVTubeTemperature2VE2 | decimal | YES | 18,4 | — |
| LVTubeTemperature2WE3 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2UE1 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2VE2 | decimal | YES | 18,4 | — |
| SecFlexibleTemperature2WE3 | decimal | YES | 18,4 | — |
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
| 36BF995D-4E13-47A7-9CE4-58DD2ED3D963 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T14:20:06.5230000 | 2025-07-21T16:45:00.0000000 | False | False | NULL |
| E9902482-FF02-4F1D-B13B-087D7F14343D | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-02T10:22:41.5370000 | 2025-08-02T10:22:41.0000000 | False | False | NULL |
| ECECCF2B-0A2A-4BD6-ABF5-934E1D3A6245 | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-16T23:26:50.5970000 | 2025-08-16T23:26:50.0000000 | False | False | NULL |
| 01BFFA7A-7D36-4291-9E87-AAB5EADF9429 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-10-15T22:12:45.8330000 | 2025-10-15T22:12:45.0000000 | False | False | NULL |
| 7AF70758-E221-414B-895E-C3C9D20835D4 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-10-15T21:44:54.9000000 | 2025-10-15T22:31:34.0000000 | False | False | NULL |
| 04E221C8-0406-404C-A3E4-3C559F0D5CA4 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-22T20:11:47.9900000 | 2025-10-22T20:11:47.0000000 | False | False | NULL |
| DFBE87C3-7DCD-491D-ABC6-D43AEF10EC04 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:13:00.3700000 | 2025-10-24T04:13:00.0000000 | False | False | NULL |
| EE3F88DA-E272-4180-8901-3CD7669929F9 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-25T22:50:26.2000000 | 2025-10-25T22:50:26.0000000 | False | False | NULL |
| 812AF24B-DC68-4BC1-8863-E60A7FC6E58C | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T01:31:34.1500000 | 2025-10-27T01:31:34.0000000 | False | False | NULL |
| 9001BB4F-32EA-4376-83C3-4D1CE0AEEC99 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T07:38:16.3470000 | 2025-10-27T07:38:16.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 655E79D9-FE9E-42B4-A45E-E5F08D4536CA | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-19T02:17:39.7330000 | 2026-08-19T02:24:39.0000000 | False | False | NULL |
| AE2B5816-BD55-49AF-9CFD-F0E1DE0764AA | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T23:31:01.4670000 | 2026-07-08T23:31:01.0000000 | False | False | NULL |
| 7872F487-3711-4399-A08E-904A6FBF3ECF | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T08:00:42.1370000 | 2026-07-08T08:00:42.0000000 | False | False | NULL |
| 643EA1FE-F8BB-455D-B7D0-1F91F4E9B267 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-07T19:31:25.5230000 | 2026-07-07T19:31:25.0000000 | False | False | NULL |
| 90FF5E25-D1F9-439B-B43E-56F8E8123E73 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-07T07:54:01.6600000 | 2026-07-07T07:54:01.0000000 | False | False | NULL |
| 82F292C2-0C4E-4939-B189-BBDBBDD2E5F9 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T19:36:49.6630000 | 2026-07-06T19:36:49.0000000 | False | False | NULL |
| 85EA219D-45E2-4FE7-886E-7B38CC8E7945 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T07:48:55.2400000 | 2026-07-06T07:48:55.0000000 | False | False | NULL |
| 72E04A1E-46AA-40CF-B471-4BAB918FA461 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-05T19:39:49.6130000 | 2026-07-05T19:39:49.0000000 | False | False | NULL |
| E111C854-F332-4FBB-A48F-58D311E1864A | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-05T08:06:51.2600000 | 2026-07-05T08:06:51.0000000 | False | False | NULL |
| EC54FA82-39CA-4A2F-BD43-B9003CF79DD0 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-04T20:12:06.4900000 | 2026-07-04T20:22:23.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_Transformer.Attendant` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
