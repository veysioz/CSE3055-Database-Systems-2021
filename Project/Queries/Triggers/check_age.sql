Create Trigger check_age on Employee
for Insert
as
if (exists(Select * from inserted where age < 18))
Begin
	raiserror('can not hire under age of 18',1,1)
	rollback transaction
End