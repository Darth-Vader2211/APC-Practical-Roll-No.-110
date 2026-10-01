"""3.	Create a dictionary containing:
Product ID
Product Name
Category
Price
Quantity
Convert it into a DataFrame.
Calculate:
Total Amount = Price × Quantity
Then find the product having the highest total sales.
"""
import pandas as pd
dict = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Audio"],
    "Price": [50000, 500, 1000, 15000, 2000],
    "Quantity": [10, 50, 30, 20, 25]
}
df = pd.DataFrame(dict)

df["Total_Amount"] = df["Price"] * df["Quantity"]
highest_sold_product = df[df["Total_Amount"] == df["Total_Amount"].max()]

print("Product Data:")
print(df)

print("\nTotal Amount for each product:")
print(df["Total_Amount"])

print("\nProduct with the highest total sales:")
print(highest_sold_product)