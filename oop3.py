

class Customer:
    """A class for custom users and their details"""
    bank_name = "Univel Bank"
    def __init__(self, fullname, acct_number, balance, pin) -> None:
        self.fullname = fullname
        self.acct_number = acct_number
        self.balance = balance
        self.pin = pin

    # def __repr__(self) -> str:
    #     return f"Customer object: {self.fullname} {self.balance}"

    def __str__(self) -> str:
        return f"Customer objectz: {self.fullname}"    
    def check_balance(self):
        """ a function that returns the balance of a user"""
        return self.balance

    def transfer(self, amount, receiver):
        """a function that transfers funds to a user"""
        pin =  int(input("enter your 4 digit pin"))
        if self.pin == pin:
            self.balance -= amount
            receiver.balance += amount
        else:
            print("wrong password")

    def change_pin(self):
        pin =  int(input("enter your 4 digit pin"))
        if self.pin == pin:
            newpin = int(input("Enter your new pin"))
            self.pin = newpin
            print("PIN changed successfully")
        else:
            print("Wrong PIN")    


    @classmethod
    def change_bank_name(cls, newname):
        """ a class method that changes the name of the customer\'s bank"""
        Customer.bank_name = newname


c1 = Customer("Ix Mo", "234355543", 5000, 1234)
# c2 = Customer("Hui Danny", "234355543", 5000, 8000)

# c2.change_pin()
print(c1)

# c1.transfer(300, c2)

# Customer.change_bank_name("Heritage Bank")
# print(help(Customer))

# print(c1.bank_name)
# print(c2.balance)

"""
i. create a class called Customer with the instance attributes fullname, acct_number, balance
ii. add a class attribute of bank_name and assign a value to it
iii. create an instance method called checkbalance that returns the balance of the customer
iv. create an instance method called transfer that transfers funds to another Customer objects.
    this function should take in amount and the reciever object
v.  create a class method that will change the name of the bank .   

"""



