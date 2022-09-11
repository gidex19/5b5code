import pickle
import os

# os.path.isfile()

# write_file = open("scores.txt", "wb")
# student_name = input("what is your full name: ")
# score = int(input("what is your score: "))
# my_dict = {
#     "name": student_name,
#     "score": score,
# }
# pickle.dump(my_dict, write_file)
# write_file.close()

# # read_file = open("scorez.txt", "rb")
# with open("scorez.txt", "rb") as read_file:
#     raw_data = read_file.read()
# pickled_data = pickle.loads(raw_data)

# print(type(pickled_data))
# print(pickled_data)



write_file = open("scores.txt", "rb+")
student_name = input("what is your full name: ")
score = int(input("what is your score: "))
my_dict = {
    "name": student_name,
    "score": score,
}
pickle.dump(my_dict, write_file)
# raw_data = write_file.read()
# pickled = pickle.loads(raw_data)
pickle.load()
write_file.close()

read_file = open("scores.txt", "rb")
data = read_file.read()
pickled_data = pickle.loads(data)
print(pickled_data)