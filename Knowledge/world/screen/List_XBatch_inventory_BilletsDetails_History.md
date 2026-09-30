---
type: screen
title: "List_XBatch_inventory_BilletsDetails_History"
built: "2026-09-24T11:36:36"
---

# List_XBatch_inventory_BilletsDetails_History

XStudio screen 'List_XBatch_inventory_BilletsDetails_History' (inventory BilletsDetails History; page List_Page_XBatch_Yard_Details, list view List_XBatch_inventory_BilletsDetails_History).
Shows rows of XStudio_List_XBatch_inventory_BilletsDetails_History_Vw.
Filter: only rows where ItemCode like '%Billet%' and (heatno in (select value from string_split('<request.heatno>',',')))  AND (
        ('<request.MT>' = 'Outward' AND MovementType = 'Outward' AND OutwardLocation IN ('Furnace', 'Mill'))
        OR ('<request.MT>' != 'Outward' AND MovementType != 'Outward')
      )
