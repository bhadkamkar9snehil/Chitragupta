---
type: screen
title: "List_XBatch_MES_Heat_Tracking_History"
built: "2026-09-24T11:36:36"
---

# List_XBatch_MES_Heat_Tracking_History

XStudio screen 'List_XBatch_MES_Heat_Tracking_History' (MES Heat Tracking History; page List_Page_XBatch_MES_Heat_Tracking, list view List_XBatch_MES_Heat_Tracking_History).
Shows rows of XStudio_List_XBatch_MES_Heat_Tracking_History_Vw.
Filter: only rows where CAST(Dateyyyymmdd AS DATE) NOT BETWEEN CAST(DATEADD(DAY, -7, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE)
