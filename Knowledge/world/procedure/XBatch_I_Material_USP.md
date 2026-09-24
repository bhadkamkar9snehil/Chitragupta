---
type: procedure
title: "XBatch_I_Material_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Material_USP

Parameters: @Name varchar, @Type varchar, @Unit varchar, @Number varchar, @Stocktype varchar, @Quantity decimal, @Description varchar, @IsEnabled bit, @CanExpire bit, @ExpireDays int, @MinInventorylevel decimal, @MaxOrderSize decimal, @LotNumberFormat varchar, @SubLotNumberFormat varchar, @UserID varchar.

## Writes

- XBatch_Material_Mst_Tbl: CanExpire, CreatedBy, CreatedOn, Description, ExpireDays, ID, IsDeleted, IsEnabled, IsSystem, LotNumberFormat, MaxOrderSize, MinInventoryLevel, Name, Number, Quantity, Source, StockType, SubLotNumberFormat, TypeID, UnitID

## Reads

- XBatch_Material_Type_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
