# This file will be used to instantiate different classes (create new objects)
from item import Item

Item.instantiate_from_csv()
print(Item.all)                 # checking if instantiation from .csv file actually worked
print()

item1 = Item("MyItem", 750)     # I don't specify quantity because we have a default value of 0
print(item1.name)

item2 = Item("Blob", 333)
print(item2.name) 

print()

# Now that we made the name a read-only attribute (@property), how to set a new value for it ?
# answer in item.py, lines 22 to 24, @name.setter
item1.name = "OtherItem"
print(item1.name)
print()

item2.name = "De Blob"  # Setting an attribute
print(item2.name)       # Getting an attribute

item3 = Item("LongName", 82)
print(item3.name)
item3.name = "TooLongName"
print(item3.name) 