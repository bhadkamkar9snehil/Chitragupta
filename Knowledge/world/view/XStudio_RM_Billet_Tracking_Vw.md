---
type: view
title: "XStudio_RM_Billet_Tracking_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_RM_Billet_Tracking_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`

## Reads

- RM_Operator_HeatSelection
- XBatch_Work_Order_Mst_Tbl
- XMES_Campaign_Plan_Mst
- XMES_Live_Billet_Charging_Bed

## Columns

- ID varchar(36)
- workorderNumber varchar(100)
- WorkorderSize varchar(100)
- BatchNo varchar(100)
- BilletNo varchar(100)
- BilletTracking varchar(50)
- ParentID varchar(36)
- campaignId varchar(36)
- Action varchar(50)
- Parent_Campaign_Material varchar(100)
- ModifiedOn datetime
- BilletType varchar(100)
- BilletLengthMtr decimal
- BilletGrade varchar(100)
- IsDeleted bit
- Delete varchar(100)
