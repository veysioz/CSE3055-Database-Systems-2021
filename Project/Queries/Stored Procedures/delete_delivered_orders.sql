Create Procedure delete_delivered_orders
as

Begin

	Delete From FoodTransaction
	Where deliveryStatus='delivered'

End