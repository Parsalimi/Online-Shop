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
                cls.search_item()
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
            
    def remove_item():
        pass
    
    def edit_item():
        pass
    
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
            table.add_row([table_row['item_id'], table_row['name'], table_row['price'], table_row['count'], table_row['category_id'], table_row['detail']])
        print(table)
        Wait()
    
    @classmethod
    def search_item_by_id(cls, items_list, item_id:int):
        table_row_list = []
        for item in items_list:
            if item['item_id'] == item_id and item['is_item_deleted'] == 0:
                table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])
                break
        cls.create_table_item(table_row_list)

    @classmethod
    def search_item_by_name(cls, items_list, name):
        items_list = cls.get_items_list()
        table_row_list = []
        for item in items_list:
            if item['name'] == name and item['is_item_deleted'] == 0:
                table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])
                break
        cls.create_table_item(table_row_list)

    @classmethod
    def search_item_by_price(cls, items_list, min_price: float = None, max_price: float = None, ascending: bool = False):
        
        table_row_list = []

        # Apply filtering
        if min_price is not None:
            items_list = [item for item in items_list if item['price'] >= min_price]
        if max_price is not None:
            items_list = [item for item in items_list if item['price'] <= max_price]
        
        # Sort the items based on price
        items_list.sort(key=lambda x: x['price'], reverse=not ascending)
        
        for item in items_list:
            if item['is_item_deleted'] == 0:
                table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])

        cls.create_table_item(table_row_list)

    @classmethod
    def search_item_by_count(cls, items_list, min_count: float = None, max_count: float = None, ascending: bool = False):
        
        table_row_list = []

        # Apply filtering
        if min_count is not None:
            items_list = [item for item in items_list if item['count'] >= min_count]
        if max_count is not None:
            items_list = [item for item in items_list if item['count'] <= max_count]
        
        # Sort the items based on price
        items_list.sort(key=lambda x: x['count'], reverse=not ascending)
        
        for item in items_list:
            if item['is_item_deleted'] == 0:
                table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])

        cls.create_table_item(table_row_list)


    @classmethod
    def search_item_by_name(cls, items_list, category_name):
        
        table_row_list = []

        for item in items_list:
            if item['category_id'] == Category.category_name_to_id_convert(category_name):
                if item['is_item_deleted'] == 0:
                    table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail']])

        cls.create_table_item(table_row_list)


    @classmethod
    def search_item(cls):
        items_list = cls.get_items_list()

        flag = True
        while flag:
            ClearTerminal()
            print(ColoredNotification("Search with ...", "green"))
            answer = input("(0 to exit)\n1. ID\n2. Name\n3. Price\n4. Remain Count\n5. Category Name\n >")
            if answer == "0":
                break
            
            elif answer == "1":
                inner_flag = True
                while inner_flag:
                    ClearTerminal()
                    item_id = int(input("(0 to exit)\nEnter ID that you're looking for: "))
                    if item_id == 0:
                        break
                    else:
                        cls.search_item_by_id(items_list, item_id)

            elif answer == "2":
                inner_flag = True
                while inner_flag:
                    ClearTerminal()
                    item_name = int(input("(0 to exit)\nEnter Name that you're looking for: "))
                    if item_name == 0:
                        break
                    else:
                        cls.search_item_by_name(items_list, item_name)

            elif answer == "3":
                inner_flag = True
                while inner_flag:
                    ClearTerminal()
                    max_price = int(input("(0 to exit)\nEnter MAX PRICE that you're looking for: "))
                    min_price = int(input("Enter MIN PRICE that you're looking for: "))
                    ascending = input("Do you want to sort it Ascending or Descending? (a/d): ")
                    if ascending == "a":
                        ascending = True
                    elif ascending == "d":
                        ascending = False

                    if max_price == 0:
                        break
                    else:
                        cls.search_item_by_price(items_list,min_price,max_price,ascending)

            elif answer == "4":
                inner_flag = True
                while inner_flag:
                    ClearTerminal()
                    max_price = int(input("(0 to exit)\nEnter MAX Count that you're looking for: "))
                    min_price = int(input("Enter MIN PRICE that you're looking for: "))
                    ascending = input("Do you want to sort it Ascending or Descending? (a/d): ")
                    if ascending == "a":
                        ascending = True
                    elif ascending == "d":
                        ascending = False

                    if max_price == 0:
                        break
                    else:
                        cls.search_item_by_price(items_list,min_price,max_price,ascending)

            elif answer == "5":
                pass
            else:
                print(ColoredNotification("Invalid Option", "red"))

    def get_items_list():
        items_list = []
        with open('DB\\item_db\\item.txt','r') as file:
            for line in file.readlines():
                items_list.append(eval(line))
            return items_list

    def update_last_item_id():
        with open("DB\\item_db\\id_last_item_created.txt","w") as file:
            file.write(str(Item.getId()))
            
    def update_item_list():
        Item.items_list = []
        with open("DB\\item_db\\item.txt", "r") as file:
            for line in file.readlines():
                Item.items_list.append(eval(line))

