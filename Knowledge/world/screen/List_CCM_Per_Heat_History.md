---
type: screen
title: "List_CCM_Per_Heat_History"
built: "2026-09-24T11:36:36"
---

# List_CCM_Per_Heat_History

XStudio screen 'List_CCM_Per_Heat_History' (CCM Per Heat History; page None, list view List_CCM_Per_Heat_History).
Shows rows of XStudio_List_CCM_Per_Heat_History_Vw.
Filter: only rows where CAST(HeatReportDate AS DATE) NOT BETWEEN CAST(DATEADD(DAY, -7, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE) and (Workorder='<request.WOId>' OR IIF('<request.WOId>'='',1,0)=1)
