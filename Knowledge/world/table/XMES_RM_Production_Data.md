---
type: table
title: "XMES_RM_Production_Data"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Production_Data

Table in XStudio_Xbatch. Rows: 821.

## Identifiers it holds

- BatchNo: same values as key `HeatNo`
- BilletNo: same values as key `BilletNo`
- HeatNo: same values as key `HeatNo`

## Written by

- MES_M_Strand
- XMES_RM_I_EndproductNo_New_Entry_Usp
- XSTUDIO_WORKFLOW_19910303-DE98-45A2-909B-EF83E8EAD0BA_SP (text)
- XSTUDIO_WORKFLOW_9A172601-2557-4597-B6A4-CDE39CA602BB_SP

## Read by

- MES_M_Strand
- XMES_RM_I_EndproductNo_New_Entry_Usp
- XMES_RM_Production_Summary_Usp
- XMES_RM_SAP_Posting_Sequence_Usp
- XMES_SAP_I_EndProduct_Production_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XSTUDIO_WORKFLOW_19910303-DE98-45A2-909B-EF83E8EAD0BA_SP
- XSTUDIO_WORKFLOW_9A172601-2557-4597-B6A4-CDE39CA602BB_SP

## Columns

- ID varchar(36)
- Workorderid varchar(-1)
- ParentID varchar(36)
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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- EndProductid varchar(-1)
- BilletNo varchar(100)
- BatchNo varchar(100)
- HeatNo varchar(100)
- SectionLength varchar(100)
- BundleWeightTon decimal
- NoofPieces int
- EndProductNo varchar(100)
- ByproductEndCut decimal
- ByproductMillScale decimal
- TieRodConsume decimal
- WorkflowStatus varchar(50)
- IsSapConsumed bit
- IsHotOut bit
- IsExtra bit
- IsShort bit
