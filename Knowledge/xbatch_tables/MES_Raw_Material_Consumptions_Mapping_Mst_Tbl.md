# XStudio_Xbatch.dbo.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference material, attributeids, entityids, materialid, name, raw, srno, type, unitid.

**Primary Key:** ID  
**Row Count:** 57  
**Date Range (ModifiedOn):** 2026-01-02T08:33:00.1470000 to 2026-08-08T09:17:23.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| RawMaterialName | varchar | YES | 100 | — |
| Materialid | varchar | YES | -1 | — |
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
| MaterialType | varchar | YES | 100 | — |
| Srno | int | YES | 10,0 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Unitid | varchar | YES | 36 | — |
| Entityids | varchar | YES | -1 | — |
| Attributeids | varchar | YES | -1 | — |

### Top 10 Records

| ID | RawMaterialName | Materialid | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 224129C4-AC91-498D-8F1B-99FA91874CA4 | SCRAP LIGHT MELTING BALED STEEL | 1C7B66B3-70E4-48EA-99B9-DC654EAF9D2E | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |
| 075BD601-EE9E-47A4-99B3-F0E854C16DB6 | H.C. FERRO MANGANESE 75 | B84FCFCC-9261-48CA-9384-A8EDAA1A26F6 | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |
| 056DECE8-A33F-4F85-BCC7-E7EE6715D6AD | BL_CUT PIECE MIXED | ED290962-6FAC-4A00-9DCD-8BDCD0DF5323 | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |
| 6CFBA66C-619B-427F-9885-2351FD046435 | ENDCUT_NA | 6E91E75F-19C7-41E9-B3FC-7C2FE395CF46 | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | True | False | NULL |
| 7166B82D-C1A8-483F-B0D8-8DBD016F69E5 | JSIS SKULL | 415FE2A3-487F-422C-A7A2-68B31CD4DD1C | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |
| 7FC3C025-6BA3-414D-BD10-76489C970690 | POOL IRON | 85D353CA-10C5-4C4A-8F1B-EFE3698C94D1 | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |
| 8341FD55-8087-4B02-BD5C-95D149011618 | REBAR DEFECTIVE | 8AE51120-5735-417D-87D6-2B68E712D091 | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |
| 84E3A77C-4931-4296-B04A-625563AA5E2C | WIREROD DEFECTIVE | AD792656-AF50-4B60-B82F-D4616675796C | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |
| 869A634B-D900-478A-A256-6550C98A1D2B | WRM END CUT | 6120578A-6EAB-4BD0-955A-DCF69596DBBC | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |
| 8A9A2C9A-BC4D-44D9-8503-1A9F959064F5 | SCRAP MIX ROUNDBILLETS | 025DF9DC-CC9A-440D-9516-6CADD4A4630F | NULL | NULL | 2026-01-01T16:50:32.5100000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | RawMaterialName | Materialid | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 593B174A-543B-42E6-A0E9-2623E0BF9CA7 | RM NATURAL GAS (Nm3) | 0924E17A-FCBB-46BA-9CEB-FA718C19773D | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-27T15:51:56.2070000 | 2026-08-08T09:17:23.0000000 | False | False | NULL |
| CE4E3CFA-CAE0-4275-BC3F-DA0852E134CC | RM MAIN POWER - KWH | 4617BA9E-2211-49B7-8AD1-A9CB138344BF | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-27T16:10:00.9630000 | 2026-07-28T13:09:04.0000000 | False | False | NULL |
| 9EBCF9E6-5289-40A4-A819-B896EEF883BF | RM POTABLE WATER | 623C1A28-8F7B-411B-8187-2A20854182DB | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-27T15:58:35.2470000 | 2026-07-27T15:58:35.0000000 | False | False | NULL |
| 71000F40-C648-46AD-966D-A8EE932DA7CB | RM PROCESS WATER | 83528728-8810-43DB-A13B-EE9CBDF72FC7 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-27T15:57:04.8930000 | 2026-07-27T15:57:04.0000000 | False | False | NULL |
| 4EDF6C46-CBC9-4878-9BE5-9B4B01019899 | Ladle/Tundish covering compound | DD55C823-A84F-45A3-9658-061DA4CC9047 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-07-04T08:12:18.2300000 | 2026-07-04T08:12:18.0000000 | False | False | NULL |
| A60A06F4-A232-4F5E-91B1-CC8413D98BE8 | POTABLE WATER | 2598E7D9-E86D-43D4-888E-B3371841CF30 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-01T16:50:32.5100000 | 2026-06-30T13:26:14.0000000 | False | False | NULL |
| E94CC7C7-FDFB-44AF-B43F-2678CE504C8F | PROCESS WATER | 3D1481E6-2DAE-45F2-BAF3-849C4D126C1D | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-01T16:50:32.5100000 | 2026-06-30T13:25:47.0000000 | False | False | NULL |
| 63F26C94-6B5B-4171-8B18-B90BDEB6E4BC | PIG IRON MATERIAL | 84C40321-4962-4B86-9775-881AAD57D8E6 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-01T16:50:32.5100000 | 2026-05-22T10:00:59.0000000 | False | False | NULL |
| 9BD1F94D-EA6E-4359-8796-B6F7243CE686 | GREEN_BRIQUETTE | 210BB6CA-C334-420C-9E70-E256415CD869 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-01T16:50:32.5100000 | 2026-05-22T09:55:08.0000000 | False | False | NULL |
| 2FFCBC24-8363-460B-BBF4-6FA89B3AA425 | EAF SKULL | 156A6C90-7030-429C-92B5-1BFF5E451553 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-01-01T16:50:32.5100000 | 2026-05-22T09:54:26.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Attributeids` -> `XStudio_Configuration_XBatch.XStudio_Attribute_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Entityids` -> `XStudio_Configuration_XBatch.XStudio_Entities_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Materialid` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Unitid` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Trn_Tbl.ParentID` -> `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Material_Mst_Tbl.RawMaterialName` -> `XStudio_XBatch.MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.ID` (Many to One)
