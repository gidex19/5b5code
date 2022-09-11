# with open("assign2.txt", "x") as file:
#     file.write('new file created')
#     print("hello")

file = open("hello.text", "r")
# print(file.read())
the_list = file.read().split(",")
the_list = [x for x in the_list if x!= ""]
print(the_list)
print(type(the_list))


while True:
    print("enter a to add\nand q to quit")
    choice = input("enter your choice: ")
    if choice == "q":
        print("in quit mode")
        print(the_list)
        file = open("hello.text", "w")
        for i in the_list:
            file.write(i+",")
        break
    elif choice == "a":
        food = input("enter food: ")
        the_list.append(food)
        print(the_list)
    else:
        print("wrong input")
        break

