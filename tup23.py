#23.	Store item prices in a tuple and calculate:
#	•	Total bill 
#	•	Average price 
#	•	Highest-priced item 
#	•	Lowest-priced item

prices = (85000, 45000, 3000, 5000, 1200)

total_bill = sum(prices)
avg_price = total_bill / len(prices)
highest_price = max(prices)
lowest_price = min(prices)

print("Item Prices:", prices)
print(f"Total bill: ₹{total_bill}")
print(f"Average price: ₹{avg_price:.2f}")
print(f"Highest-priced item: ₹{highest_price}")
print(f"Lowest-priced item: ₹{lowest_price}")
