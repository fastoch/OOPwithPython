# In my file firstClass.py, I had to declare attributes each time I wanted to instantiate a new object
# What if I don't want to hard-code these attributes for each instantiation of our class ?
# How to add some scalability here? (a good developer avoids repetitions and favor scalability)

class Item:
    def __init__(self, name, price, quantity):
        print(f"A new instance of Item named \"{name}\" has been created.")
        print(f"This item costs {price}€/unit.")
        print(f"I want to buy {quantity} units of this item.")
        print(f"This will cost me {price*quantity}€.\n")
        
# By adding parameter to my __init__ method, I make these parameters mandatory for each instatiation of the class

item1 = Item("banana", 2, 12)
item2 = Item("strawberry", 8, 50)