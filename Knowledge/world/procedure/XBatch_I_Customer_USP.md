---
type: procedure
title: "XBatch_I_Customer_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Customer_USP

Parameters: @Name varchar, @Address varchar, @City varchar, @State varchar, @County varchar, @ZipCode int, @ContactNumber1 varchar, @ContactNumber2 varchar, @EmailAddress1 varchar, @EmailAddress2 varchar, @Description varchar, @userID varchar.

## Writes

- XBatch_Customer_Mst_Tbl: Address, City, ContactNumber1, ContactNumber2, County, CreatedBy, CreatedOn, Description, EmailAddress1, EmailAddress2, ID, Name, Source, State, ZipCode
