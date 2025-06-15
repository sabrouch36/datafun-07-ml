# account.py
"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Add amount to the account balance."""
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from the account balance if funds are sufficient."""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
        return self.balance

# Only run this if the file is executed directly (not imported)
if __name__ == "__main__":
    acc = Account("Sabri", Decimal('100.00'))
    print("After deposit:", acc.deposit(Decimal('50.00')))     # 150.00
    print("After withdrawal:", acc.withdraw(Decimal('30.00'))) # 120.00
    print("Trying to withdraw too much:", acc.withdraw(Decimal('200.00')))  # warning
