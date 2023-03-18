# This file will be used to declare and update the Item class
import csv

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