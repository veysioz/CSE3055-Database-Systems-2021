Create Procedure delete_employee(	@employeeID	int)
as

Begin

	Delete From Employee
	Where employeeID=@employeeID
	Delete From EmployeePhoneNumber
	Where employeeID=@employeeID

End