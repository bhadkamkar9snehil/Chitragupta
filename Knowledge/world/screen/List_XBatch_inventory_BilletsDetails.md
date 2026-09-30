---
type: screen
title: "List_XBatch_inventory_BilletsDetails"
built: "2026-09-24T11:36:36"
---

# List_XBatch_inventory_BilletsDetails

XStudio screen 'List_XBatch_inventory_BilletsDetails' (inventory BilletsDetails; page Page_XBatch_YMS_UnstackedBillets, list view List_XBatch_inventory_BilletsDetails).
Shows rows of XStudio_List_XBatch_inventory_BilletsDetails_Vw.
Filter: only rows where ItemCode like '%Billet%' and ToLocation IS NULL and (heatno='<request.heatno>' or <request.heatno> is null)
