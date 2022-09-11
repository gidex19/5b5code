# class Person():
#     def __init__(self, name, id) -> None:
#         self.name = name
#         self.id = id


# class Bank:

#     balance = 0

#     def increase_balance(self):
#         Bank.balance += 100


# u1 = Bank()
# u1.increase_balance()
# u1.increase_balance()
# print(u1.balance)
# u2 = Bank()
# print(u2.balance)


class Bank:

    debt = 0    
    def __init__(self, balance) -> None:
        self.balance = balance
        print("hello world")
    def increase_balance(self):
        self.balance += 100
    def debt_func(self):
        Bank.debt += 100
        



u1 = Bank(0)
u1.increase_balance()
u1.increase_balance()
u1.debt_func()
print(u1.balance)
print(u1.debt)

u2 = Bank(0)
print(u2.debt)
# u2.increase_balance()
# print(u2.balance)
# print(u1.balance)

# print(Bank.balance)
