# XStudio_Xbatch.dbo.XStudio_List_MES_SAP_Consumption_Trn_Tbl_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| PostingDate | datetime | YES |
| CreationDate | date | YES |
| Edit | varchar | NO |
| WorkOrderNumber | varchar | YES |
| ID | varchar | NO |
| HeatNo | int | YES |
| Batch | varchar | YES |
| Grade | varchar | YES |
| Name | varchar | YES |
| Material | varchar | YES |
| Action | varchar | YES |
| SAPPostingStatus | varchar | YES |
| PostingMaterialType | varchar | YES |
| ErrorMessageLink | varchar | NO |
| SuccessMessage | varchar | YES |
| QuantityInCount | int | YES |
| MaterialDocument | varchar | YES |
| EntryDateTime | datetime | YES |
| GoodsMovementType | int | YES |
| QuantityInEntryUnit | decimal | YES |
| Plant | varchar | YES |
| ReportDate | date | YES |
| EntryUnit | varchar | YES |
| IsProcessed | bit | YES |
| StorageLocation | varchar | YES |
| InventoryTransactionType | varchar | YES |
| MaterialDocumentYear | int | YES |
| DocumentDate | datetime | YES |
| ControlPostingforExternamWMS | varchar | YES |
| CreationTime | time | YES |
| InspectionLot | int | YES |
| CreatedByUser | varchar | YES |
| MaterialDocumentHeaderText | varchar | YES |
| ReferenceDocument | varchar | YES |
| VersionForPrintingSlip | int | YES |
| ManualPrintLsTriggered | varchar | YES |
| GoodsMovementCode | varchar | YES |
| MaterialDocumentItem | varchar | YES |
| ErrorMessage | varchar | YES |
| SAPTransactionID | varchar | YES |
| Delete | varchar | NO |
| Details | varchar | NO |

## Sample rows (top 5, real live data)

| PostingDate | CreationDate | Edit | WorkOrderNumber | ID | HeatNo | Batch | Grade | Name | Material | Action | SAPPostingStatus | PostingMaterialType | ErrorMessageLink | SuccessMessage | QuantityInCount | MaterialDocument | EntryDateTime | GoodsMovementType | QuantityInEntryUnit | Plant | ReportDate | EntryUnit | IsProcessed | StorageLocation | InventoryTransactionType | MaterialDocumentYear | DocumentDate | ControlPostingforExternamWMS | CreationTime | InspectionLot | CreatedByUser | MaterialDocumentHeaderText | ReferenceDocument | VersionForPrintingSlip | ManualPrintLsTriggered | GoodsMovementCode | MaterialDocumentItem | ErrorMessage | SAPTransactionID | Delete | Details |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-03-17 04:00:00 | 2026-03-17 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Consumption_Trn_Tbl","LinkTarget" | 120000152984 | 5EB812C7-D1C5-4B47-98B8-27243A695744 | 1601839 | 1601839 | HHMNB500B |  | LIQUID METAL | Posted | Posted | LS | {"Link":"XBatch/ControlRoom/List_Page_XMES_SAP_API_GoodsMovement_Production_Erro |  | 1 | 4910870447 |  | 261 | 80.110 | 7502 |  | TO |  | 2103 | WA | 2026 | 2026-03-17 04:00:00 |  | 11:32:39 |  | CPIMESUSER |  |  | 2 |  | 03 |  |  | ae889b83-32cf-4591-a78d-f0ca2b1d0930 | {"LvId": "DF8CE9FA-D650-45CE-8970-FFB105AF8B9F","RecordId" : "5EB812C7-D1C5-4B47 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 |
| 2026-02-22 00:00:00 |  | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Consumption_Trn_Tbl","LinkTarget" | 120000150401 | 5EBAB5F4-CCF3-4F0F-AE3C-5A7EE63443E6 | 1601271 | 1601271 | B500B |  | LIQUID METAL | Entered | Entered | LS | {"Link":"XBatch/ControlRoom/List_Page_XMES_SAP_API_GoodsMovement_Production_Erro |  | 1 |  |  | 261 | 80.110 | 7502 |  | TO |  | 2103 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"LvId": "DF8CE9FA-D650-45CE-8970-FFB105AF8B9F","RecordId" : "5EBAB5F4-CCF3-4F0F | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 |
| 2026-03-04 04:00:00 | 2026-03-05 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Consumption_Trn_Tbl","LinkTarget" | 140000000240 | 5EBB46A5-2181-4B5A-9722-6F8F044BB22F | 1601523 | 1601523 | B500B |  | B500BLMNHC_GLS | Posted | Posted | GLS | {"Link":"XBatch/ControlRoom/List_Page_XMES_SAP_API_GoodsMovement_Production_Erro |  | 1 | 4909002708 |  | 261 | 80.110 | 7502 |  | TO |  | 2103 | WA | 2026 | 2026-03-05 04:00:00 |  | 04:48:13 |  | CPIMESUSER |  |  | 2 |  | 03 |  |  | ff77597a-bac5-4027-8ab2-9b4ebcb8a762 | {"LvId": "DF8CE9FA-D650-45CE-8970-FFB105AF8B9F","RecordId" : "5EBB46A5-2181-4B5A | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 |
| 2026-06-22 04:00:00 | 2026-06-22 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Consumption_Trn_Tbl","LinkTarget" | 120000185023 | 5EC56173-302F-4953-9B92-2537B0EB0C34 | 1603683 | 1603683 | B500B |  | LIQUID METAL | Posted | Posted | LS | {"Link":"XBatch/ControlRoom/List_Page_XMES_SAP_API_GoodsMovement_Production_Erro |  | 1 | 4911552459 |  | 261 | 78.900 | 7502 |  | TO |  | 2103 | WA | 2026 | 2026-06-22 04:00:00 |  | 12:45:27 |  | CPIMESUSER |  |  | 2 |  | 03 |  |  | 13b1a39f-fa33-4a70-b2a1-d1dc18c2f962 | {"LvId": "DF8CE9FA-D650-45CE-8970-FFB105AF8B9F","RecordId" : "5EC56173-302F-4953 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 |
| 2026-06-02 04:00:00 | 2026-06-02 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Consumption_Trn_Tbl","LinkTarget" | 140000000228 | 5EC8809F-0C49-409F-82BF-58F2CEEC769A | 1603321 | 1603321 | B500BLMNHC |  | B500BLMNHC_GLS | Posted | Posted | GLS | {"Link":"XBatch/ControlRoom/List_Page_XMES_SAP_API_GoodsMovement_Production_Erro |  | 1 | 4911418853 |  | 261 | 80.570 | 7502 |  | TO |  | 2103 | WA | 2026 | 2026-06-02 04:00:00 |  | 21:53:51 |  | CPIMESUSER |  |  | 2 |  | 03 |  |  | 795ad4e6-3efe-40fb-a4ad-422c0cee85c4 | {"LvId": "DF8CE9FA-D650-45CE-8970-FFB105AF8B9F","RecordId" : "5EC8809F-0C49-409F | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 |