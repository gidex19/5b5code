class Person:
  complexion = "dark"  
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  def namedeclarer(self,):
        print("parent nameclearer function")
          

class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        # print(super().complexion)
        self.age = age
        # super().__init__(fname, lname)
        # self.age = age
        # self.firstname = fname
        # self.lastname = lname

    def namedeclarer(self,):
        print("child nameclearer function")
        

s = Student("yemi", "lname", 9)
s.namedeclarer()
# s.printname()