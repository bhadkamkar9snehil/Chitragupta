# XStudio_Xbatch.dbo.Billet_NGConsumption_InFurnace

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, billet, discharge, duration, hhmm, ngconsumption, out, price, temp.

**Primary Key:** ID  
**Row Count:** 934  

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
| InTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| BilletNo | varchar | YES | 100 | — |
| NGConsumption | decimal | YES | 18,4 | — |
| Price | decimal | YES | 18,4 | — |
| OutTime | datetime | YES | — | — |
| DurationHHMM | varchar | YES | 100 | — |
| DischargeTemp | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01EDEBBD-57CF-411B-B70D-4CC89D6AA11E | NULL | NULL | NULL | NULL | 2026-08-19T17:10:55.3470000 | NULL | False | False | NULL |
| 019ECEE5-E28E-4268-91E5-D1673641A061 | NULL | NULL | NULL | NULL | 2026-08-18T09:28:04.1570000 | NULL | False | False | NULL |
| 01510D0D-94C9-458D-AF59-4A136B5804C3 | NULL | NULL | NULL | NULL | 2026-08-18T14:05:01.4670000 | NULL | False | False | NULL |
| 0149AB22-8B82-4C36-892E-5631E76A3E01 | NULL | NULL | NULL | NULL | 2026-08-03T17:23:09.7470000 | NULL | False | False | NULL |
| 01411FFF-7503-4524-8336-35C821240B0B | NULL | NULL | NULL | NULL | 2026-08-06T18:21:12.0630000 | NULL | False | False | NULL |
| 00D0803A-6AC3-4E6E-9E15-2F722C63D1F0 | NULL | NULL | NULL | NULL | 2026-08-21T16:01:37.0670000 | NULL | False | False | NULL |
| 0063B702-E30B-49DD-A3DB-2052FB0DB0E4 | NULL | NULL | NULL | NULL | 2026-08-22T11:02:14.9800000 | NULL | False | False | NULL |
| 0031EE29-CC5D-496B-A811-CBFEBA8A8623 | NULL | NULL | NULL | NULL | 2026-08-19T17:58:38.2100000 | NULL | False | False | NULL |
| 0030BC68-BBB3-4164-994F-19E25692746F | NULL | NULL | NULL | NULL | 2026-08-18T13:17:16.5130000 | NULL | False | False | NULL |
| 002CF713-FF3A-46A0-A2F1-89F48BDF6863 | NULL | NULL | NULL | NULL | 2026-08-21T16:18:43.9730000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01EDEBBD-57CF-411B-B70D-4CC89D6AA11E | NULL | NULL | NULL | NULL | 2026-08-19T17:10:55.3470000 | NULL | False | False | NULL |
| 019ECEE5-E28E-4268-91E5-D1673641A061 | NULL | NULL | NULL | NULL | 2026-08-18T09:28:04.1570000 | NULL | False | False | NULL |
| 01510D0D-94C9-458D-AF59-4A136B5804C3 | NULL | NULL | NULL | NULL | 2026-08-18T14:05:01.4670000 | NULL | False | False | NULL |
| 0149AB22-8B82-4C36-892E-5631E76A3E01 | NULL | NULL | NULL | NULL | 2026-08-03T17:23:09.7470000 | NULL | False | False | NULL |
| 01411FFF-7503-4524-8336-35C821240B0B | NULL | NULL | NULL | NULL | 2026-08-06T18:21:12.0630000 | NULL | False | False | NULL |
| 00D0803A-6AC3-4E6E-9E15-2F722C63D1F0 | NULL | NULL | NULL | NULL | 2026-08-21T16:01:37.0670000 | NULL | False | False | NULL |
| 0063B702-E30B-49DD-A3DB-2052FB0DB0E4 | NULL | NULL | NULL | NULL | 2026-08-22T11:02:14.9800000 | NULL | False | False | NULL |
| 0031EE29-CC5D-496B-A811-CBFEBA8A8623 | NULL | NULL | NULL | NULL | 2026-08-19T17:58:38.2100000 | NULL | False | False | NULL |
| 0030BC68-BBB3-4164-994F-19E25692746F | NULL | NULL | NULL | NULL | 2026-08-18T13:17:16.5130000 | NULL | False | False | NULL |
| 002CF713-FF3A-46A0-A2F1-89F48BDF6863 | NULL | NULL | NULL | NULL | 2026-08-21T16:18:43.9730000 | NULL | False | False | NULL |

---
