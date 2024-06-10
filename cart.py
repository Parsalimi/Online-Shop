# cart_id | products_set_id | Total Price

class Cart:
    def __init__(self, cart_id, products_set_id: list, total_price):
        self.cart_id = cart_id
        self.products_set_id = products_set_id
        self.total_price = total_price

    def getId():
        with open("DB\\cart_db\\id_last_cart_created.txt","r") as file:
            last_categry_Id = file.read()
            if last_categry_Id != "":
                last_categry_Id = int(last_categry_Id) + 1
                return last_categry_Id
            else:
                return 1
            
    def create_new_cart():
        cart_id = Cart.getId()
        products_set_id = []
        total_price = 0
        selectedCart = Cart(cart_id, products_set_id, total_price)
        with open("DB\\cart_db\\cart.txt", "a") as file:
            file.write(f'{selectedCart.__dict__}\n')

        Cart.update_last_cart_id(cart_id)

        return cart_id

    def update_last_cart_id(new_cart_id):
        with open("DB\\cart_db\\id_last_cart_created.txt","w") as file:
            file.write(str(new_cart_id))