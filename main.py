# This file will be used to instantiate different classes (create new objects)
from item import Item

Item.instantiate_from_csv()
print(Item.all)                 # checking if instantiation from .csv file actually worked

item1 = Item("MyItem", 750)     # I don't specify quantity because we have a default value of 0
item1.name = "OtherItem"

print(item1.name)

# Read-Only Attributes are declared in the class (item.py --> @property)
print(item1.read_only_name)
item1.read_only_name = "BBB"    # AttributeError: property 'read_only_name' of 'Item' object has no setter
