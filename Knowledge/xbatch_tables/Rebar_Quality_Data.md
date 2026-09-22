# XStudio_Xbatch.dbo.Rebar_Quality_Data

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** chemistry, quality, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference rib, high, low, inclination, ribht, area, spacing, centre, flank, long, relative, total.

**Primary Key:** ID  
**Row Count:** 32,595  

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
| Camp | varchar | YES | 100 | — |
| CentreRibSpacing | decimal | YES | 18,4 | — |
| RibInclination | int | YES | 10,0 | — |
| ParentID | varchar | YES | 36 | — |
| Charging | varchar | YES | 7999 | — |
| RibFlankInclination | int | YES | 10,0 | — |
| Sample | int | YES | 10,0 | — |
| ReportDate | varchar | YES | 100 | — |
| YSMPa | decimal | YES | 18,4 | — |
| Tolerance | decimal | YES | 18,5 | — |
| LongRibht | decimal | YES | 18,4 | — |
| NominalCrossSectionArea | decimal | YES | 18,4 | — |
| UTSorYSRatio | decimal | YES | 18,4 | — |
| TotalEL | decimal | YES | 18,4 | — |
| Grade | varchar | YES | 36 | — |
| HeatNo | varchar | YES | 36 | — |
| RiblessSpacing | decimal | YES | 18,4 | — |
| IsProcessed | bit | YES | — | — |
| UTSMPa | decimal | YES | 18,4 | — |
| Mn | decimal | YES | 18,4 | — |
| TestingTime | time | YES | — | — |
| ActualCrossSectionalArea | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| WtMtr | decimal | YES | 18,4 | — |
| BilletGrade | varchar | YES | 100 | — |
| Nom | varchar | YES | 36 | — |
| Line | varchar | YES | 36 | — |
| RootsofTransverseRib | varchar | YES | 36 | — |
| EntryDateTime | date | YES | — | — |
| ShiftInChargeOperation | varchar | YES | 36 | — |
| Remarks | varchar | YES | -1 | — |
| RelativeRibArea | decimal | YES | 18,4 | — |
| Rebend | varchar | YES | 36 | — |
| TranRibht | decimal | YES | 18,4 | — |
| C | decimal | YES | 18,4 | — |
| SampleRecievingTime | time | YES | — | — |
| InitialofTestingPerson | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| CentreRibSpacingHigh | decimal | YES | 18,4 | — |
| CentreRibSpacingLow | decimal | YES | 18,4 | — |
| TranRibhtHigh | decimal | YES | 18,4 | — |
| TranRibhtLow | decimal | YES | 18,4 | — |
| LongRibhtHigh | decimal | YES | 18,4 | — |
| LongRibhtLow | decimal | YES | 18,4 | — |
| RelativeRibAreaHigh | decimal | YES | 18,4 | — |
| RelativeRibAreaLow | decimal | YES | 18,4 | — |
| RibFlankInclinationHigh | decimal | YES | 18,4 | — |
| RibFlankInclinationLow | decimal | YES | 18,4 | — |
| RibInclinationHigh | decimal | YES | 18,4 | — |
| UTSorYSRatioLow | decimal | YES | 18,4 | — |
| TotalELHigh | decimal | YES | 18,4 | — |
| YSMPaHigh | decimal | YES | 18,4 | — |
| UTSorYSRatioHigh | decimal | YES | 18,4 | — |
| RibInclinationLow | decimal | YES | 18,4 | — |
| YSMPaLow | decimal | YES | 18,4 | — |
| TotalELLow | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00122192-AE0E-4C01-9A13-BDA1822903F4 | NULL | NULL | 2026-08-27T20:42:27.7100000 | NULL | False | False | NULL | NULL |  |
| 000F141C-F45B-410F-B8BB-2DD415C90D86 | NULL | NULL | 2026-08-26T10:52:37.4600000 | NULL | False | False | NULL | NULL |  |
| 000C7855-7081-404C-BA39-AFC890BD0071 | NULL | NULL | 2026-08-27T20:41:08.8300000 | NULL | False | False | NULL | NULL |  |
| 000B4ED6-49D4-4F5E-A774-3C24A56F0DC6 | NULL | NULL | 2026-08-27T20:41:57.4070000 | NULL | False | False | NULL | NULL |  |
| 000823D3-9720-444A-9094-720B82215699 | NULL | NULL | 2026-08-26T10:53:04.5000000 | NULL | False | False | NULL | NULL |  |
| 00081F95-7D09-4A95-B43B-380EDAF85406 | NULL | NULL | 2026-08-27T20:12:06.5800000 | NULL | False | False | NULL | NULL |  |
| 0007EFD8-A06D-4737-830F-1DE855D27AB8 | NULL | NULL | 2026-08-26T10:53:43.7670000 | NULL | False | False | NULL | NULL |  |
| 00068103-33FC-4713-86D0-1FDFF67520BE | NULL | NULL | 2026-08-27T20:41:19.4070000 | NULL | False | False | NULL | NULL |  |
| 00066023-8836-4A7B-B58E-7BF053AD97E9 | NULL | NULL | 2026-08-27T20:11:55.9600000 | NULL | False | False | NULL | NULL |  |
| 0003A597-0540-4263-8972-085DFF0D005E | NULL | NULL | 2026-08-20T12:39:44.5800000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00122192-AE0E-4C01-9A13-BDA1822903F4 | NULL | NULL | 2026-08-27T20:42:27.7100000 | NULL | False | False | NULL | NULL |  |
| 000F141C-F45B-410F-B8BB-2DD415C90D86 | NULL | NULL | 2026-08-26T10:52:37.4600000 | NULL | False | False | NULL | NULL |  |
| 000C7855-7081-404C-BA39-AFC890BD0071 | NULL | NULL | 2026-08-27T20:41:08.8300000 | NULL | False | False | NULL | NULL |  |
| 000B4ED6-49D4-4F5E-A774-3C24A56F0DC6 | NULL | NULL | 2026-08-27T20:41:57.4070000 | NULL | False | False | NULL | NULL |  |
| 000823D3-9720-444A-9094-720B82215699 | NULL | NULL | 2026-08-26T10:53:04.5000000 | NULL | False | False | NULL | NULL |  |
| 00081F95-7D09-4A95-B43B-380EDAF85406 | NULL | NULL | 2026-08-27T20:12:06.5800000 | NULL | False | False | NULL | NULL |  |
| 0007EFD8-A06D-4737-830F-1DE855D27AB8 | NULL | NULL | 2026-08-26T10:53:43.7670000 | NULL | False | False | NULL | NULL |  |
| 00068103-33FC-4713-86D0-1FDFF67520BE | NULL | NULL | 2026-08-27T20:41:19.4070000 | NULL | False | False | NULL | NULL |  |
| 00066023-8836-4A7B-B58E-7BF053AD97E9 | NULL | NULL | 2026-08-27T20:11:55.9600000 | NULL | False | False | NULL | NULL |  |
| 0003A597-0540-4263-8972-085DFF0D005E | NULL | NULL | 2026-08-20T12:39:44.5800000 | NULL | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Rebar_Quality_Data.BilletGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Rebar_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Rebar_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Rebar_Quality_Data.ShiftInChargeOperation` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
