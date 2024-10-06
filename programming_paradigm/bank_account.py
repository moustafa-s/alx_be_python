# bank_account.py


class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds are available."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
