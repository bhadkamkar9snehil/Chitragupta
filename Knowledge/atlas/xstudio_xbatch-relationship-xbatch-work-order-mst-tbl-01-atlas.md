---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-work-order-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Work_Order_Mst_Tbl.CampaignId -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignId-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.Equipment -> Equipment.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Equipment-Equipment
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.ItemID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ItemID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.ManufacturingOrderType -> Order_Type_MST.OrderType
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ManufacturingOrderType-Order_Type_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.ProductionPlant -> Plant_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProductionPlant-Plant_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.SalesOrder -> XBatch_Sales_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SalesOrder-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.SalesOrderItem -> XBatch_Sales_Order_Mst_Tbl.ItemID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SalesOrderItem-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.Status -> XBatch_Status_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Status-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.StorageLocation -> Storage_Location_MST.StorageLocation
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StorageLocation-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Work_Order_Mst_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
