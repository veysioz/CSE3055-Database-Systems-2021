Create Procedure new_customer (	@customerID			int,
								@firstName			varchar(30),
								@lastName			varchar(30),
								@customerAddress	varchar(120))
As

Begin
	
	SET IDENTITY_INSERT Customer ON

	Insert Into Customer (	customerID,
							firstName,
							lastName,
							customerAddress)
	Values(	@customerID,
			@firstName,
			@lastName,
			@customerAddress)
			
	SET IDENTITY_INSERT Customer OFF

End
