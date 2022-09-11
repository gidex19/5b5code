

print("Welcome to Univel Restaurant")
name = input("What is your name:")
days = ["monday", "tuesday", "wednesday", "thursday"]

order = {}

for i in days:
    user_choice = input(f"Hello {name}, What would you love to eat on {i}:")
    order[i] = user_choice
print("Thank you for your time. \nplease confirm your order")
for i in order:
    print(f"{i} ===> {order[i]}")

