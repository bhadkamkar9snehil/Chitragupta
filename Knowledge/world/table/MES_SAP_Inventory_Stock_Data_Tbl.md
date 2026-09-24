---
type: table
title: "MES_SAP_Inventory_Stock_Data_Tbl"
built: "2026-09-24T11:36:36"
---

# MES_SAP_Inventory_Stock_Data_Tbl

Table in XStudio_Xbatch. Rows: 3,961.

## Identifiers it holds

- SDDocument: same values as key `SDDocument`

## Written by

- XMES_SAP_I_Inventory_Stock_Data_Usp

## Read by

- XMES_SAP_I_Inventory_Stock_Data_Usp

## Columns

- ID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- Supplier varchar(100)
- EntryDateTime datetime
- Name varchar(100)
- Material varchar(100)
- SDDocument varchar(100)
- ReportDate date
- InventoryStockType varchar(100)
- MatlWrhsStkQtyInMatlBaseUnit decimal
- SDDocumentItem int
- Customer varchar(100)
- MaterialBaseUnit varchar(100)
- Plant int
- Batch varchar(100)
- ParentID varchar(36)
- InventorySpecialStockType varchar(100)
- WebElementInternalID varchar(100)
- StorageLocation varchar(100)
- IsProcessed bit
- MetaData varchar(-1)
- UnrestrictedUseStock varchar(100)
- StockinQualityInspection varchar(100)
- Returns varchar(100)
- StockTransferStorageLocation varchar(100)
- StockTransferPlant varchar(100)
- StockinTransit varchar(100)
- BlockedStock varchar(100)
- RestrictedUseStock varchar(100)
- TiedEmpties varchar(100)
- ValuatedGoodsReceiptBlockedStock varchar(100)
