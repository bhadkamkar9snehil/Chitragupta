---
type: screen
title: "List_MES_SAP_Consumption_Trn_Tbl_WorkOrder"
built: "2026-09-24T11:36:36"
---

# List_MES_SAP_Consumption_Trn_Tbl_WorkOrder

XStudio screen 'List_MES_SAP_Consumption_Trn_Tbl_WorkOrder' (MES SAP Consumption WorkOrder; page Page_List_MES_SAP_Production_Trn_Tbl_Reversal, list view List_MES_SAP_Consumption_Trn_Tbl_WorkOrder).
Shows rows of XStudio_List_MES_SAP_Consumption_Trn_Tbl_WorkOrder_Vw.
Filter: only rows where HeatNo in (Select HeatID from [XStudio_Xbatch]..[CCM_Per_Heat] Where WorkOrder='<Request.WOid>') or ((HeatNo='<request.HeatNo>' OR IIF('<request.HeatNO>'='',1,0)=1)) AND (SAPPostingStatus='<request.SAPPostingStatus>' OR IIF('<request.SAPPostingStatus>'='',1,0)=1)
