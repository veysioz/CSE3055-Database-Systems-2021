Create Procedure new_booking(	@bookingID		smallint,
								@personAmount	smallint,
								@tableID		smallint)
as

Begin

	Insert Into Booking(	bookingID,
							bookingDate,
							personAmount,
							tableID)
	Values(	@bookingID,
			GETDATE(),
			@personAmount,
			@tableID)

End