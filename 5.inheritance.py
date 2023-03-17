import csv

# The code below has been minimized on purpose
class Item:
    pay_rate = 0.8 
    all = []
    
    def __init__(self, name:str, price:float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        Item.all.append(self)

    def totalPrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.price = self.price * self.pay_rate 
        self.price = round(self.price, 2) 
    
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})" 
    
    @classmethod 
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:  
            reader = csv.DictReader(f)      
            items = list(reader)            
        for item in items:
            print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def check_integer(num):
        if isinstance(num, float):      
            return num.is_integer()     
        elif isinstance(num, int):
            return True
        else:
            return False        


### The code below is what will be focusing on ###

# We want to create a method that calculates the number of phones that are not broken (quantity - broken phones)
# This method will not be useful for any instance of the Item class, because it only applies to phones
# To solve this, we can create a separated class that will inherit the functionalities of the Item class

# The Phone class will inherit all the attributes and methods from the Item class
class Phone(Item):
    pass

phone1 = Phone("Moto_v10", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("Moto_v20", 700, 5)
phone2.broken_phones = 1

# Phone is the child class of Item
# Item is the parent class of Phone