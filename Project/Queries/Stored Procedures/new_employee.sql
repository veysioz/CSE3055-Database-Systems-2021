Create Procedure new_employee(	@employeeID		int,
								@positionID		int,
								@firstName		varchar(20),
								@lastName		varchar(20),
								@birthDate		date,
								@age			smallint,
								@EmployeeAddr	varchar(120),
								@salary			int)
as

Begin

	Insert Into Employee(	employeeID,
							positionID,
							firstName,
							lastName,
							birthDate,
							age,
							EmployeeAddr,
							salary)
	Values(	@employeeID,
			@positionID,
			@firstName,
			@lastName,
			@birthDate,
			@age,
			@EmployeeAddr,
			@salary)

End