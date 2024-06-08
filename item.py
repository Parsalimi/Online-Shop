### id | name | count | price | rating | Seller Shop | category | Detail | Features [Sub Feutures []] | Created Date | Created by | IsDiscounted | Discount Date ###

class Item():
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

Item.UpdateLastId()
