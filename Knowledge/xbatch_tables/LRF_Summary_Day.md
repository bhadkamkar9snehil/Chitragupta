# XStudio_Xbatch.dbo.LRF_Summary_Day

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference mtd, ytd, liquid, metal, weight, avg, calc, consumption, aluminium, argon, carbon, dolo.

**Primary Key:** ID  
**Row Count:** 1,430  
**Date Range (ModifiedOn):** 2025-10-14T08:31:04.2700000 to 2026-07-19T18:16:42.7670000  

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
| ReportDate | date | YES | — | — |
| ArgonConsumption | decimal | YES | 18,4 | — |
| HeatID | decimal | YES | 18,4 | — |
| PowerMWH | decimal | YES | 18,4 | — |
| PowerMWH_MTD | decimal | YES | 18,4 | — |
| HeatID_MTD | decimal | YES | 18,4 | — |
| ArgonConsumption_MTD | decimal | YES | 18,4 | — |
| PowerMWH_YTD | decimal | YES | 18,4 | — |
| HeatID_YTD | decimal | YES | 18,4 | — |
| ArgonConsumption_YTD | decimal | YES | 18,4 | — |
| SiMnn | decimal | YES | 18,4 | — |
| FeSi | decimal | YES | 18,4 | — |
| Dolo | decimal | YES | 18,4 | — |
| SiMn | decimal | YES | 18,4 | — |
| SiMnn_YTD | decimal | YES | 18,4 | — |
| SiMn_MTD | decimal | YES | 18,4 | — |
| Dolo_MTD | decimal | YES | 18,4 | — |
| FeSi_YTD | decimal | YES | 18,4 | — |
| FeSi_MTD | decimal | YES | 18,4 | — |
| SiMn_YTD | decimal | YES | 18,4 | — |
| Dolo_YTD | decimal | YES | 18,4 | — |
| SiMnn_MTD | decimal | YES | 18,4 | — |
| LiquidMetalWeight | decimal | YES | 18,4 | — |
| LiquidMetalWeight_YTD | decimal | YES | 18,4 | — |
| LiquidMetalWeight_MTD | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight_YTD | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight_MTD | decimal | YES | 18,4 | — |
| Lime | decimal | YES | 18,4 | — |
| Lime_YTD | decimal | YES | 18,4 | — |
| Lime_MTD | decimal | YES | 18,4 | — |
| Avg_CalcLiquidMetalWeight | decimal | YES | 18,4 | — |
| CalcLiquidMetalWeight | decimal | YES | 18,4 | — |
| Avg_CalcLiquidMetalWeight_YTD | decimal | YES | 18,4 | — |
| CalcLiquidMetalWeight_MTD | decimal | YES | 18,4 | — |
| CalcLiquidMetalWeight_YTD | decimal | YES | 18,4 | — |
| Avg_CalcLiquidMetalWeight_MTD | decimal | YES | 18,4 | — |
| TotalElectrodeConsumptionKg | decimal | YES | 18,4 | — |
| TotalElectrodeConsumptionKg_MTD | decimal | YES | 18,4 | — |
| TotalElectrodeConsumptionKg_YTD | decimal | YES | 18,4 | — |
| Aluminium | decimal | YES | 18,4 | — |
| Carbon | decimal | YES | 18,4 | — |
| Aluminium_YTD | decimal | YES | 18,4 | — |
| Carbon_MTD | decimal | YES | 18,4 | — |
| Aluminium_MTD | decimal | YES | 18,4 | — |
| Carbon_YTD | decimal | YES | 18,4 | — |
| FlourSpar | decimal | YES | 18,4 | — |
| FlourSpar_YTD | decimal | YES | 18,4 | — |
| FlourSpar_MTD | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0020A7D3-A51F-4C04-9DBF-BBA36847A44E | NULL | NULL | NULL | NULL | 2025-11-06T11:57:39.6070000 | NULL | False | False | NULL |
| 022CB36C-3005-42D9-991E-DD6498C35FAF | NULL | NULL | NULL | NULL | 2026-05-21T13:00:32.3800000 | NULL | False | False | NULL |
| 022B1082-C79A-4FAF-8A9B-99685868F33E | NULL | NULL | NULL | NULL | 2026-01-16T16:52:06.5430000 | NULL | False | False | NULL |
| 0209E4D0-02F4-4976-B8B9-EBAF4E620FA7 | NULL | NULL | NULL | NULL | 2026-02-10T14:38:11.2230000 | NULL | False | False | NULL |
| 01E8395B-8059-4AA1-96ED-13B2F49E8948 | NULL | NULL | NULL | NULL | 2025-11-14T07:13:57.9070000 | NULL | False | False | NULL |
| 01E71AD7-F99E-4BF3-A6EE-6DEEB30CB08F | NULL | NULL | NULL | NULL | 2026-03-02T16:06:46.9570000 | NULL | False | False | NULL |
| 01C80168-4DAF-40B5-BCAF-D74F153EE096 | NULL | NULL | NULL | NULL | 2025-12-08T12:32:40.0270000 | NULL | False | False | NULL |
| 018416D6-CF52-4565-98A6-8A440E6E4D6C | NULL | NULL | NULL | NULL | 2026-05-10T04:02:29.7300000 | NULL | False | False | NULL |
| 016F3962-9F0C-4FFE-9988-E819EC3ABC35 | NULL | NULL | NULL | NULL | 2026-03-28T16:02:52.8500000 | NULL | False | False | NULL |
| 025D8B14-5C81-4C4E-9A2E-EABBA2AB5C6B | NULL | NULL | NULL | NULL | 2026-01-17T18:00:10.1070000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7155037D-B8CD-4805-8B6D-52582BBA42F3 | NULL | NULL | NULL | NULL | 2026-07-08T03:03:55.1130000 | 2026-07-19T18:16:42.7670000 | False | False | NULL |
| 852F8E88-997E-455C-9F1F-F7A708043794 | NULL | NULL | NULL | NULL | 2026-07-07T05:04:57.4500000 | 2026-07-19T18:16:35.9270000 | False | False | NULL |
| 6A7A483E-CE73-461D-BE37-C1B84A3382F6 | NULL | NULL | NULL | NULL | 2026-07-05T05:03:41.6030000 | 2026-07-17T17:19:47.9000000 | False | False | NULL |
| 78EC1AA7-00DA-42E2-B07A-E81B1C40A272 | NULL | NULL | NULL | NULL | 2026-07-06T05:14:23.3800000 | 2026-07-17T17:19:47.9000000 | False | False | NULL |
| 29ECD45D-9A61-40BC-B119-5917D5EAE754 | NULL | NULL | NULL | NULL | 2026-07-02T05:14:23.7430000 | 2026-07-17T17:19:47.8970000 | False | False | NULL |
| 30629FFC-69FC-4DA6-BEFB-28CA92C867F3 | NULL | NULL | NULL | NULL | 2026-07-04T05:03:13.5000000 | 2026-07-17T17:19:47.8970000 | False | False | NULL |
| B70EFA38-5B8C-414C-A4F6-17137EF7802D | NULL | NULL | NULL | NULL | 2026-07-03T02:07:19.6530000 | 2026-07-17T17:19:47.8970000 | False | False | NULL |
| 907DA3FB-3A78-4579-9738-F823860C83C4 | NULL | NULL | NULL | NULL | 2026-06-29T05:00:33.7700000 | 2026-07-17T17:19:47.8930000 | False | False | NULL |
| AE7BC7C7-F666-49CE-B365-CEF1BDAAFBAB | NULL | NULL | NULL | NULL | 2026-07-01T05:06:17.3330000 | 2026-07-17T17:19:47.8930000 | False | False | NULL |
| F08F2FC2-0C47-4988-B450-B41DCF546BED | NULL | NULL | NULL | NULL | 2026-06-30T04:57:26.7730000 | 2026-07-17T17:19:47.8930000 | False | False | NULL |

---
