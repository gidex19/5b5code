
# x = 20
# def dsum(a, d):
    
#     return  a + d

# n = dsum(d = 10, a = 30)

# print(n)


# def country(**country):
#     decs_of_c = country["desc"]
#     print(f"{country['name']} is a {decs_of_c} country")


# country(name = "Argentina",  desc = "beautiful", population = 1000 )

# def printg():
#     print("g")

# def print_name(dname, year):
#     print(f"hello {dname}")
    
#     def print_age():
#         age = str(2022 - year)
#         print(f"You are {age} years old")
        
#     # print_age()    
#     printg()

# print_name("Alex", 1995)


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         print(f"{n} * {n-1}")
#         return  n * factorial(n-1)     

# # print(factorial(4))
def factorial(n):
    # holder = 1
    x = n
    while n > 1:
        # mult = n * (n-1)
        # x = x* (n-1)
        x *= n-1
        n-=1
    print(x)

factorial(5)

# thelist = [1,2,3,4,5,6]
# for i in thelist:
#     x = 2
# print(i)    

