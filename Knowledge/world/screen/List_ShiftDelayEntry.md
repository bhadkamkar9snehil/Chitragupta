---
type: screen
title: "List_ShiftDelayEntry"
built: "2026-09-24T11:36:36"
---

# List_ShiftDelayEntry

XStudio screen 'List_ShiftDelayEntry' (ShiftDelayEntry; page List_Page_ShiftDelayEntry, list view List_ShiftDelayEntry).
Shows rows of XStudio_List_ShiftDelayEntry_Vw.
Filter: only rows where AreaName='SMS' and cast(DelayStartTime as date) between cast(getdate() - 7 as date) and cast(getdate() as date)
