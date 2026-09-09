---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: X part 1

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
