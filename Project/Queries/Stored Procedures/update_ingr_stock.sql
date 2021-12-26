Create Procedure update_ingr_stock(	@stock_no			int,
									@new_stock_amount	int)
as

Begin
	
	Update	Stock
	Set		stockAmount_kg = @new_stock_amount
	Where	stockNo = @stock_no

End