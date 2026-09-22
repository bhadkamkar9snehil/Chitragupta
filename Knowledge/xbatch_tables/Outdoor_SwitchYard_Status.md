# XStudio_Xbatch.dbo.Outdoor_SwitchYard_Status

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, inventory, yard (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference breaker, circuit, status, chcking, counter, name, physicaland, pressure, reading, switch, visual, yard.

**Primary Key:** ID  
**Row Count:** 432  
**Date Range (ModifiedOn):** 2025-09-12T11:01:36.0000000 to 2026-09-02T07:47:04.0000000  

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
| IsProcessed | bit | YES | — | — |
| PhysicalandVisualChckingSwitchYardF1 | varchar | YES | 100 | — |
| CircuitBreakerStatusCounterReadingF2 | int | YES | 10,0 | — |
| TechnicianName | varchar | YES | -1 | — |
| BreakerPressureF1 | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |
| ReportDate | date | YES | — | — |
| PhysicalandVisualChckingSwitchYardF2 | varchar | YES | 20 | — |
| EntryDateTime | datetime | YES | — | — |
| BreakerPressureF2 | int | YES | 10,0 | — |
| Shift | varchar | YES | 100 | — |
| CircuitBreakerStatusF2 | varchar | YES | 100 | — |
| CircuitBreakerStatusCounterReadingF1 | int | YES | 10,0 | — |
| CircuitBreakerStatusF1 | varchar | YES | 100 | — |
| EngineerName | varchar | YES | -1 | — |
| Name | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 009942CC-5E01-4F91-9E01-07C90DD401C0 | NULL | NULL | 2026-08-25T00:58:05.4970000 | NULL | False | False | NULL | NULL | NULL |
| 07EE5B64-D1C1-4ECF-BB50-5602BC239F7E | NULL | NULL | 2026-08-15T00:12:41.2530000 | NULL | False | False | NULL | NULL | NULL |
| 097EFBE6-7E44-419A-B617-85E45CD72BB8 | NULL | NULL | 2026-04-30T08:06:41.9270000 | NULL | False | False | NULL | NULL | NULL |
| 0D5B9A86-9C0C-4A7C-858D-96B94A91169D | NULL | NULL | 2026-08-04T18:45:03.9300000 | NULL | False | False | NULL | NULL | NULL |
| 0E89C294-1EBD-45F7-8248-623EC33E2468 | NULL | NULL | 2026-07-28T01:22:23.7730000 | NULL | False | False | NULL | NULL | NULL |
| 14D12C75-995B-4B44-810E-ECED9311BDCC | NULL | NULL | 2026-02-19T22:19:19.5900000 | NULL | False | False | NULL | NULL | NULL |
| 153E14EE-91D7-40DA-A78A-701A7E9132D2 | NULL | NULL | 2026-08-14T00:44:39.1970000 | NULL | False | False | NULL | NULL | NULL |
| 169036C9-A588-4A0B-9D01-C4E532AC1BBF | NULL | NULL | 2026-07-13T00:50:22.1670000 | NULL | False | False | NULL | NULL | NULL |
| 1EADC56B-4606-4A71-8A83-5E7F3012C96C | NULL | NULL | 2026-07-11T00:10:56.5370000 | NULL | False | False | NULL | NULL | NULL |
| 28755BFF-8552-4CB2-982D-B37EFA0C774A | NULL | NULL | 2026-01-19T17:10:36.6100000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F0F1EC5C-1B01-4317-AE53-7517FCE0C53E | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2026-09-02T07:45:42.9030000 | 2026-09-02T07:47:04.0000000 | False | False | NULL | 172.16.4.185 | NULL |
| CEB23B82-DE2A-4558-987A-95E38FD37D80 | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:14:15.6530000 | 2026-09-02T00:33:45.0000000 | False | False | NULL |  | NULL |
| 5AE6C10D-88C5-4778-A4E0-B706CC0EE59B | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:57:43.0730000 | 2026-09-01T07:58:35.0000000 | False | False | NULL |  | NULL |
| BA407333-F753-4258-B2B7-7EBAD0F408D4 | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-31T23:30:16.1000000 | 2026-08-31T23:31:15.0000000 | False | False | NULL |  | NULL |
| EB400F58-5290-4F67-A2D7-4CCECF06B7D6 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T22:53:49.9970000 | 2026-08-30T22:55:05.0000000 | False | False | NULL |  | NULL |
| D85663C3-04DB-49B4-91BE-28802785256A | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T22:55:49.4100000 | 2026-08-29T23:47:29.0000000 | False | False | NULL |  | NULL |
| FE4322E1-323D-4AFE-A2AE-6B05A3670066 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-29T00:48:37.9700000 | 2026-08-29T00:49:55.0000000 | False | False | NULL |  | NULL |
| 984A38C1-0C0D-4399-8838-078A7708F6B2 | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-27T23:25:11.6700000 | 2026-08-27T23:26:06.0000000 | False | False | NULL |  | NULL |
| F9A97ABF-1C47-4991-A2AE-82053227AE01 | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-26T20:14:53.9470000 | 2026-08-26T20:16:44.0000000 | False | False | NULL | 10.76.5.60 | NULL |
| 82384FFD-325F-42F5-B1F1-2B918123767D | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-08-25T20:01:32.1770000 | 2026-08-25T20:02:34.0000000 | False | False | NULL | 10.76.5.60 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Outdoor_SwitchYard_Status.EngineerName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Outdoor_SwitchYard_Status.TechnicianName` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
