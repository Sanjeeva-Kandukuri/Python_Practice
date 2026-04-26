# Constructors
# Example: Constructor

class Product:
    # Constructor
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product:{self.name},Price:{self.price},Quantity:{self.quantity}")


# Create an object   
product1 = Product("HeadPhones",1500,10)
product1.display_info()