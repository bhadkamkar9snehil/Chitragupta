---
type: Reference
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: X

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Batch_BOM_Mst_Tbl.ItemID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ItemID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.OperationID -> XBatch_Batch_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OperationID-XBatch_Batch_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.ParentID -> XBatch_Batch_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.PhaseGroupID -> XBatch_Batch_Phase_Group_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PhaseGroupID-XBatch_Batch_Phase_Group_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.PhaseID -> XBatch_Batch_Phase_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PhaseID-XBatch_Batch_Phase_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.UnitProcedureID -> XBatch_Batch_Unit_Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitProcedureID-XBatch_Batch_Unit_Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_BOM_Mst_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.ParentID -> XBatch_Recipe_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.ProcessCellID -> XBatch_Process_Cell_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcessCellID-XBatch_Process_Cell_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.QuantityUnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CapacityUnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.StatusID -> XBatch_Status_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatusID-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Mst_Tbl.WorkOrderID -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrderID-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Operation_Mst_Tbl.EquipmentTypeID -> Equipment_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentTypeID-Equipment_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Operation_Mst_Tbl.OutputMaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OutputMaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Operation_Mst_Tbl.ParentID -> XBatch_Batch_Unit_Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_Unit_Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Operation_Mst_Tbl.StatusID -> XBatch_Status_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatusID-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Group_Mst_Tbl.ParentID -> XBatch_Batch_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Group_Mst_Tbl.StatusID -> XBatch_Status_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatusID-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Mst_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Mst_Tbl.ParentID -> XBatch_Batch_Phase_Group_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_Phase_Group_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Mst_Tbl.StatusID -> XBatch_Status_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatusID-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Parameter_Mst_Tbl.ParentID -> XBatch_Batch_Phase_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_Phase_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Trn_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Trn_Tbl.ParentID -> XBatch_Batch_Phase_Group_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_Phase_Group_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Phase_Trn_Tbl.StatusID -> XBatch_Status_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatusID-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Unit_Procedure_Mst_Tbl.ParentID -> XBatch_Batch_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Unit_Procedure_Mst_Tbl.StatusID -> XBatch_Status_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatusID-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Batch_Unit_Procedure_Mst_Tbl.UnitID -> XBatch_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Billets_Transfer_History_Tbl.ActionBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: LocationAssignBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Billets_Transfer_History_Tbl.InventoryID -> XBatch_Material_Inventory_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: InventoryID-XBatch_Material_Inventory_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Billets_Transfer_History_Tbl.OutwardBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: OutwardBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Connection_Mst_Tbl.ParentID -> XBatch_Process_Cell_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Process_Cell_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Formula_Dtl_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Material-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Formula_Dtl_Tbl.ParentID -> XBatch_Formula_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Formula_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Formula_Dtl_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Unit-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Formula_Mst_Tbl.ParentID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Formula_Mst_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.GradeID -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.InwardBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: InwardBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.LocationID -> XBatch_Storage_Rack_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> Many
Relation: LocationID-XBatch_Storage_Rack_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.MaterialGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.OperationID -> XBatch_Batch_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OperationID-XBatch_Batch_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.Outwardby -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: Outwardby-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.OutwardLocation -> XBatch_OutwardLocation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OutwardLocation-XBatch_OutwardLocation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.ParentID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.PlantName -> Plant_Name_MST.Plant
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PlantName-Plant_Name_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.StorageLocation -> Storage_Location_MST.StorageLocation
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StorageLocation-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Inventory_Mst_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.MaterialGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.ParentID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.PlantName -> Plant_Name_MST.Plant
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PlantName-Plant_Name_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.StorageLocation -> Storage_Location_MST.StorageLocation
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StorageLocation-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xbatch_Material_Inventory_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Cons_Per_WorkOrder_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Cons_Per_WorkOrder_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Cons_Per_WorkOrder_Tbl.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Cons_Trn_Tbl.GradeID -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Cons_Trn_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Cons_Trn_Tbl.ParentID -> XBatch_Batch_BOM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_BOM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Cons_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Mst_Tbl.GradeID -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Mst_Tbl.ParentID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Mst_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Prod_Per_WorkOrder_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Prod_Per_WorkOrder_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Prod_Per_WorkOrder_Tbl.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Prod_Trn_Tbl.GradeID -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Prod_Trn_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Prod_Trn_Tbl.ParentID -> XBatch_Batch_BOM_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Batch_BOM_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Item_Prod_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.PageID -> XStudio_Page_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: PageID-XStudio_Page_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.PlantID -> Plant_Name_MST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PlantID-Plant_Name_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.RawMaterialName -> MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: RawMaterialName-MES_Raw_Material_Consumptions_Mapping_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.StoragelocationID -> Storage_Location_MST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StoragelocationID-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.TypeID -> XBatch_Material_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TypeID-XBatch_Material_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Mst_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Sample_Mst.ParentID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Sub_Item_Mst_Tbl.ParentID -> XBatch_Material_Item_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Material_Item_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Material_Sub_Item_Mst_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.CCMWorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CCMWorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.EAFWorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EAFWorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.LFEngineer -> SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.LRFOperator
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LFEngineer-SMS_Shift_Operator_Incharge_Selection_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.LRFWorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LRFWorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.Melter -> SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.EAFOperator
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Melter-SMS_Shift_Operator_Incharge_Selection_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.Sequence -> CCM_Per_Heat.LadleSequence
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Sequence-CCM_Per_Heat
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.ShiftManager -> SMS_Shift_Operator_Incharge_Selection_Trn_Tbl.ShiftInCharge
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ShiftManager-SMS_Shift_Operator_Incharge_Selection_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.StartTime -> CCM_Per_Heat.StartTime
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StartTime-CCM_Per_Heat
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_MES_Heat_Tracking.SteelGrade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SteelGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Process_Cell_Mst_Tbl.CurrentBatchID -> XBatch_Batch_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CurrentBatchID-XBatch_Batch_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Process_Cell_Mst_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Connection_Mst_Tbl.ParentID -> XBatch_Recipe_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Mst_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Mst_Tbl.ProcessCellID -> XBatch_Process_Cell_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcessCellID-XBatch_Process_Cell_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Operation_Mst_Tbl.EquipmentTypeID -> Equipment_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentTypeID-Equipment_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Operation_Mst_Tbl.OutputMaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: OutputMaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Operation_Mst_Tbl.ParentID -> XBatch_Recipe_Unit_Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Unit_Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Phase_Group_Mst_Tbl.ParentID -> XBatch_Recipe_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Phase_Mst_Tbl.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Phase_Mst_Tbl.ParentID -> XBatch_Recipe_Phase_Group_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Phase_Group_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Phase_Parameter_Mst_Tbl.ParentID -> XBatch_Recipe_Phase_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Phase_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Recipe_Unit_Procedure_Mst_Tbl.ParentID -> XBatch_Recipe_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Recipe_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.ApprovedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ApprovedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.ItemID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ItemID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.ParentID -> XBatch_Customer_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Customer_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.Status -> XBatch_Status_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Status-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Storage_Area_Mst_Tbl.CapacityUnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CapacityUnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Storage_Area_Mst_Tbl.ParentID -> XBatch_Store_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Store_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Storage_Rack_Mst_Tbl.ParentID -> XBatch_Storage_Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Storage_Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Store_Mst_Tbl.CapacityUnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CapacityUnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Store_Mst_Tbl.SAPStorageLocation -> Storage_Location_MST.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SAPStorageLocation-Storage_Location_MST
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Equipment_Mst_Tbl.CurrentBatchID -> XBatch_Batch_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CurrentBatchID-XBatch_Batch_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Equipment_Mst_Tbl.CurrentOperationID -> XBatch_Batch_Operation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CurrentOperationID-XBatch_Batch_Operation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Equipment_Mst_Tbl.CurrentUnitProcedureID -> XBatch_Batch_Unit_Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CurrentUnitProcedureID-XBatch_Batch_Unit_Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Equipment_Mst_Tbl.EquipmentTypeID -> Equipment_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EquipmentTypeID-Equipment_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Equipment_Mst_Tbl.ParentID -> XBatch_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Mst_Tbl.CurrentBatchID -> XBatch_Batch_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CurrentBatchID-XBatch_Batch_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Mst_Tbl.CurrentUnitProcedureID -> XBatch_Batch_Unit_Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CurrentUnitProcedureID-XBatch_Batch_Unit_Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Unit_Mst_Tbl.ParentID -> XBatch_Process_Cell_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Process_Cell_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_UpdateStackLocation.StackID -> XBatch_Storage_Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StackID-XBatch_Storage_Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

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

