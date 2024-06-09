# item_id | name | price | count | category_id | detail | is_item_deleted
from tools import *
from prettytable import PrettyTable
from category import Category

class Item():
    def __init__(self, item_id, name, price, count, category_id, detail, is_item_deleted):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.count = count
        self.category_id = category_id
        self.detail = detail
        self.is_item_deleted = is_item_deleted

    def getId():
        with open("DB\\item_db\\id_last_item_created.txt","r") as file:
            lastBookId = file.read()
            if lastBookId != "":
                lastBookId = int(lastBookId) + 1
                return lastBookId
            else:
                return 1

    def UpdateLastId():
        with open("DB\\item_db\\lastItemId.txt","w") as file:
            file.write(str(Item.getId()))

    @classmethod
    def ItemMenu(cls):
        item_menu_flag = True
        while item_menu_flag:
            ClearTerminal()
            print(ColoredNotification("Item:", "red"))
            print(ColoredNotification("Add | Remove | Edit | Show | Search | Exit", "green"))
            answer = input(ColoredNotification("> ", "cyan")).lower()
            if answer == "add":
                cls.add_item()
            elif answer == "remove":
                cls.remove_item()
            elif answer == "edit":
                cls.edit_item()
            elif answer == "show":
                cls.show_item()
            elif answer == "search":
                cls.search_item_menu()
            elif answer == "exit":
                item_menu_flag = False
                break
            
    
    @classmethod
    def add_item(cls):
        ClearTerminal()
        flag = True
        while flag:
            item_id = Item.getId()
            name = input("item Name: ")
            price = float(input("item Price: "))
            count = int(input("item Count: "))

            select_categpry_result = Category.select_category()
            if select_categpry_result == False:
                break
            else:
                category_id = select_categpry_result

            detail = input("item Detail: ")
            is_item_deleted = 0
            selectedItem = cls(item_id,name,price,count,category_id,detail,is_item_deleted)
            with open("DB\\item_db\\item.txt", "a") as file:
                file.write(f'{selectedItem.__dict__}\n')

            Item.update_last_item_id()

            print(ColoredNotification("The item Added Successfuley", "green"))
            # Do admin wants to add more item?
            answer = input("Anything to Continue\n0 to EXIT\n> ")
            if answer == "0":
                flag = False
                break

    @classmethod      
    def remove_item(cls):
        items_list = cls.get_items_list()

        ClearTerminal()
        cls.show_item()
        item_id = input("Enter item ID to remove: ")
        for item in items_list:
            if item["item_id"] == int(item_id):
                item['is_item_deleted'] = 1
        cls.update_item_db(items_list)
                
    @classmethod
    def edit_item(cls):
        items_list = cls.get_items_list()
        ClearTerminal()
        cls.show_item()
        item_id = input("Enter item ID to edit: ")
        for item in items_list:
            if item["item_id"] == int(item_id):
                choice = cls.get_str_input("1. Edit Name\n2. Edit Price\n3. Edit Count\n4. Edit Category\n5. Edit Detail",['1','2','3','4','5']) # TODO: Must check a list of item names if available
                if choice == '1':
                    item['name'] = input("Enter new name: ")
                elif choice == '2':
                    item['price'] = cls.get_float_input("Enter new price: ")
                elif choice == '3':
                    item['count'] = cls.get_int_input("Enter new count: ") #TODO: havasam baiad bashe in n ham ghabol mikone va None mide
                elif choice == '4':
                    item['category_id'] = Category.select_category()
                elif choice == '5':
                    item['detail'] = input("Enter new detail: ")

                cls.update_item_db(items_list)

                
    
    @classmethod
    def show_item(cls):
        items_list = cls.get_items_list()
        ClearTerminal()
        print(ColoredNotification("All Items", "green"))
        
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price", "Count", "Category_id", "detail"]
        for item in items_list:
            if item['is_item_deleted'] == 0:
                table.add_row([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])
        print(table)
        Wait()

    def create_table_item(table_row_list: list):
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price", "Count", "Category_id", "detail"]
        for table_row in table_row_list:
            table.add_row([table_row[0], table_row[1], table_row[2], table_row[3], table_row[4], table_row[5]])
        print(table)
        Wait()
    
    @classmethod
    def search_items(cls, items_list, search_by=None, search_value=None, min_value=None, max_value=None, sort_by=None, ascending=False):
        table_row_list = []
        
        # Filtering based on search_by criteria
        if search_by == 'id':
            items_list = [item for item in items_list if item['item_id'] == search_value and item['is_item_deleted'] == 0]
        elif search_by == 'name':
            items_list = [item for item in items_list if item['name'] == search_value and item['is_item_deleted'] == 0]
        elif search_by == 'category':
            category_id = Category.category_name_to_id_convert(search_value)
            items_list = [item for item in items_list if item['category_id'] == category_id and item['is_item_deleted'] == 0]
        
        # Applying min_value and max_value filtering
        if min_value is not None:
            items_list = [item for item in items_list if item[sort_by] >= min_value]
        if max_value is not None:
            items_list = [item for item in items_list if item[sort_by] <= max_value]

        # Sorting the items
        if sort_by is not None:
            items_list.sort(key=lambda x: x[sort_by], reverse=not ascending)

        # Collecting the results
        for item in items_list:
            if item['is_item_deleted'] == 0:
                table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])

        cls.create_table_item(table_row_list)


    def get_float_input(prompt):
        while True:
            try:
                value = float(input(prompt).strip().lower())
                return value
            except ValueError:
                print("Please enter a valid integer.")

    #TODO: bayad ye get_int_input adi ham dorost konam
    def get_int_input(prompt):
        while True:
            try:
                value = input(prompt).strip().lower()
                if value == "n":
                    return None
                value = int(value)
                return value
            except ValueError:
                print("Please enter a valid integer.")

    def get_str_input_and_none(prompt, valid_options):
        while True:
            value = input(prompt).strip().lower()
            if value == "n":
                    return None
            if value in valid_options:
                return value
            else:
                print(f"Please enter one of the following: {', '.join(valid_options)}")

    @classmethod
    def get_str_input(cls, prompt, valid_options=None):
        while True:
            value = input(prompt).strip()
            if valid_options:
                if value.lower() in valid_options:
                    return value
                else:
                    print(f"Please enter one of the following: {', '.join(valid_options)}")
            else:
                return value
    @classmethod
    def get_str_input_and_none(cls, prompt, valid_options=None):
        while True:
            value = input(prompt).strip().lower()
            if value == 'n':
                return None
            elif valid_options:
                if value in valid_options:
                    return value
                else:
                    print(f"Please enter one of the following: {', '.join(valid_options)}")
            else:
                return value

    @classmethod
    def search_item_menu(cls):
        ClearTerminal()
        items_list = cls.get_items_list()

        print(ColoredNotification("Enter 'n' if you don't want to filter that attribute!!!", "red"))

        search_by = cls.get_str_input_and_none("Search By (id/name/category): ", ['id', 'name', 'category'])
        search_value = None
        if search_by == "id":
            search_value = cls.get_int_input("Item ID: ")
        elif search_by == 'name':
            search_value = cls.get_str_input("Item Name: ")  # TODO: Must check a list of item names if available
        elif search_by == 'category':
            search_value = cls.get_str_input("Item Category: ")  # TODO: Must check a list of categories if available

        sort_by = cls.get_str_input_and_none("Sort By (price/count): ", ['price', 'count'])
        sort_order = None
        if sort_by:
            sort_order = cls.get_str_input(f"Ascending or Descending on {sort_by.capitalize()}? (a/d): ", ['a', 'd'])
        
        if sort_by == "price":
            min_price = cls.get_int_input("MIN PRICE: ")
            max_price = cls.get_int_input("Max PRICE: ")
        else:
            min_count = cls.get_int_input("MIN Count: ")
            max_count = cls.get_int_input("Max Count: ")

        # Here you can use the consolidated search_items method based on the inputs
        cls.search_items(
            items_list,
            search_by=search_by,
            search_value=search_value,
            min_value=min_price if sort_by == 'price' else min_count,
            max_value=max_price if sort_by == 'price' else max_count,
            sort_by=sort_by,
            ascending=(sort_order == 'a') if sort_order else False
        )

    def get_items_list():
        items_list = []
        with open('DB\\item_db\\item.txt','r') as file:
            for line in file.readlines():
                items_list.append(eval(line))
            return items_list

    def update_last_item_id():
        with open("DB\\item_db\\id_last_item_created.txt","w") as file:
            file.write(str(Item.getId()))

    @classmethod
    def update_item_db(cls, items_list):
        with open('DB\\item_db\\item.txt', 'w') as file:
            for item in items_list:
                selectedItem = cls(item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail'], item['is_item_deleted'])
                file.write(f'{selectedItem.__dict__}\n')
