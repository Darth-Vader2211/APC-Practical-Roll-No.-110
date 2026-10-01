"""7.	A retail shop maintains sales information in a Python dictionary containing Product_ID, Product_Name, Category, Price, and Quantity.
Write a Python program to:
1.	Convert the dictionary into a Pandas DataFrame. 
2.	Add a new column Total_Sales. 
3.	Calculate the total sales using Price × Quantity. 
4.	Display products with sales greater than ₹10,000. 
5.	Find the product with maximum sales. 
6.	Calculate the average sales.
"""
import pandas as pd

sales_info = {
    "Product_ID" : [101, 102, 103, 104],
    "Product_Name": ["Laptop", "Avast Antivirus", "Windows 11 Home", "Monitor"],
    "Category": ["Hardware", "Software", "Software", "Hardware"],
    "Price" : [75000, 5000, 10000, 8000],
    "Quantity" : [50, 25, 100, 30]
}

df = pd.DataFrame(sales_info)
print(df)

print("\nAfter inserting a new Column as Total_Sales-----")
df.insert(5,"Total_Sales", df["Price"] * df["Quantity"])
print(df)

print("\nProducts with sales greater than 10000 are : ")
print(df["Total_Sales"] > 10000 )

max_prod_sales = df["Product_Name"] == df["Total_Sales"].max()
print("Product with maximum sales : ", max)