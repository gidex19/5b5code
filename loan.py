import pickle
import random

# a loan program that will
# 1. create a bank account for use
# 2. give out loan
# 3. check balance from account
# 4. transfer funds to an account
# 5. and delete account from database
# the database uses a dictionary to store the data within a .txt file 



#code to create an empty text file and dump pickled dictionary in it
# empty_dict = {}
# file = open("bank.txt", "wb")
# pickle.dump(empty_dict, file)


file = open("bank.txt", "rb")
data = file.read()
dict_data  = pickle.loads(data)
# print(dict_data)
file.close()

def write_to_file(dict_object):
    file = open("bank.txt", "wb")
    pickle.dump(dict_object, file)
    file.close()

def transfer_funds(dict_data):
    senders_acct = input("enter senders account number")
    r_acct = input("enter recievers account number")
    amount = int(input("enter the amount"))
    if amount > 0:
        if dict_data.get(senders_acct) and dict_data.get(r_acct):
            senders_balance = dict_data[senders_acct]["balance"]
            r_balance = dict_data[r_acct]["balance"]
            if senders_balance >= amount:
                dict_data[senders_acct]["balance"] -= amount
                dict_data[r_acct]["balance"] += amount
                write_to_file(dict_data)
                print("account credited successfully")
            else:
                print("insufficient funds")
                return 
        else:
            print("incorrect account number")
    else:
        print("transfer amount too low")

while True:
    print("enter 1 to create account: ")
    print("enter 2 to give out loans: ")
    print("enter 3 to check account balance: ")
    print("enter 4 to transfer funds: ")
    print("enter 5 to delete account: ")
    print("enter anything else to end program: ")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        bank_no = ''
        full_name = input("what is your full name: ").lower()
        gender = input("what is your gender: ").lower()
        for i in range(6):
            r = random.randint(0, 9)
            bank_no += str(r)
        dict_data[bank_no] = {
            "full_name": full_name,
            "gender": gender,
            "acct_no": bank_no,
            "debt": 0,
            "balance": 5000
        }
        write_to_file(dict_data)
        print(f"bank no: {bank_no}")
        print("account created successfully")

    elif choice == 2:
        acct_no = input("enter your account number: ")
        amount = int(input("enter the amount you want to borrow: "))
        if dict_data.get(acct_no):
            dict_data[acct_no]["debt"] += amount
            dict_data[acct_no]["balance"] += amount
            print(f"loan of {amount} granted succesfully")
            write_to_file(dict_data)
        else:
            print("invalid account number")
    elif choice == 3:
        acct_no = input("enter account number: ")
        if dict_data.get(acct_no):
            fullname = dict_data[acct_no]["full_name"]
            
            debt = dict_data[acct_no]["debt"]
            balance = dict_data[acct_no]["balance"]
            print(f" Hello {fullname} - {acct_no}")
            print(f" Your account balance is N{balance}")
            print(f" And Your Debt is N{debt}")
        else:
            print("invalid account number")
        
    elif choice == 4: 
        transfer_funds(dict_data= dict_data)    
    elif choice == 5:
        acct_no = input("enter acciount number: ")
        if dict_data.get(acct_no):
            dict_data.pop(acct_no)
            write_to_file(dict_data)
            
            print("Account deleted successfully")

        else:
            print("invalid account details")
    else:
        break   
# 850969
# 298353