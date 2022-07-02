Create View view_delivery as

Select transactionID as ID, customerFName +' '+ customerLName as Fullname
From FoodTransaction
Where deliveryStatus not like '%delivered%'