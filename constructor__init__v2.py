import csv

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

        # appending each new instance of our class to the list named "all"
        Item.all.append(self)

    # Methods
    def totalPrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.price = self.price * self.pay_rate # applying 20% discount
        self.price = round(self.price, 2) # rounding down to 2 decimals
    
    # Magic built-in method which formats the list Item.all (improves readability)
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})" 
    
    @classmethod # make instantiate_from_csv a class method
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:   # opens items.csv in read mode and alias it as 'f'
            reader = csv.DictReader(f)      # each line in the file becomes a new entry in a dictionary
            items = list(reader)            # turn the dictionary into a list of items

        for item in items:
            print(item)
            Item(
                name = item.get('name'),
                price = int(item.get('price')),
                quantity = int(item.get('quantity')),
            )
            
# class methods can be applied to the class, while other methods can only be applied to instances of the class

# I commented out those lines because I'm using a .csv file to create new objects (new instances of the class "Item")
    # Phone = Item("honeypot", 12.0, 4)
    # Laptop = Item("Pepper", 3.5, 5)
    # item3 = Item("Apple", 0.3, 12)
    # item4 = Item("Pasta", 1.5, 8)
    # item5 = Item("Tomato", 0.8, 10)

Item.instantiate_from_csv()
print()

print(Item.all)
print()

# check if all instances have been added to our list
for instance in Item.all:
    print(instance.name) 

Item.all[0].applyDiscount()
print(f"\nPhone: {Item.all[0].name}")
print(f"Phone pay rate: {Item.all[0].pay_rate}")
print(f"Discount unit price: {Item.all[0].price}€")
print(f"Discount Total price: {Item.all[0].totalPrice()}€")
print()

# So far, we worked with "instance attributes"
# There is another kind of attributes that we call "Class Attributes"
# A Class Attribute is an attribute which belongs to the class itself, but can also be accessed from the instance level

# Using a built-in magic attribute that displays all attributes belonging to a class|object
print("Attributes belonging to the Item class:")
print(Item.__dict__)
print("\nAttributes belonging to the Phone object:")
print(Item.all[0].__dict__)


# just testing the round() function
print("\nJust testing the round() function:")
print(f"Round 25.600002 down to 2 decimals: {round(25.600002, 2)}")
print(f"Round 25.638562 down to 2 decimals: {round(25.638562, 2)}\n")


# customizing pay rate for a specific instance
Item.all[1].pay_rate = 0.6
print(f"Laptop pay rate: {Item.all[1].pay_rate}")
Item.all[1].applyDiscount()
print(f"Discount unit price: {Item.all[1].price}€")
print(f"Discount Total price: {Item.all[1].totalPrice()}€")
