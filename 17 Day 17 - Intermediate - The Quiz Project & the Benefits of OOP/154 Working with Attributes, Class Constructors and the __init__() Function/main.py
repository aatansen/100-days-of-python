class User:
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001","Tansen")
print(user_1.username)
print(user_1.followers)

user_2 = User("002","Alahi")
print(user_2.username)