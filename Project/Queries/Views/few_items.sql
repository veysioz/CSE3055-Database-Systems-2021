Create View few_items as

Select stockNo, stockName
From Stock
Where stockAmount_kg < 10