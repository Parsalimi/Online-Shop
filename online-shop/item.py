### id | name | count | price | rating | Seller Shop | category | Detail | Features [Sub Feutures []] | Created Date | Created by | IsDiscounted | Discount Date ###

class Items():
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