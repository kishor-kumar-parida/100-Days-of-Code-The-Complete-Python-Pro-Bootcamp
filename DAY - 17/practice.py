# Building class
class User:
    # Constructor
    def __init__(self, user_name, user_id):
        print("welcome")
        self.name = user_name
        self.id = user_id
        self.followers = 0
        self.following = 0

    # methods
    def follow(self, user):
        user.followers += 1
        self.following += 1


# objects
user_1 = User("kishor", "1")
user_2 = User("som", "2")

# calling methods
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# # without constructor

# user_1 = User()
# user_1.name = "kishor"
# user_1.id = 1
# print(user_1.name)
# print(user_1.id)


# # with constructor

# user_2 = User("som", 2)
# print(user_2.name)
# print(user_2.id)
# print(user_2.followers)
