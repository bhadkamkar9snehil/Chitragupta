# XStudio_Xbatch.dbo.Transformer_6_6kv

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference ecr, tra, mvapcurrent, mvascurrent, level, status, mvabreather, mvaoil, mvaoti, mvawti, amvapcurrent, amvascurrent.

**Primary Key:** ID  
**Row Count:** 455  
**Date Range (ModifiedOn):** 2025-08-02T10:25:16.0000000 to 2026-09-01T01:20:37.0000000  

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
| ECR1Tra3MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR1Tra3MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR1Tra3MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR1Tra3MVASCurrentR | decimal | YES | 18,4 | — |
| ECR1Tra3MVASCurrentY | decimal | YES | 18,4 | — |
| ECR1Tra3MVASCurrentB | decimal | YES | 18,4 | — |
| ECR1Tra3MVAOTI | decimal | YES | 18,4 | — |
| ECR1Tra3MVAWTI | decimal | YES | 18,4 | — |
| ECR1Tra3MVAOilLevel | decimal | YES | 18,4 | — |
| ECR1Tra3MVABreatherStatus | bit | YES | — | — |
| ECR1Tra16MVAOTI | decimal | YES | 18,4 | — |
| ECR1Tra16MVAWTI | decimal | YES | 18,4 | — |
| ECR1Tra16MVAOilLevel | decimal | YES | 18,4 | — |
| ECR1Tra16MVABreatherStatus | bit | YES | — | — |
| ECR1Tra16MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR1Tra16MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR1Tra16MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR1Tra16MVASCurrentR | decimal | YES | 18,4 | — |
| ECR1Tra16MVASCurrentY | decimal | YES | 18,4 | — |
| ECR1Tra16MVASCurrentB | decimal | YES | 18,4 | — |
| ECR2Tra3MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR2Tra3MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR2Tra3MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR2Tra3MVASCurrentR | decimal | YES | 18,4 | — |
| ECR2Tra3MVASCurrentY | decimal | YES | 18,4 | — |
| ECR2Tra3MVASCurrentB | decimal | YES | 18,4 | — |
| ECR2Tra3MVAOTI | decimal | YES | 18,4 | — |
| ECR2Tra3MVAWTI | decimal | YES | 18,4 | — |
| ECR2Tra3MVAOilLevel | decimal | YES | 18,4 | — |
| ECR2Tra3MVABreatherStatus | bit | YES | — | — |
| ECR2Tra4MVAOTI | decimal | YES | 18,4 | — |
| ECR2Tra4MVAWTI | decimal | YES | 18,4 | — |
| ECR2Tra4MVAOilLevel | decimal | YES | 18,4 | — |
| ECR2Tra4MVABreatherStatus | bit | YES | — | — |
| ECR2Tra4MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR2Tra4MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR2Tra4MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR2Tra4MVASCurrentR | decimal | YES | 18,4 | — |
| ECR2Tra4MVASCurrentY | decimal | YES | 18,4 | — |
| ECR2Tra4MVASCurrentB | decimal | YES | 18,4 | — |
| ECR3Tra3MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR3Tra3MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR3Tra3MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR3Tra3MVASCurrentR | decimal | YES | 18,4 | — |
| ECR3Tra3MVASCurrentY | decimal | YES | 18,4 | — |
| ECR3Tra3MVASCurrentB | decimal | YES | 18,4 | — |
| ECR3Tra3MVAOTI | decimal | YES | 18,4 | — |
| ECR3Tra3MVAWTI | decimal | YES | 18,4 | — |
| ECR3Tra3MVAOilLevel | decimal | YES | 18,4 | — |
| ECR3Tra3MVABreatherStatus | bit | YES | — | — |
| ECR3Tra1MVAOTI | decimal | YES | 18,4 | — |
| ECR3Tra1MVAWTI | decimal | YES | 18,4 | — |
| ECR3Tra1MVAOilLevel | decimal | YES | 18,4 | — |
| ECR3Tra1MVABreatherStatus | bit | YES | — | — |
| ECR3Tra1MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR3Tra1MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR3Tra1MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR3Tra1MVASCurrentR | decimal | YES | 18,4 | — |
| ECR3Tra1MVASCurrentY | decimal | YES | 18,4 | — |
| ECR3Tra1MVASCurrentB | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR3TraBF12MVASCurrentR | decimal | YES | 18,4 | — |
| ECR3TraBF12MVASCurrentY | decimal | YES | 18,4 | — |
| ECR3TraBF12MVASCurrentB | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAOTI | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAWTI | decimal | YES | 18,4 | — |
| ECR3TraBF12MVAOilLevel | decimal | YES | 18,4 | — |
| ECR3TraBF12MVABreatherStatus | bit | YES | — | — |
| ECR4Tra3MVAPCurrentY | decimal | YES | 18,4 | — |
| ECR4Tra3MVAPCurrentR | decimal | YES | 18,4 | — |
| ECR4Tra3MVAPCurrentB | decimal | YES | 18,4 | — |
| ECR4Tra3MVASCurrentR | decimal | YES | 18,4 | — |
| ECR4Tra3MVASCurrentY | decimal | YES | 18,4 | — |
| ECR4Tra3MVASCurrentB | decimal | YES | 18,4 | — |
| ECR4Tra3MVAOTI | decimal | YES | 18,4 | — |
| ECR4Tra3MVAWTI | decimal | YES | 18,4 | — |
| ECR4Tra3MVAOilLevel | decimal | YES | 18,4 | — |
| ECR4Tra3MVABreatherStatus | bit | YES | — | — |
| ECR4Tra3AMVAPCurrentY | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAPCurrentR | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAPCurrentB | decimal | YES | 18,4 | — |
| ECR4Tra3AMVASCurrentR | decimal | YES | 18,4 | — |
| ECR4Tra3AMVASCurrentY | decimal | YES | 18,4 | — |
| ECR4Tra3AMVASCurrentB | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAOTI | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAWTI | decimal | YES | 18,4 | — |
| ECR4Tra3AMVAOilLevel | decimal | YES | 18,4 | — |
| ECR4Tra3AMVABreatherStatus | bit | YES | — | — |
| Attendants | varchar | YES | 36 | — |
| Remarks | varchar | YES | -1 | — |
| Shift | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6E83BC54-75DC-4472-ADE0-029255AC7B2D | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-22T13:24:24.7470000 | 2025-08-02T10:25:16.0000000 | False | False | NULL |
| 92DD25E8-CDCD-4B3B-B874-04F96DFF67CB | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-17T20:02:43.8000000 | 2025-08-17T20:02:43.0000000 | False | False | NULL |
| 47AC5FA9-9F6A-47D0-B936-B020BB02B023 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-10-15T22:39:20.8830000 | 2025-10-15T22:39:20.0000000 | False | False | NULL |
| 5B87B4FC-60EB-4D0E-A376-A6645801587C | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-22T21:19:05.8070000 | 2025-10-22T21:19:05.0000000 | False | False | NULL |
| A345FC73-12DC-4E7D-8F79-1CFFBBE890BC | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:06:25.8170000 | 2025-10-24T04:06:25.0000000 | False | False | NULL |
| 517C292A-1D3D-498F-93E3-D63772E6B2D3 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-24T04:33:15.8500000 | 2025-10-24T04:33:15.0000000 | False | False | NULL |
| E37E95E6-7694-4E41-A3CA-69CBF014F6F6 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-25T20:54:11.2000000 | 2025-10-25T20:54:11.0000000 | False | False | NULL |
| 37BECF3B-3116-4859-9F17-57DA684B45D1 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T02:10:47.4870000 | 2025-10-28T02:10:47.0000000 | False | False | NULL |
| 07D3404D-2121-4971-8F65-E84CAFD9DCE6 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-27T02:17:11.1970000 | 2025-10-28T02:14:02.0000000 | False | False | NULL |
| ADF2DEC9-34F6-4E1B-BF4F-C018E1FB93B1 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-10-28T09:32:57.3330000 | 2025-10-28T09:32:57.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9B130CE6-47A0-4D64-9BCF-CC2A94FB59B8 | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T00:55:57.6130000 | 2026-09-01T01:20:37.0000000 | False | False | NULL |
| 4B06D695-6411-4F3E-A2DE-3BA564725D00 | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T01:06:17.5970000 | 2026-09-01T01:06:17.0000000 | False | False | NULL |
| 9DD58F00-7581-4AC7-B6FA-1DDCFC1FBB74 | NULL | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-21T18:57:47.7600000 | 2026-08-31T07:29:14.0000000 | False | False | NULL |
| FD5DF21F-5C44-4119-9276-9293E6B7B5FA | NULL | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-08-30T23:27:38.2800000 | 2026-08-30T23:27:56.0000000 | False | False | NULL |
| FB583DBC-0600-4E24-929E-6CBF8874CDF6 | NULL | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-08-20T23:43:45.9470000 | 2026-08-21T00:46:36.0000000 | False | False | NULL |
| 2BEF6C35-F2D9-432C-81EB-AEE4119957FE | NULL | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T05:13:27.5070000 | 2026-08-20T05:13:27.0000000 | False | False | NULL |
| 4264A7F9-0AA0-4385-835B-D524B8612D66 | NULL | NULL | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 674CF3CE-292B-4E92-84D8-1A3D429723E2 | 2026-08-20T05:04:19.8900000 | 2026-08-20T05:04:19.0000000 | False | False | NULL |
| DCB5B30C-4650-4D5B-BA52-922D5F80FBBC | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-19T02:07:08.7900000 | 2026-08-19T02:16:41.0000000 | False | False | NULL |
| F1E6CFC7-3EA2-4FBA-AC1D-EB4236FEDF18 | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-17T01:58:12.8930000 | 2026-08-17T01:58:12.0000000 | False | False | NULL |
| 79B76F5E-E635-4096-9872-155845FC2282 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-09T01:02:43.7130000 | 2026-07-09T01:02:43.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Transformer_6_6kv.Attendants` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
