---
type: screen
title: "XMES_Billets_List_SAP_Posting"
built: "2026-09-24T11:36:36"
---

# XMES_Billets_List_SAP_Posting

XStudio screen 'XMES_Billets_List_SAP_Posting' (Billets List SAP Posting; page Xmes_BilletCon_SAP_Posting, list view XMES_Billets_List_SAP_Posting).
Shows rows of XStudio_XMES_Billets_List_SAP_Posting_Vw.
Filter: only rows where parentid in (select id from <dbtype.data>.[dbo].[XMES_Live_Charging_SECT1]
where parentid in (select id from <dbtype.data>.[dbo].[xmes_live_billet_charging_bed]
where parentid = (select id from <dbtype.data>.[dbo].[rm_operator_heatselection]
where id='<request.Heat>' and isdeleted=0)and isdeleted=0) and isdeleted=0)
