# XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ccmremarks, chemistry, eafremarks, file, grade, lrfremarks, section, signed, upload.

**Primary Key:** ID  
**Row Count:** 9  
**Date Range (ModifiedOn):** 2026-03-10T09:01:16.0000000 to 2026-06-10T11:29:22.0000000  

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
| SectionID | varchar | YES | 36 | — |
| GradeID | varchar | YES | 36 | — |
| ChemistryID | varchar | YES | 100 | — |
| EAFRemarks | varchar | YES | -1 | — |
| LRFRemarks | varchar | YES | -1 | — |
| CCMRemarks | varchar | YES | -1 | — |
| SignedFileUpload | varchar | YES | 8000 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3E88BE8B-1F09-4143-8F4C-FF5418F1ED9D | 3SP/PS | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-03-10T11:19:09.5670000 | 2026-03-10T09:01:16.0000000 | False | False | NULL |
| 71C6B7CB-DCA5-4E92-BF60-A268672E40F9 | HHMN_16RC | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-03-10T16:50:55.8830000 | 2026-03-10T16:51:16.0000000 | False | False | NULL |
| 9ABA19F9-D91E-4144-90CA-67D2659E6936 | B500BLMNHC | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-03-09T07:56:45.6430000 | 2026-03-12T12:59:20.0000000 | False | False | NULL |
| E4B6CA68-392D-4EAD-8C31-69C5EBF225E0 | SAE1018RB | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-02-27T18:05:37.1930000 | 2026-04-13T09:38:59.5830000 | True | False | NULL |
| 8B066F94-5287-46C5-8255-51E6124EA9C3 | HHMNB500B | NULL | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-17T15:34:45.9000000 | 2026-04-24T09:02:25.0000000 | False | False | NULL |
| CC59A598-CA72-4E6D-B523-7AFF957BA5BE | CRSRM | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-05-07T13:46:42.5400000 | 2026-05-07T18:26:32.0000000 | False | False | NULL |
| 202C2918-992A-463F-B406-E73CC0609B64 | 3SP/P | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-30T11:11:17.7200000 | 2026-05-30T11:11:58.5600000 | True | False | NULL |
| 159B32A9-FAC8-499F-8554-201A795A15D8 | XF1516 | NULL | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-06-04T10:48:20.7200000 | 2026-06-07T18:29:02.0000000 | False | False | NULL |
| D50C589D-BACA-4BC0-8856-18768550C074 | 3SP/P | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 5C14DB7C-8E2D-41B1-AD93-CE867465F4AE | 2026-05-30T11:16:36.7400000 | 2026-06-10T11:29:22.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Chemistry_Deviation_Quality_Data.Grade` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_CCM_Parameters_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_CCM_Remarks_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.Grade` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.Section` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_EAF_Remarks_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_LRF_Parameters_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_LRF_Remarks_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_Super_Heat_Speed_Nozzle_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Grade_Protocol_Tapping_Additions_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (One to One)
- `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ChemistryID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ID` (One to One)
- `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.GradeID` -> `XStudio_XBatch.Grade_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` -> `XStudio_XBatch.XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.ParentID` (One to Many)
- `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.SectionID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
