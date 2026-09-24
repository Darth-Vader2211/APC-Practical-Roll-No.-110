class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def drive(self):
        print(self.brand, self.model, "is driving fast.")


class ElectricBike(Bike):
    def charge(self):
        print(self.brand, self.model, "is charging.")


s = SportsCar("Ferrari", "SF90")
e = ElectricBike("Ola", "S1")

s.drive()
e.charge()