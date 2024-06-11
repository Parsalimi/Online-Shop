class ProductSet():
    def __init__(self, product_set_id, name, price, count):
        self.product_set_id = product_set_id
        self.name = name
        self.price = price
        self.count = count

    @classmethod
    def create_new_product_set(cls,item_name, item_price, item_count):
        product_set_id = cls.getId()

        selectedCart = cls(product_set_id, item_name, item_price, item_count)
        with open("DB\\product_set_db\\product_set.txt", "a") as file:
            file.write(f'{selectedCart.__dict__}\n')

        cls.update_last_product_set_id(product_set_id)

        return product_set_id # return id of created product set
    
    @staticmethod
    def getId():
        with open("DB\\product_set_db\\id_last_ps_created.txt","r") as file:
            last_product_set_id = file.read()
            if last_product_set_id != "":
                last_product_set_id = int(last_product_set_id) + 1
                return last_product_set_id
            else:
                return 1
            
    def update_last_product_set_id(new_product_set_id):
        with open("DB\\product_set_db\\id_last_ps_created.txt","w") as file:
            file.write(str(new_product_set_id))