---
type: screen
title: "List_EAF_PER_HEAT_Mobile_View"
built: "2026-09-24T11:36:36"
---

# List_EAF_PER_HEAT_Mobile_View

XStudio screen 'List_EAF_PER_HEAT_Mobile_View' (EAF PER HEAT Mobile View; page Page_EAF_Per_Heat_Mobile_View, list view List_EAF_PER_HEAT_Mobile_View).
Shows rows of XStudio_List_EAF_PER_HEAT_Mobile_View_Vw.
Filter: only rows where CAST(Dateyyyymmdd AS DATE) BETWEEN CAST(DATEADD(DAY, -7, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE) and (Workorder='<request.WOId>' OR IIF('<request.WOId>'='',1,0)=1)
