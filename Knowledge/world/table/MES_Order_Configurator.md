---
type: table
title: "MES_Order_Configurator"
built: "2026-09-24T11:36:36"
---

# MES_Order_Configurator

Table in XStudio_Xbatch. Rows: 3.

## Read by

- XMES_SAP_Create_Process_Order_Usp
- XSTUDIO_WORKFLOW_9B20AE0B-2E34-4BF8-9875-BB52B5C007E0_SP
- XSTUDIO_WORKFLOW_C18D4DFF-8ADA-4080-9F2F-91DE212A1257_SP

## Columns

- ID varchar(36)
- Equipment varchar(100)
- Itemid varchar(36)
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
- Quantity decimal
- Unitid varchar(36)
- OrderType varchar(100)
- SrNo int
