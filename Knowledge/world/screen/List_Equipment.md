---
type: screen
title: "List_Equipment"
built: "2026-09-24T11:36:36"
---

# List_Equipment

XStudio screen 'List_Equipment' (Equipment; page List_Page_Equipment, list view List_Equipment).
Shows rows of XStudio_List_Equipment_Vw.
Filter: only rows where (Area='<request.Area>' OR IIF('<request.Area>'='',1,0)=1)
