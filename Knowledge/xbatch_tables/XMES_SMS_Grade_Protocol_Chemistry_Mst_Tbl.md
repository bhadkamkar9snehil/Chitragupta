# XStudio_Xbatch.dbo.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference aim, max, min, per, ppm, saim, smax, smin, caim, cmax, cmin, paim.

**Primary Key:** ID  
**Row Count:** 11  
**Date Range (ModifiedOn):** 2026-03-10T11:38:44.0000000 to 2026-06-07T18:23:30.0000000  

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
| CMin | decimal | YES | 18,2 | — |
| CMax | decimal | YES | 18,2 | — |
| CAim | decimal | YES | 18,4 | — |
| MnMin | decimal | YES | 18,4 | — |
| MnMax | decimal | YES | 18,4 | — |
| MnAim | decimal | YES | 18,4 | — |
| SMin | decimal | YES | 18,2 | — |
| SMax | decimal | YES | 18,2 | — |
| SAim | decimal | YES | 18,2 | — |
| PMax | decimal | YES | 18,2 | — |
| PMin | decimal | YES | 18,2 | — |
| PAim | decimal | YES | 18,2 | — |
| SiMin | decimal | YES | 18,2 | — |
| SiMax | decimal | YES | 18,2 | — |
| SiAim | decimal | YES | 18,2 | — |
| CuMin | decimal | YES | 18,2 | — |
| CuMax | decimal | YES | 18,2 | — |
| CuAim | decimal | YES | 18,2 | — |
| CrMin | decimal | YES | 18,2 | — |
| CrMax | decimal | YES | 18,2 | — |
| CrAim | decimal | YES | 18,2 | — |
| NiMin | decimal | YES | 18,2 | — |
| NiMax | decimal | YES | 18,2 | — |
| NiAim | decimal | YES | 18,2 | — |
| MoMin | decimal | YES | 18,4 | — |
| MoMax | decimal | YES | 18,2 | — |
| MoAim | decimal | YES | 18,4 | — |
| VMin | decimal | YES | 18,2 | — |
| VMax | decimal | YES | 18,2 | — |
| VAim | decimal | YES | 18,2 | — |
| NbMin | decimal | YES | 18,4 | — |
| NbMax | decimal | YES | 18,4 | — |
| NbAim | decimal | YES | 18,4 | — |
| TiMax | decimal | YES | 18,2 | — |
| TiAim | decimal | YES | 18,2 | — |
| TiMin | decimal | YES | 18,2 | — |
| N2ppmMin | decimal | YES | 18,2 | — |
| N2ppmMax | decimal | YES | 18,2 | — |
| N2ppmAim | decimal | YES | 18,2 | — |
| AlMax | decimal | YES | 18,2 | — |
| AlMin | decimal | YES | 18,2 | — |
| AlAim | decimal | YES | 18,2 | — |
| CeMin | decimal | YES | 18,2 | — |
| CeMax | decimal | YES | 18,2 | — |
| CeAim | decimal | YES | 18,2 | — |
| MnPerSMin | decimal | YES | 18,2 | — |
| MnPerSMax | decimal | YES | 18,2 | — |
| MnPerSAim | decimal | YES | 18,2 | — |
| MnPerSiMin | decimal | YES | 18,4 | — |
| MnPerSiMax | decimal | YES | 18,4 | — |
| MnPerSiAim | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1B6C65CA-3F6E-4998-88A3-C36877CAA9B3 | NULL | 71C6B7CB-DCA5-4E92-BF60-A268672E40F9 | NULL | NULL | 2026-03-10T16:51:16.9230000 | NULL | False | False | NULL |
| EAFB832E-2259-4311-8DDE-7C75331E8973 | NULL | 3E88BE8B-1F09-4143-8F4C-FF5418F1ED9D | NULL | NULL | 2026-03-10T11:19:09.6130000 | NULL | False | False | NULL |
| B43F3CA1-66F1-4D41-A4DF-79468ADC373E | NULL | E4B6CA68-392D-4EAD-8C31-69C5EBF225E0 | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-02-28T10:46:32.6570000 | 2026-03-10T11:38:44.0000000 | False | False | NULL |
| F9865239-D850-4C86-994B-084D8DB8A691 | NULL | 9ABA19F9-D91E-4144-90CA-67D2659E6936 | NULL | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 2026-03-09T07:56:45.9770000 | 2026-03-17T15:44:48.0000000 | False | False | NULL |
| D1FBD4BD-B259-44D0-890E-CA747682069D | NULL | CC59A598-CA72-4E6D-B523-7AFF957BA5BE | NULL | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 2026-05-07T13:46:42.5600000 | 2026-03-17T15:44:48.0000000 | False | False | NULL |
| 8E6A949D-44A4-4CAC-BFE0-5173853E739F | NULL | 202C2918-992A-463F-B406-E73CC0609B64 | NULL | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 2026-05-30T11:11:17.7630000 | 2026-03-17T15:44:48.0000000 | False | False | NULL |
| 6BF39DC6-CD3C-4668-8678-2E56CD5947D6 | NULL | 8B066F94-5287-46C5-8255-51E6124EA9C3 | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-03-17T15:34:46.1230000 | 2026-04-11T22:07:39.0000000 | False | False | NULL |
| EFB6645A-4A19-4867-876E-A6AFBA510A2A | NULL | CC59A598-CA72-4E6D-B523-7AFF957BA5BE | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-05-07T13:50:41.1600000 | 2026-05-07T18:28:35.0000000 | False | False | NULL |
| 1554A1C6-CE09-4406-88EF-464A45008D66 | NULL | D50C589D-BACA-4BC0-8856-18768550C074 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-05-30T14:17:08.2300000 | 2026-05-30T14:49:59.0000000 | False | False | NULL |
| C994E768-C953-4F40-B04A-5F9F72DC6D6A | NULL | 159B32A9-FAC8-499F-8554-201A795A15D8 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-06-04T10:49:38.5470000 | 2026-06-04T10:58:01.9270000 | True | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A9AF6A2C-FD95-45F6-A7CB-BD26F07FE158 | NULL | 159B32A9-FAC8-499F-8554-201A795A15D8 | NULL | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-06-04T10:48:20.7370000 | 2026-06-07T18:23:30.0000000 | False | False | NULL |
| C994E768-C953-4F40-B04A-5F9F72DC6D6A | NULL | 159B32A9-FAC8-499F-8554-201A795A15D8 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-06-04T10:49:38.5470000 | 2026-06-04T10:58:01.9270000 | True | False | NULL |
| 1554A1C6-CE09-4406-88EF-464A45008D66 | NULL | D50C589D-BACA-4BC0-8856-18768550C074 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-05-30T14:17:08.2300000 | 2026-05-30T14:49:59.0000000 | False | False | NULL |
| EFB6645A-4A19-4867-876E-A6AFBA510A2A | NULL | CC59A598-CA72-4E6D-B523-7AFF957BA5BE | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-05-07T13:50:41.1600000 | 2026-05-07T18:28:35.0000000 | False | False | NULL |
| 6BF39DC6-CD3C-4668-8678-2E56CD5947D6 | NULL | 8B066F94-5287-46C5-8255-51E6124EA9C3 | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-03-17T15:34:46.1230000 | 2026-04-11T22:07:39.0000000 | False | False | NULL |
| F9865239-D850-4C86-994B-084D8DB8A691 | NULL | 9ABA19F9-D91E-4144-90CA-67D2659E6936 | NULL | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 2026-03-09T07:56:45.9770000 | 2026-03-17T15:44:48.0000000 | False | False | NULL |
| 8E6A949D-44A4-4CAC-BFE0-5173853E739F | NULL | 202C2918-992A-463F-B406-E73CC0609B64 | NULL | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 2026-05-30T11:11:17.7630000 | 2026-03-17T15:44:48.0000000 | False | False | NULL |
| D1FBD4BD-B259-44D0-890E-CA747682069D | NULL | CC59A598-CA72-4E6D-B523-7AFF957BA5BE | NULL | 5035F2B5-8AA7-42D5-9595-C445C7CA5D20 | 2026-05-07T13:46:42.5600000 | 2026-03-17T15:44:48.0000000 | False | False | NULL |
| B43F3CA1-66F1-4D41-A4DF-79468ADC373E | NULL | E4B6CA68-392D-4EAD-8C31-69C5EBF225E0 | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-02-28T10:46:32.6570000 | 2026-03-10T11:38:44.0000000 | False | False | NULL |
| EAFB832E-2259-4311-8DDE-7C75331E8973 | NULL | 3E88BE8B-1F09-4143-8F4C-FF5418F1ED9D | NULL | NULL | 2026-03-10T11:19:09.6130000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ParentID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ID` (One to One)
- `XStudio_XBatch.XMES_SMS_Grade_Protocol_Mst_Tbl.ChemistryID` -> `XStudio_XBatch.XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ID` (One to One)
