---
type: table
title: "Heat_Chemistry_Quality_Data"
built: "2026-09-24T11:36:36"
---

# Heat_Chemistry_Quality_Data

Table in XStudio_Xbatch. Rows: 23,023.

## Identifiers it holds

- HeatNo: same values as key `HeatNo`
- HeatSequence: same values as key `HeatSequence`
- InspectionLot: same values as key `InspectionLot`
- SAPTransactionID: same values as key `SAPTransactionID`
- SampleName: same values as key `SampleName`

## Written by

- Quality_Spectro_IsLatestSample_Update_Usp
- SP_SMS_Heat_Chemistry_Data_Section_Selection
- XMES_SAP_Posting_Sequence_Usp
- XMES_U_Heat_Chemistry_status_Usp
- XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP
- XSTUDIO_WORKFLOW_C5631C30-B02A-4FEF-B2B7-E811DB1A0B59_SP (text)
- Xstudio_Heat_Chemistry_Quality_Data_USP
- usp_Quality_Spectro_BuildWideForSample

## Read by

- Quality_Spectro_IsLatestSample_Update_Usp
- SP_SMS_Heat_Chemistry_Data_Section_Selection
- XMES_I_API_Transaction_Summary
- XMES_I_SAP_GLS_LS_Production_Trn_Usp
- XMES_Recalculate_HEAT_CHEMISTRY_DEVIATION_Usp
- XMES_SAP_Posting_Sequence_Usp
- XMES_SAP_ResultRecording_API_Error_Usp
- XMES_SP_HEAT_CHEMISTRY_DEVIATION
- XMES_SP_HEAT_CHEMISTRY_REPORT_DATA
- XMES_U_Heat_Chemistry_status_Usp
- XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP
- XSTUDIO_WORKFLOW_C5631C30-B02A-4FEF-B2B7-E811DB1A0B59_SP
- Xstudio_Heat_Chemistry_Quality_Data_USP

## Columns

- ID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- Ceq decimal
- W decimal
- ReportedTime datetime
- Nb decimal
- HeatNo varchar(100)
- Chemist varchar(100)
- Pb decimal
- Grade varchar(100)
- Sn decimal
- Shift varchar(100)
- Remarks varchar(-1)
- Ca decimal
- MnPerSi decimal
- Al decimal
- Si decimal
- SampleType varchar(100)
- C decimal
- Cu decimal
- V decimal
- N2PPM decimal
- SampleName varchar(100)
- SampleID varchar(36)
- Section varchar(100)
- TI decimal
- Date datetime
- S decimal
- SrNo int
- Mo decimal
- ReportDate varchar(100)
- Ni decimal
- Cr decimal
- Co decimal
- MnPerS decimal
- P decimal
- ReceivedTime datetime
- B decimal
- As decimal
- Mn decimal
- XMLCreatedon datetime
- MethodName varchar(100)
- Instrument varchar(100)
- Status varchar(50)
- Ag decimal
- Bi decimal
- Fe decimal
- Sb decimal
- Ta decimal
- Zr decimal
- Ce decimal
- SampleNo varchar(100)
- IsLatestSample bit
- InspectionLot varchar(100)
- IsUDStatus bit
- RRStatus varchar(100)
- SAPTransactionID varchar(100)
- Message varchar(-1)
- SAPStatus varchar(50)
- InspOper varchar(100)
- N2 decimal
- HeatSequence varchar(100)
