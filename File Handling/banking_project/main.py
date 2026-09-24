from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_loan

account = create_account("Amit", 101, 10000)

print("Account Holder:", account["name"])
print("Account Number:", account["account_no"])
print("Balance:", get_balance(account))

deposit(account, 5000)

print("\nAfter Deposit:", get_balance(account))

withdraw(account, 2000)

print("After Withdrawal:", get_balance(account))

interest, total = calculate_loan(50000, 8, 2)

print("\nLoan Interest:", interest)
print("Total Loan Amount:", total)