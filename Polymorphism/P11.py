class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 30000)
p3 = Product("Tablet", 60000)

print(p1 > p2)
print(p1 == p3)