---
type: screen
title: "List_LRF_Per_Heat_Mobile_View"
built: "2026-09-24T11:36:36"
---

# List_LRF_Per_Heat_Mobile_View

XStudio screen 'List_LRF_Per_Heat_Mobile_View' (LRF Per Heat Mobile View; page Page_List_LRF_Per_Heat_Mobile_View, list view List_LRF_Per_Heat_Mobile_View).
Shows rows of XStudio_List_LRF_Per_Heat_Mobile_View_Vw.
Filter: only rows where CAST(Dateyyyymmdd AS DATE) BETWEEN CAST(DATEADD(DAY, -7, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE) and (Workorder='<request.WOId>' OR IIF('<request.WOId>'='',1,0)=1)
