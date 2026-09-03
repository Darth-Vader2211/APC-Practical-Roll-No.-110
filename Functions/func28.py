def consultation_charges(amount):
    return amount


def laboratory_charges(amount):
    return amount


def medicine_charges(amount):
    return amount


def room_charges(amount):
    return amount


def discount(category, amount):
    if category == "senior":
        return amount * 0.20
    elif category == "regular":
        return amount * 0.05
    else:
        return 0


def final_bill(category, consultation, laboratory, medicine, room):
    total = (consultation_charges(consultation) +
             laboratory_charges(laboratory) +
             medicine_charges(medicine) +
             room_charges(room))

    return total - discount(category, total)


category = input("Enter patient category: ")

consultation = float(input("Consultation charges: "))
laboratory = float(input("Laboratory charges: "))
medicine = float(input("Medicine charges: "))
room = float(input("Room charges: "))

print("Final Bill:", final_bill(
    category, consultation, laboratory, medicine, room
))