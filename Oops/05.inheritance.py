class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def post_photo(self):
        print(f"{self.username} posted a photo.")

    def follow(self, other_user):
        print(f"{self.username} followed {other_user.username}.")

user1 = User("Sanjeeva","s@gmail.com")
user2 = User("Jyothi","j@gmail.com")

user1.post_photo()
user1.follow(user2)




# Types of Inheritance (with Instagram Examples)
# 1. Single Inheritance

class VerifiedUser(User):
    def __init__(self,username,email,badge_color):
        super().__init__(username,email)
        self.badge_color = badge_color

    def go_live(self):
        print(f"{self.username} is going live.")


user1 = VerifiedUser("Sanjeeva","s@gmail.com","Blue")
user1.post_photo()
user1.go_live()



# 2. Multilevel Inheritance
# Example: Influencer


class Influencer(VerifiedUser):
    def __init__(self,username,email,badge_color,niche):
        super().__init__(username,email,badge_color)
        self.niche = niche

    def promote_brand(self, brand):
        print(f"{self.username} is promoting {brand}.")

influencer1 = Influencer("Pallavi","p@gmail.com","Green","Fitness")

influencer1.post_photo()
influencer1.go_live()   
influencer1.promote_brand("Nike")


# 3. Hierarchical Inheritance
# Example: BusinessUser and Creator

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}, Email: {self.email}")

class BusinessUser(User):
    def __init__(self,username,email,business_name):
        super().__init__(username,email)
        self.business_name = business_name

    def view_insights(self):
        print(f"{self.username} is viewing business insights.")

class Creator(User):
    def __init__(self,username,email,content_type):
        super().__init__(username,email)
        self.content_type = content_type

    def monetize_content(self):
        print(f"{self.username} is monetizing {self.content_type} content.")


business_user1 = BusinessUser("Mamatha","m@gmail.com","Alice Crop")
creator1 = Creator("Ravi","r@gmail.com","Video")


business_user1.display_info()
business_user1.view_insights()

creator1.display_info()
creator1.monetize_content()


# 4. Multiple Inheritance
# Example: HybridUser

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username:{self.username}, Email:{self.email}")


class Analtics:
    def track_engagement(self):
        print("Track Engagement...")

class HybridUser(User, Analtics):
    def __init__(self,username,email):
        super().__init__(username,email)

    def hybrid_action(self):
        print(f"{self.username} uses hybrid features.")

h_user = HybridUser("Charlie789","charlie789@gmail.com")
h_user.display_info()
h_user.track_engagement()

h_user.hybrid_action()
