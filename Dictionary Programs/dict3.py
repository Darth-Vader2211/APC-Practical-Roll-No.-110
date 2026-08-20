#3.	Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
products = {
    "Laptop": 85000,
    "Mobile Phone": 45000,
    "Headphones": 3000,
    "Tablet": 45000,
    "Smart Watch": 5000
}
print("Original products and prices:")
for product, price in products.items():
    print(f"{product}: {price}")
    
products["RTX 5090"] = 686871

print("\nUpdated products and prices:")
for product, price in products.items():
    print(f"{product}: {price}")