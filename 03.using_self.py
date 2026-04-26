# Use of self in Python OOPs
# 1. self in Instance Methods

# Example:-

class Product:
    def __init__(self,name,price):
        self.name = name                                    # ---> Assigning instance attributes
        self.price = price

    def display_info(self):
        print(f"Product:{self.name},Price:{self.price}")

# Creating objects
p1 = Product("laptop",50000)
p2 = Product("phone",20000)


# Calling instance method
p1.display_info()
p2.display_info()



# 2. self Helps in Modifying Instance Attributes
# Example:-


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def apply_discount(self,discount):
        self.price -= self.price * (discount/100)

p1 = Product("Laptop",50000)
p1.apply_discount(10)

print(p1.price)


# 3. self is Not a Keyword
# Example (Unconventional, but works):

class Product:
    def __init__(xyz,name,price):                        # ---> Using 'xyz' instead of 'self'
        xyz.name = name
        xyz.price = price

    def display_info(abc):                                # ----> Using 'abc' instead of 'self'
        print(f"Product:{abc.name},Price:{abc.price}")

p1 = Product("Tablet",30000)
p1.display_info()




# 4. self vs. Class Attributes (cls)
# Example:-

class Product:
    discount = 5                      # ---> Class Attribute
    
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def apply_discount(self):
        self.price -= self.price * (self.discount/100)                 # ----> Uses self.discount
    
    @classmethod
    def set_discount(cls,new_discount):                                # ---> Updates class attribute
        cls.discount = new_discount

Product.set_discount(10)                                               # ---> Updating class discount

p1 = Product("Laptop",50000)
p1.apply_discount()

print(p1.price)
