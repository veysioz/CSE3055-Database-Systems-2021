Create Procedure new_order (@itemID int,
							@orderID int)
as

Begin
	Insert into ItemOrder
				(itemID,
				orderID)
	Values(	@itemID,
			@orderID)
End