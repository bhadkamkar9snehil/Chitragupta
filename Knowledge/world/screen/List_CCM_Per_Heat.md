---
type: screen
title: "List_CCM_Per_Heat"
built: "2026-09-24T11:36:36"
---

# List_CCM_Per_Heat

XStudio screen 'List_CCM_Per_Heat' (CCM Per Heat; page CCM Per Heat Data, list view List_CCM_Per_Heat).
Shows rows of XStudio_List_CCM_Per_Heat_Vw.
Filter: only rows where CAST(HeatReportDate AS DATE) BETWEEN CAST(DATEADD(DAY, -45, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE) and (Workorder='<request.WOId>' OR IIF('<request.WOId>'='',1,0)=1)
