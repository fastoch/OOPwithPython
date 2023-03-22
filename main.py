# This file will be used to instantiate different classes (create new objects)
from item import Item
from phone import Phone
from keyboard import Keyboard

Item.instantiate_from_csv()
print(Item.all)                 # checking if instantiation from .csv file actually worked
print()

item1 = Item("MyItem", 750, 6)     # I don't specify quantity because we have a default value of 0
print(item1.name)

item2 = Item("Blob", 333)
print(item2.name) 

print()

# Now that we made the name a read-only attribute (@property), how to set a new value for it ?
# answer in item.py, lines 22 to 24, @name.setter
item1.name = "OtherItem"
item1.price = 800
print(f"item1 name is: {item1.name}")
print(f"item1 price is: {item1.price}€")

item1.applyDiscount()
print(f"Price after discount is: {item1.price}€")
item1.applyIncrease(0.1)
print(f"Price after increase is: {item1.price}€")

item2.name = "De Blob"  # Setting an attribute
print(item2.name)       # Getting an attribute

item3 = Item("LongName", 82)
print(item3.name)
# item3.name = "TooLongName"
# print(item3.name) 

item1.send_email()  # I can access send_email(), but not the private methods which are part of send_email()

item4 = Phone("Zflip4", 700, 16)
item4.applyIncrease(0.11)
print(item4.price)
item4.applyDiscount()
print(item4.price)
item4.send_email()

# Polymorphism
item4.name = "randomName"
print(len(item4.name))  # 10 (10 characters)
some_list = ["tata", "toto", "titi"]
print(len(some_list))   # 3 (3 items in my list)

item5 = Keyboard("Logitech", 80, 8)
print(item5.name)
item5.applyDiscount()
print(item5.price)