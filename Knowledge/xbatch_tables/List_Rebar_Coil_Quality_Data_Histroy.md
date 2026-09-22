# XStudio_Xbatch.dbo.List_Rebar_Coil_Quality_Data_Histroy

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference rib, high, low, inclination, ribht, area, spacing, centre, flank, long, relative, total.

**Primary Key:** ID  
**Row Count:** 0  

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
| LongRibhtHigh | decimal | YES | 18,4 | — |
| LongRibht | decimal | YES | 18,4 | — |
| TotalELLow | decimal | YES | 18,4 | — |
| RibInclinationLow | decimal | YES | 18,4 | — |
| Charging | varchar | YES | 36 | — |
| TranRibht | decimal | YES | 18,4 | — |
| RibFlankInclinationHigh | decimal | YES | 18,4 | — |
| Line | varchar | YES | 36 | — |
| TranRibhtLow | decimal | YES | 18,4 | — |
| HeatNo | varchar | YES | 36 | — |
| C | decimal | YES | 18,4 | — |
| UTSorYSRatio | decimal | YES | 18,4 | — |
| RiblessSpacing | decimal | YES | 18,4 | — |
| CentreRibSpacingHigh | decimal | YES | 18,4 | — |
| RelativeRibAreaLow | decimal | YES | 18,4 | — |
| InitialofTestingPerson | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| NominalCrossSectionArea | decimal | YES | 18,4 | — |
| Nom | varchar | YES | 36 | — |
| Camp | varchar | YES | 100 | — |
| UTSorYSRatioLow | decimal | YES | 18,4 | — |
| RibInclinationHigh | decimal | YES | 18,4 | — |
| RelativeRibArea | decimal | YES | 18,4 | — |
| TotalEL | decimal | YES | 18,4 | — |
| BilletGrade | varchar | YES | 100 | — |
| CentreRibSpacing | decimal | YES | 18,4 | — |
| ActualCrossSectionalArea | decimal | YES | 18,4 | — |
| RelativeRibAreaHigh | decimal | YES | 18,4 | — |
| Tolerance | decimal | YES | 18,4 | — |
| IsProcessed | bit | YES | — | — |
| Sample | decimal | YES | 18,4 | — |
| EntryDateTime | date | YES | — | — |
| RibFlankInclination | int | YES | 10,0 | — |
| Rebend | varchar | YES | 36 | — |
| UTSorYSRatioHigh | decimal | YES | 18,4 | — |
| TranRibhtHigh | decimal | YES | 18,4 | — |
| ReportDate | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| Grade | varchar | YES | 36 | — |
| RibInclination | int | YES | 10,0 | — |
| RibFlankInclinationLow | decimal | YES | 18,4 | — |
| UTSMPa | int | YES | 10,0 | — |
| LongRibhtLow | decimal | YES | 18,4 | — |
| YSMPaLow | decimal | YES | 18,4 | — |
| ShiftInChargeOperation | varchar | YES | 36 | — |
| YSMPa | int | YES | 10,0 | — |
| Mn | decimal | YES | 18,4 | — |
| RootsofTransverseRib | varchar | YES | 36 | — |
| CentreRibSpacingLow | decimal | YES | 18,4 | — |
| SampleRecievingTime | time | YES | — | — |
| Shift | varchar | YES | 100 | — |
| Remarks | varchar | YES | -1 | — |
| WtMtr | decimal | YES | 18,4 | — |
| TotalELHigh | decimal | YES | 18,4 | — |
| TestingTime | time | YES | — | — |
| YSMPaHigh | decimal | YES | 18,4 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.List_Rebar_Coil_Quality_Data_Histroy.BilletGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.List_Rebar_Coil_Quality_Data_Histroy.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.List_Rebar_Coil_Quality_Data_Histroy.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.List_Rebar_Coil_Quality_Data_Histroy.ShiftInChargeOperation` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
