class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discount_price(self, discount):
        final_price = self.price - (self.price * discount / 100)
        print("Price after discount:", final_price)


m = MobilePhone("Samsung", "S25", "256GB", 80000)

m.display()
m.discount_price(10)