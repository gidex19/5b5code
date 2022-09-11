import pickle

# my_list = []
# file = open("students.txt", "wb")

# while len(my_list)<5:
#     students_name = input("enter your name: ")
#     my_list.append(students_name)


file = open("school.txt", "wb")

# pickle.dump(my_list, file )
# print("data pickled successfully")

# my_dict = {
#     "0123": {
#         "name": "Uche",
#         "courses": {
#             "english": 50,
#             "maths": 90,
#             "chemistry": 70
#         },
#         "traits": ["smart", "attentive", "focused"]
#     },
#     "0124": {
#         "name": "Dave",
#         "courses": {
#             "english": 50,
#             "maths": 90,
#             "chemistry": 70
#         },
#         "traits": ["smart", "attentive", "focused"]
#     }
# }

# my_dict = {
#     "country": "Nigeria",
#     "states": ["abuja", "lagos", "kogi","ogun"],
#     "traits": {
#         "good": ["lively", "funfilled", "rich culture"],
#         "bad": {
#             "bad": "a crazy place",
#             "very bad": " a really really bad place",
#             "chaotic": " a chaotic place"
#         }

#     }
# }

#print the last state
#print the "very bad" string
#print the second good item




# print(my_dict["0123"]["traits"][-1])
# for item in my_dict:
#     my_dict[item]
#     # for i in my_dict[item]:
#     #     print(my_dict[item][i])

# file = open("students.txt", "rb")
# data = file.read()
# pickled_data = pickle.loads(data)

# print(pickled_data)
# print(data)
# print(type(data))
# print(type(pickled_data))
