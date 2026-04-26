# Example: E-commerce Product Class


# Step 1: Define a class
class Product:

# Attributes (data)    
    name = 'Laptop'
    price = 50000
    quantity = 10

# Methods (functions)
    def display_info(self):
        print(f"Product:{self.name},Price:{self.price},Quantity:{self.quantity}")



# Example: Creating Objects

# Step 2: Create objects of the Product class
product1 = Product()
product2 = Product()


# Access attributes and methods
product1.display_info()
product2.display_info()



# Example: Modifying Attributes


# Step 3: Modify attributes

product1.name = 'Smartphone'
product1.price = 30000
product1.quantity = 5

product1.display_info()




# 1. Types of Attributes
# (a) Instance Attributes

# Example:-

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Creating two different product instances
p1 = Product("Laptop",50000,10)
p2 = Product("Phone",30000,2)

print(p1.name)
print(p2.name)



# (b) Class Attributes
# Example:-


class Product:
    discount = 10     #  ---> Class Attribute

    def __init__(self,name,price):
        self.name = name
        self.price = price
 
p3 = Product('Mobile',10000)
p4 = Product('Laptop',40000)

print(Product.discount)
print(p3.price)
print(p4.price)