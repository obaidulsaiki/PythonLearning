# if we put a variable outside of a function, it is called global variable
# global variable can be used in any function
# if we want to change the value of a global variable we have to do something extra
balance = 0


def main():
    print("Balance:   ", balance)
    deposit(1000)
    withdraw(500)
    print("New Balance:   ", balance)


def deposit(amount):
    global balance  # we have to declare the variable as global to change the value of the global variable
    balance += amount


def withdraw(amount):
    global balance
    balance -= amount


class Account:
    def __init__(self):
        self._balance = 0

    @property
    def getBalance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


def main2():
    account = Account()
    # to call the function of a class we have to call it with dot notation and like a variable
    print(account.getBalance)
    account.deposit(1000)
    account.withdraw(500)
    print(account.getBalance)


if __name__ == "__main__":
    # main()
    main2()
