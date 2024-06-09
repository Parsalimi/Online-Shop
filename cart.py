# cart_id | products | Total Price
from order import Order

class Cart(Order):
    def __init__(self, cart_id, products: list, total_price):
        super().__init__(cart_id, products, total_price)
        self.cart_id = cart_id
        self.products = products
        self.total_price = total_price
