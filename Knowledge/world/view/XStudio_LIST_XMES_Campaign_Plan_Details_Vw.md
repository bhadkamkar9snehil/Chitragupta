---
type: view
title: "XStudio_LIST_XMES_Campaign_Plan_Details_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_LIST_XMES_Campaign_Plan_Details_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- XBatch_Customer_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Sales_Order_Mst_Tbl
- XMES_RM_Campaign_Plan_Trn

## Columns

- Campaign varchar(100)
- SalesOrder varchar(36)
- Country varchar(100)
- ItemNo int
- MaterialNo varchar(-1)
- Specification varchar(100)
- MinQtytoRollMT decimal
- MaxQtytoRollMT int
- Length decimal
- PositiveTolerance decimal
- NegativeTolerance int
- TagDetails varchar(-1)
- MinNoOfBundles int
- MaxNoOfBundles int
- BundlesWeightton decimal
- NoOfPiecesInBundles int
- Section int
- Remarks varchar(-1)
- ID varchar(36)
- Delete varchar(100)
- Details varchar(-1)
- Edit varchar(243)
- SO_Number_Name varchar(100)
- Material_No_Name varchar(100)
- Customer_Name varchar(100)
- Name varchar(100)
- IsDeleted bit
- ParentID varchar(100)
- ModifiedOn datetime
