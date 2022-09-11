numbers = [20, 30, 40, 50]


# for i,j in enumerate(num):
#     print("----------------------------")
#     print(f"index is {i} and the value is {j}")
#     num[i] =  j + 10
#     print(f"my list now: {num}")
#     print("****************************")

# syntax:   map(function, list)

map_obj = map(lambda num: num + 10, numbers)

print(list(map_obj))