Create View near_customer as

Select customerID, firstName, lastName, customerAddress
From Customer
Where customerAddress like '%istanbul%'