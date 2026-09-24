---
type: screen
title: "Billet Consumption"
built: "2026-09-24T11:36:36"
---

# Billet Consumption

XStudio screen (menu 'Billet Consumption', page Page_List_MES_SAP_Consumption_Trn_Tbl_billet, list view List_MES_SAP_Consumption_Trn_Tbl_Billet).
Shows rows of XStudio_List_MES_SAP_Consumption_Trn_Tbl_Billet_Vw.
Filter: only rows where (HeatNo='<request.Heat>' OR IIF('<request.Heat>'='',1,0)=1) and postingmaterialtype='Billet'
