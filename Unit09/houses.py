class House:
    def __init__(self, bedrooms:int, bathrooms:int, address:str):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.address = address

def newhouse():
    inbeds = input("Enter the number of bedrooms you want: ")
    if inbeds == "stop":
        return
    inbaths = input("Enter the number of bathrooms you want: ")
    if inbaths == "stop":
        return
    inaddress = input("Enter the address you want: ")
    if inaddress == "stop":
        return

    return House(int(inbeds), int(inbaths), inaddress)

print("Say stop to end the program")

while True:
    house = newhouse()
    print(house.bedrooms)
    print(house.bathrooms)
    print(house.address)