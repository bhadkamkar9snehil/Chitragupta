---
type: view
title: "XStudio_Equipment_Mst_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_Equipment_Mst_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- CCM_Attribute_Tag_Template_Mst_Tbl
- CCM_Mst_Tbl
- CCM_SMS_Attribute_Tag_Template_Mst_Tbl
- CCM_SMS_Mst_Tbl
- Communication_System_Attribute_Tag_Template_Mst_Tbl
- Communication_System_Mst_Tbl
- EAF_SMS_Attribute_Tag_Template_Mst_Tbl
- EAF_SMS_Mst_Tbl
- LRF_SMS_Attribute_Tag_Template_Mst_Tbl
- LRF_SMS_Mst_Tbl
- RM_Furnace_Combustion_Attribute_Tag_Template_Mst_Tbl
- RM_Furnace_Combustion_Mst_Tbl
- RM_Mill_Attribute_Tag_Template_Mst_Tbl
- RM_Mill_Mst_Tbl
- RM_Rebar_Attribute_Tag_Template_Mst_Tbl
- RM_Rebar_Mst_Tbl
- RM_Reheating_Furnace_Attribute_Tag_Template_Mst_Tbl
- RM_Reheating_Furnace_Mst_Tbl
- RM_WRM_Attribute_Tag_Template_Mst_Tbl
- RM_WRM_Mst_Tbl

## Read by

- XBatch_Get_Capability_By_Type_And_Template_Usp
- XBatch_I_Material_Inventory_Transfer_USP
- XBatch_I_Material_Inventory_USP

## Columns

- ID varchar(36)
- EquipmentName varchar(100)
- EquipmetTypeID varchar(36)
- EquipmentTypeName varchar(21)
- TemplateID varchar(36)
- TemplateName varchar(100)
- AreaID varchar(36)
- MaterialID int
- MaterialName int
