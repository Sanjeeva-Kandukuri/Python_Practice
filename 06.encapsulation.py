# 1.Public Attributes
# Example of a Public Attribute (username)

class User:
    def __init__(self,username):                # -----> Public attribute
        self.username = username

# Creating an object
user1 = User("Jyothi")

# Accessing public attribute
print(user1.username)


# Modifying public attribute
user1.username = "Sanjeev"
print(user1.username)




# 2.Protected Attributes
# Example of a Protected Attribute (_otp)

class User:
    def __init__(self,username,otp):
        self.usernamre = username          # Public attribute
        self._otp = otp                    # Protected attribute


# Creating an object
user2 = User("Salman", "123456")

# Accessing public attribute
print(user2._otp)

# Modifying public attribute (not recommended, but works)
user2._otp = "654321"
print(user2._otp)


# Using Protected Attributes in a Subclass

class Admin(User):
    def show_otp(self):
        return f"Admin can see OTP: {self._otp}"
    
admin1 = Admin("admin_user", "999999")
print(admin1.show_otp())


# Protected attributes should ideally be modified using setter methods instead of direct modification.

# Setter Method
# Example:-

class User:
    def __init__(self,username, otp):
        self.usdrname = username 
        self._otp = otp

    def set_otp(self, new_otp):
        self._otp = new_otp

    def get_otp(self):
        return self._otp
    
user3 = User("Sanjeeva", "123456")

user3.set_otp("654321")
print(user3.get_otp())



# 🔹 Example 2: Setter with Validation (Very Important ⭐)


class User:
    def __init__(self,username, otp):
        self.username = username 
        self._otp = otp
    
    def set_otp(self, new_otp):
        if len(new_otp) == 6 and new_otp.isdigit():
            self._otp = new_otp
        
        else:
            print("Invalid OTP! must be 6 digits.")

    def get_otp(self):
        return self._otp
    
user1 = User("Mamatha", "123456")

user1.set_otp("999")              # ❌ Invalid
user1.set_otp("987654")           # ✔ Valid

print(user1.get_otp())


# 🔹 Example 3: Real-life Example (Bank Account 💰)

class BankAccount:
    def __init__(self,balance):
        self._balance = balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount

        else:
            print("Balance cannot be negative!.")

    def get_balance(self):
        return self._balance

user1 = BankAccount(1000)

user1.set_balance(-500)
user1.set_balance(2000)

print(user1.get_balance())


# 🔹 Example 4: Using Subclass (like your Admin example 👇)


class User:
    def __init__(self,username,otp):
        
        self.username = username 
        self._otp = otp

    def set_otp(self, new_otp):
        self._otp = new_otp

class Admin(User):
    def show_otp(self):
        return f"Admin can see OTP:{self._otp}"

admin1 = Admin("admin_user", "123456")

admin1.set_otp("999999")
print(admin1.show_otp())



# 3.Private Attributes in Python
# Example of a Private Attribute (__password)


class User:
    def __init__(self,username,password):
        self.username = username     # Public attribute 
        self._password = password    # Private attribute

user1 = User("Alice", "123456")

print(user1._password)


# Accessing Private Attributes Using Getter and Setter Methods

class User:
    def __init__(self,username,password):
        self.username = username 
        self._password = password

    
    # Getter method to retrieve password (returns masked password)
    def get_password(self):
        return "******" 
    
    # Setter method to update password with validation
    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Error: Password must be at least 6 characters long.")     

        else:
            self._password = new_password
            print("Password updated successfully") 

# Creating a user object
user1 = User("Alice", "secure123")

# Accessing password securely
print(user1.get_password())


# Updating password securely
user1.set_password("123")
user1.set_password("newSecurePass")
# print(user1._User__password)




# # 7. Complete Encapsulation Example (Public, Protected,and Private Attributes)


class User:
    def __init__(self,username,password,otp):
        self.username = username
        self._otp = otp
        self.__password = password
    
    def get_password(self):
        return "******"
    
    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Error: Password must be at least 6 characters long.")

        else:
            self.__password = new_password
            print("Password updated successfully")


    def get_otp(self):
        return self._otp
    
    def set_otp(self,new_otp):
        self._otp = new_otp
        print("OTP updated successfully")

user1 = User("Alice", "secure123", "123456")

print(user1.username) 
user1.username = "Bob"
print(user1.username)

print(user1.get_otp())
user1.set_otp("987654")
print(user1.get_otp())

print(user1.get_password())
user1.set_password("newPass123")


