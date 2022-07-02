Create Procedure new_delivery(	@transactionID	int,
								@orderID		int,
								@customerFName	varchar(25),
								@customerLName	varchar(25))
as

Begin
	
	Insert Into FoodTransaction(	transactionID,
									orderID,
									customerFName,
									customerLName,
									deliveryStatus,
									deliveryDate)
	Values(	@transactionID,
			@orderID,
			@customerFName,
			@customerLName,
			'getting ready',
			NULL)

End