Create Procedure update_item_price(	@itemID			int,
									@new_item_price	int)
as

Begin
	
	Update	Item
	Set		itemPrice = @new_item_price
	Where	itemID = @itemID

End