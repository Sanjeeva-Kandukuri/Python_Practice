# super() Keyword
# How super() Works in Different Inheritance Types

# 1. Single Inheritance

class User:
    def __init__(self,username):
        self.username = username
        print(f"User initilized:{username}")


class VerifiedUser(User):
    def __init__(self,username,badge):
        super().__init__(username)
        self.badge = badge
        print(f"Verified initilized with badge:{badge}")

user = VerifiedUser("Sanju","Blue")


# 2. Multilevel Inheritance

class User:
    def __init__(self,username):
        print("User Initilized")
        self.username = username

class VerifiedUser(User):
    def __init__(self,username,badge):
        super().__init__(username)
        self.badge = badge
        print("VerifiedUser Initilized")

class Influencer(VerifiedUser):
    def __init__(self,username,badge,niche):
        super().__init__(username,badge)
        self.niche = niche
        print("Influencer Inilized")

influencer = Influencer("Sanjeev","Blue","Tech")


# 3. Multiple Inheritance with super() and MRO

class Analytics:
    def __init__(self):
        print("Analytics Initilized")
        super().__init__()

class Moderator:
    def __init__(self):
        print("Moderator Initilized")
        super().__init__()

class AdminUser(Analytics,Moderator):
    def __init__(self):
        print("AdminUser Initilized")
        super().__init__()

admin = AdminUser()


print(AdminUser.__mro__)


# When to Use ClassName.method(self, ...)

class Moderator:
    def show_permissions(self):
        print("Medorator permissions")


class Admin:
    def show_permissions(self):
        print("Admin permissions")

class HybridUser(Moderator, Admin):
    def show_permissions(self):
        Moderator.show_permissions(self)
        Admin.show_permissions(self)

user = HybridUser()
user.show_permissions()

print(AdminUser.__mro__)
