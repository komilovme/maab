============================================================
🐄 1️⃣ MODEL A FARM (OOP + Inheritance)
============================================================
# ===============================
# FARM MODEL
# ===============================

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")


# Child Classes

class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age)
        self.milk_production = milk_production

    def make_sound(self):
        print(f"{self.name} says Moo!")

    def produce_milk(self):
        print(f"{self.name} produces {self.milk_production} liters of milk.")


class Chicken(Animal):
    def __init__(self, name, age, eggs_per_day):
        super().__init__(name, age)
        self.eggs_per_day = eggs_per_day

    def make_sound(self):
        print(f"{self.name} says Cluck!")

    def lay_eggs(self):
        print(f"{self.name} lays {self.eggs_per_day} eggs today.")


class Sheep(Animal):
    def __init__(self, name, age, wool_kg):
        super().__init__(name, age)
        self.wool_kg = wool_kg

    def make_sound(self):
        print(f"{self.name} says Baa!")

    def shear(self):
        print(f"{self.name} produces {self.wool_kg} kg of wool.")


# Farm Demo
def farm_demo():
    cow = Cow("Bella", 4, 10)
    chicken = Chicken("Chicko", 2, 3)
    sheep = Sheep("Dolly", 5, 5)

    animals = [cow, chicken, sheep]

    print("\n--- FARM STATUS ---")
    for animal in animals:
        print(f"\nAnimal: {animal.name}, Age: {animal.age}")
        animal.make_sound()
        animal.eat()
        animal.sleep()

    cow.produce_milk()
    chicken.lay_eggs()
    sheep.shear()

============================================================
🏦 2️⃣ BUILD A BANK APPLICATION (OOP + File Handling)
============================================================
import os

# ===============================
# ACCOUNT CLASS
# ===============================

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def __str__(self):
        return f"Account: {self.account_number}, Name: {self.name}, Balance: ${self.balance:.2f}"

    def to_file(self):
        return f"{self.account_number},{self.name},{self.balance}\n"


# ===============================
# BANK CLASS
# ===============================

class Bank:
    FILE_NAME = "accounts.txt"

    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def generate_account_number(self):
        return str(len(self.accounts) + 1001)

    def create_account(self, name, initial_deposit):
        acc_number = self.generate_account_number()
        account = Account(acc_number, name, initial_deposit)
        self.accounts[acc_number] = account
        self.save_to_file()
        print("Account created successfully!")
        print(account)

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        try:
            account = self.accounts.get(account_number)
            if not account:
                print("Account not found.")
                return
            account.deposit(amount)
            self.save_to_file()
            print("Deposit successful.")
        except ValueError as e:
            print("Error:", e)

    def withdraw(self, account_number, amount):
        try:
            account = self.accounts.get(account_number)
            if not account:
                print("Account not found.")
                return
            account.withdraw(amount)
            self.save_to_file()
            print("Withdrawal successful.")
        except ValueError as e:
            print("Error:", e)

    def save_to_file(self):
        with open(self.FILE_NAME, "w") as f:
            for acc in self.accounts.values():
                f.write(acc.to_file())

    def load_from_file(self):
        if not os.path.exists(self.FILE_NAME):
            return

        with open(self.FILE_NAME, "r") as f:
            for line in f:
                acc_number, name, balance = line.strip().split(",")
                self.accounts[acc_number] = Account(acc_number, name, balance)

    def menu(self):
        while True:
            print("\n===== BANK MENU =====")
            print("1. Create Account")
            print("2. View Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")

            choice = input("Select: ")

            if choice == "1":
                name = input("Enter name: ")
                deposit = float(input("Initial deposit: "))
                self.create_account(name, deposit)

            elif choice == "2":
                acc = input("Account number: ")
                self.view_account(acc)

            elif choice == "3":
                acc = input("Account number: ")
                amount = float(input("Deposit amount: "))
                self.deposit(acc, amount)

            elif choice == "4":
                acc = input("Account number: ")
                amount = float(input("Withdraw amount: "))
                self.withdraw(acc, amount)

            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


============================================================
🧠 MAIN CONTROLLER
============================================================
def main():
    while True:
        print("\n=========== MAIN MENU ===========")
        print("1. Farm Demo")
        print("2. Bank Application")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            farm_demo()
        elif choice == "2":
            bank = Bank()
            bank.menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


