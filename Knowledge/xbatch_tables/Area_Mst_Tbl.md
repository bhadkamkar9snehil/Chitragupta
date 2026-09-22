# XStudio_Xbatch.dbo.Area_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference module, asset, enabled, handover, identification, idlist, properties, role, shift, type.

**Primary Key:** ID  
**Row Count:** 8  
**Date Range (ModifiedOn):** 2025-07-11T11:47:12.0000000 to 2026-07-27T08:18:19.0000000  

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
| AssetIdentificationProperties | varchar | YES | -1 | — |
| ShiftID | varchar | YES | 36 | — |
| RoleIDList | varchar | YES | -1 | — |
| IsHandoverEnabled | bit | YES | — | — |
| ModuleID | varchar | YES | 36 | — |
| ModuleType | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5FF54C4A-067F-49D8-80E9-5F4236B03947 | EAF | 3EFA5ED2-CE26-4963-8D83-9BCFAEFB17AC | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11T11:47:12.4600000 | 2025-07-11T11:47:12.0000000 | False | False | NULL |
| B88E9146-D9DC-46D1-A46D-FC30CB5312DF | CCM | 3EFA5ED2-CE26-4963-8D83-9BCFAEFB17AC | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-11T17:22:53.7300000 | 2025-07-11T17:22:53.0000000 | False | False | NULL |
| 27D51105-BEE2-48FD-8AB8-8ADAD48DE71C | LRF | 3EFA5ED2-CE26-4963-8D83-9BCFAEFB17AC | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2025-07-22T10:35:08.3730000 | 2025-07-22T10:35:08.0000000 | False | False | NULL |
| E6817AFA-687E-408D-811A-986D2ED7922B | Reheating Furnace | F3DFBC4E-C2AD-46F6-A07C-CDF8F13B51FE | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-03T15:09:46.0430000 | 2025-09-03T15:09:46.0000000 | False | False | NULL |
| 6AD120D8-55E8-4AC4-A101-E3E0DF8A293C | WRM | F3DFBC4E-C2AD-46F6-A07C-CDF8F13B51FE | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-16T15:24:50.9500000 | 2025-09-16T15:24:50.0000000 | False | False | NULL |
| 3900221B-23BA-47F7-8145-F493B6C9B521 | Mill | F3DFBC4E-C2AD-46F6-A07C-CDF8F13B51FE | E85231EB-0A04-42D6-A407-328F17EADEFE | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-09-22T12:32:59.1300000 | 2025-09-22T12:32:59.0000000 | False | False | NULL |
| F3F72E9E-5C9A-4D96-8D6C-7BB5D9C3B637 | Rebar | F3DFBC4E-C2AD-46F6-A07C-CDF8F13B51FE | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T09:51:59.2500000 | 2025-11-26T09:51:59.0000000 | False | False | NULL |
| 1854741B-7070-4269-9390-D60CB9E00A6D | Common | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:18:19.1600000 | 2026-07-27T08:18:19.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Area_Mst_Tbl.ParentID` -> `XStudio_XBatch.Plant_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Area_Mst_Tbl.ShiftID` -> `XStudio_XBatch.XStudio_Shift_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.CCM_SMS_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Communication_System_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.EAF_SMS_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Life_Tracking.Area` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_SMS_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Procedure_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Furnace_Combustion_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Mill_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Rebar_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_WRM_Mst_Tbl.AreaID` -> `XStudio_XBatch.Area_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Tag_Configuration.Area` -> `XStudio_XBatch.Area_Mst_Tbl.Name` (Many to One)
