file = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
transactions = []

for line in file:
    type, amount = line.strip().split(",")
    amount = float(amount)

    transactions.append(amount)

    if type == "D":
        total_deposits += amount
    elif type == "W":
        total_withdrawals += amount

file.close()

final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)