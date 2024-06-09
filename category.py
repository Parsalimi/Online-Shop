# category_id | name | isCategoryDeleted
from tools import *
from prettytable import PrettyTable

class Category:
    def __init__(self, category_id, name, isCategoryDeleted):
        self.category_id = category_id
        self.name = name
        self.isCategoryDeleted = isCategoryDeleted

    @classmethod
    def show_categories(cls):
        category_list = cls.get_categories_list()
        ClearTerminal()
        print(ColoredNotification("All Categories", "green"))
        
        table = PrettyTable()
        table.field_names = ["ID", "Name"]
        for item in category_list:
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
