# XStudio_Xbatch.dbo.Rebar_Coil_Quality_Data

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** chemistry, quality, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference rib, high, low, inclination, ribht, area, spacing, centre, flank, long, relative, total.

**Primary Key:** ID  
**Row Count:** 50,593  

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
| NominalCrossSectionArea | decimal | YES | 18,4 | — |
| Nom | varchar | YES | 36 | — |
| Charging | varchar | YES | 36 | — |
| RelativeRibArea | decimal | YES | 18,4 | — |
| Tolerance | decimal | YES | 18,4 | — |
| Line | varchar | YES | 36 | — |
| IsProcessed | bit | YES | — | — |
| Sample | decimal | YES | 18,4 | — |
| EntryDateTime | date | YES | — | — |
| RibFlankInclination | int | YES | 10,0 | — |
| Rebend | varchar | YES | 36 | — |
| ParentID | varchar | YES | 36 | — |
| InitialofTestingPerson | varchar | YES | 100 | — |
| Camp | varchar | YES | 100 | — |
| BilletGrade | varchar | YES | 100 | — |
| ReportDate | varchar | YES | 100 | — |
| Grade | varchar | YES | 36 | — |
| RibInclination | int | YES | 10,0 | — |
| LongRibht | decimal | YES | 18,4 | — |
| UTSMPa | int | YES | 10,0 | — |
| HeatNo | varchar | YES | 36 | — |
| UTSorYSRatio | decimal | YES | 18,4 | — |
| ShiftInChargeOperation | varchar | YES | 36 | — |
| YSMPa | int | YES | 10,0 | — |
| Mn | decimal | YES | 18,4 | — |
| RootsofTransverseRib | varchar | YES | 36 | — |
| SampleRecievingTime | time | YES | — | — |
| C | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| TranRibht | decimal | YES | 18,4 | — |
| Remarks | varchar | YES | -1 | — |
| ActualCrossSectionalArea | decimal | YES | 18,4 | — |
| WtMtr | decimal | YES | 18,4 | — |
| TestingTime | time | YES | — | — |
| RiblessSpacing | decimal | YES | 18,4 | — |
| TotalEL | decimal | YES | 18,4 | — |
| CentreRibSpacing | decimal | YES | 18,4 | — |
| Shift | varchar | YES | 100 | — |
| CentreRibSpacingHigh | decimal | YES | 18,4 | — |
| TranRibhtHigh | decimal | YES | 18,4 | — |
| LongRibhtHigh | decimal | YES | 18,4 | — |
| RelativeRibAreaHigh | decimal | YES | 18,4 | — |
| RibFlankInclinationHigh | decimal | YES | 18,4 | — |
| RibInclinationHigh | decimal | YES | 18,4 | — |
| YSMPaHigh | decimal | YES | 18,4 | — |
| UTSorYSRatioHigh | decimal | YES | 18,4 | — |
| TotalELHigh | decimal | YES | 18,4 | — |
| CentreRibSpacingLow | decimal | YES | 18,4 | — |
| TranRibhtLow | decimal | YES | 18,4 | — |
| LongRibhtLow | decimal | YES | 18,4 | — |
| RelativeRibAreaLow | decimal | YES | 18,4 | — |
| RibFlankInclinationLow | decimal | YES | 18,4 | — |
| RibInclinationLow | decimal | YES | 18,4 | — |
| YSMPaLow | decimal | YES | 18,4 | — |
| UTSorYSRatioLow | decimal | YES | 18,4 | — |
| TotalELLow | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000B35F4-02C6-4BEC-908E-BD673115FC4A | NULL | NULL | 2026-09-01T15:36:29.4600000 | NULL | False | False | NULL | NULL |  |
| 000AF37A-F6DC-47FE-8176-8F56D46B9675 | NULL | NULL | 2026-09-01T14:59:21.8900000 | NULL | False | False | NULL | NULL |  |
| 00085EB3-EC0A-4D9F-B7CA-733B8B308D7F | NULL | NULL | 2026-08-29T22:37:03.5730000 | NULL | False | False | NULL | NULL | NULL |
| 0007EBED-9D19-46C5-A3ED-AC647377C02B | NULL | NULL | 2026-09-02T09:30:28.5370000 | NULL | False | False | NULL | NULL |  |
| 0007B461-1BD8-47A2-8C97-C4112C19405E | NULL | NULL | 2026-09-02T10:30:33.7300000 | NULL | False | False | NULL | NULL |  |
| 0007A411-E7F5-4484-87E2-81091A76EF85 | NULL | NULL | 2026-09-01T15:47:43.4570000 | NULL | False | False | NULL | NULL |  |
| 000567BE-0757-47FE-8DF8-1DA2C6C8A96E | NULL | NULL | 2026-09-02T09:31:21.4530000 | NULL | False | False | NULL | NULL |  |
| 0004BDE5-3F17-40CF-B449-94DF925D5EC3 | NULL | NULL | 2026-08-30T02:44:05.2900000 | NULL | False | False | NULL | NULL | NULL |
| 0004BDD1-7EF8-48ED-819F-065D5DDB511E | NULL | NULL | 2026-09-02T10:32:25.4700000 | NULL | False | False | NULL | NULL |  |
| 00049AF0-B846-4240-BF1B-80C6D4EA84FC | NULL | NULL | 2026-08-28T14:37:58.0300000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000B35F4-02C6-4BEC-908E-BD673115FC4A | NULL | NULL | 2026-09-01T15:36:29.4600000 | NULL | False | False | NULL | NULL |  |
| 000AF37A-F6DC-47FE-8176-8F56D46B9675 | NULL | NULL | 2026-09-01T14:59:21.8900000 | NULL | False | False | NULL | NULL |  |
| 00085EB3-EC0A-4D9F-B7CA-733B8B308D7F | NULL | NULL | 2026-08-29T22:37:03.5730000 | NULL | False | False | NULL | NULL | NULL |
| 0007EBED-9D19-46C5-A3ED-AC647377C02B | NULL | NULL | 2026-09-02T09:30:28.5370000 | NULL | False | False | NULL | NULL |  |
| 0007B461-1BD8-47A2-8C97-C4112C19405E | NULL | NULL | 2026-09-02T10:30:33.7300000 | NULL | False | False | NULL | NULL |  |
| 0007A411-E7F5-4484-87E2-81091A76EF85 | NULL | NULL | 2026-09-01T15:47:43.4570000 | NULL | False | False | NULL | NULL |  |
| 000567BE-0757-47FE-8DF8-1DA2C6C8A96E | NULL | NULL | 2026-09-02T09:31:21.4530000 | NULL | False | False | NULL | NULL |  |
| 0004BDE5-3F17-40CF-B449-94DF925D5EC3 | NULL | NULL | 2026-08-30T02:44:05.2900000 | NULL | False | False | NULL | NULL | NULL |
| 0004BDD1-7EF8-48ED-819F-065D5DDB511E | NULL | NULL | 2026-09-02T10:32:25.4700000 | NULL | False | False | NULL | NULL |  |
| 00049AF0-B846-4240-BF1B-80C6D4EA84FC | NULL | NULL | 2026-08-28T14:37:58.0300000 | NULL | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Rebar_Coil_Quality_Data.BilletGrade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Rebar_Coil_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Rebar_Coil_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
- `XStudio_XBatch.Rebar_Coil_Quality_Data.ShiftInChargeOperation` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
