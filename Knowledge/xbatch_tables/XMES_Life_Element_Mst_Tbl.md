# XStudio_Xbatch.dbo.XMES_Life_Element_Mst_Tbl

**table_kind:** production_data

### What this table is for

- No curated business description or distinguishing column vocabulary found for this table; treat as low-confidence for semantic matching.

**Primary Key:** ID  
**Row Count:** 29  
**Date Range (ModifiedOn):** 2026-03-06T16:04:51.0000000 to 2026-04-10T17:15:15.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | -1 | — |
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

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 69D673AB-853D-4C35-8A52-1E81F7FB4DF3 | Mould Tube Life Strand 3 | D74C2FC1-2790-4C29-B53B-56ACF02F4E76 | NULL | NULL | 2026-03-06T16:16:12.1400000 | NULL | False | False | NULL |
| 61A4B6AA-0E10-4CD6-B79B-17ED4173EE00 | Mould Tube Life Strand 2 | D74C2FC1-2790-4C29-B53B-56ACF02F4E76 | NULL | NULL | 2026-03-06T16:16:12.1400000 | NULL | False | False | NULL |
| 558DB9C2-A8AE-4418-BB90-683B0CE81CF7 | Ladle 3 | EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | NULL | NULL | 2026-03-06T16:08:08.5000000 | NULL | False | False | NULL |
| 4E0BD845-B867-45A4-A026-EFE3E4895516 | Ladle 2 | EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | NULL | NULL | 2026-03-06T16:08:08.4600000 | NULL | False | False | NULL |
| 49AECE88-3E5A-43FA-AD55-B1E9A66FE998 | Mould Tube Life Strand 4 | D74C2FC1-2790-4C29-B53B-56ACF02F4E76 | NULL | NULL | 2026-03-06T16:16:12.1400000 | NULL | False | False | NULL |
| 21B6DCA5-6D4D-4524-BE79-C5643A574F2D | Mould Tube Life Strand 6 | D74C2FC1-2790-4C29-B53B-56ACF02F4E76 | NULL | NULL | 2026-03-06T16:16:12.1400000 | NULL | False | False | NULL |
| 1120BD3F-BAA3-48FC-BAEC-8EF42FB397D6 | Ladle 4 | EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | NULL | NULL | 2026-03-06T16:08:08.5000000 | NULL | False | False | NULL |
| 10BB11C5-D453-4422-8546-8CABCDC1E52F | EAF EBT Tube  (Eccentric Bottom Tapping) | 66A8C44E-B9D9-4088-A59D-EEEF2A8E0189 | NULL | NULL | 2026-03-06T16:16:12.1000000 | NULL | False | False | NULL |
| 0B431AFE-B584-4788-B274-7C022A44DDF6 | Tundish 5 | F701E12D-9AEE-4999-94D1-EB71A16E8306 | NULL | NULL | 2026-03-06T16:16:12.1430000 | NULL | False | False | NULL |
| 080837CE-C504-4137-9F8A-1A4AF71A4B05 | LRF Delta | BCE2C14C-72ED-42F0-8245-1A0E9D16CC42 | NULL | NULL | 2026-03-06T16:16:12.1400000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C6FC61F3-952B-4846-B159-837332463A04 | Ladle 8 | EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-10T17:15:15.7570000 | 2026-04-10T17:15:15.0000000 | False | False | NULL |
| C793DC98-07B1-44D2-A702-6D26AC5391B5 | Ladle 7 | EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-04-10T17:15:06.2900000 | 2026-04-10T17:15:06.0000000 | False | False | NULL |
| 9D5386D7-1C1E-4C62-A6D6-73EB94A9C733 | EAF Shell 2 | 4C247527-1739-4411-AFD6-375FD37F3288 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-07T13:13:33.4400000 | 2026-03-07T13:13:33.0000000 | False | False | NULL |
| BA5ACACA-8320-43B3-BD70-329D72472D16 | EAF Shell 1 | 4C247527-1739-4411-AFD6-375FD37F3288 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-07T13:09:02.8900000 | 2026-03-07T13:09:02.0000000 | False | False | NULL |
| 033C6E08-97BA-4BCE-932D-73A007147069 | Ladle 1 | EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-03-06T16:04:51.2970000 | 2026-03-06T16:04:51.0000000 | False | False | NULL |
| 69D673AB-853D-4C35-8A52-1E81F7FB4DF3 | Mould Tube Life Strand 3 | D74C2FC1-2790-4C29-B53B-56ACF02F4E76 | NULL | NULL | 2026-03-06T16:16:12.1400000 | NULL | False | False | NULL |
| 61A4B6AA-0E10-4CD6-B79B-17ED4173EE00 | Mould Tube Life Strand 2 | D74C2FC1-2790-4C29-B53B-56ACF02F4E76 | NULL | NULL | 2026-03-06T16:16:12.1400000 | NULL | False | False | NULL |
| 558DB9C2-A8AE-4418-BB90-683B0CE81CF7 | Ladle 3 | EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | NULL | NULL | 2026-03-06T16:08:08.5000000 | NULL | False | False | NULL |
| 4E0BD845-B867-45A4-A026-EFE3E4895516 | Ladle 2 | EB1AA84A-C2EB-4B06-8AE4-DB11F372A35C | NULL | NULL | 2026-03-06T16:08:08.4600000 | NULL | False | False | NULL |
| 49AECE88-3E5A-43FA-AD55-B1E9A66FE998 | Mould Tube Life Strand 4 | D74C2FC1-2790-4C29-B53B-56ACF02F4E76 | NULL | NULL | 2026-03-06T16:16:12.1400000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Per_Heat_LadleNo.EAFShellNo` -> `XStudio_XBatch.XMES_Life_Element_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Per_Heat_LadleNo.LadleNo` -> `XStudio_XBatch.XMES_Life_Element_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Per_Heat_LadleNo.TundishNo` -> `XStudio_XBatch.XMES_Life_Element_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_ActiveLife_Element_Mst_Tbl.ElementNameID` -> `XStudio_XBatch.XMES_Life_Element_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Element_Life_Counter_Trn_Tbl.ElementNameID` -> `XStudio_XBatch.XMES_Life_Element_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Life_Element_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_Life_Element_Type_Mst_Tbl.ID` (Many to One)
