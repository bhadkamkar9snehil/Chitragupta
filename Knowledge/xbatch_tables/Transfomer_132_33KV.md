# XStudio_Xbatch.dbo.Transfomer_132_33KV

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference mva, voltagekv, pri, sec, level, mvabr, mvary, mvayb, oil, breather, conservator, cooling.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-10T09:05:29.0000000 to 2026-09-02T08:04:03.0000000  

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
| BreatherSilicaGelandoillevel63MVA | varchar | YES | 100 | — |
| SecVoltagekv125MVAYB | decimal | YES | 18,2 | — |
| MainConservatorOilLevel63MVA | varchar | YES | 100 | — |
| CoolingFanStatus125MVA | varchar | YES | 100 | — |
| BreatherSilicaGelandoillevel125MVA | varchar | YES | 100 | — |
| PriVoltagekv63MVABR | decimal | YES | 18,2 | — |
| Name | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| OLTCConservatorOilLevel125MVA | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| SecVoltagekv125MVABR | decimal | YES | 18,2 | — |
| PriVoltagekv63MVARY | decimal | YES | 18,2 | — |
| SecVoltagekv63MVARY | decimal | YES | 18,2 | — |
| SecVoltagekv63MVABR | decimal | YES | 18,2 | — |
| Shift | varchar | YES | 100 | — |
| TapPosition125MVA | int | YES | 10,0 | — |
| EngineerName | varchar | YES | -1 | — |
| OLTCConservatorOilLevel63MVA | varchar | YES | 100 | — |
| PriVoltagekv125MVAYB | decimal | YES | 18,2 | — |
| ParentID | varchar | YES | 36 | — |
| SecVoltagekv125MVARY | decimal | YES | 18,2 | — |
| MainConservatorOilLevel125MVA | varchar | YES | 100 | — |
| CoolingFanStatus63MVA | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| PriVoltagekv125MVARY | decimal | YES | 18,2 | — |
| PriVoltagekv125MVABR | decimal | YES | 18,2 | — |
| PriVoltagekv63MVAYB | decimal | YES | 18,2 | — |
| TapPosition63MVA | int | YES | 10,0 | — |
| SecVoltagekv63MVAYB | decimal | YES | 18,4 | — |
| TechnicianName | varchar | YES | 36 | — |
| NoofFansRunning63MVA | int | YES | 10,0 | — |
| NoofFansRunning125MVA | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 07A1E58A-2240-4FD4-98B3-1DF4AC831FC6 | NULL | NULL | 2026-01-25T12:55:56.8470000 | NULL | False | False | NULL | NULL | NULL |
| 00D915CA-D7E7-469C-AFFE-9ED0AE27EFEE | NULL | NULL | 2026-01-30T07:34:11.5370000 | NULL | False | False | NULL | NULL | NULL |
| 07F39128-C284-4DDA-B401-97EA0D1B68F8 | NULL | NULL | 2025-12-27T04:59:44.9770000 | NULL | False | False | NULL | NULL | NULL |
| 09414360-2D73-4B29-B156-EC00A7CA3BF6 | NULL | NULL | 2026-07-20T00:40:26.9830000 | NULL | False | False | NULL | NULL | NULL |
| 09752301-5773-4D4E-B3BF-509391C1DC5D | NULL | NULL | 2025-12-27T23:25:44.2300000 | NULL | False | False | NULL | NULL | NULL |
| 166EBF29-C3E8-4BEC-A755-99D43A030259 | NULL | NULL | 2026-08-01T00:48:30.8670000 | NULL | False | False | NULL | NULL | NULL |
| 180D53DD-E642-4DF8-874B-1B4FA4936066 | NULL | NULL | 2026-08-03T22:15:38.4530000 | NULL | False | False | NULL | NULL | NULL |
| 19ADA139-866E-4EE5-BFAF-D2571DBF9390 | NULL | NULL | 2026-07-31T01:09:14.3130000 | NULL | False | False | NULL | NULL | NULL |
| 1FE61197-ACD6-4F42-B8B6-D5CAF0E6314C | NULL | NULL | 2026-08-01T23:46:19.5970000 | NULL | False | False | NULL | NULL | NULL |
| 22E49046-927E-4F55-9D06-A7C2A4201940 | NULL | NULL | 2026-07-11T00:10:56.5670000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7E05AAE4-312D-47C0-BE9F-8BF95DDB8A11 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9230000 | 2026-09-02T08:04:03.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| F40B9A9D-F990-4CD0-A3BC-73041EE7F0A3 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.6800000 | 2026-09-02T00:36:50.0000000 | False | False | NULL |  | NULL |
| 81510F0E-CD0A-4C68-8391-774990F661AC | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.1030000 | 2026-09-01T08:13:14.0000000 | False | False | NULL |  | NULL |
| D5497D3A-657A-4801-A5B5-5328F4DCF031 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1270000 | 2026-08-31T23:37:00.0000000 | False | False | NULL |  | NULL |
| 9405C19F-30C6-45EF-B6E7-1F03F6F32071 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.0200000 | 2026-08-30T23:05:47.0000000 | False | False | NULL |  | NULL |
| C751C3AD-70F2-4A7A-8472-1226990045F4 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.4400000 | 2026-08-30T01:19:02.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 789EA41E-24B0-4C9A-B056-3512AD6DF9CF | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:37.9930000 | 2026-08-29T01:15:50.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| 0C853ADD-EA53-4E97-84F4-8FC3F1239E75 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.6900000 | 2026-08-28T00:40:51.0000000 | False | False | NULL |  | NULL |
| 1D0BCB1E-D4C9-4656-BE4A-8D6807499CD6 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:53.9700000 | 2026-08-26T21:38:16.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| F84A4CE6-8EC4-4E96-90F4-A80D68630E85 | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.1900000 | 2026-08-25T20:37:46.0000000 | False | False | NULL | 10.76.5.60 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transfomer_132_33KV.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Transfomer_132_33KV.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
