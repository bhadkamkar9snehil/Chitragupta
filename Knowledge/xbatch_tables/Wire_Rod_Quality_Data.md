# XStudio_Xbatch.dbo.Wire_Rod_Quality_Data

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference inclusion, hardenablity, dimension, metallurgical, testing, end, back, front, surface, hardness, sample, size.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2025-12-09T15:47:40.0000000 to 2025-12-12T14:35:52.0000000  

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
| ELMechanical | decimal | YES | 18,4 | — |
| ReportDate | varchar | YES | 100 | — |
| S1Dimension | decimal | YES | 18,4 | — |
| AsQuenchedHardnessHRC | decimal | YES | 18,4 | — |
| YSMpa | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| VisualSurface | varchar | YES | 36 | — |
| Remarks | varchar | YES | 36 | — |
| UTSMpa | decimal | YES | 18,4 | — |
| OvalityDimension | decimal | YES | 18,4 | — |
| ToleranceDimension | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| FrontEnd | varchar | YES | 36 | — |
| BackEndSurface | varchar | YES | 36 | — |
| HeatNo | varchar | YES | 36 | — |
| FTandBDimension | decimal | YES | 18,4 | — |
| Reason | varchar | YES | -1 | — |
| NSideDimension | decimal | YES | 18,4 | — |
| CoilNo | varchar | YES | 100 | — |
| S2Dimension | decimal | YES | 18,4 | — |
| ResonofNotOk | varchar | YES | -1 | — |
| BackEnd | varchar | YES | 36 | — |
| FrontSample | varchar | YES | 100 | — |
| FinalDisposition | varchar | YES | 36 | — |
| AsRolledHardnessHBW | decimal | YES | 18,4 | — |
| RAMechnical | decimal | YES | 18,4 | — |
| Shift | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| Size | int | YES | 10,0 | — |
| FrontEndSurface | varchar | YES | 36 | — |
| Grade | varchar | YES | 36 | — |
| ParentID | varchar | YES | 36 | — |
| BackSample | varchar | YES | 100 | — |
| InspectionLot | varchar | YES | 100 | — |
| C | decimal | YES | 18,4 | — |
| Mn | decimal | YES | 18,4 | — |
| MetallurgicalTestingGrainSize | decimal | YES | 18,4 | — |
| MetallurgicalTestingDecard | decimal | YES | 18,4 | — |
| MetallurgicalTestingResolvedPearlite | decimal | YES | 18,4 | — |
| MetallurgicalTestingCentralSegregati | decimal | YES | 18,4 | — |
| MetallurgicalTestingMicrostructure | decimal | YES | 18,4 | — |
| InclusionAthin | decimal | YES | 18,4 | — |
| InclusionAthick | decimal | YES | 18,4 | — |
| InclusionBthick | decimal | YES | 18,4 | — |
| InclusionBthin | decimal | YES | 18,4 | — |
| InclusionCthin | decimal | YES | 18,4 | — |
| InclusionCthick | decimal | YES | 18,4 | — |
| InclusionDthick | decimal | YES | 18,4 | — |
| InclusionDthin | decimal | YES | 18,4 | — |
| HardenablityJ116in | decimal | YES | 18,4 | — |
| HardenablityJ216in | decimal | YES | 18,4 | — |
| HardenablityJ316in | decimal | YES | 18,4 | — |
| HardenablityJ416in | decimal | YES | 18,4 | — |
| HardenablityJ516in | decimal | YES | 18,4 | — |
| HardenablityJ616in | decimal | YES | 18,4 | — |
| HardenablityJ716in | decimal | YES | 18,4 | — |
| Impact | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 586441E9-C22A-4806-ACB2-E57E26A7018F | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-08T10:41:56.8330000 | 2025-12-09T15:47:40.0000000 | False | False | NULL |  | NULL |
| 56BB8B82-974E-453C-B26D-56CDC252E7F6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-09T15:47:40.2270000 | 2025-12-09T15:47:49.0000000 | False | False | NULL |  | NULL |
| FB271124-783A-4663-8BA6-28BCE1A669A8 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-08T10:41:56.7730000 | 2025-12-09T15:47:51.0000000 | False | False | NULL | 172.16.6.34 | NULL |
| 9E93A7C5-EA94-499E-BDDB-A9FA61320420 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-08T10:41:56.6900000 | 2025-12-12T14:30:11.0000000 | False | False | NULL | 172.16.6.34 | NULL |
| F9E0299B-D834-4D8E-BBFC-A2EEEB10FC09 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-09T15:11:17.8730000 | 2025-12-12T14:30:11.0000000 | False | False | NULL | 172.16.6.34 | NULL |
| 4BE13176-48A9-4E91-8692-8BB4EE7B75B9 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-26T08:50:06.0700000 | 2025-12-12T14:30:11.0000000 | False | False | NULL | 172.16.6.34 |  |
| 34D53E98-3CE9-4FA8-8B64-D6B81E2550A5 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-25T15:11:55.5800000 | 2025-12-12T14:32:14.0000000 | False | False | NULL | 172.16.6.34 |  |
| A4C30375-982A-4C14-B349-50861D63E527 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-25T15:08:43.2530000 | 2025-12-12T14:32:14.0000000 | False | False | NULL | 172.16.6.34 |  |
| 87775500-4BCA-4B1E-9647-110FF998E821 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-08T10:41:56.8030000 | 2025-12-12T14:35:52.0000000 | False | False | NULL | 172.16.6.34 | NULL |
| 7D2B1190-4408-494D-B118-1EB50B38DF1A | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-12-08T10:41:56.8630000 | 2025-12-12T14:35:52.0000000 | False | False | NULL | 172.16.6.34 | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Wire_Rod_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Wire_Rod_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
