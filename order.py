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