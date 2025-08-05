# Define getter and setter instance variables in this class for all instance variables
# - The '__rooms' setter should only change the instance variable if the new value is greater than 0
# - The '__post_code' setter should only change the instance variable if the new value has a length less than 10
class House:
    def __init__(self, rooms: int, street: str, post_code: str):
        self.__rooms = rooms
        self.__street = street
        self.__post_code = post_code
