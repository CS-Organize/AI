USER_ID = 0

class User:
    def __init__(self, username):
        global USER_ID
        USER_ID += 1
        self.user_id = USER_ID
        self.username = username
        self.followers = 0
        self.following = 0
        print("Constructor called")

    def print_info(self):
        print("User ID: ", self.user_id)
        print("Username: ", self.username)
        print("Followers: ", self.followers)
        print("Following: ", self.following)

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("seunan")
user2 = User("johndoe")

user1.follow(user2)

user1.print_info()
user2.print_info()
