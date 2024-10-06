# main-0.py

import sys
from bank_account import BankAccount


def main():
    # Create a bank account with an initial balance, e.g., $100
    account = BankAccount(100)

    # Ensure there's at least one argument provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the first argument to get the command and amount if any
    command, *params = sys.argv[1].split(":")
    amount = float(params[0]) if params else None

    # Handle the 'deposit' command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")

    # Handle the 'withdraw' command
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    # Handle the 'display' command
    elif command == "display":
        account.display_balance()

    # Handle invalid commands
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()
