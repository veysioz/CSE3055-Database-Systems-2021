Create Procedure delivery_ontheway(	@transactionID	int)
as

Begin
	
	Update	FoodTransaction
	Set		deliveryStatus = 'on the way'
	Where	@transactionID = transactionID

End