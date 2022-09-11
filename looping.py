
# while True:
#     ac_balance = int(input("enter account balance: $"))
#     if ac_balance < 100:
#         print("you are still broke")
#     else:
#         print("you are rich")
#         break

# food = []

# while len(food) < 3:
#     food_item = input("enter food item to be added: ")
#     food.append(food_item)


cars = {}


while len(cars) < 4:
    car_type = input("enter type of car: ")
    car_name = input("enter name of car: ")
    cars[car_type] = car_name

print(cars)


