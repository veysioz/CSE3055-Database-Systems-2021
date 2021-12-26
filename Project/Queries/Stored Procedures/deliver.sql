Create Procedure delivered(	@transactionID	int)
as

Begin
	
	Update	FoodTransaction
	Set		deliveryStatus = 'delivered', deliveryDate = GetDate()
	Where	@transactionID = transactionID

End