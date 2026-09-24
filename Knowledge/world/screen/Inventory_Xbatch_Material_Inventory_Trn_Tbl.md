---
type: screen
title: "Inventory_Xbatch_Material_Inventory_Trn_Tbl"
built: "2026-09-24T11:36:36"
---

# Inventory_Xbatch_Material_Inventory_Trn_Tbl

XStudio screen (menu 'Inventory_Xbatch_Material_Inventory_Trn_Tbl', page List_Page_Xbatch_Material_Inventory_Trn_Tbl, list view List_Xbatch_Material_Inventory_Trn_Tbl).
Shows rows of XStudio_List_Xbatch_Material_Inventory_Trn_Tbl_Vw.
Filter: only rows where (Plantcode in (select value from string_split('<request.Plant>',',') )OR IIF('<request.Plant>'='',1,0)=1) and (ItemType='<request.ItemType>' OR IIF('<request.ItemType>'='',1,0)=1) and (PostingMaterialType like'%<request.Type>%' OR IIF('<request.Type>'='',1,0)=1)
