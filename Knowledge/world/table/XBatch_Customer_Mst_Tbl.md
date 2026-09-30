---
type: table
title: "XBatch_Customer_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XBatch_Customer_Mst_Tbl

Table in XStudio_Xbatch. Rows: 52.

## Written by

- XBatch_I_Customer_USP
- XSTUDIO_WORKFLOW_FF0AE3BF-1A32-4635-B431-3BA6931332AA_SP

## Read by

- XMES_I_SAP_Billet_Production_Trn
- XMES_RM_Campaign_Plan_WorkOrders_Creation
- XMES_WorkOrders_Creation
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
- Address varchar(1000)
- City varchar(100)
- State varchar(100)
- County varchar(100)
- ZipCode int
- ContactNumber1 varchar(100)
- ContactNumber2 varchar(100)
- EmailAddress1 varchar(200)
- EmailAddress2 varchar(200)
- Description varchar(1000)
- CustomerCode varchar(100)
