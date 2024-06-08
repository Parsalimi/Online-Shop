########################################################################### ITEM FORMAT ############################################################################
### id | name | count | price | rating | Seller Shop | category | Detail | Features [Sub Feutures []] | Created Date | Created by | IsDiscounted | Discount Date ###
####################################################################################################################################################################
from main import OnlineShop
from tools import *
from datetime import datetime

class Item():
    items_list = []

    def __init__(self, id, name, count, price, rating, sellerShop, category, detail, features, createdDate, createdBy, isDiscounted, discountDate):
        self.id = id
        self.name = name
        self.count = count
        self.price = price
        self.rating = rating
        self.sellerShop = sellerShop
        self.category = category
        self.detail = detail
        self.features = features
        self.createdDate = createdDate
        self.createdBy = createdBy
        self.isDiscounted = isDiscounted
        self.discountDate = discountDate

    def getId():
        with open("DB\\item_db\\lastItemId.txt","r") as file:
            lastBookId = file.read()
            if lastBookId != "":
                lastBookId = int(lastBookId) + 1
                return lastBookId
            else:
                return 1

    def UpdateLastId():
        with open("DB\\item_db\\lastItemId.txt","w") as file:
            file.write(str(Item.getId()))

    def AddItemMenu():
        ClearTerminal()
        if OnlineShop.selectedUser.role == "2":
            flag = True
            while flag:
                name = input("item Name: ")
                count = input("item Count: ")
                price = input("item Price: ")
                rating = 0
                sellerShop = input("What is the Seller Shop Name: ") #TODO it must be deleted from this menu and equalls to Parsa Shop
                category = input("item Category: ")
                detail = input("item Detail: ")
                features = input("item Features: ")
                createdDate = datetime.now()
                createdBy = OnlineShop.selectedUser.username
                isDiscounted = "0"
                discountDate = ""
                selectedItem = Item(Item.getId(), name,count,price,rating,sellerShop,category,detail,features,createdDate,createdBy,isDiscounted,discountDate)
                with open("DB\\item.txt", "a") as file:
                    file.write(f'{selectedItem.__dict__}\n')

                Item.update_last_item_id()

                print(ColoredNotification("The item Added Successfuley", "green"))
                # Do admin wants to add more item?
                answer = input("Anything to Continue\n0 to EXIT\n> ")
                if answer == "0":
                    flag = False
                    break

    def update_last_item_id():
        with open("DB\\lastItemId.txt","w") as file:
            file.write(str(Item.getId()))
            
    def update_item_list():
        Item.items_list = []
        with open("DB\\item_db\\item.txt", "r") as file:
            for line in file.readlines():
                Item.items_list.append(eval(line))

