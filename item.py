# This file will be used to declare and update the Item class
import csv

class Item:
    pay_rate = 0.8 
    all = []
    
    def __init__(self, name:str, price:float, quantity=0):
        self.__name = name          # name is a private attribute, not accessible from outside the class
        self.__price = price
        self.quantity = quantity
        
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise Exception("Prices can't be negative!")
        self.__price = new_price
    
    def applyDiscount(self):
        self.__price = self.__price * self.pay_rate 
        self.__price = round(self.__price, 2) 

    def applyIncrease(self, increase_rate):
        self.__price = self.__price *  (1 + increase_rate)
        self.__price = round(self.__price, 2) 

    @property   # Property decorator = read-only attribute
    def name(self):
        print("You're trying to get the current name")  # display a message every time we try to access the name attribute
        return self.__name
    
    @name.setter    # allows name modification
    def name(self, new_value):
        print("You're trying to set a new name")
        if len(new_value) > 10:     # restrict the length of the name
            raise Exception("Name length can't exceed 10 characters.")
        self.__name = new_value

    def total__Price(self):
        total = self.__price * self.quantity
        return f"Total price is: {total}€"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.__price}, {self.quantity})" 
        # self.__class__.__name__ allows us to access the name of the class (to which belongs the instance)
    
    @classmethod 
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:   # opens items.csv in read mode and give the name 'f' to the file handler
            reader = csv.DictReader(f)      # access items.csv and make a dictionary out of it
            items = list(reader)            # turns the dictionary into a list of items
        for item in items:
            Item(
                name = item.get('name'),                # get the value in the column 'name' and assign it to the name attribute
                price = float(item.get('price')),       # same thing with a type conversion (from string to floating point number)
                quantity = int(item.get('quantity')),   # same thing but converting from string to integer
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