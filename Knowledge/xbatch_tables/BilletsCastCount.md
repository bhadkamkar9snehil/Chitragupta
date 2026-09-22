# XStudio_Xbatch.dbo.BilletsCastCount

**table_kind:** production_data

### What this table is for

- **Curated domain match (billet_inventory):** Billet missing, wrong location/furnace/yard/transfer, genealogy, count, or weight issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** billet, billets, cast, confirmed, core, count, data, entities, event, flow, from, furnace, heat, insert, map, procedure, production, routing, same, sohar, stored, system, tracking, xbatch, xlsx, xstudio (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference status, time, actual, billets, countby, end, equipment, flow, heat, operator, start, work.

**Primary Key:** ID  
**Row Count:** 7,245  
**Date Range (ModifiedOn):** 2025-08-21T23:15:16.9730000 to 2026-07-08T19:30:54.4100000  

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
| EquipmentID | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| HeatID | decimal | YES | 18,4 | — |
| WorkFlowStatus | varchar | YES | 50 | — |
| ActualBilletsCountbyOperator | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 41454922-E302-46C6-AAB2-7A163B4F3EA8 | NULL | NULL | NULL | NULL | 2025-08-21T22:08:44.2970000 | 2025-08-21T23:15:16.9730000 | False | False | NULL |
| A019966B-AC6A-418C-AB68-F7FF0608E2BC | NULL | NULL | NULL | NULL | 2025-08-21T23:16:25.4000000 | 2025-08-22T00:16:56.2800000 | False | False | NULL |
| A0DD2A3F-B8AC-46AF-B2F3-5E4CFCEF042B | NULL | NULL | NULL | NULL | 2025-08-22T00:17:58.1200000 | 2025-08-22T01:18:56.1400000 | False | False | NULL |
| 42FA3106-B1EC-407A-BD32-2CBCE5A396AE | NULL | NULL | NULL | NULL | 2025-08-22T01:19:14.3870000 | 2025-08-22T02:19:10.1330000 | False | False | NULL |
| 02A003EF-4ECC-4C22-93FA-3D269CD7618B | NULL | NULL | NULL | NULL | 2025-08-22T02:19:28.8730000 | 2025-08-22T03:12:43.0630000 | False | False | NULL |
| E7799989-28E3-40D6-91E7-DC6B70472AF6 | NULL | NULL | NULL | NULL | 2025-08-22T03:17:14.9430000 | 2025-08-22T04:11:12.0300000 | False | False | NULL |
| 468C3680-30B7-494A-A5F9-B1F7BCC91386 | NULL | NULL | NULL | NULL | 2025-08-22T04:11:52.0930000 | 2025-08-22T05:10:01.1400000 | False | False | NULL |
| 7570D16A-C73C-445D-A253-BDE7CC30D7D9 | NULL | NULL | NULL | NULL | 2025-08-22T05:11:35.9630000 | 2025-08-22T06:08:11.9230000 | False | False | NULL |
| B9C155B8-3421-4306-8D0C-D97FD8989E30 | NULL | NULL | NULL | NULL | 2025-08-22T06:08:45.9000000 | 2025-08-22T07:05:47.9530000 | False | False | NULL |
| 37E6F5E9-FB7C-4BA3-9B17-FA5060F1C903 | NULL | NULL | NULL | NULL | 2025-08-22T07:06:10.2730000 | 2025-08-22T07:58:52.2170000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D2DFAAB5-5844-428B-AC34-F9D00A17C9E7 | NULL | NULL | NULL |  | 2026-07-08T19:15:26.1300000 | 2026-07-08T19:30:54.4100000 | False | False | NULL |
| AAE851D0-B61C-4B79-B2CA-708F04A6A1C2 | NULL | NULL | NULL |  | 2026-07-08T18:26:50.0130000 | 2026-07-08T19:15:20.8500000 | False | False | NULL |
| 4417EE7B-19F1-450A-9E8F-D3B08A6BDB85 | NULL | NULL | NULL |  | 2026-07-08T17:29:49.0870000 | 2026-07-08T18:23:07.4300000 | False | False | NULL |
| F3B4F966-88F5-448D-97A2-C8881EBA82B3 | NULL | NULL | NULL |  | 2026-07-08T16:35:01.1730000 | 2026-07-08T17:25:38.5800000 | False | False | NULL |
| 8CDE1B87-BB75-485B-8CF5-B1C95AE38E30 | NULL | NULL | NULL |  | 2026-07-08T15:19:38.2400000 | 2026-07-08T16:32:35.3130000 | False | False | NULL |
| E383C8CF-8E5D-4EA9-B8E4-3E42D886A4EC | NULL | NULL | NULL |  | 2026-07-08T14:18:24.1100000 | 2026-07-08T15:19:11.6430000 | False | False | NULL |
| 3193329A-A1BB-4F20-8E53-97131F7FBA36 | NULL | NULL | NULL |  | 2026-07-08T13:17:07.2230000 | 2026-07-08T14:17:38.9900000 | False | False | NULL |
| 2AB2531C-98A3-422E-B9A3-B5860DB6A748 | NULL | NULL | NULL |  | 2026-07-08T12:15:18.0830000 | 2026-07-08T13:15:36.0900000 | False | False | NULL |
| 4C1FC94F-1654-48D2-A4CB-8E2E7D1ED142 | NULL | NULL | NULL |  | 2026-07-08T11:12:22.1370000 | 2026-07-08T12:11:49.1000000 | False | False | NULL |
| 56580090-8FE4-4C97-8373-BB3479C25764 | NULL | NULL | NULL |  | 2026-07-08T10:09:31.2170000 | 2026-07-08T11:09:20.5100000 | False | False | NULL |

---
