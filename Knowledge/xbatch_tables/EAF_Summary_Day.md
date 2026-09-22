# XStudio_Xbatch.dbo.EAF_Summary_Day

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference mtd, ytd, hms, consumption, addition, avg, bundle, copex, cuts, end, ladle, scrap.

**Primary Key:** ID  
**Row Count:** 6,377  
**Date Range (ModifiedOn):** 2026-02-21T10:37:58.8230000 to 2026-07-19T18:16:42.7100000  

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
| HeatID | decimal | YES | 18,4 | — |
| PowerOnTimeMinute | decimal | YES | 18,4 | — |
| ChargeWeight | decimal | YES | 18,4 | — |
| ScullCH1 | decimal | YES | 18,4 | — |
| BundleLMSCH1 | decimal | YES | 18,4 | — |
| EndCutsCH2 | decimal | YES | 18,4 | — |
| HBIDRICH2 | decimal | YES | 18,4 | — |
| HMS1CH1 | decimal | YES | 18,4 | — |
| PowerMWH | decimal | YES | 18,4 | — |
| BriquetteCH1 | decimal | YES | 18,4 | — |
| NGConsumption | decimal | YES | 18,4 | — |
| CopexScrapCH1 | decimal | YES | 18,4 | — |
| HMS12CH2 | decimal | YES | 18,4 | — |
| HBIDRICH1 | decimal | YES | 18,4 | — |
| BriquetteCH2 | decimal | YES | 18,4 | — |
| HMS12CH1 | decimal | YES | 18,4 | — |
| ScullCH2 | decimal | YES | 18,4 | — |
| ShreeddedCH2 | decimal | YES | 18,4 | — |
| BundleLMSCH2 | decimal | YES | 18,4 | — |
| ShreeddedCH1 | decimal | YES | 18,4 | — |
| OxygenConsumption | decimal | YES | 18,4 | — |
| CopexScrapCH2 | decimal | YES | 18,4 | — |
| EndCutsCH1 | decimal | YES | 18,4 | — |
| HMS1CH2 | decimal | YES | 18,4 | — |
| PowerOnTimeMinute_MTD | decimal | YES | 18,4 | — |
| ShreeddedCH2_YTD | decimal | YES | 18,4 | — |
| HBIDRICH1_YTD | decimal | YES | 18,4 | — |
| EndCutsCH1_MTD | decimal | YES | 18,4 | — |
| PowerMWH_YTD | decimal | YES | 18,4 | — |
| NGConsumption_MTD | decimal | YES | 18,4 | — |
| CopexScrapCH1_YTD | decimal | YES | 18,4 | — |
| BundleLMSCH1_MTD | decimal | YES | 18,4 | — |
| ShreeddedCH1_MTD | decimal | YES | 18,4 | — |
| HMS12CH2_MTD | decimal | YES | 18,4 | — |
| HMS1CH1_MTD | decimal | YES | 18,4 | — |
| EndCutsCH1_YTD | decimal | YES | 18,4 | — |
| CopexScrapCH2_YTD | decimal | YES | 18,4 | — |
| OxygenConsumption_YTD | decimal | YES | 18,4 | — |
| ShreeddedCH1_YTD | decimal | YES | 18,4 | — |
| ScullCH1_MTD | decimal | YES | 18,4 | — |
| CopexScrapCH1_MTD | decimal | YES | 18,4 | — |
| HBIDRICH2_YTD | decimal | YES | 18,4 | — |
| BriquetteCH2_YTD | decimal | YES | 18,4 | — |
| HBIDRICH1_MTD | decimal | YES | 18,4 | — |
| ChargeWeight_YTD | decimal | YES | 18,4 | — |
| EndCutsCH2_MTD | decimal | YES | 18,4 | — |
| HMS1CH2_MTD | decimal | YES | 18,4 | — |
| BriquetteCH1_MTD | decimal | YES | 18,4 | — |
| BriquetteCH1_YTD | decimal | YES | 18,4 | — |
| BundleLMSCH2_YTD | decimal | YES | 18,4 | — |
| HMS12CH2_YTD | decimal | YES | 18,4 | — |
| ChargeWeight_MTD | decimal | YES | 18,4 | — |
| BundleLMSCH2_MTD | decimal | YES | 18,4 | — |
| HMS12CH1_YTD | decimal | YES | 18,4 | — |
| ShreeddedCH2_MTD | decimal | YES | 18,4 | — |
| BriquetteCH2_MTD | decimal | YES | 18,4 | — |
| PowerOnTimeMinute_YTD | decimal | YES | 18,4 | — |
| ScullCH2_YTD | decimal | YES | 18,4 | — |
| HeatID_MTD | decimal | YES | 18,4 | — |
| BundleLMSCH1_YTD | decimal | YES | 18,4 | — |
| PowerMWH_MTD | decimal | YES | 18,4 | — |
| HeatID_YTD | decimal | YES | 18,4 | — |
| NGConsumption_YTD | decimal | YES | 18,4 | — |
| HMS12CH1_MTD | decimal | YES | 18,4 | — |
| HMS1CH1_YTD | decimal | YES | 18,4 | — |
| ScullCH2_MTD | decimal | YES | 18,4 | — |
| CopexScrapCH2_MTD | decimal | YES | 18,4 | — |
| HMS1CH2_YTD | decimal | YES | 18,4 | — |
| HBIDRICH2_MTD | decimal | YES | 18,4 | — |
| OxygenConsumption_MTD | decimal | YES | 18,4 | — |
| ScullCH1_YTD | decimal | YES | 18,4 | — |
| EndCutsCH2_YTD | decimal | YES | 18,4 | — |
| BIN2DoloConsumption | decimal | YES | 18,4 | — |
| BIN3Consumption | decimal | YES | 18,4 | — |
| BIN4Consumption | decimal | YES | 18,4 | — |
| BIN1LimeConsumption | decimal | YES | 18,4 | — |
| BIN2DoloConsumption_MTD | decimal | YES | 18,4 | — |
| BIN4Consumption_YTD | decimal | YES | 18,4 | — |
| BIN4Consumption_MTD | decimal | YES | 18,4 | — |
| BIN3Consumption_YTD | decimal | YES | 18,4 | — |
| BIN1LimeConsumption_MTD | decimal | YES | 18,4 | — |
| BIN3Consumption_MTD | decimal | YES | 18,4 | — |
| BIN2DoloConsumption_YTD | decimal | YES | 18,4 | — |
| BIN1LimeConsumption_YTD | decimal | YES | 18,4 | — |
| LiquidMetalWeight | decimal | YES | 18,4 | — |
| LiquidMetalWeight_YD | decimal | YES | 18,4 | — |
| LiquidMetalWeight_YTD | decimal | YES | 18,4 | — |
| LiquidMetalWeight_MTD | decimal | YES | 18,4 | — |
| TotalChargeWeightMT | decimal | YES | 18,4 | — |
| TotalChargeWeightMT_MTD | decimal | YES | 18,4 | — |
| TotalChargeWeightMT_YTD | decimal | YES | 18,4 | — |
| TotalChargeWeightMT_YD | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight_YTD | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight_MTD | decimal | YES | 18,4 | — |
| CarbonConsumption | decimal | YES | 18,4 | — |
| LadleAdditionDolo | decimal | YES | 18,4 | — |
| LadleAdditionSiMn | decimal | YES | 18,4 | — |
| LadleAdditionLime | decimal | YES | 18,4 | — |
| LadleAdditionSiMnn | decimal | YES | 18,4 | — |
| LadleAdditionFeSi | decimal | YES | 18,4 | — |
| LadleAdditionFeSi_YTD | decimal | YES | 18,4 | — |
| LadleAdditionSiMn_MTD | decimal | YES | 18,4 | — |
| LadleAdditionFeSi_MTD | decimal | YES | 18,4 | — |
| LadleAdditionSiMnn_YTD | decimal | YES | 18,4 | — |
| LadleAdditionSiMn_YTD | decimal | YES | 18,4 | — |
| LadleAdditionLime_MTD | decimal | YES | 18,4 | — |
| LadleAdditionDolo_YTD | decimal | YES | 18,4 | — |
| CarbonConsumption_MTD | decimal | YES | 18,4 | — |
| CarbonConsumption_YTD | decimal | YES | 18,4 | — |
| LadleAdditionLime_YTD | decimal | YES | 18,4 | — |
| LadleAdditionSiMnn_MTD | decimal | YES | 18,4 | — |
| LadleAdditionDolo_MTD | decimal | YES | 18,4 | — |
| YieldPerHeat | decimal | YES | 18,4 | — |
| YieldPerHeat_MTD | decimal | YES | 18,4 | — |
| YieldPerHeat_YTD | decimal | YES | 18,4 | — |
| Avg_PoweronTIme | decimal | YES | 18,4 | — |
| Avg_TTT | decimal | YES | 18,4 | — |
| Avg_PowerMW | decimal | YES | 18,4 | — |
| Avg_PoweroffTIme | decimal | YES | 18,4 | — |
| Avg_TTT_YTD | decimal | YES | 18,4 | — |
| Avg_PowerMW_YTD | decimal | YES | 18,4 | — |
| Avg_PoweroffTIme_YTD | decimal | YES | 18,4 | — |
| Avg_TTT_MTD | decimal | YES | 18,4 | — |
| Avg_PowerMW_MTD | decimal | YES | 18,4 | — |
| Avg_PoweronTIme_MTD | decimal | YES | 18,4 | — |
| Avg_PoweroffTIme_MTD | decimal | YES | 18,4 | — |
| Avg_PoweronTIme_YTD | decimal | YES | 18,4 | — |
| TotalElectrodeConsumption | decimal | YES | 18,4 | — |
| TotalElectrodeConsumption_YTD | decimal | YES | 18,4 | — |
| TotalElectrodeConsumption_MTD | decimal | YES | 18,4 | — |
| NutCokeKgPerTon | decimal | YES | 18,4 | — |
| NutCokeKgPerTon_YTD | decimal | YES | 18,4 | — |
| NutCokeKgPerTon_MTD | decimal | YES | 18,4 | — |
| BundleLMSCH3 | decimal | YES | 18,4 | — |
| CopexScrapCH3 | decimal | YES | 18,4 | — |
| HMS1CH4 | decimal | YES | 18,4 | — |
| HBIConsumption | decimal | YES | 18,4 | — |
| BundleLMSCH4 | decimal | YES | 18,4 | — |
| ScullCH4 | decimal | YES | 18,4 | — |
| EndCutsCH3 | decimal | YES | 18,4 | — |
| ShreeddedCH4 | decimal | YES | 18,4 | — |
| HMS12CH3 | decimal | YES | 18,4 | — |
| HMS1CH3 | decimal | YES | 18,4 | — |
| CopexScrapCH4 | decimal | YES | 18,4 | — |
| ShreeddedCH3 | decimal | YES | 18,4 | — |
| CdriConsumption | decimal | YES | 18,4 | — |
| HMS12CH4 | decimal | YES | 18,4 | — |
| ScullCH3 | decimal | YES | 18,4 | — |
| EndCutsCH4 | decimal | YES | 18,4 | — |
| EndCuts | decimal | YES | 18,4 | — |
| BundleLMSCH4_MTD | decimal | YES | 18,4 | — |
| HMS12CH4_YTD | decimal | YES | 18,4 | — |
| ShreeddedCH4_YTD | decimal | YES | 18,4 | — |
| EndCuts_MTD | decimal | YES | 18,4 | — |
| CdriConsumption_YTD | decimal | YES | 18,4 | — |
| BundleLMSCH4_YTD | decimal | YES | 18,4 | — |
| BundleLMSCH3_MTD | decimal | YES | 18,4 | — |
| ScullCH3_YTD | decimal | YES | 18,4 | — |
| HMS1CH4_MTD | decimal | YES | 18,4 | — |
| ShreeddedCH3_YTD | decimal | YES | 18,4 | — |
| ScullCH4_YTD | decimal | YES | 18,4 | — |
| CopexScrapCH4_MTD | decimal | YES | 18,4 | — |
| CdriConsumption_MTD | decimal | YES | 18,4 | — |
| ScullCH3_MTD | decimal | YES | 18,4 | — |
| ShreeddedCH3_MTD | decimal | YES | 18,4 | — |
| EndCutsCH3_YTD | decimal | YES | 18,4 | — |
| HMS1CH3_MTD | decimal | YES | 18,4 | — |
| EndCutsCH4_YTD | decimal | YES | 18,4 | — |
| HMS12CH3_YTD | decimal | YES | 18,4 | — |
| HMS12CH4_MTD | decimal | YES | 18,4 | — |
| CopexScrapCH4_YTD | decimal | YES | 18,4 | — |
| EndCuts_YTD | decimal | YES | 18,4 | — |
| HMS1CH3_YTD | decimal | YES | 18,4 | — |
| CopexScrapCH3_MTD | decimal | YES | 18,4 | — |
| HMS12CH3_MTD | decimal | YES | 18,4 | — |
| EndCutsCH3_MTD | decimal | YES | 18,4 | — |
| ScullCH4_MTD | decimal | YES | 18,4 | — |
| HMS1CH4_YTD | decimal | YES | 18,4 | — |
| EndCutsCH4_MTD | decimal | YES | 18,4 | — |
| HBIConsumption_MTD | decimal | YES | 18,4 | — |
| HBIConsumption_YTD | decimal | YES | 18,4 | — |
| BundleLMSCH3_YTD | decimal | YES | 18,4 | — |
| CopexScrapCH3_YTD | decimal | YES | 18,4 | — |
| ShreeddedCH4_MTD | decimal | YES | 18,4 | — |
| CopexScrap | decimal | YES | 18,4 | — |
| HMS1 | decimal | YES | 18,4 | — |
| BundleLMS | decimal | YES | 18,4 | — |
| Shreedded | decimal | YES | 18,4 | — |
| HMS12 | decimal | YES | 18,4 | — |
| Scull | decimal | YES | 18,4 | — |
| CopexScrap_YTD | decimal | YES | 18,4 | — |
| Shreedded_YTD | decimal | YES | 18,4 | — |
| BundleLMS_YTD | decimal | YES | 18,4 | — |
| HMS1_YTD | decimal | YES | 18,4 | — |
| CopexScrap_MTD | decimal | YES | 18,4 | — |
| HMS12_MTD | decimal | YES | 18,4 | — |
| HMS12_YTD | decimal | YES | 18,4 | — |
| BundleLMS_MTD | decimal | YES | 18,4 | — |
| HMS1_MTD | decimal | YES | 18,4 | — |
| Shreedded_MTD | decimal | YES | 18,4 | — |
| Scull_YTD | decimal | YES | 18,4 | — |
| Scull_MTD | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00424009-A33E-48F3-8D7E-CC3A2EFEC997 | NULL | NULL | NULL | NULL | 2026-06-26T18:16:53.6900000 | NULL | False | False | NULL |
| 003E07AE-51C9-4A9E-8B69-D9C7936AEC47 | NULL | NULL | NULL | NULL | 2025-10-29T20:16:15.1630000 | NULL | False | False | NULL |
| 003CEA63-06B4-4E36-9E8B-B21C7793464C | NULL | NULL | NULL | NULL | 2026-06-23T08:49:01.3100000 | NULL | False | False | NULL |
| 0037F289-5C0C-49CC-BB19-7AC184721D13 | NULL | NULL | NULL | NULL | 2025-12-31T08:36:18.5170000 | NULL | False | False | NULL |
| 002F3441-FD78-4FFE-B234-6750D62A84D7 | NULL | NULL | NULL | NULL | 2026-02-13T06:42:27.8130000 | NULL | False | False | NULL |
| 002C16E8-C2A5-459E-A83F-5375D157DC9A | NULL | NULL | NULL | NULL | 2026-02-09T13:55:15.0470000 | NULL | False | False | NULL |
| 001E1CDE-3D6B-408E-A0DD-ACE0A5A4AC4D | NULL | NULL | NULL | NULL | 2025-12-07T07:15:38.7900000 | NULL | False | False | NULL |
| 001CF88F-93C8-4128-A5B5-4AFD83C022DC | NULL | NULL | NULL | NULL | 2025-12-21T01:19:21.2200000 | NULL | False | False | NULL |
| 001174B7-0D75-4B2B-B392-F77A976659DA | NULL | NULL | NULL | NULL | 2026-02-24T06:02:04.1830000 | NULL | False | False | NULL |
| 000B9376-82BA-4225-9128-30D843542D5A | NULL | NULL | NULL | NULL | 2025-10-17T23:00:51.7070000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16BA3666-3CD8-4380-AD04-AE367ECC8C8D | NULL | NULL | NULL | NULL | 2026-07-08T02:55:34.7700000 | 2026-07-19T18:16:42.7100000 | False | False | NULL |
| 48C25EA1-55AA-43C1-9E12-61E9BE445232 | NULL | NULL | NULL | NULL | 2026-07-07T05:00:27.2500000 | 2026-07-19T18:16:35.8930000 | False | False | NULL |
| 3373F597-A291-4741-A12E-69C20FF9F791 | NULL | NULL | NULL | NULL | 2026-07-06T05:08:13.0830000 | 2026-07-17T17:19:47.7030000 | False | False | NULL |
| 50E1B71F-AEEF-4321-A3E9-EEB9993A71AD | NULL | NULL | NULL | NULL | 2026-07-05T04:56:11.1630000 | 2026-07-17T17:19:47.6970000 | False | False | NULL |
| A39AFA94-3A91-4227-A7E5-5D3EF2A7A2F9 | NULL | NULL | NULL | NULL | 2026-07-04T04:58:03.1000000 | 2026-07-17T17:19:47.6900000 | False | False | NULL |
| 18171F1B-1A63-4360-A430-84A3925C73E4 | NULL | NULL | NULL | NULL | 2026-07-03T02:01:19.2130000 | 2026-07-17T17:19:47.6830000 | False | False | NULL |
| DAD9B039-1DC9-4B6D-9647-BB2C344CFFE9 | NULL | NULL | NULL | NULL | 2026-07-02T05:07:13.3800000 | 2026-07-17T17:19:47.6670000 | False | False | NULL |
| 1051750C-83E5-416F-9E12-737EFDF946B6 | NULL | NULL | NULL | NULL | 2026-07-01T04:58:47.0000000 | 2026-07-17T17:19:47.6530000 | False | False | NULL |
| 63DBF375-C072-4021-94ED-69467B55A582 | NULL | NULL | NULL | NULL | 2026-06-30T04:52:46.5000000 | 2026-07-17T17:19:47.6470000 | False | False | NULL |
| 234E1E59-86A0-4218-9B41-99A0B8320D49 | NULL | NULL | NULL | NULL | 2026-06-29T04:55:03.2530000 | 2026-07-17T17:19:47.6430000 | False | False | NULL |

---
