# This file will be used to declare and update the Item class
import csv

class Item:
    pay_rate = 0.8 
    all = []
    
    def __init__(self, name:str, price:float, quantity=0):
        self.__name = name          # __name is a private attribute, not accessible from outside of the class
        self.price = price
        self.quantity = quantity
        
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        Item.all.append(self)

    @property   # Property decorator = read-only attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_value):
        self.__name = new_value

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
    
    # @property
    # def read_only_name(self):
    #     return "AAA"

    ## To prevent access to an attribute outside of the class, you must use __attributeName (double underscore) ##