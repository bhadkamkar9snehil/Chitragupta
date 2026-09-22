# XStudio_Xbatch.dbo.EAF_LogSheet_Consumption

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, furnace, heat, production, tracking (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference consumption, electrode, mass, coke, pipe, temp, ton, and, billet, charge, ebtfilter, fettling.

**Primary Key:** ID  
**Row Count:** 17  
**Date Range (ModifiedOn):** 2025-08-02T11:11:25.0000000 to 2026-02-09T10:41:26.0000000  

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
| TempTips | decimal | YES | 18,4 | — |
| GunningMass | decimal | YES | 18,4 | — |
| Pipe3or40 | decimal | YES | 18,4 | — |
| Pipe1and1or4 | decimal | YES | 18,4 | — |
| IsProcessed | bit | YES | — | — |
| Name | varchar | YES | 100 | — |
| RamMass | decimal | YES | 18,4 | — |
| EBTFilter | decimal | YES | 18,4 | — |
| FettlingMass | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| HeatNo | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |
| ElectrodeConsumption1Kg | decimal | YES | 18,4 | — |
| RejectedBilletWeightTon | decimal | YES | 18,4 | — |
| NutCokeKgPerTon | decimal | YES | 18,4 | — |
| TapTemp | decimal | YES | 18,4 | — |
| ThroughputTPH | decimal | YES | 18,4 | — |
| PowerOnCharge | decimal | YES | 18,4 | — |
| CokeInjection | decimal | YES | 18,4 | — |
| ElectrodeConsumption2Kg | decimal | YES | 18,4 | — |
| ElectrodeConsumption3Kg | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49238C16-93CF-498C-80AD-9CE6D915B887 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T13:03:08.9900000 | 2025-08-02T11:11:25.0000000 | False | False | NULL |  |  |
| E882A730-B57E-4DD0-BB8C-3EED72C753E7 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-24T13:40:56.4270000 | 2025-11-24T13:40:56.0000000 | False | False | NULL | 10.76.15.11 |  |
| 2CE8903E-38C8-4B67-9BB1-380034723537 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-25T08:40:28.8130000 | 2025-11-25T08:40:28.0000000 | False | False | NULL |  |  |
| E9547DDE-23F1-47BD-BE46-4022C7980A54 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-27T10:15:04.8500000 | 2025-11-27T10:15:04.0000000 | False | False | NULL |  |  |
| 73925081-E0C4-4AD6-86A5-935673E678B0 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-11-28T13:50:37.1930000 | 2025-11-28T13:50:37.0000000 | False | False | NULL |  |  |
| 9163993D-DE10-47A6-8C46-F9F7BCB68F2A | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-08T08:51:35.6100000 | 2025-12-08T08:51:35.0000000 | False | False | NULL | 10.76.15.11 | NULL |
| 9C554BA5-29AE-464E-B8C4-F0D3A2A394FD | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-08T08:50:37.4100000 | 2026-01-08T08:50:37.0000000 | False | False | NULL | 10.76.5.79 | NULL |
| 474477C9-0B63-4BC1-A086-C8D722647C9C | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-01-29T15:28:59.4400000 | 2026-01-29T15:28:59.0000000 | False | False | NULL |  | NULL |
| D8B870DA-C2A5-4C38-AC6A-CAB55DA93420 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-29T15:32:05.2430000 | 2026-01-29T15:32:05.0000000 | False | False | NULL | 172.16.4.91 | NULL |
| C56EBB71-BF89-4442-A936-71981686BEAF | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-29T16:44:50.5600000 | 2026-01-29T16:44:50.0000000 | False | False | NULL | 172.16.4.91 | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D4FAD0D1-A4CE-4E54-8B95-83DF04BB7D77 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-02-09T10:41:26.2970000 | 2026-02-09T10:41:26.0000000 | False | False | NULL |  | NULL |
| E7419FBA-0DF6-47EE-96AB-A60AB38CF0A7 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-02-08T17:26:10.1970000 | 2026-02-08T17:26:10.0000000 | False | False | NULL |  | NULL |
| 971FB3C3-E42F-4F66-AF89-2FE93E26FFC9 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-02-05T17:08:03.7230000 | 2026-02-05T17:08:03.0000000 | False | False | NULL |  | NULL |
| 26C88981-0B1C-4174-93DD-62B08FE61DF9 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-02-04T08:48:20.4830000 | 2026-02-04T08:48:20.0000000 | False | False | NULL |  | NULL |
| B5DCBCB0-8EE2-4FD7-B463-7EC4F682B690 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-02-04T08:37:41.0200000 | 2026-02-04T08:37:41.0000000 | False | False | NULL |  | NULL |
| 74605557-D7FE-4DEA-9C26-2FE8399E3E2B | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-02-04T08:00:16.3070000 | 2026-02-04T08:00:16.0000000 | False | False | NULL |  | NULL |
| B6FCED59-8464-4CB1-BDBB-91D8958CAFCA | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-02-04T07:56:49.6630000 | 2026-02-04T07:56:49.0000000 | False | False | NULL |  | NULL |
| C56EBB71-BF89-4442-A936-71981686BEAF | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-29T16:44:50.5600000 | 2026-01-29T16:44:50.0000000 | False | False | NULL | 172.16.4.91 | NULL |
| D8B870DA-C2A5-4C38-AC6A-CAB55DA93420 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-01-29T15:32:05.2430000 | 2026-01-29T15:32:05.0000000 | False | False | NULL | 172.16.4.91 | NULL |
| 474477C9-0B63-4BC1-A086-C8D722647C9C | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-01-29T15:28:59.4400000 | 2026-01-29T15:28:59.0000000 | False | False | NULL |  | NULL |

---
