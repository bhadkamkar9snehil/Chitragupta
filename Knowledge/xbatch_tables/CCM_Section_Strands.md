# XStudio_Xbatch.dbo.CCM_Section_Strands

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference strand, mould, ladle, life, temp, jacket, operator, section, sizemm, time, tube, heat.

**Primary Key:** ID  
**Row Count:** 22  
**Date Range (ModifiedOn):** 2025-07-22T16:10:22.0000000 to 2026-05-04T17:10:30.0000000  

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
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| SectionSizemmStrand1 | varchar | YES | 100 | — |
| SectionSizemmStrand2 | varchar | YES | 100 | — |
| SectionSizemmStrand3 | varchar | YES | 100 | — |
| SectionSizemmStrand4 | varchar | YES | 100 | — |
| SectionSizemmStrand5 | varchar | YES | 100 | — |
| SectionSizemmStrand6 | varchar | YES | 100 | — |
| HeatNo | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |
| MouldJacketNoStrand1 | int | YES | 10,0 | — |
| MouldJacketNoStrand2 | int | YES | 10,0 | — |
| MouldJacketNoStrand3 | int | YES | 10,0 | — |
| MouldJacketNoStrand4 | int | YES | 10,0 | — |
| MouldJacketNoStrand5 | int | YES | 10,0 | — |
| MouldJacketNoStrand6 | int | YES | 10,0 | — |
| MouldTubeNoStrand1 | varchar | YES | 100 | — |
| MouldTubeNoStrand2 | varchar | YES | 100 | — |
| MouldTubeNoStrand3 | varchar | YES | 100 | — |
| MouldTubeNoStrand6 | varchar | YES | 100 | — |
| MouldTubeNoStrand4 | varchar | YES | 100 | — |
| MouldTubeNoStrand5 | varchar | YES | 100 | — |
| MouldLifeStrand5 | int | YES | 10,0 | — |
| MouldLifeStrand1 | int | YES | 10,0 | — |
| MouldLifeStrand2 | int | YES | 10,0 | — |
| MouldLifeStrand3 | int | YES | 10,0 | — |
| MouldLifeStrand6 | int | YES | 10,0 | — |
| MouldLifeStrand4 | int | YES | 10,0 | — |
| MouldOperatorStrand1 | varchar | YES | 36 | — |
| MouldOperatorStrand2 | varchar | YES | 36 | — |
| MouldOperatorStrand3 | varchar | YES | 36 | — |
| MouldOperatorStrand4 | varchar | YES | 36 | — |
| MouldOperatorStrand5 | varchar | YES | 36 | — |
| MouldOperatorStrand6 | varchar | YES | 36 | — |
| LRFLMWeightmT | decimal | YES | 18,4 | — |
| LadleNo | int | YES | 10,0 | — |
| LadleLife | int | YES | 10,0 | — |
| LadleLiftingTempC | decimal | YES | 18,4 | — |
| LadleShrouldLife | int | YES | 10,0 | — |
| LadlePalcedonArmNo | int | YES | 10,0 | — |
| LadleGrossWeightmT | decimal | YES | 18,4 | — |
| EmptyLadleWeightmT | decimal | YES | 18,4 | — |
| LadleNuzzalOpening | xml | YES | -1 | — |
| TeemingStartTime | datetime | YES | — | — |
| TeemingEndTime | datetime | YES | — | — |
| TotalTime | int | YES | 10,0 | — |
| MouldOilConsumption | decimal | YES | 18,4 | — |
| TundishNumber | int | YES | 10,0 | — |
| LaddleOnTurrentStartTime | datetime | YES | — | — |
| LaddleOnTurrentEndTime | datetime | YES | — | — |
| LaddleOnTurrentTime | datetime | YES | — | — |
| TundishTemp1 | decimal | YES | 18,4 | — |
| TundishTemp2 | decimal | YES | 18,4 | — |
| TundishTemp3 | decimal | YES | 18,4 | — |
| LiquidusAsh1 | decimal | YES | 18,4 | — |
| LiquidusAsh2 | decimal | YES | 18,4 | — |
| LiquidusAsh3 | decimal | YES | 18,4 | — |
| SuperHeatTemp1 | decimal | YES | 18,4 | — |
| SuperHeatTemp2 | decimal | YES | 18,4 | — |
| SuperHeatTemp3 | decimal | YES | 18,4 | — |
| Parentid | varchar | YES | 36 | — |
| SuperHeat | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 97E72B39-4ADE-4DB2-8A58-68C313D3E9F5 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T17:26:29.0800000 | 2025-07-22T16:10:22.0000000 | False | False | NULL |  |  |
| 8E183204-943B-4FF0-B7C8-5EEC5138B06C | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-22T15:43:50.0130000 | 2025-08-02T10:28:41.0000000 | False | False | NULL |  |  |
| 9A1A4DFD-EFE1-44B9-AB2D-793501E610BB | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-24T13:56:48.9970000 | 2025-11-24T13:56:48.0000000 | False | False | NULL | 10.76.15.11 |  |
| FDFFDCBA-F396-4BF7-A0F8-AC55C02DBF30 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-24T14:30:10.8570000 | 2025-11-24T14:30:10.0000000 | False | False | NULL | 10.76.15.11 |  |
| D7929845-A747-4D32-A20F-205C549694C3 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T08:07:29.7770000 | 2025-11-26T08:07:29.0000000 | False | False | NULL |  |  |
| 94E611EE-710A-44A5-87F1-B80365F398CE | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-27T10:31:23.1400000 | 2025-11-27T10:31:23.0000000 | False | False | NULL |  |  |
| 22BE0222-394E-466E-B280-19ECFCDA5577 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-17T11:13:23.2100000 | 2025-12-17T11:13:23.0000000 | False | False | NULL | 172.16.6.64 | NULL |
| AD3D8A9A-2A03-402C-A797-B70AE71FC558 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-17T13:52:54.5570000 | 2025-12-17T13:52:54.0000000 | False | False | NULL | 172.16.6.64 | NULL |
| 09AA1285-A30D-45C6-BAEF-295696656E9E | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-24T10:34:07.9470000 | 2025-12-24T10:34:07.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| F7BE19AF-1464-4D9A-8C1E-F0209E7BA27B | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-24T10:37:21.9970000 | 2025-12-24T10:37:21.0000000 | False | False | NULL | 10.76.15.11 | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 80DA977F-A5DE-4856-9584-EF23F63AE5D4 | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-05-04T17:10:30.2130000 | 2026-05-04T17:10:30.0000000 | False | False | NULL | 10.76.20.92 | NULL |
| 3CFB0454-F5BB-48E6-849D-63F4B56682A6 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-29T15:43:55.4130000 | 2026-04-29T15:43:55.0000000 | False | False | NULL |  | NULL |
| F104C07A-9E84-4610-B32C-55D0D16816DF | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-29T15:06:56.2330000 | 2026-04-29T15:06:56.0000000 | False | False | NULL |  | NULL |
| 8488E118-0264-4F45-A3AF-447596C36DF8 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-04-06T17:10:23.2930000 | 2026-04-06T17:10:23.0000000 | False | False | NULL |  | NULL |
| BD19F7B0-93D4-4347-9B82-6052782893FC | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-04-06T16:13:52.7300000 | 2026-04-06T16:13:52.0000000 | False | False | NULL |  | NULL |
| 3DFE03F7-4635-40A2-BA96-543DA23A8A13 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-03-22T15:25:29.8830000 | 2026-03-22T15:25:29.0000000 | False | False | NULL |  | NULL |
| 05DFA7B1-2CAD-4E2B-AC18-62DBDB5108D8 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-03-19T01:44:21.1530000 | 2026-03-19T01:44:21.0000000 | False | False | NULL |  | NULL |
| BCA855EE-180B-4CFE-948B-6F97930F3CD4 | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 5950DFF4-C534-4068-920B-3BDA00F4FCDF | 2026-03-19T01:24:42.5400000 | 2026-03-19T01:24:42.0000000 | False | False | NULL |  | NULL |
| 9EE43F34-2ACC-48F6-AF3E-B69CD133E447 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-03-08T14:32:37.0530000 | 2026-03-08T14:32:37.0000000 | False | False | NULL |  | NULL |
| AB068E0B-E83F-40C6-978F-1021F726EE72 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-29T15:34:04.5570000 | 2026-01-29T15:34:04.0000000 | False | False | NULL | 172.16.4.91 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_Per_Heat.SuperHeat` -> `XStudio_XBatch.CCM_Section_Strands.SuperHeat` (Many to One)
- `XStudio_XBatch.CCM_Section_Strands.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.CCM_Section_Strands.MouldOperatorStrand1` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_Section_Strands.MouldOperatorStrand2` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_Section_Strands.MouldOperatorStrand3` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_Section_Strands.MouldOperatorStrand4` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_Section_Strands.MouldOperatorStrand5` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_Section_Strands.MouldOperatorStrand6` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
