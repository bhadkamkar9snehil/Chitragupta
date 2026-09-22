# XStudio_Xbatch.dbo.XMES_RM_Production_Summary

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ton, cobble, billet, pct, waterm, hot, min, pcs, process, tons, actual, campaign.

**Primary Key:** ID  
**Row Count:** 7  

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
| IsProcessed | bit | YES | — | — |
| Product | varchar | YES | 100 | — |
| Section | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |
| AvgBilletWt | decimal | YES | 18,4 | — |
| ActualWeightTon | varchar | YES | 100 | — |
| PrimeProduction | varchar | YES | 100 | — |
| ShortLengthGeneration | decimal | YES | 18,4 | — |
| HoldBundlesWtTon | decimal | YES | 18,4 | — |
| Rejections | decimal | YES | 18,4 | — |
| DayProduction | decimal | YES | 18,4 | — |
| CobblePcs | int | YES | 10,0 | — |
| CobbleBilletWt | decimal | YES | 18,4 | — |
| HotOutPcs | int | YES | 10,0 | — |
| HotOutBilletWt | decimal | YES | 18,4 | — |
| RolledBilletPcs | int | YES | 10,0 | — |
| RolledBilletWTMT | decimal | YES | 18,4 | — |
| BilletConsumed | decimal | YES | 18,4 | — |
| TotalDischargeTon | decimal | YES | 18,4 | — |
| yield | decimal | YES | 18,4 | — |
| ActualYieldPCT | decimal | YES | 18,4 | — |
| NGNm3 | decimal | YES | 18,4 | — |
| NGMMBTU | decimal | YES | 18,4 | — |
| PowerKWH | decimal | YES | 18,4 | — |
| ProcessWaterm3 | decimal | YES | 18,4 | — |
| PortableWaterm3 | decimal | YES | 18,4 | — |
| NGTarget | decimal | YES | 18,4 | — |
| NGMMBTUTon | decimal | YES | 18,4 | — |
| PowerTarget | decimal | YES | 18,4 | — |
| PowerKWHTon | decimal | YES | 18,4 | — |
| ProcessWaterm3Ton | decimal | YES | 18,4 | — |
| PortableWaterm3Ton | decimal | YES | 18,4 | — |
| NoofCobblePCs | decimal | YES | 18,4 | — |
| Column103 | varchar | YES | 100 | — |
| Column102 | varchar | YES | 100 | — |
| greaterthan12mCutlength | int | YES | 10,0 | — |
| LessThan12mCutlength | int | YES | 10,0 | — |
| m16 | decimal | YES | 18,4 | — |
| m155 | decimal | YES | 18,4 | — |
| m15 | decimal | YES | 18,4 | — |
| m145 | decimal | YES | 18,4 | — |
| m14 | decimal | YES | 18,4 | — |
| m135 | decimal | YES | 18,4 | — |
| m13 | decimal | YES | 18,4 | — |
| m12 | decimal | YES | 18,4 | — |
| m115 | decimal | YES | 18,4 | — |
| m11 | decimal | YES | 18,4 | — |
| m105 | decimal | YES | 18,4 | — |
| m10 | decimal | YES | 18,4 | — |
| m95 | decimal | YES | 18,4 | — |
| m9 | decimal | YES | 18,4 | — |
| m85 | decimal | YES | 18,4 | — |
| m8 | decimal | YES | 18,4 | — |
| CampaignDate | date | YES | — | — |
| CampaignId | varchar | YES | 100 | — |
| CampaignNo | int | YES | 10,0 | — |
| TargetTons | decimal | YES | 18,4 | — |
| RatedTons | decimal | YES | 18,4 | — |
| OEE | decimal | YES | 18,4 | — |
| QualityRatio | decimal | YES | 18,4 | — |
| PerformanceRate | decimal | YES | 18,4 | — |
| ActualRollingRate | decimal | YES | 18,4 | — |
| RatedRollingRate | decimal | YES | 18,4 | — |
| AvailabilityPCT | decimal | YES | 18,4 | — |
| HotHoursMins | decimal | YES | 18,4 | — |
| Quality | decimal | YES | 18,4 | — |
| SMS | decimal | YES | 18,4 | — |
| PPC | decimal | YES | 18,4 | — |
| DispatchAndLogistics | decimal | YES | 18,4 | — |
| Crane | decimal | YES | 18,4 | — |
| Utility | decimal | YES | 18,4 | — |
| RollShop | int | YES | 10,0 | — |
| Electrical | int | YES | 10,0 | — |
| Mechanical | int | YES | 10,0 | — |
| Operation | int | YES | 10,0 | — |
| Unplanned | int | YES | 10,0 | — |
| NewSizeOrGradeDevelopment | int | YES | 10,0 | — |
| ProcessDelay | int | YES | 10,0 | — |
| StandOrPassChange | int | YES | 10,0 | — |
| SectionChange | int | YES | 10,0 | — |
| Planned | int | YES | 10,0 | — |
| Availability | int | YES | 10,0 | — |
| PlannedShutdown | int | YES | 10,0 | — |
| CalTime | decimal | YES | 18,4 | — |
| AvlPCT | decimal | YES | 18,4 | — |
| WirerodSize | varchar | YES | 100 | — |
| SPWirerodConsKGPerCoil | decimal | YES | 18,4 | — |
| WireRodCons | decimal | YES | 18,4 | — |
| TrimmingAndShearLoss | varchar | YES | 100 | — |
| EndCutPCT | varchar | YES | 100 | — |
| EndCutTon | varchar | YES | 100 | — |
| MillScale12PCT | decimal | YES | 18,4 | — |
| ENDCutTons | decimal | YES | 18,4 | — |
| CobbleTons | decimal | YES | 18,4 | — |
| HotChargingPCT | decimal | YES | 18,4 | — |
| HotChargingTon | decimal | YES | 18,4 | — |
| AvgSCTimeMinOrSC | decimal | YES | 18,4 | — |
| SCTimeMin | decimal | YES | 18,4 | — |
| NoofSCn | int | YES | 10,0 | — |
| CobbleRetensionTimeMinOrCobble | decimal | YES | 18,4 | — |
| CobbleTimeMin | decimal | YES | 18,4 | — |
| PortableWaterm3OrTon | decimal | YES | 18,4 | — |
| ProcessWaterm3OrTon | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FC01634E-A59A-4060-BAAB-0655EB0D619E | NULL | NULL | NULL | NULL | 2026-09-01T16:32:53.3800000 | NULL | False | False | NULL |
| D923426F-0B97-4F4A-894F-EE9E426BFF97 | NULL | NULL | NULL | NULL | 2026-09-01T16:33:02.8600000 | NULL | False | False | NULL |
| A1AE77D4-829E-4687-AE4F-9BDE0A441520 | NULL | NULL | NULL | NULL | 2026-09-01T16:35:49.4730000 | NULL | False | False | NULL |
| 8AAF3721-2EDE-4648-895F-20392E4F159D | NULL | NULL | NULL | NULL | 2026-09-01T16:35:57.9300000 | NULL | False | False | NULL |
| 82FA86D5-ACA9-42C9-8EE9-94E7F15261C0 | NULL | NULL | NULL | NULL | 2026-09-01T16:32:22.7870000 | NULL | False | False | NULL |
| 44494CB7-1713-4CCB-BBFA-C58C5CED9130 | NULL | NULL | NULL | NULL | 2026-09-01T16:33:33.9330000 | NULL | False | False | NULL |
| 2504581A-2C38-4BB3-898B-32BD39921CCC | NULL | NULL | NULL | NULL | 2026-09-01T16:33:08.5470000 | NULL | False | False | NULL |

---
