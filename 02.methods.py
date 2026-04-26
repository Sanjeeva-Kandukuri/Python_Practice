# Methods
# Example: Adding a Method

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product:{self.name},Price:{self.price},Quantity:{self.quantity}")

    def calculate_total_price(self):
        return self.price * self.quantity
    
product1 =Product("Tablet",30000,2)
print("Total Price:",product1.calculate_total_price())



# Types of Methods
# (a) Instance Methods

# Example:-

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def apply_discount(self,discount):
        self.price -= self.price * (discount/100)

p1 = Product('Laptop',50000)
p1.apply_discount(10)
print(p1.price)


# (b) Class Methods
# Example:-

class Product:
    discount = 10

    @classmethod
    def set_discount(cls,new_discount):
        cls.discount = new_discount         # Modifies class attribute

Product.set_discount(15)
print(Product.discount)



# (c) Static Methods
# Example:

class Product:
    @staticmethod
    def is_expensive(price):
        return price > 30000
    
print(Product.is_expensive(50000))
print(Product.is_expensive(20000))



# Real-world example of an E-commerce Product class with attributes and methods:

class Product:
    discount = 5

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self):
        self.price -= self.price * (self.discount/100)


    @classmethod
    def update_discount(cls,new_discount):
        cls.discount = new_discount

    @staticmethod
    def is_available(quantity):
        return quantity > 0
    
p1 = Product("Laptop",50000,10)
p2 = Product("Phone",20000,5)


p1.apply_discount()
print(p1.price)


Product.update_discount(10)
p2.apply_discount()
print(p2.price)

print(Product.is_available(p1.quantity))