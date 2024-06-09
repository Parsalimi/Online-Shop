# order_id | products | Total Price

class Order:
    def __init__(self, order_id, products: list, total_price):
        self.order_id = order_id
        self.products = products
        self.total_price = total_price
