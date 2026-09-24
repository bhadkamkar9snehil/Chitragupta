---
type: screen
title: "List_SubEquipment"
built: "2026-09-24T11:36:36"
---

# List_SubEquipment

XStudio screen 'List_SubEquipment' (SubEquipment; page List_Page_SubEquipment, list view List_SubEquipment).
Shows rows of XStudio_List_SubEquipment_Vw.
Filter: only rows where (EquipmentId='<request.id>' OR IIF('<request.id>'='',1,0)=1)
