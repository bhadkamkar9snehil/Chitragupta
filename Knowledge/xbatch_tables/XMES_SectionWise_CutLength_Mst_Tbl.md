# XStudio_Xbatch.dbo.XMES_SectionWise_CutLength_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference dia, bundle, pieces, weight, section.

**Primary Key:** ID  
**Row Count:** 21  

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
| Section | decimal | YES | 18,4 | — |
| RB_B500B_8_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_8_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_10_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_10_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_12_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_12_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_14_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_14_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_16_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_16_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_18_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_18_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_20_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_20_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_25_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_25_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_32_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_32_0DIA_NoOfPieces | int | YES | 10,0 | — |
| RB_B500B_40_0DIA_BundleWeight | decimal | YES | 18,4 | — |
| RB_B500B_40_0DIA_NoOfPieces | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 95FEFCAF-2F63-473B-8DF2-CBB8CB3A95D4 | NULL | NULL | 2026-08-01T10:25:19.1200000 | NULL | False | False | NULL | NULL | NULL |
| 8FAFCFF2-F675-4FFD-8D3D-1CA49E0FCECB | NULL | NULL | 2026-08-01T10:24:49.8670000 | NULL | False | False | NULL | NULL | NULL |
| 8187C87C-35A6-4BBB-A398-6A5D7855A40C | NULL | NULL | 2026-08-01T10:25:16.5930000 | NULL | False | False | NULL | NULL | NULL |
| 7B1350E1-6C6A-422B-B4F0-CDCF6FA96BBC | NULL | NULL | 2026-08-01T10:24:56.5070000 | NULL | False | False | NULL | NULL | NULL |
| 5E050387-5B4F-4BA4-BEAC-65B92AB86A50 | NULL | NULL | 2026-08-01T10:25:11.8270000 | NULL | False | False | NULL | NULL | NULL |
| 5CC8CEFD-CDAD-4A67-A268-47CFFD89B6DF | NULL | NULL | 2026-08-01T10:24:52.2800000 | NULL | False | False | NULL | NULL | NULL |
| 4C45E759-C8A0-463B-AC2E-00D83043AC2F | NULL | NULL | 2026-08-01T10:24:58.6430000 | NULL | False | False | NULL | NULL | NULL |
| 47C78E66-E3A0-4E6F-94DB-DA059801D9C4 | NULL | NULL | 2026-08-01T10:25:31.9570000 | NULL | False | False | NULL | NULL | NULL |
| 2F2C5268-0A1D-4100-803D-2AC293415BDB | NULL | NULL | 2026-08-01T10:25:21.2370000 | NULL | False | False | NULL | NULL | NULL |
| 1F3066EC-45D7-422F-82D2-A3F9AB1EA8AF | NULL | NULL | 2026-08-01T10:24:54.3870000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 95FEFCAF-2F63-473B-8DF2-CBB8CB3A95D4 | NULL | NULL | 2026-08-01T10:25:19.1200000 | NULL | False | False | NULL | NULL | NULL |
| 8FAFCFF2-F675-4FFD-8D3D-1CA49E0FCECB | NULL | NULL | 2026-08-01T10:24:49.8670000 | NULL | False | False | NULL | NULL | NULL |
| 8187C87C-35A6-4BBB-A398-6A5D7855A40C | NULL | NULL | 2026-08-01T10:25:16.5930000 | NULL | False | False | NULL | NULL | NULL |
| 7B1350E1-6C6A-422B-B4F0-CDCF6FA96BBC | NULL | NULL | 2026-08-01T10:24:56.5070000 | NULL | False | False | NULL | NULL | NULL |
| 5E050387-5B4F-4BA4-BEAC-65B92AB86A50 | NULL | NULL | 2026-08-01T10:25:11.8270000 | NULL | False | False | NULL | NULL | NULL |
| 5CC8CEFD-CDAD-4A67-A268-47CFFD89B6DF | NULL | NULL | 2026-08-01T10:24:52.2800000 | NULL | False | False | NULL | NULL | NULL |
| 4C45E759-C8A0-463B-AC2E-00D83043AC2F | NULL | NULL | 2026-08-01T10:24:58.6430000 | NULL | False | False | NULL | NULL | NULL |
| 47C78E66-E3A0-4E6F-94DB-DA059801D9C4 | NULL | NULL | 2026-08-01T10:25:31.9570000 | NULL | False | False | NULL | NULL | NULL |
| 2F2C5268-0A1D-4100-803D-2AC293415BDB | NULL | NULL | 2026-08-01T10:25:21.2370000 | NULL | False | False | NULL | NULL | NULL |
| 1F3066EC-45D7-422F-82D2-A3F9AB1EA8AF | NULL | NULL | 2026-08-01T10:24:54.3870000 | NULL | False | False | NULL | NULL | NULL |

---
