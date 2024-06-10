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
            last_item_id = file.read()
            if last_item_id != "":
                last_item_id = int(last_item_id) + 1
                return last_item_id
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

            Item.update_last_item_id(item_id)

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
        item_id = get_input(1, "(0 to exit)\nEnter item ID to edit: ",return_none_on='0',valid_options=cls.available_item_id())
        if item_id:
            for item in items_list:
                if item["item_id"] == item_id:
                    ClearTerminal()
                    choice = get_input(3,"1. Edit Name\n2. Edit Price\n3. Edit Count\n4. Edit Category\n5. Edit Detail\n> ",valid_options=['1','2','3','4','5'])
                    if choice == '1':
                        item['name'] = get_input(3, "Enter new name: ")
                    elif choice == '2':
                        item['price'] = get_input(2, "Enter new price: ")
                    elif choice == '3':
                        item['count'] = get_input(1, "Enter new count: ")
                    elif choice == '4':
                        item['category_id'] = Category.select_category()
                    elif choice == '5':
                        item['detail'] = get_input(3,"Enter new detail: ")

                    cls.update_item_db(items_list)
                    break

                
    
    @classmethod
    def show_item(cls):
        items_list = cls.get_items_list()
        ClearTerminal()
        print(ColoredNotification("All Items", "green"))
        
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price", "Count", "Category_id", "detail"]
        for item in items_list:
            if item['is_item_deleted'] == 0:
                table.add_row([item['item_id'], item['name'], item['price'], item['count'], Category.category_id_to_name(item['category_id']), item['detail']])
        print(table)
        Wait()

    def create_table_item(table_row_list: list):
        ClearTerminal()
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price", "Count", "Category_id", "detail"]
        for table_row in table_row_list:
            table.add_row([table_row[0], table_row[1], table_row[2], table_row[3], table_row[4], table_row[5]])
        print(table)
        Wait()
    
    @classmethod
    def search_items(cls, items_list, search_by=None, search_value=None, min_count:int=None, max_count:int=None, 
                     min_price:int=None, max_price:int=None,sort_by=None, ascending=True):
        
        only_one_result = False
        table_row_list = []

        # Filtering items based on search criteria
        if search_by:
            if search_by == 'id':
                for item in items_list:
                    if item['item_id'] == search_value and item['is_item_deleted'] == 0:
                        table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])
                        only_one_result = True
                        break

            elif search_by == 'name':
                for item in items_list:
                    item_name = str(item['name'])
                    item_name = item_name.lower()
                    if item_name == search_value and item['is_item_deleted'] == 0:
                        table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])
                        only_one_result = True
                        break
                    
            elif search_by == 'category':
                for item in items_list:
                    if item['category_id'] == search_value and item['is_item_deleted'] == 0:
                        table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])

            else:
                for item in items_list:
                    if item['is_item_deleted'] == 0:
                        table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])

        if only_one_result == False:
            # Filter Price
            if min_price is not None:
                for index, item in enumerate(table_row_list):
                    if item[2] < min_price:
                        table_row_list.pop(index)
            
            if max_price is not None:
                for index, item in enumerate(table_row_list):
                    if item[2] > max_price:
                        table_row_list.pop(index)

            # Filter Count
            if min_count is not None:
                for index, item in enumerate(table_row_list):
                    if item[3] < min_count:
                        table_row_list.pop(index)
            
            if max_count is not None:
                for index, item in enumerate(table_row_list):
                    if item[3] > max_count:
                        table_row_list.pop(index)



            # Sorting the items
            if sort_by is not None:
                if sort_by == 'price':
                    table_row_list = sort_list(table_row_list,2,ascending)
                else:
                    table_row_list = sort_list(table_row_list,3,ascending)

        cls.create_table_item(table_row_list)

    @classmethod
    def search_item_menu(cls):
        ClearTerminal()
        items_list = cls.get_items_list()
        only_one_result = False
        print(ColoredNotification("Enter 'n' if you don't want to filter that attribute!!!", "red"))

        search_by = get_input(3, "Search By (id/name/category): ", ['id', 'name', 'category'], 'n')
        search_value = None
        if search_by == "id":
            search_value = get_input(1, "Item ID: ", return_none_on='n')
            only_one_result = True
        elif search_by == 'name':
            search_value = get_input(3, "Item Name: ", valid_options=cls.available_item_id(), return_none_on='n')
            only_one_result = True
        elif search_by == 'category':
            ClearTerminal()
            search_value = get_input(1, "Item Category (ID): ", valid_options=Category.available_category_id(), return_none_on='n')

        sort_by, sort_by, min_price, max_price, min_count, max_count = None,None,None,None,None,None
        if only_one_result == False:
            sort_by = get_input(3, "Sort By (price/count): ", ['price', 'count'], return_none_on='n')
            sort_order = None
            if sort_by:
                sort_order = get_input(3, f"Ascending or Descending on {sort_by}? (a/d): ", ['a', 'd'], return_none_on='n')
            else:
                sort_order = None

            min_price = get_input(2, "MIN PRICE: ", return_none_on='n')
            max_price = get_input(2, "MAX PRICE: ", return_none_on='n')
            min_count = get_input(2, "MIN COUNT: ", return_none_on='n')
            max_count = get_input(2, "MAX COUNT: ", return_none_on='n')

        # Use the consolidated search_items method based on the inputs
        cls.search_items(
            items_list,
            search_by=search_by,
            search_value=search_value,
            min_count=min_count,
            max_count=max_count,
            min_price=min_price,
            max_price=max_price,
            sort_by=sort_by
        )

    def get_items_list():
        items_list = []
        with open('DB\\item_db\\item.txt','r') as file:
            for line in file.readlines():
                items_list.append(eval(line))
            return items_list

    def update_last_item_id(item_id):
        with open("DB\\item_db\\id_last_item_created.txt","w") as file:
            file.write(str(item_id))

    @classmethod
    def update_item_db(cls, items_list):
        with open('DB\\item_db\\item.txt', 'w') as file:
            for item in items_list:
                selectedItem = cls(item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail'], item['is_item_deleted'])
                file.write(f'{selectedItem.__dict__}\n')

    @classmethod
    def available_item_id(cls):
        available_id_list = []
        items_list = cls.get_items_list()
        for item in items_list:
            if item['is_item_deleted'] == 0:
                available_id_list.append(int(item['item_id']))

        return available_id_list
