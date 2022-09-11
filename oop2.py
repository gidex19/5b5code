# import oop1


class Book:
    author = "Chinua Achebe"
    publisher = "IV Publishers"
    def __init__(self, name, no_of_pages, color, author ):
        
        self.name = name
        self.no_of_pages = no_of_pages
        self.color = color
        self.author = author

    def __repr__(self):
        return f"Book Object:  {self.name} {self.color}"

    def describe(self):
        print(f"{self.name}\nwritten by {self.author}\n {self.color} in color")

    @classmethod
    def changePublisher(cls, publisher ):
           Book.publisher = publisher


    # def changePub(self, publisher):
    #     Book.publisher = publisher


b1 = Book(name = "Quantitative Methods", no_of_pages = 45, color = "yellow", author = "Dan Brown")
b2 = Book("Verbal Methods", 4, "blue", "Chinua achebe" )



# b1.isExpensive = True
# Book.author = "Dan Brown" 
# print(b2.author)
# print(b1.author)
# b1.author = "Robert Greene"
# print(b1.publisher)
# Book.changePublisher("XYZ Publishers")
# b1.changePublisher("TYY")
# Book.changePub("FRT Publishers")
# b1.changePub("ABC Publishers")
# print(b1.publisher)
# print(b2.publisher)
# describe()