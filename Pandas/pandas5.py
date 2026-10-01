"""5.	Create a dictionary containing:
Order_ID
Customer
Product
Quantity
Price
Discount
Create a DataFrame and calculate:
Final Amount = Quantity × Price − Discount
Then display:
•	All orders 
•	Orders above ₹5,000 
•	Highest-value order 
•	Average order value
"""
import pandas as pd
dict = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Yash", "Sid", "Trisha", "Aditi", "Arjun"],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Quantity": [10, 25, 30, 20, 25],
    "Price": [50000, 300, 1000, 15000, 2000],
    "Discount": [5000, 250, 300, 1500, 400]
}
df = pd.DataFrame(dict)

df["Final_Amt"] = df["Quantity"] * df["Price"] - df["Discount"]
print("Final Amount for each order:")
print(df["Final_Amt"])

print("\nAll Orders:")
print(df)

print("\nOrders above ₹5,000:")
print(df[df["Final_Amt"] > 5000])

print("\nHighest-value order:")
print(df[df["Final_Amt"] == df["Final_Amt"].max()])

avg_order_value = df["Final_Amt"].mean()
print(f"\nAverage Order Value: {avg_order_value}")