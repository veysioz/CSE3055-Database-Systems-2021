Create View view_todays_bill as

Select Sum(totalAmount) as Amount
From Bill
Where billDate = cast(GETDATE() as date)