# ==============================================================================
# Name: TEJASW
# USN: 25BTRAD096
# Lab Exercise 14: Bank account system using OOP
# Lab Exercise 15: Library management system
# Lab Exercise 16: Dice simulator using random module
# ==============================================================================

import random

# ------------------------------------------------------------------------------
# Lab Exercise 14: Bank account system using OOP
# ------------------------------------------------------------------------------
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn!")
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


def run_bank():
    name = input("Enter account holder's name: ")
    balance = float(input("Enter initial balance: "))
    b = Bank(name, balance)

    while True:
        print("\n1.Deposit 2.Withdraw 3.Display 4.Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            b.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            b.withdraw(amount)
        elif choice == '3':
            b.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")


# ------------------------------------------------------------------------------
# Lab Exercise 15: Library management system
# ------------------------------------------------------------------------------
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued!")
        else:
            print("Book not available!")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned!")
        else:
            print("Book was not issued!")

    def display(self):
        print(self.title, "-", "Available" if self.available else "Issued")


def run_library():
    b1 = Book(input("Enter title of book : "))
    b1.display()

    while True:
        print("\n1.Issue 2.Return 3.Display 4.Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            b1.issue()
        elif choice == '2':
            b1.return_book()
        elif choice == '3':
            b1.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")


# ------------------------------------------------------------------------------
# Lab Exercise 16: Dice simulator using random module
# ------------------------------------------------------------------------------
def run_dice_simulator():
    n = int(input("Enter number of dice: "))
    rolls = int(input("Enter number of times to roll: "))

    frequency = {}

    for i in range(rolls):
        dice = []
        for j in range(n):
            dice.append(random.randint(1, 6))

        total = sum(dice)
        print("Dice:", dice, "Total:", total)
        frequency[total] = frequency.get(total, 0) + 1

    print("\n--- FREQUENCY COUNTER ---")
    for total, count in frequency.items():
        print(total, ":", count)


if __name__ == "__main__":
    print("--- Bank Account System (Lab Exercise 14) ---")
    run_bank()

    print("\n--- Library Management System (Lab Exercise 15) ---")
    run_library()

    print("\n--- Dice Simulator (Lab Exercise 16) ---")
    run_dice_simulator()
