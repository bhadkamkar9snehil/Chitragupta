# XStudio_Xbatch.dbo.XStudio_List_Billets_In_Yard_Vw

## Columns

| Column | Type | Nullable |
|---|---|---|
| Action | varchar | YES |
| Edit | varchar | NO |
| Grade | varchar | YES |
| MovementType | varchar | YES |
| ItemName | varchar | YES |
| ID | varchar | NO |
| HeatNo | varchar | YES |
| BilletNo | varchar | YES |
| UOM | varchar | YES |
| Quantity | decimal | NO |
| ReceivedDate | datetime | YES |
| MaterialGrade | varchar | YES |
| ToLocation | varchar | YES |
| Expired | bit | YES |
| ParentID | varchar | NO |
| UOMID | varchar | NO |
| Details | varchar | NO |
| ItemSource | varchar | YES |
| Delete | varchar | NO |
| dd | varchar | NO |
| CreatedOn | datetime | YES |

## Sample rows (top 5, real live data)

| Action | Edit | Grade | MovementType | ItemName | ID | HeatNo | BilletNo | UOM | Quantity | ReceivedDate | MaterialGrade | ToLocation | Expired | ParentID | UOMID | Details | ItemSource | Delete | dd | CreatedOn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TBD | {"Link": "XBatch/Inventory/Edit_Page_XBatch_Material_Inventory_Mst_Tbl","LinkTar | TBD |  | BL_HHMNB500B_150X150 | FE55BDAD-0C99-410E-885D-A0042FA010D3 | 1603853_12 |  | ton | 67.97 | 2026-07-01 11:03:21.383000 | HHMNB500B |  | False | 7EAD0236-546E-4793-9454-FE721DFAACEC | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"4882653D-4F2B-4E64-B9 | Produce | {"LvId": "64458497-AAF6-42ED-B3C6-52012613F29D","RecordId" : "FE55BDAD-0C99-410E | {"Link":"XBatch/ControlRoom/EDIT_Page_YMS_Shift_Update_Billet_Location", "LinkTa | 2026-07-01 11:03:21.383000 |
|  | {"Link": "XBatch/Inventory/Edit_Page_XBatch_Material_Inventory_Mst_Tbl","LinkTar |  |  | BL_B500BLMNHC_150X150 | FE4D29B8-A5A7-4A72-AB9D-747FD3BD360F | 1603998_06 |  | ton | 3.19 |  | B500BLMNHC |  |  | 86346D18-CBF6-442E-A05F-0E9C7CB5D2D9 | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"4882653D-4F2B-4E64-B9 |  | {"LvId": "64458497-AAF6-42ED-B3C6-52012613F29D","RecordId" : "FE4D29B8-A5A7-4A72 | {"Link":"XBatch/ControlRoom/EDIT_Page_YMS_Shift_Update_Billet_Location", "LinkTa | 2026-07-18 11:23:43.537000 |
| TBD | {"Link": "XBatch/Inventory/Edit_Page_XBatch_Material_Inventory_Mst_Tbl","LinkTar | TBD |  | BL_B500BLMNHC_150X150 | FE50319C-277D-4A7B-BC6C-767634BDDC86 | 1603821_12 |  | ton | 78.59 | 2026-06-29 15:39:32.893000 | B500BLMNHC |  | False | 86346D18-CBF6-442E-A05F-0E9C7CB5D2D9 | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"4882653D-4F2B-4E64-B9 | Produce | {"LvId": "64458497-AAF6-42ED-B3C6-52012613F29D","RecordId" : "FE50319C-277D-4A7B | {"Link":"XBatch/ControlRoom/EDIT_Page_YMS_Shift_Update_Billet_Location", "LinkTa | 2026-06-29 15:39:32.893000 |
| TBD | {"Link": "XBatch/Inventory/Edit_Page_XBatch_Material_Inventory_Mst_Tbl","LinkTar | TBD |  | BL_HHMNB500B_150X150 | FE3A465E-CB3E-43D1-A2C2-21816E994B3D | 1602800_12 |  | ton | 58.73 | 2026-05-04 08:54:22.743000 | HHMNB500B |  | False | 7EAD0236-546E-4793-9454-FE721DFAACEC | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"4882653D-4F2B-4E64-B9 | Produce | {"LvId": "64458497-AAF6-42ED-B3C6-52012613F29D","RecordId" : "FE3A465E-CB3E-43D1 | {"Link":"XBatch/ControlRoom/EDIT_Page_YMS_Shift_Update_Billet_Location", "LinkTa | 2026-05-04 08:54:22.743000 |
| TBD | {"Link": "XBatch/Inventory/Edit_Page_XBatch_Material_Inventory_Mst_Tbl","LinkTar | TBD |  | BL_B500BLMNHC_150X150 | FDB7361E-CE1E-4C25-8EF8-BD267E831E55 | 1603865_12 |  | ton | 78.59 | 2026-07-01 19:08:26.180000 | B500BLMNHC |  | False | 86346D18-CBF6-442E-A05F-0E9C7CB5D2D9 | 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F | {"SystemId":"A0E0934F-B370-4374-819B-A60CF61E71AF","LvId":"4882653D-4F2B-4E64-B9 | Produce | {"LvId": "64458497-AAF6-42ED-B3C6-52012613F29D","RecordId" : "FDB7361E-CE1E-4C25 | {"Link":"XBatch/ControlRoom/EDIT_Page_YMS_Shift_Update_Billet_Location", "LinkTa | 2026-07-01 19:08:26.180000 |