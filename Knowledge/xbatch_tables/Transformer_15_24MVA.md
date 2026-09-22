# XStudio_Xbatch.dbo.Transformer_15_24MVA

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference voltagekv, mva, pri, sec, level, mvabr, mvary, mvayb, oil, breather, conservator, gelandoillevel.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-12-23T02:40:54.0000000 to 2026-09-02T08:06:03.0000000  

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
| TapPosition24MVA | int | YES | 10,0 | — |
| MainConservatorOilLevel15MVA | varchar | YES | 100 | — |
| SecVoltagekv24MVARY | decimal | YES | 18,2 | — |
| SecVoltagekv15MVARY | decimal | YES | 18,2 | — |
| PriVoltagekv15MVABR | decimal | YES | 18,2 | — |
| MainConservatorOilLevel24MVA | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| PriVoltagekv15MVARY | decimal | YES | 18,2 | — |
| PriVoltagekv24MVABR | decimal | YES | 18,2 | — |
| ParentID | varchar | YES | 36 | — |
| PriVoltagekv15MVAYB | decimal | YES | 18,2 | — |
| TechnicianName | varchar | YES | 36 | — |
| PriVoltagekv24MVAYB | decimal | YES | 18,2 | — |
| BreatherSilicaGelandoillevel15MVA | varchar | YES | 100 | — |
| SecVoltagekv15MVAYB | decimal | YES | 18,2 | — |
| OLTCConservatorOilLevel15MVA | varchar | YES | 100 | — |
| SecVoltagekv15MVABR | decimal | YES | 18,2 | — |
| TapPosition15MVA | int | YES | 10,0 | — |
| Shift | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| EngineerName | varchar | YES | 36 | — |
| SecVoltagekv24MVABR | decimal | YES | 18,2 | — |
| OLTCConservatorOilLevel24MVA | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| PriVoltagekv24MVARY | decimal | YES | 18,2 | — |
| BreatherSilicaGelandoillevel24MVA | varchar | YES | 100 | — |
| SecVoltagekv24MVAYB | decimal | YES | 18,2 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 067728B3-554D-4736-A723-A31CDF20BE3B | NULL | NULL | 2026-08-01T23:46:19.6200000 | NULL | False | False | NULL | NULL | NULL |
| 068EAFCD-882C-4016-AF0E-F3E461012EC9 | NULL | NULL | 2026-07-24T00:00:32.6170000 | NULL | False | False | NULL | NULL | NULL |
| 08DDE002-01DC-4150-A3C1-BBCFBC77DA01 | NULL | NULL | 2026-07-11T00:10:56.5870000 | NULL | False | False | NULL | NULL | NULL |
| 08E6DA59-D5D0-42A4-A9E0-EF7416E366F5 | NULL | NULL | 2026-08-04T18:45:03.9800000 | NULL | False | False | NULL | NULL | NULL |
| 0972AB06-CDA2-404B-A064-193988314F53 | NULL | NULL | 2026-02-14T09:06:38.6870000 | NULL | False | False | NULL | NULL | NULL |
| 0AADC7F4-3CB4-4E3F-967A-4520BC01B279 | NULL | NULL | 2026-07-18T00:48:14.3200000 | NULL | False | False | NULL | NULL | NULL |
| 18F0AEE9-9A58-4D12-A82B-A4D588A872E4 | NULL | NULL | 2025-12-27T04:59:45.0000000 | NULL | False | False | NULL | NULL | NULL |
| 1BEE124D-0F64-451D-8BC9-724F3CB922C1 | NULL | NULL | 2026-08-25T00:58:05.5370000 | NULL | False | False | NULL | NULL | NULL |
| 20483774-5C2D-4CA1-BA3E-A5DFF4AD2A84 | NULL | NULL | 2026-08-11T00:30:12.3270000 | NULL | False | False | NULL | NULL | NULL |
| 209045D1-2544-45B3-AB3C-2849B976E594 | NULL | NULL | 2026-01-25T12:55:56.8670000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 89C4D011-67CA-4DDB-B373-FF44FE1E438E | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9500000 | 2026-09-02T08:06:03.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| FC5C7EC4-174C-44E8-8450-83BC3A82AABA | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.7030000 | 2026-09-02T00:38:44.0000000 | False | False | NULL |  | NULL |
| 83DD8A14-C9BD-4D45-8596-C22B91B56FB5 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1500000 | 2026-08-31T23:37:46.0000000 | False | False | NULL |  | NULL |
| F5049022-EF53-4B45-A9E2-234677FE0BCA | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:50.0430000 | 2026-08-30T23:07:13.0000000 | False | False | NULL |  | NULL |
| 043270D5-677B-442C-B764-2787E3A78449 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-29T22:55:49.4630000 | 2026-08-30T01:19:56.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| CC94FC94-A874-4988-876B-1E62591EB0C6 | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2026-08-29T00:48:38.0130000 | 2026-08-29T01:17:32.0000000 | False | False | NULL | 10.76.5.34 | NULL |
| C56F57C2-3F8C-4CB2-BB6A-A76103862544 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.7100000 | 2026-08-28T00:41:58.0000000 | False | False | NULL |  | NULL |
| F492F53D-4EC0-4D45-AD32-2B65DB872105 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:53.9900000 | 2026-08-26T21:39:49.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 019592DE-54FA-414C-B314-A915C1CE4B49 | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.2030000 | 2026-08-25T20:39:40.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| E33A8CBB-2183-4BE0-84CD-05A1C8537ED9 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-23T00:12:23.0370000 | 2026-08-23T00:57:36.0000000 | False | False | NULL | 172.16.4.185 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_15_24MVA.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Transformer_15_24MVA.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
