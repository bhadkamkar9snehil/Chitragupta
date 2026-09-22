# XStudio_Xbatch.dbo.Control_and_Relay_Panels

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference relay, protection, charged, mva, diff, breaker, current, earth, efprot, fault, ocand, phase.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-10T09:04:53.0000000 to 2026-09-02T07:54:40.0000000  

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
| EntryDateTime | datetime | YES | — | — |
| CableDiffRelayArevaP541IC1 | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| BreakerSpriningCharged15MVA | varchar | YES | 100 | — |
| CableDiffRelayArevaP541IC2 | varchar | YES | 100 | — |
| BreakerSpriningChargedSVCFB | varchar | YES | 100 | — |
| CurrentDiffProtectionRelayLRF | varchar | YES | 100 | — |
| Phase3OCandEFProtRelay33kvIC1 | varchar | YES | 100 | — |
| SelectorSwitchChargedBC | varchar | YES | 36 | — |
| TXDiffProtectionRelay24MVA | varchar | YES | 100 | — |
| TXDiffProtectionRelay33kvIC1 | varchar | YES | 100 | — |
| EngineerName | varchar | YES | 36 | — |
| TXDiffProtectionRelay33kvIC2 | varchar | YES | 100 | — |
| SelectorSwitchCharged15MVA | varchar | YES | 36 | — |
| REFProtectionRelaySVCTCR | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| REFProtectionRelay33kvIC1 | varchar | YES | 100 | — |
| REFProtectionRelay24MVA | varchar | YES | 100 | — |
| Phase3OCandEFProtRelaySVCFB | varchar | YES | 100 | — |
| Phase3OCandEFProtRelayLRF | varchar | YES | 100 | — |
| REFProtectionRelaySVCFB | varchar | YES | 100 | — |
| TXDiffProtectionRelayBC | varchar | YES | 100 | — |
| BreakerSpriningChargedEAF | varchar | YES | 100 | — |
| Phase3OCandEFProtRelaySVCTCR | varchar | YES | 100 | — |
| CableDiffRelaySiemensIC1 | varchar | YES | 100 | — |
| REFProtectionRelayEAF | varchar | YES | 100 | — |
| Phase3OCandEFProtRelay15MVA | varchar | YES | 100 | — |
| SelectorSwitchCharged24MVA | varchar | YES | 36 | — |
| StandbyEarthFaultProtectionRelaySVCTCR | varchar | YES | 100 | — |
| BreakerSpriningChargedSVCTCR | varchar | YES | 100 | — |
| StandbyEarthFaultProtectionRelayIC2 | varchar | YES | 100 | — |
| CurrentDiffProtectionRelayBC | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| REFProtectionRelay33kvIC2 | varchar | YES | 100 | — |
| StandbyEarthFaultProtectionRelayBC | varchar | YES | 100 | — |
| SelectorSwitchCharged33kvIC2 | varchar | YES | 36 | — |
| Phase3OCandEFProtRelay33kvIC2 | varchar | YES | 100 | — |
| REFProtectionRelayBC | varchar | YES | 100 | — |
| StandbyEarthFaultProtectionRelay24MVA | varchar | YES | 100 | — |
| REFProtectionRelayLRF | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| Phase3OCandEFProtRelayBC | varchar | YES | 100 | — |
| CurrentDiffProtectionRelayIC2 | varchar | YES | 100 | — |
| Phase3OCandEFProtRelayIC1 | varchar | YES | 100 | — |
| SelectorSwitchCharged33kvIC1 | varchar | YES | 36 | — |
| TXDiffProtectionRelayEAF | varchar | YES | 100 | — |
| TXDiffProtectionRelaySVCTCR | varchar | YES | 100 | — |
| TXDiffProtectionRelaySVCFB | varchar | YES | 100 | — |
| CurrentDiffProtectionRelay33kvIC1 | varchar | YES | 100 | — |
| SelectorSwitchIC2 | varchar | YES | 36 | — |
| StandbyEarthFaultProtectionRelayLRF | varchar | YES | 100 | — |
| StandbyEarthFaultProtectionRelay33kvIC2 | varchar | YES | 100 | — |
| CurrentDiffProtectionRelay33kvIC2 | varchar | YES | 100 | — |
| TXDiffProtectionRelayIC1 | varchar | YES | 100 | — |
| BreakerSpriningCharged33kvIC2 | varchar | YES | 100 | — |
| BreakerSpriningChargedIC1 | varchar | YES | 100 | — |
| TXDiffProtectionRelayIC2 | varchar | YES | 100 | — |
| CurrentDiffProtectionRelayIC1 | varchar | YES | 100 | — |
| StandbyEarthFaultProtectionRelay15MVA | varchar | YES | 100 | — |
| BreakerSpriningCharged33kvIC1 | varchar | YES | 100 | — |
| CurrentDiffProtectionRelayEAF | varchar | YES | 100 | — |
| BreakerSpriningChargedLRF | varchar | YES | 100 | — |
| CurrentDiffProtectionRelaySVCTCR | varchar | YES | 100 | — |
| TechnicianName | varchar | YES | 36 | — |
| StandbyEarthFaultProtectionRelayIC1 | varchar | YES | 100 | — |
| CableDiffRelaySiemensIC2 | varchar | YES | 100 | — |
| CurrentDiffProtectionRelay24MVA | varchar | YES | 100 | — |
| BreakerSpriningChargedIC2 | varchar | YES | 100 | — |
| CurrentDiffProtectionRelaySVCFB | varchar | YES | 100 | — |
| StandbyEarthFaultProtectionRelayEAF | varchar | YES | 100 | — |
| TXDiffProtectionRelayLRF | varchar | YES | 100 | — |
| Phase3OCandEFProtRelayIC2 | varchar | YES | 100 | — |
| SelectorSwitchChargedSVCFB | varchar | YES | 36 | — |
| SelectorSwitchChargedLRF | varchar | YES | 36 | — |
| StandbyEarthFaultProtectionRelaySVCFB | varchar | YES | 100 | — |
| TXDiffProtectionRelay15MVA | varchar | YES | 100 | — |
| SelectorSwitchIC1 | varchar | YES | 36 | — |
| CurrentDiffProtectionRelay15MVA | varchar | YES | 100 | — |
| Phase3OCandEFProtRelay24MVA | varchar | YES | 100 | — |
| BreakerSpriningChargedBC | varchar | YES | 100 | — |
| BreakerSpriningCharged24MVA | varchar | YES | 100 | — |
| REFProtectionRelay15MVA | varchar | YES | 100 | — |
| SelectorSwitchChargedEAF | varchar | YES | 36 | — |
| Phase3OCandEFProtRelayEAF | varchar | YES | 100 | — |
| UnderFrequencyRelayIC2125MVA | varchar | YES | 100 | — |
| SelectorSwitchChargedSVCTCR | varchar | YES | 36 | — |
| UnderFrequencyRelayIC163MVA | varchar | YES | 100 | — |
| REFProtectionRelayIC1 | varchar | YES | 100 | — |
| StandbyEarthFaultProtectionRelay33kvIC1 | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| REFProtectionRelayIC2 | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 002A70C7-B898-436C-94B1-CA9BF278807A | NULL | NULL | 2026-07-23T00:20:25.6400000 | NULL | False | False | NULL | NULL | NULL |
| 05AB2F89-42C1-4D22-AC39-BB75FAF3CA62 | NULL | NULL | 2026-08-11T00:30:12.4100000 | NULL | False | False | NULL | NULL | NULL |
| 0A74A371-BB88-44FA-BC16-C4DE5F717E23 | NULL | NULL | 2026-07-24T00:00:32.6800000 | NULL | False | False | NULL | NULL | NULL |
| 0C91C269-E39C-479C-82C0-A2A8583749B6 | NULL | NULL | 2026-04-30T08:06:41.9300000 | NULL | False | False | NULL | NULL | NULL |
| 0C96B2D5-C0B0-4291-8FFF-4C403DAE9C0C | NULL | NULL | 2026-08-06T23:59:46.5070000 | NULL | False | False | NULL | NULL | NULL |
| 0E6E6ED6-A378-4614-9BC2-71000BE39324 | NULL | NULL | 2026-08-14T00:44:39.3330000 | NULL | False | False | NULL | NULL | NULL |
| 112464A9-3F32-4F51-A340-643ECC441EAE | NULL | NULL | 2026-08-01T00:48:30.9730000 | NULL | False | False | NULL | NULL | NULL |
| 22AC256F-2C55-49ED-8D75-A56C293F96DC | NULL | NULL | 2026-07-11T00:10:56.6430000 | NULL | False | False | NULL | NULL | NULL |
| 241A67C0-3B9F-42BD-8ABA-B42D3E66E6D3 | NULL | NULL | 2026-02-13T10:33:43.0470000 | NULL | False | False | NULL | NULL | NULL |
| 32B82435-E9F5-4869-9A54-9081FD9A8D76 | NULL | NULL | 2026-08-05T18:40:50.4530000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 748973FA-466C-442E-BC36-C1D97DD9D87A | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:43.0200000 | 2026-09-02T07:54:40.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 893933E6-6827-4F00-8D44-AD45914BEE5F | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7630000 | 2026-09-02T00:34:40.0000000 | False | False | NULL |  | NULL |
| 8DCF7268-1486-431F-AA2D-1D9D993ED613 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.1930000 | 2026-09-01T08:02:50.0000000 | False | False | NULL |  | NULL |
| 34F2AEBD-7B0A-42F5-B595-8AAD501741C1 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.2030000 | 2026-08-31T23:35:12.0000000 | False | False | NULL |  | NULL |
| 062280B2-9C7D-43E2-BA0C-CCE1D58E5DDA | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.1130000 | 2026-08-30T23:01:46.0000000 | False | False | NULL |  | NULL |
| AB743825-425C-4BCF-838F-89A823DA3BD2 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.5400000 | 2026-08-30T01:26:14.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 8DED3AAA-400D-4852-A12B-361455AC864C | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T00:48:38.0870000 | 2026-08-29T00:57:24.0000000 | False | False | NULL |  | NULL |
| 822ED211-0128-4C01-B21D-6FBFD02BBE90 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.7800000 | 2026-08-27T23:30:53.0000000 | False | False | NULL |  | NULL |
| 7FA37ED6-4C22-489D-99CB-1FFB2D22DF70 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0530000 | 2026-08-26T20:20:18.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| AB0E4A4E-5376-4002-BEFB-05B5C2B9233A | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.2470000 | 2026-08-25T20:05:42.0000000 | False | False | NULL | 10.76.5.60 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Control_and_Relay_Panels.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Control_and_Relay_Panels.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
