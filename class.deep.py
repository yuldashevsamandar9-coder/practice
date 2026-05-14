'''
Class deep diving
(1) Encapsulation
(2) Inheritence
(3) Polimorhism

'''
# Encapsulation > public, private, procted
# public __private (2 ta dunder quyiladi), _procted (1 ta dunder chiziq quyiladi) # _
print("===== Encapsulation ====")


class Account():
    # state
    description = "Thes is bank account"

    # constructor

    def __init__(self, amount, owner):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"The owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new__owner):
        self.__owner = new__owner


my_account = Account(1000, "SAM")
my_account.get_balance()
my_account.deposit(3000)
my_account.withdraw(400)
my_account.get_balance()

print("------")
my_account.amount = 4000000
my_account.get_balance()
my_account.holder = "Neo"

try:
    result = my_account.__amount
    print("result:", result)

except Exception as err:
    print("No target state found err")
account__owner = my_account.holder
print("account__owner:", account__owner)
