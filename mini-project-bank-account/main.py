import os
import random

class BankAccount(object):
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = self.generate_account_number()  # Unique account number
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        self.create_transaction_file()  # Create a new file for transactions

    def generate_account_number(self):
        """Generate a unique account ID."""
        return random.randint(10000, 99999)  # Randomly generate a 5-digit account number

    def create_transaction_file(self):
        """Create a transaction file to store user transactions."""
        with open(self.filename, 'w') as file:
            file.write("Transaction History for Account ID: {}\n".format(self.accountNumber))
            file.write("Initial balance: ${:.2f}\n".format(self.balance))
            file.write("-" * 40 + "\n")

    def deposit(self, amount):
        """Deposit money into the account and record the transaction."""
        if amount > 0:
            self.balance += amount
            self.record_transaction(f"Deposited: ${amount:.2f}")
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance is available."""
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            self.record_transaction(f"Withdrew: ${amount:.2f}")
            print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def record_transaction(self, transaction):
        """Record a transaction in the user's statement file."""
        with open(self.filename, 'a') as file:
            file.write(transaction + "\n")

    def get_balance(self):
        """Return the current account balance."""
        return self.balance

    def get_account_number(self):
        """Return the account ID."""
        return self.accountNumber

    def get_username(self):
        """Return the username."""
        return self.name

    def get_account_type(self):
        """Return the account type."""
        return self.accountType

    def get_transaction_history(self):
        """Read and return the transaction history from the statement file."""
        with open(self.filename, 'r') as file:
            history = file.readlines()
        return history

# Test the BankAccount class
def main():
    # Create multiple BankAccount objects
    account1 = BankAccount("Ali", "savings")
    account2 = BankAccount("David", "chequing")

    # Perform transactions on account1
    account1.deposit(500)
    account1.withdraw(200)
    account1.withdraw(1000)  # Attempt to withdraw more than balance
    print("Account 1 Balance:", account1.get_balance())
    print("Transaction History for Account 1:")
    print("".join(account1.get_transaction_history()))

    # Perform transactions on account2
    account2.deposit(1000)
    account2.withdraw(300)
    print("Account 2 Balance:", account2.get_balance())
    print("Transaction History for Account 2:")
    print("".join(account2.get_transaction_history()))

main()