class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

acc = BankAccount("Nikhil", 5000)
acc.deposit(1500)
acc.withdraw(2000)
acc.withdraw(6000)
