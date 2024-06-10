# order_id | products | Total Price
class Order:
    def __init__(self, order_id, products: list, total_price, payment_id):
        self.order_id = order_id
        self.products = products
        self.total_price = total_price
        self.payment_id = payment_id
