---
type: screen
title: "List_EAF_PER_HEAT_History"
built: "2026-09-24T11:36:36"
---

# List_EAF_PER_HEAT_History

XStudio screen 'List_EAF_PER_HEAT_History' (EAF PER HEAT History; page Page_EAF_Per_Heat_History, list view List_EAF_PER_HEAT_History).
Shows rows of XStudio_List_EAF_PER_HEAT_History_Vw.
Filter: only rows where CAST(Dateyyyymmdd AS DATE) NOT BETWEEN CAST(DATEADD(DAY, -7, GETDATE()) AS DATE)  AND CAST(GETDATE() AS DATE)
