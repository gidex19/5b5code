

class Person:
    def __init__(self, name) -> None:
        self.myname = name

    def get_name(self):
        return self.__myname 

    def setters_name(self, newname):

        self.__myname = newname

# print("my global scope")


p1 = Person("Gideon")
print(p1.myname)
# # p1.setters_name("Ade") 
# print(p1.get_name())



# print(x)
# print(mylist.__dir__())




# """
# assignment:

# i.   create a class called workers
# ii.  the class should have the following instance attributes name, age, level and year_of_employment
# iii. the class should have a function to promote worker to a new level if the year_of_employment
#      is greater than 5 and demote worker if the year_of_employment is less than 5 
# iv.  the value of the 

# """

