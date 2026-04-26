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

    