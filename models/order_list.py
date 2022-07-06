from models.order import Order

order_1 = Order('PEP121', 'Peppino', '06/07/2022', 'The wonderful thing', 1, "http://127.0.0.1:5000/orders/0")
order_2 = Order('NAT122', 'Nathan', '05/07/2022', 'The wonderful thing II', 2, "http://127.0.0.1:5000/orders/1")
order_3 = Order('JCK123', 'Jack', '06/07/2022', 'The wonderful thing - Origins', 1, "http://127.0.0.1:5000/orders/2") 

book_orders = [order_1, order_2, order_3]