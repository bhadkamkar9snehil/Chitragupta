---
type: Reference
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: M

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## MES_Order_Configurator.CreatedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: CreatedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Order_Configurator.Itemid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Itemid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Order_Configurator.ModifiedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ModifiedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Order_Configurator.Unitid -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Unitid-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Attributeids -> XStudio_Attribute_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Attributeids-XStudio_Attribute_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Entityids -> XStudio_Entities_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Entityids-XStudio_Entities_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Materialid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Materialid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.Unitid -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Unitid-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Trn_Tbl.ParentID -> MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-MES_Raw_Material_Consumptions_Mapping_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Trn_Tbl.SalesOrder -> XBatch_Sales_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SalesOrder-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Trn_Tbl.Unit -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Unit-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_SAP_By_Product_Trn_Tbl.Saptransactionid -> XMES_SAP_API_GoodsMovement_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Saptransactionid-XMES_SAP_API_GoodsMovement_Error
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_SAP_Consumption_Trn_Tbl.Saptransactionid -> XMES_SAP_API_GoodsMovement_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Saptransactionid-XMES_SAP_API_GoodsMovement_Error
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_SAP_Inventory_Stock_Data_Tbl.Material -> XBatch_Material_Mst_Tbl.Number
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Material-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_SAP_Production_Trn_Tbl.HeatNo -> CCM_Per_Heat.HeatID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-CCM_Per_Heat
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_SAP_Production_Trn_Tbl.Sampleid -> Heat_Chemistry_Quality_Data.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Sampleid-Heat_Chemistry_Quality_Data
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_SAP_Production_Trn_Tbl.Saptransactionid -> XMES_SAP_API_GoodsMovement_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Saptransactionid-XMES_SAP_API_GoodsMovement_Error
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_SAP_UsageDecision_Trn_Tbl.SAPTransactionID -> XMES_SAP_API_UsageDecision_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: SAPTransactionID-XMES_SAP_API_UsageDecision_Error
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_SAP_WorkOrder_Movements_Trn_Tbl.ParentID -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_TMT.ID -> MES_TMT_Small_Cut.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ID-MES_TMT_Small_Cut
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_TMT.workorder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: workorder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_TMT_Small_Cut.ID -> MES_TMT.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ID-MES_TMT
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_WRM.Workorder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Workorder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

