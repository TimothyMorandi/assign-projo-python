"""Create a python class called BankAccount with attributes like account_number, balance,
date_of_opening and customer_name, and methods like deposit, withdraw,
check_balance and customer_details
i. The deposit method should return the amount deposited
ii. The withdraw method return insufficient balance if account balance is less than amount to
be withdrawn else it should return the amount that has been withdrawn.
iii. The check_balance method should print the current balance.
iv. The customer_details method should print customer name, account number, date of
account opening and balance
Create an instance of the BankAccount class to represent a bank account. Perform the
following operations: make a deposit, withdraw funds, and display the account information
for the created bank account instance.
"""
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self):
        depo = input("Enter the amount you want to deposit: ")
        depo = float(depo)  # Convert input to a float
        self.balance += depo
        return f"You have deposited: {depo}"

    def withdraw(self):
        withdraw = input("Enter the amount: ")
        if withdraw.isdigit():
            withdraw = float(withdraw)  # Convert input to a float
            if self.balance < withdraw:
                return "Insufficient balance"
            else:
                self.balance -= withdraw
                return f"You have withdrawn {withdraw}"
        else:
            return "Invalid input. Please enter a valid amount."

    def check_balance(self):
        return f"Your current balance is {self.balance}"

    def customer_details(self):
        print(f"Customer name: {self.customer_name}")
        print(f"Account no: {self.account_number}")
        print(f"Date of opening: {self.date_of_opening}")
        print(f"Your balance: {self.balance:.2f}")

# Example usage:
customer = BankAccount(10127, 1000000, "05-07-2022", "Timothy Morandi")
customer.customer_details()
print(customer.deposit())
print(customer.withdraw())
print(customer.check_balance())