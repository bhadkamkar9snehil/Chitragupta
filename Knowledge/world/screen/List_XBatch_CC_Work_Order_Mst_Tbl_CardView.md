---
type: screen
title: "List_XBatch_CC_Work_Order_Mst_Tbl_CardView"
built: "2026-09-24T11:36:36"
---

# List_XBatch_CC_Work_Order_Mst_Tbl_CardView

XStudio screen 'List_XBatch_CC_Work_Order_Mst_Tbl_CardView' (CC Work Order CardView; page Page_List_XBatch_CC_Work_Order_Mst_Tbl_CardView, list view List_XBatch_CC_Work_Order_Mst_Tbl_CardView).
Shows rows of XStudio_List_XBatch_CC_Work_Order_Mst_Tbl_CardView_Vw.
Filter: only rows where STATUS IN ('Running','onhold') And ProductionPlant in (select value from string_split('<Request.Plant>',','))
