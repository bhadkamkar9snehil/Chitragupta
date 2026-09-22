# XStudio_Xbatch.dbo.Power_Consumption_LogSheet

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, electrical consumption, electricity, energy, energy dashboard, furnace, heat, kwh, power consumption, production, tracking (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference transformer, mva, mvalossesk, eaf, lrf, mill, ngactual, ngconsumption, oxygen, plant, reading, rmngconsumption.

**Primary Key:** ID  
**Row Count:** 245  
**Date Range (ModifiedOn):** 2026-03-01T00:42:41.0000000 to 2026-09-02T07:12:05.0000000  

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
| Transformer132kv1 | decimal | YES | 18,4 | — |
| Transformer132kv2 | decimal | YES | 18,4 | — |
| Transformer33kv1 | decimal | YES | 18,4 | — |
| Transformer33kv2 | decimal | YES | 18,4 | — |
| EAF | decimal | YES | 18,4 | — |
| LRF | decimal | YES | 18,4 | — |
| Transformer24MVA | decimal | YES | 18,4 | — |
| Transformer15MVA | decimal | YES | 18,4 | — |
| RollingMill | decimal | YES | 18,4 | — |
| WRM | decimal | YES | 18,4 | — |
| OxygenPlant4A | decimal | YES | 18,4 | — |
| NGConsumptionSm3 | decimal | YES | 18,4 | — |
| Transformer63MVALosseskWH | decimal | YES | 18,4 | — |
| Transformer125MVALosseskWH | decimal | YES | 18,4 | — |
| NGActualReading | decimal | YES | 18,4 | — |
| Shift | varchar | YES | 100 | — |
| RMNGConsumption | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18286BC4-F916-4DE9-8AFC-76E903E883BA | NULL | NULL | 2026-07-03T10:39:46.5000000 | NULL | False | False | NULL | NULL | NULL |
| 76409091-CB12-44D3-8808-078537A927AE | NULL | NULL | 2026-07-03T10:38:56.0970000 | NULL | False | False | NULL | NULL | NULL |
| 96B68CFD-E5F2-4782-B8D0-BADA80392B32 | NULL | NULL | 2026-02-20T12:48:37.2170000 | NULL | False | False | NULL | NULL | NULL |
| A41F8723-0B4A-48B4-9E70-896BC675EEE5 | NULL | NULL | 2026-07-03T10:30:45.4870000 | NULL | False | False | NULL | NULL | NULL |
| BD51F01A-77DD-4015-99BF-CA31A4C64D8F | NULL | NULL | 2026-07-03T10:32:46.0000000 | NULL | False | False | NULL | NULL | NULL |
| EE5D83A4-2BD5-4C34-B576-2F013172BCEF | NULL | NULL | 2026-07-03T10:36:55.9270000 | NULL | False | False | NULL | NULL | NULL |
| AEDBCEC3-D440-49FA-B342-69420C3AA3D9 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-03-01T00:41:08.8330000 | 2026-03-01T00:42:41.0000000 | False | False | NULL |  | NULL |
| 103E595E-D916-4C00-8C4E-47F40F8AB048 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-03-02T00:36:49.7570000 | 2026-03-02T00:41:50.0000000 | False | False | NULL |  | NULL |
| B32A81AE-ADFB-401F-9659-DFF7B2E21743 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-03-05T01:38:49.4100000 | 2026-03-06T00:41:47.0000000 | False | False | NULL |  | NULL |
| 78CDDC65-568F-4CC0-BEF6-3D29EBF9F196 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-03-04T02:01:49.4300000 | 2026-03-06T00:42:59.0000000 | False | False | NULL |  | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0E73FCBA-B4C6-41B8-8367-9F3CAAC0D1C3 | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:10:18.8000000 | 2026-09-02T07:12:05.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| 5CD65A82-F85C-42F2-B8BF-32D230B39CE2 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:41:34.5670000 | 2026-09-01T07:43:31.0000000 | False | False | NULL |  | NULL |
| BCB51326-E032-4705-B14F-2C9818A3C22F | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T17:29:31.1170000 | 2026-08-31T17:31:19.0000000 | False | False | NULL |  | NULL |
| 224A2AA2-B2B2-421D-A691-076D0C205F32 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T08:02:35.0170000 | 2026-08-30T08:04:40.0000000 | False | False | NULL |  | NULL |
| 039B7C7C-D792-4E8A-A3D8-3AE47B8DA43C | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T06:42:51.0630000 | 2026-08-29T06:54:53.0000000 | False | False | NULL |  | NULL |
| AB19E109-6B29-470D-91A8-2808A6614E62 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T10:03:53.9970000 | 2026-08-28T07:09:39.0000000 | False | False | NULL |  | NULL |
| 09FFB975-6E54-4179-B82C-F6F06B72D2F0 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-28T06:58:53.6970000 | 2026-08-28T07:09:06.0000000 | False | False | NULL |  | NULL |
| AD60E9FF-6A25-40B2-990E-C9D5040C1BBB | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-26T07:23:29.2100000 | 2026-08-26T07:25:25.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| E345F75A-079C-44F8-BBF4-0432EB1FA58C | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-25T07:00:52.2370000 | 2026-08-25T07:03:44.0000000 | False | False | NULL |  | NULL |
| BD5B93CF-3FB4-4B23-BD0B-8C2307E9FD83 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-24T06:48:42.2000000 | 2026-08-24T06:50:57.0000000 | False | False | NULL | 172.16.4.185 | NULL |

---
