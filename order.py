from prettytable import PrettyTable
from tools import *
from productset import ProductSet
from payment import Payment

# order_id | products_set_id | Total Price | payment_id
class Order:
    def __init__(self, order_id, products_set_id: list, total_price, payment_id):
        self.order_id = order_id
        self.products_set_id = products_set_id
        self.total_price = total_price
        self.payment_id = payment_id

    @classmethod
    def create_new_order(cls,products_set_id,total_price,payment_id):
        order_id = cls.getId()
        selectedorder = cls(order_id, products_set_id, total_price, payment_id)
        with open("DB\\order_db\\order.txt", "a") as file:
            file.write(f'{selectedorder.__dict__}\n')

        cls.update_last_order_id(order_id)

        return order_id # return id of created order
    
    @staticmethod
    def getId():
        with open("DB\\order_db\\id_last_order_created.txt","r") as file:
            last_order_id = file.read()
            if last_order_id != "":
                last_order_id = int(last_order_id) + 1
                return last_order_id
            else:
                return 1
            
    def update_last_order_id(new_order_id):
        with open("DB\\order_db\\id_last_order_created.txt","w") as file:
            file.write(str(new_order_id))

    def get_orders_list():
        orders_list = []
        with open('DB\\order_db\\order.txt','r') as file:
            for line in file.readlines():
                orders_list.append(eval(line))
            return orders_list
        
    @classmethod
    def show_user_orders(cls,order_ids):
        ClearTerminal()
        orders_list = cls.get_orders_list()
        for order in orders_list:
            if order['order_id'] in order_ids:
                table = PrettyTable()
                table.field_names = ["Order ID", "Product Set", "Total Price", "Payment ID"]

                print(ColoredNotification(f"Order ID: {order['order_id']}\nTotal Price: {order['total_price']}","cyan"))
                Payment.report_of_payment(order['payment_id'])
                ProductSet.show_product_set(1,order['products_set_id'])
                print(ColoredNotification('---------------------------------------',"cyan"))