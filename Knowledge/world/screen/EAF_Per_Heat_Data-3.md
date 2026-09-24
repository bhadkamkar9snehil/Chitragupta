---
type: screen
title: "EAF Per Heat Data"
built: "2026-09-24T11:36:36"
---

# EAF Per Heat Data

XStudio screen (menu 'EAF Per Heat Data', page List_Page_EAF_Per_Heat_Data, list view List_EAF_PER_HEAT).
Shows rows of XStudio_List_EAF_PER_HEAT_Vw.
Filter: only rows where CAST(Dateyyyymmdd AS DATE) BETWEEN CAST(DATEADD(DAY, -120, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE) and (Workorder='<request.WOId>' OR IIF('<request.WOId>'='',1,0)=1)
