# XStudio_Xbatch.dbo.XStudio_List_Billet_Inventory_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Material | varchar | YES |
| Edit | varchar | NO |
| MaterialCode | varchar | YES |
| ID | varchar | NO |
| HeatNo | varchar | YES |
| Operation_Name | varchar | YES |
| Billetno | varchar | YES |
| MaterialGrade | varchar | YES |
| LocationName | varchar | YES |
| Grade | varchar | YES |
| Quantity | decimal | YES |
| UOM | varchar | YES |
| IsAllocated | varchar | YES |
| LocationType | varchar | YES |
| Description | varchar | YES |
| ReceivedDate | datetime | YES |
| Remark | varchar | YES |
| ExpiryDate | date | YES |
| Crosssection | varchar | YES |
| GradeID | varchar | YES |
| GRNNumber | varchar | YES |
| Height | int | YES |
| IsAvailable | varchar | YES |
| InvoiceNumber | varchar | YES |
| IsExpired | bit | YES |
| ItemSource | varchar | YES |
| Length | int | YES |
| PONumber | varchar | YES |
| Price | decimal | YES |
| MaterialID | varchar | YES |
| OperationID | varchar | YES |
| TotalQty | int | YES |
| Vendor | varchar | YES |
| UOMID | varchar | YES |
| Delete | varchar | NO |
| Details | varchar | NO |

## Sample rows (top 5, real live data)

| Material | Edit | MaterialCode | ID | HeatNo | Operation_Name | Billetno | MaterialGrade | LocationName | Grade | Quantity | UOM | IsAllocated | LocationType | Description | ReceivedDate | Remark | ExpiryDate | Crosssection | GradeID | GRNNumber | Height | IsAvailable | InvoiceNumber | IsExpired | ItemSource | Length | PONumber | Price | MaterialID | OperationID | TotalQty | Vendor | UOMID | Delete | Details |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | {"Link": "XBatch/POManagement/Edit_Page_Billet_Inventory","LinkTarget": "null"," |  | 004E82B1-3734-432D-819F-DDFF8831D8EE | B50001 |  | B50001_2 | B500B |  | Okay | 1.0000 | ton | 1 | Store |  | 2025-07-07 12:46:42 |  |  |  | 950B0189-B75E-44D1-9BEC-F1A250DA000C |  |  | NULL |  |  | Receive |  |  |  | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 |  | 0 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"LvId": "A338CBC5-B79E-48D0-B469-78A4A47D7DCC","RecordId" : "004E82B1-3734-432D | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"A338CBC5-B79E-48D0-B4 |
|  | {"Link": "XBatch/POManagement/Edit_Page_Billet_Inventory","LinkTarget": "null"," |  | 0204A31E-5D82-48C8-A701-0D8E2C039E53 | B50001 |  | B50001_49 | B500B |  | Okay | 1.0000 | ton |  | Store |  | 2025-07-09 00:00:00 |  |  |  | 950B0189-B75E-44D1-9BEC-F1A250DA000C |  |  |  |  |  | Receive |  |  |  | AFC27FBE-93C1-4855-B3AE-3AD0791AC3E1 |  | 0 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"LvId": "A338CBC5-B79E-48D0-B469-78A4A47D7DCC","RecordId" : "0204A31E-5D82-48C8 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"A338CBC5-B79E-48D0-B4 |
|  | {"Link": "XBatch/POManagement/Edit_Page_Billet_Inventory","LinkTarget": "null"," |  | 030C69AB-BA6A-4869-8E4E-98875C5691CB | H0022 |  | H0022_2 |  |  | Okay | 1.0000 | ton |  | Store |  | 2025-07-04 12:50:06 |  |  |  | 950B0189-B75E-44D1-9BEC-F1A250DA000C |  |  | NULL |  |  | Receive |  |  |  | 359A9737-7B27-4CB8-BB2B-0D31F0E6F17A |  | 0 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"LvId": "A338CBC5-B79E-48D0-B469-78A4A47D7DCC","RecordId" : "030C69AB-BA6A-4869 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"A338CBC5-B79E-48D0-B4 |
|  | {"Link": "XBatch/POManagement/Edit_Page_Billet_Inventory","LinkTarget": "null"," |  | 03714AA3-5F1A-4699-9880-6C9B5DF6491F | H0018 |  | H0018_1 |  |  | Okay | 1.0000 | ton |  | Store |  | 2025-07-04 12:39:43 |  |  |  | 950B0189-B75E-44D1-9BEC-F1A250DA000C |  |  | NULL |  |  | Receive |  |  |  | 74107DC9-D59A-442B-AD57-10EB22DE8B6D |  | 0 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"LvId": "A338CBC5-B79E-48D0-B469-78A4A47D7DCC","RecordId" : "03714AA3-5F1A-4699 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"A338CBC5-B79E-48D0-B4 |
|  | {"Link": "XBatch/POManagement/Edit_Page_Billet_Inventory","LinkTarget": "null"," |  | 040197D3-B754-4A2C-8790-E1C95B93FED8 | H0018 |  | H0018_3 |  |  | Okay | 1.0000 | ton |  | Store |  | 2025-07-04 12:40:47 |  |  |  | 950B0189-B75E-44D1-9BEC-F1A250DA000C |  |  | NULL |  |  | Receive |  |  |  | 74107DC9-D59A-442B-AD57-10EB22DE8B6D |  | 0 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"LvId": "A338CBC5-B79E-48D0-B469-78A4A47D7DCC","RecordId" : "040197D3-B754-4A2C | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"A338CBC5-B79E-48D0-B4 |