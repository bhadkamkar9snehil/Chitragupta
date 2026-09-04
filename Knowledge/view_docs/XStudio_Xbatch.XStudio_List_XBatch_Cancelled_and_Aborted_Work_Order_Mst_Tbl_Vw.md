# XStudio_Xbatch.dbo.XStudio_List_XBatch_Cancelled_and_Aborted_Work_Order_Mst_Tbl_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Edit | varchar | NO |
| CreationDate | datetime | YES |
| ReleasedDate | datetime | YES |
| ID | varchar | NO |
| BatchSchedule | varchar | YES |
| SalesOrder | varchar | YES |
| SAPWorkOrderNumber | varchar | YES |
| WorkOrderNumber | varchar | YES |
| WorkOrderType | varchar | YES |
| Action | varchar | YES |
| Status | varchar | YES |
| ItemName | varchar | YES |
| CustomerName | varchar | YES |
| Equipment | varchar | YES |
| ItemID | varchar | NO |
| ParentID | varchar | YES |
| TotalQuantity | decimal | NO |
| Unit | varchar | YES |
| ProgressTonnage | decimal | YES |
| RemainingTonnage | decimal | YES |
| ProgressPercentage | decimal | YES |
| ProgressDurationinDays | decimal | YES |
| Details | varchar | NO |
| MfgOrderActualReleaseDate | varchar | YES |
| UnitID | varchar | YES |
| PlannedCompletionDate | datetime | YES |
| Description | varchar | YES |
| ProductionUnit | varchar | YES |
| SerialNumber | int | YES |
| ColourCode | varchar | YES |
| Delete | varchar | NO |
| StatusColourCode | varchar | YES |
| ItemColourCode | varchar | YES |
| WorkOrderMoreDetails | varchar | YES |
| ProductionPlant | int | YES |

## Sample rows (top 5, real live data)

| Edit | CreationDate | ReleasedDate | ID | BatchSchedule | SalesOrder | SAPWorkOrderNumber | WorkOrderNumber | WorkOrderType | Action | Status | ItemName | CustomerName | Equipment | ItemID | ParentID | TotalQuantity | Unit | ProgressTonnage | RemainingTonnage | ProgressPercentage | ProgressDurationinDays | Details | MfgOrderActualReleaseDate | UnitID | PlannedCompletionDate | Description | ProductionUnit | SerialNumber | ColourCode | Delete | StatusColourCode | ItemColourCode | WorkOrderMoreDetails | ProductionPlant |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 2026-03-10 13:06:48.003000 |  | 058412B5-AABA-46A8-9257-60F1FD68D443 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/058412B |  |  | 120000154929 | LI01 | Completed | Completed | SP3/PS_GLS |  | LRF | 74C3C03E-B548-4326-96E2-50A95D104D2E |  | 700000.00 | ton | 146.3200 | 699853.6800 | 0.0209 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | 2026-03-31 00:00:00 |  |  | 2780 |  | {"LvId": "437D60AF-8D2B-4FC8-8D94-29E863FACE73","RecordId" : "058412B5-AABA-46A8 | background-color:#1976d2; color:#ffffff | background-color:#563d7c; color:#f2f2f2 | {"Link":"XBatch/ControlRoom/Page_XBatch_SAP_Work_Order_Mobile_View?ID=058412B5-A | 7502 |
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 2026-04-02 09:59:03.590000 |  | 1000F5E1-7393-40D5-9E45-AAA190CAF585 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1000F5E |  |  | 140000000262 | SS02 | OnHold | OnHold | BL_HHMNB500B_150X150 |  | CCM | 7EAD0236-546E-4793-9454-FE721DFAACEC |  | 65000.00 | ton | 4697.8500 | 60302.1500 | 7.2275 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | 2026-04-30 00:00:00 |  |  | 2880 |  | {"LvId": "437D60AF-8D2B-4FC8-8D94-29E863FACE73","RecordId" : "1000F5E1-7393-40D5 | background-color:#e53935; color:#ffffff | background-color:#563d7c; color:#f2f2f2 | {"Link":"XBatch/ControlRoom/Page_XBatch_SAP_Work_Order_Mobile_View?ID=1000F5E1-7 | 7502 |
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 2026-08-21 15:52:07.357000 | 2026-08-21 15:52:07.357000 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/180EACB |  | CP3_21082026_RB25mm_WO_1 | 120000102360 | BR01 | OnHold | OnHold | RB_B500B_25.0DIA |  | RM | E61A1D64-A311-4349-93F8-22F6313372E3 |  | 300.00 | MT | 596.9380 | -296.9380 | 198.9793 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 |  | 2095DF88-C3E3-4184-BA44-BBBB0696FF14 | 2026-09-20 00:00:00 |  |  |  |  | {"LvId": "437D60AF-8D2B-4FC8-8D94-29E863FACE73","RecordId" : "180EACB3-BBC6-4DA8 | background-color:#e53935; color:#ffffff | background-color:#563d7c; color:#f2f2f2 | {"Link":"XBatch/ControlRoom/Page_XBatch_SAP_Work_Order_Mobile_View?ID=180EACB3-B | 8503 |
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 2026-03-10 13:00:04.363000 |  | 1A47B409-5542-4AB2-9EB5-6738BF235073 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1A47B40 |  |  | 140000000228 | SS02 | OnHold | OnHold | BL_B500BLMNHC_150X150 |  | CCM | 86346D18-CBF6-442E-A05F-0E9C7CB5D2D9 |  | 300000.00 | ton | 80819.4700 | 219180.5300 | 26.9398 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 |  | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | 2026-03-31 00:00:00 |  |  | 2770 |  | {"LvId": "437D60AF-8D2B-4FC8-8D94-29E863FACE73","RecordId" : "1A47B409-5542-4AB2 | background-color:#e53935; color:#ffffff | background-color:#914e80; color:#ffffff | {"Link":"XBatch/ControlRoom/Page_XBatch_SAP_Work_Order_Mobile_View?ID=1A47B409-5 | 7502 |
| {"Link": "XBatch/Order/Edit_Page_XBatch_Work_Order_Mst_Tbl","LinkTarget": "Blank | 2026-08-21 15:52:07.613000 | 2026-08-21 15:52:07.613000 | 1D9B8320-D712-41EF-BDBE-3BC6EDE99C34 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1D9B832 |  | CP3_21082026_RB25mm_WO_8 | 120000102356 | BR01 | RM ProductionOrder Created | RM ProductionOrder Created | RB_B500B_25.0DIA |  | RM | E61A1D64-A311-4349-93F8-22F6313372E3 |  | 150.00 | MT | 0.0000 | 150.0000 | 0.0000 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 |  | 2095DF88-C3E3-4184-BA44-BBBB0696FF14 | 2026-09-20 00:00:00 |  |  |  |  | {"LvId": "437D60AF-8D2B-4FC8-8D94-29E863FACE73","RecordId" : "1D9B8320-D712-41EF |  | background-color:#563d7c; color:#f2f2f2 | {"Link":"XBatch/ControlRoom/Page_XBatch_SAP_Work_Order_Mobile_View?ID=1D9B8320-D | 8503 |