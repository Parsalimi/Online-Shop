# cart_id | products | Total Price

class Cart:
    def __init__(self, cart_id, products: list, total_price):
        self.cart_id = cart_id
        self.products = products
        self.total_price = total_price
