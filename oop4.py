import oop5
# class User:
#     def __init__(self, fname, lname, email) -> None:
#         self.fname = fname
#         self.lname = lname
#         self.email = email
    
#     def describe(self):
#         print(f"My name is {self.lname} {self.fname}\ncontact me at {self.email} ")


# class Patients(User):
#     pass 

# p1 = Patients("Daniel", "Uzor", "daniel@gmail.com" )


# p1.describe()




class User:
    def __init__(self, fname, lname, email) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
    
    def describe(self):
        print(f"My name is {self.lname} {self.fname}\ncontact me at {self.email} ")



class Patients(User):
    def __init__(self, fname, lname, email, location, ward) -> None:
        super().__init__(fname, lname, email)
        self.location = location
        self.ward = ward

    def describe(self):
        print(f"My name is {self.lname} {self.fname}\ncontact me at {self.email}\n I stay at {self.location} ")

    # def __repr__(self) -> str:
    #     return super().__repr__()
    
p1 = Patients("Daniel", "Uzor", "daniel@gmail.com", "Yaba", "A" )

print(p1)
# print(p1.location)







"""

i. create a automobile class that has attributes called makeup, color and cost 
ii. create another class called Vehicle that inherits from the automobile class
 and adds two extra instance attributes called brandname and origin.

iii. add an instance method within the vehicle class called describe_vehicle that 
    prints out a short description the vehicle class/object


"""