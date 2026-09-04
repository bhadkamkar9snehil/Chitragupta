# XStudio_Xbatch.dbo.XStudio_XMes_Campaign_Plan_work_order_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Edit | varchar | NO |
| WorkOrderNumber | varchar | YES |
| WorkOrderType | varchar | YES |
| ID | varchar | NO |
| BatchSchedule | varchar | YES |
| MESWorkOrderNumber | varchar | YES |
| CampaignNo | varchar | YES |
| CreatedDate | datetime | YES |
| ReleasedDate | datetime | YES |
| Action | varchar | YES |
| SalesOrder | varchar | YES |
| ProductionPosting | varchar | YES |
| CustomerName | varchar | YES |
| Status | varchar | YES |
| Equipment | varchar | YES |
| ItemID | varchar | NO |
| ParentID | varchar | YES |
| ItemName | varchar | YES |
| TotalQuantity | decimal | NO |
| Unit | varchar | YES |
| CutLengthMtr | decimal | YES |
| CrossSectionmm | varchar | YES |
| ProgressDurationinDays | decimal | YES |
| Details | varchar | NO |
| UnitID | varchar | YES |
| MfgOrderActualReleaseDate | varchar | YES |
| ProductionUnit | varchar | YES |
| Description | varchar | YES |
| Grade | varchar | YES |
| ProgressTonnage | decimal | YES |
| SerialNumber | int | YES |
| WorkOrderMoreDetails | varchar | YES |
| ColourCode | varchar | YES |
| RemainingTonnage | decimal | YES |
| Delete | varchar | NO |
| StatusColourCode | varchar | YES |
| ItemColourCode | varchar | YES |
| ListPageName | varchar | YES |
| ProgressPercentage | decimal | YES |
| CampaignId | varchar | YES |
| Campaign_Status | varchar | YES |
| IsDeleted | bit | YES |

## Sample rows (top 5, real live data)

