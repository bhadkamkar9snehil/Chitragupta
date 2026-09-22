---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-sap-createbatch-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_SAP_CreateBatch_Mst_Tbl.SAPTransactionID -> XMES_SAP_API_Batch_Creation_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: SAPTransactionID-XMES_SAP_API_Batch_Creation_Error
Provenance: xstudio_configuration_relationship (1 source row(s))
