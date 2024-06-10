# category_id | name | is_category_deleted
from tools import *
from prettytable import PrettyTable

class Category:
    def __init__(self, category_id, name, is_category_deleted):
        self.category_id = category_id
        self.name = name
        self.is_category_deleted = is_category_deleted

    @classmethod
    def show_categories(cls):
        category_list = cls.get_categories_list()
        ClearTerminal()
        print(ColoredNotification("All Categories", "green"))
        
        table = PrettyTable()
        table.field_names = ["ID", "Name"]
        for category in category_list:
            if category['is_category_deleted'] == 0:
                table.add_row([category['category_id'], category['name']])
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
                ClearTerminal()
                cls.show_categories()
                category_id = get_input(1, "Item Category (ID): ", valid_options=Category.available_category_id())
                for category in category_list:
                    if category['category_id'] == int(category_id) and category['is_category_deleted'] == 0:
                        category_id = int(category_id)
                        return category_id


    @classmethod
    def category_id_to_name(cls,category_id):
        category_list = cls.get_categories_list()
        for category in category_list:
            if category['category_id'] == category_id:
                return category['name']
            

    @classmethod
    def category_menu(cls):
        category_menu_flag = True
        while category_menu_flag:
            ClearTerminal()
            print(ColoredNotification("Category:", "red"))
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
            else:
                print(ColoredNotification("Invalid Option", "red"))
                Wait()

    def getId():
        with open("DB\\category_db\\id_last_cat_created.txt","r") as file:
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
            ClearTerminal()
            category_id = Category.getId()
            name = input("Category Name: ")
            selectedCategory = cls(category_id,name,0)
            with open("DB\\category_db\\category.txt", "a") as file:
                file.write(f'{selectedCategory.__dict__}\n')

            Category.update_last_category_id(category_id)

            print(ColoredNotification("The Category Added Successfuley", "green"))
            # Do admin wants to add more category?
            answer = input("Anything to Continue\n0 to EXIT\n> ")
            if answer == "0":
                flag = False
                break

    def update_last_category_id(new_category_id):
        with open("DB\\category_db\\id_last_cat_created.txt","w") as file:
            file.write(str(new_category_id))


    @classmethod      
    def remove_category(cls):
        category_list = cls.get_categories_list()

        ClearTerminal()
        cls.show_categories()
        category_id = get_input(1,"(0 to exit)\nEnter category ID to remove: ",valid_options=cls.available_category_id(),return_none_on='0')
        if category_id:
            for category in category_list:
                if category["category_id"] == int(category_id):
                    category['is_category_deleted'] = 1
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
        category_id = get_input(1,"(0 to exit)\nEnter Category ID to edit: ",valid_options=cls.available_category_id(),return_none_on='0')
        if category_id:
            for category in category_list:
                if category["category_id"] == int(category_id) and category['is_category_deleted'] == 0:
                    category['name'] = input("Enter new CATEGORY Name: ")

                    cls.update_category_db(category_list)
                    break

    def create_table_category(table_row_list: list):
        table = PrettyTable()
        table.field_names = ["ID", "Name"]
        for table_row in table_row_list:
            table.add_row([table_row[0], table_row[1]])
        print(table)
        Wait()

    @classmethod
    def search_category(cls, category_list, search_by=None, search_value=None):
        table_row_list = []

        # Filtering based on search_by criteria
        if search_by == 'id':
            for category in category_list:
                if category['category_id'] == search_value and category['is_category_deleted'] == 0:
                    table_row_list.append([category['category_id'], category['name']])
                    break
        elif search_by == 'name':
            for category in category_list:
                if category['name'].lower() == search_value and category['is_category_deleted'] == 0:
                    table_row_list.append([category['category_id'], category['name']])
                    break

        cls.create_table_category(table_row_list)

    @classmethod
    def search_category_menu(cls):
        ClearTerminal()
        category_list = cls.get_categories_list()

        print(ColoredNotification("Enter 'n' if you don't want to filter that attribute!!!", "red"))

        search_by = get_input(3, "Search By (id/name): ", ['id', 'name', ], 'n')
        search_value = None
        if search_by == "id":
            search_value = get_input(1,"Category ID: ",return_none_on='n',valid_options=cls.available_category_id())
        elif search_by == 'name':
            search_value = get_input(3,"Category Name: ",return_none_on='n')  # TODO: Must check a list of category names if available

        cls.search_category(category_list, search_by=search_by, search_value=search_value)

    @classmethod
    def available_category_id(cls):
        available_id_list = []
        category_list = cls.get_categories_list()
        for category in category_list:
            if category['is_category_deleted'] == 0:
                available_id_list.append(int(category['category_id']))

        return available_id_list