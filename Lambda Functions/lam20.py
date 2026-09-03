products = [
    ("Laptop", 50000, 2),
    ("Mouse", 800, 5),
    ("Keyboard", 1500, 2),
    ("Monitor", 12000, 3)
]


def total_value(product):
    return product[1] * product[2]


# a) Calculate total value
values = list(
    map(lambda product: (
        product[0],
        total_value(product)
    ), products)
)

# b) Products costing more than 1000
expensive = list(
    filter(lambda product: product[1] > 1000, products)
)

# c) Sort according to total value
sorted_products = sorted(
    products,
    key=lambda product: total_value(product)
)

print("Total values:", values)
print("Products above 1000:", expensive)
print("Sorted products:", sorted_products)