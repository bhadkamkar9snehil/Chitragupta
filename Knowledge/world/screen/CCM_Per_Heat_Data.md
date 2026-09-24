---
type: screen
title: "CCM Per Heat Data"
built: "2026-09-24T11:36:36"
---

# CCM Per Heat Data

XStudio screen (menu 'CCM Per Heat Data', page List_Page_CCM_Per_Heat, list view List_CCM_Per_Heat).
Shows rows of XStudio_List_CCM_Per_Heat_Vw.
Filter: only rows where CAST(HeatReportDate AS DATE) BETWEEN CAST(DATEADD(DAY, -45, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE) and (Workorder='<request.WOId>' OR IIF('<request.WOId>'='',1,0)=1)
