# Create a class and instantiate some object of this class
class Item:
    pass

item1 = Item()

# Create some attributes for our object
item1.name = "Phone"
item1.price = 600
item1.color = "red"
item1.quantity = 8

print(type(item1)) # Item
print(type(item1.name)) # str
print(type(item1.price)) # int
print(type(item1.quantity)) # int