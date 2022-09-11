
import pickle

file = open("hellox.txt", "rb")

# mydict = {
#     'name': "univel",
#     'class': "backend",
#     'duration': 2
# }

# pickle.dump(mydict, file)
# print("done")

data = file.read()

print(f"type of data: {type(data)}")

pickled_data = pickle.loads(data)
print(f"type of data: {type(pickled_data)}")
print(pickled_data)