---
type: screen
title: "List_XBatch_inventory_BilletsDetails_CP"
built: "2026-09-24T11:36:36"
---

# List_XBatch_inventory_BilletsDetails_CP

XStudio screen 'List_XBatch_inventory_BilletsDetails_CP' (inventory BilletsDetails CP; page None, list view List_XBatch_inventory_BilletsDetails_CP).
Shows rows of XStudio_List_XBatch_inventory_BilletsDetails_CP_Vw.
Filter: only rows where ((ItemCode like '%Billet%' and locationID is not NULL) and Materialgrade = (select Name from 	Xstudio_Xbatch..Xstudio_Xbatch_ChargingPlan_Mst_Tbl where id='<request.saveAndContinueRecordId>' ))
