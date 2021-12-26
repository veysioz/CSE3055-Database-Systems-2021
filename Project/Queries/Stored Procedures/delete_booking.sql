Create Procedure delete_booking(	@bookingID	smallint)
as

Begin
	
	Delete From Booking
	Where bookingID = @bookingID

End