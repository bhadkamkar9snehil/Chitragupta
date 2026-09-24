---
type: screen
title: "List_MES_SAP_Production_Trn_Tbl_Workorder"
built: "2026-09-24T11:36:36"
---

# List_MES_SAP_Production_Trn_Tbl_Workorder

XStudio screen 'List_MES_SAP_Production_Trn_Tbl_Workorder' (MES SAP Production Workorder; page List_Page_CCM_Per_Heat_SAP, list view List_MES_SAP_Production_Trn_Tbl_Workorder).
Shows rows of XStudio_List_MES_SAP_Production_Trn_Tbl_Workorder_Vw.
Filter: only rows where HeatNo in (Select HeatID from [XStudio_Xbatch]..[CCM_Per_Heat] Where WorkOrder='<Request.WOid>')
