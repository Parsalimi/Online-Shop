# item_id | name | price | count | category_id | detail | min_age | is_item_deleted
from tools import *
from prettytable import PrettyTable
from category import Category
from cart import Cart

class Item():
    def __init__(self, item_id, name, price, count, category_id, detail, min_age, is_item_deleted):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.count = count
        self.category_id = category_id
        self.detail = detail
        self.min_age = min_age
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
                cls.admin_search_item_menu()
            elif answer == "exit":
                item_menu_flag = False
                break
            
    
    @classmethod
    def add_item(cls):
        items_list = cls.get_items_list()
        ClearTerminal()
        flag = True
        while flag:
            item_id = Item.getId()

            notcheck = True
            while notcheck:
                tagged = False
                name = get_input(3, "item Name: ")
                # Check if that item name exists
                for item in items_list:
                    if item['name'].lower() == name:
                        print(ColoredNotification("That item name is already EXISTS!!!", "red"))
                        Wait()
                        ClearTerminal()
                        tagged = True
            
                if tagged == False:
                    notcheck = False
            
            price = get_input(2,"item Price: ")
            count = get_input(1,"item Count: ")

            select_categpry_result = Category.select_category()
            if select_categpry_result == False:
                break
            else:
                category_id = select_categpry_result

            detail = input("item Detail: ")

            notcheck = True
            while notcheck:
                min_age = get_input(1,"Minimum Age: ")
                if min_age < 0 or min_age > 120:
                    print(ColoredNotification("Invalid Age!!!", "red"))
                    Wait()
                    ClearTerminal()
                else:
                    notcheck = False

            is_item_deleted = 0
            selectedItem = cls(item_id,name,price,count,category_id,detail,min_age,is_item_deleted)
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
                    choice = get_input(3,"Name | Price | Count | Category | Age | Detail\n> ",valid_options=['name','price','count','category','age','detail'])
                    
                    if choice == 'name':
                        notcheck = True
                        while notcheck:
                            tagged = False
                            name = get_input(3, "Enter new item Name: ")
                            # Check if that item name exists
                            for item in items_list:
                                if item['name'].lower() == name:
                                    print(ColoredNotification("That item name is already EXISTS!!!", "red"))
                                    Wait()
                                    ClearTerminal()
                                    tagged = True
                        
                            if tagged == False:
                                notcheck = False

                        item['name'] = name

                    elif choice == 'price':
                        item['price'] = get_input(2, "Enter new price: ")
                    elif choice == 'count':
                        item['count'] = get_input(1, "Enter new count: ")
                    elif choice == 'category':
                        item['category_id'] = Category.select_category()

                    elif choice == 'age':
                        notcheck = True
                        while notcheck:
                            min_age = get_input(1,"Minimum Age: ")
                            if min_age < 0 or min_age > 120:
                                print(ColoredNotification("Invalid Age!!!", "red"))
                                Wait()
                                ClearTerminal()
                            else:
                                notcheck = False

                        item['min_age'] = min_age

                    elif choice == 'detail':
                        item['detail'] = get_input(3,"Enter new detail: ")

                    cls.update_item_db(items_list)
                    break
 
    @classmethod
    def show_item(cls):
        items_list = cls.get_items_list()
        ClearTerminal()
        print(ColoredNotification("All Items", "green"))
        
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price", "Count", "Category_id", "detail", 'min_age']
        for item in items_list:
            if item['is_item_deleted'] == 0:
                table.add_row([item['item_id'], item['name'], item['price'], item['count'], Category.category_id_to_name(item['category_id']), item['detail'],item['min_age']])
        print(table)
        Wait()

    @staticmethod
    def create_table_item_for_admin(table_row_list: list):
        ClearTerminal()
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Price", "Count", "Category_id", "detail", 'min_age']
        for table_row in table_row_list:
            table.add_row([table_row[0], table_row[1], table_row[2], table_row[3], table_row[4], table_row[5], table_row[6]])
        print(table)
        Wait()

    @staticmethod
    def create_table_item_for_user(table_row_list: list):
        ClearTerminal()
        table = PrettyTable()
        table.field_names = ["ID","Name", "Price", "Count", "Category_id", "detail"]
        for table_row in table_row_list:
            table.add_row([table_row[0],table_row[1], table_row[2], table_row[3], table_row[4], table_row[5]])
        print(table)
        Wait()
    
    @classmethod
    def search_items(cls, items_list:list, search_by=None, search_value=None, min_count:int=None, max_count:int=None, 
                     min_price:int=None, max_price:int=None,sort_by=None, ascending=True, user_age:int=None):
        
        only_one_result = False
        table_row_list = []
        possible_id_to_select = []

        # if search from user_search_item_menu check the user age
        if user_age:
            for index, item in enumerate(items_list):
                if user_age < item['min_age']:
                    items_list.pop(index)
                    
        # Filtering items based on search criteria
        if search_by:
            if search_by == 'id':
                for item in items_list:
                    if item['item_id'] == search_value and item['is_item_deleted'] == 0:
                        table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], Category.category_id_to_name(item['category_id']), item['detail'],item['min_age']])
                        only_one_result = True
                        possible_id_to_select.append(item['item_id'])
                        break

            elif search_by == 'name':
                for item in items_list:
                    item_name = str(item['name'])
                    item_name = item_name.lower()
                    if item_name == search_value and item['is_item_deleted'] == 0:
                        table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], Category.category_id_to_name(item['category_id']), item['detail'],item['min_age']])
                        only_one_result = True
                        possible_id_to_select.append(item['item_id'])
                        break
                    
            elif search_by == 'category':
                for item in items_list:
                    if item['category_id'] == search_value and item['is_item_deleted'] == 0:
                        table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], Category.category_id_to_name(item['category_id']), item['detail'],item['min_age']])
                        possible_id_to_select.append(item['item_id'])

            else:
                for item in items_list:
                    if item['is_item_deleted'] == 0:
                        table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], Category.category_id_to_name(item['category_id']), item['detail'],item['min_age']])
                        possible_id_to_select.append(item['item_id'])

        if only_one_result == False:
            # Filter Price
            if min_price is not None:
                for index, item in enumerate(table_row_list):
                    if item[2] < min_price:
                        table_row_list.pop(index)
                        possible_id_to_select.remove(item[0])
            
            if max_price is not None:
                for index, item in enumerate(table_row_list):
                    if item[2] > max_price:
                        table_row_list.pop(index)
                        possible_id_to_select.remove(item[0])

            # Filter Count
            if min_count is not None:
                for index, item in enumerate(table_row_list):
                    if item[3] < min_count:
                        table_row_list.pop(index)
                        possible_id_to_select.remove(item[0])
            
            # if max_count is not None:
            #     for index, item in enumerate(table_row_list):
            #         if item[3] > max_count:
            #             table_row_list.pop(index)
            #             possible_id_to_select.remove(item[0])
                # TODO: Fix here i have to use while and index = 0 ; when if = True then index -= 1
                for index in range(0, len(table_row_list)):
                    if table_row_list[index][3] > max_count:
                        table_row_list.pop(index)
                        possible_id_to_select.remove(table_row_list[index][0])



            # Sorting the items
            if sort_by is not None:
                if sort_by == 'price':
                    table_row_list = sort_list(table_row_list,2,ascending)
                else:
                    table_row_list = sort_list(table_row_list,3,ascending)

        if user_age:
            cls.create_table_item_for_user(table_row_list)
        else:
            cls.create_table_item_for_admin(table_row_list)

        return possible_id_to_select

    @classmethod
    def admin_search_item_menu(cls):
        ClearTerminal()
        items_list = cls.get_items_list()
        only_one_result = False
        print(ColoredNotification("Enter 'n' if you don't want to filter that attribute!!!", "red"))

        search_by = get_input(3, "Search By (id/name/category): ", ['id', 'name', 'category'], 'n')
        search_value = None
        if search_by == "id":
            search_value = get_input(1, "Item ID: ", valid_options=cls.available_item_id(), return_none_on='n')
            only_one_result = True
        elif search_by == 'name':
            search_value = get_input(3, "Item Name: ", return_none_on='n')
            only_one_result = True
        elif search_by == 'category':
            ClearTerminal()
            Category.show_categories()
            search_value = get_input(1, "Item Category (ID): ", valid_options=Category.available_category_id(), return_none_on='n')

        ascending, sort_by, min_price, max_price, min_count, max_count = True, None,None,None,None,None
        if only_one_result == False:
            sort_by = get_input(3, "Sort By (price/count): ", ['price', 'count'], return_none_on='n')
            if sort_by:
                ascending = get_input(3, f"Ascending or Descending on {sort_by}? (a/d): ", ['a', 'd'], return_none_on='n')
                if ascending == 'd':
                    ascending = False

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
            ascending=ascending,
            sort_by=sort_by
        )

    @classmethod
    def user_search_item_menu(cls, user_age):
        ClearTerminal()
        items_list = cls.get_items_list()
        only_one_result = False
        print(ColoredNotification("Enter 'n' if you don't want to filter that attribute!!!", "red"))

        search_by = get_input(3, "Search By (name/category): ", ['name', 'category'], 'n')
        search_value = None
        if search_by == 'name':
            search_value = get_input(3, "Item Name: ", return_none_on='n')
            only_one_result = True
        elif search_by == 'category':
            ClearTerminal()
            Category.show_categories()
            search_value = get_input(1, "Item Category (ID): ", valid_options=Category.available_category_id(), return_none_on='n')

        ascending, sort_by, min_price, max_price, min_count, max_count = True, None,None,None,None,None
        if only_one_result == False:
            sort_by = get_input(3, "Sort By (price/count): ", ['price', 'count'], return_none_on='n')
            if sort_by:
                ascending = get_input(3, f"Ascending or Descending on {sort_by}? (a/d): ", ['a', 'd'], return_none_on='n')
                if ascending == 'd':
                    ascending = False

            min_price = get_input(2, "MIN PRICE: ", return_none_on='n')
            max_price = get_input(2, "MAX PRICE: ", return_none_on='n')
            min_count = get_input(2, "MIN COUNT: ", return_none_on='n')
            max_count = get_input(2, "MAX COUNT: ", return_none_on='n')

        # Use the consolidated search_items method based on the inputs
        possible_id_to_select = cls.search_items(
            items_list,
            search_by=search_by,
            search_value=search_value,
            min_count=min_count,
            max_count=max_count,
            min_price=min_price,
            max_price=max_price,
            sort_by=sort_by,
            ascending=ascending,
            user_age=user_age
        )

        return possible_id_to_select
        
    @classmethod
    def user_free_search(cls, search_word:str,user_age):
        table_row_list = []
        possible_id_to_select = []
        items_list = cls.get_items_list()
        for item in items_list:
            if search_word in item['name'].lower() or search_word in Category.category_id_to_name(item['category_id']).lower():
                if user_age >= item['min_age']:
                    table_row_list.append([item['item_id'], item['name'], item['price'], item['count'], Category.category_id_to_name(item['category_id']), item['detail'],item['min_age']])
                    possible_id_to_select.append(item['item_id'])

        cls.create_table_item_for_user(table_row_list)
        return possible_id_to_select


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
                selectedItem = cls(item['item_id'], item['name'], item['price'], item['count'], item['category_id'], item['detail'], item['min_age'], item['is_item_deleted'])
                file.write(f'{selectedItem.__dict__}\n')

    @classmethod
    def available_item_id(cls):
        available_id_list = []
        items_list = cls.get_items_list()
        for item in items_list:
            if item['is_item_deleted'] == 0:
                available_id_list.append(int(item['item_id']))

        return available_id_list

    @classmethod
    def item_id_to_buy_it(cls, item_id_to_buy,user_age, buy_count, user_cart_id):
        was_it_right = False
        items_list = cls.get_items_list()
        for item in items_list:
            if item['item_id'] == item_id_to_buy:
                if user_age >= item['min_age']:
                    if buy_count <= item['count']:
                        was_it_right = True
                        Cart.add_item_to_user_cart(user_cart_id, item['name'], item['price'], buy_count)
                    else:
                        print(ColoredNotification(f"Sorry, You want ({buy_count}), but we dont have that much right now!\nWe have only ({item['count']})","cyan"))
                        Wait()
                else:
                    print(ColoredNotification(f"You are ({user_age}) years old!!!\nCome back when you are ({item['min_age']})!","red"))
                    Wait()

        if was_it_right == False:
            print(ColoredNotification(f"Item ID ({item_id_to_buy}) wasn't found!!!","red"))
            Wait()

    @classmethod
    def convert_item_id_to_name(cls, item_id):
        items_list = cls.get_items_list()
        for item in items_list:
            if item['item_id'] == item_id:
                return item['name']

