---
type: Reference
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: P

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Per_Heat_LadleNo.EAFShellNo -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EAFShellNo-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Per_Heat_LadleNo.LadleNo -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LadleNo-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Per_Heat_LadleNo.TundishNo -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TundishNo-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Plant_Mst_Tbl.ParentID -> Organisation_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-Organisation_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Plant_Mst_Tbl.ParentID -> Organization_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-Organization_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Power_Meter_Reading_Time.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Power_Meter_Reading_Time.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Procedure_Mst_Tbl.AreaID -> Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: AreaID-Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Procedure_Steps_Mst_Tbl.ProcedureID -> Procedure_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcedureID-Procedure_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Procedure_Task_Mst_Tbl.EntityID -> XStudio_Entities_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EntityID-XStudio_Entities_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Procedure_Task_Mst_Tbl.PageID -> XStudio_Page_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: PageID-XStudio_Page_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Procedure_Task_Mst_Tbl.ViewPageID -> XStudio_Page_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ViewPageID-XStudio_Page_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Product_Master.Name -> XMES_Billet_Strand_tracking.EndProduct
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> Many
Relation: Name-XMES_Billet_Strand_tracking
Provenance: xstudio_configuration_relationship (1 source row(s))

## ProductionMonthlyTargets.FiscalYear -> financialyears.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: FiscalYear-financialyears
Provenance: xstudio_configuration_relationship (1 source row(s))

## ProductionWeeklyTargets.Month -> ProductionMonthlyTargets.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Month-ProductionMonthlyTargets
Provenance: xstudio_configuration_relationship (1 source row(s))

## ProductionWeeklyTargets.Week -> Week_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Week-Week_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## PTW_Details.EngineerName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: EngineerName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## PTW_Details.TechnicianName -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: TechnicianName-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

