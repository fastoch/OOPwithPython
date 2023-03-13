# When invoking a method, you might use wrong data type (for ex, string instead of integer)
# To prevent this, we have to validate the data types of the values that are passed in
class Item:
    def __init__(self, name:str, price:float, quantity=0): # no need to specify the data type because default value is an integer
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Run validations to the received arguments (args) and help debugging
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

    def totalPrice(self):
        return self.price * self.quantity
    
item1 = Item("honeypot", 12.0, 4)

print(f"{item1.totalPrice()}€")
print(item1.name)

# So far, we worked with "instance attributes"
# There is another kind of attributes that we call "Class Attributes"
# A Class Attribute is an attribute to belong to the class itself, but can also be accessed from the instance level