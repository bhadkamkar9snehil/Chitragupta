---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: sap-posting-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## SAP_Posting_Tbl.CreatedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: CreatedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SAP_Posting_Tbl.MaterialCode -> XBatch_Material_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialCode-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SAP_Posting_Tbl.ModifiedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ModifiedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SAP_Posting_Tbl.StorageLocation -> XBatch_Store_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StorageLocation-XBatch_Store_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## SAP_Posting_Tbl.WorkOrderNo -> XBatch_Work_Order_Mst_Tbl.WorkOrderNumber
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrderNo-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
