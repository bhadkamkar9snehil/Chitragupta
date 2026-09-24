---
type: screen
title: "List_RM_ShiftDelayEntry"
built: "2026-09-24T11:36:36"
---

# List_RM_ShiftDelayEntry

XStudio screen 'List_RM_ShiftDelayEntry' (RM ShiftDelayEntry; page List_Page_RM_ShiftDelayEntry, list view List_RM_ShiftDelayEntry).
Shows rows of XStudio_List_RM_ShiftDelayEntry_Vw.
Filter: only rows where AreaName='RM' and DateyyyyMMdd=cast(getdate() as date) and Shift=[Xstudio_Xbatch].[dbo].[FN_Get_ShiftName] (Getdate())
