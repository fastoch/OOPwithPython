# In my file "1.firstClass.py", I had to declare attributes each time I wanted to instantiate a new object
# What if I don't want to hard-code these attributes for each instantiation of our class ?
# It is best practice to declare these attributes in the class definition

class Item:
    def __init__(self, name, price, quantity): # This block is what we call a constructor
    # By adding parameters without setting a default value, I make these parameters mandatory for each instatiation of the class
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"A new instance of Item named \"{name}\" has been created.") # this is an f-string, or formatted string
        print(f"This item costs {price}€/unit.")
        print(f"I want to buy {quantity} units of this item.")
        print(f"This will cost me {price*quantity}€.\n")

    def calculateTotalPrice(self):
        return self.price * self.quantity
        
item1 = Item("banana", 2, 12)
item2 = Item("strawberry", 8, 50)

print(f"{item1.calculateTotalPrice()}€")
print(f"{item2.calculateTotalPrice()}€")

# The following lines will induce an AttributeError if I forget to declare my attributes in __init__ (self.attributeName)
print(item1.name)
print(item2.name)
print(item1.quantity)
print(item2.price)

# When defining our constructor, we can differentiate mandatory parameters from non-mandatory ones
class Item2:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
# By setting a default value for the parameter quantity, I make it a non-mandatory parameter

# Assigning attributes outside of the constructor (__init__)
item1.is_yellow = True
item2.is_yellow = False