---
type: table
title: "XMES_Campaign_Plan_Mst"
built: "2026-09-24T11:36:36"
---

# XMES_Campaign_Plan_Mst

Table in XStudio_Xbatch. Rows: 5.

## Written by

- MES_M_Sect2_to_Furnace (text)
- MES_M_Sect2_to_Furnace_Billet_Tracking (text)
- MES_M_Strand
- MES_M_Strand_TMT (text)
- MES_M_Strand_WRM (text)
- XMES_CampaignId_generation_usp (text)
- XSTUDIO_WORKFLOW_1902B563-DDCD-4A38-9487-FE6186063998_SP
- XSTUDIO_WORKFLOW_35A3A6C3-97F5-4029-9B30-47985E01CF21_SP (text)
- XSTUDIO_WORKFLOW_7BBFE023-3C57-4473-96E0-B6CF231296F9_SP (text)
- XSTUDIO_WORKFLOW_92A749C7-433A-4097-B5A2-95E6350FB25B_SP (text)
- XSTUDIO_WORKFLOW_9F899B3A-621E-426A-B53F-11EDD062EC6B_SP
- XSTUDIO_WORKFLOW_A33E0C6A-390E-4BFA-812D-0CF28EC79BF6_SP (text)
- XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP
- XSTUDIO_WORKFLOW_DE81675D-78C0-4060-BC94-D8FD0973FC62_SP (text)
- XSTUDIO_WORKFLOW_E2571DEB-9445-4B73-9BA2-5ED89412D715_SP (text)
- XSTUDIO_WORKFLOW_F4CB27BF-724B-4771-B93E-C17AAA1CFB9E_SP (text)
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP (text)
- Xstudio_XMES_Campaign_Plan_Mst_USP
- errorfortest
- sp_Xstudio_XMES_RM_CampaignPlan_USP

## Read by

- Billet_Furnace_Movement
- Billet_Furnace_Movement_Billet_Tracking
- Billet_Furnace_Movement_GradeGap
- Billet_Furnace_Movement_HeatGap
- MES_M_Sect2_to_Furnace
- MES_M_Sect2_to_Furnace_Billet_Tracking
- MES_M_Strand
- XMES_DisplayCampaignPlanDetails_usp
- XMES_MaterialProcess_Cursor_usp
- XMES_Nested_heat_selection_usp
- XMES_RM_Campaign_Plan_WorkOrders_Creation
- XMES_RM_Production_Summary_Usp
- XMES_SAP_I_EndProduct_Production_Usp
- XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp
- XMES_heat_selection_usp
- XSTUDIO_WORKFLOW_1902B563-DDCD-4A38-9487-FE6186063998_SP
- XSTUDIO_WORKFLOW_35A3A6C3-97F5-4029-9B30-47985E01CF21_SP
- XSTUDIO_WORKFLOW_7BBFE023-3C57-4473-96E0-B6CF231296F9_SP
- XSTUDIO_WORKFLOW_92A749C7-433A-4097-B5A2-95E6350FB25B_SP
- XSTUDIO_WORKFLOW_9F899B3A-621E-426A-B53F-11EDD062EC6B_SP
- XSTUDIO_WORKFLOW_A33E0C6A-390E-4BFA-812D-0CF28EC79BF6_SP
- XSTUDIO_WORKFLOW_C7EA6F22-24BB-490A-A748-6AE14C39B81D_SP
- XSTUDIO_WORKFLOW_CBDD76F9-AF65-4113-B5FE-987066DC8DDD_SP
- XSTUDIO_WORKFLOW_DE81675D-78C0-4060-BC94-D8FD0973FC62_SP
- XSTUDIO_WORKFLOW_E2571DEB-9445-4B73-9BA2-5ED89412D715_SP
- XSTUDIO_WORKFLOW_F4CB27BF-724B-4771-B93E-C17AAA1CFB9E_SP
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP
- Xmes_Billet_Finished_Good_Production_usp
- Xstudio_XMES_Campaign_Plan_Mst_USP
- campaignplan_released_workflow_usp
- errorfortest
- sp_Xstudio_XMES_RM_CampaignPlan_USP

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
- Working varchar(100)
- Material varchar(100)
- Size decimal
- Grade varchar(100)
- TotalQtyWt decimal
- TotalPieces int
- Status varchar(50)
- CampaignId varchar(100)
- Length varchar(100)
- StartDate date
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- MinQtytoRollMT decimal
- MaxQtytoRollMT decimal
- MinNoOfBundles decimal
- MaxNoOfBundles decimal
- Action varchar(50)
- AllFilesUpload varchar(8000)
- EndDate date
- UploadStatus varchar(50)
- Productname varchar(36)
- ProgressTonnage decimal
- ProgressPercentage decimal
- RemaningTonnage decimal
- CampaignstartDate date
- CampaignEndDate date
- WRMExcelUpload varchar(8000)
- WRMStatus varchar(50)
- WRMUploadStatus varchar(50)
- BilletsRolled int
- BilletsCobble int
- BilletsHotout int
- BilletDischarged int
- BilletsRemaining int
- TotalBillets int
- BilletDischargedWeight decimal
