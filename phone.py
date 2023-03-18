# This file will be used to declare and update the Phone class
from item import Item   # import the Item class from the file item.py

class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        # Call to super function to inheritk all attributes and methods from the parent class (Item)
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
print(Item.all)