| Edit | WorkOrderNumber | WorkOrderType | ID | BatchSchedule | MESWorkOrderNumber | CampaignNo | CreatedDate | ReleasedDate | Action | SalesOrder | ProductionPosting | CustomerName | Status | Equipment | ItemID | ParentID | ItemName | TotalQuantity | Unit | CutLengthMtr | CrossSectionmm | ProgressDurationinDays | Details | UnitID | MfgOrderActualReleaseDate | ProductionUnit | Description | Grade | ProgressTonnage | SerialNumber | WorkOrderMoreDetails | ColourCode | RemainingTonnage | Delete | StatusColourCode | ItemColourCode | ListPageName | ProgressPercentage | CampaignId | Campaign_Status | IsDeleted |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {"Link": "XBatch/ControlRoom/Page_Edit_XBatch_SAP_Work_Order_Mst_Tbl_RM","LinkTa | 120000154929 | LI01 | 058412B5-AABA-46A8-9257-60F1FD68D443 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/058412B |  |  | 2026-03-10 13:06:48.003000 |  | Completed |  | {"Link":"XBatch/ControlRoom/Page_List_LRF_Per_Heat_SAP?WOid=058412B5-AABA-46A8-9 |  | Completed | LRF | 74C3C03E-B548-4326-96E2-50A95D104D2E |  | SP3/PS_GLS | 700000.00 | ton |  |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F |  |  |  | 3SP/PS | 146.3200 | 2780 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | 699853.6800 | {"LvId": "1B2C77A3-1A0B-4C32-969F-AFADC091D441","RecordId" : "058412B5-AABA-46A8 | background-color:#1976d2; color:#ffffff | background-color:#563d7c; color:#f2f2f2 | Page_List_LRF_Per_Heat_SAP | 0.0209 |  |  | False |
| {"Link": "XBatch/ControlRoom/Page_Edit_XBatch_SAP_Work_Order_Mst_Tbl_RM","LinkTa | 140000000262 | SS02 | 1000F5E1-7393-40D5-9E45-AAA190CAF585 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1000F5E |  |  | 2026-04-02 09:59:03.590000 |  | OnHold |  | {"Link":"XBatch/ControlRoom/List_Page_CCM_Per_Heat_SAP?WOid=1000F5E1-7393-40D5-9 |  | OnHold | CCM | 7EAD0236-546E-4793-9454-FE721DFAACEC |  | BL_HHMNB500B_150X150 | 65000.00 | ton |  |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F |  |  |  | HHMNB500B | 4697.8500 | 2880 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | 60302.1500 | {"LvId": "1B2C77A3-1A0B-4C32-969F-AFADC091D441","RecordId" : "1000F5E1-7393-40D5 | background-color:#e53935; color:#ffffff | background-color:#563d7c; color:#f2f2f2 | List_Page_CCM_Per_Heat_SAP | 7.2275 |  |  | False |
| {"Link": "XBatch/ControlRoom/Page_Edit_XBatch_SAP_Work_Order_Mst_Tbl_RM","LinkTa | 120000102360 | BR01 | 180EACB3-BBC6-4DA8-AF75-21A68771A773 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/180EACB | CP3_21082026_RB25mm_WO_1 | CP3_21082026_RB25mm | 2026-08-21 15:52:07.357000 | 2026-08-21 15:52:07.357000 | OnHold |  | {"Link":"XBatch/ControlRoom/?WOid=180EACB3-BBC6-4DA8-AF75-21A68771A773", "LinkTa |  | OnHold | RM | E61A1D64-A311-4349-93F8-22F6313372E3 |  | RB_B500B_25.0DIA | 300.00 | MT | 8.5000 | 25.00 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 2095DF88-C3E3-4184-BA44-BBBB0696FF14 |  |  |  | B500B | 596.9380 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | -296.9380 | {"LvId": "1B2C77A3-1A0B-4C32-969F-AFADC091D441","RecordId" : "180EACB3-BBC6-4DA8 | background-color:#e53935; color:#ffffff | background-color:#563d7c; color:#f2f2f2 |  | 198.9793 | C3EB832C-E44D-4178-97CB-148B02262E15 | Running | False |
| {"Link": "XBatch/ControlRoom/Page_Edit_XBatch_SAP_Work_Order_Mst_Tbl_RM","LinkTa | 140000000228 | SS02 | 1A47B409-5542-4AB2-9EB5-6738BF235073 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1A47B40 |  |  | 2026-03-10 13:00:04.363000 |  | OnHold |  | {"Link":"XBatch/ControlRoom/List_Page_CCM_Per_Heat_SAP?WOid=1A47B409-5542-4AB2-9 |  | OnHold | CCM | 86346D18-CBF6-442E-A05F-0E9C7CB5D2D9 |  | BL_B500BLMNHC_150X150 | 300000.00 | ton |  |  |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F |  |  |  | B500BLMNHC | 80819.4700 | 2770 | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | 219180.5300 | {"LvId": "1B2C77A3-1A0B-4C32-969F-AFADC091D441","RecordId" : "1A47B409-5542-4AB2 | background-color:#e53935; color:#ffffff | background-color:#914e80; color:#ffffff | List_Page_CCM_Per_Heat_SAP | 26.9398 |  |  | False |
| {"Link": "XBatch/ControlRoom/Page_Edit_XBatch_SAP_Work_Order_Mst_Tbl_RM","LinkTa | 120000102356 | BR01 | 1D9B8320-D712-41EF-BDBE-3BC6EDE99C34 | {"Link":"/A0E0934F-B370-4374-819B-A60CF61E71AF/XBatch/BatchCreateControl/1D9B832 | CP3_21082026_RB25mm_WO_8 | CP3_21082026_RB25mm | 2026-08-21 15:52:07.613000 | 2026-08-21 15:52:07.613000 | RM ProductionOrder Created |  | {"Link":"XBatch/ControlRoom/?WOid=1D9B8320-D712-41EF-BDBE-3BC6EDE99C34", "LinkTa |  | RM ProductionOrder Created | RM | E61A1D64-A311-4349-93F8-22F6313372E3 |  | RB_B500B_25.0DIA | 150.00 | MT | 14.0000 | 25.00 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"AB525A23-E034-4FFB-84 | 2095DF88-C3E3-4184-BA44-BBBB0696FF14 |  |  |  | B500B | 0.0000 |  | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"0E6FCE0D-B435-4489-A8 |  | 150.0000 | {"LvId": "1B2C77A3-1A0B-4C32-969F-AFADC091D441","RecordId" : "1D9B8320-D712-41EF |  | background-color:#563d7c; color:#f2f2f2 |  | 0.0000 | C3EB832C-E44D-4178-97CB-148B02262E15 | Running | False |