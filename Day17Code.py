class User:

    # Initializes starting values
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def to_string(self):
        return f"Username: {self.username} Password: {self.id} Followers: {self.followers} Following: {self.following}"
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("002", "oscar")
user2 = User("003", "julianna")
# user1.id = "001"
# user1.username = "oscar"

print(user1.to_string())
print(user2.to_string())

user2.follow(user1)

print(user1.to_string())
print(user2.to_string())

