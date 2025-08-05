# Fix the errors in this program
# - The setter variable should use the correct instance variable
class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    def set_password(self, old_password: str, new_password: str):
        if old_password == self.password:
            self.password = new_password
            print("UPDATED PASSWORD")
        else:
            print("INCORRECT PASSWORD!")


user = User("username", "password")
user.set_password("not_username", "new_username")
user.set_password("username", "new_username")
