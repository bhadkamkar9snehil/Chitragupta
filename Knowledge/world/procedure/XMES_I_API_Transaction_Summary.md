---
type: procedure
title: "XMES_I_API_Transaction_Summary"
built: "2026-09-24T11:36:36"
---

# XMES_I_API_Transaction_Summary

Parameters: @transactionid varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Heat_Chemistry_Quality_Data: SAPTransactionID
- MES_SAP_By_Product_Trn_Tbl: Saptransactionid
- MES_SAP_Consumption_Trn_Tbl: PostingMaterialType, Saptransactionid
- MES_SAP_Production_Trn_Tbl: PostingMaterialType, Saptransactionid
- MES_SAP_UsageDecision_Trn_Tbl: MaterialType, SAPTransactionID
- XMES_SAP_Batch_Characteristic_Trn_Tbl: Saptransactionid
- XMES_SAP_CreateBatch_Mst_Tbl: SAPTransactionID
- XMES_SAP_PlantToPlantTransfer_Trn_Tbl: SAPTransactionID

## Writes (named in its SQL text)

- XMES_API_Transaction_Summary_Fact_Tbl

## What its own log shows

553,206 log rows, 2026-03-20 00:40 to 2026-07-08 23:45.

Steps:
- Completed
- Cursor Cur on #Txn Process End
- Cursor Cur on #Txn Process Start
- Entered
- Insert API transaction Summary Fact Table Using #Txn Process End
- Insert API transaction Summary Fact Table Using #Txn Process Start
- Set EntityName When Caller type scheduler in Cur Process End
- Set EntityName When Caller type scheduler in Cur Process Start
- Set Host and Username When Entity and Recordid have value in Cur Process End
- Set Host and Username When Entity and Recordid have value in Cur Process Start
- Store in #Txn One row per TransactionID From #TxnBase Process End
- Store in #Txn One row per TransactionID From #TxnBase Process Start
- Store in #TxnBase Transactionid wise Latest Record Process End
- Store in #TxnBase Transactionid wise Latest Record Process Start
- Update #Txn Entity, Host and Username in Cur Process End
- Update #Txn Entity, Host and Username in Cur Process Start
- Update API transaction Summary Fact Table Using #Txn Process End
- Update API transaction Summary Fact Table Using #Txn Process Start

Example call: `EXEC XStudio_Xbatch.dbo.XMES_I_API_Transaction_Summary @transactionid='fffdd1ab-26bc-453e-88be-4c52a314bc72'`
