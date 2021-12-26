Create Procedure todays_bill
as

Begin
	Select Sum(totalAmount) as Amount
	From Bill
	Where billDate = cast(GETDATE() as date)
End