class Customer:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class NewCustomer(Customer):
    def output_new_customer(self):
        print(self.first_name, self.last_name, self.age)

class VIPCustomer(Customer):
    def output_vip_customer(self):
        print(self.first_name, self.last_name, self.age)

customer = Customer("Steven", "Universe", "16")
new_customer = NewCustomer("Connie", "Maheswaran", "13")
vip_customer = VIPCustomer("Elon", "Musk", "54")
new_customer.output_new_customer()
vip_customer.output_vip_customer()