def calculate_units(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 500 + (units - 100) * 7
    else:
        return 1200 + (units - 200) * 10


def fixed_charge():
    return 100


def calculate_tax(amount):
    return amount * 0.05


def calculate_discount(amount):
    if amount > 5000:
        return amount * 0.10
    return 0


def final_bill(units):
    energy = calculate_units(units)
    fixed = fixed_charge()

    subtotal = energy + fixed
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)

    return subtotal + tax - discount


units = float(input("Enter units: "))

print("Final Bill:", final_bill(units))