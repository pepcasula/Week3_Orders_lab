from datetime import date
from unicodedata import name


class Order:

    def __init__(self, cust_id, customer_name, order_date, product_name, quantity, link):
        self.customer_name = customer_name
        self.cust_id = cust_id
        self.order_date = order_date
        self.product_name = product_name
        self.quantity = quantity
        self.link = link
        