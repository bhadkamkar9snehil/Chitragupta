---
type: table
title: "NM3_To_MMBTU_Factor"
built: "2026-09-24T11:36:36"
---

# NM3_To_MMBTU_Factor

Table in XStudio_Xbatch. Rows: 1.

## Read by

- XBatch_RM_BilletWiseNGConsumption
- XMES_RM_Production_Summary_Usp
- Xstudio_RM_NGConsumption_USP

## Columns

- ID varchar(36)
- Month date
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
- Nm3toMMBTUFactor decimal
- RebarTieRodFactor decimal
- WRMTieRodFactor decimal
- RebarCoilTieRodFactor decimal
- ScalelossFactor decimal
- EndCutFactor decimal
