# XStudio_Xbatch.dbo.SMS_EAF_Per_Heat_ChargeMix

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** data, eaf, flow, heat, insert, per (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference weight, charge, total, manual, eafhms, cuts, eafbriquettes, eafbundles, eafcopex, eafend, eafshredded, eafskull.

**Primary Key:** ID  
**Row Count:** 5,964  
**Date Range (ModifiedOn):** 2026-01-02T14:59:31.6600000 to 2026-08-10T09:48:31.1400000  

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
| EAFCopexScrapCharge1Weight | decimal | YES | 18,2 | — |
| EAFCopexScrapCharge2Weight | decimal | YES | 18,2 | — |
| EAFHMS1Charge1Weight | decimal | YES | 18,2 | — |
| EAFHMS1Charge2Weight | decimal | YES | 18,2 | — |
| EAFHMS12Charge1Weight | decimal | YES | 18,2 | — |
| EAFHMS12Charge2Weight | decimal | YES | 18,2 | — |
| EAFEndCutsCharge1Weight | decimal | YES | 18,2 | — |
| EAFEndCutsCharge2Weight | decimal | YES | 18,2 | — |
| EAFBriquettesCharge1Weight | decimal | YES | 18,2 | — |
| EAFBriquettesCharge2Weight | decimal | YES | 18,2 | — |
| EAFBundlesLMSCharge1Weight | decimal | YES | 18,2 | — |
| EAFBundlesLMSCharge2Weight | decimal | YES | 18,2 | — |
| EAFHBIDRICharge1Weight | decimal | YES | 18,2 | — |
| EAFHBIDRICharge2Weight | decimal | YES | 18,2 | — |
| EAFShreddedCharge1Weight | decimal | YES | 18,2 | — |
| EAFShreddedCharge2Weight | decimal | YES | 18,2 | — |
| EAFSkullCharge1Weight | decimal | YES | 18,2 | — |
| EAFSkullCharge2Weight | decimal | YES | 18,2 | — |
| EAFHeatNo | int | YES | 10,0 | — |
| EAFCopexScrapCharge1WeightManual | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge1WeightTotal | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge2WeightManual | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge2WeightTotal | decimal | YES | 18,4 | — |
| EAFHMS1Charge1WeightManual | decimal | YES | 18,4 | — |
| EAFHMS1Charge1WeightTotal | decimal | YES | 18,4 | — |
| EAFHMS1Charge2WeightMaual | decimal | YES | 18,4 | — |
| EAFHMS1Charge2WeightTotal | decimal | YES | 18,4 | — |
| EAFHMS12Charge1WeightManual | decimal | YES | 18,4 | — |
| EAFHMS12Charge1WeightTotal | decimal | YES | 18,4 | — |
| EAFHMS12Charge2WeightManual | decimal | YES | 18,4 | — |
| EAFHMS12Charge2WeightTotal | decimal | YES | 18,4 | — |
| EAFEndCutsCharge1WeightManual | decimal | YES | 18,4 | — |
| EAFEndCutsCharge1WeightTotal | decimal | YES | 18,4 | — |
| EAFEndCutsCharge2WeightManual | decimal | YES | 18,4 | — |
| EAFEndCutsCharge2WeightTotal | decimal | YES | 18,4 | — |
| EAFBriquettesCharge1WeightManual | decimal | YES | 18,4 | — |
| EAFBriquettesCharge1WeightTotal | decimal | YES | 18,4 | — |
| EAFBriquettesCharge2WeightManual | decimal | YES | 18,4 | — |
| EAFBriquettesCharge2WeightTotal | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge1WeightManual | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge1WeightTotal | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge2WeightManual | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge2WeightTotal | decimal | YES | 18,4 | — |
| EAFHBIDRICharge1WeightManual | decimal | YES | 18,4 | — |
| EAFHBIDRICharge1WeightTotal | decimal | YES | 18,4 | — |
| EAFHBIDRICharge2WeightManual | decimal | YES | 18,4 | — |
| EAFHBIDRICharge2WeightTotal | decimal | YES | 18,4 | — |
| EAFShreddedCharge1WeightManual | decimal | YES | 18,4 | — |
| EAFShreddedCharge1WeightTotal | decimal | YES | 18,4 | — |
| EAFShreddedCharge2WeightManual | decimal | YES | 18,4 | — |
| EAFShreddedCharge2WeightTotal | decimal | YES | 18,4 | — |
| EAFSkullCharge1WeightManual | decimal | YES | 18,4 | — |
| EAFSkullCharge1WeightTotal | decimal | YES | 18,4 | — |
| EAFSkullCharge2WeightManual | decimal | YES | 18,4 | — |
| EAFSkullCharge2WeightTotal | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge3Weight | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge3WeightManual | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge3WeightTotal | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge4WeightTotal | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge4WeightManual | decimal | YES | 18,4 | — |
| EAFCopexScrapCharge4Weight | decimal | YES | 18,4 | — |
| EAFHMS1Charge3Weight | decimal | YES | 18,4 | — |
| EAFHMS1Charge3WeightManaul | decimal | YES | 18,4 | — |
| EAFHMS1Charge3WeightTotal | decimal | YES | 18,4 | — |
| EAFHMS1Charge4WeightTotal | decimal | YES | 18,4 | — |
| EAFHMS1Charge4WeightManual | decimal | YES | 18,4 | — |
| EAFHMS1Charge4Weight | decimal | YES | 18,4 | — |
| EAFHMS12Charge3Weight | decimal | YES | 18,4 | — |
| EAFHMS12Charge3WeightManual | decimal | YES | 18,4 | — |
| EAFHMS12Charge3WeightTotal | decimal | YES | 18,4 | — |
| EAFHMS12Charge4WeightTotal | decimal | YES | 18,4 | — |
| EAFHMS12Charge4WeightManual | decimal | YES | 18,4 | — |
| EAFHMS12Charge4Weight | decimal | YES | 18,4 | — |
| EAFEndCutsCharge3Weight | decimal | YES | 18,4 | — |
| EAFEndCutsCharge3WeightManual | decimal | YES | 18,4 | — |
| EAFEndCutsCharge3WeightTotal | decimal | YES | 18,4 | — |
| EAFEndCutsCharge4WeightTotal | decimal | YES | 18,4 | — |
| EAFEndCutsCharge4WeightManual | decimal | YES | 18,4 | — |
| EAFEndCutsCharge4Weight | decimal | YES | 18,4 | — |
| EAFBriquettesCharge3Weight | decimal | YES | 18,4 | — |
| EAFBriquettesCharge3WeightManual | decimal | YES | 18,4 | — |
| EAFBriquettesCharge3WeightTotal | decimal | YES | 18,4 | — |
| EAFBriquettesCharge4WeightTotal | decimal | YES | 18,4 | — |
| EAFBriquettesCharge4WeightManual | decimal | YES | 18,4 | — |
| EAFBriquettesCharge4Weight | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge3Weight | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge3WeightManual | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge3WeightTotal | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge4WeightTotal | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge4Weight | decimal | YES | 18,4 | — |
| EAFBundlesLMSCharge4WeightManual | decimal | YES | 18,4 | — |
| EAFHBIDRICharge3Weight | decimal | YES | 18,4 | — |
| EAFHBIDRICharge3WeightManual | decimal | YES | 18,4 | — |
| EAFHBIDRICharge3WeightTotal | decimal | YES | 18,4 | — |
| EAFHBIDRICharge4WeightTotal | decimal | YES | 18,4 | — |
| EAFHBIDRICharge4Weight | decimal | YES | 18,4 | — |
| EAFHBIDRICharge4WeightManual | decimal | YES | 18,4 | — |
| EAFShreddedCharge3Weight | decimal | YES | 18,4 | — |
| EAFShreddedCharge3WeightManual | decimal | YES | 18,4 | — |
| EAFShreddedCharge3WeightTotal | decimal | YES | 18,4 | — |
| EAFShreddedCharge4WeightTotal | decimal | YES | 18,4 | — |
| EAFShreddedCharge4Weight | decimal | YES | 18,4 | — |
| EAFShreddedCharge4WeightManual | decimal | YES | 18,4 | — |
| EAFSkullCharge3Weight | decimal | YES | 18,4 | — |
| EAFSkullCharge3WeightManual | decimal | YES | 18,4 | — |
| EAFSkullCharge3WeightTotal | decimal | YES | 18,4 | — |
| EAFSkullCharge4WeightTotal | decimal | YES | 18,4 | — |
| EAFSkullCharge4WeightManual | decimal | YES | 18,4 | — |
| EAFSkullCharge4Weight | decimal | YES | 18,4 | — |
| EAFCopexScrapWeightAutoTotal | decimal | YES | 18,4 | — |
| EAFCopexScrapWeightManualTotal | decimal | YES | 18,4 | — |
| EAFHMS1WeightAutoTotal | decimal | YES | 18,4 | — |
| EAFHMS1WeightManualTotal | decimal | YES | 18,4 | — |
| EAFHMS12WeightAutoTotal | decimal | YES | 18,4 | — |
| EAFHMS12WeightManualTotal | decimal | YES | 18,4 | — |
| EAFEndCutsWeightAutoTotal | decimal | YES | 18,4 | — |
| EAFEndCutsWeightManualTotal | decimal | YES | 18,4 | — |
| EAFBriquettesWeightAutoTotal | decimal | YES | 18,4 | — |
| EAFBriquettesWeightManualTotal | decimal | YES | 18,4 | — |
| EAFHBIDRIWeightAutoTotal | decimal | YES | 18,4 | — |
| EAFHBIDRIWeightManualTotal | decimal | YES | 18,4 | — |
| EAFBundlesLMSWeightAutoTotal | decimal | YES | 18,4 | — |
| EAFBundlesLMSWeightManualTotal | decimal | YES | 18,4 | — |
| EAFShreddedWeightAutoTotal | decimal | YES | 18,4 | — |
| EAFShreddedWeightManualTotal | decimal | YES | 18,4 | — |
| EAFSkullWeightAutoTotal | decimal | YES | 18,4 | — |
| EAFSkullWeightManualTotal | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B413B029-7C31-4B08-A080-C2E3BA631176 | NULL | NULL | NULL | NULL | 2026-01-02T14:42:11.4470000 | 2026-01-02T14:59:31.6600000 | False | False | NULL |
| 8605ACAA-EFC0-40DB-B65B-BEF836AA2886 | NULL | NULL | NULL | NULL | 2026-01-02T15:01:55.6470000 | 2026-01-02T15:57:19.7770000 | False | False | NULL |
| 7A58A754-E206-4FA8-9895-6E70506714C9 | NULL | NULL | NULL | NULL | 2026-01-02T15:59:09.7970000 | 2026-01-02T16:58:11.5330000 | False | False | NULL |
| 6378C77E-0A05-44D1-B5F6-58FDD4374420 | NULL | NULL | NULL | NULL | 2026-01-02T17:00:01.4970000 | 2026-01-02T17:52:51.7330000 | False | False | NULL |
| D40734E6-3B93-44D8-A969-D15F855DD67A | NULL | NULL | NULL | NULL | 2026-01-02T17:54:40.8170000 | 2026-01-02T18:47:33.8470000 | False | False | NULL |
| FAFF6AB5-F4B2-41FF-9297-DDCF5DE58F1D | NULL | NULL | NULL | NULL | 2026-01-02T18:49:38.6000000 | 2026-01-02T19:50:36.5170000 | False | False | NULL |
| 8781E539-EC57-430E-99E0-EBE4D0F6A479 | NULL | NULL | NULL | NULL | 2026-01-02T19:52:39.7200000 | 2026-01-02T20:49:27.5670000 | False | False | NULL |
| A57F1573-73AF-43FE-9584-567F88FFFC33 | NULL | NULL | NULL | NULL | 2026-01-02T20:51:32.8970000 | 2026-01-02T21:47:09.7270000 | False | False | NULL |
| D3E3408E-6ED3-4CED-801F-87D950B401EE | NULL | NULL | NULL | NULL | 2026-01-02T21:49:08.4170000 | 2026-01-02T22:42:52.4200000 | False | False | NULL |
| FFF9DBD5-5148-4964-8FB2-8848E14791C0 | NULL | NULL | NULL | NULL | 2026-01-02T22:45:00.8070000 | 2026-01-02T23:37:27.6970000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B8E2723B-DDF5-4AC4-884C-39B34DF95203 | NULL | NULL | NULL | NULL | 2026-08-10T09:48:25.0470000 | 2026-08-10T09:48:31.1400000 | False | False | NULL |
| 032AF720-489E-44DC-8413-2E814206DC14 | NULL | NULL | NULL | NULL | 2026-08-09T11:28:16.6400000 | 2026-08-10T09:39:17.1070000 | False | False | NULL |
| 35774A41-102E-4851-88E1-DF8CF4247DB4 | NULL | NULL | NULL | NULL | 2026-08-09T11:24:41.8100000 | 2026-08-09T11:28:07.9900000 | False | False | NULL |
| CABC0D18-AA50-47EE-8F4F-AF2BB11F299C | NULL | NULL | NULL | NULL | 2026-08-09T11:22:19.9570000 | 2026-08-09T11:24:32.6230000 | False | False | NULL |
| D0D73B0F-2EBD-458B-980D-FF9DA4D057AB | NULL | NULL | NULL | NULL | 2026-08-09T11:22:10.7930000 | 2026-08-09T11:22:14.8470000 | False | False | NULL |
| 7B243FD7-1C71-4572-94F8-1295DEEFADBA | NULL | NULL | NULL | NULL | 2026-08-04T17:23:17.8470000 | 2026-08-09T11:21:59.5630000 | False | False | NULL |
| 980043F1-8348-49E6-8DC7-5171CDC71D22 | NULL | NULL | NULL | NULL | 2026-08-04T17:23:09.7270000 | 2026-08-04T17:23:14.7970000 | False | False | NULL |
| 34703154-986C-44C6-9E2E-D18CC80C42ED | NULL | NULL | NULL | NULL | 2026-08-04T17:11:30.9170000 | 2026-08-04T17:23:04.6300000 | False | False | NULL |
| BE44FB83-5B70-4DD8-AA4B-B9CB71C34112 | NULL | NULL | NULL | NULL | 2026-08-04T17:11:24.8130000 | 2026-08-04T17:11:26.8430000 | False | False | NULL |
| F7658B11-3505-4082-9F3C-DDCF5F82D0B6 | NULL | NULL | NULL | NULL | 2026-08-04T17:09:57.7000000 | 2026-08-04T17:10:42.0000000 | False | False | NULL |

---
