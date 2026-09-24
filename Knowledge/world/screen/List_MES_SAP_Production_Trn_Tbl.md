---
type: screen
title: "List_MES_SAP_Production_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# List_MES_SAP_Production_Trn_Tbl

XStudio screen 'List_MES_SAP_Production_Trn_Tbl' (MES SAP Production; page List_Page_MES_SAP_Trn_Tbl, list view List_MES_SAP_Production_Trn_Tbl).
Shows rows of XStudio_List_MES_SAP_Production_Trn_Tbl_Vw.
Filter: only rows where (HeatNo='<request.Heat>' OR IIF('<request.Heat>'='',1,0)=1) and (WorkOrderNumber =(Select WorkOrderNumber from [XStudio_Xbatch]..[XBatch_Work_Order_Mst_Tbl] Where ID='<request.WOid>') OR IIF('<request.WOid>'='',1,0)=1)
