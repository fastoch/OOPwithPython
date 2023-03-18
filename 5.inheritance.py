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
        total = self.price * self.quantity
        return f"Total price is: {total}€"
    
    def applyDiscount(self):
        self.price = self.price * self.pay_rate 
        self.price = round(self.price, 2) 
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})" 
        # self.__class__.__name__ allows us to access the name of the class (to which belongs the instance)
    
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

# The Phone class will inherit all attributes and methods from the Item class, including the list appending (line 16)
class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        # Call to super function to inheritk all attributes and methods from the parent class
        super().__init__(           # This calls the __init__ method in the parent class
            name, price, quantity   # This imports attributes from the parent class (Item) to the child class (Phone)
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken_Phones {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

phone1 = Phone("Moto_v10", 500, 5)
phone2 = Phone("Moto_v20", 700, 8)

# using a method declared in the parent class (Item)
print(phone1.totalPrice())
print(phone2.totalPrice()) 

# Note that I replaced 'Item' with '{self.__class__.__name__}' in the __repr__ method (line 27)
print(Item.all)     # same result as print(Phone.all)

# Phone is the child class of Item
# Item is the parent class of Phone

# when declaring a child class, we don't have to copy the entirety of the constructor (__init__)
# instead, we can use the 'super' function