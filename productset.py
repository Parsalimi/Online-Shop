from prettytable import PrettyTable

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
        
    @classmethod
    def show_product_set(cls, kind:int, product_set_ids:list):
        table = PrettyTable()
        product_set_list = ProductSet.get_carts_list()

        if kind == 1: # name | count | Price | Total
            table.field_names = ["Name", "Count", "Price", "Total"]
            for product_set in product_set_list:
                if product_set['product_set_id'] in product_set_ids:
                    table.add_row([product_set['name'],product_set['count'],product_set['price'],product_set['count']*product_set['price']])
        else: # ID | name | count | Price | Total
            table.field_names = ["ID","Name", "Count", "Price", "Total"]
            for product_set in product_set_list:
                if product_set['product_set_id'] in product_set_ids:
                    table.add_row([product_set['product_set_id'],product_set['name'],product_set['count'],product_set['price'],product_set['count']*product_set['price']])

        print(table)

    @classmethod
    def remove_product_set(cls, product_set_id):
        cost_free = 0

        product_set_list = ProductSet.get_carts_list()
        for index, product_set in enumerate(product_set_list):
            if product_set['product_set_id'] == product_set_id:
                product_set_list.pop(index)
                cost_free = product_set['price']*product_set['count']

        cls.update_product_set_db(product_set_list)

        return cost_free

    @classmethod
    def update_product_set_db(cls, product_set_list):
        with open('DB\\product_set_db\\product_set.txt', 'w') as file:
            for product in product_set_list:
                selectedProductSet = cls(product['product_set_id'],product['name'],product['price'],product['count'])
                file.write(f'{selectedProductSet.__dict__}\n')