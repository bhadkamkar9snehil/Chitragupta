# XStudio_Xbatch.dbo.XStudio_List_XBatch_Work_Order_Mst_Tbl_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Edit | varchar | NO |
| WorkOrderNumber | varchar | YES |
| WorkOrderType | varchar | YES |
| ID | varchar | NO |
| CreationDate | datetime | YES |
| BatchSchedule | varchar | YES |
| SAPWorkOrderNumber | varchar | YES |
| ReleasedDate | datetime | YES |
| SalesOrder | varchar | YES |
| Action | varchar | YES |
| ProductionPosting | varchar | YES |
| Status | varchar | YES |
| ItemName | varchar | YES |
| CustomerName | varchar | YES |
| ItemID | varchar | NO |
| Equipment | varchar | YES |
| ParentID | varchar | YES |
| TotalQuantity | decimal | NO |
| Unit | varchar | YES |
| ProgressTonnage | decimal | YES |
| RemainingTonnage | decimal | YES |
| Details | varchar | NO |
| ProgressPercentage | decimal | YES |
| ProgressDurationinDays | decimal | YES |
| UnitID | varchar | YES |
| MfgOrderActualReleaseDate | varchar | YES |
| ProductionUnit | varchar | YES |
| Description | varchar | YES |
| SerialNumber | int | YES |
| WorkOrderMoreDetails | varchar | YES |
| ColourCode | varchar | YES |
| Delete | varchar | NO |
| StatusColourCode | varchar | YES |
| ItemColourCode | varchar | YES |
| ListPageName | varchar | YES |

## Sample rows (top 5, real live data)

| Edit | WorkOrderNumber | WorkOrderType | ID | CreationDate | BatchSchedule | SAPWorkOrderNumber | ReleasedDate | SalesOrder | Action | ProductionPosting | Status | ItemName | CustomerName | ItemID | Equipment | ParentID | TotalQuantity | Unit | ProgressTonnage | RemainingTonnage | Details | ProgressPercentage | ProgressDurationinDays | UnitID | MfgOrderActualReleaseDate | ProductionUnit | Description | SerialNumber | WorkOrderMoreDetails | ColourCode | Delete | StatusColourCode | ItemColourCode | ListPageName |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 120000154929 | LI01 | 058412B5-AABA-46A8-9257-60F1FD68D443 | 2026-03-10 13:06:48.003000 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/058412B |  |  |  | Completed | {"Link":"XBatch/ControlRoom/Page_List_LRF_Per_Heat_SAP?WOid=058412B5-AABA-46A8-9 | Completed | SP3/PS_GLS |  | 74C3C03E-B548-4326-96E2-50A95D104D2E | LRF |  | 700000.00 | ton | 146.3200 | 699853.6800 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 0.0209 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F |  |  |  | 2780 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | {"LvId": "AB525A23-E034-4FFB-8436-9F972199391F","RecordId" : "058412B5-AABA-46A8 | background-color:#1976d2; color:#ffffff | background-color:#563d7c; color:#f2f2f2 | Page_List_LRF_Per_Heat_SAP |
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 140000000262 | SS02 | 1000F5E1-7393-40D5-9E45-AAA190CAF585 | 2026-04-02 09:59:03.590000 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1000F5E |  |  |  | OnHold | {"Link":"XBatch/ControlRoom/List_Page_CCM_Per_Heat_SAP?WOid=1000F5E1-7393-40D5-9 | OnHold | BL_HHMNB500B_150X150 |  | 7EAD0236-546E-4793-9454-FE721DFAACEC | CCM |  | 65000.00 | ton | 4697.8500 | 60302.1500 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 7.2275 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F |  |  |  | 2880 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | {"LvId": "AB525A23-E034-4FFB-8436-9F972199391F","RecordId" : "1000F5E1-7393-40D5 | background-color:#e53935; color:#ffffff | background-color:#563d7c; color:#f2f2f2 | List_Page_CCM_Per_Heat_SAP |
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 120000102360 | BR01 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | 2026-08-21 15:52:07.357000 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/180EACB | CP3_21082026_RB25mm_WO_1 | 2026-08-21 15:52:07.357000 |  | OnHold | {"Link":"XBatch/ControlRoom/?WOid=180EACB3-BBC6-4DA8-AF75-21A68771A773", "LinkTa | OnHold | RB_B500B_25.0DIA |  | E61A1D64-A311-4349-93F8-22F6313372E3 | RM |  | 300.00 | MT | 596.9380 | -296.9380 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 198.9793 |  | 2095DF88-C3E3-4184-BA44-BBBB0696FF14 |  |  |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | {"LvId": "AB525A23-E034-4FFB-8436-9F972199391F","RecordId" : "180EACB3-BBC6-4DA8 | background-color:#e53935; color:#ffffff | background-color:#563d7c; color:#f2f2f2 |  |
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 140000000228 | SS02 | 1A47B409-5542-4AB2-9EB5-6738BF235073 | 2026-03-10 13:00:04.363000 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1A47B40 |  |  |  | OnHold | {"Link":"XBatch/ControlRoom/List_Page_CCM_Per_Heat_SAP?WOid=1A47B409-5542-4AB2-9 | OnHold | BL_B500BLMNHC_150X150 |  | 86346D18-CBF6-442E-A05F-0E9C7CB5D2D9 | CCM |  | 300000.00 | ton | 80819.4700 | 219180.5300 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 26.9398 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F |  |  |  | 2770 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | {"LvId": "AB525A23-E034-4FFB-8436-9F972199391F","RecordId" : "1A47B409-5542-4AB2 | background-color:#e53935; color:#ffffff | background-color:#914e80; color:#ffffff | List_Page_CCM_Per_Heat_SAP |
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 120000102356 | BR01 | 1D9B8320-D712-41EF-BDBE-3BC6EDE99C34 | 2026-08-21 15:52:07.613000 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1D9B832 | CP3_21082026_RB25mm_WO_8 | 2026-08-21 15:52:07.613000 |  | RM ProductionOrder Created | {"Link":"XBatch/ControlRoom/?WOid=1D9B8320-D712-41EF-BDBE-3BC6EDE99C34", "LinkTa | RM ProductionOrder Created | RB_B500B_25.0DIA |  | E61A1D64-A311-4349-93F8-22F6313372E3 | RM |  | 150.00 | MT | 0.0000 | 150.0000 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 0.0000 |  | 2095DF88-C3E3-4184-BA44-BBBB0696FF14 |  |  |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | {"LvId": "AB525A23-E034-4FFB-8436-9F972199391F","RecordId" : "1D9B8320-D712-41EF |  | background-color:#563d7c; color:#f2f2f2 |  |