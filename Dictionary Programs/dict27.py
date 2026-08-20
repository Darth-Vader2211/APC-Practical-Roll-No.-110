#27.	Create a dictionary containing product names and quantities.
#Perform:
#	•	Add a product 
#	•	Update quantity 
#	•	Delete a product 
#	•	Search for a product 
#	•	Display products with quantity below 10

products = {
    "Laptop": 15,
    "Mobile Phone": 5,
    "Headphones": 8,
    "Smart Watch": 20
}

# Add a product
products["Tablet"] = 12

# Update quantity
products["Laptop"] = 18

# Delete a product
if "Smart Watch" in products:
    del products["Smart Watch"]

# Search for a product
search_prod = "Mobile Phone"
if search_prod in products:
    print(f"{search_prod} quantity: {products[search_prod]}")

# Display products with quantity below 10
print("\nProducts with quantity below 10:")
for prod, qty in products.items():
    if qty < 10:
        print(f"{prod}: {qty}")
