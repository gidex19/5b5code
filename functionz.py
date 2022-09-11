
# def my_names(*namez ):

#     print(namez[0])
#     print(namez[1])
#     # print(age)


# def keywordnames(**knames):

#     print(knames)
#     print(type(knames))
#     print(knames["secondname"])
#     print(knames["lastname"])
# keywordnames(firstname = "Oz", secondname = "Ab", lastname = "fm")

# my_names(name = "ella")





# def describe(name, age, complexion):
#     print(f"My name is {name}")
#     print(f"I am {age} years old")
#     print(f"I am {complexion}")


# describe(age = 9, name= "ade", complexion = "dark")



import random

r = '9'
print(id(r))
def password_gen(n):
    r = '2'
    print(id(r))
    # for i in range(n):
    #     num = random.randint(0,9)
    #     r+= str(num)
    # print(id(r))
    # return r 

password_gen(5)
print(r)
# print(mypassword)

# print(int(random.random()* 10**5))


# print(type(6))
# for i in range(100):
#     # num = 10**6
#     print(random.randint(0, 1000))


"""
1. write a function that generates a random
 password consisting of n numbers and return this password.
 the length of the password should entered as the argument
 for the function   

2. write a function that will take in the breadth and length
   of a triangle, then calculate and return the area
   where area = 0.5*breadth*height

3. perform the following tasks

i. create a file called helperz.py
ii. write two functions within the helperz.py module.
iii. the first function to calculate the area of a rectangle
iv. the second function to calculate the area of a circle
v. create another file called main.py
vi. import the tasks.py into main.py,. rename it and then use its functions

"""