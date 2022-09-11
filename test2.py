# import platform
mylist = [1,2,3,4,5,6,7,8]

# print(platform.dir())
def print_name(dname):
    
    # a function to print a name
    

    print(f"hello {dname}")

# print_name.__doc__ = "a new function"
def calc_age(year):
    return 2022 - year    

y = print_name("harry")
# x = .__dir__()   
print(help(print_name))

# len()
# __len__()