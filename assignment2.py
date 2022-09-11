import pickle
import random
# empty_dict = {}

# the_file = open("patients.txt", "wb")
# pickle.dump(empty_dict, the_file)


the_file = open("patients.txt", "rb")
data = the_file.read()
converted_dict = pickle.loads(data)

while True:
    print("enter 1 to add a patient\nenter 2 to search a patient\nenter 3 to remove a patient\nenter anything else to end program")
    choice = int(input("enter your choice: "))
    if choice == 1:
        patient_id = ''
        full_name = input("enter your full name: ")
        ward = input("enter your ward: ")
        ailment = input("enter your failment: ")
        for i in range(4):
            r = random.randint(0, 9)
            patient_id += str(r)

        converted_dict[patient_id] = {
            "full_name": full_name,
            "ward": ward,
            "ailment": ailment
        }    

    elif choice == 2:
        pat_id = input("enter the patient\'s ID: ")
        patient = converted_dict.get(pat_id)
        if patient == None:
            print("invalid patient ID")
        else:
            print(patient)    
    elif choice == 3:
        pat_id = input("enter the patient\'s ID: ")
        if converted_dict.get(pat_id):
            converted_dict.pop(pat_id)
            print("patient record has been deleted successfully")
        else:
            print("this patient does not exist")    
    else:

        the_file.close()
        the_file = open("patients.txt", "wb")
        pickle.dump(converted_dict, the_file)
        print("program ended successfully")

        break    


"""

{
    "10123": {
        "full_name": data,
        "ward": data,
        "ailment": data
    },
    "10123": {
        "full_name": data,
        "ward": data,
        "ailment": data
    },
    "10123": {
        "full_name": data,
        "ward": data,
        "ailment": data
    },
    "
}

"""

