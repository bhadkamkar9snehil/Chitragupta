# XStudio_Xbatch.dbo.Ngconsumption_Summary_Day

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, mtd, ytd, discharge, total, ngcons, cold, discharged, hot, ngcong, avg, mmbtper.

**Primary Key:** ID  
**Row Count:** 65  
**Date Range (ModifiedOn):** 2026-08-06T12:53:53.1270000 to 2026-09-02T10:00:11.9830000  

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
| ReportDate | date | YES | — | — |
| NGCong | decimal | YES | 18,4 | — |
| Discharged | int | YES | 10,0 | — |
| NGCons | decimal | YES | 18,4 | — |
| NGconsMMBTPerTon | decimal | YES | 18,4 | — |
| ColdDischargeBillet | int | YES | 10,0 | — |
| HotDischargeBillet | int | YES | 10,0 | — |
| Discharged_MTD | int | YES | 10,0 | — |
| HotDischargeBillet_YTD | int | YES | 10,0 | — |
| HotDischargeBillet_MTD | int | YES | 10,0 | — |
| Discharged_YTD | int | YES | 10,0 | — |
| TotalBillet | decimal | YES | 18,4 | — |
| TotalNG | decimal | YES | 18,4 | — |
| NGCons_MTD | int | YES | 10,0 | — |
| TotalNG_YTD | decimal | YES | 18,4 | — |
| NGCong_MTD | decimal | YES | 18,4 | — |
| ColdDischargeBillet_MTD | int | YES | 10,0 | — |
| ColdDischargeBillet_YTD | int | YES | 10,0 | — |
| TotalNG_MTD | decimal | YES | 18,4 | — |
| NGCong_YTD | decimal | YES | 18,4 | — |
| TotalBillet_YTD | decimal | YES | 18,4 | — |
| NGCons_YTD | int | YES | 10,0 | — |
| TotalBillet_MTD | decimal | YES | 18,4 | — |
| AvgResidenceTime | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FF61CB16-7768-423E-B602-219A86E7456C | NULL | NULL | 2026-08-06T11:13:15.8800000 | 2026-08-06T12:53:53.1270000 | False | False | NULL | NULL | NULL |
| 09E233A3-E356-4D0E-A3A1-F60C24B89701 | NULL | NULL | 2026-08-01T10:38:03.9670000 | 2026-08-06T13:06:25.9370000 | False | False | NULL | NULL | NULL |
| 7298FFED-A81C-487B-94FC-5DEF5D6B0CDC | NULL | NULL | 2026-08-01T10:38:14.1400000 | 2026-08-06T13:06:36.5730000 | False | False | NULL | NULL | NULL |
| BE7A4E17-9BAA-4C7E-9902-793EE4AE0A45 | NULL | NULL | 2026-08-01T10:38:14.2530000 | 2026-08-06T13:06:36.6600000 | False | False | NULL | NULL | NULL |
| 00BA84A2-8660-45DD-808E-B5B3A7E77915 | NULL | NULL | 2026-08-01T10:38:14.1170000 | 2026-08-06T13:06:45.5200000 | False | False | NULL | NULL | NULL |
| 69786BEF-EB4D-4AB4-AAF2-27ED83C28D64 | NULL | NULL | 2026-08-01T10:38:23.9300000 | 2026-08-06T13:06:45.5200000 | False | False | NULL | NULL | NULL |
| AC8E34A7-9AD6-412F-8A2E-59DBB1AA8C82 | NULL | NULL | 2026-08-01T10:38:23.8530000 | 2026-08-06T13:06:55.3170000 | False | False | NULL | NULL | NULL |
| BF20C332-E2FF-4FC6-A015-BB993D9B1ACE | NULL | NULL | 2026-08-01T10:38:24.0800000 | 2026-08-06T13:07:04.8730000 | False | False | NULL | NULL | NULL |
| FD7158EE-F793-45FE-93B6-66D979D09894 | NULL | NULL | 2026-08-01T10:38:33.9130000 | 2026-08-06T13:07:04.9300000 | False | False | NULL | NULL | NULL |
| CA06163F-FCB4-4D43-BB4D-4A57ECAF231E | NULL | NULL | 2026-08-01T10:38:33.9030000 | 2026-08-06T13:07:15.2070000 | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 123ACD61-DD21-4F33-AE86-1EF17EB1CD5D | NULL | NULL | 2026-09-02T01:00:04.9000000 | 2026-09-02T10:00:11.9830000 | False | False | NULL | NULL | NULL |
| CD3E61FD-589E-470E-9B59-D92BF20EF8D4 | NULL | NULL | 2026-09-01T01:00:07.1000000 | 2026-09-02T00:00:10.2800000 | False | False | NULL | NULL | NULL |
| 75BEF33B-3421-41C5-AA92-7C4862055BCC | NULL | NULL | 2026-08-31T01:00:10.1870000 | 2026-09-01T00:00:11.1630000 | False | False | NULL | NULL | NULL |
| 8C5954B8-6969-450E-8017-AA7CFC3DC354 | NULL | NULL | 2026-08-30T01:00:08.2100000 | 2026-08-31T00:00:06.5330000 | False | False | NULL | NULL | NULL |
| 0EA4BD0A-2123-4E4A-8F4F-C38C3FB1E9AF | NULL | NULL | 2026-08-29T01:00:07.7930000 | 2026-08-30T00:00:03.4070000 | False | False | NULL | NULL | NULL |
| DAC463CA-4D98-42EE-8CBE-FE6D41958FBA | NULL | NULL | 2026-08-28T01:00:10.2400000 | 2026-08-29T00:00:11.3270000 | False | False | NULL | NULL | NULL |
| 8353F595-F0A7-45F1-8C55-9DA5A5319468 | NULL | NULL | 2026-08-27T01:00:09.9500000 | 2026-08-28T00:00:05.2970000 | False | False | NULL | NULL | NULL |
| 49C9AC1E-C4E1-4480-93D1-98EC6F568E08 | NULL | NULL | 2026-08-26T01:00:11.6830000 | 2026-08-27T00:00:03.1330000 | False | False | NULL | NULL | NULL |
| 6DAFE33F-0ADA-4840-B643-E9F004AC0495 | NULL | NULL | 2026-08-25T01:00:07.0130000 | 2026-08-26T00:00:04.4170000 | False | False | NULL | NULL | NULL |
| 86F669D9-BD70-47E4-8453-C8F5A51401FD | NULL | NULL | 2026-08-24T01:00:10.2730000 | 2026-08-25T00:00:11.2500000 | False | False | NULL | NULL | NULL |

---
