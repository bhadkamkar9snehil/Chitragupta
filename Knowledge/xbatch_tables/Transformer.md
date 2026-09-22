# XStudio_Xbatch.dbo.Transformer

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference mva, transformer, channel, hot, spot, temp, level, oil, wti, mvaoil, mvaoti, mvawti.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-13T10:55:32.0000000 to 2026-09-02T08:10:36.0000000  

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
| Transformer43MVAOTI | int | YES | 10,0 | — |
| TransformerOTI63MVA | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| Transformer31MVAWTI | int | YES | 10,0 | — |
| Transformer31MVAOilLevel | int | YES | 10,0 | — |
| Tranboosterfan12MVAOilLevel | decimal | YES | 18,4 | — |
| Transformer4a3MVAWTI | decimal | YES | 18,4 | — |
| Transformer23MVAWTI | int | YES | 10,0 | — |
| Transformer23MVAOTI | int | YES | 10,0 | — |
| Transformer43MVAWTI | int | YES | 10,0 | — |
| EntryDateTime | datetime | YES | — | — |
| Transformer4a3MVAOTI | int | YES | 10,0 | — |
| TransformerOilLevel125MVA | int | YES | 10,0 | — |
| Transformer4a3MVAOilLevel | decimal | YES | 18,4 | — |
| Transformer516MVAOilLevel | int | YES | 10,0 | — |
| IsProcessed | bit | YES | — | — |
| TransformerOilLevel63MVA | int | YES | 10,0 | — |
| Transformer3a3MVAOilLevel | int | YES | 10,0 | — |
| Transformer516MVAWTI | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |
| Tranboosterfan12MVAOTI | int | YES | 10,0 | — |
| Transformer13MVAOilLevel | int | YES | 10,0 | — |
| TechnicianName | varchar | YES | 36 | — |
| Tranboosterfan12MVAWTI | decimal | YES | 18,4 | — |
| Transformer3a3MVAWTI | int | YES | 10,0 | — |
| Transformer2a4MVAOTI | int | YES | 10,0 | — |
| TransformerWTI15MVA | int | YES | 10,0 | — |
| EngineerName | varchar | YES | 36 | — |
| EAFTransfomer80MVAWTI | decimal | YES | 18,4 | — |
| Transformer13MVAOTI | int | YES | 10,0 | — |
| EAFTransfomer80MVAOTI | decimal | YES | 18,4 | — |
| LRFTransfomer30MVAOTI | decimal | YES | 18,4 | — |
| Transformer3a3MVAOTI | int | YES | 10,0 | — |
| Transformer13MVAWTI | int | YES | 10,0 | — |
| TransformerOTI125MVA | int | YES | 10,0 | — |
| Transformer31MVAOTI | int | YES | 10,0 | — |
| TransformerOilLevel15MVA | int | YES | 10,0 | — |
| Shift | varchar | YES | 100 | — |
| Transformer516MVAOTI | int | YES | 10,0 | — |
| TransformerWTI125MVA | int | YES | 10,0 | — |
| TransformerOTI24MVA | int | YES | 10,0 | — |
| EAFTransfomer80MVAOilLevel | decimal | YES | 18,4 | — |
| LRFTransfomer30MVAOilLevel | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| Transformer43MVAOilLevel | int | YES | 10,0 | — |
| TransformerWTI24MVA | int | YES | 10,0 | — |
| LRFTransfomer30MVAWTI | decimal | YES | 18,4 | — |
| Transformer2a4MVAWTI | decimal | YES | 18,4 | — |
| TransformerOTI15MVA | int | YES | 10,0 | — |
| TransformerWTI63MVA | varchar | YES | 100 | — |
| Transformer2a4MVAOilLevel | int | YES | 10,0 | — |
| Transformer23MVAOilLevel | int | YES | 10,0 | — |
| TransformerOilLevel24MVA | int | YES | 10,0 | — |
| MVA125HotSpotTempChannel1 | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel2 | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel3 | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel4 | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel5 | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel6 | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel7 | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel8 | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel1WTI | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel1OilLevel | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel2OilLevel | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel2WTI | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel3WTI | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel3OilLevel | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel4OilLevel | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel5OilLevel | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel7OilLevel | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel6OilLevel | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel8OilLevel | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel4WTI | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel5WTI | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel6WTI | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel7WTI | varchar | YES | 100 | — |
| MVA125HotSpotTempChannel8WTI | varchar | YES | 100 | — |
| TransformerWTIHV63MVA | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0836D34E-EF2F-482C-A8B1-39B7A300885F | NULL | NULL | 2026-07-24T00:00:32.6270000 | NULL | False | False | NULL | NULL | NULL |
| 0759248C-B6CD-4FDC-A071-0D6475E57620 | NULL | NULL | 2026-07-20T00:13:44.6730000 | NULL | False | False | NULL | NULL | NULL |
| 0867FEC8-BC40-4A6E-87EC-5139E373C406 | NULL | NULL | 2026-08-01T00:48:30.9130000 | NULL | False | False | NULL | NULL | NULL |
| 0D78ECDA-D343-4025-AFCC-0158AF053B2A | NULL | NULL | 2026-08-12T00:22:03.9500000 | NULL | False | False | NULL | NULL | NULL |
| 114D79E6-3B8E-4673-BCB2-FE97E716427F | NULL | NULL | 2026-01-23T09:09:31.4700000 | NULL | False | False | NULL | NULL | NULL |
| 141CC760-D985-4EA9-A2BA-D0CB4BB9B9C5 | NULL | NULL | 2026-02-24T19:44:37.7830000 | NULL | False | False | NULL | NULL | NULL |
| 212B07D8-FC5C-4E2E-BEB3-4397DFCBDC56 | NULL | NULL | 2026-09-01T07:57:43.1500000 | NULL | False | False | NULL | NULL | NULL |
| 2843CC6B-B77D-4785-9D78-463F6DFD7D18 | NULL | NULL | 2026-07-20T00:40:27.0300000 | NULL | False | False | NULL | NULL | NULL |
| 2B521E70-32D4-464C-B43F-8B59192D3539 | NULL | NULL | 2026-05-03T19:50:55.8100000 | NULL | False | False | NULL | NULL | NULL |
| 2F0B8F05-691F-4B6C-859B-35D75500B978 | NULL | NULL | 2026-07-23T00:20:25.5830000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABC51BCC-48A3-4381-AF2B-9DEB9ADF1C6F | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9730000 | 2026-09-02T08:10:36.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| D41E3E08-2534-4154-88B3-528B32747B20 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7200000 | 2026-09-02T01:05:32.0000000 | False | False | NULL |  | NULL |
| 6E913E4F-1BA6-4818-B9F8-BDF535FE7B20 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1730000 | 2026-09-01T00:09:01.0000000 | False | False | NULL |  | NULL |
| 2EE3057F-37F0-458D-9E5B-01D9265CA194 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.0670000 | 2026-08-30T23:11:33.0000000 | False | False | NULL |  | NULL |
| B65CC9BE-5BC8-4318-A1C4-5A3375CB7176 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.4900000 | 2026-08-30T01:21:33.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 665D1437-A5C9-4E91-8BF5-B22D4B8DA74D | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:38.0400000 | 2026-08-29T01:21:43.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 76F12D86-C7F3-4541-A1E7-53B3CEC2F369 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.7300000 | 2026-08-28T00:46:00.0000000 | False | False | NULL |  | NULL |
| 7DD4E34D-302E-4431-B4B3-F6FFC7B319E1 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:54.0100000 | 2026-08-26T20:42:31.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| A712ACF1-36B0-4113-91B6-99CFE4CBE6A8 | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.2170000 | 2026-08-25T20:43:46.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 34E9998B-331D-4FFD-A230-AC99FD4252F0 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-23T00:12:23.0770000 | 2026-08-23T01:00:07.0000000 | False | False | NULL | 172.16.4.185 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Transformer.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
