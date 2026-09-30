---
type: screen
title: "XMes_Campaign_Plan_Tracking_workorder_Active_compaign"
built: "2026-09-24T11:36:36"
---

# XMes_Campaign_Plan_Tracking_workorder_Active_compaign

XStudio screen 'XMes_Campaign_Plan_Tracking_workorder_Active_compaign' (XMes Campaign Plan Tracking workorder Active compaign; page None, list view XMes_Campaign_Plan_Tracking_workorder_Active_compaign).
Shows rows of XStudio_XMes_Campaign_Plan_Tracking_workorder_Active_compaign_Vw.
Filter: only rows where CampaignId in (select id from xstudio_xbatch.dbo.XMES_Campaign_Plan_Mst where isdeleted=0 and status = 'Running')
