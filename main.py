# This file will be used to instantiate different classes (create new objects)
from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)                 # checking if instantiation from .csv file actually worked