## XMES_ActiveLife_Element_Mst_Tbl.ElementNameID -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ElementNameID-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.ChargingBedBilletNo -> XMES_Live_Billet_Charging_Bed.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ChargingBedBilletNo-XMES_Live_Billet_Charging_Bed
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.Section1BilletNo -> XMES_Live_Charging_SECT1.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section1BilletNo-XMES_Live_Charging_SECT1
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.Section2BilletNo -> XMES_Live_Charging_SECT2.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section2BilletNo-XMES_Live_Charging_SECT2
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Movement_Dtl_Tbl.ZonewiseBilletNo -> XMES_RM_Furnace_Billet_Trn_Tbl.BilletNo
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ZonewiseBilletNo-XMES_RM_Furnace_Billet_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Strand_tracking.EndProduct -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EndProduct-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Strand_tracking.ParentID -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> Many
Relation: ParentID-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.Materialid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Materialid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.ProcessStage -> XMES_Process_Stage_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcessStage-XMES_Process_Stage_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.Qualitygradeid -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Qualitygradeid-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.StatePosition -> XMES_State_Position_State_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatePosition-XMES_State_Position_State_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_VS_GLS_Grade_Mapping.BilletGrade -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BilletGrade-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_VS_GLS_Grade_Mapping.EndproductGrade -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EndproductGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_VS_GLS_Grade_Mapping.GLSGrade -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GLSGrade-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Campaign_Plan_Mst.ID -> XMES_RM_Campaign_Plan_Trn.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_RM_Campaign_Plan_Trn
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Campaign_Plan_Mst.Productname -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Productname-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.Materialid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Materialid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.ProcessStage -> XMES_Process_Stage_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcessStage-XMES_Process_Stage_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.Qualitygradeid -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Qualitygradeid-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.StatePosition -> XMES_State_Position_State_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatePosition-XMES_State_Position_State_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_CCM_Billet_Master_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Element_Life_Counter_Trn_Tbl.ElementNameID -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ElementNameID-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Element_Life_Type_Mapping_Mst_Tbl.ElementType -> XMES_Life_Element_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ElementType-XMES_Life_Element_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Element_Life_Type_Mapping_Mst_Tbl.ParentID -> XMES_Life_Tracker_Register_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Life_Tracker_Register_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_CCM_Parameters_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_CCM_Remarks_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.Grade -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.Section -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Section-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_EAF_Remarks_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_LRF_Parameters_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_LRF_Remarks_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_Super_Heat_Speed_Nozzle_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Grade_Protocol_Tapping_Additions_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Life_Element_Mst_Tbl.ParentID -> XMES_Life_Element_Type_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Life_Element_Type_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Billet_Charging_Bed.ID -> XMES_Billet_Tracking_Trn_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ID-XMES_Billet_Tracking_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Billet_Charging_Bed.ParentID -> RM_Operator_HeatSelection.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-RM_Operator_HeatSelection
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Charging_SECT1.ParentID -> XMES_Live_Billet_Charging_Bed.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Live_Billet_Charging_Bed
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Charging_SECT2.ID -> XMES_RM_Furnace_Billet_Trn_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_RM_Furnace_Billet_Trn_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Live_Charging_SECT2.ParentID -> XMES_Live_Charging_SECT1.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Live_Charging_SECT1
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Production_Campaign_Tracking.CampaignId -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignId-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Production_Campaign_Tracking.Work_Order -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Work_Order-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.Customer -> XBatch_Customer_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Customer-XBatch_Customer_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.MaterialNo -> XBatch_Material_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialNo-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.ParentID -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.SONumber -> XBatch_Sales_Order_Mst_Tbl.SalesOrderNumber
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SONumber-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Campaign_Plan_Trn.WorkorderNo -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkorderNo-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Furnace_Billet_Trn_Tbl.HeatNo -> XBatch_Material_Inventory_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-XBatch_Material_Inventory_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Furnace_Billet_Trn_Tbl.ParentID -> XMES_Live_Charging_SECT2.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XMES_Live_Charging_SECT2
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Heated_Billet_trn_tbl.Campaignid -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Campaignid-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Heated_Billet_trn_tbl.ProductType -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProductType-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Heated_Billet_trn_tbl.Workorderid -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Workorderid-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Production_Data.EndProductid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EndProductid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Production_Data.Workorderid -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Workorderid-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Tag_Printing_MST.Product -> Product_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Product-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Tag_Printing_TRN.Campaignid -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Campaignid-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_RM_Tag_Printing_TRN.Product -> Product_Master.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Product-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SAP_Batch_Characteristic_Trn_Tbl.Saptransactionid -> XMES_SAP_API_Batch_Characteristics_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Saptransactionid-XMES_SAP_API_Batch_Characteristics_Error
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SAP_CreateBatch_Mst_Tbl.SAPTransactionID -> XMES_SAP_API_Batch_Creation_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: SAPTransactionID-XMES_SAP_API_Batch_Creation_Error
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ParentID -> XMES_SMS_Grade_Protocol_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: ParentID-XMES_SMS_Grade_Protocol_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.ChemistryID -> XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: ChemistryID-XMES_SMS_Grade_Protocol_Chemistry_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.GradeID -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GradeID-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.ID -> XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl.ParentID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: ID-XMES_Grade_Protocol_EAF_Parameters_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_SMS_Grade_Protocol_Mst_Tbl.SectionID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SectionID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Stage_Position_Mapping_Mst_Tbl.PositionType -> XMES_State_Position_State_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: PositionType-XMES_State_Position_State_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Stage_Position_Mapping_Mst_Tbl.StageCode -> XMES_Process_Stage_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StageCode-XMES_Process_Stage_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Work_Order_Trn_Tbl.CampaignID -> XMES_Campaign_Plan_Mst.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: CampaignID-XMES_Campaign_Plan_Mst
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Work_Order_Trn_Tbl.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xstudio_Xbatch_ChargingPlan_Mst_Tbl.Stackid -> XBatch_Storage_Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Stackid-XBatch_Storage_Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

