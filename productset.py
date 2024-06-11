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

    @classmethod
    def check_if_item_name_exists_in_product_set(cls, product_set_id, item_name):
        product_set_list = cls.get_carts_list()

        for prodcut_set in product_set_list:
            if product_set_id == prodcut_set['product_set_id']:
                if item_name == prodcut_set['name']:
                    return True
            
        return False
    
    def get_carts_list():
        product_set_list = []
        with open('DB\\product_set_db\\product_set.txt','r') as file:
            for line in file.readlines():
                product_set_list.append(eval(line))
            return product_set_list