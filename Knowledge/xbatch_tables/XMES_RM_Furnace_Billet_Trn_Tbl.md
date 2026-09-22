# XStudio_Xbatch.dbo.XMES_RM_Furnace_Billet_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference time, residence, zone, minute, mmss, billet, end, heat, starttime, total.

**Primary Key:** ID  
**Row Count:** 2,680  
**Date Range (ModifiedOn):** 2026-07-13T13:29:21.0000000 to 2026-07-13T13:29:21.2300000  

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
| Starttime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| HeatNo | varchar | YES | 36 | — |
| BilletNo | varchar | YES | 100 | — |
| TotalResidenceTime | decimal | YES | 18,2 | — |
| zone2ResidenceTime | datetime | YES | — | — |
| zone3ResidenceTime | datetime | YES | — | — |
| zone4ResidenceTime | datetime | YES | — | — |
| zone5ResidenceTime | datetime | YES | — | — |
| zone6ResidenceTime | datetime | YES | — | — |
| zone7ResidenceTime | datetime | YES | — | — |
| zone8ResidenceTime | datetime | YES | — | — |
| zone1ResidenceTime | datetime | YES | — | — |
| Zone4ResidenceTimeMinute | decimal | YES | 18,4 | — |
| Zone1ResidenceTimeMinute | decimal | YES | 18,4 | — |
| Zone2ResidenceTimeMinute | decimal | YES | 18,4 | — |
| Zone3ResidenceTimeMinute | decimal | YES | 18,4 | — |
| Zone5ResidenceTimeMinute | decimal | YES | 18,4 | — |
| Zone6ResidenceTimeMinute | decimal | YES | 18,4 | — |
| Zone7ResidenceTimeMinute | decimal | YES | 18,4 | — |
| Zone8ResidenceTimeMinute | decimal | YES | 18,4 | — |
| Zone1ResidenceTimeMMSS | varchar | YES | 100 | — |
| Zone2ResidenceTimeMMSS | varchar | YES | 100 | — |
| Zone3ResidenceTimeMMSS | varchar | YES | 100 | — |
| Zone4ResidenceTimeMMSS | varchar | YES | 100 | — |
| Zone5ResidenceTimeMMSS | varchar | YES | 100 | — |
| Zone6ResidenceTimeMMSS | varchar | YES | 100 | — |
| Zone7ResidenceTimeMMSS | varchar | YES | 100 | — |
| Zone8ResidenceTimeMMSS | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00D9F8B2-DC56-49BF-8B9D-37A74B0722B1 | NULL | 82B540D3-8AD7-4FB6-A904-C9C642F1461B | NULL | NULL | 2026-06-30T21:21:06.2830000 | NULL | False | False | NULL |
| 00CAB265-C609-4A4F-9160-84B1A5156005 | NULL | E66B4437-BD4F-4877-AFB4-9DD30F7F4791 | NULL | NULL | 2026-06-30T21:02:42.3830000 | NULL | False | False | NULL |
| 00C63EE1-2E8C-474F-8F0C-C5A911BADF0C | NULL | 7CAD7E3A-E2F3-49FB-8357-7411446732F1 | NULL | NULL | 2026-06-30T17:50:41.9600000 | NULL | False | False | NULL |
| 00A76945-1D4B-4B59-A5A9-51813CF35A25 | NULL | AB7FCFFF-496C-4647-8695-4D6990F29713 | NULL | NULL | 2026-08-20T13:55:10.0130000 | NULL | False | False | NULL |
| 00889416-C618-484E-B386-03383DE86C45 | NULL | DA462292-DE38-439F-9CA5-5FB7EDAD423F | NULL | NULL | 2026-08-22T12:14:48.1770000 | NULL | False | False | NULL |
| 006E0685-A218-429C-A1B4-9596ECBE4C63 | NULL | B6C510A6-D98B-4407-8C47-0471FED88EFF | NULL | NULL | 2026-08-18T14:55:52.2230000 | NULL | False | False | NULL |
| 005EB00D-4EFC-40E9-8A49-2C4F03A7EBCC | NULL | A4F665E1-47C1-49D5-8031-29CAF596354C | NULL | NULL | 2026-07-30T16:31:53.6700000 | NULL | False | False | NULL |
| 0059414B-AB07-42D1-AE50-3A9E475EF0AD | NULL | A3DFE373-2502-4DA6-A404-225A69AC825D | NULL | NULL | 2026-08-21T16:07:42.3700000 | NULL | False | False | NULL |
| 004F2BFB-C23A-48C2-94BF-767D037BE736 | NULL | 1EBC012A-48A6-42FF-A501-486B9F7F9B04 | NULL | NULL | 2026-08-01T14:11:19.9000000 | NULL | False | False | NULL |
| 003928FE-8779-4C21-93E1-F1086C3E67FE | NULL | 2D7CA795-FF36-444A-983D-A8AB79D08145 | NULL | NULL | 2026-07-31T12:32:00.2970000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B3A87304-1652-4905-894B-26C21D55F0A9 | NULL | B3FD3E1C-274B-4141-A505-CE5D05B71C62 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-30T16:38:53.1430000 | 2026-07-13T13:29:21.2300000 | True | False | NULL |
| F5AC1277-14EC-4F4D-8690-E6D1DF1C2B89 | NULL | 8547EB9D-F164-4DC0-831B-68341BCCF762 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-30T16:37:19.9100000 | 2026-07-13T13:29:21.2270000 | True | False | NULL |
| 44D7D3BD-8853-4B0B-9917-70C4D772BD6B | NULL | 817C7467-6269-4E64-ADAC-D1B33F8F1B61 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-30T16:43:32.0730000 | 2026-07-13T13:29:21.0000000 | True | False | NULL |
| 4BFA9C6C-1CFA-4748-A6A5-DCB1690FFB88 | NULL | E6BAEB6F-1A66-4363-846A-9DC77AC86281 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-30T16:45:03.6300000 | 2026-07-13T13:29:21.0000000 | True | False | NULL |
| 831B236B-81DE-4D64-9ADC-41C03A4EE92D | NULL | 5DC866FA-1563-47B0-AFE2-5A306587512D | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-30T16:49:40.8100000 | 2026-07-13T13:29:21.0000000 | True | False | NULL |
| B2B07480-0A84-45A7-AB3E-C5D1BF21AAE1 | NULL | 610A7BD7-7559-4E7B-8E40-6A6839C67F87 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-30T16:46:41.1900000 | 2026-07-13T13:29:21.0000000 | True | False | NULL |
| D579AA71-3ED3-48F2-AC8C-1EC54BACAC63 | NULL | C745284E-5BDB-4F09-ADBB-19C8766AE76E | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-30T16:48:08.1700000 | 2026-07-13T13:29:21.0000000 | True | False | NULL |
| EFC1166B-E753-4F41-B03E-387AE8D4D02E | NULL | ECC61A91-8EFD-4B88-A456-32B7C8ADFF58 | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-30T16:41:59.2030000 | 2026-07-13T13:29:21.0000000 | True | False | NULL |
| 00D9F8B2-DC56-49BF-8B9D-37A74B0722B1 | NULL | 82B540D3-8AD7-4FB6-A904-C9C642F1461B | NULL | NULL | 2026-06-30T21:21:06.2830000 | NULL | False | False | NULL |
| 00CAB265-C609-4A4F-9160-84B1A5156005 | NULL | E66B4437-BD4F-4877-AFB4-9DD30F7F4791 | NULL | NULL | 2026-06-30T21:02:42.3830000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Billet_Movement_Dtl_Tbl.ZonewiseBilletNo` -> `XStudio_XBatch.XMES_RM_Furnace_Billet_Trn_Tbl.BilletNo` (Many to One)
- `XStudio_XBatch.XMES_Live_Charging_SECT2.ID` -> `XStudio_XBatch.XMES_RM_Furnace_Billet_Trn_Tbl.ParentID` (One to Many)
- `XStudio_XBatch.XMES_RM_Furnace_Billet_Trn_Tbl.HeatNo` -> `XStudio_XBatch.XBatch_Material_Inventory_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Furnace_Billet_Trn_Tbl.ParentID` -> `XStudio_XBatch.XMES_Live_Charging_SECT2.ID` (Many to One)
