Create Trigger check_table on Booking 
for Insert
as

if(exists(	Select i.tableID, b.tableID 
			From inserted i, Booking b 
			Where i.tableID = b.tableID and 
			i.bookingDate != b.bookingDate))
Begin
	raiserror('table already booked',1,1)
	rollback transaction
End