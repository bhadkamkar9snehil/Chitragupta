---
type: screen
title: "List_Xbatch_Material_Inventory_Trn_Tbl_RowTemplate"
built: "2026-09-24T11:36:36"
---

# List_Xbatch_Material_Inventory_Trn_Tbl_RowTemplate

XStudio screen 'List_Xbatch_Material_Inventory_Trn_Tbl_RowTemplate' (Xbatch Material Inventory RowTemplate; page Page_List_Xbatch_Material_Inventory_Trn_Tbl_RowTemplate, list view List_Xbatch_Material_Inventory_Trn_Tbl_RowTemplate).
Shows rows of XStudio_List_Xbatch_Material_Inventory_Trn_Tbl_RowTemplate_Vw.
Filter: only rows where (Plantcode in (select value from string_split('<request.Plant>',',') )OR IIF('<request.Plant>'='',1,0)=1) and (ItemType='<request.ItemType>' OR IIF('<request.ItemType>'='',1,0)=1) and (PostingMaterialType like'%<request.Type>%' OR IIF('<request.Type>'='',1,0)=1) and ItemName like 'BL%' and  0 < Quantity
