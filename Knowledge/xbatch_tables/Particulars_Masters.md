# XStudio_Xbatch.dbo.Particulars_Masters

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference particulars, type, uom.

**Primary Key:** ID  
**Row Count:** 62  
**Date Range (ModifiedOn):** 2025-09-18T14:55:58.0000000 to 2026-02-07T11:43:58.0000000  

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
| ParentID | varchar | YES | 36 | — |
| UOM | varchar | YES | 100 | — |
| Type | varchar | YES | 100 | — |
| SrNo | int | YES | 10,0 | — |
| Name | varchar | YES | 100 | — |
| ReportDate | datetime | YES | — | — |
| Particulars | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0321E68E-16FC-4629-ADFC-E26C747FCFDA | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 12056D72-D8CF-465B-9067-FF121265156B | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 117CA496-C342-49F6-8437-19339418C787 | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 0A794C52-4124-4C6D-8421-B926C909C352 | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 210F09FF-09E5-4B67-9452-2AEE34BD060B | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 1DD64BC9-DB2C-4773-A5A7-E439A51ADDFF | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 1C82B81F-412C-472A-B0DD-B4681D000A43 | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 1B7FD13A-ECEF-46E6-BFE5-7DFB41AF8F99 | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 146CA42D-FC46-4AC3-86FB-7EE4CBCE440A | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |
| 21EDFF3B-37F9-4C50-8467-812E70A149E5 | NULL | NULL | 2025-09-04T08:09:09.1170000 | NULL | False | False | NULL | NULL |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5204129D-4F8A-4B4F-813A-B87810C4FDCE | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-02-07T11:42:23.7400000 | 2026-02-07T11:43:58.0000000 | False | False | NULL | 10.76.5.79 | NULL |
| D91AADF7-8D2D-4DFE-B038-D9C3954E061C | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-04T08:09:09.1170000 | 2026-02-07T11:40:38.0000000 | False | False | NULL | 10.76.5.79 |  |
| 929C9EDE-1659-4B59-9A15-83E388180B6A | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-04T08:09:09.1170000 | 2025-10-10T14:42:36.0000000 | False | False | NULL | 172.16.3.201 |  |
| C4B156C7-FE2A-491E-AE3D-74C4EE7006CA | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-04T08:09:09.1170000 | 2025-10-10T14:07:26.0000000 | False | False | NULL | 172.16.3.201 |  |
| 8AEB160A-BEEF-4A82-9CFA-865CBBDFA788 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-04T08:09:09.1170000 | 2025-10-10T14:06:37.5200000 | True | False | NULL | 172.16.3.201 |  |
| ECD31656-03BB-45CD-998E-AD2276922C93 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-04T08:09:09.1170000 | 2025-10-10T14:06:22.0000000 | False | False | NULL | 172.16.3.201 |  |
| F56E5846-D67D-4684-897B-B35BF61A2C34 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-04T08:09:09.1170000 | 2025-10-10T14:06:12.0000000 | False | False | NULL | 172.16.3.201 |  |
| 060107DD-5070-4D48-B839-546A0F653059 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-04T08:09:09.1170000 | 2025-10-10T14:04:58.0000000 | False | False | NULL | 172.16.3.201 |  |
| D7C4D769-DE1F-40B7-82F6-A3F649CA1F35 | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-04T08:09:09.1170000 | 2025-10-10T14:04:47.0000000 | False | False | NULL | 172.16.3.201 |  |
| 7A51B907-6B8E-4E94-8F29-6B8B3895627B | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-04T08:09:09.1170000 | 2025-10-10T14:04:36.3830000 | True | False | NULL | 172.16.3.201 |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.SMS_Production_Summary.Particulars` -> `XStudio_XBatch.Particulars_Masters.Particulars` (Many to One)
- `XStudio_XBatch.SMS_Production_Summary.Type` -> `XStudio_XBatch.Particulars_Masters.Type` (Many to One)
- `XStudio_XBatch.SMS_Production_Summary.UOM` -> `XStudio_XBatch.Particulars_Masters.UOM` (Many to One)
