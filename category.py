# category_id | name | isCategoryDeleted
from tools import *
from prettytable import PrettyTable

class Category:
    def __init__(self, category_id, name, is_category_deleted):
        self.category_id = category_id
        self.name = name
        self.isCategoryDeleted = is_category_deleted

    @classmethod
    def show_categories(cls):
        category_list = cls.get_categories_list()
        ClearTerminal()
        print(ColoredNotification("All Categories", "green"))
        
        table = PrettyTable()
        table.field_names = ["ID", "Name"]
        for item in category_list:
            if item['is_category_deleted'] == 0:
                table.add_row([item['category_id'], item['name']])
        print(table)
        Wait()

    def get_categories_list():
        category_list = []
        with open('DB\\category_db\\category.txt','r') as file:
            for line in file.readlines():
                category_list.append(eval(line))
            return category_list
    
    @classmethod
    def select_category(cls):
        category_list = cls.get_categories_list()
        flag = True
        while flag:
            ClearTerminal()
            if not category_list:
                print(ColoredNotification("You haven't Created any Category\nFirst Create a Category", "red"))
                Wait()
                return False
            else:
                cls.show_categories()
                category_id = input("Enter the ID of the category you want to select\n> ")
                for item in category_list:
                    if item['category_id'] == int(category_id) and item['isCategoryDeleted'] == 0:
                        category_id = int(category_id)
                        return category_id
                    else:
                        print(ColoredNotification("Category not found or deleted", "red"))
                        Wait()

    @classmethod
    def category_name_to_id_convert(cls,category_name):
        category_list = cls.get_categories_list()
        for category in category_list:
            if category['name'] == category_name:
                return category['category_id']
            

    @classmethod
    def category_menu(cls):
        category_menu_flag = True
        while category_menu_flag:
            ClearTerminal()
            print(ColoredNotification("Item:", "red"))
            print(ColoredNotification("Add | Remove | Edit | Show | Search | Exit", "green"))
            answer = input(ColoredNotification("> ", "cyan")).lower()
            if answer == "add":
                cls.add_category()
            elif answer == "remove":
                cls.remove_category()
            elif answer == "edit":
                cls.edit_category()
            elif answer == "show":
                cls.show_categories()
            elif answer == "search":
                cls.search_category_menu()
            elif answer == "exit":
                category_menu_flag = False
                break

    def getId():
        with open("DB\\category_db\\id_last_cat_created","r") as file:
            last_categry_Id = file.read()
            if last_categry_Id != "":
                last_categry_Id = int(last_categry_Id) + 1
                return last_categry_Id
            else:
                return 1
            
    @classmethod
    def add_category(cls):
        ClearTerminal()
        flag = True
        while flag:
            category_id = Category.getId()
            name = input("item Name: ")
            selectedCategory = cls(category_id,name)
            with open("DB\\item_db\\item.txt", "a") as file:
                file.write(f'{selectedCategory.__dict__}\n')

            Category.update_last_item_id()

            print(ColoredNotification("The Category Added Successfuley", "green"))
            # Do admin wants to add more item?
            answer = input("Anything to Continue\n0 to EXIT\n> ")
            if answer == "0":
                flag = False
                break

    def update_last_item_id():
        with open("DB\\category_db\\id_last_cat_created","w") as file:
            file.write(str(Category.getId()))


    @classmethod      
    def remove_category(cls):
        category_list = cls.get_categories_list()

        ClearTerminal()
        cls.show_categories()
        category_id = input("Enter category ID to remove: ")
        for item in category_list:
            if item["category_id"] == int(category_id):
                item['is_category_deleted'] = 1
        cls.update_category_db(category_list)
        
    @classmethod
    def update_category_db(cls, category_list):
        with open('DB\\category_db\\category.txt', 'w') as file:
            for category in category_list:
                selectedCategory = cls(category['category_id'], category['name'], category['is_category_deleted'])
                file.write(f'{selectedCategory.__dict__}\n')

    @classmethod
    def edit_category(cls):
        category_list = cls.get_categories_list()
        ClearTerminal()
        cls.show_categories()
        item_id = input("Enter Category ID to edit: ")
        for category in category_list:
            if category["category_id"] == int(item_id) and category['is_category_deleted'] == 0:
                category['name'] = input("Enter new CATEGORY Name: ")

                cls.update_category_db(category_list)
                break

    @classmethod
    def search_category(cls, category_list, search_by=None, search_value=None):
        table_row_list = []
        
        # Filtering based on search_by criteria
        if search_by == 'id':
            items_list = [item for item in items_list if item['category_id'] == search_value and item['is_item_deleted'] == 0]
        elif search_by == 'name':
            items_list = [item for item in items_list if item['name'] == search_value and item['is_item_deleted'] == 0]

        # Collecting the results
        for category in category_list:
            if category['is_item_deleted'] == 0:
                table_row_list.append([category['category_id'], category['name']])

        cls.create_table_category(table_row_list)

    def create_table_category(table_row_list: list):
        table = PrettyTable()
        table.field_names = ["ID", "Name"]
        for table_row in table_row_list:
            table.add_row([table_row[0], table_row[1]])
        print(table)
        Wait()


    @classmethod
    def search_category_menu(cls):
        ClearTerminal()
        items_list = cls.get_categories_list()

        print(ColoredNotification("Enter 'n' if you don't want to filter that attribute!!!", "red"))

        search_by = get_input(3, "Search By (id/name): ", ['id', 'name', ], 'n')
        search_value = None
        if search_by == "id":
            search_value = get_input(1,"Item ID: ",return_none_on='n') # TODO: Must check a list of item names if available
        elif search_by == 'name':
            search_value = get_input(3,"Item Name: ",return_none_on='n')  # TODO: Must check a list of item names if available

        # Here you can use the consolidated search_items method based on the inputs
        cls.search_category(items_list, search_by=search_by, search_value=search_value)