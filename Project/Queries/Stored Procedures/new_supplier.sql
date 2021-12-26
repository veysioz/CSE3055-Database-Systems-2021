Create Procedure new_supplier(	@supplierID			int,
								@supplierName		varchar(20),
								@supplierAddress	varchar(120))
as

Begin

	Insert Supplier(	supplierID,
						supplierName,
						supplierAddress)
	Values(	@supplierID,
			@supplierName,
			@supplierAddress)

End