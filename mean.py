
numbers = []
while True:
    print("Enter a to add a number to the list \n or Enter c to calculate the mean")
    user_choice = input("Enter choice : ").lower()
    if user_choice == "a":    
        user_input = int(input("Enter the number to be added : "))
        numbers.append(user_input)
    elif user_choice == "c":
        no_items = len(numbers)
        total = 0
        for i in numbers:
            total += i
        mean = total/no_items 
        print(f"the numbers list: {numbers}")
        print(f"there are {no_items} numbers in the list")
        print(f"the mean of the numbers is: {mean}")
        break
    else:       
        break