---
type: table
title: "XMES_ActiveLife_Element_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# XMES_ActiveLife_Element_Mst_Tbl

Table in XStudio_Xbatch. Rows: 29.

## Identifiers it holds

- LastUsedBatch: same values as key `HeatNo`

## Written by

- Per_Heat_LadleNo_Conformation_usp
- SMS_Ladle_Life_Tracking
- XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP (text)
- XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP
- XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP
- XSTUDIO_WORKFLOW_6F954B26-CB87-40FC-8B73-26EE001C55DC_SP
- XSTUDIO_WORKFLOW_A6124179-0C6C-4218-A43F-FBDE140C034A_SP

## Read by

- Per_Heat_LadleNo_Conformation_usp
- SMS_Ladle_Life_Tracking
- XSTUDIO_WORKFLOW_17E91BC0-FC67-4CB1-9699-1625D71488F2_SP
- XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP
- XSTUDIO_WORKFLOW_2F446F30-57E6-4AC7-A199-42928FC388E2_SP
- XSTUDIO_WORKFLOW_6F954B26-CB87-40FC-8B73-26EE001C55DC_SP
- XSTUDIO_WORKFLOW_A6124179-0C6C-4218-A43F-FBDE140C034A_SP

## Columns

- ID varchar(36)
- ElementNameID varchar(-1)
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
- Status varchar(50)
- Activeinactiveflag bit
- LastUsedBatch varchar(100)
