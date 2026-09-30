---
type: table
title: "XBatch_Sales_Order_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Sales_Order_Mst_Tbl

Table in XStudio_Xbatch. Rows: 55.

## Identifiers it holds

- SalesOrderNumber: same values as key `SONumber`

## Written by

- XBatch_I_SO_USP (text)
- XBatch_U_SO_USP (text)
- XMES_AUTO_WO_AND_SO_CALCULATION
- XMES_AUTO_WO_AND_SO_CALCULATION_old
- XMES_RM_Campaign_Plan_WorkOrders_Creation
- XMES_WorkOrders_Creation
- XSTUDIO_WORKFLOW_21B64647-6F2C-4089-AEA4-54D9482E3A83_SP (text)
- XSTUDIO_WORKFLOW_29CCAEB2-7671-407A-8BC3-A40164145BD2_SP (text)
- XSTUDIO_WORKFLOW_2AF85FD5-BE15-4380-9504-341EE986C74D_SP (text)
- XSTUDIO_WORKFLOW_9B20AE0B-2E34-4BF8-9875-BB52B5C007E0_SP
- XSTUDIO_WORKFLOW_A1B200C6-5046-41BE-9CD1-84454600575D_SP
- XSTUDIO_WORKFLOW_A6D3AC4F-60D5-4423-8936-0F59CEEA2C39_SP
- XSTUDIO_WORKFLOW_C18D4DFF-8ADA-4080-9F2F-91DE212A1257_SP
- XSTUDIO_WORKFLOW_C2B0C95A-B3B7-466F-9BFE-CDCC5017EB57_SP (text)
- XSTUDIO_WORKFLOW_C67D7329-8634-4DCC-94B2-B2B950981934_SP (text)
- XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP
- XSTUDIO_WORKFLOW_E5621281-3613-41D8-BF2E-4FFB17C30EAC_SP (text)
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP
- Xstudio_XBatch_Sales_Order_Mst_Tbl_USP
- campaignplan_released_workflow_usp

## Read by

- XBatch_I_WO_USP
- XBatch_U_WO_USP
- XMES_AUTO_WO_AND_SO_CALCULATION
- XMES_AUTO_WO_AND_SO_CALCULATION_old
- XMES_I_SAP_Billet_Production_Trn
- XMES_RM_Campaign_Plan_WorkOrders_Creation
- XMES_SO_Trn_VW
- XSTUDIO_WORKFLOW_21B64647-6F2C-4089-AEA4-54D9482E3A83_SP
- XSTUDIO_WORKFLOW_29CCAEB2-7671-407A-8BC3-A40164145BD2_SP
- XSTUDIO_WORKFLOW_2AF85FD5-BE15-4380-9504-341EE986C74D_SP
- XSTUDIO_WORKFLOW_9B20AE0B-2E34-4BF8-9875-BB52B5C007E0_SP
- XSTUDIO_WORKFLOW_A1B200C6-5046-41BE-9CD1-84454600575D_SP
- XSTUDIO_WORKFLOW_A6D3AC4F-60D5-4423-8936-0F59CEEA2C39_SP
- XSTUDIO_WORKFLOW_C18D4DFF-8ADA-4080-9F2F-91DE212A1257_SP
- XSTUDIO_WORKFLOW_C2B0C95A-B3B7-466F-9BFE-CDCC5017EB57_SP
- XSTUDIO_WORKFLOW_C67D7329-8634-4DCC-94B2-B2B950981934_SP
- XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP
- XSTUDIO_WORKFLOW_E5621281-3613-41D8-BF2E-4FFB17C30EAC_SP
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP
- Xstudio_XBatch_Sales_Order_Mst_Tbl_USP
- Xstudio_XBatch_Work_Order_Mst_Tbl_USP
- campaignplan_released_workflow_usp

## Columns

- ID varchar(36)
- Name varchar(100)
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
- ItemID varchar(36)
- Quantity decimal
- UnitID varchar(36)
- ReleasedDate datetime
- ApprovedDate datetime
- ApprovedBy varchar(36)
- PlannedCompletionDate datetime
- Remarks varchar(1000)
- SalesOrderNumber varchar(100)
- ColourCode varchar(50)
- Status varchar(50)
- ProgressTonnage decimal
- ProgressPercentage decimal
- RemainingTonnage decimal
- ActualCompletionDate datetime
- PlannedStartDate datetime
- RequiredCompletionDate datetime
- ActualStartDate datetime
- OrderCompletionVariance int
- OrderStartVariance int
- ActualOrderCompletionSlack int
- PlannedOrderCompletionSlack int
- ActualOrderStartLeadTime int
- ActualOrderExecutionDuration int
- PlannedOrderExecutionDuration int
- PlannedOrderStartLeadTime int
- Grade varchar(100)
- SalesOrderItem varchar(100)
- Area varchar(100)
