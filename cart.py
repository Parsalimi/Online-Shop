# cart_id | products_set_id | Total Price
from productset import ProductSet
from tools import *
from payment import Payment
from order import Order

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

    @classmethod
    def add_item_to_user_cart(cls, user_cart_id, item_name, item_price, item_count):
        carts_list = cls.get_carts_list()
        for cart in carts_list:
            if cart['cart_id'] == user_cart_id:
                cart['products_set_id'].append(ProductSet.create_new_product_set(item_name, item_price, item_count))
                cart['total_price'] += item_price * item_count
        
        cls.update_cart_db(carts_list)
    
    def get_carts_list():
        carts_list = []
        with open('DB\\cart_db\\cart.txt','r') as file:
            for line in file.readlines():
                carts_list.append(eval(line))
            return carts_list
        
    @classmethod
    def update_cart_db(cls, carts_list):
        with open('DB\\cart_db\\cart.txt', 'w') as file:
            for cart in carts_list:
                selectedCart = cls(cart['cart_id'],cart['products_set_id'],cart['total_price'])
                file.write(f'{selectedCart.__dict__}\n')

    @classmethod
    def count_items_in_cart(cls, user_cart_id):
        carts_list = cls.get_carts_list()
        for cart in carts_list:
            if cart['cart_id'] == user_cart_id:
                item_count_in_cart = len(cart['products_set_id'])
        return item_count_in_cart
    
    @classmethod
    def check_is_item_id_exists_in_cart(cls, user_cart_id, item_name):
        carts_list = cls.get_carts_list()
        for cart in carts_list:
            if user_cart_id == cart['cart_id']:
                for products_set_id in cart['products_set_id']:
                    if ProductSet.check_if_item_name_exists_in_product_set(products_set_id, item_name):
                        return True
                    
        return False
    
    @classmethod
    def show_cart(cls, kind:int,cart_id):
        carts_list = cls.get_carts_list()
        ClearTerminal()
        
        for cart in carts_list:
            if cart_id == cart['cart_id']:
                if len(cart['products_set_id']) > 0:
                    print(f"Cart ID: {cart['cart_id']}\nFinal Price: {cart['total_price']}")
                    if kind == 1:
                        ProductSet.show_product_set(1, cart['products_set_id'])
                    else:
                        ProductSet.show_product_set(2, cart['products_set_id'])
                    Wait()
                    break
                else:
                    print(ColoredNotification("Cart is empty!!!","red"))
                    Wait()
                    break
        
    @classmethod
    def remove_product_from_cart(cls, cart_id):
        carts_list = cls.get_carts_list()
        ClearTerminal()
        for cart in carts_list:
            if cart_id == cart['cart_id']:
                if len(cart['products_set_id']) > 0:
                    cls.show_cart(2, cart_id)
                    product_set_id = get_input(1,"Item ID: ", valid_options=cart['products_set_id'])
                    cart['products_set_id'].remove(product_set_id)

                    cost_free = ProductSet.remove_product_set(product_set_id)
                    cart['total_price'] -= cost_free

                    cls.update_cart_db(carts_list)

                    break
                else:
                    print(ColoredNotification("Cart is empty!!!","red"))
                    Wait()
                    break

    @classmethod
    def edit_product_of_cart(cls,cart_id):
        carts_list = cls.get_carts_list()
        ClearTerminal()
        for cart in carts_list:
            if cart_id == cart['cart_id']:
                if len(cart['products_set_id']) > 0:
                    cls.show_cart(2, cart_id)
                    product_set_id = get_input(1,"Item ID to Edit: ", valid_options=cart['products_set_id'])

                    cost_free = ProductSet.edit_product_set(product_set_id)
                    cart['total_price'] += cost_free

                    cls.update_cart_db(carts_list)
                else:
                    print(ColoredNotification("Cart is empty!!!","red"))
                    Wait()
                    break

    @classmethod 
    def cart_checkout(cls,cart_id):
        ClearTerminal()
        carts_list = cls.get_carts_list()
        for cart in carts_list:
            if cart_id == cart['cart_id']:
                if len(cart['products_set_id']) > 0:
                    cls.show_cart(1, cart_id)
                    choice = get_input(3, f"Cart ID: {cart['cart_id']}\nFinal Price: {cart['total_price']}\n\nWould you like to proceed to checkout? ('y' to Proceed)\n> ")
                    if choice == 'y':
                        #card_num = get_input(5,"Please enter your credit card number: ")
                        payment_id = Payment.create_new_payment(cart['total_price'])
                        order_id = Order.create_new_order(cart['products_set_id'],cart['total_price'],payment_id)
                        ProductSet.update_items_list_after_check_out(cart['products_set_id'])
                        cls.update_user_after_checkout(order_id, cart_id)
                        print(ColoredNotification("The checkout process was successful!!!","green"))
                        Wait()
                        break

                else:
                    print(ColoredNotification("Cart is empty!!!","red"))
                    Wait()
                    break
                

    @classmethod
    def update_user_after_checkout(cls,order_id, cart_id): # Add new order_id to order_ids & Give user a new cart ID
        users_list = cls.get_users_list()
        
        for user in users_list:
            if user['cart_id'] == cart_id:
                user['cart_id'] = Cart.create_new_cart()
                user['order_ids'].append(order_id)


        cls.update_user_db(users_list)

    # COPYING FROM USER - THEY'RE NOT RELATED TO Product Set
    @classmethod
    def update_user_db(cls, users_list):
        with open('DB\\user_db\\users.txt', 'w') as file:
            for user in users_list:
                selectedUser = {'user_id': user['user_id'], 
                                'username': user['username'], 
                                'password': user['password'], 
                                'fname': user['fname'], 
                                'lname': user['lname'], 
                                'age': user['age'], 
                                'phone': user['phone'], 
                                'role': user['role'], 
                                'order_ids': user['order_ids'], 
                                'cart_id': user['cart_id']}
                
                file.write(f'{selectedUser}\n')

    def get_users_list():
        users_list = []
        with open('DB\\user_db\\users.txt','r') as file:
            for line in file.readlines():
                users_list.append(eval(line))
            return users_list