# order_id | products_set_id | Total Price | payment_id
class Order:
    def __init__(self, order_id, products_set_id: list, total_price, payment_id):
        self.order_id = order_id
        self.products_set_id = products_set_id
        self.total_price = total_price
        self.payment_id = payment_id
