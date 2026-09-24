---
type: screen
title: "LRF Per Heat Data"
built: "2026-09-24T11:36:36"
---

# LRF Per Heat Data

XStudio screen 'LRF Per Heat Data' (LRF Per Heat; page List_Page_LRF_Per_Heat_Data, list view List_LRF_Per_Heat).
Shows rows of XStudio_List_LRF_Per_Heat_Vw.
Filter: only rows where CAST(Dateyyyymmdd AS DATE) BETWEEN CAST(DATEADD(DAY, -7, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE) and (Workorder='<request.WOId>' OR IIF('<request.WOId>'='',1,0)=1)
