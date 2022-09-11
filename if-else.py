
print("what time of the day is it?")
print("enter 1 for morning \n enter 2 for afternoon \n enter 3 for night")
our_input = int(input("what time of the day is it? "))
if our_input == 1:
    print("Good morning")
elif our_input == 2:
    print("Good afternoon")
elif our_input == 3:
    print("Good night")
else:
    print("wrong input")        


# 0-29 f
# 30 - 40 e 
# 41 - 49 d 
# 50 - 59 c 
# 60 - 80 b
# 81 - 100 a 
# else invalid

# users = []
# first_user = int(input("first user: enter your age : "))
# second_user = int(input("second user: enter your age : "))
# third_user = int(input("third user: enter your age : "))
# users.append(first_user)
# users.append(second_user)
# users.append(third_user)

# youngest = min(users)
# eldest = max(users)
# print(youngest)
# print(eldest)
# # print(users[-1])


my_name = ["leonard", "uche", "nwax", "imole"]
scores = [10, 20, 40, 35]

newlist = [score + 10 for score in scores if score <= 20 ]

print(newlist)