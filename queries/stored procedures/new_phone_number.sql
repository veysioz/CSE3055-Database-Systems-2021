Create Procedure new_customer_phone_num (	@customerID			int,
											@phoneNumber		char(15))
As

Begin
	
	Insert Into Customer_Phone_Num(	customerID,
									phoneNumber)
	Values(	@customerID,
			@phoneNumber)			

End