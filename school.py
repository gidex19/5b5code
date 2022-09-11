import pickle
import random


file = open("school.txt", "rb")

data = file.read()
pickled_data = pickle.loads(data)

print(pickled_data)
print(type(pickled_data))



# dict = {
#     '0123':{
#         "name": full_name,
#         "english_score": english_score,
#         "maths_score:" maths_score
#     }
# }


while True:
    print("enter 1 to add a student")
    print("enter 2 to search a  student")
    print("enter 3 to quit program")
    choice = int(input("enter your choice: "))
    if choice == 1:
        mat_no = ''
        full_name = input("Enter your full name: ")
        english_score = int(input("Enter your english score: "))
        maths_score = int(input("Enter your maths score: "))
        for i in range(4):
            r = random.randint(0, 9)
            mat_no += str(r)
        print(f"mat_no: {mat_no}")    
        pickled_data[mat_no] = {
            "name": full_name,
            "english_score": english_score,
            "maths_score": maths_score
        }
        print(pickled_data)
    elif choice ==2:
        user_id = input("enter your matric number: ")
        student_dict =  pickled_data.get(user_id)
        if student_dict == None:
            print("Sorry!!! This student does not exist")
        else:
            st_name = student_dict["name"]
            eng_score = student_dict["english_score"]
            math_score = student_dict["maths_score"]
            print(f"Hello {st_name}\nEnglish score ==> {eng_score}\nMaths score ==> {math_score}")    
        # print(student_dict)
        break
    else:
        file.close()
        file = open("school.txt", "wb") 
        pickle.dump(pickled_data, file)
        print("exitting out of the program")
        break




#write a program that will asjk the user for the name of a 
# fruit and then store this data in a list which will later be stored in
# a .txt file in bytes format.

# the program should run repeatedly such that the user will enter 1 to add a fruit
# and anything else to end the program. 



# write a program that will ask a patient for his/her full_name, ward and then ailment
# and then store this data in a dictionary which will later be stored in a .txt file in
# bytes format using pickle.

#the program should run repeatedly such that the user will enter 1 to add a patient,
#enter 2 to search a patient and enter anything else to end the program.


