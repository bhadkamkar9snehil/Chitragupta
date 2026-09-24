---
type: screen
title: "List_MES_SAP_Production_Trn_Tbl_Row_Template"
built: "2026-09-24T11:36:36"
---

# List_MES_SAP_Production_Trn_Tbl_Row_Template

XStudio screen 'List_MES_SAP_Production_Trn_Tbl_Row_Template' (MES SAP Production Row Template; page Page_List_MES_SAP_Production_Trn_Tbl_Row_Template, list view List_MES_SAP_Production_Trn_Tbl_Row_Template).
Shows rows of XStudio_List_MES_SAP_Production_Trn_Tbl_Row_Template_Vw.
Filter: only rows where (HeatNo='<request.Heat>' OR IIF('<request.Heat>'='',1,0)=1) and (WorkOrderNumber =(Select WorkOrderNumber from [XStudio_Xbatch]..[XBatch_Work_Order_Mst_Tbl] Where ID='<request.WOid>') OR IIF('<request.WOid>'='',1,0)=1)
AND id='<Request.id>'
