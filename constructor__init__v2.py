# When invoking a method, you might use wrong data type (for ex, string instead of integer)
# To prevent this, we have to validate the data types of the values that are passed in
class Item:
    # Class Attributes
    pay_rate = 0.8 # The default pay rate = 20% discount
    all = [] # empty list in which we will store objects (items)
    
    # Constructor
    def __init__(self, name:str, price:float, quantity=0): # no need to specify the data type because default value is an integer
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Run validations to the received arguments (args) and help debugging
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # appending instances of our class (objects) to the list
        Item.all.append(self)

    # Methods
    def totalPrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.price = self.price * self.pay_rate # applying 20% discount
        self.price = round(self.price, 2) # rounding down to 2 decimals
    
    # Magic built-in method returning a string that represents the object
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})" 
        # name is a string, so we use single quotes to escape surrounding double quotes

item1 = Item("honeypot", 12.0, 4)
item2 = Item("Pepper", 3.5, 5)
item3 = Item("Apple", 0.3, 12)
item4 = Item("Pasta", 1.5, 8)
item5 = Item("Tomato", 0.8, 10)

print(Item.all)
print()

# check if all instances have been added to our list
for instance in Item.all:
    print(instance.name) 

item1.applyDiscount()
print(f"\nItem1: {item1.name}")
print(f"Item1 pay rate: {item1.pay_rate}")
print(f"Discount unit price: {item1.price}€")
print(f"Discount Total price: {item1.totalPrice()}€")
print()

# So far, we worked with "instance attributes"
# There is another kind of attributes that we call "Class Attributes"
# A Class Attribute is an attribute which belongs to the class itself, but can also be accessed from the instance level

print(f"Item pay_rate (class level): {Item.pay_rate}") # accessing attribute from the class level
print(f"item1 pay_rate (instance level): {item1.pay_rate}") # accessing attribute from the instance level
print()

# Using a built-in magic attribute that displays all attributes belonging to a class|object
print("Attributes belonging to the Item class:")
print(Item.__dict__)
print("\nAttributes belonging to the item1 object:")
print(item1.__dict__)


# just testing the round() function
print("\nJust testing the round() function:")
print(f"Round 25.600002 down to 2 decimals: {round(25.600002, 2)}")
print(f"Round 25.638562 down to 2 decimals: {round(25.638562, 2)}\n")


# customizing pay rate for a specific instance
item2 = Item("Pepper", 3.5, 5)
print(f"Item2: {item2.name}")
item2.pay_rate = 0.6 # instance attribute
print(f"Item2 pay rate: {item2.pay_rate}")
item2.applyDiscount()
print(f"Discount unit price: {item2.price}€")
print(f"Discount Total price: {item2.totalPrice()}€")
