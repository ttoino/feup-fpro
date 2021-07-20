# 3. Process orders

Consider sales records, given as a nested list with each invoice, of a sale, in the format *(order number, book title and author, quantity, price per item)*.


Write a Python function `invoice_totals(orders, min)` which returns a list with 2-tuples. Each tuple consists of the order number and the total (the product of the price per item by the quantity). The total should be increased by 10€ if the value of the order is smaller than the `min` value.


You must use a lambda function and the function `map()`.



## Private Tests [100%]

## Public Tests [100%]
