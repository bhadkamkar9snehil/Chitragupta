# XStudio_Xbatch.dbo.XMES_UK_CARES

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference message, lot, mic, bbendtest, bexported, blrib, brebendtest, che, chemical, code, darea, dcarbocequiv.

**Primary Key:** ID  
**Row Count:** 7  

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
| UID | int | YES | 10,0 | — |
| LMILLID | int | YES | 10,0 | — |
| LCERTIFICATEID | varchar | YES | 100 | — |
| SCERTIFICATENUMBER | varchar | YES | 100 | — |
| SCASTNUMBER | varchar | YES | 100 | — |
| SDIGITALRECORDGUID | varchar | YES | 100 | — |
| SPRODUCTDESCRIPTION | varchar | YES | 100 | — |
| LSTANDARD | int | YES | 10,0 | — |
| LFORMAT | int | YES | 10,0 | — |
| LFINISHING | int | YES | 10,0 | — |
| DDIAM | decimal | YES | 18,4 | — |
| LLENGTH | int | YES | 10,0 | — |
| SSTEELPROCESS | varchar | YES | 100 | — |
| DCHEMCOMPC | decimal | YES | 18,4 | — |
| DCHEMCOMPSI | decimal | YES | 18,4 | — |
| DCHEMCOMPMN | decimal | YES | 18,4 | — |
| DCHEMCOMPP | decimal | YES | 18,4 | — |
| DCHEMCOMPS | decimal | YES | 18,4 | — |
| DCHEMCOMPCR | decimal | YES | 18,4 | — |
| DCHEMCOMPMO | decimal | YES | 18,4 | — |
| DCHEMCOMPNI | decimal | YES | 18,4 | — |
| DCHEMCOMPCU | decimal | YES | 18,4 | — |
| DCHEMCOMPV | decimal | YES | 18,4 | — |
| DCHEMCOMPNB | decimal | YES | 18,4 | — |
| DCHEMCOMPN | decimal | YES | 18,4 | — |
| DCHEMCOMPB | decimal | YES | 18,4 | — |
| DCHEMCOMPAL | decimal | YES | 18,4 | — |
| DCHEMCOMPSN | decimal | YES | 18,4 | — |
| DCARBOCEQUIV | decimal | YES | 18,4 | — |
| BEXPORTED | bit | YES | — | — |
| LTESTLINENUMBER | int | YES | 10,0 | — |
| DAREA | decimal | YES | 18,4 | — |
| DMASSPERMETER | decimal | YES | 18,4 | — |
| DYIELDSTRENGTH | decimal | YES | 18,4 | — |
| DTENSILESTRENGTH | decimal | YES | 18,4 | — |
| DRATIO | decimal | YES | 18,4 | — |
| DELONGATIONAS | decimal | YES | 18,4 | — |
| DELONGATIONAGT | decimal | YES | 18,4 | — |
| BBENDTEST | bit | YES | — | — |
| BREBENDTEST | bit | YES | — | — |
| BLRIB | bit | YES | — | — |
| SWORKSORDER | varchar | YES | 100 | — |
| SCUSTOMERORDERNUMBER | varchar | YES | 100 | — |
| LBUNDLESIZE | int | YES | 10,0 | — |
| DTDESPATCH | datetime | YES | — | — |
| DTTEST | datetime | YES | — | — |
| SPORTDISCHARGE | varchar | YES | 100 | — |
| SCOUNTRYDISCHARGE | varchar | YES | 100 | — |
| SSHIPID | varchar | YES | 100 | — |
| STESTGUID | varchar | YES | 100 | — |
| MEC_LOT | varchar | YES | 100 | — |
| CHE_LOT | varchar | YES | 100 | — |
| MATERIAL_CODE | varchar | YES | 100 | — |
| MESSAGE | varchar | YES | -1 | — |
| MECHANICAL_MIC_MESSAGE | varchar | YES | -1 | — |
| CHEMICAL_MIC_MESSAGE | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F3BC682D-79C7-4EDE-802A-BD27E325741C | NULL | NULL | NULL | NULL | 2026-08-19T08:18:44.2570000 | NULL | False | False | NULL |
| 9B2C8443-AFB1-4B8B-954C-3F5F18839AAA | NULL | NULL | NULL | NULL | 2026-08-19T08:18:44.2570000 | NULL | False | False | NULL |
| 8E2764D4-3CA1-4E35-ACAA-A97095C6E6ED | NULL | NULL | NULL | NULL | 2026-08-19T08:18:44.2570000 | NULL | False | False | NULL |
| 7CBE1BB4-31B0-44F2-B531-F5B174A2AFFF | NULL | NULL | NULL | NULL | 2026-08-19T08:18:44.2570000 | NULL | False | False | NULL |
| 795FF74E-9B34-408D-B171-F9AB43AB729B | NULL | NULL | NULL | NULL | 2026-08-19T08:18:44.2570000 | NULL | False | False | NULL |
| 59D5FA58-3F7D-4C10-A3E8-06E7A461C4AF | NULL | NULL | NULL | NULL | 2026-08-19T08:18:44.2570000 | NULL | False | False | NULL |
| 149444CB-527C-4A1A-A0C7-B7B0E9E2766D | NULL | NULL | NULL | NULL | 2026-08-19T08:18:44.2570000 | NULL | False | False | NULL |

---
