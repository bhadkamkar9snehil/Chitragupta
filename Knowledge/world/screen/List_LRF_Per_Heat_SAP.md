---
type: screen
title: "List_LRF_Per_Heat_SAP"
built: "2026-09-24T11:36:36"
---

# List_LRF_Per_Heat_SAP

XStudio screen 'List_LRF_Per_Heat_SAP' (LRF Per Heat SAP; page Page_List_LRF_Per_Heat_SAP, list view List_LRF_Per_Heat_SAP).
Shows rows of XStudio_List_LRF_Per_Heat_SAP_Vw.
Filter: only rows where CAST(Dateyyyymmdd AS DATE) BETWEEN CAST(DATEADD(DAY, -7, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE) and (Workorder='<request.WOId>' OR IIF('<request.WOId>'='',1,0)=1)
