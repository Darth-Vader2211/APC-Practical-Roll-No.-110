class BankAccount:
    def calculate_interest(self, amount):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        return amount * 0.04

class CurrentAccount(BankAccount):
    def calculate_interest(self, amount):
        return amount * 0.02

class FixedDepositAccount(BankAccount):
    def calculate_interest(self, amount):
        return amount * 0.07

accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

amount = 100000

for account in accounts:
    print("Interest:", account.calculate_interest(amount))