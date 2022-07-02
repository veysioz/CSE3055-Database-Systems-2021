Create Procedure delete_customer(	@customerID	int)
as

Begin

	Delete From Customer
	Where customerID=@customerID
	Delete From Customer_Phone_Num
	Where customerID=@customerID

End