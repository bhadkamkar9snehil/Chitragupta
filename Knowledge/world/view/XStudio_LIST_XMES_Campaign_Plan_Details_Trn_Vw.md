---
type: view
title: "XStudio_LIST_XMES_Campaign_Plan_Details_Trn_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_LIST_XMES_Campaign_Plan_Details_Trn_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- SONumber: same values as key `SONumber`

## Reads

- XBatch_Material_Mst_Tbl
- XBatch_Sales_Order_Mst_Tbl
- XMES_RM_Campaign_Plan_Trn

## Columns

- Country varchar(100)
- SONumber varchar(36)
- ItemNo int
- MaterialNo varchar(-1)
- Customer varchar(36)
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
- BundlesWeightton decimal
- NoOfPiecesInBundles int
- ID varchar(36)
- Section int
- Delete varchar(100)
- Details varchar(-1)
- Edit varchar(243)
- SO_Number_Name varchar(100)
- Material_No_Name varchar(100)
- Customer_Name varchar(100)
- Name varchar(100)
- CampaignId varchar(100)
- ParentID varchar(36)
- IsDeleted bit
