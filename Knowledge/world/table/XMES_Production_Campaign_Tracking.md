---
type: table
title: "XMES_Production_Campaign_Tracking"
built: "2026-09-24T11:36:36"
---

# XMES_Production_Campaign_Tracking

Table in XStudio_Xbatch. Rows: 125.

## Written by

- XSTUDIO_WORKFLOW_1902B563-DDCD-4A38-9487-FE6186063998_SP
- XSTUDIO_WORKFLOW_35A3A6C3-97F5-4029-9B30-47985E01CF21_SP
- XSTUDIO_WORKFLOW_7BBFE023-3C57-4473-96E0-B6CF231296F9_SP
- XSTUDIO_WORKFLOW_92A749C7-433A-4097-B5A2-95E6350FB25B_SP
- XSTUDIO_WORKFLOW_9F899B3A-621E-426A-B53F-11EDD062EC6B_SP
- XSTUDIO_WORKFLOW_A33E0C6A-390E-4BFA-812D-0CF28EC79BF6_SP
- XSTUDIO_WORKFLOW_E2571DEB-9445-4B73-9BA2-5ED89412D715_SP
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP
- campaignplan_released_workflow_usp

## Read by

- XSTUDIO_WORKFLOW_1902B563-DDCD-4A38-9487-FE6186063998_SP
- XSTUDIO_WORKFLOW_35A3A6C3-97F5-4029-9B30-47985E01CF21_SP
- XSTUDIO_WORKFLOW_7BBFE023-3C57-4473-96E0-B6CF231296F9_SP
- XSTUDIO_WORKFLOW_92A749C7-433A-4097-B5A2-95E6350FB25B_SP
- XSTUDIO_WORKFLOW_A33E0C6A-390E-4BFA-812D-0CF28EC79BF6_SP
- XSTUDIO_WORKFLOW_E2571DEB-9445-4B73-9BA2-5ED89412D715_SP
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP
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
- EntryDateTime datetime
- ReportDate date
- IsProcessed bit
- Work_Order varchar(100)
- Sales_Order varchar(100)
- Billet_Charged varchar(100)
- Billet_Rolled varchar(100)
- Quantity_Produce_MT varchar(100)
- Bundles varchar(100)
- Total_Pcs varchar(100)
- Remaining_Pcs varchar(100)
- PercentageComplete varchar(100)
- Status varchar(100)
- CampaignId varchar(100)
- ProductionStartDate datetime
- ProductionEndDate datetime
- ReleasedDate datetime
- OnholdDate datetime
- CancelledDate datetime
- CompletedDate datetime
- AbortDate datetime
- RunningDate datetime
