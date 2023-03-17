# Create a class
class Item:
    # __init__ constructor
    def __init__(self):
        print("I am a new item!")
    # basic method
    def calculateTotalPrice(self, x, y):
        return x * y

# class instantiation (= object creation)
item1 = Item()
item2 = Item()

# Create some attributes for our object
item1.name = "Phone"
item1.price = 600
item1.color = "red"
item1.quantity = 8

print(type(item1)) # __main__.Item
print(type(item1.name)) # str
print(type(item1.price)) # int
print(type(item1.quantity)) # int

# an object is an instance of a class
# attributes are the object properties

# String is a built-in class, including multiple built-in methods
random_str = "aaa"
print(random_str.upper()) # AAA

# Methods must be defined inside our class
# Methods are functions inside classes

# Python passes the object itself as a first argument when you call a method, 
# which is why you always see a default parameter named 'self' when you declare a method
# using the word self is a common convention. It's best practise to use this specific word

# arguments are what you pass to a method while invoking it
# parameters are what you pass to a method while declaring it

print(item1.calculateTotalPrice(item1.price, item1.quantity))