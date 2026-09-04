# XStudio_Xbatch.dbo.XStudio_List_MES_SAP_Production_Trn_Tbl_SAPPostingFail_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| CreationDate | date | YES |
| WorkOrderNumber | varchar | YES |
| ID | varchar | NO |
| PostingDate | datetime | YES |
| Name | varchar | YES |
| HeatNo | int | YES |
| EntryDateTime | datetime | YES |
| CreatedOn | datetime | YES |
| Edit | varchar | NO |
| ReportDate | date | YES |
| IsProcessed | bit | YES |
| Action | varchar | YES |
| SAPPostingStatus | varchar | YES |
| Batch | varchar | YES |
| Material | varchar | YES |
| QuantityInEntryUnit | decimal | YES |
| QuantityInCount | int | YES |
| InspectionLot | varchar | YES |
| MaterialDocument | bigint | YES |
| Plant | varchar | YES |
| InventoryTransactionType | varchar | YES |
| StorageLocation | varchar | YES |
| DocumentDate | datetime | YES |
| CreationTime | time | YES |
| CreatedByUser | varchar | YES |
| Grade | varchar | YES |
| EntryUnit | varchar | YES |
| MaterialDocumentHeaderText | varchar | YES |
| ReferenceDocument | varchar | YES |
| ControlPostingforExternamWMS | varchar | YES |
| VersionForPrintingSlip | int | YES |
| ManualPrintLsTriggered | varchar | YES |
| PostingMaterialType | varchar | YES |
| MaterialDocumentItem | varchar | YES |
| Delete | varchar | NO |
| Details | varchar | NO |
| GoodsMovementType | int | YES |
| MaterialDocumentYear | int | YES |
| GoodsMovementCode | varchar | YES |
| ErrorMessage | varchar | YES |
| SAPTransactionID | varchar | YES |

## Sample rows (top 5, real live data)

| CreationDate | WorkOrderNumber | ID | PostingDate | Name | HeatNo | EntryDateTime | CreatedOn | Edit | ReportDate | IsProcessed | Action | SAPPostingStatus | Batch | Material | QuantityInEntryUnit | QuantityInCount | InspectionLot | MaterialDocument | Plant | InventoryTransactionType | StorageLocation | DocumentDate | CreationTime | CreatedByUser | Grade | EntryUnit | MaterialDocumentHeaderText | ReferenceDocument | ControlPostingforExternamWMS | VersionForPrintingSlip | ManualPrintLsTriggered | PostingMaterialType | MaterialDocumentItem | Delete | Details | GoodsMovementType | MaterialDocumentYear | GoodsMovementCode | ErrorMessage | SAPTransactionID |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-03-03 | 140000000240 | 8FD240F0-DBF1-4B25-9F1F-4EE4368AFC0A | 2026-03-03 04:00:00 |  | 1601478 |  | 2026-03-03 05:17:38.910000 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Production_Trn_Tbl","LinkTarget": |  |  | Posted | Posted | 1601478_12 | BL_B500BLMNHC_150X150 | 75.600 | 36 | 40002997923 | 5003177253 | 7502 | WF | 2103 | 2026-03-03 04:00:00 | 05:18:27 | CPIMESUSER | B500BLMNHC | TO |  |  |  | 2 |  | Hot Billet | 0001 | {"LvId": "5E98480E-394C-4CB6-875C-0C019F70187F","RecordId" : "8FD240F0-DBF1-4B25 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 | 101 | 2026 | 02 |  | 4ea1cacb-eb6b-413c-b140-16bea2ff21af |
| 2026-06-21 | 120000185023 | 8FD5A763-9476-4DB3-9588-AC50935DB107 | 2026-06-21 04:00:00 |  | 1603667 |  | 2026-06-21 14:50:14.733000 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Production_Trn_Tbl","LinkTarget": |  |  | Posted | Posted | 1603667 | B500B_GLS | 76.770 | 1 | 40004237401 | 5003497628 | 7502 | WF | 2103 | 2026-06-21 04:00:00 | 14:50:44 | CPIMESUSER | B500B | TO |  |  |  | 2 |  | GLS | 0001 | {"LvId": "5E98480E-394C-4CB6-875C-0C019F70187F","RecordId" : "8FD5A763-9476-4DB3 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 | 101 | 2026 | 02 |  | 04c9deed-1c8d-49ae-83c6-d876d58077bb |
|  | MES_2025122217_BL | 8FE23620-F6FA-45CD-A742-F735C86C4FAD | 2025-12-23 00:00:00 |  | 1507694 |  | 2025-12-23 11:42:25.810000 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Production_Trn_Tbl","LinkTarget": |  |  | Posted | Posted | 1507694_12 | BL_BS4449_130X130 | 8.400 | 4 |  |  |  |  |  |  |  |  | 3SP/PS | TO |  |  |  |  |  | Cold Billet |  | {"LvId": "5E98480E-394C-4CB6-875C-0C019F70187F","RecordId" : "8FE23620-F6FA-45CD | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 | 110 |  |  |  |  |
| 2026-07-05 | 120000186310 | 8FE23CFA-864E-43C2-83F2-7FF2FB5ADBB4 | 2026-07-05 00:00:00 |  | 1603947 |  | 2026-07-05 15:50:33.600000 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Production_Trn_Tbl","LinkTarget": |  |  | Posted | Posted | 1603947 | LIQUID METAL | 81.060 | 1 |  | 5003507428 | 7502 | WF | 2103 | 2026-07-05 00:00:00 | 15:51:17 | CPIMESUSER | HHMNB500B | TO |  |  |  | 2 |  | LS |  | {"LvId": "5E98480E-394C-4CB6-875C-0C019F70187F","RecordId" : "8FE23CFA-864E-43C2 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 | 101 | 2026 | 02 |  | 9724a526-9685-46e0-9354-b95f36a45dea |
| 2026-02-18 | 120000150400 | 8FE4D1E5-56FB-451E-82C7-F785699DFA0F | 2026-02-18 00:00:00 |  | 1601153 |  | 2026-02-18 04:52:38.927000 | {"Link": "XBatch/ControlRoom/Edit_Page_MES_SAP_Production_Trn_Tbl","LinkTarget": |  |  | Posted | Posted | 1601153 | LIQUID METAL | 82.210 | 1 |  | 5003176296 | 7502 | WF | 2103 | 2026-02-18 00:00:00 | 04:53:58 | CPIMESUSER | 3SP/PS | TO |  |  |  | 2 |  | LS |  | {"LvId": "5E98480E-394C-4CB6-875C-0C019F70187F","RecordId" : "8FE4D1E5-56FB-451E | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"5C74E38C-94FF-47E8-A2 | 101 | 2026 | 02 |  | b3eaa1b0-8c54-4a08-831f-3512bec163b1 |