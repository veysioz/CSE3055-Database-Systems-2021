Create Procedure update_salary(	@employeeID	int,
								@new_salary	int)
as

Begin
	
	Update	Employee
	Set		salary = @new_salary
	Where	employeeID = @employeeID

End