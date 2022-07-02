Create Procedure total_salary
as
Begin
	
	Select Sum(salary) as Total_Salary
	From Employee

End

