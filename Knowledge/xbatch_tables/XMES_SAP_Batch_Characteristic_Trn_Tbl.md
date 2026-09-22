# XStudio_Xbatch.dbo.XMES_SAP_Batch_Characteristic_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference class, grade, heat, number, pieces, sectional, weight, actual, agency, batch, code, colour.

**Primary Key:** ID  
**Row Count:** 3,690  
**Date Range (ModifiedOn):** 2026-01-28T14:22:11.8230000 to 2026-07-08T23:43:53.7900000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Plant | varchar | YES | 100 | — |
| Saptransactionid | varchar | YES | 36 | — |
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
| HeatNo | varchar | YES | 100 | — |
| Product | varchar | YES | 100 | — |
| Length | decimal | YES | 18,2 | — |
| Thickness | int | YES | 10,0 | — |
| Width | int | YES | 10,0 | — |
| SectionalWeight | decimal | YES | 18,3 | — |
| ProductionSectionalWeight | decimal | YES | 18,3 | — |
| NoOfPieces | int | YES | 10,0 | — |
| TonsPerPiece | decimal | YES | 18,3 | — |
| ExternalGrade | varchar | YES | 100 | — |
| ProcessRoute | varchar | YES | 100 | — |
| InspectionAgency | varchar | YES | 100 | — |
| TDCRefNo | int | YES | 10,0 | — |
| ColourCode | varchar | YES | 100 | — |
| Pieces | int | YES | 10,0 | — |
| ActualGrade | varchar | YES | 100 | — |
| HeatSequenceNumber | varchar | YES | 100 | — |
| BatchNo | varchar | YES | 100 | — |
| Material | varchar | YES | 100 | — |
| SAPPostingStatus | varchar | YES | 50 | — |
| ClassNumber | varchar | YES | 100 | — |
| ClassType | varchar | YES | 100 | — |
| ObjectTable | varchar | YES | 100 | — |
| Message | varchar | YES | -1 | — |

### Top 10 Records

| ID | Plant | Saptransactionid | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 009D9C65-A6B9-463B-9AFD-370F1E3E05B5 | 7502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-02-02T05:02:02.3370000 | NULL | False | False | NULL |
| 024A03E2-392D-43E3-9F15-F98256F8D203 | 7502 | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | NULL | 2026-03-10T15:41:40.5600000 | NULL | False | False | NULL |
| 02532F93-3936-455B-BE74-E8CE099990DB | 8502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-01-28T18:06:13.9100000 | NULL | False | False | NULL |
| 02EA7470-8088-4C5C-A72B-304E086BB5A3 | 8502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-01-29T04:38:05.6200000 | NULL | False | False | NULL |
| 04AEE04F-91EF-4CB7-9C3B-3B9C6679AAEB | 7502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-02-03T01:38:14.0700000 | NULL | False | False | NULL |
| 0870D6EC-0772-43A8-9476-9158E900159B | 8502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-01-29T04:37:48.0930000 | NULL | False | False | NULL |
| 09216DD6-D9E2-4154-95BD-5A9CDA13563E | 8502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-01-28T17:19:02.4630000 | NULL | False | False | NULL |
| 09759E4C-25A1-46C9-9048-B5A743A83395 | 8502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-01-28T17:19:13.8770000 | NULL | False | False | NULL |
| 0B67DD6E-69FA-4A5C-A9F7-38B2EAD06B52 | 7502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-02-08T10:55:50.6630000 | NULL | False | False | NULL |
| 0BFB26D6-49D3-47AA-A3DF-E63D845A82F1 | 7502 | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | NULL | 2026-02-01T16:55:12.9830000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Plant | Saptransactionid | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 452305F4-7AD3-4D39-8AE1-06F52C0A47B6 | 7502 | 460b36bb-cf40-45e6-9f9e-04e7e0266c7a | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:07.7600000 | 2026-07-08T23:43:53.7900000 | False | False | NULL |
| DDD0A698-F20F-4FFD-860B-0A88E01CBD03 | 7502 | 2ba04b0e-4a01-493b-b9db-5f41818d3e1e | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:43:07.7600000 | 2026-07-08T23:43:50.8100000 | False | False | NULL |
| D7413F9F-F738-4C1A-B937-79E1448D2216 | 7502 | c4db56e4-ee69-426d-9390-a80d19bfabf6 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T23:41:49.6730000 | 2026-07-08T23:42:37.1570000 | False | False | NULL |
| 88E94F2C-8E40-4489-A2F3-6112FD883CC3 | 7502 | 53d2b70b-06ed-4049-8530-882f6ba487fa | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T18:00:21.9900000 | 2026-07-08T18:01:03.4770000 | False | False | NULL |
| 63BD0619-3CB7-420E-B290-6C1A190C3267 | 7502 | 67b29500-9839-48e1-bac7-9fa1e5503c30 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T16:48:41.6430000 | 2026-07-08T16:49:44.7770000 | False | False | NULL |
| 09E9E2EC-A880-4500-9AE2-29A31B8B1B16 | 7502 | b2d4e32e-0fa5-463d-bf4e-4a97bead30a8 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T15:38:53.0070000 | 2026-07-08T15:40:47.5600000 | False | False | NULL |
| A8DC740D-7347-433B-AE4D-B7A88017FA3D | 7502 | d91db014-b309-40e5-8e1b-b518ecc1854a | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T15:38:24.6800000 | 2026-07-08T15:39:44.0030000 | False | False | NULL |
| 48B053C6-9E2B-41DF-8BFB-D314FD6E3525 | 7502 | adbbf1dd-f14e-4311-892c-1593ba8749c8 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T15:37:58.8530000 | 2026-07-08T15:39:27.3900000 | False | False | NULL |
| BF0504E2-09B3-4816-B5BF-CB613AE3B42E | 7502 | 7144a3e4-22ef-49d1-bcaa-a59ca3eb6e6b | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T12:24:42.4870000 | 2026-07-08T12:25:48.0730000 | False | False | NULL |
| AC9D3D1B-B64F-4AE0-9960-102C6DBCE6D8 | 7502 | 328dbb2b-60d0-4860-8877-1245084f5804 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-08T11:40:05.7270000 | 2026-07-08T11:41:11.7470000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_SAP_Batch_Characteristic_Trn_Tbl.Saptransactionid` -> `XStudio_XBatch.XMES_SAP_API_Batch_Characteristics_Error.TransactionID` (Many to One)
