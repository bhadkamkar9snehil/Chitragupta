# XStudio_Xbatch.dbo.Wire_Rod_Quality_Data_File_Import

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference inclusion, hardenablity, dimension, metallurgical, testing, end, front, sample, shift, surface, back, hardness.

**Primary Key:** ID  
**Row Count:** 1,52,586  

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
| EntryDateTime | datetime | YES | — | — |
| MetallurgicalTestingDecard | decimal | YES | 18,4 | — |
| BackEnd | varchar | YES | 100 | — |
| FrontEnd | varchar | YES | 100 | — |
| FrontSample | varchar | YES | 100 | — |
| AsQuenchedHardnessHRC | decimal | YES | 18,4 | — |
| InclusionDthick | decimal | YES | 18,4 | — |
| HardenablityJ416in | decimal | YES | 18,4 | — |
| CoilNo | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| OvalityDimension | decimal | YES | 18,4 | — |
| MetallurgicalTestingMicrostructure | decimal | YES | 18,4 | — |
| InspectionLot | varchar | YES | 100 | — |
| HardenablityJ716in | decimal | YES | 18,4 | — |
| ELMechanical | decimal | YES | 18,4 | — |
| ReportDate | varchar | YES | 100 | — |
| S1Dimension | decimal | YES | 18,4 | — |
| YSMpa | decimal | YES | 18,4 | — |
| InclusionCthick | decimal | YES | 18,4 | — |
| HardenablityJ216in | decimal | YES | 18,4 | — |
| Mn | decimal | YES | 18,4 | — |
| InclusionDthin | decimal | YES | 18,4 | — |
| MetallurgicalTestingCentralSegregati | decimal | YES | 18,4 | — |
| Reason | varchar | YES | -1 | — |
| HardenablityJ116in | decimal | YES | 18,4 | — |
| HardenablityJ616in | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| InclusionAthin | decimal | YES | 18,4 | — |
| InclusionCthin | decimal | YES | 18,4 | — |
| C | decimal | YES | 18,4 | — |
| VisualSurface | varchar | YES | 100 | — |
| Remarks | varchar | YES | 100 | — |
| UTSMpa | decimal | YES | 18,4 | — |
| HardenablityJ316in | decimal | YES | 18,4 | — |
| ToleranceDimension | varchar | YES | 100 | — |
| ResonofNotOk | varchar | YES | -1 | — |
| Impact | decimal | YES | 18,4 | — |
| BackEndSurface | varchar | YES | 100 | — |
| HeatNo | varchar | YES | 100 | — |
| FTandBDimension | decimal | YES | 18,4 | — |
| NSideDimension | decimal | YES | 18,4 | — |
| MetallurgicalTestingResolvedPearlite | decimal | YES | 18,4 | — |
| S2Dimension | decimal | YES | 18,4 | — |
| MetallurgicalTestingGrainSize | decimal | YES | 18,4 | — |
| IsProcessed | bit | YES | — | — |
| InclusionBthick | decimal | YES | 18,4 | — |
| InclusionBthin | decimal | YES | 18,4 | — |
| FinalDisposition | varchar | YES | 100 | — |
| AsRolledHardnessHBW | decimal | YES | 18,4 | — |
| RAMechnical | decimal | YES | 18,4 | — |
| Shift | varchar | YES | 100 | — |
| InclusionAthick | decimal | YES | 18,4 | — |
| Size | decimal | YES | 18,4 | — |
| FrontEndSurface | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |
| HardenablityJ516in | decimal | YES | 18,4 | — |
| SampleLocationSample | varchar | YES | 100 | — |
| Samplereceivingtime | time | YES | — | — |
| ShiftInchargeQA | varchar | YES | 100 | — |
| ShiftInchargeQPR | varchar | YES | 100 | — |
| SamplelocationFB | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00063711-D1FE-4F37-92C5-773E8ED2D9B5 | NULL | NULL | 2026-08-30T06:40:19.1130000 | NULL | False | False | NULL | NULL | NULL |
| 00050D27-4911-47AE-BA20-6FAB7F501A62 | NULL | NULL | 2026-08-30T06:09:16.4770000 | NULL | False | False | NULL | NULL | NULL |
| 0004ACDF-093D-4AA1-8433-AEA40BBBB831 | NULL | NULL | 2026-08-30T05:06:54.5330000 | NULL | False | False | NULL | NULL | NULL |
| 00044A25-340F-4EB0-A1FE-54ED0289236E | NULL | NULL | 2026-08-31T07:32:41.6800000 | NULL | False | False | NULL | NULL | NULL |
| 0003D747-03B6-4206-8511-A56260C6502E | NULL | NULL | 2026-08-30T07:24:25.8800000 | NULL | False | False | NULL | NULL | NULL |
| 00034F93-F05C-42BA-8FA6-091F18161C46 | NULL | NULL | 2026-08-31T07:32:38.1770000 | NULL | False | False | NULL | NULL | NULL |
| 00033D30-5E0F-460D-8E15-3190DE7FB625 | NULL | NULL | 2026-08-30T02:45:18.5000000 | NULL | False | False | NULL | NULL | NULL |
| 0002D032-CF9B-45A4-9C77-D20C6A70FFB3 | NULL | NULL | 2026-08-31T09:28:02.6300000 | NULL | False | False | NULL | NULL | NULL |
| 00015CEE-C794-4BCE-B253-17817980E707 | NULL | NULL | 2026-08-30T04:51:55.7970000 | NULL | False | False | NULL | NULL | NULL |
| 00008F4C-B34F-4D47-A09F-B1B27607F365 | NULL | NULL | 2026-08-30T05:06:53.8600000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00063711-D1FE-4F37-92C5-773E8ED2D9B5 | NULL | NULL | 2026-08-30T06:40:19.1130000 | NULL | False | False | NULL | NULL | NULL |
| 00050D27-4911-47AE-BA20-6FAB7F501A62 | NULL | NULL | 2026-08-30T06:09:16.4770000 | NULL | False | False | NULL | NULL | NULL |
| 0004ACDF-093D-4AA1-8433-AEA40BBBB831 | NULL | NULL | 2026-08-30T05:06:54.5330000 | NULL | False | False | NULL | NULL | NULL |
| 00044A25-340F-4EB0-A1FE-54ED0289236E | NULL | NULL | 2026-08-31T07:32:41.6800000 | NULL | False | False | NULL | NULL | NULL |
| 0003D747-03B6-4206-8511-A56260C6502E | NULL | NULL | 2026-08-30T07:24:25.8800000 | NULL | False | False | NULL | NULL | NULL |
| 00034F93-F05C-42BA-8FA6-091F18161C46 | NULL | NULL | 2026-08-31T07:32:38.1770000 | NULL | False | False | NULL | NULL | NULL |
| 00033D30-5E0F-460D-8E15-3190DE7FB625 | NULL | NULL | 2026-08-30T02:45:18.5000000 | NULL | False | False | NULL | NULL | NULL |
| 0002D032-CF9B-45A4-9C77-D20C6A70FFB3 | NULL | NULL | 2026-08-31T09:28:02.6300000 | NULL | False | False | NULL | NULL | NULL |
| 00015CEE-C794-4BCE-B253-17817980E707 | NULL | NULL | 2026-08-30T04:51:55.7970000 | NULL | False | False | NULL | NULL | NULL |
| 00008F4C-B34F-4D47-A09F-B1B27607F365 | NULL | NULL | 2026-08-30T05:06:53.8600000 | NULL | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Wire_Rod_Quality_Data_File_Import.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Wire_Rod_Quality_Data_File_Import.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
