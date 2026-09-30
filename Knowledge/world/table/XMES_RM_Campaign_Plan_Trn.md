---
type: table
title: "XMES_RM_Campaign_Plan_Trn"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Campaign_Plan_Trn

Table in XStudio_Xbatch. Rows: 112.

## Identifiers it holds

- SONumber: same values as key `SONumber`

## Written by

- XMES_MaterialProcess_Cursor_usp
- XSTUDIO_WORKFLOW_C7EA6F22-24BB-490A-A748-6AE14C39B81D_SP (text)
- sp_Xstudio_XMES_RM_CampaignPlan_USP

## Read by

- XMES_MaterialProcess_Cursor_usp
- XMES_RM_Campaign_Plan_WorkOrders_Creation
- XMES_WorkOrders_Creation
- XSTUDIO_WORKFLOW_9F899B3A-621E-426A-B53F-11EDD062EC6B_SP
- XSTUDIO_WORKFLOW_C7EA6F22-24BB-490A-A748-6AE14C39B81D_SP
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP
- campaignplan_released_workflow_usp
- errorfortest
- sp_Xstudio_XMES_RM_CampaignPlan_USP

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(100)
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
- Country varchar(100)
- SONumber varchar(36)
- ItemNo int
- MaterialNo varchar(-1)
- Specification varchar(100)
- MinQtytoRollMT decimal
- MaxQtytoRollMT int
- Length decimal
- PositiveTolerance decimal
- NegativeTolerance int
- TagDetails varchar(-1)
- Remarks varchar(-1)
- MinNoOfBundles int
- MaxNoOfBundles int
- BundlesweightTon decimal
- NumberOfPiecesInBundles int
- Section int
- CampaignId varchar(100)
- WorkorderNo varchar(36)
- status varchar(50)
- AllFIleUpload varchar(8000)
- Size varchar(100)
- Validation bit
- ContractNo int
- Grade varchar(100)
- NoofCoilstoBeRoll int
- BilletType varchar(100)
- Customer varchar(-1)
