# XStudio_Xbatch.dbo.XMES_Log_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference execution, query, seq, status, sub, type.

**Primary Key:** ID  
**Row Count:** 47,50,596  

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
| ExecutionQuery | nvarchar | YES | -1 | — |
| Type | varchar | YES | 100 | — |
| Status | varchar | YES | -1 | — |
| SrNo | int | YES | 10,0 | — |
| SubSeqNo | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000019FC-EA28-44E1-88A2-A8C186B87A4E | XMES_I_API_Transaction_Summary | NULL | NULL | NULL | 2026-05-24T20:48:51.9930000 | NULL | False | False | NULL |
| 00000D3B-D350-4A06-8E01-5FD0EF5C1B42 | XMES_I_API_Transaction_Summary | NULL | NULL | NULL | 2026-04-11T20:27:12.9570000 | NULL | False | False | NULL |
| 00000D14-D829-47CD-870D-7E664AEC2B0A | XMES_CREATE_BILLETNO_USP | NULL | NULL | NULL | 2026-06-29T08:32:14.5630000 | NULL | False | False | NULL |
| 00000CBC-FF5D-41A8-B248-1C82967A4CA5 | XBatch_RM_BilletWiseNGConsumption | NULL | NULL | NULL | 2026-09-21T02:02:00.5070000 | NULL | False | False | NULL |
| 00000AC9-6533-4278-9918-66DFB8D7729F | XBatch_I_Material_Consume_NoBOM_USP | NULL | NULL | NULL | 2026-06-27T06:37:20.7100000 | NULL | False | False | NULL |
| 00000A5B-11B9-4D62-A833-08E240C82BE7 | BilletsPosition_InFurnace_Usp | NULL | NULL | NULL | 2026-06-02T05:22:00.1800000 | NULL | False | False | NULL |
| 000009CD-C06E-4A3D-8C7E-232D4E668D78 | XBatch_RM_Mill_Billet_DischargeTemp | NULL | NULL | NULL | 2026-06-11T01:23:44.0100000 | NULL | False | False | NULL |
| 0000068F-C379-4E37-8150-B03FB8D40074 | XMES_BackCalculation_GLS_Usp | NULL | NULL | NULL | 2026-07-17T17:12:37.3800000 | NULL | False | False | NULL |
| 00000453-CF4F-40F4-95B1-3986F8B81E48 | XMES_CREATE_BILLETNO_USP | NULL | NULL | NULL | 2026-06-17T15:42:32.2900000 | NULL | False | False | NULL |
| 00000367-08B0-4B65-AF09-AC4319A79AEA | XBatch_RM_BilletWiseNGConsumption | NULL | NULL | NULL | 2026-06-07T13:27:18.6800000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 000019FC-EA28-44E1-88A2-A8C186B87A4E | XMES_I_API_Transaction_Summary | NULL | NULL | NULL | 2026-05-24T20:48:51.9930000 | NULL | False | False | NULL |
| 00000D3B-D350-4A06-8E01-5FD0EF5C1B42 | XMES_I_API_Transaction_Summary | NULL | NULL | NULL | 2026-04-11T20:27:12.9570000 | NULL | False | False | NULL |
| 00000D14-D829-47CD-870D-7E664AEC2B0A | XMES_CREATE_BILLETNO_USP | NULL | NULL | NULL | 2026-06-29T08:32:14.5630000 | NULL | False | False | NULL |
| 00000CBC-FF5D-41A8-B248-1C82967A4CA5 | XBatch_RM_BilletWiseNGConsumption | NULL | NULL | NULL | 2026-09-21T02:02:00.5070000 | NULL | False | False | NULL |
| 00000AC9-6533-4278-9918-66DFB8D7729F | XBatch_I_Material_Consume_NoBOM_USP | NULL | NULL | NULL | 2026-06-27T06:37:20.7100000 | NULL | False | False | NULL |
| 00000A5B-11B9-4D62-A833-08E240C82BE7 | BilletsPosition_InFurnace_Usp | NULL | NULL | NULL | 2026-06-02T05:22:00.1800000 | NULL | False | False | NULL |
| 000009CD-C06E-4A3D-8C7E-232D4E668D78 | XBatch_RM_Mill_Billet_DischargeTemp | NULL | NULL | NULL | 2026-06-11T01:23:44.0100000 | NULL | False | False | NULL |
| 0000068F-C379-4E37-8150-B03FB8D40074 | XMES_BackCalculation_GLS_Usp | NULL | NULL | NULL | 2026-07-17T17:12:37.3800000 | NULL | False | False | NULL |
| 00000453-CF4F-40F4-95B1-3986F8B81E48 | XMES_CREATE_BILLETNO_USP | NULL | NULL | NULL | 2026-06-17T15:42:32.2900000 | NULL | False | False | NULL |
| 00000367-08B0-4B65-AF09-AC4319A79AEA | XBatch_RM_BilletWiseNGConsumption | NULL | NULL | NULL | 2026-06-07T13:27:18.6800000 | NULL | False | False | NULL |

---
