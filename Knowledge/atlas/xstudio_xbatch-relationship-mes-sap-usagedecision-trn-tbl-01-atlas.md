---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: mes-sap-usagedecision-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## MES_SAP_UsageDecision_Trn_Tbl.SAPTransactionID -> XMES_SAP_API_UsageDecision_Error.TransactionID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: One -> One
Relation: SAPTransactionID-XMES_SAP_API_UsageDecision_Error
Provenance: xstudio_configuration_relationship (1 source row(s))
