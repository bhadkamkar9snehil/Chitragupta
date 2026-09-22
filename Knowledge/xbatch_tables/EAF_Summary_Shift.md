# XStudio_Xbatch.dbo.EAF_Summary_Shift

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference hms, consumption, addition, avg, bundle, copex, cuts, end, ladle, scrap, scull, shreedded.

**Primary Key:** ID  
**Row Count:** 6,510  
**Date Range (ModifiedOn):** 2025-07-14T17:10:32.8300000 to 2026-07-19T18:16:42.6700000  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| ShiftName | varchar | YES | 100 | — |
| ChargeWeight | decimal | YES | 18,4 | — |
| PowerOnTimeMinute | decimal | YES | 18,4 | — |
| HeatID | decimal | YES | 18,4 | — |
| ScullCH1 | decimal | YES | 18,4 | — |
| ShreeddedCH2 | decimal | YES | 18,4 | — |
| HMS12CH2 | decimal | YES | 18,4 | — |
| CopexScrapCH2 | decimal | YES | 18,4 | — |
| EndCutsCH1 | decimal | YES | 18,4 | — |
| BundleLMSCH1 | decimal | YES | 18,4 | — |
| HBIDRICH2 | decimal | YES | 18,4 | — |
| HMS1CH1 | decimal | YES | 18,4 | — |
| BriquetteCH1 | decimal | YES | 18,4 | — |
| BundleLMSCH2 | decimal | YES | 18,4 | — |
| EndCutsCH2 | decimal | YES | 18,4 | — |
| NGConsumption | decimal | YES | 18,4 | — |
| BriquetteCH2 | decimal | YES | 18,4 | — |
| ShreeddedCH1 | decimal | YES | 18,4 | — |
| OxygenConsumption | decimal | YES | 18,4 | — |
| PowerMWH | decimal | YES | 18,4 | — |
| HBIDRICH1 | decimal | YES | 18,4 | — |
| CopexScrapCH1 | decimal | YES | 18,4 | — |
| ScullCH2 | decimal | YES | 18,4 | — |
| HMS12CH1 | decimal | YES | 18,4 | — |
| HMS1CH2 | decimal | YES | 18,4 | — |
| BIN4Consumption | decimal | YES | 18,4 | — |
| BIN2DoloConsumption | decimal | YES | 18,4 | — |
| BIN1LimeConsumption | decimal | YES | 18,4 | — |
| BIN3Consumption | decimal | YES | 18,4 | — |
| LiquidMetalWeight | decimal | YES | 18,4 | — |
| TotalChargeWeightMT | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight | decimal | YES | 18,4 | — |
| LadleAdditionSiMn | decimal | YES | 18,4 | — |
| LadleAdditionDolo | decimal | YES | 18,4 | — |
| CarbonConsumption | decimal | YES | 18,4 | — |
| LadleAdditionFeSi | decimal | YES | 18,4 | — |
| LadleAdditionSiMnn | decimal | YES | 18,4 | — |
| LadleAdditionLime | decimal | YES | 18,4 | — |
| YieldPerHeat | decimal | YES | 18,4 | — |
| Avg_PowerMW | decimal | YES | 18,4 | — |
| Avg_PoweroffTIme | decimal | YES | 18,4 | — |
| Avg_PoweronTIme | decimal | YES | 18,4 | — |
| Avg_TTT | decimal | YES | 18,4 | — |
| TotalElectrodeConsumption | decimal | YES | 18,4 | — |
| NutCokeKgPerTon | decimal | YES | 18,4 | — |
| ScullCH4 | decimal | YES | 18,4 | — |
| EndCutsCH4 | decimal | YES | 18,4 | — |
| HMS12CH4 | decimal | YES | 18,4 | — |
| EndCuts | decimal | YES | 18,4 | — |
| BundleLMSCH4 | decimal | YES | 18,4 | — |
| EndCutsCH3 | decimal | YES | 18,4 | — |
| HBIConsumption | decimal | YES | 18,4 | — |
| BundleLMSCH3 | decimal | YES | 18,4 | — |
| HMS1CH3 | decimal | YES | 18,4 | — |
| ShreeddedCH4 | decimal | YES | 18,4 | — |
| ScullCH3 | decimal | YES | 18,4 | — |
| CopexScrapCH4 | decimal | YES | 18,4 | — |
| CopexScrapCH3 | decimal | YES | 18,4 | — |
| HMS1CH4 | decimal | YES | 18,4 | — |
| CdriConsumption | decimal | YES | 18,4 | — |
| ShreeddedCH3 | decimal | YES | 18,4 | — |
| HMS12CH3 | decimal | YES | 18,4 | — |
| HMS12 | decimal | YES | 18,4 | — |
| HMS1 | decimal | YES | 18,4 | — |
| Scull | decimal | YES | 18,4 | — |
| Shreedded | decimal | YES | 18,4 | — |
| CopexScrap | decimal | YES | 18,4 | — |
| BundleLMS | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0039E57C-02C7-40D6-8055-9D368B603DD8 | NULL | NULL | NULL | NULL | 2025-12-22T01:27:01.5870000 | NULL | False | False | NULL |
| 0039511F-2B0C-42BD-9369-7348C8F998A5 | NULL | NULL | NULL | NULL | 2026-02-14T00:02:11.1230000 | NULL | False | False | NULL |
| 00244389-FFBF-4F3C-AF3E-FDEDCDFE57F4 | NULL | NULL | NULL | NULL | 2025-10-15T03:16:12.8330000 | NULL | False | False | NULL |
| 001CB552-4FD2-45A0-8615-E229162D9B50 | NULL | NULL | NULL | NULL | 2026-04-11T02:17:57.4030000 | NULL | False | False | NULL |
| 00820E85-9F64-43A0-879F-3AE8E5FAEDA4 | NULL | NULL | NULL | NULL | 2026-02-01T07:23:40.2300000 | NULL | False | False | NULL |
| 006C35A1-F8EE-4039-B0B7-2AE01E74224F | NULL | NULL | NULL | NULL | 2025-12-24T05:55:16.8570000 | NULL | False | False | NULL |
| 006112DA-2204-4DA3-942B-5AD84EB4A938 | NULL | NULL | NULL | NULL | 2026-06-19T05:59:18.6400000 | NULL | False | False | NULL |
| 00557DAD-88E8-4942-B641-34A496492C13 | NULL | NULL | NULL | NULL | 2025-11-15T07:19:47.3600000 | NULL | False | False | NULL |
| 004F4255-12A8-4443-814D-0E18C75996B3 | NULL | NULL | NULL | NULL | 2026-01-13T20:00:55.8630000 | NULL | False | False | NULL |
| 004F1B26-9440-4AC5-98A1-468DF283096B | NULL | NULL | NULL | NULL | 2026-04-14T03:07:07.8530000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21482E81-06D9-4658-B342-37562F239F34 | NULL | NULL | NULL | NULL | 2026-07-08T02:55:34.6630000 | 2026-07-19T18:16:42.6700000 | False | False | NULL |
| 5CE21F6F-CB86-4C4E-8740-D1703292B854 | NULL | NULL | NULL | NULL | 2026-07-07T05:00:27.1570000 | 2026-07-19T18:16:35.8500000 | False | False | NULL |
| 7CAFB617-240F-45C1-8495-0AC85FC57E07 | NULL | NULL | NULL | NULL | 2026-02-21T01:42:20.0370000 | 2026-07-17T17:19:46.7700000 | False | False | NULL |
| E3070447-DE3B-4343-B07A-109C4ABEEFB1 | NULL | NULL | NULL | NULL | 2026-02-22T01:27:00.2500000 | 2026-07-17T17:19:42.6400000 | False | False | NULL |
| 8565447A-BA19-4E93-8E21-839C512855DA | NULL | NULL | NULL | NULL | 2026-02-20T01:52:52.2370000 | 2026-07-17T17:19:39.8570000 | False | False | NULL |
| 97A97604-9B49-4C3F-9282-3ED0AB196598 | NULL | NULL | NULL | NULL | 2026-02-18T01:52:53.5600000 | 2026-07-17T17:19:29.8730000 | False | False | NULL |
| 1E7E25A7-F76A-4253-9370-2A768938E36A | NULL | NULL | NULL | NULL | 2026-02-24T01:39:35.5900000 | 2026-07-17T17:19:29.7000000 | False | False | NULL |
| 3FD2F01F-73A2-4957-A83C-81E72AA9151D | NULL | NULL | NULL | NULL | 2026-02-23T01:39:49.8630000 | 2026-07-17T17:19:26.9430000 | False | False | NULL |
| C68EC829-8673-458A-8A34-0EBD4514F542 | NULL | NULL | NULL | NULL | 2026-02-19T01:06:18.3170000 | 2026-07-17T17:19:26.1600000 | False | False | NULL |
| 32E97764-B434-4841-9CD2-121DEA2BF43B | NULL | NULL | NULL | NULL | 2026-02-17T01:08:51.2500000 | 2026-07-17T17:19:04.4130000 | False | False | NULL |

---
