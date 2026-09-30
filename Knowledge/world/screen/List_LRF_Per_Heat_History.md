---
type: screen
title: "List_LRF_Per_Heat_History"
built: "2026-09-24T11:36:36"
---

# List_LRF_Per_Heat_History

XStudio screen 'List_LRF_Per_Heat_History' (LRF Per Heat History; page Page_LRF_Per_Heat_History, list view List_LRF_Per_Heat_History).
Shows rows of XStudio_List_LRF_Per_Heat_History_Vw.
Filter: only rows where CAST(Dateyyyymmdd AS DATE) NOT BETWEEN CAST(DATEADD(DAY, -7, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE)
