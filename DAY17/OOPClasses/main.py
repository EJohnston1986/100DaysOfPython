class User:
    # create initialisation values for class attributes inside this function
    # 'user_id' function parameter name for actual attribute of class 'id'
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Bert")
user_2 = User("002", "Fred")

user_1.follow(user_2)
print(user_2.followers)

