# In 'constructor__init__v2.py', we saw an example of a class method with instantiate_from_csv()
# Now, we will see an example of a static method with check_integer()

import csv

class Item:
    pay_rate = 0.8 
    all = []
    
    # Constructor
    def __init__(self, name:str, price:float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        Item.all.append(self)

    # Methods
    def totalPrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.price = self.price * self.pay_rate 
        self.price = round(self.price, 2) 
    
    # Magic built-in method which formats the list Item.all (improves readability)
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})" 
    
    # class methods can be applied to a class, while other methods can only be applied to instances of a class
    @classmethod 
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:   # opens items.csv in read mode and alias it as 'f'
            reader = csv.DictReader(f)      # each line in the file becomes a new entry in a dictionary
            items = list(reader)            # turn the dictionary into a list of items

        for item in items:
            print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def check_integer(num):
        # we count out the floats that are point zero (5.0, 10.0, 7.0, ...)
        if isinstance(num, float):      # if num is a float (floating point number)
            return num.is_integer()     # built-in function that returns True for 7.0 and False for 7.3
        elif isinstance(num, int):
            return True
        else:
            return False


Item.instantiate_from_csv()     # Displays items contained in my items.csv file
print()
print(Item.check_integer(12))   # True
print(Item.check_integer(12.0)) # True
print(Item.check_integer(12.5)) # False

# When to use class methods and when to use static methods ?
    # We use a static method when want to do something that should not be instance-specific (object-specific)
    # We use a class method for instantiating objects from some structured data like a .csv file